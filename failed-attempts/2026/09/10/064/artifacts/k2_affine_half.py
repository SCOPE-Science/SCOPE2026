"""Affine-half (chart-change) linear system of Hou k=2 pipeline at (m,t)=(3,3)
on EXACT fallback fiber R=1+x^16+y^16+z^16+x^14 y^2 over F_251. stdlib only.
Implements: Prop-4.1 (m=3) explicit numerators N1 (i=1), N2 (i=2), N3 (i=3);
quotient-ring normal form deg_y<16 via monic y^16-relation; z-truncation (4.31)
r<(d-1)*i; exact Gaussian elimination rank over F_251.
Infinity T-system (4.32) NOT included -> affine-half result only (honestly labelled)."""
p = 251
def add(A,B,s=1):
    C=dict(A)
    for k,v in B.items(): C[k]=(C.get(k,0)+s*v)%p
    return {k:v for k,v in C.items() if v}
def mul(A,B):
    C={}
    for ka,va in A.items():
        for kb,vb in B.items():
            k=(ka[0]+kb[0],ka[1]+kb[1],ka[2]+kb[2]); C[k]=(C.get(k,0)+va*vb)%p
    return {k:v for k,v in C.items() if v}
def pw(A,e):
    R_={(0,0,0):1}
    for _ in range(e): R_=mul(R_,A)
    return R_
X={(1,0,0):1};Y={(0,1,0):1};Z={(0,0,1):1}
def C0(c): return {(0,0,0):c%p} if c%p else {}
R=add(add(add(add(C0(1),pw(X,16)),pw(Y,16)),pw(Z,16)),mul(pw(X,14),pw(Y,2)))
def diff(F,v):
    G={}
    for (a,b,c),cf in F.items():
        if v==0 and a: G[(a-1,b,c)]=(G.get((a-1,b,c),0)+cf*a)%p
        if v==1 and b: G[(a,b-1,c)]=(G.get((a,b-1,c),0)+cf*b)%p
        if v==2 and c: G[(a,b,c-1)]=(G.get((a,b,c-1),0)+cf*c)%p
    return {k:v%p for k,v in G.items() if v%p}
Rx,Ry,Rz=diff(R,0),diff(R,1),diff(R,2)
Rzz=diff(Rz,2);Ryz=diff(Ry,2);Ryy=diff(Ry,1);Rxz=diff(Rx,2);Rxy=diff(Rx,1);Rxx=diff(Rx,0)
assert Rz=={(0,0,15):16}, Rz
# unknown coefficient functions: A0..A3, B0 with deg bounds D (m=3,t=3,d=16)
Ds={('A',0):39,('A',1):40,('A',2):41,('A',3):42,('B',0):10}
def mons(D):
    out=[]
    for a in range(D+1):
        for b in range(min(15,D-a)+1):
            for c in range(D-a-b+1): out.append((a,b,c))
    return out
bases={k:mons(D) for k,D in Ds.items()}
col={}; cols=[]
for k,ms in bases.items():
    for m_ in ms: col[(k,m_)]=len(cols); cols.append((k,m_))
n=len(cols); print("unknowns:",n)
# Formal term: dict exonent-> {occurrences}; represent linear form per monomial as dict col->val.
# Unknown poly U = sum_u e_u * mon_u. K*U product: for each mon_u, shift K exponents.
def KU(K,uk):
    out={}
    for mu in bases[uk]:
        cu=col[(uk,mu)]
        for mk,vk in K.items():
            m2=(mu[0]+mk[0],mu[1]+mk[1],mu[2]+mk[2])
            d=out.get(m2)
            if d is None: out[m2]={cu:vk}
            else: d[cu]=(d.get(cu,0)+vk)%p
    return out
def Fadd(*fs):
    out={}
    for f in fs:
        for m2,d in f.items():
            t=out.get(m2)
            if t is None: out[m2]=dict(d)
            else:
                for c,v in d.items(): t[c]=(t.get(c,0)+v)%p
    return {m2:{c:v for c,v in d.items() if v} for m2,d in out.items() if any(v for v in d.values())}
def Fscale(f,s):
    return {m2:{c:(v*s)%p for c,v in d.items()} for m2,d in f.items()}
def fold_known(F):
    F=dict(F)
    while True:
        big=[k for k in F if k[1]>=16]
        if not big: break
        (a,b,c)=big[0]; cf=F.pop((a,b,c)); e=b-16
        for (dx,dy,dz),s in [((0,0,0),p-1),((16,0,0),p-1),((0,0,16),p-1),((14,2,0),p-1)]:
            k2=(a+dx,e+dy,c+dz); F[k2]=(F.get(k2,0)+cf*s)%p
    return {k:v for k,v in F.items() if v}
