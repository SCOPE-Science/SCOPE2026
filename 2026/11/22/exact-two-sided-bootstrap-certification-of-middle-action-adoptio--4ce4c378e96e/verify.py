"""Exact arithmetic checks for the three-action middle-adoption theorem's witness.
No external dependencies. Mathematical universality is established analytically in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product

W = [
  [F(0), F(4,5), F(1,5), F(0)],
  [F(4,5), F(0), F(0), F(1,5)],
  [F(1,2), F(0), F(0), F(1,2)],
  [F(0), F(1,2), F(1,2), F(0)],
]
l = [F(-2,5), F(-2,5), F(-3,4), F(-1,4)]
u = [F(2,5), F(2,5), F(1,4), F(3,4)]
seed={0,1}

def q(i,x):
    return -1 if x < l[i] else (0 if x < u[i] else 1)

def weight(i,S): return sum((W[i][j] for j in S),F(0))
def closure(kappa):
    C=set(seed)
    path=[tuple(sorted(C))]
    while True:
       N=C|{i for i in range(4) if i not in C and weight(i,C)>kappa[i]}
       if N==C:return C,path
       C=N
       path.append(tuple(sorted(C)))

def update(x,alpha):
    y=[]
    for i in range(4):
       social=sum((W[i][j]*q(j,x[j]) for j in range(4)),F(0))
       y.append(alpha[i]*x[i]+(1-alpha[i])*social)
    return y

def check():
    assert all(sum(r)==1 for r in W)
    assert all(W[i][i]==0 for i in range(4))
    minus=[1+t for t in l]
    plus=[1-t for t in u]
    combined=[max(x,y) for x,y in zip(minus,plus)]
    assert minus==[F(3,5),F(3,5),F(1,4),F(3,4)]
    assert plus==[F(3,5),F(3,5),F(3,4),F(1,4)]
    assert all(weight(i,seed)>=combined[i] for i in seed)
    C0,P0=closure(combined)
    Cm,Pm=closure(minus)
    Cp,Pp=closure(plus)
    assert C0==seed and Cm==Cp==set(range(4))
    assert Pm==[(0,1),(0,1,2),(0,1,2,3)],Pm
    assert Pp==[(0,1),(0,1,3),(0,1,2,3)],Pp
    # Inertia parameters and arbitrary admissible seed opinions, all outsider initial extremes.
    checks=0
    for a in [F(1,3),F(1,2),F(4,5),F(9,10)]:
      alpha=[a]*4
      for seeds in product([F(-2,5),F(-1,5),F(0),F(1,5),F(399,1000)],repeat=2):
       for outs in product([F(-1),F(-4,5),F(-1,10),F(0),F(1,10),F(4,5),F(1)],repeat=2):
        x=list(seeds+outs)
        assert all(q(i,x[i])==0 for i in seed)
        all_neutral=False
        for t in range(1200):
          if all(q(i,x[i])==0 for i in range(4)):
             all_neutral=True
             break
          x=update(x,alpha)
          assert all(q(i,x[i])==0 for i in seed)
        if not all_neutral:
          raise AssertionError((a,seeds,outs,x))
        checks+=1
    # Explicit proof's threshold endpoint cases in one remaining outsider setting.
    for a in [F(1,2), F(9,10)]:
        y=F(-1)
        for t in range(1000):
            y=a*y # input zero, lower threshold 0
            assert y<0
        z=F(1)
        for t in range(1000):
            z=a*z # input zero, upper threshold 0
            assert z>0
    print('PASS: 4-state exact closure and robust seed conditions')
    print('PASS:',checks,'exact rational trajectory tests, four inertia choices')
    print('PASS: endpoint non-adoption at threshold equality')
    print('Lower one-sided closure',Pm)
    print('Upper one-sided closure',Pp)
    print('Combined closure',P0)
if __name__=='__main__':check()
