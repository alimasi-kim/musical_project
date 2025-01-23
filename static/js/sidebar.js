document.addEventListener('DOMContentLoaded', function() {
    const sidebar = document.getElementById('sidebar');
    const sidebarToggle = document.getElementById('sidebarToggle');
    const mainContent = document.querySelector('.main-content');

    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', function() {
            sidebar.classList.toggle('show');
        });
    }

    // Fermer le sidebar en cliquant en dehors
    document.addEventListener('click', function(event) {
        const isClickInside = sidebar.contains(event.target) || 
                            sidebarToggle.contains(event.target);

        if (!isClickInside && sidebar.classList.contains('show')) {
            sidebar.classList.remove('show');
        }
    });

    // Gérer la largeur du contenu principal
    function adjustMainContent() {
        if (window.innerWidth > 991.98) {
            mainContent.style.marginLeft = '280px';
        } else {
            mainContent.style.marginLeft = '0';
        }
    }

    window.addEventListener('resize', adjustMainContent);
    adjustMainContent();

    // Animation des sous-menus
    const dropdowns = document.querySelectorAll('.dropdown-toggle');
    dropdowns.forEach(dropdown => {
        dropdown.addEventListener('click', function(e) {
            e.preventDefault();
            const submenu = this.nextElementSibling;
            const icon = this.querySelector('.dropdown-icon');
            
            // Toggle aria-expanded
            const isExpanded = this.getAttribute('aria-expanded') === 'true';
            this.setAttribute('aria-expanded', !isExpanded);
            
            // Animer le submenu
            submenu.classList.toggle('show');
            
            // Animer les éléments du submenu
            const items = submenu.querySelectorAll('li');
            items.forEach((item, index) => {
                setTimeout(() => {
                    item.style.transitionDelay = `${index * 50}ms`;
                }, 0);
            });
        });
    });

    // Effet de ripple sur les liens
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const ripple = document.createElement('div');
            ripple.classList.add('ripple');
            
            const rect = this.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            ripple.style.left = `${x}px`;
            ripple.style.top = `${y}px`;
            
            this.appendChild(ripple);
            
            setTimeout(() => ripple.remove(), 1000);
        });
    });

    // Animation du badge LIVE
    const liveBadge = document.querySelector('.nav-badge.live');
    if (liveBadge) {
        setInterval(() => {
            liveBadge.classList.add('pulse');
            setTimeout(() => liveBadge.classList.remove('pulse'), 1000);
        }, 2000);
    }
}); 