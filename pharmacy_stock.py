# Simple Inventory Predictor
medicines = {
    "Paracetamol": {"stock": 500, "daily_usage": 45},
    "Amoxicillin": {"stock": 200, "daily_usage": 15},
    "Cough Syrup": {"stock": 50, "daily_usage": 8}
}

print("--- Pharmacy Inventory Prediction ---")
for med, data in medicines.items():
    days_left = data["stock"] // data["daily_usage"]
    print(f"{med}: {data['stock']} units left. Will last for approx {days_left} days.")
    
    if days_left < 5:
        print(f"!!! ALERT: Reorder {med} immediately !!!")
