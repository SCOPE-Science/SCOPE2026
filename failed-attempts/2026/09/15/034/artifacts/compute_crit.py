"""Critical points + Hessian type of Pascaleff-Tonkonog torus potential for Bl_4 CP^2 in char 5.

W = (1+x+y)(1+1/x)(1+1/y) - 3 in k[x^+-1,y^+-1], k = alg. closure of F5.
Critical eqs: F1 = x*Nx - N = 0, F2 = y*Ny - N = 0 with N=(1+x+y)(x+1)(y+1),
since x*dW/dx = (x*Nx-N)/(x*y), y*dW/dy = (y*Ny-N)/(x*y).
"""
import json

P = 5

def mod(a):
    return a % P

# Represent polynomials as dicts {(i,j): c}
def add(A,B,s=1):
    C=dict(A)
    for k,v in B.items():
        C[k]=(C.get(k,0)+s*v)%P
        if C[k]==0: del C[k]
    return C
def mul(A,B):
    C={}
    for (i1,j1),c1 in A.items():
        for (i2,j2),c2 in B.items():
            k=(i1+i2,j1+j2); C[k]=(C.get(k,0)+c1*c2)%P
            if C[k]==0: del C[k]
    return C
def dx(A):
    C={}
    for (i,j),c in A.items():
        if i>0:
            C[(i-1,j)]=(C.get((i-1,j),0)+i*c)%P
            if C[(i-1,j)]==0: del C[(i-1,j)]
    return C
def dy(A):
    C={}
    for (i,j),c in A.items():
        if j>0:
            C[(i,j-1)]=(C.get((i,j-1),0)+j*c)%P
            if C[(i,j-1)]==0: del C[(i,j-1)]
    return C

x={(1,0):1}; y={(0,1):1}; one={(0,0):1}
s=add(add(one,x),y)            # 1+x+y
xp1=add(x,one); yp1=add(y,one)
t=mul(mul(x,y),one)            # placeholder
t=add(add(mul(x,y),x),add(y,one))  # xy+x+y+1
N=mul(s,mul(xp1,yp1))
Nx=dx(N); Ny=dy(N)
F1=add(mul(x,Nx),N,s=-1)       # x*Nx - N
F2=add(mul(y,Ny),N,s=-1)       # y*Ny - N

def fmt(A):
    ts=sorted(A.items(),key=lambda kv:(kv[0][0]+kv[0][1],kv[0]))
    out=[]
    for (i,j),c in ts:
        out.append(f"{c}*x^{i}y^{j}")
    return " + ".join(out) if out else "0"

print("N =",fmt(N))
print("F1=",fmt(F1))
print("F2=",fmt(F2))

# Brute force zeros over F5
pts=[]
for a in range(5):
    for b in range(5):
        def ev(A):
            return sum(c*pow(a,i,P)*pow(b,j,P) for (i,j),c in A.items())%P
        if ev(F1)==0 and ev(F2)==0:
            pts.append((a,b))
print("affine zeros (F5):",pts)

# values of W at torus points: W+3 = N/(x*y)
def ev(A,a,b):
    return sum(c*pow(a,i,P)*pow(b,j,P) for (i,j),c in A.items())%P
for (a,b) in pts:
    if a!=0 and b!=0:
        n=ev(N,a,b); d=(a*b)%P
        w3=(n*pow(d,P-2,P))%P
        print(f"pt=({a},{b}) N={n} W+3={w3} W=lambda={(w3-3)%P}")

# Hessian in log coords: H11=thx thx W, etc. Compute polys:
# thx W = F1/(xy), thy W = F2/(xy). thx = x d/dx.
# H11 = x*d/dx(F1/(xy)) ; H12 = x*d/dx(F2/(xy)) ; H22 = y*d/dy(F2/(xy))
# Write G1=F1, with Q=xy. x*d(G/Q) = (x*Gx*Q - G*x*Qx)/Q^2 = (x*Gx - G)/Q since x*Qx=Q.
# So numerators: H11num = x*dx(F1)-F1 ; H12num = x*dx(F2)-F2 ; H21num = y*dy(F1)-F1; H22num = y*dy(F2)-F2,
# all over Q=xy.
Q=mul(x,y)
H11=add(mul(x,dx(F1)),F1,s=-1)
H12=add(mul(x,dx(F2)),F2,s=-1)
H21=add(mul(y,dy(F1)),F1,s=-1)
H22=add(mul(y,dy(F2)),F2,s=-1)
print("H11num=",fmt(H11)); print("H12num=",fmt(H12)); print("H21num=",fmt(H21)); print("H22num=",fmt(H22))
for (a,b) in pts:
    if a!=0 and b!=0:
        q=(a*b)%P
        h11=ev(H11,a,b)*pow(q,P-2,P)%P
        h12=ev(H12,a,b)*pow(q,P-2,P)%P
        h22=ev(H22,a,b)*pow(q,P-2,P)%P
        det=(h11*h22-h12*h12)%P
        print(f"H({a},{b})=[[{h11},{h12}],[{h12},{h22}]] det={det}")

# Groebner check via brute-force counting + factor F1-F2
D=add(F1,F2,s=-1)
print("F1-F2 =",fmt(D))
