"""Independent density-resolved and rule-number consistency checks."""
from itertools import product
from collections import Counter
from math import gcd

# Independent local-triple description (no flux array).
def tick(v):
    n=len(v)
    return tuple(v[j] + min(v[(j-1)%n], 2-v[j])
                 - min(v[j], 2-v[(j+1)%n]) for j in range(n))

def mobius(m):
    if m==1:return 1
    p=2;sign=1
    while p*p<=m:
        if m%p==0:
            m//=p;sign=-sign
            if m%p==0:return 0
        p+=1
    return -sign if m>1 else sign

def low_counts(n):
    counts=Counter()
    for v in product(range(3),repeat=n):
        if all(v[j]+v[(j+1)%n]<=2 for j in range(n)):
            counts[sum(v)]+=1
    return counts

def recurrent_mass_counts(n):
    L=low_counts(n)
    return Counter({k:L[k]+L[2*n-k]-(1+2*(n%2==0) if k==n else 0)
                    for k in range(2*n+1)})

def masses_for_temporal_period(n,d):
    poly=Counter()
    for e in range(1,d+1):
        if d%e:continue
        factor=mobius(d//e)
        if not factor:continue
        for mass,count in recurrent_mass_counts(e).items():
            poly[mass*(n//e)]+=factor*count
    for k in poly:
        assert poly[k]%d==0
        poly[k]//=d
    return +poly

nchecked=0
for n in range(1,10):
    observed=Counter(); byperiod=Counter(); visited=set()
    for x in product(range(3),repeat=n):
        if x in visited:continue
        traj=[];positions={};y=x
        while y not in positions and y not in visited:
            positions[y]=len(traj)
            traj.append(y);y=tick(y)
        if y in positions:
            cycle=traj[positions[y]:]
            p=len(cycle)
            for z in cycle:
                observed[sum(z)]+=1
                byperiod[(p,sum(z))]+=1
            visited.update(traj)
        else:
            visited.update(traj)
    expected=recurrent_mass_counts(n)
    assert observed==+expected,(n,observed,expected)
    for d in range(1,n+1):
        if n%d:continue
        expected_cycles=masses_for_temporal_period(n,d)
        for k,v in expected_cycles.items():
            assert byperiod[(d,k)]//d==v,(n,d,k,v,byperiod[(d,k)])
        assert set(k for (p,k),v in byperiod.items() if p==d and v) == set(expected_cycles)
    nchecked+=1
    print('n',n,'recurrent mass polynomial coefficients',sorted(observed.items()),'temporal orbit counts', {d:sum(masses_for_temporal_period(n,d).values()) for d in range(1,n+1) if n%d==0})
# Match the standard enumeration number for the capacity-two local rule.
rule_number=sum((b+min(a,2-b)-min(b,2-c))*3**(9*a+3*b+c)
                for a,b,c in product(range(3),repeat=3))
assert rule_number==6171534259461
print('All independent checks passed; exact rule number',rule_number,'ring lengths',nchecked)
