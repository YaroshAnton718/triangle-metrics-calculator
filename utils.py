import math

def median(arr):
    """
    Calculates the medians of all sides of triangle.

    Parameters:
        arr (list): A list of sides

    Returns:
        Ma (float): Median A of triangle
        Mb (float): Median B of triangle
        Mc (float): Median C of triangle
    """
    a, b, c = arr[0], arr[1], arr[2]

    Ma = (1/2)*math.sqrt(2*c**2+2*b**2-a**2)
    Mb = (1/2)*math.sqrt(2*c**2+2*a**2-b**2)
    Mc = (1/2)*math.sqrt(2*b**2+2*a**2-c**2)

    return Ma, Mb, Mc

def bisector(arr):
    """
    Calculates the bisector of all sides of triangle.

    Parameters:
        arr (list): A list of sides

    Returns:
        La (float): Bisector A of triangle
        Lb (float): Bisector B of triangle
        Lc (float): Bisector C of triangle
    """
    p = perimeter(arr)/2
    a, b, c = arr[0], arr[1], arr[2]

    La = (2*math.sqrt(c*b*p*(p-a)))/(c+b)
    Lb = (2*math.sqrt(c*a*p*(p-b)))/(c+a)
    Lc = (2*math.sqrt(a*b*p*(p-c)))/(a+b)

    return La, Lb, Lc

def area(arr):
    """
    Calculates the area of triangle. Returns three arguments, that are equal.

    Parameters:
        arr (list): A list of sides

    Returns:
        Sa (float): Area of triangle
        Sb (float): Area of triangle
        Sc (float): Area of triangle
    """
    a, b, c = arr[0], arr[1], arr[2]
    ha, hb, hc = height(arr)[0], height(arr)[1], height(arr)[2]

    Sa= (1/2)*a*ha
    Sb= (1/2)*b*hb
    Sc= (1/2)*c*hc

    return Sa, Sb, Sc

def height(arr):
    """
    Calculates the height of all sides of triangle.

    Parameters:
        arr (list): A list of sides

    Returns:
        Ha (float): Height A of triangle
        Hb (float): Height B of triangle
        Hc (float): Height C of triangle
    """
    p = perimeter(arr)/2
    a, b, c = arr[0], arr[1], arr[2]

    Ha = (2/a)*math.sqrt(p*(p-a)*(p-b)*(p-c))
    Hb = (2/b)*math.sqrt(p*(p-a)*(p-b)*(p-c))
    Hc = (2/c)*math.sqrt(p*(p-a)*(p-b)*(p-c))

    return Ha, Hb, Hc

def perimeter(arr):
    """
    Calculates the perimeter of triangle.

    Parameters:
        arr (list): A list of sides

    Returns:
        perimeter (float): Perimeter of triangle
    """
    perimeter = sum(arr)

    return perimeter

def get_numbers():
    """
    Gets from user the sides of the triangle.
    Validates the user input.
    Calls other functions and prints result.
    """
    while True:
        i = 0
        sides = []
        while i < 3:
            try:
                side = float(input(f"Enter a side {i+1} [1; 100]: "))
                if side < 1 or side > 100:
                    print("Please enter a number between 1 and 100.")
                    continue
                else:
                    sides.append(side)
            except ValueError:
                print("Please enter a number.")
                continue

            i += 1

        if (sides[0] + sides[1]) > sides[2] and (sides[0] + sides[2]) > sides[1] and (sides[1] + sides[2]) > sides[0]:
            break
        else:
            print("This triangle doesn't exist. Please try again.")

    print(f"\nPerimeter of triangle: {round(perimeter(sides), 2)}")
    print(f"\nHeight a: {round(height(sides)[0], 2)}\nHeight b: {round(height(sides)[1], 2)}\nHeight c: {round(height(sides)[2], 2)}")
    print(f"\nArea of triangle: {round(area(sides)[0], 2)}")
    print(f"\nBisector a: {round(bisector(sides)[0], 2)}\nBisector b: {round(bisector(sides)[1], 2)}\nBisector c: {round(bisector(sides)[2], 2)}")
    print(f"\nMedian a: {round(median(sides)[0], 2)}\nMedian b: {round(median(sides)[1], 2)}\nMedian c: {round(median(sides)[2], 2)}")

def choice():
    """
    User's choice continue the program or not.
    Validates the user input.
    Calls get_number() function.
    """
    while True:
        get_numbers()

        while True:
            choice = input("\nWould you like to continue? (y/n): ")

            if choice == "y" or choice == "Y":
                break
            elif choice == "n" or choice == "N":
                return
            else:
                print("Please enter y or n.")
                continue