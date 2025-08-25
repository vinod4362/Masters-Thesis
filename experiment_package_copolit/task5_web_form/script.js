document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('regForm');
  const nameEl = document.getElementById('name');
  const emailEl = document.getElementById('email');
  const passwordEl = document.getElementById('password');
  const confirmEl = document.getElementById('confirm');
  const btn = document.getElementById('submitBtn');
  const success = document.getElementById('success');

  function setError(id, msg){ document.getElementById(id).textContent = msg || ''; }
  function validateName(v){ return typeof v === 'string' && v.trim().length >= 2; }
  function validateEmail(v){ return /.+@.+\..+/.test(v); }
  function validatePassword(v){ return /^(?=.*\d).{8,}$/.test(v); }
  function validateConfirm(p, c){ return p === c && c.length > 0; }

  function update(){
    const vn = validateName(nameEl.value);
    const ve = validateEmail(emailEl.value);
    const vp = validatePassword(passwordEl.value);
    const vc = validateConfirm(passwordEl.value, confirmEl.value);

    setError('nameErr', vn ? '' : 'Name must be at least 2 characters');
    setError('emailErr', ve ? '' : 'Invalid email');
    setError('passwordErr', vp ? '' : 'Password min 8 chars & 1 digit');
    setError('confirmErr', vc ? '' : 'Passwords must match');

    btn.disabled = !(vn && ve && vp && vc);
  }

  [nameEl, emailEl, passwordEl, confirmEl].forEach(el => el.addEventListener('input', update));

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if(btn.disabled) return;
    success.style.display = 'block';
    form.reset();
    update();
  });

  update();
});
