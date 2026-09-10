"""Graded-root + greedy monotone-subroot extraction for Sigma(2,9,r).
Conventions: tau from Can-Karakurt Delta (Delta=+1 on semigroup S, -1 on N0-S).
DM greedy run on chi=-tau so stem extends downward (bounded above), matching Dai-Manolescu Sec 6.
"""
import math

def semigroup_S(p,q,r):
    pq,pr,qr=p*q,p*r,q*r
    N0=p*q*r-p*q-p*r-q*r
    reach=[False]*(N0+1); reach[0]=True
    for n in range(1,N0+1):
        for g in (pq,pr,qr):
            if n-g>=0 and reach[n-g]: reach[n]=True; break
    S=[n for n in range(N0+1) if reach[n]]
    return N0,S,set(S)

def delta_tau(p,q,r):
    N0,S,Sset=semigroup_S(p,q,r)
    Delta=[]
    for n in range(N0+1):
        inS=n in Sset; inQ=(N0-n) in Sset
        assert not (inS and inQ), f"overlap at {n}"
        Delta.append(1 if inS else (-1 if inQ else 0))
    tau=[0]*(N0+2)
    for n in range(N0+1): tau[n+1]=tau[n]+Delta[n]
    assert tau[N0+1]==0
    return N0,S,Delta,tau

def extrema(tau):
    # compress plateaus
    vals=[tau[0]]; pos=[0]
    for i in range(1,len(tau)):
        if tau[i]!=vals[-1]: vals.append(tau[i]); pos.append(i)
    # classify interior points of compressed sequence
    mins=[]; maxs=[]
    if len(vals)==1: return vals,pos,mins,maxs
    # endpoints: tau[0]=tau[-1]=0; treat as neither (stem ends)
    for k in range(1,len(vals)-1):
        if vals[k]<vals[k-1] and vals[k]<vals[k+1]: mins.append((k,vals[k],pos[k]))
        elif vals[k]>vals[k-1] and vals[k]>vals[k+1]: maxs.append((k,vals[k],pos[k]))
    return vals,pos,mins,maxs

def merge_tree_chi(tau):
    """Sublevel merge tree of chi=-tau. Returns clusters: dict base->list of leaf tip heights.
    Leaves born at local minima of chi (=local maxima of tau); merges at local maxima of chi (=local minima of tau)."""
    chi=[-t for t in tau]
    n=len(chi)
    # union-find over indices activated in increasing chi
    order=sorted(range(n), key=lambda i:(chi[i],i))
    parent=list(range(n)); active=[False]*n; comp_min={}  # root->min leaf height? track max tip (birth height)
    birth={}  # root -> max birth height among leaves in component (= max chi minimum? )
    def find(a):
        while parent[a]!=a: parent[a]=parent[parent[a]]; a=parent[a]
        return a
    # process grouped by level
    import itertools
    clusters={}  # base level -> list of tip heights of merging components
    for level,grp in itertools.groupby(order, key=lambda i:chi[i]):
        grp=list(grp)
        for i in grp: active[i]=True; parent[i]=i; birth[i]=level
        for i in grp:
            for nb in (i-1,i+1):
                if 0<=nb<n and active[nb]:
                    ri=find(i); rn=find(nb)
                    if ri!=rn:
                        # merge two components at level `level`; record tips
                        t1=birth[ri]; t2=birth[rn]
                        clusters.setdefault(level,[]).append((t1,t2))
                        # union, keep max birth (highest tip)
                        parent[rn]=ri; birth[ri]=max(t1,t2)
    return chi,clusters

