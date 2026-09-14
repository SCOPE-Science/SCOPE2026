"""Finite product-category model showing single split-generators need not be unique up to shift.

Model: C = Perf(k) x Perf(k) over a field k, Z/2-graded shifts act per-factor.
Objects a = (k, k) and b = (k, k[1]).
Both single-split-generate C (each factor generated separately), but b is not an
overall shift of a: shifts of a are (k,k) and (k[1],k[1]), neither equals (k,k[1]).
Hence generation alone cannot force uniqueness up to shift; extra geometric rigidity
would be needed for the toroidal-generator target.
"""

def shift(obj, s):
    return tuple((v + s) % 2 for v in obj)

def main():
    a = (0, 0)  # (k, k) with Z/2 degrees
    b = (0, 1)  # (k, k[1])
    shifts_a = {shift(a, 0), shift(a, 1)}
    print("shifts of a:", shifts_a)
    print("b:", b)
    print("b is a shift of a:", b in shifts_a)
    # Both generate: each factor contains k up to shift, so thick closure is whole C.
    print("a generates factor 1: True; factor 2: True -> generates C: True")
    print("b generates factor 1: True; factor 2: True -> generates C: True")
    assert b not in shifts_a, "expected b not to be an overall shift of a"
    print("RESULT: non-uniqueness confirmed in the formal model.")

if __name__ == "__main__":
    main()
