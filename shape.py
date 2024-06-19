#To move the square across the graph
import matplotlib.pyplot as plt
import sys
import csv

def read_csv(csv_path):
    with open(csv_path) as file:
        csv_contents = csv.reader(file)
        coordinates = [item for item in csv_contents]
        coordinates.pop(0)
    return coordinates

def draw_square(coordinates,shift_x,shift_y):
    for coords in coordinates:
        x1, y1,side_length= int(coords[0]), int(coords[1]),int(coords[2])
        x1,y1,x2,y2=x1+shift_x,y1+shift_y,x1+side_length,y1+side_length
        x = [x1, x2, x2, x1, x1]
        y = [y1, y1, y2, y2, y1]
        plt.plot(x, y, marker='o')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def get_user_input():
    return {
        "csv_path" : sys.argv[1],
        "shift_x" : float(sys.argv[2]),
        "shift_y":  float(sys.argv[2]) }

#User Input for x and y coordinates +-x,+-y
#python3 shape.py shape_coordinates.csv 2 3
def main():
    user_inputs = get_user_input()
    coordinates = read_csv(user_inputs["csv_path"])    
    draw_square(coordinates,user_inputs["shift_x"],user_inputs["shift_y"])

if __name__ == "__main__":
    main()
