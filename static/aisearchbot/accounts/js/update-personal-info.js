

function togglePasswordField(event, icon) {
    let passwordField = icon.closest('.password-input-div').querySelector('input[data-type="password"]');

    if (icon.classList.contains('hide-password-icon') && passwordField.type == 'password') {
        passwordField.type = 'text';
        icon.classList.add('hide');
        console.log(icon.closest('.password-input-div').querySelector('.show-password-icon'));
        icon.closest('.password-input-div').querySelector('.show-password-icon').classList.remove('hide');
    }
    else if (icon.classList.contains('show-password-icon') && passwordField.type == 'text') {
        passwordField.type = 'password';
        icon.classList.add('hide');
        icon.closest('.password-input-div').querySelector('.hide-password-icon').classList.remove('hide');
    }
}

function previewImage(event, inputElement) {
    let image = event.currentTarget.files;
    let imageTag = document.getElementById('profile-image');
    imageTag.src = window.URL.createObjectURL(image[0]);
}

function preventSubmission(event) {
    event.preventDefault(); 
    location.pathname = '/aisearchbot/account/'
}
function formDataToObject(formData) {
    let getData = {}
    formData.forEach(function(value, key) {
        getData[key] = value;
    });
    return getData
}

// const phoneRegex = /^\+[0-9]{10,}$/;
// const emailRegex = /[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}/i



let error_message = document.querySelector('.create-error-msg');
let first_name = document.getElementById('first_name_errors')
let last_name = document.getElementById('last_name_errors')
let phone__number = document.getElementById('phone_number_errors')
let email = document.getElementById('email_errors')

function updatepersonalInfoForm(event) {
    event.preventDefault()
    let form = event.currentTarget;
    let formData = new FormData(form);
    let data = formDataToObject(formData);
    let isValid = true
    if (data.first_name.trim().length == 0) {
        first_name.innerText = 'This field is required';
        isValid = false
    }
    else
        first_name.innerText = '';
    if (data.last_name.trim().length == 0) {
        last_name.innerText = 'This field is required';
        isValid = false
    }
    else
        last_name.innerText = ''
    if (phoneRegex.test(data.phone_number) == false) {
        phone__number.innerText = 'Please enter a valid number with country code';
        isValid = false
    }
    else
        phone__number.innerText = ''
    if (emailRegex.test(data.email) == false) {
        email.innerText = 'Enter valid email';
        isValid = false
    }
    else
        email.innerText = ''
    if(!isValid)
        return false
    form.submit();
}