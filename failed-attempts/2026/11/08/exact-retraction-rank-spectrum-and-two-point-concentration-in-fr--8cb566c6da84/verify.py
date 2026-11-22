"""Finite-field direct checks and independent arithmetic for free class-two Lie retractions.
Run: python3 verify.py   (Python 3 standard library only).
"""
from collections import Counter
from itertools import combinations, product
from math import comb, floor, sqrt


def gaussian(n, r, q):
    num = 1
    den = 1
    for j in range(1, r + 1):
        num *= q ** (n-r+j) - 1
        den *= q**j - 1
    assert num % den == 0
    return num // den


def predicted(n, q):
    out = {}
    for r in range(n+1):
        h = r * (comb(n,2)-comb(r,2)) + (n-r)*comb(r,2)
        out[r + comb(r,2)] = gaussian(n,r,q) * q**(r*(n-r)+h)
    return out


def apply(cols, v, q):
    d = len(cols)
    return tuple(sum(cols[j][i]*v[j] for j in range(d)) % q for i in range(d))


def rank(cols, q):
    d=len(cols)
    A=[[cols[j][i] % q for j in range(d)] for i in range(d)]
    piv=0
    for j in range(d):
        k=next((i for i in range(piv,d) if A[i][j]),None)
        if k is None: continue
        A[piv],A[k]=A[k],A[piv]
        inv=pow(A[piv][j],-1,q)
        A[piv]=[(v*inv)%q for v in A[piv]]
        for i in range(d):
            if i != piv and A[i][j]:
                c=A[i][j]
                A[i]=[(a-c*b)%q for a,b in zip(A[i],A[piv])]
        piv+=1
        if piv==d:break
    return piv


def wedge(u, v, pairs, q):
    return tuple((u[i]*v[j]-u[j]*v[i])%q for i,j in pairs)


def brute(n,q):
    pairs=list(combinations(range(n),2)); z=len(pairs); d=n+z
    counts=Counter(); idem=0
    for a in product(range(q),repeat=n*n):
        acols=[a[n*i:n*(i+1)] for i in range(n)]
        ccols=[wedge(acols[i],acols[j],pairs,q) for i,j in pairs]
        # Test the quotient projection before trying all central offsets.
        if any(apply(acols,acols[j],q)!=acols[j] for j in range(n)):continue
        if any(apply(ccols,ccols[j],q)!=ccols[j] for j in range(z)):continue
        for b in product(range(q),repeat=n*z):
            bcols=[b[z*i:z*(i+1)] for i in range(n)]
            pcols=[tuple(acols[j])+tuple(bcols[j]) for j in range(n)] + [tuple([0]*n)+tuple(ccols[j]) for j in range(z)]
            # Independently compare each generator image to its second iterate.
            if all(apply(pcols,pcols[j],q)==pcols[j] for j in range(d)):
                assert all(pcols[n+t][n:] == wedge(pcols[i][:n], pcols[j][:n], pairs, q)
                           for t,(i,j) in enumerate(pairs))
                idem+=1
                counts[rank(pcols,q)]+=1
    expected=predicted(n,q)
    assert dict(counts)=={k:v for k,v in expected.items() if v},(n,q,counts,expected)
    print('DIRECT',n,q,dict(sorted(counts.items())),'TOTAL',idem)



def shear_orbit_checks(n, q):
    pairs=list(combinations(range(n),2)); z=len(pairs)
    for r in range(n+1):
        in_u=[int(i<r and j<r) for i,j in pairs]
        cnt=0
        for b in product(range(q),repeat=n*z):
            bcols=[b[z*i:z*(i+1)] for i in range(n)]
            ok=True
            for i in range(n):
                for a in range(z):
                    if i<r and in_u[a] and bcols[i][a]:ok=False
                    if i>=r and not in_u[a] and bcols[i][a]:ok=False
            if not ok:continue
            cnt+=1
            ccols=[tuple(v if i<r else -v % q for v in bcols[i]) for i in range(n)]
            recovered=[]
            for i in range(n):
                rec=tuple(((ccols[i][a] if i<r else 0) - in_u[a]*ccols[i][a])%q for a in range(z))
                recovered.append(rec)
            assert recovered==bcols,(n,q,r)
        h=r*(comb(n,2)-comb(r,2))+(n-r)*comb(r,2)
        assert cnt==q**h,(n,q,r,cnt,h)
    print('SHEAR_ORBITS_OK',n,q)

def mode_checks(q):
    for n in [3,4,5,6,8,10,20,50,100]:
        weights=predicted(n,q)
        N=sum(weights.values())
        rstar=(n-2+sqrt(7*n*n+8*n+4))/6
        k=floor(rstar)
        inside=sum(weights[r*(r+1)//2] for r in {k,k+1} if 0<=r<=n)
        p_out=(N-inside)/N
        assert p_out < 1.0 if n<8 else p_out < 0.002,(n,p_out)
        if n>=20:
            assert p_out<q**(-n//2),(n,p_out)
        print('MODE',q,n,'r*',round(rstar,6),'outside',format(p_out,'.4g'))

if __name__=='__main__':
    for n,q in [(2,2),(2,3),(3,2)]: brute(n,q)
    shear_orbit_checks(3,2)
    for q in [2,3]: mode_checks(q)
    print('VERIFY_OK')
