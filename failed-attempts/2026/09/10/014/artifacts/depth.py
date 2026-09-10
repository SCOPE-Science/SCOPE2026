#!/usr/bin/env python3
"""Lane-526 depth screen: exact null vector + fresh-jet validation + m-scan."""
import itertools, json
from fractions import Fraction
P = 11
import random
rng = random.Random(1526)

def tuples_sum(n, k):
    if k == 1:
        yield (n,); return
    for i in range(n+1):
        for t in tuples_sum(n-i, k-1):
            yield (i,)+t
PERMS = list(itertools.permutations(range(4)))
def canon(rep):
    a,b,c = rep; best=None
    for s in PERMS:
        key=(tuple(a[i] for i in s),tuple(b[i] for i in s),tuple(c[i] for i in s))
        if best is None or key<best: best=key
    return best
def orbit_images(rep):
    a,b,c=rep; out=set()
    for s in PERMS:
        out.add((tuple(a[i] for i in s),tuple(b[i] for i in s),tuple(c[i] for i in s)))
    return sorted(out)
def diag_invariant(a,b,c):
    e=[(a[i]+b[i]+c[i])%5 for i in range(4)]
    return len(set(e))==1
def enum_orbits(m,r):
    seen={}
    jet_monos=[]
    for nc in range(m//2+1):
        nb=m-2*nc
        for b in tuples_sum(nb,4):
            for c in tuples_sum(nc,4):
                jet_monos.append((b,c))
    for a in tuples_sum(r,4):
        for (b,c) in jet_monos:
            if not diag_invariant(a,b,c): continue
            key=canon((a,b,c)); seen.setdefault(key,0); seen[key]+=1
    reps=sorted(seen); return reps,[orbit_images(rp) for rp in reps]
def mon_val(img,jet):
    a,b,c=img; x,xp,xpp=jet; v=1
    for i in range(4):
        if a[i]: v=v*pow(x[i],a[i],P)%P
        if b[i]: v=v*pow(xp[i],b[i],P)%P
        if c[i]: v=v*pow(xpp[i],c[i],P)%P
    return v
def orb_val(images,jet):
    return sum(mon_val(im,jet) for im in images)%P
def add_mod(vec,tgt,piv):
    inv=pow(pow(vec[piv],4,P),P-2,P)
    s=sum(pow(vec[k],4,P)*tgt[k] for k in range(4) if k!=piv)%P
    tgt[piv]=((-s)*inv)%P; return tgt
def rand_X_jet():
    while True:
        x=[rng.randrange(P) for _ in range(4)]
        if any(x) and sum(pow(v,5,P) for v in x)%P==0: break
    piv=rng.choice([i for i in range(4) if x[i]%P!=0])
    xp=[rng.randrange(P) for _ in range(4)]; add_mod(x,xp,piv)
    rhs=sum((4*pow(x[k],3,P)*pow(xp[k],2,P))%P for k in range(4))%P
    xpp=[rng.randrange(P) for _ in range(4)]; add_mod(x,xpp,piv)
    corr=(rhs*pow(pow(x[piv],4,P),P-2,P))%P
    xpp[piv]=(xpp[piv]-corr)%P
    return (x,xp,xpp)
def nullspace_modp(rows,ncols):
    M=[list(r) for r in rows]; nrows=len(M)
    where=[-1]*ncols; r=0
    for c in range(ncols):
        piv=None
        for i in range(r,nrows):
            if M[i][c]%P!=0: piv=i; break
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]; where[c]=r
        inv=pow(M[r][c]%P,P-2,P)
        M[r]=[(v*inv)%P for v in M[r]]
        for i in range(nrows):
            if i!=r and M[i][c]%P!=0:
                f=M[i][c]%P
                M[i]=[(M[i][j]-f*M[r][j])%P for j in range(ncols)]
        r+=1
    free=[c for c in range(ncols) if where[c]==-1]
    vecs=[]
    for f in free:
        v=[0]*ncols; v[f]=1
        for c in range(ncols):
            if where[c]!=-1:
                v[c]=(-M[where[c]][f])%P
        vecs.append(v)
    return vecs, r
