"""Independent bit-level fixed-point and cut-distribution test on labelled wheels."""
from collections import Counter
from itertools import product
from math import comb

def minority_step(state):
    h = state[0]
    xs = state[1:]
    n = len(xs)
    k = sum(xs)
    nh = 0 if k * 2 > n else (1 if k * 2 < n else h)
    nr = tuple(1 if h + xs[(i - 1) % n] + xs[(i + 1) % n] <= 1 else 0 for i in range(n))
    return (nh,) + nr

def cut_size(state):
    h = state[0]
    xs = state[1:]
    return sum(v != h for v in xs) + sum(xs[i] != xs[(i+1) % len(xs)] for i in range(len(xs)))

def theoretical(n):
    return {n+z: 2*n*comb(z,n-2*z)//z for z in range((n+2)//3,n//2+1)}

def main():
    tested=0
    for n in range(3,15):
        hist = Counter()
        for s in product((0,1), repeat=n+1):
            tested += 1
            if minority_step(s)==s:
                hist[cut_size(s)] += 1
        assert dict(hist) == theoretical(n), (n, hist, theoretical(n))
        print(f'n={n} fixed={sum(hist.values())} spectrum={dict(sorted(hist.items()))}')
    print(f'PASS: exhaustive binary states={tested}; n=3..14')
if __name__ == '__main__': main()
