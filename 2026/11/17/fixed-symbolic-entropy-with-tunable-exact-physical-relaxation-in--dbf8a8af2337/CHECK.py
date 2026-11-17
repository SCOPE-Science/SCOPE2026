#!/usr/bin/env python3
"""Exact rational transfer and numerical entropy checks for a five-branch family."""
from fractions import Fraction as Q
from math import sqrt, log
import random


def mul(A, v):
    return [sum(a*x for a, x in zip(row, v)) for row in A]


def model(lengths):
    assert len(lengths) == 5 and sum(lengths) == 1
    c3 = sum(lengths[:3]); c4 = c3 + lengths[3]
    assert c4 > Q(1,2) and lengths[3] < c3
    heights = [c4,c3,c4,c3,c4]
    assert all(h > ell for h,ell in zip(heights,lengths))
    W = [[(lengths[j] / heights[j]) if (i < (4 if j%2==0 else 3)) else Q(0)
          for j in range(5)] for i in range(5)]
    E = (lengths[0] + lengths[2])/c4
    d = lengths[3]/c3
    q=E*d
    Astar=1/(c3+E*lengths[3]); Dstar=E*Astar
    r1=mul(W,[Q(1)]*5)
    assert r1[0]==r1[1]==r1[2] and r1[4]==0
    A1=r1[0]; D1=r1[3]
    assert mul(W,[Astar,Astar,Astar,Dstar,Q(0)])==[Astar,Astar,Astar,Dstar,Q(0)]
    assert Q(0)<q<Q(1,2)
    for n in range(1,12):
        an=Astar+(A1-Astar)*(-q)**(n-1)
        dn=Dstar+(D1-Dstar)*(-q)**(n-1)
        assert r1==[an,an,an,dn,Q(0)]
        assert sum(u*v for u,v in zip(lengths,r1))==1
        tv=sum(u*abs(a-b) for u,a,b in zip(lengths,r1,[Astar]*3+[Dstar,Q(0)]))/2
        assert tv==c3*abs(A1-Astar)*q**(n-1)
        r1=mul(W,r1)
    return q,Astar,Dstar


def entropy(lengths):
    c3=sum(lengths[:3]);c4=c3+lengths[3]
    q,A,D=model(lengths)
    h=[c4,c3,c4,c3]
    pi=[float(lengths[i]*(A if i<3 else D)) for i in range(4)]
    P=[]
    for j in range(4):
        P.append([float(lengths[i]/h[j]) if i<(4 if j%2==0 else 3) else 0. for i in range(4)])
    assert abs(sum(pi)-1)<1e-12
    for i in range(4):
        assert abs(sum(pi[j]*P[j][i] for j in range(4))-pi[i])<1e-12
    lam=(3+sqrt(17))/2
    s=(lam-2)/2
    rr=[1,s,1,s]
    KL=0.; hm=0.
    for j in range(4):
        for i in range(4):
            p=P[j][i]
            if p:
                qq=rr[i]/(lam*rr[j])
                hm-=pi[j]*p*log(p)
                KL+=pi[j]*p*log(p/qq)
    assert abs(log(lam)-hm-KL)<1e-12
    assert KL>-1e-12
    return KL,hm


def main():
    equal=[Q(1,5)]*5
    q,A,D=model(equal)
    assert (q,A,D)==(Q(1,6),Q(10,7),Q(5,7))
    f1=mul([[equal[j]/([Q(4,5),Q(3,5),Q(4,5),Q(3,5),Q(4,5)][j])
             if i < (4 if j%2==0 else 3) else Q(0) for j in range(5)] for i in range(5)], [Q(1)]*5)
    assert f1==[Q(17,12)]*3+[Q(3,4),Q(0)]
    assert Q(3,5)*abs(f1[0]-A)==Q(1,140)
    rng=random.Random(811)
    for _ in range(90):
        # Choose a rational geometry satisfying the strict expansion conditions.
        c4=Q(rng.randint(60,90),100)
        r=Q(rng.randint(3,90),100)
        theta=Q(rng.randint(2,90),100)
        c3=c4/(1+r)
        ls=[c3*(1-theta)/2,theta*c3,c3*(1-theta)/2,r*c3,1-c4]
        model(ls)
        entropy(ls)
    lam=(3+sqrt(17))/2
    s=(lam-2)/2
    for c4 in (0.6,0.8,0.93):
        ls=[c4/lam,s*c4/lam,c4/lam,s*c4/lam,1-c4]
        c3=sum(ls[:3]); q=(ls[0]+ls[2])*ls[3]/(c4*c3)
        assert all((c4 if j%2==0 else c3)>ls[j] for j in range(5))
        rr=[1,s,1,s]
        for j in range(4):
            for i in range(4 if j%2==0 else 3):
                assert abs(ls[i]/(c4 if j%2==0 else c3)-rr[i]/(lam*rr[j]))<1e-12
    for target in [0.005,0.17,0.33,0.49]:
        theta=(1-2*target)/2
        r=target/(1-theta-target)
        c4=Q(4,5)
        c3=float(c4)/(1+r)
        ls=[(1-theta)*c3/2,theta*c3,(1-theta)*c3/2,r*c3,0.2]
        q=(ls[0]+ls[2])*ls[3]/(float(c4)*c3)
        assert 0<r<1 and abs(q-target)<1e-12
    print('VERIFY_OK exact_transfer_cases=91 exact_tv=1001 entropy_KL_cases=90 parry_equality=3 tunable_rates=4')

if __name__=='__main__':
    main()
