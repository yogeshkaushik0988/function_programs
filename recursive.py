def solve_hanoi(n, source, auxiliary, target):
    """
    Solves the Tower of Hanoi puzzle recursively.
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    solve_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    solve_hanoi(n - 1, auxiliary, source, target)

print("Solving Tower of Hanoi for 3 disks:")
solve_hanoi(3, 'A', 'B', 'C')