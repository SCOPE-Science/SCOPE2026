"""Finite Fourier sampling on checksum hyperplanes: independent numerical/combinatorial tests."""
from itertools import product
from math import factorial, comb
import numpy as np

def run(dims,n,r):
    # finite abelian alphabet A = product_j Z/dims[j]Z
    alphabet=list(product(*[range(d) for d in dims])); q=len(alphabet)
    coeff=list(product(alphabet,repeat=n))
    site=[x for x in coeff if all(sum(t[j] for t in x)%dims[j]==0 for j in range(len(dims)))]
    freq=[a for a in coeff if sum(aa!=alphabet[0] for aa in a)<=r]
    M=np.empty((len(site),len(freq)),complex)
    for i,x in enumerate(site):
        for j,a in enumerate(freq):
            z=sum(sum(x[k][h]*a[k][h]/dims[h] for h in range(len(dims))) for k in range(n))
            M[i,j]=np.exp(2j*np.pi*z)/np.sqrt(len(site))
    eigen=np.linalg.eigvalsh(M.conj().T@M)
    # orbit cosets by constant additive shift; each orbit is of size q
    unseen=set(coeff); mult=[]
    while unseen:
        a=next(iter(unseen)); orbit={tuple(tuple((a[k][j]+c[j])%dims[j] for j in range(len(dims))) for k in range(n)) for c in alphabet}
        assert len(orbit)==q
        unseen-=orbit
        t=sum(w in freq for w in orbit)
        if t: mult.append(t)
    expected=sorted([0.]*(len(freq)-len(mult))+[float(t) for t in mult])
    err=float(np.max(abs(np.sort(eigen)-expected)))
    assert err<1e-8,(dims,n,r,err)
    s=n-r
    max_t=min(q,n//s)
    assert max(mult)==max_t,(dims,n,r,max(mult),max_t)
    # count distribution by multinomial occupancy using word compositions
    counts=[0]*(q+1)
    for a in coeff:
        tally={sym:0 for sym in alphabet}
        for sym in a:tally[sym]+=1
        t=sum(v>=s for v in tally.values())
        counts[t]+=1
    assert all(c%q==0 for c in counts)
    observed=[mult.count(t) for t in range(q+1)]
    assert observed[1:]==[counts[t]//q for t in range(1,q+1)]
    if n%2==0 and r==n//2:
        assert mult.count(2)==(q-1)*comb(n,n//2)//2
        assert max_t==2
    return len(site),len(freq),len(mult),max_t,err

if __name__=='__main__':
    cases=[]
    for dims, ns in [((2,),range(2,8)),((3,),range(2,6)),((4,),range(2,5)),((2,2),range(2,5)),((5,),range(2,4)),((2,3),range(2,4))]:
        for n in ns:
            for r in range(n):
                cases.append((dims,n,r,run(dims,n,r)))
    print('CHECKSUM_FOURIER_SPECTRUM_PASS', 'cases=',len(cases),'max_residual=',max(k[-1][-1] for k in cases))
    for dims,n,r,v in cases[:8]: print(dims,n,r,v)
