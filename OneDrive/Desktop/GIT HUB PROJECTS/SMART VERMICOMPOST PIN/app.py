import random
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return open("index.html").read()

@app.route('/generate', methods=['POST'])
def generate_pin():
    name = request.form['name']
    city = request.form['city']
    quantity = request.form['quantity']

    # Generate PIN
    pin = name[:3].upper() + city[:2].upper() + str(quantity)

    # Simulate sensor readings
    moisture = random.randint(20, 80)      # %
    humidity = random.randint(30, 90)      # %
    air_quality = random.randint(200, 500) # ppm
    compost_temp = random.randint(25, 50)  # Celsius

    # Notifications
    notifications = []
    if moisture < 30:
        notifications.append("Moisture too low! Water the compost.")
    if humidity > 80:
        notifications.append("Humidity high! Ensure proper ventilation.")
    if air_quality > 400:
        notifications.append("Air quality poor! Check airflow.")
    if compost_temp > 45:
        notifications.append("Compost temperature high! Monitor closely.")

    notification_text = "<br>".join(notifications) if notifications else "All parameters normal."

    return f"""
    Hello {name}, your Vermicompost PIN is: <b>{pin}</b><br><br>
    Moisture: {moisture}%<br>
    Humidity: {humidity}%<br>
    Air Quality: {air_quality} ppm<br>
    Compost Temp: {compost_temp}°C<br><br>
    Notifications:<br>{notification_text}
    """

if __name__ == "__main__":
    app.run(debug=True)
