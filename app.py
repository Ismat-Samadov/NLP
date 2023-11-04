import requests
import streamlit as st

def get_ip_geolocation(ip_address):
    url = f"https://ipapi.co/{ip_address}/json"
    
    # Define custom headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Referer": "https://ipapi.co/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,ru;q=0.7,az;q=0.6",
        "Cookie": "csrftoken=ZFpiWuIi9nUY2NFtkSZkPUmR3np7u6sKgYHbWkHYfAhs1s4OidIJvDjfGEtkzee0",
        "Dnt": "1",
        "Sec-Ch-Ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        geolocation_data = response.json()
        return geolocation_data
    else:
        print(f"Failed to retrieve geolocation data. Status code: {response.status_code}")
        return None

def get_public_ip():
    try:
        response = requests.get("https://httpbin.org/ip")
        if response.status_code == 200:
            data = response.json()
            return data.get("origin", "Unable to retrieve IP")
        else:
            return "Unable to retrieve IP"
    except Exception as e:
        return "Unable to retrieve IP"

ip_address = get_public_ip()
geolocation_data = get_ip_geolocation(ip_address)
image_url = "https://images.unsplash.com/photo-1545987796-200677ee1011?auto=format&fit=crop&q=80&w=2070&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""

if geolocation_data:
    print("Geolocation Data:")
    for key, value in geolocation_data.items():
        print(f"{key}: {value}")

def main():
    ip_address = get_public_ip()
    if ip_address:
        geolocation_data = get_ip_geolocation(ip_address)
        if geolocation_data:
            city = geolocation_data.get("city", "N/A")
            country = geolocation_data.get("country_name", "N/A")
            st.sidebar.write(f"IP address: {ip_address}")
            st.sidebar.write(f"City: {city}")
            st.sidebar.write(f"Country: {country}")
        else:
            st.sidebar.error("Failed to retrieve geolocation data.")
    else:
        st.sidebar.error("Unable to retrieve your public IP address")

if __name__ == "__main__":
    st.markdown(hide_st_style, unsafe_allow_html=True)
    st.markdown(f'<img src="{image_url}" style="max-width: 100%; height: auto; width: 100vw;">', unsafe_allow_html=True)
    main()