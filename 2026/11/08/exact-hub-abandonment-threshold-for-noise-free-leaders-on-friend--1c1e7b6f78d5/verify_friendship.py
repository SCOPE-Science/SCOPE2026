"""Direct exact-rational matrix checks of a grounded-Laplacian theorem.
Requires Python 3 standard library only. Run: python verify_friendship.py
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb


def laplacian(m):
    n = 2*m+1
    a = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        u, v = 2*i+1, 2*i+2
        for x, y in ((0, u), (0, v), (u, v)):
            a[x][x] += 1
            a[y][y] += 1
            a[x][y] -= 1
            a[y][x] -= 1
    return a


def inverse_trace(a, selected):
    remaining = [i for i in range(len(a)) if i not in selected]
    n = len(remaining)
    if not n:
        return Q(0)
    z = [[Q(a[i][j]) for j in remaining]
         + [Q(int(i == j)) for j in remaining] for i in remaining]
    for i in range(n):
        p = next((r for r in range(i, n) if z[r][i]), None)
        assert p is not None
        z[i], z[p] = z[p], z[i]
        t = z[i][i]
        z[i] = [u/t for u in z[i]]
        for r in range(n):
            if r == i or not z[r][i]:
                continue
            t = z[r][i]
            z[r] = [u-t*v for u, v in zip(z[r], z[i])]
    return sum((z[i][n+i] for i in range(n)), Q(0))


def profile(m, selected):
    h = int(0 in selected)
    t1 = t2 = 0
    for i in range(m):
        c = int((2*i+1) in selected)+int((2*i+2) in selected)
        t1 += c == 1
        t2 += c == 2
    return h,t1,t2


def trace_formula(m, h, t1, t2):
    t0 = m-t1-t2
    ans = Q(4,3)*t0 + Q(1,2)*t1
    if h:
        return ans
    d = Q(3,2)*t1 + 2*t2
    assert d > 0
    return ans + (1 + 2*t0 + Q(t1,4))/d


def predicted(m, k):
    if 3*k <= 2*m+1:
        hub = Q(8*m-5*k+5,6)
    else:
        hub = None
    if k <= m:
        outer = Q(8*m-5*k-7,6)+Q(4*m+2,3*k)
        n_outer = comb(m,k)*2**k
    else:
        outer = Q(2*m-k,2)+Q(2*m-k+4,2*(2*m+k))
        n_outer = comb(m,2*m-k)*2**(2*m-k)
    n_hub = comb(m,k-1)*2**(k-1) if 3*k <= 2*m+1 else 0
    if 3*k < 2*m+1:
        return hub,n_hub,True
    if 3*k == 2*m+1:
        assert hub==outer
        return hub,n_hub+n_outer,None
    return outer,n_outer,False


def check():
    matrix_cases=0; budgets=0; profile_cases=0; nonnest=0
    for m in range(2,6):
        L=laplacian(m)
        for k in range(1,2*m+1):
            scored=[]
            for s in combinations(range(2*m+1),k):
                set_s=set(s)
                h,t1,t2=profile(m,set_s)
                p=trace_formula(m,h,t1,t2)
                actual=inverse_trace(L,set_s)
                assert actual==p,(m,k,s,actual,p)
                scored.append((p,s))
                matrix_cases+=1
            expected,count,hub=predicted(m,k)
            observed=min(v for v,_ in scored)
            winners=[s for v,s in scored if v==observed]
            assert observed==expected and len(winners)==count, (m,k,expected,observed,count,len(winners))
            if hub is not None:
                assert all((0 in s)==hub for s in winners)
            budgets+=1
    # Extended exact-rational profile enumeration: every orbit, no matrix inversion.
    for m in range(2,32):
        for k in range(1,2*m+1):
            values=[]
            for h in (0,1):
                for t1 in range(m+1):
                    t2=(k-h-t1)//2
                    if k-h-t1!=2*t2 or t2<0 or t1+t2>m: continue
                    values.append((trace_formula(m,h,t1,t2),h,t1,t2))
                    profile_cases+=1
            best,count,hub=predicted(m,k)
            assert min(x[0] for x in values)==best,(m,k)
            winners=[x for x in values if x[0]==best]
            if hub is True:
                assert len(winners)==1 and winners[0][1]==1
            elif hub is False:
                assert len(winners)==1 and winners[0][1]==0
            else:
                assert len(winners)==2 and {x[1] for x in winners}=={0,1}
    # Specific strict non-nesting transition: F_5 budget 3 uses apex, budget 4 forbids apex.
    assert predicted(5,3)[2] is True and predicted(5,4)[2] is False
    nonnest+=1
    print('PASS exact grounded matrices:', matrix_cases)
    print('PASS exhaustive finite budgets:', budgets)
    print('PASS exact orbit/profile checks:', profile_cases)
    print('PASS strict nonnesting witnesses:', nonnest)


if __name__ == '__main__':
    check()
