"""Independent verifier: different MN implementation (diagram strip-walk, no beta-sets)
plus certificate replay from stored table. Run: python3 verify_independent.py"""
import math, json
from functools import lru_cache
N=15; FACT=math.factorial(15)
D=json.load(open("chartable15.json"))
LAM=[tuple(p) for p in D["lambdas"]]; MUS=[tuple(p) for p in D["mus"]]
CS=D["class_sizes"]; X=D["table"]
R=json.load(open("staircase_row.json"))

def strips(lam,k):
    # enumerate border strips of size k by walking rim from top-right end
    # rim path: cells of lam with no cell strictly SE; order them from top row to bottom.
    if sum(lam)<k or k<=0: return
    cells=set((i,j) for i,r in enumerate(lam) for j in range(r))
    # build rim as ordered list along border: start at (0, lam[0]-1), walk: prefer down else left
    rim=[]
    c=(0,lam[0]-1)
    seen=set()
    while c is not None and c in cells and c not in seen:
        seen.add(c); rim.append(c)
        d=(c[0]+1,c[1]); l=(c[0],c[1]-1)
        if d in cells and d not in seen: c=d
        elif l in cells and l not in seen: c=l
        else:
            # may need to jump: find adjacent rim cell not visited
            nxt=None
            for q in (d,l):
                if q in cells and q not in seen: nxt=q; break
            c=nxt
    # candidate strips = consecutive segments of rim of size k whose removal leaves a diagram
    def is_diag(s):
        rows={}
        for (i,j) in s: rows.setdefault(i,[]).append(j)
        # each row must be 0..m-1 prefix
        for i,js in rows.items():
            if sorted(js)!=list(range(max(js)+1)) and not (set(js)==set(range(len(js)))):
                # rows of s need not be prefix; check lam\s rows are prefix
                pass
        return True
    for a in range(len(rim)-k+1):
        seg=rim[a:a+k]
        # connectivity along rim guaranteed by consecutiveness; check removal leaves diagram
        S=set(seg); rem=cells-S
        # check rem is a Young diagram (prefix rows, nonincreasing lengths)
        if not rem:
            # height = (#rows spanned)-1
            rows2=sorted(set(i for (i,j) in seg)); h=len(rows2)-1
            yield ((),h); continue
        maxr=max(i for (i,j) in rem)
        ok=True; lens=[]
        for i in range(maxr+1):
            js=sorted(j for (ii,j) in rem if ii==i)
            if js!=list(range(len(js))): ok=False; break
            lens.append(len(js))
        if not ok: continue
        if any(lens[i]<lens[i+1] for i in range(len(lens)-1)): continue
        # also rows beyond maxr must be empty in lam (they are, since rem subset)
        # and no holes: rows 0..maxr all present? if row i empty but later nonempty -> fail
        # lens covers 0..maxr consecutively, empty row would be lens 0 then positive -> caught by nonincreasing? 0<positive fails only if later bigger; leading zeros impossible since row0 contains (0,0) unless removed... if (0,0) in seg then rem misses row0 start -> js for row0 might be [] -> lens has 0 first -> nonincreasing ok but invalid (must be dropped). Handle: strip leading-zero rows? Actually if (0,0) removed, rem is not a diagram unless rem empty. Our check: row0 js=[] -> lens[0]=0, rest must be 0 too. Enforce.
        if lens[0]==0 and any(l>0 for l in lens[1:]): continue
        while lens and lens[-1]==0: lens.pop()
        rows2=sorted(set(i for (i,j) in seg)); h=len(rows2)-1
        yield (tuple(lens),h)

@lru_cache(maxsize=None)
def chi2(lam,mu):
    if not mu: return 1 if sum(lam)==0 else 0
    if sum(lam)!=sum(mu) or not lam: return 0
    k=mu[0]; rest=mu[1:]; tot=0
    for nl,h in strips(lam,k): tot+=((-1)**h)*chi2(nl,rest)
    return tot

# 1) byte-identity of full table
mism=0
for i,lam in enumerate(LAM):
    for j,mu in enumerate(MUS):
        if chi2(lam,mu)!=X[i][j]:
            mism+=1
            if mism<5: print("MISMATCH",lam,mu,chi2(lam,mu),X[i][j])
print("table mismatches:",mism,"/",len(LAM)*len(MUS))
# 2) orthogonality + hook dims replay from stored table
def hookdim(lam):
    hl=[]
    for i,r in enumerate(lam):
        for j in range(r):
            hl.append(r-j-1+sum(1 for rr in lam[i+1:] if rr>j)+1)
    return FACT//math.prod(hl)
ident=LAM.index((1,)*N)
assert all(X[i][ident]==hookdim(LAM[i]) for i in range(len(LAM)))
assert sum(X[i][ident]**2 for i in range(len(LAM)))==FACT
assert all(sum(X[i][j]**2*CS[j] for j in range(len(MUS)))==FACT for i in range(len(LAM)))
print("orthogonality+hookdim replay: OK")
# 3) certificate replay: class sums
pindex={p:i for i,p in enumerate(LAM)}
ri=pindex[(5,4,3,2,1)]
bad=0; ming=None
for e in R["rows"]:
    nu=tuple(e["nu"]); ni=pindex[nu]
    s=sum(CS[j]*X[ri][j]**2*X[ni][j] for j in range(len(MUS)))
    if s!=e["g"]*FACT or s!=e["class_sum"]: bad+=1; print("CERT FAIL",nu)
    if ming is None or e["g"]<ming[1]: ming=(nu,e["g"])
print("cert replay fails:",bad,"/176; min:",ming)
print("VERIFY_OK" if mism==0 and bad==0 else "VERIFY_FAIL")
