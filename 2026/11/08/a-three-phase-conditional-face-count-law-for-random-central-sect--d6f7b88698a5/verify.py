#!/usr/bin/env python3
"""Numerical and combinatorial consistency tests for the cube width/section joint law.
Only standard-library Python is required. Random tests are supporting evidence, not proof.
"""
import math, random, itertools
PI=math.pi
SQ3=math.sqrt(3)
LOW=math.sqrt(2)
HIGH=math.sqrt(8/3)
END=SQ3

def clamp(x):return min(1.,max(-1.,x))
def alpha(s):return math.acos(clamp(s/(2*math.sqrt(6-2*s*s))))
def beta(s):return math.acos(clamp(s/math.sqrt(6-2*s*s)))

def densities(s):
    if not (1<s<END):return (0.,0.)
    if s<LOW:return ((4/SQ3)*(1-3*beta(s)/PI),0.)
    if s<HIGH:
        p4=12*alpha(s)/(PI*SQ3)
        return (p4,4/SQ3-p4)
    return (0.,4/SQ3)

def integrate(f,a,b,eps=1e-10):
    # Adaptive Simpson, endpoints open to avoid division by zero roundoff.
    def simp(x,y,fx,fy,fm):return (y-x)*(fx+4*fm+fy)/6
    def go(x,y,fx,fy,fm,whole,budget):
        mid=(x+y)/2; lm=(x+mid)/2; rm=(mid+y)/2
        fl=f(lm);fr=f(rm)
        left=simp(x,mid,fx,fm,fl);right=simp(mid,y,fm,fy,fr)
        if budget<1 or abs(left+right-whole)<15*eps:
            return left+right+(left+right-whole)/15
        return go(x,mid,fx,fm,fl,left,budget-1)+go(mid,y,fm,fy,fr,right,budget-1)
    fx=f(a);fy=f(b);fm=f((a+b)/2)
    return go(a,b,fx,fy,fm,simp(a,b,fx,fy,fm),24)

def integrate_law(power=0,typ=None):
    f=lambda s: (sum(densities(s)) if typ is None else densities(s)[typ])*s**power
    return sum(integrate(f,a,b) for a,b in ((1,LOW),(LOW,HIGH),(HIGH,END)))

def gaussian_vector(rng):
    x=[rng.gauss(0,1) for _ in range(3)]
    rr=math.sqrt(sum(c*c for c in x))
    return tuple(c/rr for c in x)

def direct_sections(u):
    vertices=list(itertools.product((-1,1),repeat=3))
    edges=[]
    for v in vertices:
        for k in range(3):
            if v[k]!=-1:continue
            w=list(v);w[k]=1
            if sum(a*b for a,b in zip(v,u))*sum(a*b for a,b in zip(w,u)) <0:
                edges.append((v,tuple(w)))
    return len(edges)

def q_from_u(u):
    v=sorted(map(abs,u),reverse=True)
    return 4 if v[0]>v[1]+v[2] else 6

def direct_phi_density(s,steps=18000):
    # Condition on s, angular coordinate around e=(1,1,1)/sqrt(3).
    e1=(1/math.sqrt(2),-1/math.sqrt(2),0)
    e2=(1/math.sqrt(6),1/math.sqrt(6),-2/math.sqrt(6))
    r=math.sqrt(1-s*s/3); pos=zero4=zero6=0
    for i in range(steps):
        t=2*PI*(i+.5)/steps
        u=[s/3+r*(math.cos(t)*e1[k]+math.sin(t)*e2[k]) for k in range(3)]
        if min(u)>0:
            pos+=1
            if q_from_u(u)==4:zero4+=1
            else:zero6+=1
    factor=(2*PI/steps)*2/(PI*SQ3)
    return zero4*factor,zero6*factor

def main():
    p4=integrate_law(typ=0);p6=integrate_law(typ=1)
    target=3-12/PI*math.atan(1/math.sqrt(2))
    assert abs(p4-target)<1e-8,(p4,target)
    assert abs(p4+p6-1)<1e-8
    assert abs(integrate_law(power=1)-1.5)<1e-7
    assert abs(integrate_law(power=2)-(1+4/PI))<1e-7
    for s in (1.01,1.17,1.35,LOW+.01,1.46,1.55,1.62,1.635,1.68,1.72):
        analytic=densities(s);direct=direct_phi_density(s)
        assert max(abs(a-b) for a,b in zip(analytic,direct))<0.001,(s,analytic,direct)
    rng=random.Random(20261103)
    n=350000
    counts=[0,0]
    data=[]
    for _ in range(n):
        u=gaussian_vector(rng)
        w=sum(map(abs,u))
        sides=direct_sections(u)
        q=q_from_u(u)
        assert sides==q,(u,sides,q)
        counts[0 if sides==4 else 1]+=1
        data.append((w,0 if sides==4 else 1))
    assert abs(counts[0]/n-p4)<0.004
    intervals=((1,1.20),(1.20,LOW),(LOW,1.50),(1.50,1.60),(1.60,HIGH),(HIGH,END))
    maxdiff=0.
    for lo,hi in intervals:
        for typ in (0,1):
            observed=sum(lo<w<hi and t==typ for w,t in data)/n
            expected=integrate(lambda s:densities(s)[typ],lo,hi)
            maxdiff=max(maxdiff,abs(observed-expected))
            assert abs(observed-expected)<0.004,(lo,hi,typ,observed,expected)
    print('VERIFY_OK normal_samples=%d direct_edge_crossings=%d circle_sections=%d exact_marginal_checks=4 width_type_bin_checks=%d max_bin_error=%.7f P4=%.12f P6=%.12f'%(n,n,10,12,maxdiff,p4,p6))

if __name__=='__main__':main()
