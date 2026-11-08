"""Exact finite checks and symbolic certificates for weighted friendship-network pinning.
Run: python verification.py  (requires SymPy).  No network access.
"""
import itertools
from sympy import (symbols, Matrix, Rational, factor, simplify, expand, Poly,
                   S, together)

m,k,r=symbols('m k r', integer=True, positive=True)

def module(pin):
    A=Matrix([[1+r+k*pin[0],-r],[-r,1+r+k*pin[1]]])
    V=A.inv(); o=Matrix([1,1])
    return [simplify(V.trace()),simplify((o.T*V*o)[0]),simplify((o.T*V*V*o)[0])]

n0=module((0,0)); n1=module((1,0)); n2=module((1,1))

def J(groups,h):
    tr=sum(q*values[0] for q,values in groups)
    b=sum(q*values[1] for q,values in groups)
    c=sum(q*values[2] for q,values in groups)
    return factor(tr+(1+c)/(2*m+k*h-b))

H=J([(m-1,n0),(1,n1)],1)
D=J([(m-2,n0),(2,n1)],0)
SAME=J([(m-1,n0),(1,n2)],0)
P=factor((D-H)*2*(2*r+1)*(k*r+k+2*r+1)*(k*r+k+4*r+2))
Q=factor((SAME-D)*2*(2*r+1)*(k+2*r+1)*(k*r+k+2*r+1)/r)
p2=(k*k+1)+(-k*k-8*k+1)*r+(-5*k*k-26*k-8)*r*r-(k+6)*(3*k+2)*r**3
p3=(3*k*k+4*k+3)+(5*k*k+8*k+11)*r+(k-4)*(k-2)*r*r+(-k*k-12*k-4)*r**3
p4=(k-2)**2*r**3+(7*k*k+14*k+24)*r*r+(11*k*k+24*k+21)*r+(5*k*k+8*k+5)
assert expand(P.subs(m,2)-p2)==0
assert expand(P.subs(m,3)-p3)==0
assert expand(P.subs(m,4)-p4)==0
assert expand(P-p4-2*(m-4)*(r+1)*(k*r+k+2*r+1)**2)==0
assert all(a>0 for a in Poly(Q,m,k,r).coeffs())
assert expand(p2.subs(r,Rational(1,4))-(25*k*k-252*k+36)/64)==0
print('symbolic identities and positive-coefficient certificate: passed')

checks=0
for mm in range(2,7):
    for rr in [Rational(1,20),Rational(1,4),Rational(1),Rational(2),Rational(9)]:
        for kk in [Rational(1,10),Rational(1),Rational(3),Rational(20)]:
            N=2*mm+1
            L=Matrix.zeros(N)
            for petal in range(mm):
                i,j=1+2*petal,2+2*petal
                for a,b,w in [(0,i,S.One),(0,j,S.One),(i,j,rr)]:
                    L[a,a]+=w;L[b,b]+=w;L[a,b]-=w;L[b,a]-=w
            vals={}
            for name,leaders in [('H',(0,1)),('D',(1,3)),('S',(1,2))]:
                G=L.copy()
                for index in leaders: G[index,index]+=kk
                direct=G.inv().trace()
                expression={'H':H,'D':D,'S':SAME}[name].subs({m:mm,r:rr,k:kk})
                assert simplify(direct-expression)==0,(mm,rr,kk,name,direct,expression)
                vals[name]=direct;checks+=1
            poly=P.subs({m:mm,r:rr,k:kk})
            assert (vals['D']-vals['H']>0)==(poly>0) if poly != 0 else vals['D']==vals['H']
            assert vals['S']>vals['D']
print('exact grounded-matrix comparisons:',checks,'passed')

# Exhaustive combinatorial classification on representative graphs; all pairs.
allpairs=0
for mm in [2,3,4]:
    for rr,kk in [(Rational(1,4),Rational(1,100)),(Rational(1,4),Rational(1)),
                  (Rational(1,4),Rational(100)),(Rational(2),Rational(1))]:
        N=2*mm+1;L=Matrix.zeros(N)
        for i in range(mm):
            a,b=2*i+1,2*i+2
            for x,y,w in [(0,a,S.One),(0,b,S.One),(a,b,rr)]:
                L[x,x]+=w;L[y,y]+=w;L[x,y]-=w;L[y,x]-=w
        reps={'H':H,'D':D,'S':SAME}
        for aa,bb in itertools.combinations(range(N),2):
            if 0 in (aa,bb): kind='H'
            elif (aa-1)//2==(bb-1)//2:kind='S'
            else:kind='D'
            A=L.copy(); A[aa,aa]+=kk;A[bb,bb]+=kk
            assert A.inv().trace()==reps[kind].subs({m:mm,r:rr,k:kk})
            allpairs+=1
print('additional exhaustive pair classifications:',allpairs,'passed')
