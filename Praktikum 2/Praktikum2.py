def find_lis(arr):
    n = len(arr)
    best_solutions = []
    longest = 0

    # Fungsi DFS untuk membangun subsekuens
    def explore(idx, path):
        nonlocal longest, best_solutions
        
        next_found = False
        current_value = arr[idx]

        for nxt in range(idx + 1, n):
            if arr[nxt] > current_value:
                next_found = True
                explore(nxt, path + [arr[nxt]])

        # Jika tidak ada angka lebih besar, ya itu leaf 
        if not next_found:
            length = len(path)
            if length > longest:
                longest = length
                best_solutions = [path]
            elif length == longest:
                best_solutions.append(path)

    # Mulai DFS dari setiap posisi
    for i in range(n):
        explore(i, [arr[i]])

    return best_solutions, longest

data = [4, 1, 13, 7, 0, 2, 8, 11, 3]

hasil, p = find_lis(data)

print("Deret:", data)
print("Panjang LIS =", p)
print("LIS yang ditemukan:")
for seq in hasil:
    print(" →", seq)
