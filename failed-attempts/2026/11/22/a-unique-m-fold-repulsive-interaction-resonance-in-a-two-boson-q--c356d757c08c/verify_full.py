#!/usr/bin/env python3
"""Independent full two-boson occupation-basis check (requires SymPy).

A nonorthonormal monomial basis is used so every hopping coefficient is an
integer; this is an invertible similarity of the normalized bosonic Fock basis.
"""
import sympy as sp

x = sp.symbols('x')

def full_hamiltonian(m, interaction):
    sites = m + 1
    states = [(i, j) for i in range(sites) for j in range(i, sites)]
    lookup = {st: p for p, st in enumerate(states)}
    H = sp.zeros(len(states))
    for col, (a, b) in enumerate(states):
        occupation = [0] * sites
        occupation[a] += 1
        occupation[b] += 1
        if a == b:
            H[col, col] = interaction
        for leaf in range(1, sites):
            for dest, src in ((0, leaf), (leaf, 0)):
                if not occupation[src]:
                    continue
                update = occupation[:]
                update[src] -= 1
                update[dest] += 1
                updated_pair = tuple(k for k, n in enumerate(update) for _ in range(n))
                H[lookup[updated_pair], col] -= occupation[src]
    return H

def claimed_polynomial(m, u):
    singlet = x**3 - u*x**2 - 4*m*x + 2*(m-1)*u
    standard = x**3 - u*x**2 - m*x + (m-2)*u
    return sp.Poly((x-u)*x**(m*(m-3)//2)*singlet*standard**(m-1), x)

def main():
    poly_tests = 0
    for m in range(4, 9):
        for u in (1, 3, 6):
            H = full_hamiltonian(m, u)
            assert H.charpoly(x).as_poly(x) == claimed_polynomial(m, u), (m, u)
            poly_tests += 1
    resonance_tests = 0
    for m, u, eigenvalue in ((4, 3, 1), (7, 6, 2)):
        H = full_hamiltonian(m, u)
        nullity = H.rows - (H - eigenvalue*sp.eye(H.rows)).rank()
        assert nullity == m, (m, nullity)
        resonance_tests += 1
    print('FULL_TWO_BOSON_OK polynomial_checks=%d exact_resonance_ranks=%d' %
          (poly_tests, resonance_tests))

if __name__ == '__main__':
    main()
