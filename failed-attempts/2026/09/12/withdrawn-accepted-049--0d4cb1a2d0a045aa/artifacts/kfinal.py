from fractions import Fraction as Fr
import sympy as sp
ZERO=(Fr(0),Fr(0),Fr(0)); ONE=(Fr(1),Fr(0),Fr(0))
def add(x,y): return (x[0]+y[0],x[1]+y[1],x[2]+y[2])
def neg(x): return (-x[0],-x[1],-x[2])
def sub(x,y): return (x[0]-y[0],x[1]-y[1],x[2]-y[2])
def mul(x,y):
    a0,a1,a2=x; b0,b1,b2=y
    c=[Fr(0)]*5
    a=[a0,a1,a2]; b=[b0,b1,b2]
    for i in range(3):
        for j in range(3):
            c[i+j]+=a[i]*b[j]
    c0,c1,c2,c3,c4=c
    return (c0+c3-c4, c1+2*c3-c4, c2-c3+3*c4)
def matmul(A,B):
    return ((add(mul(A[0][0],B[0][0]),mul(A[0][1],B[1][0])),add(mul(A[0][0],B[0][1]),mul(A[0][1],B[1][1]))),
            (add(mul(A[1][0],B[0][0]),mul(A[1][1],B[1][0])),add(mul(A[1][0],B[0][1]),mul(A[1][1],B[1][1]))))
def mattr(A): return add(A[0][0],A[1][1])
def matdet(A): return sub(mul(A[0][0],A[1][1]),mul(A[0][1],A[1][0]))
def matinv(A):
    assert matdet(A)==ONE, ("det",matdet(A))
    return ((A[1][1],neg(A[0][1])),(neg(A[1][0]),A[0][0]))
T=(Fr(0),Fr(1),Fr(0)); T2=mul(T,T)
p0=sub((Fr(2),Fr(0),Fr(0)),T2); pt=neg(T); TWO=(Fr(2),Fr(0),Fr(0))
M0=((ZERO,neg(ONE)),(ONE,p0))
M1=((ONE,ONE),(sub(p0,TWO),sub(p0,ONE)))
# candidate d=(-1,0,0), e=(0,-2,1); compute f = Mq^{-1}(rhs - Mc d - E(e)q) with CORRECT Mc=mult(t-t^2)
def ematC(ex,ey,ez):
    c1=(ex,ey,ez); c2=(ez,ex+2*ez,ey-ez); c3=(ey-ez,2*ey-ez,ex-ey+3*ez)
    return (c1,c2,c3)
def mapp(M,v):
    c1,c2,c3=M
    return (v[0]*c1[0]+v[1]*c2[0]+v[2]*c3[0], v[0]*c1[1]+v[1]*c2[1]+v[2]*c3[1], v[0]*c1[2]+v[1]*c2[2]+v[2]*c3[2])
Mc=ematC(Fr(0),Fr(1),Fr(-1)); Mq=ematC(Fr(1),Fr(0),Fr(-1))
d=(Fr(-1),Fr(0),Fr(0)); e=(Fr(0),Fr(-2),Fr(1))
Me=ematC(*e)
q=(Fr(1),Fr(0),Fr(-1)); rhs=(Fr(1),Fr(2),Fr(-2))
Mc_d=mapp(Mc,d); Me_q=mapp(Me,q)
target=(rhs[0]-Mc_d[0]-Me_q[0],rhs[1]-Mc_d[1]-Me_q[1],rhs[2]-Mc_d[2]-Me_q[2])
S=sp.Matrix([[Mq[j][i] for j in range(3)] for i in range(3)])
B=S.inv()
Qm=tuple(tuple(B[i,j] for i in range(3)) for j in range(3))
f=mapp(Qm,target)
print("f=",f)
Mt=((d,e),(f,sub(pt,d)))
print("detMt=",matdet(Mt),"trMt=",mattr(Mt))
P=matmul(matmul(Mt,M1),M0)
print("detP=",matdet(P),"trP=",mattr(P),"want pt=",pt)
Minf=matinv(P)
print("Minf tr=",mattr(Minf))
print("M0 tr/det:",mattr(M0),matdet(M0))
print("M1 tr/det:",mattr(M1),matdet(M1))
print("Mt=",Mt)
print("Minf=",Minf)
