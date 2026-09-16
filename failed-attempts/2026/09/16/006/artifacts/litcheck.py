# Verify the two structural rigidity facts used in the k=2 proof, computationally:
# (a) balanced LBT edge bound (Klee-Novik): f1 >= ... ; we verify Gamma achieves it and cross-polytope is unique minimizer at k=2 (done by enumeration: only closed complex is full K_{2,2,2,2}).
# (b) For k>=3, is stacked-chain graph the UNIQUE (up to iso) minimizer of f1? If yes, equality case understood; if no, multiple Gammas with same f1 but possibly different higher strands -> the target's "any Gamma" + fixed formula would need all stacked spheres to share the strand (verified d=4,k=3 chain (30 facets) vs strand.py single-glue (30 facets): both gave SAME strand [0,24,80,...]. Good: formula independent of stacking arrangement, at least for these two.
# Test a third stacking arrangement for d=4,k=4 (chain of 3): strand.py built 2-glued (30? no: chain t=3: n=16, facets=3*16-4=44?). k4sweep stacked k=4 strand matched formula. The arrangement there = linear chain. Star arrangements impossible in cross-polytopal stacking? (tree-like gluings along distinct facets = all stacked; linear chain is one tree; branched tree needs 3+ glue facets on one summand: possible! e.g., summand with 3 glue facets removed (16-3=13 facets) + ... total n = 8*4-4*3=20? k=5 class. Different tree -> same f-vector? f1 same by LBT count. Strand same? Test branched (star) vs chain for k=5,d=4 (n=20): 2^20=1M masks, feasible (~1-2 min?). Try chain t=4 vs star.
import itertools, sys
sys.path.insert(0,'output/artifacts')
from flipsearch import check_valid, strand_of_facets
def chain(d,t,branch=False):
    ids={}; nx=[0]
    def g(k):
        if k not in ids: ids[k]=nx[0]; nx[0]+=1
        return ids[k]
    facets=[]
    if not branch:
        right=None
        for s in range(t):
            L=right if s>0 else {c:g(('L',0,c)) for c in range(d)}
            R={c:g(('M',s,c,1)) for c in range(d)}
            skip=set()
            if s>0: skip.add(frozenset(L[c] for c in range(d)))
            if s<t-1: skip.add(frozenset(R[c] for c in range(d)))
            for ch in itertools.product([0,1],repeat=d):
                F=frozenset((L[c] if ch[c]==0 else R[c]) for c in range(d))
                if F in skip: continue
                facets.append(F)
            right=R
    else:
        # star: center summand 0 with left fixed + 3 arms; arms attach at 3 distinct facets of center? Center cross-polytope: use facets F_a,F_b,F_c pairwise... arms each share one facet. Total n = 8 + 4*3 = 20 (each arm adds 4 new verts). t-arm star with t=3: n=20, k=5.
        C0={c:g(('C0',c)) for c in range(d)}
        C1={c:g(('C1',c)) for c in range(d)}
        gluefacets=[frozenset(C0[c] if c!=j else C1[c] for c in range(d)) for j in range(3)]
        arms=[]
        for j in range(3):
            A={c:g(('A',j,c)) for c in range(d)}
            arms.append(A)
        skip=set(gluefacets)
        for ch in itertools.product([0,1],repeat=d):
            F=frozenset((C0[c] if ch[c]==0 else C1[c]) for c in range(d))
            if F in skip: continue
            facets.append(F)
        for j,A in enumerate(arms):
            G=gluefacets[j]
            # color of C0[c]/C1[c] is c
            Gc={}
            for c in range(d):
                # which of C0[c],C1[c] is in G: j-th glue facet differs in coordinate j
                Gc[c]= C1[c] if c==j else C0[c]
                Gc[c]=g(('C0',c)) if c!=j else g(('C1',c))
            for ch in itertools.product([0,1],repeat=d):
                F=frozenset((Gc[c] if ch[c]==0 else A[c]) for c in range(d))
                if F==G: continue
                facets.append(F)
    N=nx[0]
    colors=[None]*N
    for k,i in ids.items():
        if k[0]=='M': colors[i]=k[2]
        elif k[0]=='A': colors[i]=k[2]
        else: colors[i]=k[-1]
    return facets,colors,N
for branch in (False,True):
    f,c,N=chain(4,4,branch)
    tag='star' if branch else 'chain'
    print(tag,'n=',N,'nfacets=',len(f),'valid=',check_valid(f,4,c))
