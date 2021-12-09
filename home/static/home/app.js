function carosel() {
  let hero1 = document.querySelector(".hero1");
  let hero2 = document.querySelector(".hero2");
  let hero3 = document.querySelector(".hero3");

  let state = 1;

  window.addEventListener("DOMContentLoaded", e => {
      if(state == 1) {
        console.log("Test")
        gsap.to(hero2, {duration: 3, opacity: 1, ease: "Power2.easeOut"});
        gsap.to(hero1, {duration: 3, opacity: 0, ease: "Power2.easeOut"});

        // state = 2;
      }

      if(state == 2) {
        gsap.to(hero3, {duration: 3, opacity: 1, ease: "Power2.easeOut"});
        gsap.to(hero2, {duration: 3, opacity: 0, ease: "Power2.easeOut"});

        // state = 3
      };

      if(state == 3) {
        gsap.to(hero1, {duration: 3, opacity: 1, ease: "Power2.easeOut"});
        gsap.to(hero3, {duration: 3, opacity: 0, ease: "Power2.easeOut"});

        // state = 1
      }
  })
}

// carosel()