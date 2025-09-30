#git add .
#git commit -m "Fixed encryption bug"
#git push


import numpy as np


#This function will convert the deciphered numbers to letters and symbols
def number_to_letter(number: int) -> str:
    if 1 <= number <= 26:
        return chr(number + 64)
    elif number == 27:
        return  "."
    elif number == 28:
        return "!"
    elif number == 29:
        return ","
    elif number == 0:
        return " "
    else:
        return "?"
    

A = np.array([[0, -1/2, 1, 4], 
              [1, -1/2, -1, -2],
              [-1, 1, 1, 1],
              [0, 0, 0, -1]])

A_inv = np.linalg.inv(A)

B = np.array([[1, 3, 2, 0], 
              [0, 2, 2, -2],
              [1, 1, 1, 3],
              [0, 0, 0, -1]])

B_inv = np.linalg.inv(B)

message = np.array([[-11, 4, 34, 86],
                    [12, -2, -12, -37],
                    [5, -12, 14, 47],
                    [4, -9/2, 12, 40],
                    [-23, 16, 37, 64],
                    [-15, 8, 33, 83],
                    [3, 0, 12, 36],
                    [-2, -3/2, 14, 36],
                    [14, -29/2, 1, 9],
                    [0, 3/2, 9, 24],
                    [5, -7/2, -3, -20],
                    [7, 7/2, -2, 0],
                    [1, -8, 18, 70],
                    [3, 3, 3, -10],
                    [12, -2, -12, -37],
                    [18, -27/2, 7, 23],
                    [-5, -2, 19, 60],
                    [12, -11, 6, 40],
                    [-3, -4, 26, 74],
                    [-3, 4, 3, -6],
                    [-14, 33/2, 23, 36],
                    [5, -14, 18, 79],
                    [-3, -13/2, 22, 64],
                    [2, -4, 13, 42],
                    [27, -23, -8, 8],
                    [-14, 13/2, 29, 53],
                    [19, -39/2, 1, 26],
                    [4, -15/2, 8, 20],
                    [-27, 49/2, 32, 20],
                    [-13, -1/2, 40, 120],
                    [-2, 1/2, 14, 41],
                    [19, -14, -10, -3],
                    [7, -7, 5, 11],
                    [6, -5, 1, -14]
                    ])

    #print(message[0, :])

for row in message:
    decoded_row = row @ A_inv 
    for num in decoded_row:
        num_int = int(num)
        print(number_to_letter(num_int), end="")


