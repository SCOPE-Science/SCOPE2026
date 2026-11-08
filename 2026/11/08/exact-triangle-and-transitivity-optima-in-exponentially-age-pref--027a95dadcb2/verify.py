#!/usr/bin/env python3
"""Independent arithmetic checks for geometric-age two-parent graph motifs.

Run with Python 3; no third-party dependencies.
"""
from fractions import Fraction
from itertools import product
from math import comb

def model_probs(n,q):
    return [[q**(j-1-k)/sum(q**h for h in range(j)) for k in range(j)] for j in range(1,n)]

def exact_finite_means(n,q):
    # n vertices indexed 0,...,n-1.
    P=model_probs(n,q)
    triangles=Fraction(0)
    for j in range(2,n):
        for i in range(1,j):
            for k in range(i):
                triangles += 2*P[j-1][i]*P[j-1][k]*(2*P[i-1][k]-P[i-1][k]**2)
    wedges=Fraction(0)
    for i in range(n):
        if i==0:
            outgoing=Fraction(0); out_pairs=Fraction(0)
        else:
            same=sum(p*p for p in P[i-1])
            outgoing=2-same
            out_pairs=1-same
        r=[2*P[j-1][i]-P[j-1][i]**2 for j in range(i+1,n)]
        incoming=sum(r)
        pair_in=(incoming**2-sum(t*t for t in r))/Fraction(2)
        wedges+=out_pairs+outgoing*incoming+pair_in
    return triangles,wedges

def counts(parents):
    n=len(parents)+1
    adj=[set() for _ in range(n)]
    for j,ps in enumerate(parents,1):
        for k in ps:
            adj[j].add(k);adj[k].add(j)
    tri=sum(1 for a in range(n) for b in range(a+1,n) for c in range(b+1,n) if b in adj[a] and c in adj[b] and c in adj[a])
    wedges=sum(comb(len(neigh),2) for neigh in adj)
    return tri,wedges

def brute(n,q):
    p=model_probs(n,q)
    terms=[]
    for j in range(1,n):
        arr=[]
        for a in range(j):
            for b in range(j):
                arr.append(((a,b),p[j-1][a]*p[j-1][b]))
        terms.append(arr)
    tri=wedge=Fraction(0)
    for t in product(*terms):
        val=Fraction(1)
        for pair,pr in t: val*=pr
        ct,cw=counts([entry[0] for entry in t])
        tri+=ct*val;wedge+=cw*val
    return tri,wedge

def T(q):
    return 2*q*(1-q)*(3*q*q+2*q+1)/((q+1)**2*(q*q+q+1))

def W(q):
    return (20*q**6+28*q**5+43*q**4+39*q**3+26*q**2+11*q+1)/((1+q)**2*(1+q*q)*(1+q+q*q))

def finite_stationary_triangle(q,R):
    p=lambda i:(1-q)*q**(i-1)
    return sum(2*p(a)*p(a+b)*(2*p(b)-p(b)**2) for a in range(1,R+1) for b in range(1,R+1))

def finite_stationary_wedges(q,R):
    ps=[(1-q)*q**(h-1) for h in range(1,R+1)]
    S2=sum(x*x for x in ps)
    r=[2*x-x*x for x in ps]
    incoming=sum(r)
    return (1-S2)+(2-S2)*incoming+(incoming**2-sum(x*x for x in r))/Fraction(2)

def P_T(q):return 10*q**5+16*q**4+13*q**3-q*q-q-1

def P_C(q):return 104*q**10+178*q**9+372*q**8+426*q**7+435*q**6+276*q**5+177*q**4+42*q**3+9*q*q-2*q-1


# Integer-polynomial arithmetic with constant coefficient first.
def add(a,b):
    return [ (a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b))) ]
def neg(a):return [-x for x in a]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out
def scale(a,c):return [c*x for x in a]
def derivative(a):return [(i+1)*a[i+1] for i in range(len(a)-1)]
def trim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def exact_derivative_identities():
    Q=[0,1];one=[1];one_q=[1,1];S=[1,1,1];U=[1,2,3]
    N_T=scale(mul(mul(Q,[1,-1]),U),2)
    D_T=mul(mul(one_q,one_q),S)
    PT=[-1,-1,-1,13,16,10]
    assert trim(sub(mul(derivative(N_T),D_T),mul(N_T,derivative(D_T))))==trim(scale(mul(one_q,PT),-2))
    P6=[1,11,26,39,43,28,20]
    N_C=scale(mul(mul(mul(Q,[1,-1]),[1,0,1]),U),6)
    PC=[-1,-2,9,42,177,276,435,426,372,178,104]
    assert trim(sub(mul(derivative(N_C),P6),mul(N_C,derivative(P6))))==trim(scale(PC,-6))
    # Descartes: each root polynomial has exactly one positive root.
    for coeff in (PT,PC):
        seq=[1 if x>0 else -1 for x in coeff if x]
        assert sum(seq[i]!=seq[i-1] for i in range(1,len(seq)))==1
        assert sum(coeff)>0 and coeff[0]<0
    return 4

def main():
    assertions=exact_derivative_identities()
    for q in (Fraction(1,2),Fraction(2,3),Fraction(1,4)):
        for n in range(2,7):
            exact=exact_finite_means(n,q)
            enumerated=brute(n,q)
            assert exact==enumerated,(n,q,exact,enumerated)
            assertions+=2
        # Directly derived stationary identities.
        p2=(1-q)/(1+q)
        s=2-p2
        R=4*(1-q)/(1+q)-4*(1-q)**2/(1+q+q*q)+(1-q)**3/(1+q+q*q+q**3)
        assert W(q)==2*q/(1+q)+(3*s*s-R)/2
        assertions+=1
        # Two distinct geometric sums for triangle density.
        assert T(q)==4*q*(1-q)/(1+q)**2-2*q*(1-q)**4/((1-q*q)*(1-q**3))
        assertions+=1
        # Finite truncation omitted mass is positive and small at R=30.
        assert 0<=T(q)-finite_stationary_triangle(q,30)<Fraction(1,100000)
        assert 0<=W(q)-finite_stationary_wedges(q,40)<Fraction(1,100000)
        assertions+=2
    # Exact polynomial identity for derivatives via symmetric difference rational function.
    for q in (Fraction(1,7),Fraction(1,3),Fraction(4,7),Fraction(5,6)):
        c= lambda x: 3*T(x)/W(x)
        # Compare derivatives from rational fractions using the identity: derivative=... 
        h=Fraction(1,10**7)
        num=(T(q+h)-T(q-h))/(2*h)
        claimed=-2*P_T(q)/((1+q)**3*(1+q+q*q)**2)
        assert abs(num-claimed)<Fraction(1,10000000)
        der=(c(q+h)-c(q-h))/(2*h)
        denominator=(20*q**6+28*q**5+43*q**4+39*q**3+26*q**2+11*q+1)**2
        expect=-6*P_C(q)/denominator
        assert abs(der-expect)<Fraction(1,10000000)
        assertions+=2
    # Isolating intervals, signs and disjointness of the two unique positive critical roots.
    assert P_T(Fraction(420,1000))<0<P_T(Fraction(421,1000))
    assert P_C(Fraction(216,1000))<0<P_C(Fraction(218,1000))
    assert P_T(Fraction(0))<0<P_T(Fraction(1))
    assert P_C(Fraction(0))<0<P_C(Fraction(1))
    assertions+=4
    print('PASS',assertions,'exact/direct enumeration, limit-sum, algebraic and root checks')

if __name__=='__main__':main()
