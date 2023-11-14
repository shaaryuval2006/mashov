function enter_masseges(){
    window.location="masseges.html";
}
function hours_system(){
    window.location="hours_system.html";
}

function grades(){
    window.location="select_grades_type.html";
}

function myFunction() {
    var x = document.getElementById("myDIV");
    x.classList.toggle("slide-animation"); // Toggle the animation class
    x.style.display = x.classList.contains("slide-animation") ? "block" : "none"; // Toggle display
}

function back(){
    window.location = "entry_page.html";
}

function behavior(){
    window.location = "behavior.html";
}

function toggleAdditionalButtons() {
    const additionalButtons = document.getElementById('additional-buttons');

    if (additionalButtons.style.display === 'none' || additionalButtons.style.display === '') {
        additionalButtons.style.display = 'block';
    } else {
        additionalButtons.style.display = 'none';
    }
}

function back_to_home_page(){
    window.location="home_page.html";
}



async function move(){
    console.log("start");
    const t_id = document.getElementById("pass").value; // Get the value of the password input
    console.log("hello");
    let p_id = await eel.move_id(t_id)();
    console.log(p_id);
    if(p_id==true){
        window.location="home_page.html";
        console.log("yuval");
    }
    else{
        window.location="entry_page.html";
        console.log("tomer is fat");
    }
}

function clicked_student(){
    window.location="grades_page.html";
}

function new_massege(){
    window.location="send_massege.html";
}



function startLoading() {
    const button = document.querySelector('.cool-button');
    const loading = document.querySelector('.loading');
    const checkmark = document.querySelector('.checkmark');

    button.style.display = 'none';
    loading.style.display = 'inline-block';

    setTimeout(function () {
        loading.style.display = 'none';
        checkmark.style.display = 'inline-block';
    }, 700); // Simulating a 2-second loading time
}
