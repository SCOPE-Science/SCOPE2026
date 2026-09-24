"""Strict-EKR certificates for explicit transitive degree-8 groups (stdlib only)."""
import json, random, sys, time

# ---------- permutations on {0..7} as tuples ----------
def comp(p, q):  # p after q
    return tuple(p[q[i]] for i in range(8))

def inv(p):
    q = [0]*8
    for i in range(8):
        q[p[i]] = i
    return tuple(q)

def ident():
    return tuple(range(8))

def build_group(gens):
    e = ident()
    G = {e}
    gens = list(gens) + [inv(g) for g in gens]
    stack = [e]
    while stack:
        a = stack.pop()
        for g in gens:
            for c in (comp(g, a), comp(a, g)):
                if c not in G:
                    G.add(c)
                    stack.append(c)
    return sorted(G)

def orbit(G, x=0):
    return sorted({g[x] for g in G})

def agree(p, q):
    return any(p[i] == q[i] for i in range(8))

def cyc(mapping):
    """mapping dict -> full tuple."""
    return tuple(mapping[i] for i in range(8))

# ---------- group models ----------
def model_C8():
    return [(1,2,3,4,5,6,7,0)]

def model_G24():
    # S4 by conjugation on its eight 3-cycles
    def cmul(a,b):  # perms of 0..3
        return tuple(a[b[i]] for i in range(4))
    def cinv(a):
        q=[0]*4
        for i in range(4): q[a[i]]=i
        return tuple(q)
    s=(1,0,2,3); t=(1,2,3,0)
    import itertools
    tc=[]
    for p in itertools.permutations(range(4)):
        fixed=sum(1 for i in range(4) if p[i]==i)
        if fixed==1 and cmul(cmul(p,p),p)==(0,1,2,3):
            tc.append(p)
    assert len(tc)==8, tc
    # note: the eight 3-cycles of S4 as image tuples
    def conj(g,c):
        return cmul(cmul(g,c),cinv(g))
    gens=[]
    for g in (s,t):
        mp={}
        for j,c in enumerate(tc):
            mp[j]=tc.index(conj(g,c))
        gens.append(tuple(mp[j] for j in range(8)))
    return gens

def model_G32():
    a=(1,2,3,0,4,5,6,7)
    b=(0,1,2,3,5,6,7,4)
    t=(4,5,6,7,0,1,2,3)
    return [a,b,t]

def model_G48():
    # S4 x C2 product action on pairs (i,j), idx=2i+j
    def emb(f, flip=False):
        m={}
        for i in range(4):
            for j in range(2):
                ni,nj=(f[i],j) if not flip else (i,1-j)
                m[2*i+j]=2*ni+nj
        return tuple(m[k] for k in range(8))
    A=(1,2,3,0); B=(1,0,2,3)
    return [emb(A),emb(B),emb(None,flip=True)] if False else [emb(A),emb(B),
        tuple(2*i+(1-j) for i in range(4) for j in range(2))]

def model_GW64():
    # C2 wr V4: flips within 4 pairs + V4 permuting pairs
    f0=(1,0,2,3,4,5,6,7)
    def pairperm(f):
        m={}
        for k in range(4):
            for e in range(2):
                m[2*k+e]=2*f[k]+e
        return tuple(m[v] for v in range(8))
    return [f0,pairperm((1,0,3,2)),pairperm((2,3,0,1))]

def model_AGL18():
    # x -> x+1 (xor) and x -> alpha*x in GF(8)=GF(2)[x]/(x^3+x+1)
    def gmul(a,b):
        p=0
        while b:
            if b&1: p^=a
            a<<=1
            if a&8: a^=0b1011  # x^3+x+1
            b>>=1
        return p&7
    t=tuple(v^1 for v in range(8))
    m=tuple(gmul(2,v) for v in range(8))
    return [t,m]

def model_GW384():
    # C2 wr S4
    f0=(1,0,2,3,4,5,6,7)
    def pairperm(f):
        m={}
        for k in range(4):
            for e in range(2):
                m[2*k+e]=2*f[k]+e
        return tuple(m[v] for v in range(8))
    return [f0,pairperm((1,2,3,0)),pairperm((1,0,2,3))]

# ---------- bitset max clique ----------
def adj_masks(G):
    n=len(G)
    adj=[0]*n
    for i in range(n):
        m=0
        gi=G[i]
        for j in range(n):
            if i!=j and agree(gi,G[j]):
                m|=1<<j
        adj[i]=m
    return adj

def color_sort(P, adj):
    classes=[]
    for v in P:
        for c in classes:
            ok=True
            av=adj[v]
            for u in c:
                if (av>>u)&1:
                    ok=False; break
            if ok:
                c.append(v); break
        else:
            classes.append([v])
    order=[]; colors=[]
    for k,c in enumerate(classes,1):
        for v in c:
            order.append(v); colors.append(k)
    return order,colors

def max_clique(adj,n,log):
    best=[0]; nodes=[0]
    sys.setrecursionlimit(10000)
    def expand(rs, P):
        nodes[0]+=1
        order,colors=color_sort(P,adj)
        for i in range(len(order)-1,-1,-1):
            if rs+colors[i]<=best[0]:
                return
            v=order[i]
            av=adj[v]
            newP=[u for u in order[:i] if (av>>u)&1]
            if rs+1>best[0]:
                best[0]=rs+1
            if newP:
                expand(rs+1,newP)
    expand(0,list(range(n)))
    log.append(f"max-clique BB: n={n} omega={best[0]} nodes={nodes[0]}")
    return best[0],nodes[0]

