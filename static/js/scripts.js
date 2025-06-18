document.addEventListener('DOMContentLoaded', () => {
  renderHighlightPosts();
  renderProducts();
  renderRecentPosts();
});


// === HIGHLIGHTS SECTION ===
const highlightPosts = [
  {
    type: 'main',
    title: 'Title',
    authorDate:{
      author:'Michelle Nhengu',
      date:''
    },
     image: '/static/images/img7.jpeg',
     link:'#'
  },
  {
    type: 'small',
    title: 'Title',
    authorDate:{
      author:'Michelle Nhengu',
      date:''
    },
     image: '/static/images/img7.jpeg',
     link:'#'
  },
  {
    type: 'small',
    title: 'Title',
    authorDate:{
      author:'Michelle Nhengu',
      date:''
    },
     image: '/static/images/img7.jpeg',
     link:'#'
  }
];

function createHighlightPost(type, title,authorDate, image) {
 const post = document.createElement('div');
  post.className = type === 'main' ? 'main-post' : 'small-post';
  post.innerHTML = `
    <img src="${image}" class="highlight-post-img" alt="${title}" />
    <div class="${type === 'main' ? 'overlay-text' : 'small-overlay-text'}">
      <h3>${title}</h3>
      <h5>${authorDate}</h5>
    </div>
  `;
  return post;
}

function renderHighlightPosts() {
  const highlightGrid = document.getElementById('highlight-grid');
  if (!highlightGrid) return;
  highlightPosts.forEach(post => highlightGrid.appendChild(createHighlightPost(post)));
}


// === PRODUCTS SECTION ===
const products = [
  { title: 'Tech Gadget', image: 'images/img13.jpeg' },
  { title: 'Smart Device', image: 'images/img14.jpg' },
  { title: 'AI Assistant', image: 'images/img15.jpg' }
];

function createProductCard({ title, image }) {
  const div = document.createElement('div');
  div.className = 'product-container';
  div.innerHTML = `
    <img src="${image}" alt="${title}" />
    <div style="padding:10px;">
      <h4>${title}</h4>
    </div>
  `;
  return div;
}

function renderProducts() {
  const productsSection = document.getElementById('products-section');
  if (!productsSection) return;
  products.forEach(product => productsSection.appendChild(createProductCard(product)));
}


// === RECENT POSTS SECTION ===
const recentPosts = [
 
    {
        title: "AI Breakthrough",
        author: "Michelle Nhengu",
        date: "2025-06-18",
        description: "Latest in artificial intelligence...",
        image: "/static/images/img9.jpeg",
        link:  "#"
    },
   {
        title: "Cybersecurity Trends",
        author: "Michelle Nhengu",
        date: "2025-06-15",
        description: "Top security practices...",
        image: "/static/images/img10.jpeg",
        link: "#"
    },
    {
        title: "Cybersecurity Trends",
        author: "Michelle Nhengu",
        date: "2025-06-15",
        description: "Top security practices...",
        image: "/static/images/img11.jpeg",
        link: "#"
    },
    {
        title: "Cybersecurity Trends",
        author: "Michelle Nhengu",
        date: "2025-06-15",
        description: "Top security practices...",
        image: "/static/images/img12.jpeg",
        link: "#"
    },
   

];

function createRecentPost({ title, description, image }) {
  const container = document.createElement('div');
  container.className = 'recent-post-container';
  container.innerHTML = `
    <img class="recent-post-img" src="${image}" alt="${title}" />
    <div class="text">
      <h4>${title}</h4>
      <p>${author} - ${date}</p>
      <p>${description}</p>
      <button>Read More</button>
    </div>
  `;
  return container;
}

function renderRecentPosts() {
  const recentPostsSection = document.getElementById('recent-posts-section');
  if (!recentPostsSection) return;
  recentPosts.forEach(post => recentPostsSection.appendChild(createRecentPost(post)));
}

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