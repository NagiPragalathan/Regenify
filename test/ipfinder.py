import requests

def get_external_ip():
    try:
        # Make a GET request to a service that returns the user's public IP address
        response = requests.get('https://api.ipify.org')

        # Extract the IP address from the response content
        ip_address = response.text.strip()

        return ip_address
    except Exception as e:
        print("Error:", e)
        return None

# Get and print the external IP address
print("External IP address:", get_external_ip())
