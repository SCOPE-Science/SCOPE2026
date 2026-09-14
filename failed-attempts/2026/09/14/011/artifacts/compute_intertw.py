import sympy as sp
from itertools import permutations, product

def perm_op(p):
    M = sp.zeros(27,27)
    for i0 in range(3):
        for i1 in range(3):
            for i2 in range(3):
                src=(i0,i1,i2); dst=(src[p[0]],src[p[1]],src[p[2]])
                M[dst[0]*9+dst[1]*3+dst[2], i0*9+i1*3+i2]=1
    return M
I27=sp.eye(27)
C=(I27+perm_op((1,0,2)))*(I27-perm_op((2,1,0)))
print("rank C=",C.rank(),flush=True)
B=sp.Matrix.hstack(*C.columnspace())
BTBinv=(B.T*B).inv()
def kron3(A):
    K=sp.zeros(27,27)
    for i0 in range(3):
        for i1 in range(3):
            for i2 in range(3):
                for j0 in range(3):
                    for j1 in range(3):
                        for j2 in range(3):
                            K[i0*9+i1*3+i2,j0*9+j1*3+j2]=A[i0,j0]*A[i1,j1]*A[i2,j2]
    return K
def hook_mat(A):
    return BTBinv*(B.T*kron3(A)*B)

def monoms(d):
    L=[]
    for a1 in range(d+1):
        for a2 in range(d+1-a1):
            L.append((a1,a2,d-a1-a2))
    return L
def sym_mat(A,d):
    mons=monoms(d); idx={m:i for i,m in enumerate(mons)}; n=len(mons)
    M=sp.zeros(n,n)
    for bi,beta in enumerate(mons):
        poly={(0,0,0):sp.Integer(1)}
        for i in range(3):
            base={(1,0,0):A[i,0],(0,1,0):A[i,1],(0,0,1):A[i,2]}
            pw={(0,0,0):sp.Integer(1)}
            for _ in range(beta[i]):
                npw={}
                for e1,c1 in pw.items():
                    for e2,c2 in base.items():
                        e=(e1[0]+e2[0],e1[1]+e2[1],e1[2]+e2[2])
                        npw[e]=npw.get(e,sp.Integer(0))+c1*c2
                pw=npw
            npoly={}
            for e1,c1 in poly.items():
                for e2,c2 in pw.items():
                    e=(e1[0]+e2[0],e1[1]+e2[1],e1[2]+e2[2])
                    npoly[e]=npoly.get(e,sp.Integer(0))+c1*c2
            poly=npoly
        for e,c in poly.items():
            if c!=0:
                M[bi,idx[e]]=c
    return M

def intertw_dim(Hmats, Sms):
    n=Sms[0].rows; N=8*n
    # var index (a,alpha) -> a*n+alpha
    rows=[]
    for Hm,Sm in zip(Hmats,Sms):
        for a in range(8):
            for alpha in range(n):
                row=[sp.Integer(0)]*N
                for gam in range(n):
                    row[a*n+gam]+=Sm[gam,alpha]
                for b in range(8):
                    row[b*n+alpha]-=Hm[a,b]
                rows.append(row)
    Mall=sp.Matrix(rows)
    return N-Mall.rank()

def E(i,j,s=1):
    M=sp.eye(3); M[i,j]=s; return M

SLgens=[E(0,1),E(0,2),E(1,0),E(1,2),E(2,0),E(2,1)]
H3=[]
verts=[[0,0,0],[1,0,0],[0,1,0],[0,0,1]]
for perm in permutations(range(4)):
    b=verts[perm[0]]
    cols=[[verts[k][r]-b[r] for r in range(3)] for k in (perm[1],perm[2],perm[3])]
    A=sp.Matrix(cols).T
    if A.det()==1:
        H3.append(A)
print("H3=",len(H3),flush=True)
V2=[(0,0,0),(1,0,0),(0,1,0)]
G2=[]
for perm in permutations(range(3)):
    b=V2[perm[0]]
    c1=(V2[perm[1]][0]-b[0],V2[perm[1]][1]-b[1],0)
    c2=(V2[perm[2]][0]-b[0],V2[perm[2]][1]-b[1],0)
    det2=c1[0]*c2[1]-c1[1]*c2[0]
    A=sp.Matrix([[c1[0],c2[0],0],[c1[1],c2[1],0],[0,0,det2]])
    assert A.det()==1
    G2.append(A)
S1=sp.eye(3); S1[0,2]=1
S2=sp.eye(3); S2[1,2]=1
G2+=[S1,S2]
D1=sp.diag(-1,-1,1)
H1=[E(0,1),E(0,2),E(1,2),E(2,1),D1]
groups={"SL":SLgens,"H3-tet":H3,"G2-tri":G2,"H1-line":H1}
for name,gens in groups.items():
    Hmats=[hook_mat(A) for A in gens]
    dims=[]
    for d in range(4):
        Sms=[sym_mat(A,d) for A in gens]
        dims.append(intertw_dim(Hmats,Sms))
    print(name,"dims d=0..3:",dims,flush=True)
print("DONE",flush=True)
