function openLoginModal() {
    const loginUrl = "{% url 'login' %}"; // Django will render this into the actual URL
    window.location.href = loginUrl;
// document.getElementById('loginModal').classList.remove('hidden');
}

function closeLoginModal() {
document.getElementById('loginModal').classList.add('hidden');
}

document.getElementById('loginModal').addEventListener('click', function(event) {
if (event.target === this) {
    closeLoginModal();
}
});

document.getElementById('loginForm').addEventListener('submit', function(event) {
event.preventDefault();
// Add login logic here
alert('Login functionality to be implemented');
closeLoginModal();
});

function startSignup() {
// Placeholder for signup process
alert('Signup functionality to be implemented');
}

// const dropdownTrigger = document.querySelector('.dropdown-trigger');
// const dropdownMenu = document.querySelector('.dropdown-menu');
// const userAccountDropdown = document.querySelector('.user-account-dropdown');

// dropdownTrigger.addEventListener('click', () => {
//   userAccountDropdown.classList.toggle('open');
// });

// document.addEventListener('click', (event) => {
//   if (!userAccountDropdown.contains(event.target)) {
//     userAccountDropdown.classList.remove('open');
//   }
// });


document.addEventListener('DOMContentLoaded', () => {
    // Select the dropdown toggle and menu elements
    const dropdownToggle = document.getElementById('dropdown-toggle');
    const dropdownMenu = document.getElementById('dropdown-menu');

    // Add click event listener to the dropdown toggle
    dropdownToggle.addEventListener('click', (event) => {
        event.stopPropagation(); // Prevent event from propagating to the document
        dropdownMenu.classList.toggle('active'); // Toggle the active class
    });

    // Close the dropdown if the user clicks outside of it
    document.addEventListener('click', () => {
        if (dropdownMenu.classList.contains('active')) {
            dropdownMenu.classList.remove('active');
        }
    });
});