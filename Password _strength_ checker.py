<DOCTYPE! html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>SecurePass - Password Strength Analyzer</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: 'Courier New', monospace;
    background: #0a0e17;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
  }
  .container {
    background: #131a29;
    border: 1px solid #2d3748;
    padding: 36px;
    border-radius: 12px;
    width: 420px;
    box-shadow: 0 0 40px rgba(56, 189, 248, 0.1);
  }
  h1 {
    color: #38bdf8;
    font-size: 20px;
    text-align: center;
    margin-bottom: 4px;
    letter-spacing: 1px;
  }
  .subtitle {
    color: #64748b;
    text-align: center;
    font-size: 12px;
    margin-bottom: 24px;
  }
  .input-row {
    display: flex;
    gap: 8px;
  }
  input {
    flex: 1;
    padding: 12px;
    background: #0a0e17;
    border: 1px solid #2d3748;
    border-radius: 6px;
    color: #e2e8f0;
    font-family: monospace;
    font-size: 14px;
    outline: none;
  }
  input:focus { border-color: #38bdf8; }
  button {
    padding: 12px 14px;
    background: #1e293b;
    border: 1px solid #2d3748;
    border-radius: 6px;
    color: #38bdf8;
    cursor: pointer;
    font-size: 12px;
    white-space: nowrap;
  }
  button:hover { background: #2d3748; }

  .meter {
    display: flex;
    gap: 4px;
    margin-top: 18px;
  }
  .seg {
    height: 6px;
    flex: 1;
    background: #2d3748;
    border-radius: 3px;
    transition: background 0.3s;
  }

  .status-row {
    display: flex;
    justify-content: space-between;
    margin-top: 10px;
    font-size: 13px;
  }
  #status { font-weight: bold; }
  #crackTime { color: #64748b; }

  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px;
    margin-top: 20px;
  }
  .chip {
    font-size: 11px;
    padding: 6px 8px;
    border-radius: 4px;
    background: #1e293b;
    color: #64748b;
    border-left: 3px solid #2d3748;
}
.chip.ok {
    color: #4ade80;
    border-left-color: #4ade80;
  }

  .footer-note {
    margin-top: 20px;
    font-size: 10px;
    color: #475569;
    text-align: center;
  }
</style>
</head>
<body>

<div class="container">
  <h1>&gt; SecurePass_</h1>
  <div class="subtitle">Real-time Password Strength Analyzer</div>

  <div class="input-row">
    <input type="text" id="pwd" placeholder="Type or generate password" oninput="analyze()">
    <button onclick="generatePwd()">Generate</button>
  </div>

  <div class="meter">
    <div class="seg" id="s1"></div>
    <div class="seg" id="s2"></div>
    <div class="seg" id="s3"></div>
    <div class="seg" id="s4"></div>
    <div class="seg" id="s5"></div>
  </div>

  <div class="status-row">
    <span id="status">Awaiting input...</span>
    <span id="crackTime"></span>
  </div>

  <div class="grid">
    <div class="chip" id="c-length">Min 8 characters</div>
    <div class="chip" id="c-upper">Uppercase (A-Z)</div>
    <div class="chip" id="c-lower">Lowercase (a-z)</div>
    <div class="chip" id="c-number">Number (0-9)</div>
    <div class="chip" id="c-special">Symbol (!@#$)</div>
    <div class="chip" id="c-nocommon">Not a common word</div>
  </div>

  <div class="footer-note">No data is stored or transmitted. All checks run locally in your browser.</div>
</div>

<script>
const commonPasswords = ["password","123456","123456789","qwerty","abc123","password1","111111","iloveyou","admin","welcome"];

function analyze() {
  const pwd = document.getElementById('pwd').value;

  const checks = {
    length: pwd.length >= 8,
    upper: /[A-Z]/.test(pwd),
    lower: /[a-z]/.test(pwd),
    number: /[0-9]/.test(pwd),
    special: /[^A-Za-z0-9]/.test(pwd),
    nocommon: pwd.length > 0 && !commonPasswords.includes(pwd.toLowerCase())
  };

  Object.keys(checks).forEach(key => {
    const el = document.getElementById('c-' + key);
    if (el) el.className = 'chip' + (checks[key] ? ' ok' : '');
  });

  const score = Object.values(checks).filter(Boolean).length;
  const segs = [document.getElementById('s1'),document.getElementById('s2'),document.getElementById('s3'),document.getElementById('s4'),document.getElementById('s5')];
  const colors = ['#ef4444','#f97316','#eab308','#22c55e','#4ade80'];

  segs.forEach(s => s.style.background = '#2d3748');

  let statusText = 'Awaiting input...';
  let statusColor = '#64748b';
  let level = 0;

  if (pwd.length > 0) {
    if (score <= 2) { level = 1; statusText = 'WEAK'; statusColor = '#ef4444'; }
    else if (score === 3) { level = 2; statusText = 'FAIR'; statusColor = '#f97316'; }
    else if (score === 4) { level = 3; statusText = 'GOOD'; statusColor = '#eab308'; }
    else if (score === 5) { level = 4; statusText = 'STRONG'; statusColor = '#22c55e'; }
    else if (score === 6) { level = 5; statusText = 'VERY STRONG'; statusColor = '#4ade80'; }
  }

  for (let i = 0; i < level; i++) {
    segs[i].style.background = colors[level-1];
  }

  document.getElementById('status').textContent = statusText;
  document.getElementById('status').style.color = statusColor;
  document.getElementById('crackTime').textContent = pwd.length > 0 ? estimateCrackTime(pwd) : '';
}

function estimateCrackTime(pwd) {
  let poolSize = 0;
  if (/[a-z]/.test(pwd)) poolSize += 26;
  if (/[A-Z]/.test(pwd)) poolSize += 26;
  if (/[0-9]/.test(pwd)) poolSize += 10;
  if (/[^A-Za-z0-9]/.test(pwd)) poolSize += 32;
