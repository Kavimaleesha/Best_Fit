# Best Fit

def best_fit(block_sizes, process_sizes):

    allocations = [-1] * len(process_sizes)

    for i in range(len(process_sizes)):
        best_index = -1

        for j in range(len(block_sizes)):
            if block_sizes[j] >= process_sizes[i]:
                if best_index == -1 or block_sizes[j] < block_sizes[best_index]:
                    best_index = j

        if best_index != -1:
            allocations[i] = best_index
            block_sizes[best_index] -= process_sizes[i]

    return allocations


block_sizes = list(map(int, input("Enter the sizes of memory blocks separated by spaces: ").split()))

process_sizes = list(map(int, input("Enter the sizes of processes separated by spaces: ").split()))

allocations = best_fit(block_sizes, process_sizes)

print("\nProcess No.   Process Size   Block Allocated")
for i in range(len(process_sizes)):
    block = f"Block {allocations[i] + 1}" if allocations[i] != -1 else "Not Allocated"
    print(f"{i + 1:<12} {process_sizes[i]:<14} {block}")

