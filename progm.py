import numpy as np
#Q1
sales =  [100, 200, 150, 300, 250, 400, 350]
sales_array = np.array(sales)
print(sales_array)

#Q2
arr1 = np.array([10, 20, 30])
arr2 = np.array([1, 2, 3])
addition = arr1 + arr_2
multiply = arr1 * arr_2
print("Addition result:", addition)
print("Multiplication result:", multiply)

#Q3
sales_jan = np.array([300, 400])
sales_feb = np.array([500, 600])
combined = np.concatenate((sales_jan, sales_feb))
print("Combined sales data:", combined)

#Q4
data = np.array([1, 2, 3, 4, 5, 6])
reshaped = data.reshape(2, 3)
print("Reshaped data:\n", reshaped)

#Q5
scores = np.array([[80, 90], [85, 95]])
flattened = scores.reshape(-1)
print("Flattened scores:", flattened)
