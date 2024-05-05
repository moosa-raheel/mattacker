const passwordField = document.querySelector(".password input")
const openEye = document.querySelector(".close.eye")
passwordField.addEventListener("input",(e)=>{
    let val = e.target.value
    val.length>=1?openEye.classList.remove("none"):openEye.classList.add("none")
})

const eyes = document.querySelectorAll(".eye")
eyes.forEach((eye)=>{
    eye.addEventListener("click",()=>{
        eyes.forEach((ey)=>{
            ey.classList.toggle("none")
        })
        if(passwordField.type=="password"){
            passwordField.type='text'
        }else{
            passwordField.type='password'
        }
    })
})