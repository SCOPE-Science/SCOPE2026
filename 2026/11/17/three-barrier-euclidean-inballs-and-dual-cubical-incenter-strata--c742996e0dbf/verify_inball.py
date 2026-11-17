"""Independent finite-dimensional checks for elementary split-polytope inballs.

Runs with Python >=3.10 and scipy.  Finite tests are not an infinite proof.
"""
from math import sqrt, isclose
from scipy.optimize import linprog


def predicted(n, k, h, r):
    s = n - h
    q = sqrt((n - 1) / n)
    p = sqrt(h * s / n)
    vals = (min(k, n-k)/(n*q), r/(h*q+p), (s-k+r)/(s*q+p))
    return vals, min(vals), q, p


def check_case(n, k, h, r):
    vals, radius, q, p = predicted(n, k, h, r)
    Au, bu = [], []
    for i in range(n):
        row = [0.] * (n+1)
        row[i], row[-1] = -1., q
        Au.append(row);bu.append(0.)
        row = [0.] * (n+1)
        row[i], row[-1] = 1., q
        Au.append(row);bu.append(1.)
    row = [1.] * h + [0.] * (n-h) + [p]
    Au.append(row);bu.append(float(r))
    obj = [0.] * n + [-1.]
    res = linprog(obj, A_ub=Au, b_ub=bu, A_eq=[[1.]*n+[0.]], b_eq=[float(k)],
                  bounds=[(None,None)]*n+[(0,None)], method='highs')
    assert res.success, (n,k,h,r,res.message)
    assert isclose(res.x[-1], radius, abs_tol=2e-8, rel_tol=2e-8), (n,k,h,r,vals,res.x[-1])
    t = q * radius
    # An explicit symmetric certificate at each parameter point.
    A = max(h*t, k-(n-h)*(1-t))
    bsum = k-A
    assert h*t-1e-8 <= A <= h*(1-t)+1e-8
    assert (n-h)*t-1e-8 <= bsum <= (n-h)*(1-t)+1e-8
    assert A+p*radius <= r+1e-8
    return vals


def main():
    cases = 0
    winning = {'0':0, 'L':0, 'U':0}
    for n in range(8, 22):
        for k in range(4, n-3):
            for h in range(4, n-3):
                s = n-h
                for r in range(2,h-1):
                    if not (2 <= k-r <= s-2):
                        continue
                    vals = check_case(n,k,h,r)
                    winning['0LU'[min(range(3), key=lambda i:vals[i])]] += 1
                    cases += 1
    print(f'ELEMENTARY_SPLIT_INBALL_PASS cases={cases} winning={winning}')

if __name__=='__main__':
    main()
