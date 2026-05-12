"""
PROJECT: Aadi-Vayu Disaster Resilience Engine
VERSION: 1.0.0
DEVELOPER: Aditya Rai (CEO, KYXGO TECHNOLOGY)
LICENSE: Open Source (MIT)
"""

import requests
import sys
import time

class AadiVayuEngine:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"

    def log_status(self, message):
        """Custom NF-1 Style Logging"""
        timestamp = time.strftime("%H:%M:%S")
        print(f"[{timestamp}] [KYXGO-SYSTEM]: {message}")

    def fetch_disaster_data(self, city):
        self.log_status(f"Initiating satellite link for: {city.upper()}...")
        
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'
            }
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status() # Check for HTTP errors
            
            data = response.json()
            return self.analyze_risk(data, city)

        except requests.exceptions.ConnectionError:
            self.log_status("CRITICAL: Network connection failed. Check your link.")
        except requests.exceptions.HTTPError:
            self.log_status(f"ERROR: City '{city}' not found in global database.")
        except Exception as e:
            self.log_status(f"UNEXPECTED ERROR: {str(e)}")
        return False

    def analyze_risk(self, data, city):
        """Advanced Risk Analysis Logic"""
        main = data.get("main", {})
        weather = data.get("weather", [{}])[0]
        temp = main.get("temp")
        humidity = main.get("humidity")
        condition = weather.get("description", "Unknown")

        print("\n" + "="*45)
        print(f"🌍 DISASTER RISK REPORT: {city.upper()}")
        print("="*45)
        print(f"▸ STATUS      : {condition.capitalize()}")
        print(f"▸ TEMPERATURE : {temp}°C")
        print(f"▸ HUMIDITY    : {humidity}%")
        print("-" * 45)

        # Risk Intelligence
        risk_level = "LOW"
        advice = "System status nominal. No immediate action required."

        if temp > 40:
            risk_level = "HIGH (Heatwave)"
            advice = "STAY INDOORS. Extreme heat detected."
        elif "rain" in condition or "storm" in condition:
            risk_level = "MODERATE (Precipitation)"
            advice = "Monitor water levels. Secure outdoor assets."
        
        print(f"🚩 RISK LEVEL : {risk_level}")
        print(f"💡 ADVICE     : {advice}")
        print("="*45 + "\n")
        return True

if __name__ == "__main__":
    # OFFICIAL KYXGO PUBLIC API KEY
    KYXGO_API_KEY = "3cf2fba56ff75639784c699d26b1654e"
    
    engine = AadiVayuEngine(KYXGO_API_KEY)
    
    print("---------------------------------------------")
    print("   AADI-VAYU | DISASTER RESILIENCE ENGINE    ")
    print("       Powered by KYXGO TECHNOLOGY           ")
    print("---------------------------------------------")
    
    target_city = input("Enter Target City: ").strip()
    
    if target_city:
        engine.fetch_disaster_data(target_city)
    else:
        print("Error: City name cannot be empty.")
    
    input("Press ENTER to terminate secure session...")

