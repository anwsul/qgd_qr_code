const button = document.querySelector("button");
button.addEventListener('click', changeButtonColor);

function changeButtonColor () {
  button.style.backgroundColor = "rgb(167, 167, 205)";
  setTimeout(() => {
    button.style.backgroundColor = "rgb(105, 105, 159)";
  }, 300);
}