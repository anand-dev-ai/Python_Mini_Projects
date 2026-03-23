import matplotlib.pyplot as plt

# Data: Time (Morning, Afternoon, Evening, Night) and Cups Sold
times = ["8AM-12PM", "12PM-4PM", "4PM-8PM", "8PM-10PM"]
cups_sold = [45, 30, 85, 40] # Aap apna asli data yahan daal sakte hain

plt.figure(figsize=(8, 5))
plt.bar(times, cups_sold, color='brown')
plt.title("Daily Sales Trend - sukun chai.com")
plt.xlabel("Time Slot")
plt.ylabel("Cups Sold")
plt.show() # Ye ek graph generate karega
