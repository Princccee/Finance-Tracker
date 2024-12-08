document.addEventListener('DOMContentLoaded', function() {
    // SVG Icons
    const icons = {
        user: `<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-6 h-6 text-gray-400">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
              </svg>`,
        mail: `<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-6 h-6 text-gray-400">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
              </svg>`,
        phone: `<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-6 h-6 text-gray-400">
                 <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
               </svg>`,
        lock: `<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-6 h-6 text-gray-400">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
              </svg>`,
        userPlus: `<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-12 h-12 text-blue-600">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z" />
                   </svg>`
    };

    // Icon Insertion Function
    function insertIcons() {
        const iconMappings = {
            'user-icon': icons.userPlus,
            'username-icon': icons.user,
            'email-icon': icons.mail,
            'phone-icon': icons.phone,
            'password-icon': icons.lock,
            'confirm-password-icon': icons.lock
        };

        Object.entries(iconMappings).forEach(([id, icon]) => {
            const element = document.getElementById(id);
            if (element) element.innerHTML = icon;
        });
    }

    // Form Validation Utilities
    const validationUtils = {
        showError: function(input, message) {
            const errorElement = document.getElementById(`${input.id}-error`);
            errorElement.textContent = message;
            errorElement.classList.remove('hidden');
            input.classList.add('border-red-500');
        },
        clearError: function(input) {
            const errorElement = document.getElementById(`${input.id}-error`);
            errorElement.textContent = '';
            errorElement.classList.add('hidden');
            input.classList.remove('border-red-500');
        },
        validators: {
            required: function(value) {
                return value.trim() !== '';
            },
            email: function(value) {
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                return emailRegex.test(value);
            },
            phone: function(value) {
                const phoneRegex = /^\d{10}$/;
                return phoneRegex.test(value);
            },
            minLength: function(value, length) {
                return value.length >= length;
            },
            matchPassword: function(password, confirmPassword) {
                return password === confirmPassword;
            }
        }
    };

    // Form Validation Function
    function validateForm(form) {
        let isValid = true;
        const inputs = form.querySelectorAll('input');

        inputs.forEach(input => {
            // Clear previous errors
            validationUtils.clearError(input);

            // Validation based on input type
            switch(input.id) {
                case 'username':
                    if (!validationUtils.validators.required(input.value)) {
                        validationUtils.showError(input, 'Username is required');
                        isValid = false;
                    }
                    break;
                case 'firstName':
                    if (!validationUtils.validators.required(input.value)) {
                        validationUtils.showError(input, 'First name is required');
                        isValid = false;
                    }
                    break;
                case 'lastName':
                    if (!validationUtils.validators.required(input.value)) {
                        validationUtils.showError(input, 'Last name is required');
                        isValid = false;
                    }
                    break;
                case 'email':
                    if (!validationUtils.validators.required(input.value)) {
                        validationUtils.showError(input, 'Email is required');
                        isValid = false;
                    } else if (!validationUtils.validators.email(input.value)) {
                        validationUtils.showError(input, 'Invalid email format');
                        isValid = false;
                    }
                    break;
                case 'phone':
                    if (!validationUtils.validators.required(input.value)) {
                        validationUtils.showError(input, 'Phone number is required');
                        isValid = false;
                    } else if (!validationUtils.validators.phone(input.value)) {
                        validationUtils.showError(input, 'Phone number must be 10 digits');
                        isValid = false;
                    }
                    break;
                case 'password':
                    if (!validationUtils.validators.required(input.value)) {
                        validationUtils.showError(input, 'Password is required');
                        isValid = false;
                    } else if (!validationUtils.validators.minLength(input.value, 8)) {
                        validationUtils.showError(input, 'Password must be at least 8 characters');
                        isValid = false;
                    }
                    break;
                case 'confirmPassword':
                    const password = document.getElementById('password').value;
                    if (!validationUtils.validators.required(input.value)) {
                        validationUtils.showError(input, 'Please confirm your password');
                        isValid = false;
                    } else if (!validationUtils.validators.matchPassword(password, input.value)) {
                        validationUtils.showError(input, 'Passwords do not match');
                        isValid = false;
                    }
                    break;
            }
        });

        return isValid;
    }

    // Form Submission Handler
    function handleFormSubmit(event) {
        event.preventDefault();
        const form = event.target;

        if (validateForm(form)) {
            // Collect form data
            const formData = new FormData(form);
            const userData = Object.fromEntries(formData.entries());

            // Log user data (replace with actual submission logic)
            console.log('User Registration Data:', userData);

            // Optional: Send data to server
            // fetch('/register', {
            //     method: 'POST',
            //     headers: {
            //         'Content-Type': 'application/json',
            //     },
            //     body: JSON.stringify(userData)
            // })
            // .then(response => response.json())
            // .then(data => {
            //     // Handle successful registration
            //     alert('Registration Successful!');
            // })
            // .catch(error => {
            //     // Handle registration error
            //     console.error('Registration Error:', error);
            // });
        }
    }

    // Initialize Page
    function initPage() {
        insertIcons();
        const registrationForm = document.getElementById('registrationForm');
        registrationForm.addEventListener('submit', handleFormSubmit);
    }

    // Run initialization
    initPage();
});