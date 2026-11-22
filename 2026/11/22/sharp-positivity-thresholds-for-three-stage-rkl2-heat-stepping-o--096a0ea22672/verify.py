"""Exact-rational checks for three-stage RKL2 graph-heat endpoint positivity.

The finite checks support, but do not replace, the all-size analytic theorem.
Run: python3 verify.py
Python standard library only.
"""
from fractions import Fraction as F

checks = 0


def test(condition, explanation):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(explanation)


def r(t):
    return 1 - t + t*t/2 - t*t*t/15


def laplacian(p, q):
    n = p+q
    return [[F(q if i < p else p) if i == j else
             (F(-1) if (i < p) != (j < p) else F(0))
             for j in range(n)] for i in range(n)]


def product(A, B):
    n = len(A)
    return [[sum((A[i][k]*B[k][j] for k in range(n)), F(0))
             for j in range(n)] for i in range(n)]


def matrix(p, q, h):
    L = laplacian(p, q)
    L2 = product(L, L)
    L3 = product(L2, L)
    n = p + q
    return [[(F(i == j) - h*L[i][j] + h*h*L2[i][j]/2
              - h*h*h*L3[i][j]/15) for j in range(n)] for i in range(n)]


def predicted(p, q, h, i, j):
    n = p+q
    if (i < p) != (j < p):
        return (1-r(n*h))/n
    if i < p:
        y = q*h*h*(F(1,2)-h*(n+q)/15)
        return y + (r(q*h) if i == j else 0)
    y = p*h*h*(F(1,2)-h*(n+p)/15)
    return y + (r(p*h) if i == j else 0)


def bisect_minus_target(target, left=F(5), right=F(6), iterations=70):
    # Find unique zero of r(t)-target in (5,6); r is strictly decreasing.
    assert r(left) > target > r(right)
    for _ in range(iterations):
        mid = (left+right)/2
        if r(mid) >= target:
            left = mid
        else:
            right = mid
    return left,right


# Check exact polynomial matrix calculations against independently derived
# entry-type formula on all small bipartite graphs and many rational steps.
steps = [F(0), F(1,30), F(1,9), F(1,4), F(2,5), F(1,2),
         F(3,4), F(1), F(7,5), F(2), F(4)]
for p in range(1,6):
    for q in range(p,9):
        for h in steps:
            M = matrix(p,q,h)
            for i in range(p+q):
                test(sum(M[i], F(0)) == 1, 'row sum')
                for j in range(p+q):
                    test(M[i][j] == predicted(p,q,h,i,j),
                         'formula mismatch for p=%s q=%s h=%s i=%s j=%s' % (p,q,h,i,j))
                    test(M[i][j] == M[j][i], 'symmetric')

# Every nontrivial class's first crossing is realized in the predicted entry.
for p in range(2,10):
    for q in range(p,12):
        n = p+q
        critical = F(15, 2*(p+2*q))
        for scale in (F(999,1000), F(1), F(1001,1000)):
            h = critical * scale
            cross = predicted(p,q,h,0,p)
            within_A = predicted(p,q,h,0,1)
            within_B = predicted(p,q,h,p,p+1)
            test(cross > 0, 'cross edge should stay positive near threshold')
            test((within_B >= 0) if (q>p or scale<=1) else (within_B<0), 'other part cannot preempt first when q>p; ties when equal')
            test((within_A >= 0) == (scale <= 1), 'first within-class threshold')
            for i in range(n):
                test(predicted(p,q,h,i,i)>0, 'diagonal positive near cutoff')

# For the star graph the hub diagonal uniquely preempts the first leaf-pair.
for q in range(2,50):
    n = q+1
    lo, hi = bisect_minus_target(-F(1,q))
    leaf_cut = F(15*n, 2*(n+1))
    test(lo > 5 and hi < leaf_cut, 'star hub has earliest cutoff')
    test(hi < F(45,8), 'star root universally bounded by 45/8')
    test(r(lo) >= -F(1,q) and r(hi) <= -F(1,q), 'root bracket')
    test((F(1)+q*r(lo))/n >= 0, 'hub before root')
    test((F(1)+q*r(hi))/n <= 0, 'hub after root')
    h = hi/n
    test(predicted(1,q,h,1,2) > 0, 'leaf-to-leaf entry still positive')
    test(predicted(1,q,h,1,1) > 0, 'leaf diagonal still positive')
    test(predicted(1,q,h,0,1) > 0, 'hub-leaf entry still positive')

# Two-state graph positivity persists to scalar spectral endpoint.
a0, a1 = bisect_minus_target(F(-1))
test(a0 > F(29,5) and a1 < F(581,100), 'scalar edge bracket')
for t in [F(0), F(1), F(3), F(5), a0, a1 + F(1,100)]:
    M=matrix(1,1,t/2)
    test((min(min(row) for row in M)>=0) == (t<=a0), 'two-state endpoint')

print('VERIFY_OK', checks)
