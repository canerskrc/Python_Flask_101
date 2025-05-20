// Add active class to current nav item
document.addEventListener('DOMContentLoaded', function() {
    const currentLocation = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (currentLocation === href || (href !== '/' && currentLocation.startsWith(href))) {
            link.classList.add('active');
        }
    });
}); 