import requests
from plyer import notification
import time

def get_price():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        price = data['bitcoin']['usd']
        return price
    else:
        print("Error getting the price.")
        return None

def track_bitcoin():
    target_price = float(input("Enter the target price for Bitcoin (in USD): "))
    print(f"Tracking Bitcoin. Notifying when it drops below ${target_price}.")

    while True:
        current_price = get_price()

        if current_price is not None:
            print(f"Current Bitcoin price: ${current_price}")
            
            if current_price <= target_price:
                notification.notify(
                    title="Bitcoin Price Alert",
                    message=f"The price is now ${current_price}!",
                    timeout=10
                )
                print(f"Alert! Bitcoin is now at ${current_price}.")
                break
            else:
                print(f"Still higher than ${target_price}. Checking again...\n")
        
        time.sleep(60)

track_bitcoin()
