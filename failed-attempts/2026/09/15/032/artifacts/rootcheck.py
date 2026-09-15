import numpy as np

def solve_root_eq(alpha, q):
    # solve (1 - J/r)^{1/q} = J/q, r = 1 - J/alpha, 0<J<min(alpha,1?) J<r
    # => 1 - J/r = (J/q)^q => J/r = 1 - (J/q)^q => with r=1-J/alpha
    # f(J) = J/(1-J/alpha) + (J/q)^q - 1 = 0
    from bisect import bisect
    lo, hi = 1e-12, min(alpha*0.999999, q*0.999999)
    def f(J):
        r = 1 - J/alpha
        return J/r + (J/q)**q - 1
    # check signs
    flo, fhi = f(lo), f(hi)
    return flo, fhi

for alpha in [0.2, 0.5, 1.0, 2.0]:
    for q in [2,3]:
        print(alpha, q, solve_root_eq(alpha,q))
