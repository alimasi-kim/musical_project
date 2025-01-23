// Animations au scroll
const animateOnScroll = () => {
    const elements = document.querySelectorAll('.animate-on-scroll');
    
    elements.forEach(element => {
        const elementTop = element.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;
        
        if (elementTop < windowHeight - 100) {
            element.classList.add('animate');
        }
    });
};

// Animation des statistiques
function animateStats() {
    const stats = document.querySelectorAll('.stat-number');
    
    stats.forEach(stat => {
        const value = parseInt(stat.getAttribute('data-value')) || 0;
        const duration = 2000;
        const increment = value / (duration / 16);
        let current = 0;
        
        const updateCounter = () => {
            if (current < value) {
                current += increment;
                stat.textContent = Math.floor(current) + '+';
                requestAnimationFrame(updateCounter);
            } else {
                stat.textContent = value + '+';
            }
        };
        
        updateCounter();
    });
}

// Parallax effect
const parallax = () => {
    const elements = document.querySelectorAll('.parallax');
    
    elements.forEach(element => {
        const speed = element.getAttribute('data-speed') || 0.5;
        const yPos = -(window.pageYOffset * speed);
        element.style.transform = `translateY(${yPos}px)`;
    });
};

// Initialisation
document.addEventListener('DOMContentLoaded', () => {
    // Smooth scroll
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Observer pour déclencher l'animation
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateStats();
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });
    
    document.querySelector('.stats-section')?.forEach(section => {
        observer.observe(section);
    });
    
    // Event listeners
    window.addEventListener('scroll', () => {
        requestAnimationFrame(() => {
            animateOnScroll();
            parallax();
        });
    });

    // Navbar Scroll Effect
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(18, 18, 18, 0.98)';
            navbar.style.padding = '0.5rem 0';
        } else {
            navbar.style.background = 'rgba(18, 18, 18, 0.95)';
            navbar.style.padding = '1rem 0';
        }
    });

    // Gestion du menu mobile
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');

    if (navbarToggler && navbarCollapse) {
        navbarToggler.addEventListener('click', function() {
            navbarCollapse.classList.toggle('show');
        });

        // Fermer le menu mobile lors du clic sur un lien
        document.querySelectorAll('.navbar-nav .nav-link').forEach(link => {
            link.addEventListener('click', function() {
                if (navbarCollapse.classList.contains('show')) {
                    navbarToggler.click();
                }
            });
        });
    }

    // Gestion du formulaire Newsletter
    const newsletterForm = document.querySelector('.newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const emailInput = this.querySelector('input[type="email"]');
            const email = emailInput.value;

            // Animation de chargement
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
            submitBtn.disabled = true;

            // Simuler l'envoi (à remplacer par votre logique d'API)
            setTimeout(() => {
                submitBtn.innerHTML = '<i class="fas fa-check"></i> Merci !';
                emailInput.value = '';
                
                // Réinitialiser après 3 secondes
                setTimeout(() => {
                    submitBtn.innerHTML = originalText;
                    submitBtn.disabled = false;
                }, 3000);
            }, 1500);
        });
    }

    // Lazy loading des images
    document.querySelectorAll('img[data-src]').forEach(img => {
        img.setAttribute('src', img.getAttribute('data-src'));
        img.onload = function() {
            img.removeAttribute('data-src');
        };
    });

    // Gestion du sidebar mobile
    const sidebar = document.querySelector('.sidebar');
    const sidebarOpen = document.querySelector('.sidebar-open');
    const sidebarToggle = document.querySelector('.sidebar-toggle');

    if (sidebarOpen) {
        sidebarOpen.addEventListener('click', function() {
            sidebar.classList.add('show');
        });
    }

    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', function() {
            sidebar.classList.remove('show');
        });
    }

    // Fermer le sidebar au clic sur un lien (mobile)
    document.querySelectorAll('.sidebar-nav a').forEach(link => {
        link.addEventListener('click', function() {
            if (window.innerWidth < 992) {
                sidebar.classList.remove('show');
            }
        });
    });

    // Gestion du sidebar collapse
    const toggleBtn = document.querySelector('.sidebar-toggle-btn');
    const mainContent = document.querySelector('.main-content');
    
    // Récupérer l'état du sidebar depuis le localStorage
    const sidebarState = localStorage.getItem('sidebarCollapsed');
    if (sidebarState === 'true') {
        sidebar.classList.add('collapsed');
    }

    if (toggleBtn) {
        toggleBtn.addEventListener('click', function() {
            sidebar.classList.toggle('collapsed');
            // Sauvegarder l'état dans le localStorage
            localStorage.setItem('sidebarCollapsed', sidebar.classList.contains('collapsed'));
        });
    }

    // Double-clic sur le sidebar pour le collapse/expand
    sidebar.addEventListener('dblclick', function(e) {
        if (window.innerWidth >= 992) { // Seulement sur desktop
            sidebar.classList.toggle('collapsed');
            localStorage.setItem('sidebarCollapsed', sidebar.classList.contains('collapsed'));
        }
    });
});

// Preloader
window.addEventListener('load', function() {
    const preloader = document.querySelector('.preloader');
    if (preloader) {
        preloader.classList.add('preloader-finish');
    }
}); 