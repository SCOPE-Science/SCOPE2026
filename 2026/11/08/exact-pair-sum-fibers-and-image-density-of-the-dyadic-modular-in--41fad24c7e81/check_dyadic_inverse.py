"""Exact integer checker for two-sum inverse-graph theorem (no external packages)."""
from collections import Counter

def v2(t):
    return (t & -t).bit_length() - 1

def roots_square(w,m,parity):
    """Count solutions z^2 = w modulo 2^m with z mod 2^m of given parity."""
    modulus=1<<m; w%=modulus
    if w==0:
        return (1 << (m//2)) if parity==0 else 0
    e=v2(w)
    if e&1: return 0
    j=e//2
    if (j==0 and parity!=1) or (j>=1 and parity!=0):
        return 0
    n=m-2*j
    unit=w>>(2*j)
    if n==1: base=1
    elif n==2: base=2 if unit%4==1 else 0
    else: base=4 if unit%8==1 else 0
    return (1<<j)*base

def r(k,s,t):
    q=1<<k
    s%=q;t%=q
    if s==0: return q//2 if t==0 else 0
    if s%2 or t==0: return 0
    h=v2(s)
    if v2(t)!=h: return 0
    m=k-h; mod=1<<m
    S=s>>h;T=t>>h
    w=((s//2)**2-S*pow(T,-1,mod))%mod
    return (1<<h)*roots_square(w,m,0 if h==1 else 1)

def closed(k):
    q=1<<k
    return ((q*q+(40 if k%2==0 else 32)*q+256)//96,
            3*(k-3)*q*q//2)

def run():
    for k in range(4,12):
        q=1<<k
        points=[(u,pow(u,-1,q)) for u in range(1,q,2)]
        observed=Counter(((u+v)%q,(a+b)%q) for u,a in points for v,b in points)
        for s in range(q):
            for t in range(q):
                actual=observed.get((s,t),0)
                expected=r(k,s,t)
                assert actual==expected,(k,s,t,actual,expected)
        support,energy=closed(k)
        assert len(observed)==support,(k,len(observed),support)
        e_observed=sum(z*z for z in observed.values())
        assert e_observed==energy,(k,e_observed,energy)
        print('k=%d q=%d support=%d energy=%d exact_targets=%d PASS'%(k,q,support,energy,q*q))
    print('DYADIC_INVERSE_GRAPH_FULL_CONVOLUTION_PASS')
if __name__=='__main__':run()
