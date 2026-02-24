document.addEventListener('DOMContentLoaded', () => {
    const glow = document.querySelector('.glow-capture');
    
    // Suivi de souris pour l'effet de lumière en fond
    window.addEventListener('mousemove', (e) => {
        const x = e.clientX;
        const y = e.clientY;
        glow.style.background = `radial-gradient(600px circle at ${x}px ${y}px, rgba(79, 97, 77, 0.15), transparent 80%)`;
    });

    // Animation au scroll simplifiée
    const cards = document.querySelectorAll('.glass');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.1 });

    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = 'all 0.6s ease-out';
        observer.observe(card);
    });
});