def enum_max_cliques(adj,n,k,log,cap=2000000):
    out=[]; nodes=[0]
    sys.setrecursionlimit(10000)
    def expand(R,P):
        nodes[0]+=1
        if len(out)>=cap:
            return True
        order,colors=color_sort(P,adj)
        for i in range(len(order)-1,-1,-1):
            if len(R)+colors[i]<k:
                return False
            v=order[i]
            av=adj[v]
            newP=[u for u in order[:i] if (av>>u)&1]
            if len(R)+1==k:
                out.append(tuple(sorted(R+[v])))
                if len(out)>=cap:
                    return True
            elif newP:
                if expand(R+[v],newP):
                    return True
        return False
    expand([],list(range(n)))
    log.append(f"enum BB: target={k} found={len(out)} nodes={nodes[0]} capped={len(out)>=cap}")
    return out

def stars(G):
    idx={g:i for i,g in enumerate(G)}
    S=set()
    for x in range(8):
        st=[g for g in G if g[x]==x]
        for a in G:
            S.add(frozenset(idx[comp(a,s)] for s in st))
    return S

def analyze(name, gens, exact=True):
    log=[f"=== {name} ==="]
    G=build_group(gens)
    n=len(G)
    log.append(f"order={n} transitive={len(orbit(G))==8} staborder={n//8 if n%8==0 else '?'}")
    assert len(orbit(G))==8, "not transitive!"
    assert n%8==0
    k=n//8
    adj=adj_masks(G)
    S=stars(G)
    log.append(f"num distinct stars(as sets)={len(S)}  (8 points x {k} cosets)")
    res=dict(name=name,order=n,k=k)
    if exact:
        om,nodes=max_clique(adj,n,log)
        res['omega']=om; res['bb_nodes']=nodes
        assert om==k, f"EKR upper bound mismatch: omega={om} k={k}"
        cl=enum_max_cliques(adj,n,k,log)
        res['num_max_cliques']=len(cl)
        non=[c for c in cl if frozenset(c) not in S]
        res['num_noncanonical']=len(non)
        res['strict_ekr']=len(non)==0
        log.append(f"strict-EKR verdict: {'HOLDS' if not non else 'FAILS'}")
        res['noncanonical']= [list(c) for c in non[:5]]
        res['cliques_idx']= [list(c) for c in cl] if len(cl)<=64 else None
    res['log']=log
    res['gens']=[list(g) for g in gens]
    return G,res

def heuristic_GW384(G, adj, n, k, S):
    rng=random.Random(20260908)
    found=[]; best=0; tries=6000
    idxG={g:i for i,g in enumerate(G)}
    for t in range(tries):
        # random-seed greedy from random edge
        a=rng.randrange(n)
        nbrs=[j for j in range(n) if (adj[a]>>j)&1]
        if not nbrs: continue
        b=rng.choice(nbrs)
        C={a,b}
        common=adj[a]&adj[b]
        cand=[j for j in range(n) if (common>>j)&1]
        rng.shuffle(cand)
        for v in cand:
            if all((adj[v]>>u)&1 for u in C):
                C.add(v)
        # maximal extension
        improved=True
        while improved:
            improved=False
            for v in range(n):
                if v not in C and all((adj[v]>>u)&1 for u in C):
                    C.add(v); improved=True
        if len(C)>best:
            best=len(C)
        if len(C)>=k and frozenset(C) not in S:
            # trim to exactly k if larger (can't exceed k=48 by theorem; record)
            found.append(sorted(C))
            if len(found)>=3:
                break
    return best,found,tries

if __name__=='__main__':
    t0=time.time()
    G48m=build_group(model_G48())
    print("G48 order",len(G48m),flush=True)
    results={}
    Gdict={}
    for name,fn in [("C8",model_C8),("G24",model_G24),("G32",model_G32),
                    ("G48",model_G48),("GW64",model_GW64),("AGL18",model_AGL18)]:
        G,res=analyze(name,fn())
        Gdict[name]=G; results[name]=res
        print("\n".join(res['log']),flush=True)
    # GW384 heuristic
    GW=build_group(model_GW384())
    n=len(GW); k=n//8
    log=[f"=== GW384 === order={n} transitive={len(orbit(GW))==8} staborder={k}"]
    print("\n".join(log),flush=True)
    adj=adj_masks(GW); S=stars(GW)
    best,found,tries=heuristic_GW384(GW,adj,n,k,S)
    print(f"heuristic: best_maximal_size={best} tries={tries} noncanonical_ge{k}={len(found)}",flush=True)
    wit=None
    if found:
        C=found[0][:k]
        # verify pairwise
        ok=all(agree(GW[i],GW[j]) for a,i in enumerate(C) for j in C[a+1:])
        instar=frozenset(C) in S
        print(f"witness size={len(C)} pairwise={ok} in_star={instar}",flush=True)
        wit=dict(clique_idx=C, perms=[list(GW[i]) for i in C], pairwise=ok, in_star=instar)
    results['GW384']=dict(name='GW384',order=n,k=k,heuristic_best=best,
                          witness=wit,gens=[list(g) for g in model_GW384()])
    Gdict['GW384']=GW
    with open('output/artifacts/results.json','w') as f:
        json.dump(results,f,indent=1)
    # save groups for verifier
    with open('output/artifacts/groups.json','w') as f:
        json.dump({m:[list(g) for g in Gdict[m]] for m in Gdict},f)
    print("elapsed",round(time.time()-t0,1),"s",flush=True)
