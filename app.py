import requests
from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)

# --- CONFIGURATION ---
WALLET_ADDRESS = "0x8b76b5c8e37fe09f0e8537174220ee375731fb74"
ETHERSCAN_API_KEY = "W34WN2AWITCC89GCFPQP43KM7D11X47UQ1" 

# میسجز اسٹور کرنے کے لیے ایک عارضی لسٹ
customer_requests = []

SERVICES = {
    "drop": {"name": "Drop Shipping Solutions", "keywords": "drop shipping ecommerce"},
    "model": {"name": "Design & Modeling Service", "keywords": "logo design branding art"},
    "micro": {"name": "Task Management", "keywords": "tasks work earning"},
    "workspace": {"name": "Digital Workspace", "keywords": "tools office setup"},
    "health_coach": {"name": "Health & Fitness Coaching", "keywords": "diet fitness workout"},
    "gig": {"name": "Global Gig Market", "keywords": "freelance services jobs"},
    "health": {"name": "Health Consultation", "keywords": "medical checkup advice"},
    "market": {"name": "Global Marketplace", "keywords": "buy sell products"},
    "contract": {"name": "Smart Contract Development", "keywords": "blockchain token crypto"},
    "blogger": {"name": "Guest Blogging & SEO", "keywords": "writing articles blog"},
    "web": {"name": "Web Development", "keywords": "website coding html"},
    "plugin": {"name": "Link & Plugin Creation", "keywords": "tools link generator"}
}

# --- HTML TEMPLATES ---
HTML_HOME = '''... (پہلے والا ہوم پیج کوڈ یہاں آئے گا) ...'''

@app.route('/')
def home():
    return render_template_string(HTML_HOME, services=SERVICES, wallet=WALLET_ADDRESS)

@app.route('/submit_request', methods=['POST'])
def submit_request():
    msg = request.form.get('message')
    svc = request.form.get('service')
    customer_requests.append({"service": svc, "message": msg}) # یہاں آپ کا ڈیٹا سیو ہو رہا ہے
    return "<h1>Your request has been sent to Customer Service.</h1>"

# --- OWNER ADMIN PANEL ---
@app.route('/admin')
def admin_panel():
    # یہاں آپ کسٹمرز کے تمام میسجز دیکھ سکتے ہیں
    rows = "".join([f"<tr><td>{r['service']}</td><td>{r['message']}</td></tr>" for r in customer_requests])
    return f'''
    <body style="background:#0b0f19; color:white; font-family:sans-serif; padding:50px;">
        <h1>👑 Owner Admin Panel</h1>
        <table border="1" style="width:100%; border-collapse:collapse;">
            <tr style="background:#238636;"><th>Service</th><th>Customer Message</th></tr>
            {rows}
        </table>
        <br><a href="/" style="color:#58a6ff;">Back to Home</a>
    </body>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