def rank_modp(rows,ncols):
    M=[list(r) for r in rows]; nr=len(M); rk=0
    for c in range(ncols):
        piv=None
        for i in range(rk,nr):
            if M[i][c]%P!=0: piv=i; break
        if piv is None: continue
        M[rk],M[piv]=M[piv],M[rk]
        inv=pow(M[rk][c]%P,P-2,P)
        M[rk]=[(v*inv)%P for v in M[rk]]
        for i in range(nr):
            if i!=rk and M[i][c]%P!=0:
                f=M[i][c]%P
                M[i]=[(M[i][j]-f*M[rk][j])%P for j in range(ncols)]
        rk+=1
    return rk

M_STAR,R_STAR=12,2
reps,images=enum_orbits(M_STAR,R_STAR)
ncols=len(reps)
jets=[rand_X_jet() for _ in range(500)]
Erows=[]
for _ in range(400):
    jx,jxp,jxpp=jets[rng.randrange(len(jets))]
    lam=rng.randrange(1,P); mu=rng.randrange(P)
    jr=(jx,[(lam*v)%P for v in jxp],[((lam*lam*w+mu*v)%P) for v,w in zip(jxp,jxpp)])
    base=[orb_val(im,(jx,jxp,jxpp)) for im in images]
    new=[orb_val(im,jr) for im in images]
    scl=pow(lam,M_STAR,P)
    Erows.append([(new[k]-scl*base[k])%P for k in range(ncols)])
vecs,rk=nullspace_modp(Erows,ncols)
print(f"NCOLS={ncols} ERANK={rk} NULLDIM={len(vecs)}")
# fresh-jet validation of first null vector
v0=vecs[0]
ntest=300; maxres=0; nfail=0
for _ in range(ntest):
    jx,jxp,jxpp=rand_X_jet()
    lam=rng.randrange(1,P); mu=rng.randrange(P)
    jr=(jx,[(lam*v)%P for v in jxp],[((lam*lam*w+mu*v)%P) for v,w in zip(jxp,jxpp)])
    b=sum((v0[k]*orb_val(images[k],(jx,jxp,jxpp)))%P for k in range(ncols))%P
    n=sum((v0[k]*orb_val(images[k],jr))%P for k in range(ncols))%P
    res=(n-pow(lam,M_STAR,P)*b)%P
    maxres=max(maxres,min(res,P-res))
    if res!=0: nfail+=1
print(f"V0 fresh-jet: fails {nfail}/{ntest}, max balanced residue {maxres}")
print("V0 nonzero entries:",sum(1 for v in v0 if v!=0))
print("V0:",v0)
# check V0 not identically zero on X jets
nz=sum(1 for jt in jets[:100] if sum((v0[k]*orb_val(images[k],jt))%P for k in range(ncols))%P!=0)
print(f"V0 nonvanishing on {nz}/100 sampled X-jets")
# m-scan of orbit dims for r=2
scan={}
for m in range(1,16):
    rr,ii=enum_orbits(m,2)
    scan[m]=len(rr)
print("ORBIT_SCAN_r2:",scan)
# r-scan at m=12
rscan={}
for r in range(0,5):
    rr,ii=enum_orbits(M_STAR,r)
    rscan[r]=len(rr)
print("ORBIT_SCAN_m12:",rscan)
with open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-526/output/artifacts/depth_log.json","w") as f:
    json.dump({"ncols":ncols,"erank":rk,"nulldim":len(vecs),
               "v0":v0,"v0_fails":nfail,"v0_nz":nz,
               "orbit_scan_r2":scan,"orbit_scan_m12":rscan},f,indent=1)
print("DEPTH_OK")
