// script.js

// Wait for the DOM to fully load
document.addEventListener("DOMContentLoaded", function() {
    // Filter portfolio items
    const filterButtons = document.querySelectorAll(".filter-btn");
    const portfolioItems = document.querySelectorAll(".portfolio-item");
  
    filterButtons.forEach(button => {
      button.addEventListener("click", function() {
        const category = this.getAttribute("data-category");
  
        // Remove active class from all buttons
        filterButtons.forEach(btn => btn.classList.remove("active"));
        // Add active class to the clicked button
        this.classList.add("active");
  
        // Show or hide portfolio items based on the selected category
        portfolioItems.forEach(item => {
          if (category === "all" || item.getAttribute("data-category") === category) {
            item.style.display = "block";
          } else {
            item.style.display = "none";
          }
        });
      });
    });
  
    // Video modal functionality
    const modal = document.getElementById("video-modal");
    const modalVideo = document.getElementById("modal-video");
    const closeModal = document.querySelector(".close-modal");
    
    // Function to open video in modal
    portfolioItems.forEach(item => {
      const link = item.querySelector(".overlay a");
      link.addEventListener("click", function(event) {
        event.preventDefault(); // Prevent default anchor behavior
        const videoSrc = this.getAttribute("href");
        modalVideo.src = videoSrc;
        modal.style.display = "block"; // Show the modal
      });
    });
  
    // Close modal
    closeModal.addEventListener("click", function() {
      modal.style.display = "none"; // Hide the modal
      modalVideo.src = ""; // Reset video source to stop playback
    });
  
    // Close modal when clicking outside of it
    window.addEventListener("click", function(event) {
      if (event.target === modal) {
        modal.style.display = "none"; // Hide the modal
        modalVideo.src = ""; // Reset video source to stop playback
      }
    });
  });
  