from collections import Counter,deque,defaultdict
from functools import lru_cache
from itertools import combinations

# Cubic Möbius ladder: 2n vertices, outer cycle, n opposite-vertex chords.
def edge_list(n):
    assert n >= 3
    N=2*n
    return sorted({tuple(sorted((i,(i+1)%N))) for i in range(N)}|{(i,i+n) for i in range(n)})

def faces_of(n):
    es=edge_list(n);faces=[]
    for mask in range(1<<len(es)):
        deg=[0]*(2*n);ok=True
        for i,(a,b) in enumerate(es):
            if mask>>i&1:
                deg[a]+=1;deg[b]+=1
                if deg[a]>2 or deg[b]>2:ok=False;break
        if ok:faces.append(mask)
    return es,faces

def match(faces,m,order):
    rest=set(faces); upper={}; lower={}
    for i in order:
        for f in faces:
            g=f |(1<<i)
            if not f>>i&1 and f in rest and g in rest:
                rest.remove(f);rest.remove(g);upper[f]=g;lower[g]=f
    return rest,upper,lower

def directed_hasse_acyclic(faces,upper,lower,m):
    idx={f:i for i,f in enumerate(faces)}
    indeg=[0]*len(faces);outs=[[] for _ in faces];covers=0
    for f in faces:
        a=idx[f]
        for i in range(m):
            if f>>i&1:
                g=f^(1<<i);b=idx[g];covers+=1
                if lower.get(f)==g:
                    outs[b].append(a);indeg[a]+=1
                else:
                    outs[a].append(b);indeg[b]+=1
    q=deque(i for i,d in enumerate(indeg) if d==0); seen=0
    while q:
        a=q.popleft();seen+=1
        for b in outs[a]:
            indeg[b]-=1
            if not indeg[b]:q.append(b)
    return seen==len(faces),covers

def signed_bd(f):
    out={};i=0
    for j in range(f.bit_length()):
        if f>>j&1:
            out[f^(1<<j)]=(-1)**i
            i+=1
    return out

def morse_matrix(crit,lower,upper,dimension):
    # Morse reduction of chains in degree dimension; remove matched upper generators,
    # substitute for matched lower using unit signed boundary.
    @lru_cache(None)
    def reduce(f):
        if f in lower: return {} # f is matched upper, removed
        if f not in upper: return {f:1}
        u=upper[f]
        bd=signed_bd(u);a=bd[f]
        acc=defaultdict(int)
        for g,co in bd.items():
            if g==f: continue
            for h,coeff in reduce(g).items():acc[h]-=a*co*coeff
        return {h:co for h,co in acc.items() if co}
    low=sorted(f for f in crit if f.bit_count()-1==dimension)
    high=sorted(f for f in crit if f.bit_count()-1==dimension+1)
    M=[]
    for f in high:
        d=defaultdict(int)
        for g,co in signed_bd(f).items():
            for h,c in reduce(g).items():d[h]+=co*c
        M.append([d.get(g,0) for g in low])
    return low,high,M,reduce.cache_info()

def rank_mod2(n):
    # for small n, independent GF(2) simplicial homology
    E,fs=faces_of(n);F={k:[] for k in range(-1,3*n)}
    for x in fs:F[x.bit_count()-1].append(x)
    dimensions=[];ranks={}
    for dim in range(0,max(k for k,v in F.items() if v)+1):
        lows={f:i for i,f in enumerate(F[dim-1])}
        pivots={};rank=0
        for f in F[dim]:
            b=0
            for i in range(f.bit_length()):
                if f>>i&1:b^=1<<lows[f^(1<<i)]
            while b:
                p=b.bit_length()-1
                if p not in pivots:
                    pivots[p]=b;rank+=1;break
                b^=pivots[p]
        ranks[dim]=rank
    hom={k:len(v)-ranks.get(k,0)-ranks.get(k+1,0) for k,v in F.items() if k>=0 and v}
    return {k:v for k,v in hom.items() if v>0}

if __name__ == '__main__':
    expected = {
        3: (265, 936, {3:1}, {3:1}),
        4: (1697, 7976, {5:1}, {5:1}),
        5: (10897, 64040, {6:2,7:3}, {7:1}),
        6: (69941, 493212, {7:1,8:4}, {8:3}),
    }
    for n in range(3, 7):
        edges,faces=faces_of(n)
        ef,ec,forward_crit,hom=expected[n]
        assert len(edges)==3*n
        assert len(faces)==ef
        # Euler and integral Morse checks alone would not establish the result;
        # independent mod-two simplicial boundary ranks are checked as well.
        assert rank_mod2(n)==hom
        print('n',n,'edges',len(edges),'faces_with_empty',len(faces))
        print('mod_two_reduced_homology',rank_mod2(n))
        for ordering in ('forward','reverse'):
            ids=range(len(edges)) if ordering=='forward' else range(len(edges)-1,-1,-1)
            crit,up,down=match(faces,len(edges),ids)
            good,covers=directed_hasse_acyclic(faces,up,down,len(edges))
            assert good and covers==ec
            assert len(crit)+2*len(up)==len(faces)
            cd=dict(sorted(Counter(f.bit_count()-1 for f in crit).items()))
            assert (-1 not in cd) and (0 not in cd)
            if n<=4:
                assert cd==forward_crit
                matrix=[]
            elif n==5:
                d=6
                assert cd==({6:2,7:3} if ordering=='forward' else {6:1,7:2})
                _,_,matrix,_=morse_matrix(crit,down,up,d)
                assert matrix==([[1,0],[0,1],[-1,1]] if ordering=='forward' else [[-1],[-1]])
            else:
                d=7
                assert cd==forward_crit
                _,_,matrix,_=morse_matrix(crit,down,up,d)
                assert matrix==([[-1],[1],[-1],[1]] if ordering=='forward' else [[1],[-1],[-1],[-1]])
            print(ordering,'pairs',len(up),'critical',cd,'cover_relations',covers,'acyclic',good,'integer_boundary',matrix)
    print('all_four_cases_verified')
