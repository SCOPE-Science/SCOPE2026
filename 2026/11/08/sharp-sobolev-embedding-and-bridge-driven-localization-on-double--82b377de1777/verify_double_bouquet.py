#!/usr/bin/env python3
"""Independent exact piecewise-quadratic Green-function checks for finite metric networks."""
from fractions import Fraction as F
from sympy import Matrix, Rational

def formula(left,right,bridge):
    a=[F(v) for v in left]; c=[F(v) for v in right]; b=F(bridge)
    A=sum(a); C=sum(c); L=A+C+b
    Q=sum(x*x for x in a+c); T=sum(x**3 for x in a+c)
    J=L*Q/3-T/6+b**3/3+b*b*(A+C)+2*A*C*b
    M0=Q/6+b*b/2
    ML=M0+b*C+max(x*(L-x)/4 for x in a)
    MR=M0+b*A+max(x*(L-x)/4 for x in c)
    K=max(ML,MR)/L-J/(2*L*L)
    per_cycle=[(Q/6+b*b/2+b*C+z*(L-z)/4)/L-J/(2*L*L) for z in a]+[(Q/6+b*b/2+b*A+z*(L-z)/4)/L-J/(2*L*L) for z in c]
    return K,ML,MR,per_cycle

def direct(left,right,bridge):
    # Circle of length s is replaced by two parallel semicircle edges of length s/2.
    # Solve for the exact quadratic Green representer (second derivative 1/L).
    left=[F(x) for x in left];right=[F(x) for x in right];b=F(bridge)
    lengths=left+right
    N=2+len(lengths); edges=[(0,1,b)]
    for z,a in enumerate(left):edges.extend([(0,z+2,a/2),(0,z+2,a/2)])
    for z,a in enumerate(right):edges.extend([(1,z+2+len(left),a/2),(1,z+2+len(left),a/2)])
    total=sum(s for _,_,s in edges)
    mat=[[F(0) for _ in range(N)] for _ in range(N)]
    mass=[F(0) for _ in range(N)]
    for i,j,s in edges:
        mat[i][i]+=1/s;mat[j][j]+=1/s
        mat[i][j]-=1/s;mat[j][i]-=1/s
        mass[i]+=s/2;mass[j]+=s/2
    out=[]
    for x in range(2,N):
        v=[F(int(i==x))-mass[i]/total for i in range(1,N)]
        mat1=Matrix([[Rational(mat[i][j].numerator,mat[i][j].denominator) for j in range(1,N)] for i in range(1,N)])
        vec=Matrix([Rational(z.numerator,z.denominator) for z in v]);sol=mat1.inv()*vec
        U=[F(0)]+[F(int(t.p),int(t.q)) for t in sol]
        integral=F(0)
        for i,j,s in edges:
            # mean of linear endpoints plus the exact quadratic interior particular.
            integral+=s*(U[i]+U[j])/2-s*s*s/(12*total)
        out.append(U[x]-integral/total)
    return out

def main():
    cases=0;phase=0;ties=0
    for r in (1,2,3):
      for s in (1,2,3):
       for z in range(5):
        left=[1+((2*i+z)%6) for i in range(r)]
        right=[1+((3*i+z+1)%5) for i in range(s)]
        for b in (F(1,5),F(1),F(7,3)):
         predicted,ML,MR,expected=formula(left,right,b);vals=direct(left,right,b)
         assert all(v>0 for v in vals)
         assert vals==expected, (left,right,b,vals,expected)
         assert max(vals)==predicted,(left,right,b,max(vals),predicted)
         # independent tie/winner checks based on exact best K values at the two hubs
         assert (max(vals[:r])>=max(vals[r:]))==(ML>=MR)
         if ML==MR:ties+=1
         else:phase+=1
         cases+=1
    # Explicit bridge-length crossing: three length-3 loops versus one length-2 loop.
    Lh=[3,3,3];Rh=[2]
    for b,side in [(F(1,9),'left'),(F(2,9),'tie'),(F(1),'right')]:
      _,IL,IR,_=formula(Lh,Rh,b)
      assert ('left' if IL>IR else 'tie' if IL==IR else 'right')==side
      out=direct(Lh,Rh,b)
      assert max(out)==formula(Lh,Rh,b)[0]
    print('INDEPENDENT_EXACT_PIECEWISE_QUADRATIC_GREEN_CHECKS_OK',cases,'strict_hub_compares',phase,'ties',ties)
    print('BRIDGE_LENGTH_LOCALIZATION_TRANSITION_OK', '2/9')
    print('ALL_DOUBLE_BOUQUET_CHECKS_OK')
if __name__=='__main__': main()
