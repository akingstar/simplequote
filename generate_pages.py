import os

pages = {
    "debt-relief": "Debt Relief",
    "auto-insurance": "Auto Insurance",
    "health-insurance": "Health Insurance",
    "final-expense": "Final Expense",
    "ssdi": "SSDI Assistance",
    "home-warranty": "Home Warranty",
    "pest-control": "Pest Control"
}

for folder, title in pages.items():
    path = os.path.join(folder, "index.html")
    os.makedirs(folder, exist_ok=True)
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} Quotes & Services | Simple Quote Solution</title>
    <meta name="description" content="Compare top-rated US {title.lower()} plans and get free, no-obligation quotes instantly from licensed providers.">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {{ --primary: #0f172a; --accent: #2563eb; --cta: #16a34a; --bg: #f8fafc; --text: #0f172a; --gray: #64748b; }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', system-ui, sans-serif; }}
        body {{ background: var(--bg); color: var(--text); line-height: 1.6; }}
        .nav {{ background: #fff; border-bottom: 1px solid #e2e8f0; padding: 15px 5%; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 100; }}
        .logo {{ font-size: 18px; font-weight: 800; color: var(--accent); text-decoration: none; display: flex; align-items: center; gap: 8px; }}
        .back-home {{ color: var(--gray); text-decoration: none; font-weight: 600; font-size: 14px; }}
        .hero {{ background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%); color: #fff; padding: 45px 5%; text-align: center; }}
        .hero h1 {{ font-size: 2.2rem; margin-bottom: 10px; font-weight: 800; }}
        .hero p {{ font-size: 1.1rem; color: #cbd5e1; max-width: 600px; margin: 0 auto; }}
        .container {{ max-width: 950px; margin: 35px auto; padding: 0 20px; display: grid; grid-template-columns: 1.2fr 1fr; gap: 30px; }}
        @media(max-width: 768px){{ .container {{ grid-template-columns: 1fr; }} }}
        .content-box {{ background: #fff; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }}
        .content-box h2 {{ font-size: 1.4rem; margin-bottom: 15px; color: var(--primary); }}
        .content-box ul {{ margin-left: 20px; margin-top: 15px; color: var(--gray); }}
        .content-box li {{ margin-bottom: 10px; }}
        .form-box {{ background: #fff; border-radius: 12px; padding: 30px; box-shadow: 0 10px 25px rgba(0,0,0,0.08); border: 1px solid #e2e8f0; }}
        .form-box h3 {{ font-size: 1.25rem; margin-bottom: 5px; color: var(--primary); }}
        .form-group {{ margin-bottom: 14px; }}
        .form-group label {{ display: block; font-size: 0.82rem; font-weight: 700; color: #475569; margin-bottom: 5px; }}
        .form-group input {{ width: 100%; padding: 11px 14px; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 0.95rem; outline: none; }}
        .form-group input:focus {{ border-color: var(--accent); }}
        .submit-btn {{ width: 100%; background: var(--cta); color: #fff; border: none; padding: 13px; border-radius: 8px; font-size: 1rem; font-weight: 800; cursor: pointer; margin-top: 5px; transition: background 0.2s; }}
        .submit-btn:hover {{ background: #15803d; }}
        .tcpa {{ font-size: 0.7rem; color: #94a3b8; margin-top: 12px; line-height: 1.4; text-align: justify; }}
        .footer {{ background: #0f172a; color: #94a3b8; padding: 35px 5%; text-align: center; font-size: 0.85rem; margin-top: 60px; }}
        .footer a {{ color: #fff; text-decoration: none; margin: 0 8px; }}
    </style>
</head>
<body>
    <nav class="nav">
        <a href="../" class="logo"><i class="fa-solid fa-shield-halved"></i> Simple Quote Solution</a>
        <a href="../" class="back-home">&larr; Back to All Categories</a>
    </nav>
    <header class="hero">
        <h1>{title} Services & Coverage</h1>
        <p>Compare verified US providers, check your eligibility, and secure the best rates tailored for you.</p>
    </header>
    <div class="container">
        <div class="content-box">
            <h2>Why Choose Our {title} Program?</h2>
            <p>We connect qualified consumers directly with top-tier licensed agents and certified professionals across the United States to guarantee maximum savings and trusted service.</p>
            <ul>
                <li><strong>100% Free Comparison:</strong> No upfront costs or hidden fees.</li>
                <li><strong>Verified US Network:</strong> Partnered with accredited carriers and specialists.</li>
                <li><strong>Fast & Secure:</strong> Get connected within seconds with zero hassle.</li>
            </ul>
        </div>
        <div class="form-box">
            <h3>Get Your Free Quote</h3>
            <p style="font-size:0.82rem; color:var(--gray); margin-bottom:18px;">Takes less than 60 seconds.</p>
            <form id="leadForm">
                <input type="hidden" name="service" value="{title}">
                <div class="form-group"><label>Full Name</label><input type="text" name="fullName" placeholder="John Doe" required></div>
                <div class="form-group"><label>Phone Number (US)</label><input type="tel" name="phone" placeholder="(555) 000-0000" required></div>
                <div class="form-group"><label>Email Address</label><input type="email" name="email" placeholder="john@example.com" required></div>
                <div class="form-group"><label>ZIP Code</label><input type="text" name="zipCode" placeholder="90210" maxlength="5" required></div>
                <button type="submit" class="submit-btn"><i class="fa-solid fa-paper-plane"></i> Request Free Quote</button>
                <p class="tcpa"><strong>TCPA Consent:</strong> By clicking, you authorize Simple Quote Solution and partner network to contact you via phone, SMS, or automated dialer. Consent is not required to purchase.</p>
            </form>
            <div id="formSuccess" style="display:none; text-align:center; padding: 30px 0;">
                <i class="fa-solid fa-circle-check" style="font-size: 45px; color: var(--cta); margin-bottom: 10px;"></i>
                <h3 style="color:#1e293b;">Request Received!</h3>
                <p style="color:var(--gray); font-size:0.9rem; margin-top:5px;">A licensed specialist will reach out to you shortly.</p>
            </div>
        </div>
    </div>
    <footer class="footer">
        <p>&copy; 2026 Simple Quote Solution. All Rights Reserved.</p>
        <p style="margin-top:10px;"><a href="../privacy/">Privacy Policy</a> | <a href="../terms/">Terms of Service</a> | <a href="../tcpa/">TCPA Disclosure</a></p>
    </footer>
    <script>
        const SCRIPT_URL = "https://script.google.com/macros/s/AKfycbyAMPJQbQw7zctmpA3Flen-H2NG4gk1wKTDXNkS4J1uXavidkE2WFS51RbVU2mEZmGeYQ/exec";
        document.getElementById('leadForm').addEventListener('submit', async function(e) {{
            e.preventDefault();
            const btn = this.querySelector('button');
            btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Processing...';
            btn.disabled = true;
            let userIp = "Unknown";
            try {{ let res = await fetch('https://api.ipify.org?format=json'); let d = await res.json(); userIp = d.ip; }} catch(e){{}}
            const fd = new FormData(this);
            fd.append('ip', userIp); fd.append('userAgent', navigator.userAgent);
            fetch(SCRIPT_URL, {{ method: 'POST', body: fd }}).then(() => {{
                document.getElementById('leadForm').style.display = 'none';
                document.getElementById('formSuccess').style.display = 'block';
            }}).catch(() => {{
                document.getElementById('leadForm').style.display = 'none';
                document.getElementById('formSuccess').style.display = 'block';
            }});
        }});
    </script>
</body>
</html>"""
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated clean landing page for: {title}")

print("All dedicated pages generated successfully!")
