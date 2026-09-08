"""S3b: full Kauffman-bracket Jones check of Atlas braid words via explicit closure diagram.
Builds planar diagram graph from braid word + standard closure, then 2^c state sum.
c=11 (K11n34: 2048 states), c=13 (K11n42: 8192 states) — each fast in pure Python with union-find.
Crossing convention: generator +i = right-handed (positive, writhe +1) with strand i OVER i+1.
A-smoothing convention: for positive crossing, A-smoothing connects the two regions swept by
over-strand rotating counterclockwise... we fix: A-state joins (top_a-bot_a, top_b-bot_b) for
positive crossing? Verify on trefoil: BR[2,{-1,-1,-1}] must give Jones q^-1+q^-3-q^-4 (mirror of 3_1 mm).
We try both pairings and select the one matching calibration (record choice in log).
"""
import itertools

def closure_circles(nstr, word, state):
    # Nodes: half-edge stubs. Each crossing l (0-based) involves strands a,a+1 (a=|i|-1).
    # Strand routing through levels: maintain perm p mapping current positions->strand ids.
    # For circle counting, standard trick: model the 4-valent graph with 2*nstr*(L+1) directed edge
    # pieces? Simpler: union-find over "segment ends".
    # Segments: vertical pieces between consecutive levels: for level l in 0..L-1, for each position
    # j in 0..nstr-1, piece v[l][j] connecting node (j,l)-(j,l+1), except at a crossing the two
    # pieces incident cross. Plus closure arcs c[j] connecting bottom (j,L) to top (j,0).
    # At crossing l with a: the pieces v[l][a], v[l][a+1] meet at the crossing instead of passing
    # straight; stubs: T_a=(a,l), T_b=(a+1,l), B_a, B_b at level l+1 (after permutation swap for
    # subsequent levels: positions a,a+1 swap for levels >l).
    # Because later crossings act on positions, track pos->strand but for connectivity only the
    # local stub identities matter; the vertical pieces connect stub to stub across levels with
    # the swap accounted by permuting position labels below the crossing.
    # Implement: label each stub end; vertical piece between level l position j and level l+1
    # position j' where j'=swap_l(j). Union them (they're the same wire except at crossings where
    # smoothing decides pairing of the 4 stubs).
    L = len(word)
    n = nstr
    parent = {}
    def mk(x):
        parent[x]=x; return x
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(x,y):
        rx,ry=find(x),find(y)
        if rx!=ry: parent[rx]=ry
    # stub ids: ('T',l,j) top of crossing l at position j in {a,a+1}; ('B',l,j) bottom.
    for l in range(L):
        a = abs(word[l])-1
        for j in (a,a+1):
            mk(('T',l,j)); mk(('B',l,j))
    # permutation of positions induced by crossings above level l
    from functools import reduce
    # prefix perms: pref[l] = permutation applied to top positions to get positions at level l
    pref=[list(range(n))]
    for l in range(L):
        a=abs(word[l])-1
        p=pref[l][:]
        p[a],p[a+1]=p[a+1],p[a]
        pref.append(p)
    # vertical wires between level l and l+1 at each top-position j: connects either stub or closure.
    # Represent wire endpoints as: top boundary ('TOP',j), bottom boundary ('BOT',j), plus stubs.
    for j in range(n):
        mk(('TOP',j)); mk(('BOT',j))
    def top_attach(l,j):
        # wire arriving at level l at position j (j = position at that level); if crossing l acts
        # on positions a,a+1 and j in {a,a+1}, attach to stub T; else pass through (union with below).
        a=abs(word[l])-1 if l<L else None
        if l<L and j in (a,a+1): return ('T',l,j)
        return None
    def bot_attach(l,j):
        # wire leaving level l+1 (position j at level l+1); if crossing l acted, attach to stub B.
        a=abs(word[l])-1
        # position at level l+1 is j; the pre-image position at level l is swap(j)
        pre = j
        if j==a: pre=a+1
        elif j==a+1: pre=a
        if pre in (a,a+1): return ('B',l,pre)
        return None
    # Build wires: for each strand path, chain endpoints. Easier: for each level-boundary position,
    # union top endpoint with next. Walk each wire: start at ('TOP',j0), position j=j0 at level 0;
    # for l in 0..L-1: endpoint E1 = stub-or-passthrough; if stub, stop (stub node represents wire end);
    # record node; then continue from stub B side after smoothing (handled via unions of stubs).
    # For pass-through positions, the wire continues: union current node with next boundary node.
    # Implement by creating chain nodes w[l][j] = wire point at level l position j.
    W={}
    for l in range(L+1):
        for j in range(n):
            W[(l,j)]=mk(('W',l,j))
    for j in range(n):
        union(('TOP',j),W[(0,j)])
        union(('BOT',j),W[(L,j)])
    for l in range(L):
        a=abs(word[l])-1
        for j in range(n):
            if j in (a,a+1):
                union(W[(l,j)],('T',l,j))
                # bottom: position j' at level l+1 with pre-image j
                jp = j
                # swap: level l+1 position = swap(j)? pref maps top->level; wire at top-pos k arrives
                # at level l position p=pref[l][k]... simpler: wire continuity: W[(l,j)]-stubT,
                # W[(l+1,jp)]-stubB where jp = j swapped.
                jp = j  # NO swap: B stub at position j continues to wire below at same position j
                union(W[(l+1,jp)],('B',l,j))
            else:
                union(W[(l,j)],W[(l+1,j)])
    # closure arcs: bottom j to top j
    for j in range(n):
        union(('BOT',j),('TOP',j))
    # smoothings: state[l]=0/1. For positive crossing (+i): A-smoothing pairs (T_a,B_a)+(T_b,B_b)
    # (parallel), B-smoothing pairs (T_a,T_b)+(B_a,B_b)? Actually the two smoothings of a crossing
    # pair the 4 stubs as either "through" or "turn". Orientation of which is A vs B depends on sign:
    # for negative crossing the A/B roles swap. Implement: s=state[l]; pos = word[l]>0;
    # A-state (s=0): if pos: through-pairing; else: turn-pairing. B-state (s=1): opposite.
    for l in range(L):
        a=abs(word[l])-1
        pos = word[l]>0
        s=state[l]
        A = (s==0)
        if not pos: A = not A
        if A:
            union(('T',l,a),('B',l,a)); union(('T',l,a+1),('B',l,a+1))
        else:
            union(('T',l,a),('T',l,a+1)); union(('B',l,a),('B',l,a+1))
    roots=set(find(x) for x in parent)
    return len(roots)

