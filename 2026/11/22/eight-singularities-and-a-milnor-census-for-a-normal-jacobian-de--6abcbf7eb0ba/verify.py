"""Exact local Jacobian-length and incidence checks for a normal decic model.

Only uses SymPy and Python integers. The genericity and incidence geometry
are established in the accompanying written proof, not by this finite check.
"""
from sympy import symbols, groebner, diff
from math import comb
x,y,z=symbols('x y z')

def standard_count(generators, max_degree=32):
    G=groebner(generators,x,y,z,order='lex')
    lt=[p.LM(order='lex').exponents for p in G.polys]
    counts=[]
    for limit in (max_degree, max_degree+3):
        c=0
        for a in range(limit+1):
            for b in range(limit+1-a):
                for d in range(limit+1-a-b):
                    if not any(a>=A and b>=B and d>=D for A,B,D in lt):
                        c+=1
        counts.append(c)
    assert counts[0]==counts[1], (counts,lt)
    return counts[0]

# An ordinary quintuple point leads to the smooth tangent cone z^5=x^5+y^5.
ordinary=z**5-x**5-y**5
assert standard_count([diff(ordinary,t) for t in (x,y,z)],16)==64
# The two-tangent/one-transverse three-branch germ has an exact analytic normal form.
triple=z**5-x*(y**2-x**4)
assert standard_count([diff(triple,t) for t in (x,y,z)],16)==24
# A generic vertex has isolated weight-10 principal part with weights (1,1,2).
vertex=z**5-x**10-y**10
assert standard_count([diff(vertex,t) for t in (x,y,z)],28)==324
# Genus / intersection consistency for union of five (1,1) curves, then five plane conics.
assert (5-1)*(5-1)==5*4-5+1
assert (10-1)*(10-2)//2==5*4+2*comb(5,2)-5+1
assert 5*4==comb(5,2)*2
assert 5*24+2*64+324==572
# Independent global Euler consistency from the five-sheeted projection
# away from the vertex and compact hypersurface smoothing.
e_branch = 5*2 - 5*(3-1) - 2*(5-1)
e_line = 2
n_meet = 10
e_unramified_base = 3 - (e_branch + e_line - n_meet)
e_surface = 5*e_unramified_base + (e_branch-n_meet) + n_meet + 1
smooth_decic_euler = 10*(10**2 - 4*10 + 6)
assert (e_branch,e_unramified_base,e_surface,smooth_decic_euler-e_surface)==(-8,19,88,572)
print('PASS: Jacobian lengths 24/64/324; branch-genus and Euler identities; total 8 points and Milnor sum 572')
