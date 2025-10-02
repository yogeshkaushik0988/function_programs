def create_multiplier(factor):
    """
    Returns a function that multiplies its input by 'factor'.
    This demonstrates a closure.
    """
    def multiplier(number):
        return number * factor
    return multiplier

# Create specific multiplier functions
double = create_multiplier(2)
triple = create_multiplier(3)

print(f"Doubling 5: {double(5)}")
print(f"Tripling 7: {triple(7)}")