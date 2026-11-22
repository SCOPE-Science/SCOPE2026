"""Direct integer prefix-count checks and independent spectral-profile checks.
This file is scientific verification for an exact logarithmic fluctuation law."""
from bisect import bisect_right
from math import sqrt, log, floor
from itertools import product
from decimal import Decimal, localcontext


def raw_lengths(d, stages):
    ell = {-1:1,0:1}
    for i in range(1,stages+1):
        ell[i] = d[(i-1)%len(d)]*ell[i-1]+ell[i-2]
    return ell


def positive_theta(d, stages):
    ell = raw_lengths(d, stages)
    return sorted(j*ell[i-1]+ell[i-2]-2 for i in range(1,stages+1) for j in range(1,d[(i-1)%len(d)]+1) if (i,j)!=(1,1))


def spectral(d):
    k=len(d)
    ell=raw_lengths(d,2*k+1)
    # B=M(d_k)...M(d_1), obtained via column (ell_k,ell_{k-1})
    # trace of B from explicit integer matrix multiplication
    B=((1,0),(0,1))
    for a in d:
        M=((a,1),(1,0))
        B=((M[0][0]*B[0][0]+M[0][1]*B[1][0],M[0][0]*B[0][1]+M[0][1]*B[1][1]),(M[1][0]*B[0][0]+M[1][1]*B[1][0],M[1][0]*B[0][1]+M[1][1]*B[1][1]))
    tr=B[0][0]+B[1][1]; det=(-1)**k
    lam=(tr+sqrt(tr*tr-4*det))/2
    mu=det/lam
    dat=[]
    for r in range(1,k+1):
        for j in range(1,d[r-1]+1):
            v0=j*ell[r-1]+ell[r-2]
            v1=j*ell[k+r-1]+ell[k+r-2]
            c=(v1-mu*v0)/(lam-mu)
            e=(lam*v0-v1)/(lam-mu)
            dat.append((r,j,c,e,v0,v1))
    cstar=dat[0][2]
    z=[log(v[2]/cstar)/log(lam) for v in dat]
    assert all(z[i+1]>z[i]+1e-12 for i in range(len(z)-1)),(d,z)
    assert 0<=z[0]<1e-12 and z[-1]<1,(d,z)
    return lam,mu,dat,z


def prediction(d,N,lam,dat,z):
    cstar=dat[0][2]
    x=log((N+2)/cstar)/log(lam)
    q=floor(x)
    t=x-q
    m=bisect_right(z,t)
    # predicted count ignores exponentially small negative-eigenvalue terms
    return q*len(z)+m-1



def direct_palindromic_closures(d, count):
    # Independent literal-word oracle, using only iterated palindromic closure.
    p = ''
    lengths = []
    ix = 0
    remaining = d[0]
    for _ in range(count):
        symbol = '0' if ix % 2 == 0 else '1'
        w = p + symbol
        j = max(t for t in range(1, len(w)+1) if w[-t:] == w[-t:][::-1])
        p = w + w[:-j][::-1]
        assert p == p[::-1]
        lengths.append(len(p))
        remaining -= 1
        if remaining == 0:
            ix += 1
            remaining = d[ix % len(d)]
    return lengths

def run():
    samples=[[1],[2],[3],[4],[1,1],[1,2],[2,1],[1,3],[2,2],[1,2,3],[3,1,2],[1,1,2,3]]
    totals=0
    for d in samples:
        lam,mu,dat,z=spectral(d)
        count = min(12, 3*len(d))
        closed = direct_palindromic_closures(d,count)
        expected = positive_theta(d, count)[:count]
        # Some directive blocks have >1 letters, so use enough stage blocks.
        expected = positive_theta(d, count+1)[:count]
        assert closed == expected,(d,closed,expected)
        th=positive_theta(d,180)
        exceptions=[]
        for N in range(1,30001):
            actual=bisect_right(th,N)
            pred=prediction(d,N,lam,dat,z)
            if actual!=pred:
                exceptions.append((N,actual,pred))
                # A mismatch must be within distance 2 of an actual threshold;
                # this follows for q sufficiently large and is checked directly here.
                assert any(abs((N+2)-(t+2))<=2 for t in th[max(0,actual-2):actual+3]),(d,N,actual,pred)
        totals+=30000
        print('d=',d,'S=',len(z),'lambda=',round(lam,8),'phases=',[round(x,8) for x in z], 'mismatches=',len(exceptions),'examples=',exceptions[:5])
        # Independently verify integer exact closed form for every recorded
        # palindromic-prefix length at k full periods using matrix arithmetic.
        for q in range(0,14):
            for i,(r,j,c,e,v0,v1) in enumerate(dat):
                exact=j*raw_lengths(d,(q+1)*len(d))[q*len(d)+r-1]+raw_lengths(d,(q+1)*len(d))[q*len(d)+r-2]
                approx=c*lam**q+e*mu**q
                assert abs(exact-approx)<=max(1e-5,exact*1e-12),(d,q,r,j,exact,approx)
        # F(t) value distribution mean from uniform phase
        mean=len(z)/2 -1-sum(z)
        # numerical midpoint quadrature consistency check
        def F(t): return bisect_right(z,t)-1-len(z)*t
        n=100000
        quad=sum(F((i+0.5)/n) for i in range(n))/n
        assert abs(quad-mean)<0.001,(d,quad,mean)
        if d in ([1],[2],[1,2]):
            X=30000
            u=(log((X+2)/dat[0][2])/log(lam))%1
            def rho(t):
                return log(lam)*lam**(t-u)*(1/(lam-1)+(1 if t <= u else 0))
            weighted_mean=sum(F((i+.5)/n)*rho((i+.5)/n) for i in range(n))/n
            empirical_mean=sum(bisect_right(th,N)-len(z)*log((N+2)/dat[0][2])/log(lam) for N in range(1,X+1))/X
            assert abs(empirical_mean-weighted_mean)<.025,(d,empirical_mean,weighted_mean)
            print('ordinary_phase_law',d,'phase',round(u,6),'mean_pred',round(weighted_mean,6),'mean_actual',round(empirical_mean,6))
    print('PASS direct_palindromic_closure_cases=',len(samples),'direct_integer_checks=',totals,'spectral_cases=',sum(len(spectral(d)[2])*14 for d in samples))

if __name__=='__main__':run()
