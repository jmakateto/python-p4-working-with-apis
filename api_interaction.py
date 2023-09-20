import requests

# Define the API endpoint URL
api_url = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

# Send a GET request to the API
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Initialize lists to store specific attributes
    names = []
    species_list = []  # Renamed to avoid conflict with the 'species' attribute

    zookeepers = []
    enclosures = []

    # Process and use the data as needed
    for item in data:
        # Access specific attributes in each item
        name = item.get("name", "N/A")
        species = item.get("species", "N/A")
        zookeeper = item.get("zookeeper", "N/A")
        enclosure = item.get("enclosure", "N/A")

        # Append data to respective lists
        names.append(name)
        species_list.append(species)  
        zookeepers.append(zookeeper)
        enclosures.append(enclosure)

    # Perform actions with the data 
    for i in range(len(names)):
        print(f"Name: {names[i]}, Species: {species_list[i]}, Zookeeper: {zookeepers[i]}, Enclosure: {enclosures[i]}")
else:
    print("Failed to retrieve data from the API.")