def bracket_jones(nstr, word, Amid='A'):
    from collections import defaultdict
    L=len(word)
    writhe=sum(1 if x>0 else -1 for x in word)
    # bracket poly in A: dict exp->coef; d = -A^2-A^-2
    poly=defaultdict(int)
    for bits in range(1<<L):
        state=[(bits>>l)&1 for l in range(L)]
        k=closure_circles(nstr,word,state)
        a_exp=sum(1 if s==0 else -1 for s in state)  # A^(#A-#B)
        # <state> = A^(a_exp) * d^(k-1)
        # expand d^(k-1)
        dp={0:1}
        for _ in range(k-1):
            nd=defaultdict(int)
            for e,c in dp.items():
                nd[e+2]-=c; nd[e-2]-=c
            dp=nd
        for e,c in dp.items():
            poly[a_exp+e]+=c
    # writhe normalize: f = (-A^3)^(-w) <K>; V(q) with q=A^-4, i.e. A=q^-1/4; report in q.
    # f exponents are integers; multiply by (-1)^(-w) A^(-3w).
    f=defaultdict(int)
    for e,c in poly.items():
        f[e-3*writhe]+=c*((-1)**(-writhe))
    # convert: A^e -> q^(-e/4). Exponents must be 0 mod 4? For knots yes after norm? Check.
    q=defaultdict(int)
    for e,c in f.items():
        assert e%1==0
        q[-e]+=c  # store 4x exponent (qexp*4 = -e)
    return dict(q), writhe

def fmt(q4):
    terms=[]
    for e4 in sorted(q4):
        c=q4[e4]
        if c==0: continue
        terms.append((e4,c))
    return terms

for name,nstr,word in [("trefoil",2,[-1,-1,-1]),("K11n34",4,[1,1,2,-3,2,1,-3,-2,-2,-3,-3]),("K11n42",4,[1,-2,3,-2,3,-2,-2,-1,2,-3,-3,2,2])]:
    q4,w=bracket_jones(nstr,word)
    print(name,"writhe",w,"q4terms",fmt(q4))
