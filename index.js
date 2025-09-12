/* scripts.js - Detaylı JavaScript */

document.addEventListener('DOMContentLoaded', () => {
  // Değişken Tanımlamaları
  const header = document.getElementById('header');
  const mobileMenuButton = document.getElementById('mobile-menu-button');
  const mobileMenu = document.getElementById('mobile-menu');
  const navLinks = document.querySelectorAll('nav.desktop a');
  const filterButtons = document.querySelectorAll('#course-filters .filter-btn');
  const courseCards = document.querySelectorAll('#course-grid .course-card');
  const contactForm = document.getElementById('contact-form');
  const formStatus = document.getElementById('form-status');

  /**
   * Header Scroll Değişimi
   * Sayfa kaydırıldıkça header'a arka plan ve gölge ekler.
   */
  function handleScroll() {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  }
  window.addEventListener('scroll', handleScroll);
  handleScroll(); // Başlangıç durumu

  /**
   * Mobil Menü Toggle
   * Butona tıklandığında mobil menüyü göster/gizle.
   */
  mobileMenuButton.addEventListener('click', () => {
    mobileMenu.classList.toggle('show');
  });

  /**
   * Smooth Scroll
   * Menü linklerine tıklandığında yumuşak kaydırma sağlar.
   */
  navLinks.forEach(link => {
    link.addEventListener('click', e => {
      e.preventDefault();
      const targetId = link.getAttribute('href');
      const targetEl = document.querySelector(targetId);
      if (targetEl) {
        window.scrollTo({
          top: targetEl.offsetTop - header.offsetHeight,
          behavior: 'smooth'
        });
      }
      // Mobil menüyü kapat
      if (mobileMenu.classList.contains('show')) {
        mobileMenu.classList.remove('show');
      }
    });
  });

  /**
   * Görünürlük Tetikleyici (Scroll Animations)
   * IntersectionObserver kullanarak elementleri görünür hale getirir.
   */
  const observerOptions = { threshold: 0.1 };
  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        obs.unobserve(entry.target);
      }
    });
  }, observerOptions);

  document.querySelectorAll('.animate-on-scroll').forEach(el => {
    observer.observe(el);
  });

  /**
   * Kurs Filtreleme
   * Yaş grubu butonlarına göre kurs kartlarını göster/gizle.
   */
  filterButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const filter = btn.getAttribute('data-filter');

      // Aktif buton stilini güncelle
      filterButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      // Kartları göster/gizle
      courseCards.forEach(card => {
        const category = card.getAttribute('data-category');
        if (filter === 'all' || filter === category) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });

  /**
   * İletişim Formu Gönderimi
   * Gerçek backend yoksa simülasyon ile yanıt gösterir.
   */
  if (contactForm) {
    contactForm.addEventListener('submit', e => {
      e.preventDefault();
      formStatus.textContent = 'Mesajınız gönderiliyor...';
      formStatus.style.color = 'var(--color-light-blue)';

      setTimeout(() => {
        formStatus.textContent = 'Mesajınız başarıyla gönderildi! Teşekkür ederiz.';
        formStatus.style.color = 'var(--color-green)';
        contactForm.reset();
      }, 1500);
    });
  }
});