def fold_y(form):
    # fold any y-exponent>=16 using y^16=-(1+x^16+z^16+x^14 y^2); iterate to fixpoint
    form={m2:dict(d) for m2,d in form.items()}
    while True:
        big=[m2 for m2 in form if m2[1]>=16]
        if not big: break
        m2=big[0]; d=form.pop(m2); a,b,c=m2; e=b-16
        for (dx,dy,dz),s in [((0,0,0),p-1),((16,0,0),p-1),((0,0,16),p-1),((14,2,0),p-1)]:
            m3=(a+dx,e+dy,c+dz)
            t=form.get(m3)
            if t is None: form[m3]={cc:(vv*s)%p for cc,vv in d.items()}
            else:
                for cc,vv in d.items(): t[cc]=(t.get(cc,0)+vv*s)%p
        form={m2_:dd for m2_,dd in form.items() if any(v for v in dd.values())}
    return form
# Correction brackets from Prop 4.1 display
C1 = Ry  # placeholder pieces below use explicit combos
B1 = mul(mul(Ry,Ry),Rzz)
N1 = Fadd(Fscale(KU(fold_known(Rx),('A',3)),p-3), KU(fold_known(Ry),('A',2)), KU(B1,('B',0)))
N1 = fold_y(N1)
T1 = add(mul(mul(mul(Ry,Ry),Rz),Rxz),mul(mul(mul(Rx,Ry),Rz),Ryz),p-2)
T2 = add(mul(mul(Ry,mul(Rz,Rz)),Rxy),mul(mul(Rx,mul(Rz,Rz)),Ryy),p-1)
B2inner = fold_known(add(T1,T2))
N2 = Fadd(Fscale(KU(fold_known(mul(Rx,Rx)),('A',3)),p-3),
          Fscale(KU(fold_known(mul(Rx,Ry)),('A',2)),2),
          Fscale(KU(fold_known(mul(Ry,Ry)),('A',1)),p-1),
          Fscale(KU(B2inner,('B',0)),2))
N2 = fold_y(N2)
U1 = mul(mul(mul(Ry,Ry),mul(Rz,Rz)),Rxx)
U2 = mul(mul(mul(Rx,Ry),mul(Rz,Rz)),Rxy)
U3 = mul(mul(mul(Rx,Rx),mul(Rz,Rz)),Ryy)
B3inner = fold_known(add(add(U1,U2,p-2),U3))
N3 = Fadd(Fscale(KU(fold_known(mul(Rx,mul(Rx,Rx))),('A',3)),p-1),
          KU(fold_known(mul(mul(Rx,Rx),Ry)),('A',2)),
          Fscale(KU(fold_known(mul(mul(Rx,Ry),Ry)),('A',1)),p-1),
          KU(fold_known(mul(mul(Ry,mul(Ry,Ry)),C0(1))),('A',0)),
          KU(B3inner,('B',0)))
N3 = fold_y(N3)
# Truncation (4.31): keep z-exponent r<(d-1)*i ; rows = kept monomials
systems=[(N1,1),(N2,2),(N3,3)]
rows=[]
for N,i in systems:
    lim=15*i
    for m2,d in N.items():
        if m2[2]<lim and m2[1]<16: rows.append(d)
print("affine-half rows:",len(rows))
# exact rank over F_251
def rank(rows,n):
    M=[dict(r) for r in rows]; r_=0; piv=[-1]*n
    # order columns; iterate rows
    import sys
    row=0
    # build dense-ish elimination using dicts, pivot per column scan
    cols_order=list(range(n))
    prow=[None]*len(M)
    cur=0
    pivcol={}
    for rr in range(len(M)):
        # find pivot
        d=M[rr]
        # reduce by existing pivots
        for pc in sorted(pivcol):
            if pc in d and d[pc]:
                pivrow=pivcol[pc]; pr=pivrow
                f=d[pc]*pow(pr[pc],p-2,p)%p
                for cc,vv in pr.items():
                    if cc==pc: continue
                    d[cc]=(d.get(cc,0)-f*vv)%p
                d={cc:vv for cc,vv in d.items() if vv and cc!=pc}
                if pc in d: del d[pc]
        if not d: M[rr]={}; continue
        pc=min(d)
        inv=pow(d[pc],p-2,p)
        for cc in list(d): d[cc]=d[cc]*inv%p
        pivcol[pc]=d; M[rr]=d; cur+=1
    return cur, len(pivcol)
rk,_=rank(rows,n)
print("affine-half rank:",rk,"/ unknowns:",n,"/ rows:",len(rows))
print("affine-half nullity:", n-rk, "(>0 expected: infinity T-system not yet imposed)")
