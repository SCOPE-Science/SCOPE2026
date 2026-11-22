"""Stand-alone exact integral topological computation for the full strong matching complex of the unfilled ten-cycle."""
from collections import defaultdict, Counter, deque
from functools import lru_cache
from itertools import product

N = 10
ORDER=(9,7,14,12,6,2,5,10,11,15,16,13,0,4,3,1,17,19,8,18)

def faces_orientations():
    # Edge (i,i+1) has orientation '+' if i->i+1 and '-' otherwise.
    full=[]
    for orientations in product((1,-1),repeat=N):
        # All equal would produce a directed cycle, not an ordering.
        if len(set(orientations))==1: continue
        mask=0
        for i in range(N):
            if orientations[(i-1)%N]==orientations[i]:
                b=2*i+(orientations[i]==-1)
                mask|=1<<b
        full.append(mask)
    faces=set()
    for x in set(full):
        t=x
        while t:
            faces.add(t)
            t=(t-1)&x
    return set(full),faces

def faces_words():
    faces=set()
    for w in product((0,1,-1),repeat=N):
        if not any(w):continue
        if any(w[i] and w[(i+1)%N] and w[i]!=w[(i+1)%N] for i in range(N)):continue
        if (1 not in w or -1 not in w) and not any(w[i]==w[(i+1)%N]==0 for i in range(N)):continue
        faces.add(sum(1<<(2*i+(w[i]==-1)) for i in range(N) if w[i]))
    return faces

def matching(faces):
    remain=faces.copy(); low_to_high={}; high_to_low={}
    for bit in ORDER:
        b=1<<bit
        for lo in sorted(remain):
            if lo&b:continue
            hi=lo|b
            if hi in remain:
                remain.remove(lo);remain.remove(hi)
                low_to_high[lo]=hi;high_to_low[hi]=lo
    assert len(remain)+2*len(low_to_high)==len(faces)
    return remain,low_to_high,high_to_low

def hasse_acyclic(faces,low_to_high):
    degree={x:0 for x in faces}; dest=defaultdict(list); edges=0
    for hi in faces:
        bits=hi
        while bits:
            b=bits&-bits;bits^=b
            lo=hi^b
            if not lo:continue
            if low_to_high.get(lo)==hi:
                src,trg=lo,hi
            else:
                src,trg=hi,lo
            dest[src].append(trg);degree[trg]+=1;edges+=1
    q=deque(x for x,d in degree.items() if d==0)
    seen=0
    while q:
        u=q.popleft();seen+=1
        for v in dest[u]:
            degree[v]-=1
            if degree[v]==0:q.append(v)
    assert seen==len(faces),(seen,len(faces))
    return edges

def signed_boundary(x):
    # Homological boundary of oriented sorted vertices of a simplex.
    bits=x;j=0
    while bits:
        b=bits&-bits;bits^=b
        yield x^b, (-1 if j&1 else 1)
        j+=1

def morse_boundary(critical,low_to_high,high_to_low):
    crit4={f for f in critical if f.bit_count()==5}
    crit5={f for f in critical if f.bit_count()==6}
    assert len(crit4)==1 and len(crit5)==2
    @lru_cache(None)
    def push(f):
        if f in crit4:return 1
        if f in high_to_low:return 0
        if f not in low_to_high:raise AssertionError(('unclassified',f))
        up=low_to_high[f]
        eps=next(c for g,c in signed_boundary(up) if g==f)
        s=sum(c*push(g) for g,c in signed_boundary(up) if g!=f)
        return -eps*s
    matrix={h:sum(c*push(g) for g,c in signed_boundary(h)) for h in crit5}
    assert all(v==0 for v in matrix.values()),matrix
    return matrix,push.cache_info()

def rank_mod2(columns):
    piv={}
    for col in columns:
        while col:
            i=col.bit_length()-1
            if i not in piv:
                piv[i]=col;break
            col^=piv[i]
    return len(piv)

def simplicial_betti(faces):
    levels=defaultdict(list)
    for x in faces:levels[x.bit_count()-1].append(x)
    ranks={0:0}
    for dim in range(1,max(levels)+1):
        inds={x:i for i,x in enumerate(levels[dim-1])}
        cols=[]
        for f in levels[dim]:
            col=0
            for g,_ in signed_boundary(f):col^=1<<inds[g]
            cols.append(col)
        ranks[dim]=rank_mod2(cols)
    betti={k:len(v)-ranks.get(k,0)-ranks.get(k+1,0)-(k==0) for k,v in levels.items()}
    return {k:v for k,v in betti.items() if v},ranks

def main():
    assert len(ORDER)==2*N and set(ORDER)==set(range(2*N))
    generating,faces=faces_orientations()
    assert faces==faces_words(),('word disagreement',len(faces),len(faces_words()))
    assert len(faces)==6480
    print('FACES',len(faces),'GENERATORS',len(generating),'FACET_VECTOR',sorted(Counter(f.bit_count()-1 for f in faces).items()))
    max_size=max(x.bit_count() for x in generating)
    top_generators=[x for x in generating if x.bit_count()==max_size]
    pure=set()
    for x in top_generators:
        sub=x
        while sub:
            pure.add(sub)
            sub=(sub-1)&x
    extra=faces-pure
    assert (max_size,len(top_generators),len(pure),len(extra))==(8,90,6280,200)
    assert Counter(x.bit_count()-1 for x in extra)=={3:50,4:100,5:50}
    pure_betti,_=simplicial_betti(pure)
    assert pure_betti=={2:1,5:2},pure_betti
    print('PURE_COMPARISON',len(pure),'EXTRA',sorted(Counter(x.bit_count()-1 for x in extra).items()),'PURE_MOD2',sorted(pure_betti.items()))
    critical,lt,ht=matching(faces)
    profile=Counter(f.bit_count()-1 for f in critical)
    assert profile=={0:1,4:1,5:2},profile
    print('MATCHED_PAIRS',len(lt),'CRITICAL',sorted((x,x.bit_count()-1) for x in critical))
    edges=hasse_acyclic(faces,lt)
    print('HASSE_ACYCLIC',len(faces),'INCIDENCES',edges)
    matrix,cache=morse_boundary(critical,lt,ht)
    print('SIGNED_MORSE_BOUNDARY',sorted(matrix.items()),'CACHE',cache)
    betti,ranks=simplicial_betti(faces)
    assert betti=={4:1,5:2},betti
    print('RAW_MOD2_BETTI',sorted(betti.items()),'RANKS',sorted(ranks.items()))
    print('ALL_VERIFY_OK')

if __name__=='__main__':main()
