document.addEventListener("DOMContentLoaded", () => {
  const accountMenu = document.querySelector(".account-menu");

  accountMenu.addEventListener("click",  (e) => {
    e.stopPropagation(); //prevents click from bubbling
    accountMenu.classList.toggle("show-dropdown");
  });

  document.addEventListener("click", () => {
    accountMenu.classList.remove("show-dropdown");
  });
});

 function scrollLeft() {
            document.getElementById('scrollBar').scrollBy({ left: -200, behavior: 'smooth' });
        }

        function scrollRight() {
            document.getElementById('scrollBar').scrollBy({ left: 200, behavior: 'smooth' });
        }
 
        // 1. Email subscription validation
        document.querySelector('.cta-button').addEventListener('click', function () {
          const email = document.querySelector('.input-box').value;
          const pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
          if (!pattern.test(email)) {
            alert('Please enter a valid email address.');
          } else {
            console.log('Subscribed:', email);
            alert('Thank you for subscribing!');
            // You can use fetch() here to send to backend
          }
        });
      
        // 2. Mobile menu toggle (requires menu container in HTML)
        const menuIcon = document.querySelector('.menu-nav img');
        const navLinks = document.querySelector('.quick-links'); // example
        if (menuIcon && navLinks) {
          menuIcon.addEventListener('click', () => {
            navLinks.classList.toggle('show');
          });
        }
      
        // 3. Ad banner visibility (optional if dynamically loaded)
        const adBanner = document.getElementById('ad-banner');
        if (adBanner && adBanner.offsetHeight === 0) {
          adBanner.style.display = 'none';
        }
      
        // 4. Dynamic date injection (replace "author-date")
        document.querySelectorAll('p').forEach(p => {
          if (p.textContent.includes('author-date')) {
            const today = new Date();
            const formatted = `${today.toLocaleDateString('en-GB')}`;
            p.textContent = `Author - ${formatted}`;
          }
        });
      
        // 5. Expandable 'Read More' buttons
       
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.recent-post-container').forEach(container => {
    const btn = container.querySelector('button');
    const desc = container.querySelector('.text p'); // Get the only <p> inside .text

    if (btn && desc) {
      const fullText = desc.textContent.trim();
      const shortText = fullText.length > 80 ? fullText.slice(0, 80) + '...' : fullText;
      let isShort = true;

      if (fullText.length > 70) {
        desc.textContent = shortText;

        btn.addEventListener('click', () => {
          desc.textContent = isShort ? fullText : shortText;
          btn.textContent = isShort ? 'Show Less' : 'Read More';
          isShort = !isShort;
        });
      } else {
        btn.style.display = 'none'; // Hide button if text is already short
      }
    }
  });
});


        document.addEventListener('DOMContentLoaded', function () {
  const menuToggle = document.getElementById('menu-toggle');
  const menuList = document.getElementById('menu-list');

  menuToggle.addEventListener('click', function (event) {
    event.stopPropagation(); // Prevent click from bubbling
    menuList.classList.toggle('show');
  });

  // Prevent closing the menu if you click inside it
  menuList.addEventListener('click', function (event) {
    event.stopPropagation();
  });

  // Close menu if clicking anywhere else
  document.addEventListener('click', function () {
    menuList.classList.remove('show');
  });
});


const carousel = document.getElementById("eventCarousel");
const dots = document.querySelectorAll(".dot");

carousel.addEventListener("scroll", () => {
  const scrollLeft = carousel.scrollLeft;
  const width = carousel.clientWidth;

  const index = Math.round(scrollLeft / width);
  dots.forEach(dot => dot.classList.remove("active"));
  if (dots[index]) dots[index].classList.add("active");
});

// Optional: click dot to scroll to card
dots.forEach((dot, index) => {
  dot.addEventListener("click", () => {
    carousel.scrollTo({
      left: carousel.clientWidth * index,
      behavior: "smooth"
    });
  });
});



console.log("js is working");