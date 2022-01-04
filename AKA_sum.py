
A = [0, 1, 2, 3, 4, 5]

def sum(n):
    i = 0
    x = 0
    for i <= n[x]:
        if n[x] <= 1:
            return n[1]
    else:
        return sum((n-1) + n[x])

print(sum(A))