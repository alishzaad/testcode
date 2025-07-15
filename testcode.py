import hmac
import hashlib

def get_lucky_number(server_seed, client_seed, nonce):
    message = f"{client_seed}:{nonce}"
    hash_hex = hmac.new(
        server_seed.encode(),
        message.encode(),
        hashlib.sha512
    ).hexdigest()

    # پیدا کردن اولین عدد زیر 1,000,000 برای محاسبه
    for i in range(0, len(hash_hex) - 5, 5):
        segment = hash_hex[i:i+5]
        number = int(segment, 16)
        if number < 1000000:
            return number % 100
    return 0

def main():
    print("🔐 LuckyGames Lucky Number Predictor")
    
    server_seed = input("🔑 Server Seed (revealed): ").strip()
    client_seed = input("🧪 Client Seed: ").strip()
    target_result = input("🎯 Do you want to find a specific lucky number? (y/n): ").lower()

    if target_result == 'y':
        desired_number = int(input("🎯 Enter desired lucky number (0–99): "))
        max_nonce = int(input("🔁 Max nonce to try (e.g. 1000): "))
        
        print(f"🔍 Searching for nonce that gives lucky number {desired_number}...")

        for nonce in range(0, max_nonce):
            lucky = get_lucky_number(server_seed, client_seed, nonce)
            if lucky == desired_number:
                print(f"✅ Found! Nonce = {nonce} → Lucky Number = {lucky}")
                break
        else:
            print("❌ Not found in given range.")

    else:
        nonce = int(input("🔢 Nonce: "))
        lucky = get_lucky_number(server_seed, client_seed, nonce)
        print(f"🎲 Lucky Number for nonce {nonce}: {lucky}")

if __name__ == "__main__":
    main()
