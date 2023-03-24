// Scripts for index Page i.e index.html goes here Please...

  // Dropdown
  const dropDownLink = document.getElementById('dropdown-link');
  const dropDownMenu = document.getElementById('dropdown-menu');

  dropDownLink.addEventListener("click", () => {
    if (!dropDownMenu.classList.contains("dropdown-active")) {
        dropDownMenu.classList.add("dropdown-active");
    } 
    else {
        dropDownMenu.classList.remove("dropdown-active");
    }
  })