from itertools import product
from collections import Counter

def phi_pq(p,q):
    n=(p-1)*(q-1); a=[0]*(p*(q-1)+1)
    for j in range(q): a[j*p]=1
    b=[1]*q; out=[0]*(n+1)
    for k in range(n,-1,-1):
        out[k]=a[k+q-1]
        for i in range(q): a[k+i]-=out[k]
    assert not any(a)
    return out

def test(p,q,m):
    a=phi_pq(p,q);d=len(a)-1
    state_set=set();hist=Counter(); nstates=m**d
    for state in product(range(m),repeat=d):
        if state in state_set:continue
        s=state; orbit=[]
        while s not in state_set:
            state_set.add(s);orbit.append(s)
            s=tuple([( -a[0]*s[-1])%m]+[(s[i-1]-a[i]*s[-1])%m for i in range(1,d)])
        assert s==state
        hist[len(orbit)]+=1
    gp=__import__('math').gcd(p,m);gq=__import__('math').gcd(q,m)
    assert hist == {k:v for k,v in {1:1,p:(gq**(p-1)-1)//p,q:(gp**(q-1)-1)//q,p*q:(m**d-gq**(p-1)-gp**(q-1)+1)//(p*q)}.items() if v}
    assert sum(k*v for k,v in hist.items())==nstates
    print('ORBIT_CENSUS_OK',p,q,m,nstates,sorted(hist.items()),flush=True)
for args in [(3,5,2),(3,5,3),(3,5,5),(3,7,2),(3,7,3)]:test(*args)
print('VERIFY_OK finite_checks_only=True analytic_proof_separate=True independent_audit=False')
