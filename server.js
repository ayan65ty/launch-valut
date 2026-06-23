const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const CREATOR_PASSCODE = "9999";
const VIP_PASSCODE = "LAUNCH2026"; 

const htmlPage = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Launch & Secure Vault</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', sans-serif; }
        body { background: #0b0f19; color: #f3f4f6; display: flex; justify-content: center; align-items: center; min-height: 100vh; padding: 20px; }
        .container { background: #111827; border: 1px solid #1f2937; border-radius: 12px; width: 100%; max-width: 500px; padding: 30px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); text-align: center; }
        .badge { background: #2563eb; color: white; text-transform: uppercase; font-size: 11px; font-weight: bold; padding: 4px 10px; border-radius: 20px; display: inline-block; margin-bottom: 15px; letter-spacing: 1px; }
        h1 { font-size: 28px; margin-bottom: 10px; font-weight: 700; color: #ffffff; }
        p.subtitle { color: #9ca3af; font-size: 15px; margin-bottom: 25px; line-height: 1.5; }
        .status-box { background: #1f2937; border-left: 4px solid #9ca3af; padding: 12px; border-radius: 6px; font-size: 14px; color: #d1d5db; margin-bottom: 25px; text-align: left; }
        .status-box.secure { border-left-color: #10b981; background: rgba(16, 185, 129, 0.1); color: #10b981; }
        .screen { display: none; }
        .active { display: block; }
        .btn { background: #2563eb; color: white; border: none; width: 100%; padding: 14px; font-size: 16px; font-weight: 600; border-radius: 8px; cursor: pointer; transition: background 0.2s; text-decoration: none; display: inline-block; }
        .btn:hover { background: #1d4ed8; }
        .btn-alt { background: transparent; border: 1px solid #374151; color: #9ca3af; margin-top: 15px; font-size: 14px; padding: 10px; }
        .btn-alt:hover { background: #1f2937; color: white; }
        input { width: 100%; padding: 12px; background: #1f2937; border: 1px solid #374151; border-radius: 8px; color: white; font-size: 16px; margin-bottom: 15px; text-align: center; }
        input:focus { border-color: #2563eb; outline: none; }
        .vault-item { background: #1f2937; border: 1px solid #374151; padding: 15px; border-radius: 8px; margin-bottom: 15px; text-align: left; display: flex; justify-content: space-between; align-items: center; }
        .vault-item span { font-weight: 500; font-size: 15px; }
        .download-link { background: #10b981; color: white; padding: 6px 12px; border-radius: 4px; text-decoration: none; font-size: 13px; font-weight: bold; }
        .download-link:hover { background: #059669; }
        .log-panel { background: #000; border: 1px solid #1f2937; font-family: monospace; font-size: 12px; padding: 10px; border-radius: 6px; color: #10b981; text-align: left; max-height: 100px; overflow-y: auto; margin-top: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <span class="badge" id="badge-text">Product Launch</span>
        <h1 id="main-title">The Ultimate Blueprint</h1>
        <p class="subtitle" id="main-subtitle">Get instant access to the master framework, private video guides, and premium resources code files.</p>
        <div class="status-box" id="status-message">🔒 Vault Status: LOCKED. Enter access key to unlock files.</div>

        <div id="landing-screen" class="screen active">
            <button class="btn" onclick="simulatePayment()">Buy Now ($19)</button>
            <button class="btn btn-alt" onclick="showScreen('login-screen')">Already bought? Enter Access Key</button>
        </div>

        <div id="login-screen" class="screen">
            <input type="password" id="passcode-input" placeholder="Enter Access Key or Creator PIN">
            <button class="btn" onclick="verifyAccess()">Unlock Vault</button>
            <button class="btn btn-alt" onclick="showScreen('landing-screen')">← Back to Details</button>
        </div>

        <div id="vault-screen" class="screen">
            <div class="vault-item">
                <span>📘 Blueprint Guide (PDF)</span>
                <a href="#" class="download-link" onclick="logDownload('Blueprint Guide')">Download</a>
            </div>
            <div class="vault-item">
                <span>📦 Complete Resource Pack (.zip)</span>
                <a href="#" class="download-link" onclick="logDownload('Resource Pack')">Download</a>
            </div>
            <button class="btn btn-alt" onclick="lockVault()">Lock Vault & Log Out</button>
        </div>

        <div class="log-panel" id="log-panel">
            [SYSTEM LOG] Core server active. Awaiting user handshake...
        </div>
    </div>

    <script>
        function addLog(message) {
            const logPanel = document.getElementById('log-panel');
            const time = new Date().toLocaleTimeString();
            logPanel.innerHTML += \`<br>[\${time}] \${message}\`;
            logPanel.scrollTop = logPanel.scrollHeight;
        }
        function showScreen(screenId) {
            document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
            document.getElementById(screenId).classList.add('active');
        }
        function simulatePayment() {
            addLog("Processing mock payment gateway transaction...");
            setTimeout(() => {
                addLog("Payment Successful! Received $19.00 USD.");
                addLog("Generated client access token: LAUNCH2026");
                alert("Payment complete! Your secret access token is: LAUNCH2026\\n\\nCopy this token and use it to unlock the vault!");
                showScreen('login-screen');
            }, 1000);
        }
        async function verifyAccess() {
            const key = document.getElementById('passcode-input').value;
            if(!key) return alert("Please enter a token!");
            addLog("Sending authorization token request to Express server...");
            
            const response = await fetch('/api/auth', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ key })
            });
            const data = await response.json();

            if (data.success) {
                addLog(\`Access Granted! Role authenticated: \${data.role.toUpperCase()}\`);
                document.getElementById('status-message').innerText = "🔓 Vault Status: OPEN (Role: " + data.role.toUpperCase() + ")";
                document.getElementById('status-message').classList.add('secure');
                if(data.role === 'creator') {
                    document.getElementById('badge-text').innerText = "OVERLORD CONTROL";
                    document.getElementById('main-title').innerText = "Creator Console";
                } else {
                    document.getElementById('badge-text').innerText = "VIP MEMBER";
                    document.getElementById('main-title').innerText = "Your Secure Vault";
                }
                showScreen('vault-screen');
            } else {
                addLog("WARNING: Unauthorized access attempt blocked by firewall.");
                alert("Invalid Token or PIN! Access Denied.");
            }
        }
        function logDownload(fileName) { addLog(\`File downloaded tracking event fired for: \${fileName}\`); }
        function lockVault() {
            addLog("User logged out. Revoking authorization session states.");
            document.getElementById('status-message').innerText = "🔒 Vault Status: LOCKED. Enter access key to unlock files.";
            document.getElementById('status-message').classList.remove('secure');
            document.getElementById('badge-text').innerText = "Product Launch";
            document.getElementById('main-title').innerText = "The Ultimate Blueprint";
            document.getElementById('passcode-input').value = "";
            showScreen('landing-screen');
        }
    </script>
</body>
</html>
`;

app.get('/', (req, res) => { res.send(htmlPage); });

app.post('/api/auth', (req, res) => {
    const { key } = req.body;
    if (key === CREATOR_PASSCODE) {
        return res.json({ success: true, role: 'creator' });
    } else if (key === VIP_PASSCODE) {
        return res.json({ success: true, role: 'vip' });
    } else {
        return res.json({ success: false, role: 'guest' });
    }
});

app.listen(PORT, () => console.log(`Server blasting off at http://localhost:${PORT}`));