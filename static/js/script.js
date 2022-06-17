toggler=document.querySelector("#toggler");
image_svg=document.querySelector("#image_svg");
image_text=document.querySelector(".text_user");
toggler.addEventListener('click',change_svg);
flag=0;
function change_svg(){
    if(flag==1){
        image_svg.src="static/svg/todo1.svg";
        image_text.style.color="#FFF";
        flag=0;
    }
    else {
        image_svg.src="static/svg/todo2.svg";
        image_text.style.color="#ffc85c";
        flag=1;
    }
}
