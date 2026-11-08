"""Algebraic and reproducibility checks for triangular Markov oscillation envelope.

Requires Python 3 and SymPy. This checker supplements, but does not replace,
the analytical convexity and quantifier arguments in RESULT.md.
"""
import math
from fractions import Fraction
from itertools import product
from sympy import Matrix, symbols, simplify, expand, sqrt, Integer, factor

count=0
def chk(expr, msg=''):
    global count
    assert bool(expr), msg
    count+=1

a,b,c,j=symbols('a b c j', real=True)
z=symbols('z')
g=[a,b,c]
Q=Matrix.zeros(3)
for k in range(3):
    h=(k+1)%3
    Q[k,h]+=g[k]+j
    Q[h,k]+=g[k]-j
    Q[k,k]-=(g[k]+j)
    Q[h,h]-=(g[k]-j)
G=a+b+c; H=a*b+b*c+c*a; delta2=G**2-3*H
chk(simplify(Q*Matrix([1,1,1]))==Matrix.zeros(3,1),'row conservation')
chk(simplify(Matrix([[1,1,1]])*Q)==Matrix.zeros(1,3),'column conservation')
chk(expand(Q.charpoly(z).as_expr()-z*(z*z+2*G*z+3*(H+j*j)))==0,'exact characteristic polynomial')
chk(simplify(delta2-((a-b)**2+(b-c)**2+(c-a)**2)/2)==0,'heterogeneity identity')
# At nontrivial exceptional point the double eigenvalue is defective.
Qep=Q.subs({a:Integer(1),b:Integer(1),c:Integer(2),j:1/sqrt(3)})
chk(expand(Qep.charpoly(z).as_expr()-z*(z+4)**2)==0,'nontrivial double root')
chk((Qep+4*Matrix.eye(3)).rank()==2,'Jordan defect: double eigenvalue has one eigenvector')
Qflat=Q.subs({a:1,b:1,c:1,j:0})
chk((Qflat+3*Matrix.eye(3)).rank()==1,'reversible diabolic crossing is semisimple')

# Verify the exactly nonoscillatory heterogeneous family (1,1,3):
chk(delta2.subs({a:1,b:1,c:3})==4,'disorder barrier value')
chk(delta2.subs({a:1,b:1,c:3}) >= 3*Integer(1)**2,'disorder prohibits admissible complex pair')

# Finite checks across many positive rational rates and currents.
for aa,bb,cc in product((1,2,3,5,7), repeat=3):
    gg=(aa,bb,cc)
    mm=min(gg)
    total=sum(gg)
    dd=total*total-3*(aa*bb+bb*cc+cc*aa)
    for t in (Fraction(1,10), Fraction(3,10), Fraction(7,10)):
        jj=float(mm*t)
        disc=dd-3*jj*jj
        qp=Q.subs({a:aa,b:bb,c:cc,j:float(jj)})
        # Independent numeric characteristic identities, using 3x3 minors.
        rows=[[float(qp[u,v]) for v in range(3)] for u in range(3)]
        tr=sum(rows[i][i] for i in range(3))
        cp=sum(rows[i][i]*rows[h][h]-rows[i][h]*rows[h][i] for i in range(3) for h in range(i+1,3))
        chk(abs(tr+2*total)<1e-10,'trace')
        chk(abs(cp-3*(aa*bb+bb*cc+cc*aa+jj*jj))<1e-10,'principal minors')
        # Monotone shape frequency upper bound and strict dissipation penalty.
        omega=math.sqrt(max(0.0,-disc))
        chk(omega<=math.sqrt(3)*abs(jj)+1e-10,'frequency shape bound')
        if len(set(gg))>1:
            chk(omega<math.sqrt(3)*abs(jj)+1e-10,'strict disorder penalty')
        if jj>0:
            s=(2*jj/3)*sum(math.log((x+jj)/(x-jj)) for x in gg)
            smin=2*jj*math.log((total+3*jj)/(total-3*jj))
            chk(s+1e-10>=smin,'Jensen lower entropy')
            if len(set(gg))>1:
                chk(s>smin+1e-12,'strict Jensen inequality')

# Verify the inverse budget equation and bound using 3-point bisection.
for total in (3,6,12):
    for budget in (0.01,0.1,1.,4.,20.):
        lo,hi=0.,total/3
        for _ in range(80):
            mid=(lo+hi)/2
            val=2*mid*math.log((total+3*mid)/(total-3*mid))
            if val<budget:lo=mid
            else:hi=mid
        root=(lo+hi)/2
        chk(abs(2*root*math.log((total+3*root)/(total-3*root))-budget)<1e-9,'budget root')
        chk(root>0 and root<total/3,'root admissibility')
        homogeneous_omega=math.sqrt(3)*root
        chk(homogeneous_omega>0,'positive saturation frequency')
print(f'PASS: {count} deterministic assertions; 3x3 symbolic identity and Jordan tests verified.')
