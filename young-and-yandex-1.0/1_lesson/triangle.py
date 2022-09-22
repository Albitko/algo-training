edges = []
counter = 0

for edge in range(3):
    edges.append(int(input()))

for i in range(3):
    if edges[i] < edges[(i - 1) % 3] + edges[(i + 1) % 3]:
        counter += 1

if counter == 3:
    print("YES")
else:
    print("NO")
