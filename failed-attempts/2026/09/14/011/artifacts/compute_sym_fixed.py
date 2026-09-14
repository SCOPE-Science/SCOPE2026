import sympy as sp
from itertools import permutations, product

def perm_op(p):
    M = sp.zeros(27,27)
    for i0 in range(3):
        for i1 in range(3):
            for i2 in range(3):
                src=(i0,i1,i2); dst=(src[p[0]],src[p[1]],src[p[2]])
                s=i0*9+i1*3+i2; d=dst[0]*9+dst[1]*3+dst[2]
                M[d,s]=1
    return M
I27=sp.eye(27)
C=(I27+perm_op((1,0,2)))*(I27-perm_op((2,1,0)))
print("rank C=",C.rank(),flush=True)
col_basis=C.columnspace()
B=sp.Matrix.hstack(*col_basis)
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

# monomial basis for Sym^d in 3 vars: exponents
def monoms(d):
    L=[]
    for a1 in range(d+1):
        for a2 in range(d+1-a1):
            a3=d-a1-a2
            L.append((a1,a2,a3))
    return L
from math import comb
# S_d(A): coefficients s.t. (A t)^alpha = sum_beta S_d(A)[alpha,beta] t^beta? We need F S = H F with F row-vector over monomials.
# Represent polynomial vector: F(t)=sum_beta F_beta t^beta. Then F(A t)=sum_beta F_beta (A t)^beta = sum_alpha (sum_beta F_beta M_{beta,alpha}) t^alpha where (A t)^beta = sum_alpha M_{beta,alpha} t^alpha.
# So condition F M(A) = H(A) F, with M(A) dim x dim.
def sym_mat(A,d):
    # A 3x3 sympy
    mons=monoms(d)
    idx={m:i for i,m in enumerate(mons)}
    n=len(mons)
    M=sp.zeros(n,n)
    # (A t)^beta = prod_i (sum_j A[i,j] t_j)^{beta_i}. Expand via multinomial: coefficient of t^alpha.
    # brute force via polynomial multiplication using dicts
    for bi,beta in enumerate(mons):
        # poly as dict exp->coeff, start 1
        poly={(0,0,0):sp.Integer(1)}
        for i in range(3):
            # linear form L_i = sum_j A[i,j] t_j, raise to beta_i
            base={ (1 if j==0 else 0, 1 if j==1 else 0, 1 if j==2 else 0): A[i,j] for j in range(3)}
            # power
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

def intertwiner_dim(Hmats,Smd_list):
    # unknowns F 8 x n. equations F S = H F per generator. Build matrix rows*(8n) unknowns.
    n=Smd_list[0].shape[0]
    N=8*n
    rows=[]
    for Hm,Sm in zip(Hmats,Smd_list):
        # F*Sm - Hm*F = 0. vec(F) with F flattened row-major? Use kron: vec(F S) = (S^T \otimes I_8) vec(F); vec(H F) = (I_n \otimes H) vec(F).
        left = sp.tensorproduct(Sm.T, sp.eye(8)) - sp.tensorproduct(sp.eye(n), Hm)
        # tensorproduct gives TensorProduct object? convert to Matrix
        left = sp.Matrix(left)
        rows.append(left)
    Mall=sp.Matrix.vstack(*rows)
    return N - Mall.rank(), Mall.rank(), N

def E(i,j,s=1):
    M=sp.eye(3); M[i,j]=s; return M

# groups (subsets sufficient)
SLgens=[E(0,1),E(0,2),E(1,0),E(1,2),E(2,0),E(2,1)]
# line stabilizer subset: shears + SL2 block + sign
D1=sp.diag(-1,-1,1)
H1gens=[E(0,1),E(0,2),E(1,2),E(2,1),D1, sp.Matrix([[-1,0,0],[0,-1,0],[0,0,1]])]
# check membership: first col +-e1, det 1
for A in H1gens:
    assert A.det()==1 and (tuple(A.col(0))==((1,0,0)) or tuple(A.col(0))==((-1,0,0))), A
# triangle affine-linear subset: 6 vertex perms (third col (0,0,r)) + 2 normal shears
V2=[(0,0,0),(1,0,0),(0,1,0)]
G2=[]
for perm in permutations(range(3)):
    b=V2[perm[0]]
    c1=(V2[perm[1]][0]-b[0],V2[perm[1]][1]-b[1],V2[perm[1]][2]-b[2])
    c2=(V2[perm[2]][0]-b[0],V2[perm[2]][1]-b[1],V2[perm[2]][2]-b[2])
    # 2x2 det
    det2=c1[0]*c2[1]-c1[1]*c2[0]
    assert det2 in (1,-1)
    r=det2
    A=sp.Matrix([[c1[0],c2[0],0],[c1[1],c2[1],0],[0,0,r]])
    assert A.det()==1
    G2.append(A)
# normal shears fixing triangle pointwise
S1=sp.eye(3); S1[0,2]=1
S2=sp.eye(3); S2[1,2]=1
G2 += [S1,S2]
print("G2 count",len(G2))
# T3 rotations: 12
verts=[[0,0,0],[1,0,0],[0,1,0],[0,0,1]]
H3=[]
for perm in permutations(range(4)):
    b=verts[perm[0]]
    cols=[]
    for k in (perm[1],perm[2],perm[3]):
        cols.append([verts[k][r]-b[r] for r in range(3)])
    A=sp.Matrix(cols).T
    if A.det()==1:
        H3.append(A)
print("H3 count",len(H3))

groups={"SL":SLgens,"H1-line":H1gens,"G2-tri":G2,"H3-tet":H3}
for name,gens in groups.items():
    Hmats=[hook_mat(A) for A in gens]
    line=[]
    for d in range(4):
        Sm=[sym_mat(A,d) for A in gens]
        dim,rk,N=intertwiner_dim(Hmats,Sm)
        line.append(dim)
    print(name,"intertwiner dims d=0..3:",line,flush=True)
