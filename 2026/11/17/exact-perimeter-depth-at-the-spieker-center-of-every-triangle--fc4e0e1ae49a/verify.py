#!/usr/bin/env python3
"""Independent angular boundary-cut checks for the triangle arclength-center depth."""
import math
import random


def closed_formula(a,b,c):
    a,b,c=sorted((a,b,c),reverse=True)
    P=a+b+c
    assert a < b+c and c>0
    threshold=b*(a+b)*(a+c) <= c*(P+b)**2
    if threshold:
        value=(math.sqrt(c*(a+c))+math.sqrt(b*(a+b)))**2/(2*P*P)
    else:
        value=(b+c)/(P+b)
    return value, threshold


def angular_check(a,b,c,steps=16384):
    # Independent construction: explicit segment-line intersections, no W-line formulas.
    x=(b*b+c*c-a*a)/(2*c)
    y=math.sqrt(max(0.,b*b-x*x))
    A=(0.,0.); B=(c,0.); C=(x,y)
    sides=[(A,B),(B,C),(C,A)]
    P=a+b+c
    S=((a*(B[0]+C[0])+b*(C[0]+A[0])+c*(A[0]+B[0]))/(2*P),
       (a*(B[1]+C[1])+b*(C[1]+A[1])+c*(A[1]+B[1]))/(2*P))
    best=1.0
    for k in range(steps):
        theta=(k+.223)/steps*math.pi
        nx,ny=math.cos(theta),math.sin(theta)
        hits=[]
        offset=0.0
        for U,V in sides:
            du=nx*(U[0]-S[0])+ny*(U[1]-S[1]);dv=nx*(V[0]-S[0])+ny*(V[1]-S[1]);
            length=math.hypot(V[0]-U[0],V[1]-U[1])
            if du*dv<=0 and abs(du-dv)>1e-14:
                t=du/(du-dv)
                if -1e-12<=t<=1+1e-12: hits.append(offset+t*length)
            offset+=length
        if len(hits)==2:
            d=abs(hits[0]-hits[1]);best=min(best,d/P,1-d/P)
    return best


def run():
    rng=random.Random(17419)
    samples=0; hits=[0,0]
    for i in range(6000):
        x,y,z=[rng.expovariate(1.) for _ in range(3)]
        a,b,c=sorted((y+z,x+z,x+y),reverse=True)
        val,branch=closed_formula(a,b,c)
        hits[int(branch)]+=1
        assert 1/3-2e-13 < val < 1/2, (a,b,c,val)
        samples+=1
    details=[]
    test_shapes=[(1,1,1),(2.9,2,1),(1.9,1,1),(1.25,1.1,.3),(2.01,2, .02),
                 (4.1,4.1,1),(4.9,4,1),(5,3.6,1.6),(1.3,1,.5)]
    for a,b,c in test_shapes:
        formula,branch=closed_formula(a,b,c)
        sampled=angular_check(a,b,c,steps=200000 if c/min(a,b)<.03 else 40000)
        err=sampled-formula
        assert -1e-10 <=err<=.00020,(a,b,c,formula,sampled,err)
        details.append((a,b,c,round(formula,10),round(sampled,10),branch))
    for e in (1e-3,1e-4,1e-5):
        val,_=closed_formula(1,1,e)
        assert 0<val-1/3<3*e
    print('PASS random triangle inequalities',samples,'W/end branches',hits)
    print('PASS independent angular cuts',len(details))
    for line in details:print(line)
    print('PASS sharp near-degenerate limiting family')
if __name__=='__main__':run()
