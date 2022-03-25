from flask import Flask
from flask import send_file
from PIL import ImageGrab
# the StringIO and BytesIO are used to make file like object
from io import StringIO, BytesIO
from flask import request
import sys

if sys.platform != "linux":
    import ctypes
    user32 = ctypes.windll.user32  # the user32.dll reference
    MOUSEEVENT_LEFTDOWN = 2
    MOUSEEVENT_LEFTUP = 4

app = Flask(__name__)

# html_file = open('static/index.html', 'w+')
# html_file.write('''
# <!DOCTYPE html>
# <html>
# <head>
# <meta charset-"UTF-8">
# <title>Remote Desktop</title>
# </head>
# <body>
# <script scr= "//code.jquery.com/jquery-1.11.1.js"></script>
# <script>
# alert('hello');
#
# </script>
#
# </body>
# </html>
#
#
# ''')
# html_file.close()


@app.route('/click')
def click():
    try:
        x = int(request.args.get('x'))
        y = int(request.args.get('y'))
        print(f"(x,y) >> ({x},{y})")
    except TypeError:
        return 'error: expecting 2 ints, x and y'
    # the following code can be replaced with the module pynput
    if sys.platform != "linux":
        user32.SetCursorPos(x, y)
        user32.mouse_event(MOUSEEVENT_LEFTDOWN, 0, 0, 0, 0)
        user32.mouse_event(MOUSEEVENT_LEFTUP, 0, 0, 0, 0)
    return 'done\a'


# the path
@app.route('/desktop.jpeg')
def desktop():
    # taking screenshot
    screen = ImageGrab.grab(bbox=None)
    # to make a virtual file so it won't be saved in hard disk
    buf = BytesIO()
    # to save the image withe the required extension and quality
    screen.save(buf, 'JPEG', quality=75)
    # seek(0) is used to rewind the StrinIO instance otherwise it will be a the end of data stream
    buf.seek(0)
    return send_file(buf, mimetype='image/jpeg')
    # of send_file(filename=buf, mimetype='image/jpeg')


# 127.0.0.1:7080/host can differ due to 0.0.0.0 in app.run()
# but the port must be as in app.run()
@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == "__main__":
    app.run("0.0.0.0", 7080)
    # or app.run(host="0.0.0.0", port=7080, debug=None)
