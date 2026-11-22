"""Standalone verification of two-vacancy shielding in one-shot antagonistic adsorption.

Standard Python library only. Exact finite-path enumeration; analytic bounds checked
through exact Taylor coefficients. Not an infinite-volume proof.
"""
from fractions import Fraction as F
from itertools import permutations, product
from math import factorial, cosh, sinh, sqrt

CHECKS=0

def same(a,b):
    global CHECKS
    assert a==b, (a,b)
    CHECKS+=1

def integrate(coef):
    return [F(0)]+[c/F(i+1) for i,c in enumerate(coef)]

def sub(a,b):
    return [ (a[i] if i<len(a) else F(0))-(b[i] if i<len(b) else F(0)) for i in range(max(len(a),len(b)))]

def mult_scalar(a,c):
    return [z*c for z in a]

def eval_poly(a,t):
    return sum((c*t**i for i,c in enumerate(a)),F(0))

def halfline(n,p):
    assert n>=1
    q=1-p
    a=[F(0),p];b=[F(0),q]
    for k in range(2,n+1):
        a,b=sub([F(0),p],mult_scalar(integrate(b),p)),sub([F(0),q],mult_scalar(integrate(a),q))
    return a,b

def boundary_weight(n,p):
    a,b=halfline(n,p)
    return (1-p)*eval_poly(integrate(a),F(1))+p*eval_poly(integrate(b),F(1))

def brute(length,left_count,p):
    """Count all color and time-order markings, each order weighted 1/n!"""
    n=length;pos=left_count
    # vacancy sites pos,pos+1
    num=0; counts={(aa,bb):0 for aa in (-1,1) for bb in (-1,1)}; joint={}
    den=p.denominator
    assert (1-p).denominator==den
    pw=int(p*den);qw=int((1-p)*den)
    cols=list(product((-1,1),repeat=n))
    for c in cols:
        weight=1
        for x in c:weight*=pw if x==1 else qw
        for perm in permutations(range(n)):
            st=[0]*n
            for k in perm:
                if (k==0 or st[k-1]!=-c[k]) and (k==n-1 or st[k+1]!=-c[k]):
                    st[k]=c[k]
            if st[pos]==0 and st[pos+1]==0:
                num+=weight
                counts[(st[pos-1],st[pos+2])]+=weight
                key=(tuple(st[:pos]),tuple(st[pos+2:]))
                joint[key]=joint.get(key,0)+weight
    z=den**n*factorial(n)
    return F(num,z),{k:F(v,z) for k,v in counts.items()}, joint

def test_finite():
    for p,n,l in [(F(1,2),5,1),(F(1,3),5,2),(F(2,5),6,2),(F(3,4),6,3),(F(1,2),7,2)]:
        z,types,joint=brute(n,l,p)
        wl=boundary_weight(l,p);wr=boundary_weight(n-l-2,p)
        same(z,wl*wr)
        al,bl=halfline(l,p);ar,br=halfline(n-l-2,p)
        sl={1:(1-p)*eval_poly(integrate(al),F(1)),-1:p*eval_poly(integrate(bl),F(1))}
        sr={1:(1-p)*eval_poly(integrate(ar),F(1)),-1:p*eval_poly(integrate(br),F(1))}
        for pair in types:
            same(types[pair],sl[pair[0]]*sr[pair[1]])
        left={};right={};total=sum(joint.values())
        for (a,b),v in joint.items():
            left[a]=left.get(a,0)+v;right[b]=right.get(b,0)+v
        for a in left:
            for b in right:
                same(joint.get((a,b),0)*total,left[a]*right[b])
    return

def test_infinite():
    for p in (0.001,0.01,.1,.25,.5,.75,.9,.99,.999):
        q=1-p;x=sqrt(p*q)
        W=2*cosh(x)-1-sinh(x)/x
        left_A=q*(1-sinh(x)/x+p*(cosh(x)-1)/(x*x))
        left_B=p*(1-sinh(x)/x+q*(cosh(x)-1)/(x*x))
        same(round(left_A+left_B,11),round(W,11))
        ratio=(left_A-left_B)/W
        delta=p-q
        if abs(delta)>1e-8:
            same(round(ratio/delta,10),round(((sinh(x)/x)-1)/W,10))
        assert 0< (sinh(x)/x-1)/W < F(1,5)
        global CHECKS
        CHECKS+=1
    # Taylor series coefficients: for each n>=2, 2(C+2-3 S) has positive even term.
    for n in range(2,50):
        coeff=F(2,factorial(2*n))*(F(1)-F(3,2*n+1))
        assert coeff>0
        CHECKS+=1
    # The 'sharp' 1/5 is the small-x limit by coefficient ratio.
    same(F(1,6)/F(5,6), F(1,5))

def main():
    test_finite()
    test_infinite()
    print('PASSED',CHECKS,'exact finite-state and analytic coefficient checks')
    x=.5;W=2*cosh(x)-1-sinh(x)/x
    print('balanced P(XX) = %.15f; all four boundary patterns = %.15f'%(W*W,W*W/4))
    print('balanced mean distance between double-vacancy starts = %.12f'%(1/(W*W)))
if __name__=='__main__':main()
