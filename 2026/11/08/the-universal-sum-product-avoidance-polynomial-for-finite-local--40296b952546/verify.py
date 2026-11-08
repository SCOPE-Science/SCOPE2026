"""Exact finite checks for the local-ring sum-product avoidance polynomial.
No dependence on web services or external packages. The proof is symbolic, not finite enumeration.
"""
from collections import Counter
from math import gcd

def ring_zpk(p,k):
    n=p**k
    return n,p**(k-1),list(range(n)),lambda a,b:(a+b)%n,lambda a,b:(a*b)%n,(1%n),0

def ring_f25():
    p=5
    elems=[(a,b) for a in range(p) for b in range(p)]
    def add(x,y):return ((x[0]+y[0])%p,(x[1]+y[1])%p)
    def mul(x,y):return ((x[0]*y[0]+2*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
    return len(elems),1,elems,add,mul,(1,0),(0,0)

def ring_dual(p=5,r=1):
    from itertools import product
    els=list(product(range(p),repeat=r+1))
    def add(x,y):return tuple((a+b)%p for a,b in zip(x,y))
    def mul(x,y):return (x[0]*y[0]%p,)+tuple((x[0]*y[j]+y[0]*x[j])%p for j in range(1,r+1))
    return len(els),p**r,els,add,mul,(1,)+(0,)*r,(0,)*(r+1)

def polmul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b): c[i+j]+=u*v
    return c

def polpow(a,n):
    r=[1]
    for _ in range(n):r=polmul(r,a)
    return r

def calc_and_check(label,ring,full_brute=False):
    n,m,elems,add,mul,one,zero=ring
    index={x:i for i,x in enumerate(elems)}
    edges=[set() for _ in elems]
    loops=set()
    for i,x in enumerate(elems):
        for j,y in enumerate(elems):
            if add(x,y)==one or mul(x,y)==one:
                if i==j:loops.add(i)
                else:edges[i].add(j)
    comps=[];used=set()
    for i in range(n):
        if i in used:continue
        visit=[i];used.add(i);comp=[]
        while visit:
            v=visit.pop();comp.append(v)
            for j in edges[v]:
                if j not in used:used.add(j);visit.append(j)
        comps.append(comp)
    poly=[1];forms=Counter()
    for comp in comps:
        t=len(comp);pc=[0]*(t+1);ni=0
        for mask in range(1<<t):
            ids=[x for i,x in enumerate(comp) if mask>>i&1]
            if any(v in loops or any(w in edges[v] for w in ids) for v in ids):continue
            pc[len(ids)]+=1;ni+=1
        if t==2 and pc==[1,1,0]:typ='exception-01'
        elif t==3 and pc==[1,1,0,0]:typ='exception-2'
        elif t==2 and pc==[1,2,0]:typ='root-pair'
        elif t==4 and pc==[1,4,3,0,0]:typ='path4'
        elif t==6 and pc==[1,6,9,2,0,0,0]:typ='cycle6'
        else:raise AssertionError((label,t,pc))
        forms[typ]+=1
        while pc and pc[-1]==0: pc.pop()
        poly=polmul(poly,pc)
    q=n//m;delta=2 if q%3==1 else 0
    h=(m-1)//2;c=(n-2*m-3-delta)//6
    exp=polmul(polmul(polpow([1,1],2),polpow([1,2],delta//2)),polmul(polpow([1,4,3],h),polpow([1,6,9,2],c)))
    assert poly==exp,(label,'coefficient mismatch')
    assert len(poly)-1==(n-1)//2
    assert poly[-1]==3**h*2**(c+delta//2)
    assert forms['exception-01']==1 and forms['exception-2']==1 and forms['path4']==h and forms['cycle6']==c and forms['root-pair']==delta//2
    if full_brute:
        # Independent arithmetic check on all subsets, no graph component reduction
        count=[0]*(n+1)
        for mask in range(1<<n):
            ids=[i for i in range(n) if mask>>i&1]
            ok=True
            for i in ids:
                for j in ids:
                    if add(elems[i],elems[j])==one or mul(elems[i],elems[j])==one:ok=False;break
                if not ok:break
            if ok:count[len(ids)]+=1
        assert count[:len(poly)]==poly
    print(f'{label}: N={n}, M={m}, field_order={q}, paths={h}, cycles={c}, roots={delta}, degree={len(poly)-1}, maximum_count={poly[-1]}, all_sets={sum(poly)}, full_brute={full_brute}, PASS')

if __name__=='__main__':
    for p,k in [(5,1),(7,1),(11,1),(13,1),(5,2),(7,2),(5,3)]:calc_and_check('Z/%d'% (p**k),ring_zpk(p,k),full_brute=p**k<=13)
    calc_and_check('F_25',ring_f25())
    calc_and_check('F_5[eps]/(eps^2)',ring_dual(5,1))
    calc_and_check('F_5[eps,eta]/(eps,eta)^2',ring_dual(5,2))
    print('ALL_EXACT_RING_COMPARISONS_PASS; infinite local-ring theorem requires symbolic proof')
