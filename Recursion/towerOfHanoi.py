# Recursive Approach to solve tower of Hanoi
# https://www.tutorialspoint.com/data_structures_algorithms/tower_of_hanoi.htm
def towerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod", from_rod, "to rod", to_rod)
        return

    towerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to_rod", to_rod)
    towerOfHanoi(n - 1, aux_rod, to_rod, from_rod)


# Driver Code
n = 4
towerOfHanoi(n, 'A', 'B', 'C')