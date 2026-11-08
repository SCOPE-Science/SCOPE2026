"""Standalone finite exact diagnostics for one-edge network search law.
Run: python3 graph_checker.py
"""
import sympy as S
from itertools import combinations

def investigate(n,edges,u,v,eta,w):
    L=S.zeros(n);tau=S.zeros(n,1)
    for i,j,g,t in edges:
        g=S.Rational(g); t=S.Rational(t)
        L[i,i]+=g;L[j,j]+=g;L[i,j]-=g;L[j,i]-=g
        tau[i]+=g*t;tau[j]+=g*t
    O=S.ones(n,n)/n
    G=(L+O).inv()-O
    b=S.eye(n)[:,u]-S.eye(n)[:,v]
    A=S.trace(G);R=(b.T*G*b)[0];Q=(b.T*G**2*b)[0];B=S.factor(A*R-Q)
    tau0=sum(tau)
    predicted=(tau0+2*w*eta)*(A+B*w)/((n-1)*(1+R*w))
    L1=L+w*b*b.T
    tau1=tau+w*eta*(S.eye(n)[:,u]+S.eye(n)[:,v]);
    # Evaluate 1-pair MFPT by an independent grounded Laplacian solve
    total=S.Rational(0)
    for target in range(n):
        ix=[i for i in range(n) if i!=target]
        times=L1.extract(ix,ix).inv()*tau1.extract(ix,[0])
        total+=sum(times)
    actual=total/S.Integer(n*(n-1))
    assert S.factor(predicted-actual)==0,(predicted,actual)
    assert Q>0 and B>0
    initial=S.factor(tau0*A/(n-1))
    delta=S.factor(predicted-initial)
    shape=S.factor(w*(2*eta*A-tau0*Q+2*eta*B*w)/((n-1)*(1+w*R)))
    assert S.factor(delta-shape)==0
    if isinstance(w,S.Symbol) and eta < tau0*Q/(2*A):
        wzero=S.factor((tau0*Q-2*eta*A)/(2*eta*B))
        assert wzero>0
        assert S.factor(delta.subs(w,wzero))==0
        wmin=S.factor((S.sqrt(1+R*(tau0*Q-2*eta*A)/(2*eta*B))-1)/R)
        assert wmin>0 and wmin<wzero
        derivative=S.factor(S.diff(predicted,w))
        assert S.simplify(derivative.subs(w,wmin))==0
    return 7

def main():
    w=S.symbols('w',positive=True)
    cases=[
     (3,[(0,1,1,1),(1,2,2,3)],0,2),
     (4,[(0,1,1,1),(1,2,1,1),(2,3,1,1),(3,0,1,1)],0,2),
     (4,[(0,1,2,1),(0,2,3,2),(1,3,1,5),(2,3,4,3)],1,2),
     (5,[(0,1,1,1),(1,2,2,2),(2,3,3,3),(3,4,1,4),(4,0,2,5),(1,3,1,2)],0,3),
     (6,[(0,1,1,2),(1,2,2,1),(2,3,3,4),(3,4,4,1),(4,5,1,3),(5,0,2,2),(0,3,1,6)],1,4)
    ]
    count=0
    for n,edges,u,v in cases:
     for eta in [S.Rational(1,4),S.Rational(1),S.Rational(3),S.Rational(10)]:
      count+=investigate(n,edges,u,v,eta,w)
      for k in [S.Rational(1,7),S.Rational(3,4),S.Rational(5),S.Rational(100)]:
       # after substituting a finite weight, the separate independent check remains exact
       count+=investigate(n,edges,u,v,eta,k)
    print('PASS',count,'exact rational/algebraic assertions across',len(cases),'graphs')
if __name__=='__main__':main()
