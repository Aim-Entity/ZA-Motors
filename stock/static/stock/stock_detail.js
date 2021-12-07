function tabs() {
  let description_tab = document.querySelector(".description-tab");
  let detail_tab = document.querySelector(".detail-tab");

  let description = document.querySelector(".description-cont")
  let detail = document.querySelector(".detail-cont")

  let state = 0;

  description_tab.addEventListener("click", e => {
    if(state == 1) {
      console.log("Pass")
      description.classList.toggle("active-cont");
      detail.classList.toggle("active-cont");

      description_tab.classList.toggle("active-tab");
      detail_tab.classList.toggle("active-tab");

      state = 0;
    }
  });

  detail_tab.addEventListener("click", e => {
    if(state == 0) {
      description.classList.toggle("active-cont");
      detail.classList.toggle("active-cont");

      description_tab.classList.toggle("active-tab");
      detail_tab.classList.toggle("active-tab");

      state = 1;
    }
  });
}

function gallery() {
  let active = document.querySelector(".active-cover");

  let image1 = document.querySelectorAll(".cover")[0];
  let image2 = document.querySelectorAll(".cover")[1];
  let image3 = document.querySelectorAll(".cover")[2];
  let image4 = document.querySelectorAll(".cover")[3];
  let image5 = document.querySelectorAll(".cover")[4];
  let image6 = document.querySelectorAll(".cover")[5];

  let image1_tab = document.querySelectorAll(".cover-option")[0];
  let image2_tab = document.querySelectorAll(".cover-option")[1];
  let image3_tab = document.querySelectorAll(".cover-option")[2];
  let image4_tab = document.querySelectorAll(".cover-option")[3];
  let image5_tab = document.querySelectorAll(".cover-option")[4];
  let image6_tab = document.querySelectorAll(".cover-option")[5];

  image1_tab.addEventListener("click", e => {
    active.classList.toggle("active-cover");
    image1.classList.toggle("active-cover");

    active = image1;
  });

  image2_tab.addEventListener("click", e => {
    active.classList.toggle("active-cover");
    image2.classList.toggle("active-cover");

    active = image2;
  });

  image3_tab.addEventListener("click", e => {
    active.classList.toggle("active-cover");
    image3.classList.toggle("active-cover");

    active = image3;
  });

  image4_tab.addEventListener("click", e => {
    active.classList.toggle("active-cover");
    image4.classList.toggle("active-cover");

    active = image4;
  });

  image5_tab.addEventListener("click", e => {
    active.classList.toggle("active-cover");
    image5.classList.toggle("active-cover");

    active = image5;
  });

  image6_tab.addEventListener("click", e => {
    active.classList.toggle("active-cover");
    image6.classList.toggle("active-cover");

    active = image6;
  });
}

tabs()
gallery()