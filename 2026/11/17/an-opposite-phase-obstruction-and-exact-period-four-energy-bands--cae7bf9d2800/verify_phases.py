"""Independent firing-word inequality intersection versus four-part multinomial census."""
from collections import Counter
from itertools import product
from math import factorial


def poly_product(powered):
    d=Counter({0:1})
    for width,multiplicity in powered:
        for _ in range(multiplicity):
            nxt=Counter()
            for k,v in d.items():
                for shift in range(width):
                    nxt[k+shift]+=v
            d=nxt
    return d


def phase_formula(n):
    out=Counter()
    for a in range(1,n-2):
      for b in range(1,n-a-1):
       for c in range(1,n-a-b):
        d=n-a-b-c
        if d<1:continue
        ns=[a,b,c,d]
        mult=factorial(n)
        for k in ns:mult//=factorial(k)
        B=n*(n-1)-sum(ns[i]*ns[j] for i in range(4) for j in range(i+1,4))
        p=poly_product([(ns[(j-1)%4],ns[j]) for j in range(4)])
        for k,coeff in p.items():out[B+k]+=mult*coeff
    return out


def inequality_enumeration(n):
    out=Counter()
    # Label every vertex independently by its unique firing instant.
    for phases in product(range(4),repeat=n):
        totals=[phases.count(i) for i in range(4)]
        if any(v==0 for v in totals):continue
        intervals=[]
        for f in phases:
            delta=0; lower=0; upper=2*n-3
            for t in range(4):
                if t==f:lower=max(lower,n-1-delta)
                else:upper=min(upper,n-2-delta)
                delta+=totals[t]-n*(t==f)
            if lower>upper:break
            intervals.append((lower,upper))
        if len(intervals)!=n:continue
        coeffs=Counter({0:1})
        for l,u in intervals:
            nxt=Counter()
            for base,v in coeffs.items():
                for x in range(l,u+1):nxt[base+x]+=v
            coeffs=nxt
        out.update(coeffs)
    return out

for n in range(4,9):
    a=phase_formula(n);b=inequality_enumeration(n)
    assert a==b,(n, [(k,a[k],b[k]) for k in sorted(set(a)|set(b)) if a[k]!=b[k]][:5])
    L=n*(n-1)-3*n*n//8; U=(n-1)*(n-2)
    assert set(a)==set(range(L,U+1))
    n4,rem=divmod(n,4)
    lowCoeff=factorial(4)//(factorial(rem)*factorial(4-rem))*factorial(n)//(factorial(n4+1)**rem*factorial(n4)**(4-rem))
    assert a[L]==lowCoeff,(n,a[L],lowCoeff)
    maxCoeff=4*n*(n-1)*(2**(n-2)-n)+(24 if n==4 else 0)
    assert a[U]==maxCoeff,(n,a[U],maxCoeff)
    print('n',n,'phase1_states',sum(a.values()),'low_mass',L,'upper_mass',U,'low_coefficient',a[L],'edge_coefficient',a[U])
print('PHASE FORMULA PASS')
