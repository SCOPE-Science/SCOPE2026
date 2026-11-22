"""Independent matrix tests for finite interlaced-character Gabor spectra.
Reproduces the formula from explicit time-frequency atoms, without using the proof's
coordinate eigenbasis.
"""
import itertools
import numpy as np

def check(p, m, phases, lmask):
    n = p*m
    j = np.arange(n)
    g = np.array([np.exp(2j*np.pi*phases[int(x % m)]*int(x // m)/p) for x in j])
    atoms=[]
    for a in range(p):
        for ell in lmask:
            atoms.append(np.exp(2j*np.pi*ell*j/n)*np.roll(g,m*a))
    v=np.column_stack(atoms) if atoms else np.zeros((n,0),complex)
    s=v@v.conj().T
    counts=[sum(l%p == a for l in lmask) for a in range(p)]
    predicted=sorted([p*p*c for c in counts for _ in range(m)])
    eigen=np.linalg.eigvalsh(s)
    assert np.max(np.abs(eigen-predicted))<1e-8,(p,m,phases,lmask,eigen,predicted)
    # Frame atoms must be individual eigenvectors of the frame operator.
    for col, ell in zip(atoms,[l for _ in range(p) for l in lmask]):
        c=counts[ell%p]
        assert np.linalg.norm(s@col-(p*p*c)*col)<1e-8,(p,m,phases,lmask)
    return 1

def main():
    tested=0
    for p in range(2,7):
        for m in range(1,min(p,3)+1):
            for phases in itertools.islice(itertools.permutations(range(p),m),0,5):
                for trial in range(21):
                    mask=[i for i in range(p*m) if ((i*9+trial*7+i*trial) % 19) < (trial%14)]
                    tested+=check(p,m,phases,mask)
    print('PASS explicit frame-matrix spectra and atom eigenvector checks:',tested,'cases')
if __name__=='__main__':main()

# Exact frequency-mask counts: independent explicit enumeration.
from math import comb

def count_tests():
    checks=0
    for p in range(2,5):
        for m in range(1,4):
            n=p*m
            if n>12:continue
            samples={k:[] for k in range(n+1)}
            for bits in range(1<<n):
                c=tuple(sum(bool(bits & (1<<i)) for i in range(a,n,p)) for a in range(p))
                samples[bits.bit_count()].append(c)
            for k,cs in samples.items():
                frame=sum(min(c)>0 for c in cs)
                # Direct binomial convolution coefficient.
                coeff=[1]
                for _ in range(p):
                    out=[0]*(len(coeff)+m)
                    for i,v in enumerate(coeff):
                        for j in range(1,m+1):out[i+j]+=v*comb(m,j)
                    coeff=out
                assert frame==coeff[k]
                if p<=k<=n:
                    q,r=divmod(k,p)
                    good=[c for c in cs if min(c)>0]
                    best=min(max(c)/min(c) for c in good)
                    expect=1 if r==0 else (q+1)/q
                    assert abs(best-expect)<1e-12
                    optimal=sum(abs(max(c)/min(c)-best)<1e-12 for c in good)
                    count=comb(p,r)*comb(m,q+1)**r*comb(m,q)**(p-r) if r else comb(m,q)**p
                    # If equal-condition (not just balanced) can happen, this assertion will detect it.
                    assert optimal==count,(p,m,k,optimal,count)
                checks+=1
    return checks
if __name__=='__main__': print('PASS exact mask-design count tests:',count_tests())
