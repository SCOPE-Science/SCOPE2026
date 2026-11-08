"""Direct exhaustive transition-graph isomorphism and stationary bottleneck check."""
from itertools import product
from fractions import Fraction
# Independent implementation of the self-inclusive minority flip condition.
def update(state,v,m):
    b=lambda j: (state>>j)&1
    if v==0:
        d=2*m
        matching=sum(b(j)==b(0) for j in range(1,d+1))
    else:
        mate=v+1 if v%2 else v-1
        d=2
        matching=(b(0)==b(v))+(b(mate)==b(v))
    return state ^ (1<<v) if matching*2>=d else state

def encoded(h,z):
    # z_i=0 if both peripheral oppose hub, 1 if first matches hub,
    # 2 if second matches hub
    bit=h
    for i,st in enumerate(z):
        a,b=((1-h,1-h) if st==0 else ((h,1-h) if st==1 else (1-h,h)))
        bit|=a<<(2*i+1);bit|=b<<(2*i+2)
    return bit

for m in range(1,6):
    N=2*m+1
    states={encoded(h,z):(h,z) for h in (0,1) for z in product(range(3),repeat=m)}
    assert len(states)==2*3**m
    boundary=0
    for s,(h,z) in states.items():
        for v in range(N):
            t=update(s,v,m)
            if t==s: continue
            assert t in states
            h2,z2=states[t]
            if v==0:
                assert h2!=h and 0 not in z and z2==tuple(3-x for x in z)
                boundary+=1
            else:
                i=(v-1)//2
                assert h2==h and all(z2[j]==z[j] for j in range(m) if j!=i)
                assert {z[i],z2[i]} in ({0,1},{0,2})
    assert boundary==2**(m+1)
    phi=Fraction(2**m,3**m*N)
    assert Fraction(boundary,2*3**m*N)==phi
    print('m',m,'recurrent',len(states),'oriented_hub_edges',boundary,'phi',phi,'lower_bound_tmix',Fraction(1,4*phi))
print('PRODUCT AND CONDUCTANCE CHECK PASS')
