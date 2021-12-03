// const elementProject = document.querySelector("#project");
// const elementProjectList =document.querySelector(".project__list")
// const elementHome = document. querySelector("#home");
// elementHome.addEventListener('click',()=>{
//     if(elementHome.classList.contains("nav__menu-item--active")){
//         elementHome.classList.remove("nav__menu-item--active");
//     }else{
//         elementHome.classList.add("nav__menu-item--active");
//     }
// })
// elementProject.addEventListener('click',()=>{
//     if(elementProject.classList.contains("nav__menu-item--active")){
//         elementProject.classList.remove("nav__menu-item--active")
//         elementProjectList.style.display="none";
//     }else{
//         elementProject.classList.add("nav__menu-item--active")
//         elementProjectList.style.display="block";
//     }
// })

// const elementLabel = document.querySelector("#label");
// const elementLabelList =document.querySelector(".label__list")
// elementLabel.addEventListener('click',()=>{
//     if(elementLabel.classList.contains("nav__menu-item--active")){
//         elementLabel.classList.remove("nav__menu-item--active")
//         elementLabelList.style.display="none";
//     }else{
//         elementLabel.classList.add("nav__menu-item--active")
//         elementLabelList.style.display="block";
//     }
// })

var dropdown = document.querySelectorAll(".nav__list-item");
const elementProjectList =document.querySelector(".project__list")
const elementLabelList =document.querySelector(".label__list")
console.log(dropdown)
var i;
// const elementActive = document.querySelector("nav__menu-item--active");

for (i = 0; i < dropdown.length; i++) {
    
    dropdown[i].addEventListener("click", function() {
        

        // for(j=0;j< dropdown.length;j++){
        //     dropdown[j].classList.remove("nav__menu-item--active");
        //     // console.log(dropdown)
        //     // dropdownContent.style.display = "none";
        //     elementLabelList.style.display="none";
        //     elementProjectList.style.display="none";
        // }
        var dropdownContent = this.nextElementSibling;
    this.classList.toggle("nav__menu-item--active");
   
    // console.log(dropdownContent);
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
    } else {
      dropdownContent.style.display = "block";
     
    }
  });
}

function openMyPrio(evt, myprios) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("content-my-prio");
  // console.log(tabcontent)
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks-my-prio");
  for (i = 0; i < tablinks.length; i++) {
    // if(tablinks[i].contains('.active-my-prio')) {
    //     tablinks[i].remove('.active-my-prio')
    // } else {
    //     tablinks[i].add('.active-my-prio')
    // }
    tablinks[i].className = tablinks[i].className.replace("active-my-prio", "");
  }
  document.getElementById(myprios).style.display = "block";
  // e.target.className += "active";
  evt.currentTarget.className += " active-my-prio";
}

