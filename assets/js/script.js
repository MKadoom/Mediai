// API Base URL
const API_URL = 'http://localhost:8000';

// Login/Signup Logic
document.getElementById('loginForm')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = document.querySelector('#loginForm input[type="email"]').value;
    const password = document.querySelector('#loginForm input[type="password"]').value;
    
    const response = await fetch(`${API_URL}/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password }),
    });

    if (response.ok) {
        window.location.href = 'dashboard.html';
    } else {
        alert('فشل تسجيل الدخول!');
    }
});

// Analyze Skin Image (diagnosis.html)
async function analyzeSkin(imageFile) {
    const formData = new FormData();
    formData.append('image', imageFile);

    const response = await fetch(`${API_URL}/analyze-skin`, {
        method: 'POST',
        body: formData,
    });

    const result = await response.json();
    document.getElementById('result').innerHTML = `
        التشخيص: ${result.diagnosis}<br>
        الثقة: ${result.confidence}%
    `;
}
