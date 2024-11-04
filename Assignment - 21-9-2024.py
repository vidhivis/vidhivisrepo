'''def get_season(month):
    seasons = ("Winter", "Winter", "Spring", "Spring", "Spring", "Summer",
               "Summer", "Summer", "Autumn", "Autumn", "Autumn", "Winter")

    if 1 <= month <= 12:

        return seasons[month - 1]
    else:
        return "Invalid month number"

def main():
    try:
        month = int(input("Enter a month number (1-12): "))

        season = get_season(month)
        print(f"The corresponding season is: {season}")

    except ValueError:
        print("Please enter a valid integer for the month.")

if __name__ == "__main__":
    main()


def collect_names():
    names_set = set()
    while True:
        name = input("Enter a name (or press Enter to stop): ")

        if name == "":
            break

        if name in names_set:
            print("Existing name")
        else:
            print("New name")
            names_set.add(name)

    return names_set

def print_names(names_set):
    print("\nThe names you entered are:")
    for name in names_set:
        print(name)

def main():
    names_set = collect_names()
    print_names(names_set)

if __name__ == "__main__":
    main()


def enter_airport(airports):
    icao_code = input("Enter the ICAO code of the airport: ").upper()
    if icao_code in airports:
        print("This airport is already in the system.")
    else:
        airport_name = input("Enter the name of the airport: ")
        airports[icao_code] = airport_name
        print(f"Airport {airport_name} with ICAO code {icao_code} has been added.")


def fetch_airport(airports):
    icao_code = input("Enter the ICAO code of the airport to fetch: ").upper()
    if icao_code in airports:
        print(f"The airport with ICAO code {icao_code} is: {airports[icao_code]}")
    else:
        print("No airport found with that ICAO code.")

def main():
    airports = {}

    while True:
        print("\nChoose an option:")
        print("1. Enter a new airport")
        print("2. Fetch airport information")
        print("3. Quit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            enter_airport(airports)
        elif choice == "2":
            fetch_airport(airports)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()'''
import sklearn
from contourpy.util import data

'''import array
original_array = array.array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array:", original_array)
original_array.reverse()
print("Reverse the order of the items:")
print(original_array)'''
'''import array
original_array = array.array('i', [1, 3, 5, 3, 7, 9, 3])
element_to_count = 3
occurrences = original_array.count(element_to_count)
print("Original array:", original_array)
print(f"Number of occurrences of the number {element_to_count} in the said array: {occurrences}")'''
'''def sort_string_by_unicode(input_string):
    sorted_string = ''.join(sorted(input_string))
    return sorted_string
input_string = "wikipedia"
sorted_result = sort_string_by_unicode(input_string)
print(f"Input: {input_string}")
print(f"Result: {sorted_result}")'''
'''my_array = [63,34,25,12,22,11,90,5]
n = len(my_array)
for i in range(1,n):
    insert_index = i
    current_value = my_array[i]
    for j in range(i-1,-1,-1):
        if my_array[j] > current_value:
            my_array[j+1] = my_array[j]
            insert_index = j
        else:
            break
        my_array[insert_index] = current_value

    print("sorted array:", my_array)'''
'''vertexData = ['A', 'B', 'C', 'D', 'E']

adjacency_matrix = [
    [0, 76, 47, 0, 47],  # Edges for A
    [76 ,0 ,47 ,49 ,0],  # Edges for B
    [47, 47, 0, 54, 47],  # Edges for C
    [0, 49, 54, 0, 0],
    [47, 0, 47, 0, 0]
]

def print_adjacency_matrix(matrix):
    print("\nAdjacency Matrix:")
    for row in matrix:
        print(row)

print('vertexData:', vertexData)
print_adjacency_matrix(adjacency_matrix)'''

'''def linearSearch(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
    return -1

arr = [2, 4, 7, 8, 67, 78, 3, 10, 11, 13, 85]
targetVal = 11

result = linearSearch(arr, targetVal)

if result != -1:
    print("Value", targetVal, "found at index", result)
else:
    print("Value", targetVal, "not found")'''
'''arr = [2, 4, 7, 8, 67, 78, 3, 10, 11, 13, 85]

n = len(arr)
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("Sorted array:", arr)'''
'''arr = [1, 4, 7, 8, 6, 9, 3, 10, 11, 13, 17]

n = len(arr)
for i in range(1, n):
    insert_index = i
    current_value = arr[i]

    for j in range(i - 1, -1, -1):
        if arr[j] > current_value:
            arr[j + 1] = arr[j]
            insert_index = j
        else:
            break

    arr[insert_index] = current_value

print("Sorted array:", arr)'''
import numpy as np
A = np.array([[1,2,3], [4,5,6]])
np.sum(A)
np.sum(A,0)
np.sum(A,1)

np.prod(A)
np.prod(A,0)
np.prod(A,1)
np.min(A)
np.min(A,0)
np.min(A,1)
np.max(A)
np.max(A,0)
np.max(A,1)
np.mean(A)
np.mean(A,0)
np.mean(A,1)
np.median(A)
np.median(A,0)
np.median(A,1)
np.std(A)
np.std(A,0)
np.std(A,1)
np.var(A)
np.var(A,0)
np.var(A,1)
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("linreg_data.csv",skiprows=0,names=["x","y"])
print(data)
xpd = data["x"]
ypd = data["y"]
n = xpd.size
plt.scatter(xpd,ypd)
plt.show()
xbar = np.mean(xpd)
ybar = np.mean(ypd)
term1 = np.sum(xpd*ypd)
term2 = np.sum(xpd**2)
b = (term1-n*xbar*ybar)/(term2-n*xbar*xbar)
a = ybar - b*xbar
x = np.linspace(0,2,100)
y = a+b*x
plt.plot(x,y,color="black")
plt.scatter(xpd,ypd)
plt.scatter(xbar,ybar,color="red")
plt.show()
import numpy as np
from sklearn import linear_model
my_data = np.genfromtxt('linreg_data.csv',delimiter=',')
xp = my_data[:,0]
yp = my_data[:,1]
xp = xp.reshape(-1,1)
yp = yp.reshape(-1,1)
regr = linear_model.LinearRegression()
regr.fit(xp,yp)
print(regr.coef_,regr.intercept_)
xval = np.full((1,1),0.5)
yval = regr.predict(xval)
print(yval)
xval = np.linspace(-1,2,20).reshape(-1,1)
yval  = regr.predict(xval)
plt.plot(xval,yval)
plt.scatter(xp,yp,color="red")
plt.show()
from sklearn import metrics
yhat = regr.predict(xp)
print('Mean Absolute Error:', metrics.mean_absolute_error(yp,yhat))
print('Mean Squared Error:', metrics.mean_squared_error(yp,yhat))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(yp,yhat)))
print('R2 value:', metrics.r2_score(yp,yhat))
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
data_pd = pd.read_csv("quadreg_data.csv",skiprows=0,names=["x","y"])
print(data_pd)

xpd = np.array(data_pd["x"])
ypd = np.array(data_pd["y"])
xpd = xpd.reshape(-1,1)
ypd = ypd.reshape(-1,1)
poly_reg = PolynomialFeatures(degree=2)
X_poly = poly_reg.fit_transform(xpd)
pol_reg = LinearRegression()
pol_reg.fit(X_poly,ypd)
plt.scatter(xpd,ypd, color='red')
xval = np.linspace(-1,1,10).reshape(-1,1)
plt.plot(xval,pol_reg.predict(poly_reg.transform(xval)), color="blue")
plt.show()
print(pol_reg.coef_)
print("c=",pol_reg.intercept_)

