"""Exact symbolic checks for Gauss--Legendre heat-step kernels on complete multipartite graphs.

Run: python verify_gauss_multipartite.py
Requires sympy. The finite checks supplement, but do not substitute for, the all-order analytic proof.
"""
import math
import sympy as sp

z=sp.Symbol('z'); checks=0

def coefficients(s):
    return [sp.Rational(math.factorial(2*s-k)*math.factorial(s), math.factorial(2*s)*math.factorial(k)*math.factorial(s-k)) for k in range(s+1)]

def p_eval(s, x):
    return sum(c*x**j for j,c in enumerate(coefficients(s)))

def scalar(s,x):
    return sp.factor(p_eval(s,-x)/p_eval(s,x))

def spectral(s, parts, h):
    n=sum(parts); out=sp.zeros(n)
    r_n=scalar(s,h*n)
    for u in range(n):
        for v in range(n):out[u,v]=(1-r_n)/n
    off=0
    for a in parts:
        r_b=scalar(s,h*(n-a))
        for u in range(off,off+a):
            for v in range(off,off+a):
                out[u,v]+=(r_n-r_b)/a
                if u==v:out[u,v]+=r_b
        off+=a
    return out

def lap(parts):
    n=sum(parts); out=sp.zeros(n); starts=[]; off=0
    for a in parts:
        starts.extend([off]*a);off+=a
    for i in range(n):
        for j in range(n):
            if i != j and starts[i]!=starts[j]:
                out[i,j]=-1;out[i,i]+=1
    return out

def direct(s,L,h):
    x=h*L
    num=sp.zeros(L.rows); den=sp.zeros(L.rows)
    power=sp.eye(L.rows)
    for k,q in enumerate(coefficients(s)):
        num+=q*((-1)**k)*power
        den+=q*power
        power=power*x
    return den.inv()*num

# Exact Padé order and coefficientwise monotonicity evidence for many stages.
for s in range(1,29):
    qs=coefficients(s)
    E=sum(qs[2*j]*z**j for j in range((s//2)+1))
    O=sum(qs[2*j+1]*z**j for j in range((s+1)//2))
    W=sp.Poly(sp.expand(sp.diff(E,z)*O-E*sp.diff(O,z)),z)
    assert all(c>=0 for c in W.all_coeffs());checks+=1
    # The defining [s/s] approximant matches exp(-z) through order 2s.
    Q=sum(q*z**j for j,q in enumerate(qs))
    residual=sp.series(sp.exp(-z)*Q-Q.subs(z,-z),z,0,2*s+1).removeO()
    assert sp.expand(residual)==0;checks+=1
    for j in range((s-1)//2):
        r0=qs[2*j+1]/qs[2*j];r1=qs[2*j+3]/qs[2*j+2]
        assert r0>r1;checks+=1

# Exact rational functional calculus against spectral-entry formula.
for parts in ([1,1,1],[1,2],[1,3],[2,2],[1,2,3],[2,3],[1,1,3]):
    L=lap(parts)
    for s in range(1,7):
        for h in (sp.Rational(1,3),sp.Rational(3,2),sp.Integer(11)):
            S=spectral(s,parts,h)
            D=direct(s,L,h)
            assert S==D,(parts,s,h);checks+=1
            assert all(sum(S[i,j] for j in range(S.cols))==1 for i in range(S.rows));checks+=1
            assert all(S[i,j]>0 for i in range(S.rows) for j in range(S.cols) if i!=j);checks+=1
            if s%2==0:
                assert all(S[i,i]>0 for i in range(S.rows));checks+=1

# Exact odd-stage diagonal loss at a large finite step for each n>=3.
for s in (1,3,5,7,9):
    for parts in ([1,2],[2,2],[1,1,1],[1,2,3]):
        M=spectral(s,parts,sp.Integer(10**8))
        assert any(M[i,i]<0 for i in range(M.rows)),(s,parts);checks+=1

# Every stage remains nonnegative on the two-vertex complete graph.
for s in range(1,15):
    for h in (sp.Rational(1,7),sp.Integer(3),sp.Integer(100)):
        M=spectral(s,[1,1],h)
        assert all(M[i,j]>=0 for i in range(2) for j in range(2));checks+=1

print(f'PASS exact checks={checks}; stages 1..28 coefficient tests, graph spectral/direct identities, odd/even boundaries.')
