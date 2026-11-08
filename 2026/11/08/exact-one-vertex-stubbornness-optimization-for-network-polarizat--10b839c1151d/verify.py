"""Exact-arithmetic checks for single-coordinate Friedkin--Johnsen optimization.

Run: python3 verify.py
Only Python's standard library is used. These finite checks supplement the proof.
"""
from fractions import Fraction as F
from random import Random


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))


def mul(A, x):
    return [dot(row, x) for row in A]


def solve(A, b):
    n = len(A)
    aug = [[F(q) for q in row] + [F(b[i])] for i, row in enumerate(A)]
    for i in range(n):
        piv = next(j for j in range(i, n) if aug[j][i] != 0)
        aug[i], aug[piv] = aug[piv], aug[i]
        q = aug[i][i]
        aug[i] = [x/q for x in aug[i]]
        for j in range(n):
            if j != i:
                c = aug[j][i]
                aug[j] = [x-c*y for x, y in zip(aug[j], aug[i])]
    return [row[-1] for row in aug]


def pd(L, z):
    n = len(z)
    mean = sum(z, F(0))/n
    centered = [a-mean for a in z]
    return dot(z, mul(L,z))+dot(centered,centered)


def test_case(L, k, s, ell):
    n = len(k)
    fixed = k[:]
    fixed[ell] = F(0)
    A = [[L[i][j] + (fixed[i] if i==j else 0) for j in range(n)] for i in range(n)]
    x0 = solve(A, [fixed[i]*s[i] for i in range(n)])
    e = [F(int(i==ell)) for i in range(n)]
    u = solve(A,e)
    g = u[ell]
    d = s[ell]-x0[ell]
    Hx0 = [a+b-sum(x0,F(0))/n for a,b in zip(mul(L,x0),x0)]
    Hu = [a+b-sum(u,F(0))/n for a,b in zip(mul(L,u),u)]
    B = dot(u,Hx0)
    C = dot(u,Hu)
    assert g>0 and C>0
    q0 = pd(L,x0)
    assertions=0
    for t in (F(0),F(1,7),F(1,3),F(3,4),F(1),F(2),F(5),F(17)):
        kt=fixed[:]; kt[ell]=t
        At=[[L[i][j]+(kt[i] if i==j else 0) for j in range(n)] for i in range(n)]
        direct = solve(At,[kt[i]*s[i] for i in range(n)])
        eta=t/(1+t*g)
        proposed=[x0[i]+eta*d*u[i] for i in range(n)]
        assert direct==proposed
        assert pd(L,direct) == q0+2*eta*d*B+eta*eta*d*d*C
        assertions+=2
    if d!=0:
        eta_opt=max(F(0),min(F(1)/g,-B/(d*C)))
        qopt=q0+2*eta_opt*d*B+eta_opt**2*d*d*C
        for t in (F(0),F(1,7),F(1,3),F(3,4),F(1),F(2),F(5),F(17)):
            eta=t/(1+t*g)
            assert q0+2*eta*d*B+eta*eta*d*d*C >= qopt
            assertions+=1
    return assertions


def main():
    rng=Random(193715)
    num_graphs=0
    checks=0
    for n in range(2,8):
        for _ in range(90):
            L=[[F(0) for j in range(n)] for i in range(n)]
            edges={(i,i+1) for i in range(n-1)}
            edges |= {(i,j) for i in range(n) for j in range(i+2,n) if rng.randrange(5)==0}
            for i,j in edges:
                w=rng.choice([F(1,2),F(2,3),F(1),F(3,2),F(2)])
                L[i][i]+=w; L[j][j]+=w
                L[i][j]-=w; L[j][i]-=w
            ell=rng.randrange(n)
            k=[rng.choice([F(1,3),F(1,2),F(1),F(3,2),F(2)]) for _ in range(n)]
            s=[rng.choice([F(-1),F(-1,2),F(-1,3),F(0),F(1,3),F(1,2),F(1)]) for _ in range(n)]
            checks += test_case(L,k,s,ell)
            num_graphs += 1
    L=[[F(1),F(-1),F(0)],[F(-1),F(2),F(-1)],[F(0),F(-1),F(1)]]
    s=[F(1,2),F(-1),F(1,2)]
    def direct(t):
        K=[t,F(1),F(1)]
        return solve([[L[i][j]+(K[i] if i==j else 0) for j in range(3)] for i in range(3)], [K[i]*s[i] for i in range(3)])
    def closed(t):
        return 3*(21*t*t+6*t+5)/(4*(5*t+3)**2)
    for t in (F(0),F(1,7),F(1,3),F(1,2),F(1),F(8)):
        assert pd(L,direct(t))==closed(t)
    assert closed(F(0))==F(5,12)
    assert closed(F(1,3))==F(9,28)
    assert closed(F(1))==F(3,8)
    assert F(63,100)>F(9,28)
    # The derivative is exactly 24*(3*t-1)/(5*t+3)^3.
    for t in (F(0),F(1,7),F(1,3),F(1),F(8)):
        left=(3*(42*t+6)*4*(5*t+3)**2-3*(21*t*t+6*t+5)*40*(5*t+3))/(16*(5*t+3)**4)
        assert left==24*(3*t-1)/(5*t+3)**3
    print(f'VERIFY_OK configurations={num_graphs} exact_assertions={checks+15} three_vertex_minimizer=1/3')

if __name__ == '__main__':
    main()
