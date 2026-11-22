#!/usr/bin/env python3
"""Independent exact checks of the commuting graph of rank-one partial bijections.
Requires SymPy. Prints finite corroborations only, not a proof for general n.
"""
import sympy as sp

def compose(x, y):
    """Partial composition x followed by y; None is the empty map."""
    a, b = x
    c, d = y
    return (a, d) if b == c else None

def adjacency(n):
    arrows = [(a, b) for a in range(n) for b in range(n)]
    M = sp.zeros(n*n)
    for i, x in enumerate(arrows):
        for j, y in enumerate(arrows):
            directly_commute = compose(x, y) == compose(y, x)
            shortcut = (x[1] != y[0] and y[1] != x[0])
            if i != j:
                assert directly_commute == shortcut, (n, x, y)
            M[i,j] = int(i != j and directly_commute)
    return M

def predicted(n, x):
    return sp.Poly(
        (x*x-(n-1)**2*x+(n-1)*(n-2))
        * (x*x+(n-1)*x-(n-2))**(n-1)
        * (x-(n-2))**(n-1)
        * (x+2)**((n-1)*(n-2)//2)
        * x**(n*(n-3)//2), x)

def main():
    x = sp.symbols('x')
    for n in range(3, 7):
        A = adjacency(n)
        computed = sp.Poly(A.charpoly(x).as_expr(), x)
        assert computed == predicted(n, x), f'characteristic polynomial mismatch at n={n}'
        degree_set = sorted(set(int(sum(A[i,j] for j in range(n*n))) for i in range(n*n)))
        assert degree_set == [(n-1)**2-1, (n-1)**2]
        assert A.rank() == n*(n+3)//2
        print(f'n={n}: vertices={n*n}, edges={sum(A)//2}, degrees={degree_set}, '
              f'nullity={n*(n-3)//2}, exact_spectrum=PASS, independent_compositions=PASS')
    print('All finite checks passed; uniform proof is in RESULT.md.')
if __name__ == '__main__':
    main()
