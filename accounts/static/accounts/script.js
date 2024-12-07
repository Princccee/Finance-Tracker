// script.js
const loginForm = document.getElementById('login-form');
const forgotPasswordLink = document.getElementById('forgot-password');
const signUpLink = document.getElementById('sign-up-link');

loginForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  // Perform login logic here
  console.log('Logging in with email:', email, 'and password:', password);
});

forgotPasswordLink.addEventListener('click', () => {
  // Implement forgot password functionality here
  console.log('Forgot password clicked');
});

signUpLink.addEventListener('click', () => {
  // Redirect to sign up page
  console.log('Sign up link clicked');
});