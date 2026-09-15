from fractions import Fraction
import itertools
from collections import defaultdict

def mons(nvars,deg):
    return sorted([e for e in itertools.product(range(deg+1),repeat=nvars) if sum(e)==deg])

def diff_poly(F,a):
    G=dict(F)
    for vi,ee in enumerate(a):
        for _ in range(ee):
            NG=defaultdict(Fraction)
            for e,c in G.items():
                if e[vi]>0:
                    ne=list(e); ne[vi]-=1; ne=tuple(ne)
                    NG[ne]+=c*e[vi]
            G=dict(NG)
    return G

def rank_frac(M):
    if not M or not M[0]: return 0
    R=[row[:] for row in M]; m=len(R); n=len(R[0]); r=0
    for c in range(n):
        piv=None
        for i in range(r,m):
            if R[i][c]!=0: piv=i; break
        if piv is None: continue
        R[r],R[piv]=R[piv],R[r]
        inv=R[r][c]
        for i in range(m):
            if i!=r and R[i][c]!=0:
                f=R[i][c]/inv
                for j in range(c,n): R[i][j]-=f*R[r][j]
        r+=1
    return r

def nullspace_frac(M):
    # M rows x cols; return basis of ker (as row action? we need ker of map R_i->S_{d-i}: vector v with sum v_a * diff^a F =0)
    # M is len(src) x len(tgt); kernel = {v : v M = 0} = left kernel. Compute via elimination on transpose.
    if not M or not M[0]: return []
    m=len(M); n=len(M[0])
    # solve v M=0: transpose to M^T x=0
    MT=[[M[i][j] for i in range(m)] for j in range(n)]  # n x m
    # row-reduce MT to find nullspace dim m - rank
    A=[row[:] for row in MT]
    pivcol=[]
    r=0
    where=[-1]*m
    for c in range(m):
        piv=None
        for i in range(r,n):
            if A[i][c]!=0: piv=i; break
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        where[c]=r
        inv=A[r][c]
        for j in range(c,m): A[r][j]/=inv
        for i in range(n):
            if i!=r and A[i][c]!=0:
                f=A[i][c]
                for j in range(c,m): A[i][j]-=f*A[r][j]
        r+=1
    # free vars
    basis=[]
    for f in range(m):
        if where[f]==-1:
            v=[Fraction(0)]*m; v[f]=Fraction(1)
            for c in range(m):
                if where[c]!=-1:
                    v[c]=-A[where[c]][f]
            basis.append(v)
    return basis

def cat_matrix(F,d,i):
    src=mons(4,i); tgt=mons(4,d-i)
    tindex={b:j for j,b in enumerate(tgt)}
    M=[]
    for a in src:
        G=diff_poly(F,a)
        row=[Fraction(0)]*len(tgt)
        for e,c in G.items():
            if sum(e)==d-i and e in tindex: row[tindex[e]]=c
        M.append(row)
    return src,tgt,M

def ann_basis(F,d,i):
    src,tgt,M=cat_matrix(F,d,i)
    ns=nullspace_frac(M)
    # each ns vector gives element of Ann_i: sum v_a x^a
    return src,ns

def hvec(F,d):
    h=[]
    for i in range(d+1):
        s,t,M=cat_matrix(F,d,i)
        h.append(rank_frac(M))
    return h

def mul_rank(F,d,i,L):
    # multiplication by L (coeffs length4) map A_i -> A_{i+1}. Compute via duality?
    # Represent A_i = R_i / Ann_i. Choose complement basis: row-space basis of M (cat).
    # Easier: compute matrix of composed map R_i -> A_{i+1} via multiply by L then project.
    # Steps: basis of R_i: src_i; multiply by L: image in R_{i+1}: coeffs. Then project R_{i+1} -> S_{d-i-1} via cat (that's the quotient map R_{i+1}->A_{i+1} dual to ...?). Actually A_{i+1} dual is image of cat transpose? The linear map R_{i+1} -> S_{d-i-1} has kernel Ann_{i+1}, image dim = h_{i+1}. So rank of A_i -> A_{i+1} equals rank of composition R_i --xL--> R_{i+1} --cat--> S_{d-i-1} restricted? But domain must mod Ann_i: the composition factors through A_i iff Ann_i maps to Ann_{i+1} (true since ideal). Rank of induced map = rank of composed matrix minus? Actually composed matrix M_comp (dim R_i x dim S_{d-i-1}): its kernel contains Ann_i, and its image = image of mult map. Its rank equals rank of induced map A_i -> A_{i+1} because Ann_i subset ker. So compute M_comp and take rank.
    if i+1>d: return 0
    src_i=mons(4,i); src_ip1=mons(4,i+1); tgt=mons(4,d-i-1)
    tindex={b:j for j,b in enumerate(tgt)}
    # precompute diff of F by b in src_ip1: D_b = diff^b F as dict
    D={}
    for b in src_ip1:
        D[b]=diff_poly(F,b)
    # index of src_ip1
    idx={b:k for k,b in enumerate(src_ip1)}
    Mcomp=[]
    for a in src_i:
        # x^a * L = sum_j L_j x^{a+e_j}
        # row = sum_j L_j * (row of cat for exponent a+e_j)
        row=[Fraction(0)]*len(tgt)
        for j in range(4):
            na=list(a); na[j]+=1; na=tuple(na)
            G=D[na]
            for e,c in G.items():
                if sum(e)==d-i-1 and e in tindex:
                    row[tindex[e]]+=Fraction(L[j])*c
        Mcomp.append(row)
    return rank_frac(Mcomp)

def pw(form,p):
    cur={(0,0,0,0):Fraction(1)}
    for _ in range(p):
        nxt=defaultdict(Fraction)
        for e1,c1 in cur.items():
            for e2,c2 in form.items():
                ne=tuple(e1[k]+e2[k] for k in range(4))
                nxt[ne]+=c1*c2
        cur=dict(nxt)
    return dict(cur)
def lin(a,b,c,dd):
    return {(1,0,0,0):Fraction(a),(0,1,0,0):Fraction(b),(0,0,1,0):Fraction(c),(0,0,0,1):Fraction(dd)}
def add(*Fs):
    r=defaultdict(Fraction)
    for F in Fs:
        for e,c in F.items(): r[e]+=c
    return dict(r)

# Candidate Perazzo-like degree 4 in 4 vars: F = X1^3*X2 + X3^3*X4? check codim (need all vars appear in first partials)
F=add({(3,1,0,0):Fraction(1)},{(0,0,3,1):Fraction(1)},{(2,0,2,0):Fraction(1)},{(0,2,0,2):Fraction(1)})
print("h",hvec(F,4))
for L in ([1,1,1,1],[1,2,3,5],[1,0,1,2]):
    print("L",L,[mul_rank(F,4,i,L) for i in range(4)], "h",hvec(F,4))
