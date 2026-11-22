"""Exact-rational reproducibility checks for a two-level inverse-trace estimator.

Run: python verify.py. Uses Python's standard library only.
Finite checks corroborate, but do not replace, the universal algebraic proof.
"""
from fractions import Fraction as Q
from itertools import product


def mm(A, B):
    return [[sum((a*b for a,b in zip(row,col)), Q(0)) for col in zip(*B)] for row in A]


def tr(A):
    return sum((A[i][i] for i in range(len(A))), Q(0))


def examine(n,p,k):
    # Exact, dense, rational rotation of a two-level spectrum.
    q=n-p
    I=[[Q(i==j) for j in range(n)] for i in range(n)]
    H=[[I[i][j]-Q(2,n) for j in range(n)] for i in range(n)]
    D=[[Q(1 if i==j and i<p else k if i==j else 0) for j in range(n)] for i in range(n)]
    Di=[[Q(1 if i==j and i<p else Q(1,k) if i==j else 0) for j in range(n)] for i in range(n)]
    A=mm(mm(H,D),H); Ai=mm(mm(H,Di),H)
    assert mm(A,Ai)==I
    mu=tr(A)/n
    h=[[Q(2,1)/mu*I[i][j]-A[i][j]/mu**2 for j in range(n)] for i in range(n)]
    M=[[Ai[i][j]-h[i][j] for j in range(n)] for i in range(n)]
    alpha=Q(1)-Q(k)/mu**2
    beta=Q(k+1)/mu**2-Q(2)/mu
    assert all(M[i][j]==alpha*Ai[i][j]+beta*I[i][j] for i in range(n) for j in range(n))
    raw=[]; corr=[]
    for z in product([-1,1],repeat=n):
        r=sum((Q(z[i]*z[j])*Ai[i][j] for i in range(n) for j in range(n)),Q(0))
        c=Q(n)/mu+sum((Q(z[i]*z[j])*M[i][j] for i in range(n) for j in range(n)),Q(0))
        assert c-tr(Ai)==alpha*(r-tr(Ai))
        raw.append(r);corr.append(c)
    avg=lambda x:sum(x,Q(0))/len(x)
    var=lambda x:avg([(v-avg(x))**2 for v in x])
    assert avg(raw)==avg(corr)==tr(Ai)
    assert var(corr)==alpha**2*var(raw)
    return len(raw)


def flat_spike(n,k):
    # A=I+(k-1)J/n, exactly aligned with the all-ones direction.
    I=[[Q(i==j) for j in range(n)] for i in range(n)]
    A=[[I[i][j]+Q(k-1,n) for j in range(n)] for i in range(n)]
    Ai=[[I[i][j]+(Q(1,k)-1)/n for j in range(n)] for i in range(n)]
    mu=tr(A)/n
    alpha=Q(1)-Q(k)/mu**2
    raw=[];corr=[]
    for z in product([-1,1],repeat=n):
        rr=sum((Q(z[i]*z[j])*Ai[i][j] for i in range(n) for j in range(n)),Q(0))
        # One-node Hermite correction, using actual matrix products.
        cc=Q(n)/mu+sum((Q(z[i]*z[j])*(Ai[i][j]-Q(2)/mu*I[i][j]+A[i][j]/mu**2)
                         for i in range(n) for j in range(n)),Q(0))
        assert cc-tr(Ai)==alpha*(rr-tr(Ai))
        raw.append(rr);corr.append(cc)
    mean=lambda vals:sum(vals,Q(0))/len(vals)
    var=lambda vals:mean([(x-mean(vals))**2 for x in vals])
    vr=Q(2)*(Q(1)-Q(1,k))**2*Q(n-1,n)
    assert var(raw)==vr
    assert var(corr)==alpha**2*vr
    return len(raw)


def main():
    cases=0; checks=0
    for n in range(2,9):
        for p in range(1,n):
            for k in (2, n+1):
                checks+=examine(n,p,k);cases+=1
        for k in (2,max(3,n-1),(n-1)**2 if n>=3 else 4,3*n):
            checks+=flat_spike(n,k);cases+=1
    # Critical transitions at the first dimension and spectral contrast.
    assert (Q(1)-Q(6)/Q(12,7)**2)**2==Q(625,576)
    assert Q(1)-Q(36)/Q(6)**2==0
    assert Q(6)*Q(25,144)**2+Q(25,24)**2==Q(4375,3456)
    assert (Q(4375,3456))/(Q(217,36))==Q(625,2976)
    # At n=6 no admissible p/q exceeds 3+2sqrt(2); n=7,p=6,q=1 does.
    assert 36 < 8*5 and 49 > 8*6
    # n=7, one spike, exact inflation window 9/2<k<8.
    assert (Q(6)+Q(9,2))**2==Q(49,2)*Q(9,2)
    assert (Q(6)+Q(8))**2==Q(49,2)*Q(8)
    print('VERIFY_OK |',cases,'exact matrix families |',checks,'exhaustive sign-vector comparisons')

if __name__=='__main__':
    main()
