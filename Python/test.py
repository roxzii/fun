# A Dynamic Programming based Python3 program to
# find minimum of coins to make a given change V
import sys

# m is size of coins array (number of
# different coins)
def minCoins(coins, m, V):

    # table[i] will be storing the minimum
    # number of coins required for i value.
    # So table[V] will have result
    table = [0 for i in range(V + 1)]

    # Base case (If given value V is 0)
    table[0] = 0

    # Initialize all table values as Infinite
    for i in range(1, V + 1):
        table[i] = sys.maxsize

    # Compute minimum coins required
    # for all values from 1 to V
    for i in range(1, V + 1):

        # Go through all coins smaller than i
        for j in range(m):
            if coins[j] <= i:
                sub_res = table[i - coins[j]]
                if sub_res != sys.maxsize and sub_res + 1 < table[i]:
                    table[i] = sub_res + 1

    if table[V] == sys.maxsize:
        return -1

    return table[V]


# Driver Code
if __name__ == "__main__":

    for b in range(3):
        for d in range(450):
            V =7
            if b == 0:
                coins = [1, 4, 5, d]
                m = len(coins)
                print("Valores = 1 | 4 | 5 | ", d, "\n")
                print("Minimum coins required is ", minCoins(coins, m, V))
            if b == 1:
                coins = [1, 4, d, 7]
                m = len(coins)
                print("Valores = 1 | 4 | ", d, " | 7\n")
                print("Minimum coins required is ", minCoins(coins, m, V))
            if b == 2:
                coins = [1, d, 5, 7]
                m = len(coins)
                print("Valores = 1 | ", d, " | 5 | 7\n")
                print("Minimum coins required is ", minCoins(coins, m, V))
            if b == 3:
                coins = [d, 4, 5, 7]
                m = len(coins)
                print("Valores = ", d, " | 4 | 5 | 7\n")
                print("Minimum coins required is ", minCoins(coins, m, V))

    

# This code is contributed by ita_c