def greedy_monotone(tau):
    chi,clusters=merge_tree_chi(tau)
    top=max(chi)
    # J0-invariant top vertex: level `top`. Determine if top cluster trivial:
    # top level vertices: indices with chi==top (tau minima, global). Symmetric pair => nontrivial.
    tops=[i for i,c in enumerate(chi) if c==top]
    # cluster at top? merges AT top level involve components born at top merging immediately (adjacent minima with no valley).
    # Simpler: if len(tops)>=2 and adjacent (plateau-merged) or symmetric pair -> nontrivial cluster with tips at top.
    # Use clusters dict at level top: merges recorded at top level.
    S=[]  # list of (tip, base)
    # Start: r = top. If cluster at top nontrivial -> add two tips; else add single vertex (bare tip).
    # Nontrivial at top means >=2 distinct global-minima components merging at top (adjacent global minima).
    # Check: number of indices attaining top that are connected at top level.
    # For our symmetric taus, global min attained at symmetric pair, separated -> they merge higher? No—higher than top impossible.
    # Actually components born at top merge only at HIGHER level, none exists. So each top component survives down; the "cluster at top"
    # in DM sense = set of branches meeting stem at top = the outermost pair. Treat as nontrivial if >=2 global minima OR >=1?
    # Follow DM: Cr = branches meeting stem at r. The stem top IS the merge point of the two outermost branches (they meet at top? no...).
    # Pragmatic implementation of DM greedy directly on (tip,base) pairs from merges:
    # Each merge at base b joins components with tips t1,t2; the pair that survives has tip max(t1,t2); the other branch is a side branch with tip min(t1,t2) meeting stem (or larger branch) at b.
    # Collect side branches: for each merge, side tip = min(t1,t2), base = b. Then greedy: sort side branches by base descending; select record highs of tip.
    # Also consider final surviving tip (global max birth = top) with base = +inf? It becomes stem tip hn=rn=... handle separately.
    # Rebuild merges in order to list side branches:
    # Re-run union-find recording side branches in merge order (increasing level).
    n=len(chi)
    order=sorted(range(n), key=lambda i:(chi[i],i))
    parent=list(range(n)); active=[False]*n; birth={}
    def find(a):
        while parent[a]!=a: parent[a]=parent[parent[a]]; a=parent[a]
        return a
    side=[]  # (tip, base)
    import itertools
    for level,grp in itertools.groupby(order, key=lambda i:chi[i]):
        grp=list(grp)
        for i in grp: active[i]=True; parent[i]=i; birth[i]=level
        for i in grp:
            for nb in (i-1,i+1):
                if 0<=nb<n and active[nb]:
                    ri=find(i); rn=find(nb)
                    if ri!=rn:
                        t1=birth[ri]; t2=birth[rn]
                        side.append((min(t1,t2),level))
                        parent[rn]=ri; birth[ri]=max(t1,t2)
    # greedy from top: sort by base descending, pick strictly increasing tip records above... DM: add tips iff tip > all in S.
    # S starts with outermost: the surviving global tip? DM starts at r=top: if Cr trivial add single v (stem tip at top). Else add pair.
    # Our side-branch list excludes the final survivor (tip=top, never a side). Initialize S with survivor tip=top (single), then scan bases desc, add side tips strictly greater than current max? They can't exceed top. So instead DM must initialize S EMPTY at top and scan DOWN picking record... Let's implement: sort side by base DESC; running max m=-inf; for (t,b) in order: if t>m: select; m=t. This yields monotone subroot leaves (outermost first? outermost has lowest base... hmm order desc picks innermost first).
    # Sort desc: first entries = merges at high base (near top) = small valleys near global minima? Their side tips are near-top values. Records will pick increasing tips as base decreases? Tips bounded by top, so picks tips approaching top as we go down — plausible: selects branches with ever-higher tips (up to top). Final survivor (top) is the stem tip.
    side_sorted=sorted(side,key=lambda x:(-x[1],-x[0]))
    sel=[]; m=float('-inf')
    for t,b in side_sorted:
        if t>m: sel.append((t,b)); m=t
        if m>=top: break
    return chi,clusters,side,sel,top

for r in [5,7,11,13,17,19,23,25,29,31,37]:
    if math.gcd(r,18)!=1: continue
    N0,S,Delta,tau=delta_tau(2,9,r)
    vals,pos,mins,maxs=extrema(tau)
    chi,clusters,side,sel,top=greedy_monotone(tau)
    print(f"=== r={r} N0={N0} kappa={len(S)} tauMin={min(tau)} tauMax={max(tau)} nMin={len(mins)} nMax={len(maxs)}")
    print(f"    S={S}")
    print(f"    extrema vals={vals}")
    print(f"    nSide={len(side)} sel(tip,base)[chi coords]={sel}")
    # HF_conn estimate: each selected pair (t,b) with t>b gives torsion length (t-b)/2 in chi grading (= (tauBase-tauTip)/2 in tau).
    tors=sorted([(t-b)//2 for t,b in sel if t>b])
    print(f"    torsion lengths={tors} nTors={len(tors)}")
