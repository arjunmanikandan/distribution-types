#To create squares based on the coordinates provided in the CSV file
import matplotlib.pyplot as plt
import sys
import csv

def read_csv(csv_path):
    with open(csv_path) as file:
        csv_contents = csv.reader(file)
        coordinates = [item for item in csv_contents]
        coordinates.pop(0)
    return coordinates

def draw_square(coordinates):
    for coords in coordinates:
        x1, y1, x2, y2 = int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3])
        x = [x1, x2, x2, x1, x1]
        y = [y1, y1, y2, y2, y1]
        plt.plot(x, y, marker='o')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def main():
    # user_input python3 shape.py shape_coordinates.csv
    csv_path = sys.argv[1]
    coordinates = read_csv(csv_path)    
    draw_square(coordinates)

if __name__ == "__main__":
    main()
