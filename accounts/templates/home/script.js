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