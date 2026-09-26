#!/usr/bin/env python3
"""Independent replay verifier: reads ONLY committed CSVs, reproduces splitting,
checks s+a=g, Sym/Alt dimension sums, nonnegativity, gap maximality.
Also re-derives character values by from-scratch Murnaghan-Nakayama and diffs
against committed chartable (byte-identical row check). Stdlib only.
"""
import csv, json, math, itertools, sys
from functools import lru_cache

def rim_hooks(shape, r):
    cells=[(i,j) for i,r_ in enumerate(shape) for j in range(r_)]
    cellset=set(cells)
    out=[]
    for combo in itertools.combinations(cells, r):
        s=set(combo)
        bad=False
        for (i,j) in combo:
            if (i+1,j) in s and (i,j+1) in s and (i+1,j+1) in s:
                bad=True; break
        if bad: continue
        stack=[combo[0]]; vis={combo[0]}
        while stack:
            a=stack.pop()
            for b in combo:
                if b not in vis and abs(a[0]-b[0])+abs(a[1]-b[1])==1:
                    vis.add(b); stack.append(b)
        if len(vis)!=r: continue
        rem=cellset-s
        newshape=[]; ok=True
        for i in range(len(shape)):
            rc=sorted(j for (ii,j) in rem if ii==i)
            if rc and rc!=list(range(len(rc))): ok=False; break
            newshape.append(len(rc))
        if not ok: continue
        while newshape and newshape[-1]==0: newshape.pop()
        for i in range(len(newshape)-1):
            if newshape[i]<newshape[i+1]: ok=False; break
        if not ok: continue
        h=len(set(i for (i,j) in combo))-1
        out.append((newshape,h))
    return out

@lru_cache(maxsize=None)
def _mn(shape, ctype):
    shape=list(shape); ctype=list(ctype)
    if sum(shape)==0: return 1 if sum(ctype)==0 else 0
    if not ctype: return 1 if sum(shape)==0 else 0
    r=ctype[0]; rest=tuple(ctype[1:])
    return sum(((-1)**h)*_mn(tuple(ns),rest) for (ns,h) in rim_hooks(shape,r))

def parse_part(s):
    s=s.strip()
    if s in ("[]",""): return ()
    return tuple(map(int,s.split("+")))

ok=True
for n in (7,8):
    fn=math.factorial(n)
    cl=list(csv.DictReader(open(f"output/artifacts/classes_S{n}.csv")))
    nc=len(cl)
    ctypes=[parse_part(r["cycle_type"]) for r in cl]
    sizes=[int(r["class_size"]) for r in cl]
    sq_idx=[int(r["square_class_index"]) for r in cl]
    # check squaring map independently
    for i,ct in enumerate(ctypes):
        out=[]
        for L in ct:
            out.extend([L] if L%2 else [L//2,L//2])
        out=tuple(sorted(out,reverse=True))
        assert tuple(ctypes[sq_idx[i]])==out, (n,i,ct,out)
    # chartable
    ct_rows=list(csv.DictReader(open(f"output/artifacts/chartable_S{n}.csv")))
    shapes=[parse_part(r["shape"]) for r in ct_rows]
    tab={s:[int(r[f"class_{i}"]) for i in range(nc)] for s,r in zip(shapes,ct_rows)}
    # re-derive MN and compare
    for s in shapes:
        for i,ct in enumerate(ctypes):
            v=_mn(tuple(s),tuple(ct))
            if v!=tab[s][i]:
                print(f"MISMATCH S{n} shape {s} class {ct}: csv {tab[s][i]} vs MN {v}")
                ok=False
    # row orthogonality
    for a in shapes:
        for b in shapes:
            raw=sum(sizes[k]*tab[a][k]*tab[b][k] for k in range(nc))
            assert raw%fn==0
            ip=raw//fn
            assert ip==(1 if a==b else 0), (n,a,b,ip)
    # splitting rows
    sp=list(csv.DictReader(open(f"output/artifacts/splitting_tworow_S{n}.csv")))
    # dims: value at identity class
    idx=[i for i,c in enumerate(ctypes) if list(c)==[1]*n][0]
    dims={s:tab[s][idx] for s in shapes}
    seen={}
    for r in sp:
        lam=parse_part(r["lambda"]); nu=parse_part(r["nu"])
        s,a,g=int(r["s"]),int(r["a"]),int(r["g"])
        assert s>=0 and a>=0 and g>=0
        assert s+a==g, (n,lam,nu)
        assert abs(s-a)==int(r["gap_abs"])
        # recompute from class sums
        chi=tab[lam]; chin=tab[nu]
        chiS=[(chi[i]**2+chi[sq_idx[i]])//2 for i in range(nc)]
        chiA=[(chi[i]**2-chi[sq_idx[i]])//2 for i in range(nc)]
        for i in range(nc): assert (chi[i]**2+chi[sq_idx[i]])%2==0
        es=sum(sizes[i]*chiS[i]*chin[i] for i in range(nc))//fn
        ea=sum(sizes[i]*chiA[i]*chin[i] for i in range(nc))//fn
        assert es==s and ea==a, (n,lam,nu,es,ea,s,a)
        seen[(lam,nu)]=(s,a,g)
    tworow=[s for s in shapes if len(s)<=2]
    assert len(tworow)==(4 if n==7 else 5)
    for lam in tworow:
        for nu in shapes:
            assert (lam,nu) in seen, (n,lam,nu)
        d=dims[lam]
        ss=sum(seen[(lam,nu)][0]*dims[nu] for nu in shapes)
        aa=sum(seen[(lam,nu)][1]*dims[nu] for nu in shapes)
        assert ss==d*(d+1)//2 and aa==d*(d-1)//2, (n,lam,ss,aa)
    # gap max
    mx=max(abs(v[0]-v[1]) for v in seen.values())
    cands=sorted([(lam,nu) for (lam,nu),v in seen.items() if abs(v[0]-v[1])==mx])
    print(f"S{n}: classes={nc} shapes={len(shapes)} entries={len(seen)} maxgap={mx} lexfirst=({'+'.join(map(str,cands[0][0]))},{'+'.join(map(str,cands[0][1]))}) s,a,g={seen[cands[0]]}")
    # trivial/sign spot
    triv=(n,); sign=tuple([1]*n)
    for lam in tworow:
        assert seen[(lam,triv)]==(1,0,1),(n,lam,seen[(lam,triv)])
        assert seen[(lam,sign)]==(0,0,0),(n,lam,seen[(lam,sign)])
print("VERIFY_OK" if ok else "VERIFY_FAIL")
sys.exit(0 if ok else 1)
