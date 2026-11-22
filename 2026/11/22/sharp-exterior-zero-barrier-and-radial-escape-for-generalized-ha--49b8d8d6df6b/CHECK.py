"""Reproduce finite checks for the generalized-Hartogs vertex-polynomial theorem.
Requires Python 3 standard library only. Finite tests supplement the analytic proof.
"""
import cmath
import math


def add(a, b):
    return [((a[k] if k < len(a) else 0) + (b[k] if k < len(b) else 0)) for k in range(max(len(a), len(b)))]


def conv(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            r[j + k] += x * y
    return r


def deriv(a):
    return [k * a[k] for k in range(1, len(a))]


def mult(a, c):
    return [c * v for v in a]


def poly(a, z):
    v = 0j
    for c in reversed(a):
        v = v * z + c
    return v


def C(n):
    return [j * (n + 1 - j) for j in range(1, n + 1)]


def U_and_derivative(n, x):
    u0, d0 = 1., 0.
    if n == 0:
        return u0, d0
    u1, d1 = 2*x, 2.
    for _ in range(1, n):
        u0, u1, d0, d1 = u1, 2*x*u1-u0, d1, 2*u1 + 2*x*d1 - d0
    return u1, d1


def roots_C_via_chebyshev(n):
    nodes = sorted(math.cos(k * math.pi/(n+1)) for k in range(1,n+1))
    out = []
    for a,b in zip(nodes,nodes[1:]):
        da = U_and_derivative(n,a)[1]
        db = U_and_derivative(n,b)[1]
        assert da*db < 0, (n,a,b,da,db)
        for _ in range(70):
            mid=(a+b)/2
            dm=U_and_derivative(n,mid)[1]
            if da*dm <= 0:
                b=mid
                db=dm
            else:
                a=mid
                da=dm
        x=(a+b)/2
        theta=2*math.acos(x)
        out.append(cmath.exp(1j*theta))
    return out


def durand_kerner(a, max_iter=15000):
    """Approximate roots of small complex-coefficient polynomials."""
    d = len(a) - 1
    b = [c/a[-1] for c in a]
    if d == 1:
        return [-b[0]]
    radius = max(1.5, 1 + max(abs(v) for v in b[:-1]))
    roots = [radius*cmath.exp(2j*math.pi*(j+0.371)/d) for j in range(d)]
    for it in range(max_iter):
        delta = 0
        for j in range(d):
            denominator = 1.0+0j
            for k in range(d):
                if j != k:
                    denominator *= roots[j] - roots[k]
            if abs(denominator) < 1e-25:
                denominator += complex(1e-13,1e-13)
            step = poly(b, roots[j])/denominator
            roots[j] -= step
            delta=max(delta,abs(step))
        if delta < 4e-12:
            break
    assert it < max_iter-1, (a, roots)
    assert all(abs(poly(b,z)) < 2e-7 for z in roots), (a, roots)
    return roots


def run():
    algebra = 0
    for n in range(2,51):
        c=C(n);p=C(n-1)
        lhs = conv(c,[1,-3,3,-1])
        rhs = [0]*(n+3)
        rhs[0]=n;rhs[1]=-(n+2);rhs[n+1]=n+2;rhs[n+2]=-n
        assert lhs==rhs, ('boundary identity', n)
        # (n-1)C_n = z(z-1)C'_{n-1} + (n+2z)C_{n-1}
        a = mult(c,n-1)
        b=add(conv(deriv(p),[0,-1,1]),conv(p,[n,2]))
        assert add(a,mult(b,-1)) == [0]*n, ('lower endpoint',n)
        # (n+2)C_{n-1} = (1-z) C'_n + (n-1) C_n
        a=mult(p,n+2)
        b=add(conv(deriv(c),[1,-1]),mult(c,n-1))
        assert all(x==0 for x in add(a,mult(b,-1))), ('upper endpoint',n)
        assert c==list(reversed(c)), ('palindrome',n)
        algebra+=4
    cheby=0
    for n in range(2,15):
        for z in roots_C_via_chebyshev(n):
            assert abs(poly(C(n),z)) < 1e-6, (n,z,poly(C(n),z))
            assert abs(poly(C(n-1),z)) > 1e-6, (n,z)
            v=poly(C(n-1),z)/(z*poly(deriv(C(n)),z))
            expected=(1/z-1)/(n+2)
            assert abs(v-expected) < 1e-8, (n,z,v,expected)
            cheby+=1
    roots_count=0
    for n in range(2,9):
        for alpha in (.125,.375,.625,.875):
            p=C(n-1)+[0]
            c=C(n)
            a=[alpha*c[j]+(1-alpha)*p[j] for j in range(n)]
            roots=durand_kerner(a)
            assert len(roots)==n-1
            assert min(abs(z) for z in roots)>1+1e-5, (n,alpha,roots)
            roots_count += len(roots)
    velocities=0
    epsilon=1e-4
    for n in range(2,10):
        c=C(n)
        prev=C(n-1)+[0]
        perturbed=[(1-epsilon)*x+epsilon*y for x,y in zip(c,prev)]
        shifted=durand_kerner(perturbed)
        for z in roots_C_via_chebyshev(n):
            nearest=min(shifted,key=lambda w:abs(w-z))
            velocity=(abs(nearest)-1)/epsilon
            predicted=(1-z.real)/(n+2)
            assert abs(velocity-predicted)<6e-5, (n,z,velocity,predicted)
            velocities+=1
    print('PASS: {} exact polynomial identities; {} Chebyshev root/velocity comparisons; {} numerical exterior roots; {} first-order velocity comparisons'.format(algebra,cheby,roots_count,velocities))

if __name__=='__main__':
    run()
