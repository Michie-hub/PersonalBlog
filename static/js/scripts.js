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
    //highlight toggle
   document.addEventListener("DOMContentLoaded", function () {
  const categorySelect = document.getElementById("category-select");
  const highlightOptions = document.getElementById("highlight-options");

  categorySelect.addEventListener("change", function () {
    if (categorySelect.value === "highlight") {
      highlightOptions.style.display = "block";
    } else {
      highlightOptions.style.display = "none";
      // Optional: uncheck radios if not highlight
      document.querySelectorAll('input[name="highlight_type"]').forEach(r => r.checked = false);
    }
  });
});


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
        document.querySelectorAll('.recent-post-container').forEach(container => {
          const btn = container.querySelector('button');
          const desc = container.querySelectorAll('p')[1];
          if (btn && desc) {
            const fullText = desc.textContent;
            const shortText = fullText.slice(0, 80) + '...';
            desc.textContent = shortText;
      
            btn.addEventListener('click', () => {
              if (desc.textContent === shortText) {
                desc.textContent = fullText;
                btn.textContent = 'Show Less';
              } else {
                desc.textContent = shortText;
                btn.textContent = 'Read More';
              }
            });
          }
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
console.log("js is working");