from flask import Flask, render_template, request

app = Flask(__name__)

PROBLEMS = {
    "brake_noise": """Likely cause: Worn brake pads

Urgency: ⚠️ Drive carefully. Replace within 2–3 days.

Estimated cost: ₹3,000 – ₹6,000

Ask your mechanic: Ask mechanic to check brake pad thickness before replacing discs.

Disclaimer: This tool gives general guidance only. Not a professional diagnosis.""",

    "engine_overheat": """Likely cause: Low coolant or radiator issue

Urgency: 🚨 Stop driving immediately if temperature rises.

Estimated cost: ₹2,000 – ₹8,000

Ask your mechanic: Check coolant leaks and radiator fan.""",

    "battery_issue": """Likely cause: Weak or dead battery

Urgency: ⚠️ Jump start only if needed.

Estimated cost: ₹4,000 – ₹7,000

Ask your mechanic: Test battery health before replacing.""",

    "vibration": """Likely cause: Wheel imbalance or worn suspension

Urgency: ⚠️ Safe for short drives.

Estimated cost: ₹1,500 – ₹5,000

Ask your mechanic: Wheel balancing + suspension inspection.""",

    "ac_not_cooling": """Likely cause: Low refrigerant or clogged AC filter

Urgency: ❄️ Not critical, but uncomfortable.

Estimated cost: ₹1,500 – ₹4,000

Ask your mechanic: Check refrigerant pressure and cabin filter.""",

    "smoke_exhaust": """Likely cause: Engine oil burning or coolant leak

Urgency: 🚨 Stop driving if smoke is thick.

Estimated cost: ₹5,000 – ₹20,000

Ask your mechanic: Identify smoke color before repair.""",

    "poor_mileage": """Likely cause: Dirty air filter or worn spark plugs

Urgency: ⚠️ Can drive, but inefficient.

Estimated cost: ₹800 – ₹3,000

Ask your mechanic: Replace air filter and inspect plugs.""",

    "hard_steering": """Likely cause: Low power steering fluid

Urgency: ⚠️ Fix soon to avoid damage.

Estimated cost: ₹1,000 – ₹3,000

Ask your mechanic: Check for leaks in steering system."""
}


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        problem = request.form.get("problem")
        result = PROBLEMS.get(problem)

    return render_template("index.html", result=result)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
