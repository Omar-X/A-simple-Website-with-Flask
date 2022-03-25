// http://localhost:63342/learning_html_css/index.html?_ij_reload

console.log("hello world")
let ip = location.host
console.log("your ip: ")
let h2text = document.getElementById("total_number")
console.log(h2text.textContent)
function increment (){
    console.log("button has been pressed")
    h2text.innerText ++

}
