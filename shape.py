#Square size can be increased or decreased using scaling factor
import matplotlib.pyplot as plt
import sys
import csv

def read_csv(csv_path):
    with open(csv_path) as file:
        csv_contents = csv.reader(file)
        coordinates = [item for item in csv_contents]
        coordinates.pop(0)
    return coordinates

def draw_square(coordinates,scale_value):
    for coords in coordinates:
        x1, y1,side_length= int(coords[0]), int(coords[1]),int(coords[2])
        scaling_factor = side_length*scale_value
        x2,y2=x1+scaling_factor,y1+scaling_factor
        x = [x1, x2, x2, x1, x1]
        y = [y1, y1, y2, y2, y1]
        plt.plot(x, y, marker='o')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def main():
    # user_input python3 shape.py shape_coordinates.csv 2
    csv_path = sys.argv[1]
    scale_value = float(sys.argv[2])
    coordinates = read_csv(csv_path)    
    draw_square(coordinates,scale_value)

if __name__ == "__main__":
    main()
