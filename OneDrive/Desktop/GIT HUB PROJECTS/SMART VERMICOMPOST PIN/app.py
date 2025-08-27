import random
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Use inline template to avoid template folder issues
template = """
<!DOCTYPE html>
<html>
<head>
    <title>Smart Vermicompost PIN</title>
</head>
<body>
    <h1>Smart Vermicompost PIN Generator</h1>
    <form action="/generate" method="POST">
        <label>Name:</label>
        <input type="text" name="name" required><br><br>

        <label>City:</label>
        <input type="text" name="city" required><br><br>

        <label>Quantity (kg):</label>
        <input type="number" name="quantity" required><br><br>

        <button type="submit">Generate PIN & Check Sensors</button>
    </form>
    {% if pin %}
        <h2>PIN: {{pin}}</h2>
        <p>Moisture: {{moisture}}%</p>
        <p>Humidity: {{humidity}}%</p>
        <p>Air Quality: {{air_quality}} ppm</p>
        <p>Compost Temp: {{compost_temp}}°C</p>
        <h3>Notifications:</h3>
        <p>{{notification_text}}</p>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        quantity = request.form['quantity']

        pin = name[:3].upper() + city[:2].upper() + str(quantity)

        # Simulate sensor readings
        moisture = random.randint(20, 80)
        humidity = random.randint(30, 90)
        air_quality = random.randint(200, 500)
        compost_temp = random.randint(25, 50)

        notifications = []
        if moisture < 30:
            notifications.append("🟠 Moisture too low! Water the compost.")
        if humidity > 80:
            notifications.append("🔴 Humidity high! Ensure proper ventilation.")
        if air_quality > 400:
            notifications.append("🔴 Air quality poor! Check airflow.")
        if compost_temp > 45:
            notifications.append("🔴 Compost temperature high! Monitor closely.")

        notification_text = "<br>".join(notifications) if notifications else "🟢 All parameters normal."

        return render_template_string(template, pin=pin, moisture=moisture, humidity=humidity,
                                      air_quality=air_quality, compost_temp=compost_temp,
                                      notification_text=notification_text)
    return render_template_string(template)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

