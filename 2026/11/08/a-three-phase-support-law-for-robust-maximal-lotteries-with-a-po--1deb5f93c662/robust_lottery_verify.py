"""Exact rational finite checks for a three-choice robust-lottery theorem.
Standard-library only. These checks complement, not replace, the analytic proof.
Run: python robust_lottery_verify.py
"""
from fractions import Fraction as F
from itertools import combinations, product


def matrices(u,v,w):
    return (((F(0),u,v),(-u,F(0),-w),(-v,w,F(0))),
            ((F(0),-u,-w),(u,F(0),v),(w,-v,F(0))))


def mix(A,B,theta):
    return tuple(tuple(theta*A[i][j]+(1-theta)*B[i][j]
                       for j in range(3)) for i in range(3))


def gaussian(rows, vals):
    a=[list(row)+[val] for row,val in zip(rows,vals)]
    for col in range(4):
        pivot=next((j for j in range(col,4) if a[j][col]),None)
        if pivot is None: return None
        a[col],a[pivot]=a[pivot],a[col]
        t=a[col][col]
        a[col]=[v/t for v in a[col]]
        for j in range(4):
            if j!=col:
                t=a[j][col]
                a[j]=[a[j][k]-t*a[col][k] for k in range(5)]
    return tuple(row[-1] for row in a)


def exact_lp(u,v,w,r):
    A,B=matrices(u,v,w)
    lo,hi=(1-r)/2,(1+r)/2
    constraints=[]
    for M in (mix(A,B,lo),mix(A,B,hi)):
        for j in range(3):
            constraints.append([M[0][j],M[1][j],M[2][j],F(-1)])
    for i in range(3):
        constraints.append([F(int(i==j)) for j in range(3)]+[F(0)])
    best=None
    for tri in combinations(range(9),3):
        sol=gaussian([[F(1),F(1),F(1),F(0)]]+[constraints[i] for i in tri],
                     [F(1),F(0),F(0),F(0)])
        if sol is None or any(sum(c[j]*sol[j] for j in range(4))<0 for c in constraints):
            continue
        if best is None or sol[3]>best[3]:best=sol
    assert best is not None
    return best


def analytic(u,v,w,r):
    t=w-v
    slope=t+r*(u-w-v)
    f=lambda z:min(-r*u/2+slope*z/2,(v-w)*(1-z)/2)
    choices=[F(0),F(1)]
    denom=r*(u-w-v)
    if denom:
        z=(r*u-t)/denom
        if 0<=z<=1: choices.append(z)
    z=max(choices,key=f)
    return ((1-z)/2,(1-z)/2,z,f(z))


def exact_margins(ballots):
    n=sum(ballots.values())
    def m(a,b):
        return F(sum(v*(1 if s.index(a)<s.index(b) else -1)
                     for s,v in ballots.items()),n)
    return (m('A','B'),m('A','C'),m('C','B'))


def run():
    checks=0
    for U,V,W,R in product([1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]):
        u,v,w,r=(F(U,5),F(V,5),F(W,5),F(R,5))
        if r==0:continue
        sol=exact_lp(u,v,w,r)
        prediction=analytic(u,v,w,r)
        assert sol[3]==prediction[3],(u,v,w,r,sol,prediction)
        checks+=1
    # Three distinct full-ambiguity supports, from actual ballots.
    profile_mix={'ACB':12,'BAC':2,'CBA':6}
    profile_loser={'ACB':3,'ABC':7,'BAC':2,'CAB':8}
    profile_AB={'ACB':11,'BAC':4,'CAB':3,'CBA':2}
    assert exact_margins(profile_mix)==(F(1,5),F(2,5),F(4,5))
    assert exact_margins(profile_loser)==(F(4,5),F(1,5),F(1,10))
    assert exact_margins(profile_AB)==(F(2,5),F(1,2),F(3,5))
    assert analytic(F(1,5),F(2,5),F(4,5),F(1))==(F(2,5),F(2,5),F(1,5),-F(4,25))
    assert analytic(F(4,5),F(1,5),F(1,10),F(1))==(F(0),F(0),F(1),-F(1,5))
    assert analytic(F(2,5),F(1,2),F(3,5),F(1))==(F(1,2),F(1,2),F(0),-F(1,5))
    # Radius transition for a pooled Condorcet loser.
    u,v,w=F(4,5),F(1,5),F(1,10)
    rc=(v-w)/(u-v-w)
    assert rc==F(1,5)
    assert analytic(u,v,w,F(1,10))[:3]==(F(1,2),F(1,2),F(0))
    assert analytic(u,v,w,F(3,10))[:3]==(F(0),F(0),F(1))
    assert analytic(u,v,w,rc)[3]==-rc*u/2
    print('PASS: %d exact rational LP/analytic comparisons; 3 exact ballot profiles; radius switch 1/5' % checks)

if __name__=='__main__':run()
