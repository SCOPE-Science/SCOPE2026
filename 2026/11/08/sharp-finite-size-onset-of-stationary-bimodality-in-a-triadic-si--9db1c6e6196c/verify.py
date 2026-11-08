"""Exact finite-state checks for the triadic SIS importation mode threshold."""
from fractions import Fraction as Q
from math import floor

def rates(n, recovery, importation, triadic):
    births = [Q(n-i) * (importation + triadic*Q(i*(i-1),(n-1)*(n-2))) for i in range(n)]
    deaths = [recovery*i for i in range(n+1)]
    return births, deaths

def stationary(n, recovery, importation, triadic):
    b,d = rates(n,recovery,importation,triadic)
    w = [Q(1)]
    for i in range(n):
        w.append(w[-1] * b[i] / d[i+1])
    z = sum(w)
    return [x/z for x in w]

def critical(n,recovery,importation):
    m=n//2
    return Q((n-1)*(n-2),m*(m+1)) * (recovery*Q(m+2,n-m-1)-importation)

def candidates(n,recovery,importation):
    return [Q((n-1)*(n-2),i*(i-1)) * (recovery*Q(i+1,n-i)-importation) for i in range(2,n)]

def modal_plateaus(v):
    """Maximal constant intervals exceeding their immediate external neighbours."""
    found=[]
    start=0
    while start < len(v):
        end=start
        while end+1<len(v) and v[end+1]==v[start]:
            end+=1
        if (start==0 or v[start]>v[start-1]) and (end==len(v)-1 or v[end]>v[end+1]):
            found.append((start,end))
        start=end+1
    return found

def check_detailed_balance(n,mu,eps,gamma):
    b,d=rates(n,mu,eps,gamma)
    pi=stationary(n,mu,eps,gamma)
    assert sum(pi)==1 and all(x>0 for x in pi)
    assert all(pi[i]*b[i] == pi[i+1]*d[i+1] for i in range(n))
    # Independent stationarity check using all incoming/outgoing currents.
    for i in range(n+1):
        inflow = (pi[i-1]*b[i-1] if i else Q(0)) + (pi[i+1]*d[i+1] if i<n else Q(0))
        outflow = pi[i]*((b[i] if i<n else Q(0))+d[i])
        assert inflow==outflow
    return pi

cases=0
for n in range(3,30):
    for mu in [Q(1),Q(3,2)]:
        for a in [Q(1,10),Q(1,2),Q(9,10)]:
            eps = a*mu/n
            threshold=critical(n,mu,eps)
            all_critical=candidates(n,mu,eps)
            assert threshold==min(all_critical)
            assert all_critical.index(threshold)==n//2-1
            for gamma in sorted(set([Q(0),threshold*Q(9,10),threshold,threshold*Q(11,10),threshold*4]+all_critical)):
                pi=check_detailed_balance(n,mu,eps,gamma)
                if gamma<threshold:
                    assert all(pi[i]>pi[i+1] for i in range(n))
                    assert modal_plateaus(pi)==[(0,0)]
                elif gamma==threshold:
                    assert all(pi[i]>=pi[i+1] for i in range(n))
                    j=n//2+1
                    assert pi[j]==pi[j+1]
                    assert modal_plateaus(pi)==[(0,0)]
                else:
                    modes=modal_plateaus(pi)
                    assert len(modes)==2 and modes[0]==(0,0) and modes[1][0]>=3
                    assert modes[1][1]-modes[1][0]<=1
                cases+=1

# In the vanishing-importation limit thresholds pair by parity.
for m in range(2,80):
    t_even=critical(2*m,Q(1),Q(0))
    t_odd=critical(2*m+1,Q(1),Q(0))
    exact=Q(2*(2*m-1)*(m+2),m*(m+1))
    assert t_even==t_odd==exact
    assert exact<=Q(21,5)
assert critical(8,Q(1),Q(0)) == critical(11,Q(1),Q(0)) == Q(21,5)
assert critical(8,Q(1),Q(1,32))==Q(1323,320)
print('VERIFY_OK',cases,'exact stationarity and mode tests; parity pairs and maximum checked')
