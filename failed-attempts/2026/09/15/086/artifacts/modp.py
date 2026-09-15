"""Fast exact arithmetic mod p=17 (i=4, zeta8=2). Rebuild M(t), Burnside image-dim (one-sided char-0 simplicity cert), exact kernels."""
P=17; I=4; Z=2
def add(a,b): return (a+b)%P
def mul(a,b): return (a*b)%P
def inv(a):
    assert a%P!=0; return pow(a,P-2,P)
def neg(a): return (-a)%P
def mat_eye(n): return [[1 if i==j else 0 for j in range(n)] for i in range(n)]
def mat_mul(A,B):
    n=len(A); m=len(B[0]); k=len(B)
    C=[[0]*m for _ in range(n)]
    for i in range(n):
        for l in range(k):
            if A[i][l]:
                for j in range(m): C[i][j]=(C[i][j]+A[i][l]*B[l][j])%P
    return C
def mat_vec(M,v): return [sum(M[i][j]*v[j] for j in range(len(v)))%P for i in range(len(M))]
def rref_rank(rows):
    M=[list(r) for r in rows]; m=len(M)
    n=len(M[0]) if m else 0
    r=0; piv=0
    for c in range(n):
        p=None
        for i in range(r,m):
            if M[i][c]%P!=0: p=i; break
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        d=inv(M[r][c]); M[r]=[(x*d)%P for x in M[r]]
        for i in range(m):
            if i!=r and M[i][c]%P!=0:
                f=M[i][c]; M[i]=[(x-f*y)%P for x,y in zip(M[i],M[r])]
        piv+=1; r+=1
    return piv
def ker(M):
    n=len(M)
    R=[list(r) for r in M]; pivcols=[]; r=0
    pivrow={}
    for c in range(n):
        p=None
        for i in range(r,n):
            if R[i][c]%P!=0: p=i; break
        if p is None: continue
        R[r],R[p]=R[p],R[r]
        d=inv(R[r][c]); R[r]=[(x*d)%P for x in R[r]]
        for i in range(n):
            if i!=r and R[i][c]%P!=0:
                f=R[i][c]; R[i]=[(x-f*y)%P for x,y in zip(R[i],R[r])]
        pivrow[c]=r; pivcols.append(c); r+=1
    free=[c for c in range(n) if c not in pivrow]
    out=[]
    for f in free:
        v=[0]*n; v[f]=1
        for c,ri in pivrow.items(): v[c]=neg(R[ri][f])
        out.append(v)
    return out
def contains(cols,v):
    if not cols: return all(x==0 for x in v)
    n=len(v); k=len(cols)
    B=[[cols[j][i] for j in range(k)] for i in range(n)]
    return rref_rank(B)==rref_rank(B+[v])
def basis_of(vecs):
    out=[]
    for v in vecs:
        if not contains(out,v): out.append(v)
    return out
def spin(gens,seeds):
    S=basis_of(seeds)
    while True:
        grew=False
        for g in gens:
            for v in list(S):
                w=mat_vec(g,v)
                if not contains(S,w): S.append(w); grew=True
        S=basis_of(S)
        if not grew or len(S)==len(gens[0]): return S
# --- M(t) mod p: replicate BLZ recursion with ints ---
Q=I
import sys
sys.path.insert(0,'output/artifacts')
from engine import WORDS,LENS,descend,act_s,Qpoly,left_mult_by_s
def terms(s,w):
    out=[]
    for c,u in left_mult_by_s(s,w):
        if abs(c-1)<1e-9: out.append((1,u))
        elif abs(c-1j)<1e-9: out.append((Q,u))
        elif abs(complex(c-(1j-1)))<1e-9: out.append(((Q-1)%P,u))
        else: raise AssertionError(c)
    return out
def gp(g,k):
    if k==0: return 1
    r=1
    for _ in range(abs(k)): r=(r*g)%P
    return r if k>0 else inv(r)
def th(x,w,t):
    n=12
    if w==0:
        r=[0]*n; r[0]=(gp(t[0],x[0])*gp(t[1],x[1]))%P; return r
    s,v=descend(w)
    sx=act_s(s,x)
    rec=th(sx,v,t)
    out=[0]*n
    for u,bu in enumerate(rec):
        if bu:
            for (c,z) in terms(s,u): out[z]=(out[z]+bu*c)%P
    Qp=Qpoly(x,s)
    if Qp:
        for y,cy in Qp.items():
            c=int(round(cy.real))
            r2=th(y,v,t)
            for u,bu in enumerate(r2):
                if bu: out[u]=(out[u]+bu*c*(Q-1))%P
    return out
def Mof(t):
    n=12
    T1=[[0]*n for _ in range(n)]; T2=[[0]*n for _ in range(n)]
    for w in range(n):
        for c,u in terms(1,w): T1[u][w]=(T1[u][w]+c)%P
        for c,u in terms(2,w): T2[u][w]=(T2[u][w]+c)%P
    X1=[[0]*n for _ in range(n)]; X2=[[0]*n for _ in range(n)]
    for w in range(n):
        r1=th((1,0),w,t); r2=th((0,1),w,t)
        for u in range(n): X1[u][w]=r1[u]; X2[u][w]=r2[u]
    return [T1,T2,X1,X2]
def image_dim(gens,max_rounds=80):
    n=len(gens[0])
    def flat(M): return [M[i][j] for i in range(n) for j in range(n)]
    bl=[flat(mat_eye(n))]+[flat(g) for g in gens]
    r=rref_rank(bl)
    mats=[mat_eye(n)]+list(gens)
    indep=list(mats)
    for _ in range(max_rounds):
        grew=False
        for g in gens:
            for X in list(indep):
                Y=mat_mul(g,X)
                f=flat(Y)
                if rref_rank([flat(Z) for Z in indep]+[f])>len(indep):
                    indep.append(Y); grew=True
                if len(indep)==n*n: return 144
        if not grew: break
    return len(indep)
if __name__=="__main__":
    tests={"gen(2,3)":(2,3),"t11":(1,1),"t1m1":(1,16),"ti1":(I,1),"t1i":(1,I),"tz1":(Z,1),"tzz":(Z,Z)}
    for name,t in tests.items():
        gens=Mof(t)
        print(name,"image_dim=",image_dim(gens),flush=True)
