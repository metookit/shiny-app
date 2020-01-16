//Night Mode
const checkbox = document.querySelector('input[name=theme]');

checkbox.addEventListener('change', function() {
    if(this.checked) {
        trans()
        document.documentElement.setAttribute('data-theme', 'dark')
    }
    else{
        trans()
        document.documentElement.setAttribute('data-theme', 'light')
    }
})

window.addEventListener('unload', function() {

  if(checkbox.checked){
    localStorage.setItem('currentTheme', 'dark');
  }
  else{
    localStorage.setItem('currentTheme', 'light');
  }
})

window.addEventListener('load', function() {
    var curTheme = this.localStorage.getItem('currentTheme');
    if(curTheme == 'dark'){
      document.documentElement.setAttribute('data-theme', 'dark')
      this.document.getElementById("checkboxSwitch").checked = true;
    }
    else{
      document.documentElement.setAttribute('data-theme', 'light')
    }
})
let trans = () => {
    document.documentElement.classList.add('transition');
    window.setTimeout(() => {
        document.documentElement.classList.remove('transition');
    }, 1000)
};

//Modal
var modal = document.querySelector("[data-modal]");
var line = document.querySelector("[data-line]");

var span = document.getElementsByClassName("modal__close")[0];

line.onclick = function() {
  modal.style.display = "block";
}

span.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
} 