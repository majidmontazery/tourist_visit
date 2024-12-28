def collect_travel_data():
    travel_data = []  # List to store user input data
    
    # Get the number of entries
    num_entries = int(input("How many countries would you like to add? "))
    
    for _ in range(num_entries):
        # Get user input for each entry
        country_visited = input("Enter the name of the country you visited: ")
        times_visited = int(input(f"How many times have you visited {country_visited}? "))
        cities_visited = input(f"Enter the cities you visited in {country_visited}, separated by commas: ").split(",")
        cities_visited = [city.strip() for city in cities_visited]  # Remove extra spaces
        
        # Create a dictionary for the country and append it to the list
        travel_entry = {
            "country": country_visited,
            "visits": times_visited,
            "cities": cities_visited
        }
        travel_data.append(travel_entry)
    
    return travel_data

# Collect travel data from the user
user_travel_data = collect_travel_data()

# Print the collected data
print("\nYour Travel Data:")
for entry in user_travel_data:
    print(entry)
