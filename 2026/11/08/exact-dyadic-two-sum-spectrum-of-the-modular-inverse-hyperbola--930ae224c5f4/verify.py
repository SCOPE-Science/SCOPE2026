"""Finite exact checks for dyadic inverse-graph two-sum representations."""
from collections import Counter


def roots(m, delta):
    mod=1<<m
    return sum((z*z-delta)%mod==0 for z in range(mod))


def multiplicity(k,s,t):
    q=1<<k
    if s==0 or t==0:
        return q//2 if s==0 and t==0 else 0
    if s&1 or t&1:
        return 0
    h=(s & -s).bit_length()-1
    g=(t & -t).bit_length()-1
    if h!=g: return 0
    m=k-h
    mod=1<<m
    a=s//2
    u=s>>h
    v=t>>h
    delta=(a*a-u*pow(v,-1,mod))%mod
    return (1<<h)*roots(m,delta)


def square_count(n):
    if n==0:return 1
    if n%2==0:
        return ((1<<n)+8)//6
    return ((1<<(n-1))+5)//3


def image_size(k):
    if k==1:return 1
    if k==2:return 2
    if k==3:return 4
    return (1<<(k-2))*square_count(k-3) + ((1<<(2*k-6))+8)//3


def check(k):
    q=1<<k
    units=range(1,q,2)
    C=Counter()
    for x in units:
        rx=pow(x,-1,q)
        for y in units:
            C[((x+y)%q,(rx+pow(y,-1,q))%q)]+=1
    for s in range(q):
        for t in range(q):
            assert C[s,t]==multiplicity(k,s,t),(k,s,t,C[s,t],multiplicity(k,s,t))
    assert len(C)==image_size(k),(k,len(C),image_size(k))
    assert sum(C.values())==(q//2)**2
    if k>=4:
        assert sum(v*v for v in C.values())==3*(k-3)*q*q//2
    return k,len(C),sum(v*v for v in C.values()),dict(sorted(Counter(C.values()).items()))

if __name__=='__main__':
    for k in range(1,10):
        print('OK',check(k))
    print('VERIFY_OK levels=1..9 exact_target_comparisons=',sum(4**k for k in range(1,10)), 'sumset_cardinalities=PASS energy_crosscheck=PASS')
