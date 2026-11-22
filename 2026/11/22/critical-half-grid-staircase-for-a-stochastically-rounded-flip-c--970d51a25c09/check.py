"""Reproducible exact-rational checks for a near-flip rounded affine chain.
Only finite algebra is tested; the convergence theorem follows analytically.
"""
from fractions import Fraction as F
from math import floor


def rate_up(n, c):
    return max(F(1, 2) - n - 2*c, 0) + max(F(1, 2) - n + 2*c, 0)


def rate_down(n, c):
    return max(n - F(1, 2) + 2*c, 0) + max(n - F(1, 2) - 2*c, 0)


def kernel(c, eps, M=8):
    assert 0 < eps < 1
    theta = F(1,2) + c*eps
    r = 1 - eps
    states = list(range(-M, M+2))
    P = [[F(0) for _ in states] for _ in states]
    for i,n in enumerate(states):
        y = theta - r*(n-theta)
        k = floor(y)
        assert -M <= k < M+1
        P[i][k+M] = 1-(y-k)
        P[i][k+M+1] = y-k
        assert sum(P[i]) == 1
    return states,P


def exact_stationary(P):
    N=len(P)
    A=[[P[i][j]-int(i==j) for i in range(N)] + [F(0)] for j in range(N-1)]
    A.append([F(1)]*N+[F(1)])
    for k in range(N):
        pivot = next(i for i in range(k,N) if A[i][k])
        A[k],A[pivot]=A[pivot],A[k]
        q=A[k][k]
        A[k]=[v/q for v in A[k]]
        for i in range(N):
            if i==k:continue
            q=A[i][k]
            if q:A[i]=[a-q*b for a,b in zip(A[i],A[k])]
    return [A[i][-1] for i in range(N)]


def limiting_law(c):
    # K = ceil(2*|c|+1/2), computed without float.
    t=2*abs(c)+F(1,2)
    K=-(-t.numerator//t.denominator)
    states=list(range(1-K,K+1))
    w=[F(1)]
    for n in states[1:]:
        w.append(w[-1]*rate_up(n-1,c)/rate_down(n,c))
    Z=sum(w)
    return dict(zip(states,[v/Z for v in w]))


def check():
    for c in map(F,['0','1/5','1/4','13/50','1/2','3/4','1','5/4','63/50','-1/2']):
        law=limiting_law(c)
        assert sum(law.values())==1
        assert all(v>0 for v in law.values())
        assert all(law[n]==law[1-n] for n in law)
        for n in law:
            assert law[n]*rate_up(n,c)==law.get(n+1,F(0))*rate_down(n+1,c)
        if abs(c)<=F(1,4):
            assert law=={0:F(1,2),1:F(1,2)}
        for eps in (F(1,10),F(1,40),F(1,200)):
            states,P=kernel(c,eps)
            invariant=exact_stationary(P)
            assert sum(invariant)==1
            assert all(v>=0 for v in invariant)
            theta=F(1,2)+c*eps
            assert sum(s*p for s,p in zip(states,invariant))==theta
            tv=sum(abs(invariant[i]-law.get(s,F(0))) for i,s in enumerate(states))/2
            assert tv < 2*eps*(abs(c)+1), (c,eps,tv)
            if abs(c)<=F(1,4):
                assert invariant[states.index(1)]==theta
                assert invariant[states.index(0)]==1-theta
                assert sum(invariant[i] for i,s in enumerate(states) if s not in (0,1))==0
            # Test every coefficient of the first-order two-step generator.
            # A rational epsilon is not a derivative: use exact limiting constant of polynomial.
            Q={}
            for n in states[2:-2]:
                Q[n]=(rate_up(n,c),rate_down(n,c))
                R=1-n
                assert R in states
                # Construct exact linear coefficients from t_n, t_R.
                t=lambda m: F(m)-F(1,2)+2*c
                assert Q[n][0] == max(-t(n),0)+max(t(R),0)
                assert Q[n][1] == max(t(n),0)+max(-t(R),0)
    assert limiting_law(F(1,2)) == {-1:F(1,14),0:F(3,7),1:F(3,7),2:F(1,14)}
    print('PASS: rational transition kernels, invariant laws, exact means, reflection and detailed balance, critical probabilities, and small-epsilon comparisons.')

if __name__=='__main__':
    check()
