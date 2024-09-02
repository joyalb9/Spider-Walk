import sys

def find_min_bridges_anticlockwise(strands, bridges_number, fav_strand, bridges):
    # Initialize a list to track anticlockwise bridges
    bridge_anticlockwise = [0 for _ in range(strands)]
    
    # Create a dictionary to store bridges by distance
    bridges_dict = {}
    for distance, start in bridges:
        if distance in bridges_dict:
            bridges_dict[distance].append(start)
        else:
            bridges_dict[distance] = [start]
    
    print("Bridges:", bridges_dict)
    
    # Find sorted distances
    distances = sorted(bridges_dict.keys())
    print("Distances:", distances)
    
    # Finding minimum number of bridges from start to fav_strand
    start_strand = fav_strand
    start_distance = distances[0]
    
    for i in range(1, len(distances)):
        next_distance = distances[i]
        print("Next Distance:", next_distance)
        
        if start_strand in bridges_dict[next_distance]:
            if len(bridges_dict[next_distance]) > 1:
                start_strand = bridges_dict[next_distance][bridges_dict[next_distance].index(start_strand)]
            else:
                start_strand = bridges_dict[next_distance][0]
            
            start_distance = next_distance
            print("Updated Start:", start_distance, start_strand)
        else:
            bridge_anticlockwise[start_strand] += (next_distance - start_distance - 1)
            print("Bridges Anticlockwise:", bridge_anticlockwise)
    
    # Create operation list
    operation = [1 if i > 0 else 0 for i in bridge_anticlockwise]
    return operation

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) < 4:
        print("Usage: python spider_walk.py <strands> <bridges_number> <fav_place> <bridge pairs...>")
        sys.exit(1)

    strands = int(sys.argv[1])
    bridges_number = int(sys.argv[2])
    fav_place = int(sys.argv[3])
    
    # Ensure there are enough arguments for the bridges
    expected_arguments = 4 + 2 * bridges_number
    if len(sys.argv) != expected_arguments:
        print(f"Error: Expected {bridges_number} pairs of bridge values, but got {len(sys.argv) - 4} values.")
        sys.exit(1)

    bridges = []
    for i in range(bridges_number):
        x, y = map(int, sys.argv[4 + 2*i: 4 + 2*(i + 1)])
        bridges.append((x, y))
    
    print("Strands:", strands)
    print("Bridges Number:", bridges_number)
    print("Favorite Place:", fav_place)
    print("Bridges:", bridges)
    
    result = find_min_bridges_anticlockwise(strands, bridges_number, fav_place, bridges)
    print("Operation:", result)

if __name__ == "__main__":
    main()
