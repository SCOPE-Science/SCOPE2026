"""Reproduce renewal-cover and Thue--Morse phase diagnostics (standard library)."""
from decimal import Decimal, getcontext
from itertools import product

getcontext().prec = 85
D=Decimal
ONE=D(1)
K=360
bits=[i.bit_count()%2 for i in range(K+1)]

def tm_sum(q):
    p=ONE; total=D(0)
    for i in range(1,K+1):
        p*=q
        if bits[i]:total+=p
    return total

def bisect_root(fun):
    lo=D('0.5');hi=D('0.65')
    assert fun(lo)<0 and fun(hi)>0
    for _ in range(300):
        mid=(lo+hi)/2
        if fun(mid)>0:hi=mid
        else:lo=mid
    return (lo+hi)/2

q=bisect_root(lambda v:tm_sum(v)-ONE)
lam=ONE/q
h=-q.ln()
S=sum((D(i)*q**i for i in range(1,K+1) if bits[i]),D(0))
print('lambda=',lam)
print('entropy=',h)
print('S=',S)

def finite_root(n):
    def fun(v):
        return sum((v**j for j in range(1,n) if bits[j]),D(0))+v**n/(ONE-v)-ONE
    return bisect_root(fun)

for n in [4,5,6,7,8,15,16,17,31,32,33,47,63,64,65,79,96,112,127,128,129,160]:
    qn=finite_root(n)
    scaled=(q/qn).ln()/q**n
    a=sum(((ONE-D(bits[n+j]))*q**j for j in range(0,K-n)),D(0))
    approx=a/S
    delta=abs(scaled-approx)
    # Finite-size correction decays like n*q**n.
    print(f'n={n:3d} t={bits[n]} scaled={scaled:.14f} phase={approx:.14f} abs_diff={delta:.3E}')
    assert delta < D(150)*D(n)*q**n

def direct_ok(w,n):
    at=[i for i,v in enumerate(w) if v]
    return all(d>=n or bits[d] for d in (b-a for a,b in zip(at,at[1:])))

def graph_ok(w,n):
    states=set(range(n))
    for a in w:
        nxt=set()
        for st in states:
            if a==0:
                nxt.add(min(st+1,n-1))
            elif st+1>=n or bits[st+1]:
                nxt.add(0)
        states=nxt
        if not states:return False
    return bool(states)

number=0
for n in range(1,11):
    for k in range(1,13):
        for w in product((0,1),repeat=k):
            assert direct_ok(w,n)==graph_ok(w,n),(n,k,w)
            number+=1
print('language-membership comparisons:',number)
print('PASS')
