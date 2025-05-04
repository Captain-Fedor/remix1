import os
from dotenv import load_dotenv

def check_env():
    print("Checking environment setup...")
    
    # Try to load .env file
    load_dotenv()
    
    # Check for Infura Project ID
    infura_id = os.getenv('WEB3_INFURA_PROJECT_ID')
    if infura_id:
        print(f"✓ Found Infura Project ID (length: {len(infura_id)})")
        print(f"  First 6 chars: {infura_id[:6]}...")
    else:
        print("✗ WEB3_INFURA_PROJECT_ID not found!")
    
    # Check .env file exists
    if os.path.exists('.env'):
        print("✓ .env file exists")
        # Read and print file contents (safely)
        with open('.env', 'r') as f:
            contents = f.read().strip()
            print("\nFile contents (sanitized):")
            for line in contents.split('\n'):
                if line.startswith('WEB3_INFURA_PROJECT_ID'):
                    key, value = line.split('=', 1)
                    print(f"{key}={value[:6]}...")
                elif line.startswith('PRIVATE_KEY'):
                    print("PRIVATE_KEY=<hidden>")
                else:
                    print(line)
    else:
        print("✗ .env file not found!")
        print("  Looking in:", os.path.abspath('.'))

if __name__ == "__main__":
    check_env()