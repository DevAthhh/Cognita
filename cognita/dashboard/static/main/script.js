document.addEventListener('keydown', function(event) {
  if (event.repeat === false) {
    if (event.ctrlKey) {
      event.preventDefault();
    }
  }
});