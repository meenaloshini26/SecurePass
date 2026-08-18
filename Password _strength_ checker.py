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
