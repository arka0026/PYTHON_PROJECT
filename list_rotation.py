def rotate_list(lst, positions):
    if not lst:  # Handle empty lists
        return []
    positions %= len(lst)  # Adjust positions to avoid unnecessary rotations
    rotated = lst[len(lst) - positions:] + lst[:len(lst) - positions]
    return rotated

# Sample Input
result = rotate_list([1, 2, 3, 4, 5], 2)
print(f"Rotated list: {result}")