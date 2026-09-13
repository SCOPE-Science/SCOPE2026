"""Extend closed-form guesses to l=4,5 (fewer k), and b-polynomial view.

For l=4: try classes C_top, D_top(m=k), S_bot(m=-k+1), Z with k=1,2(,3 if feasible).
Also compute Q(t) - (t-b)^l at t=b for formulas.
"""
import sympy as sp
import sys
sys.path.insert(0, '.')
from scan_one import chi_poly_auto

t, K = sp.symbols('t K')


def show_class(l, tag, mk, ks):
    print(f'=== l={l} {tag} ===')
    for k in ks:
        skip = mk(k)
        chi = chi_poly_auto(l, k, skip)
        b = 2 * k * l
        Q = sp.simplify(chi / (t - 1))
        print(f'k={k} skip={skip} Q(b)={int(Q.subs(t,b))} chi={sp.expand(chi)}', flush=True)


if __name__ == '__main__':
    l = int(sys.argv[1])
    ks = [int(x) for x in sys.argv[2].split(',')]
    show_class(l, 'C_top', lambda k: ('c', k), ks)
    show_class(l, 'D_top', lambda k: ('d', k), ks)
    show_class(l, 'S_bot', lambda k: ('s', -k + 1), ks)
    show_class(l, 'Z', lambda k: ('z',), ks)
