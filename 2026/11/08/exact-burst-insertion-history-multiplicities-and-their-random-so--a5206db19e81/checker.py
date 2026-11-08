"""Reproducibility checks for the burst-insertion history multiplicity law.

Run with Python 3, using only the standard library.
"""
from itertools import product
from collections import Counter
from fractions import Fraction

def outcomes(y, q, b):
    m=len(y)
    locations={}
    for i in range(m+1):
        for block in product(range(q), repeat=b):
            x=y[:i]+block+y[i:]
            locations.setdefault(x,set()).add(i)
    return locations

def predicted(y,q,b):
    m=len(y)
    t={m+2:0,m+3:0}
    for s in range(1,m+2):
        if s<=b+1:
            t[s]=(m-s+2)*q**(b-s+1)
        else:
            t[s]=sum(all(y[k]==y[k+b] for k in range(i,i+s-1-b)) for i in range(m-s+2))
    return {s:t[s]-2*t[s+1]+t[s+2] for s in range(1,m+2)}

def independent_run_max(y,b):
    m=len(y)
    matches=[int(y[i]==y[i+b]) for i in range(max(0,m-b))]
    run=best=0
    for e in matches:
        run=(run+1)*e
        best=max(best,run)
    return min(b+1,m+1)+best

def main():
    tested=0
    totalwords=0
    for q in (2,3):
        for b in range(1,5):
            for m in range(0,6 if q==2 else 5):
                for y in product(range(q),repeat=m):
                    out=outcomes(y,q,b)
                    observed=Counter(len(loc) for loc in out.values())
                    formula=predicted(y,q,b)
                    assert all(loc==set(range(min(loc),max(loc)+1)) for loc in out.values())
                    assert all(observed[s]==formula[s] for s in formula), (q,b,y,observed,formula)
                    assert len(out)==q**b+m*q**(b-1)*(q-1)
                    assert max(observed)==independent_run_max(y,b)
                    assert sum(s*v for s,v in formula.items())==(m+1)*q**b
                    tested+=1
                    totalwords+=len(out)
    # Independently check the averaged spectrum and the exact longest-run law.
    for q in (2,3):
        for b in (1,2,3):
            for m in range(0,7 if q==2 else 5):
                sample=list(product(range(q),repeat=m))
                counts=Counter()
                maxfreq=Counter()
                for y in sample:
                    pp=predicted(y,q,b)
                    for s,c in pp.items():counts[s]+=c
                    maxfreq[independent_run_max(y,b)]+=1
                for s in range(1,m+2):
                    expectation=Fraction(counts[s],len(sample))
                    target=(Fraction(q**b, q**m) if s==m+1 else Fraction((q-1)*((m-s+2)*(q-1)+2)) * Fraction(q)**(b-s-1))
                    assert expectation==target,(q,b,m,s,expectation,target)
                n=max(0,m-b)
                p=Fraction(1,q)
                for r in range(1,n+2):
                    a=[Fraction(1) for _ in range(min(r,n+1))]
                    for t in range(r,n+1):
                        a.append((1-p)*sum(p**j*a[t-j-1] for j in range(r)))
                    probability=sum(v for h,v in maxfreq.items() if h<min(b+1,m+1)+r)
                    assert Fraction(probability,len(sample))==a[n]
    print('PASS',tested,'centers;',totalwords,'distinct insertion outputs checked; averaged laws and run recurrence verified')
if __name__=='__main__':main()
