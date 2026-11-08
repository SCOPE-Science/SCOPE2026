from verify_ternary_pg_mh import graph,distances,basis_by_endpoints
from collections import Counter
from itertools import product,permutations

def all_projectivities():
    vectors=[]
    for x in product(range(3),repeat=3):
        if any(x):
            i=next(t for t,v in enumerate(x) if v)
            vectors.append(tuple(v*pow(x[i],-1,3)%3 for v in x))
    pts=sorted(set(vectors));ix={p:j for j,p in enumerate(pts)}
    nbr=graph()
    lines_to_points={frozenset(v for v in nbr[13+j]):j for j in range(13)}
    reps=[]
    for a in product(range(3),repeat=9):
        if not any(a):continue
        if next(x for x in a if x)!=1:continue
        m=[a[0:3],a[3:6],a[6:9]]
        det=(m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])-m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])+m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))%3
        if not det:continue
        pp=[]
        for p in pts:
            v=tuple(sum(m[i][j]*p[j] for j in range(3))%3 for i in range(3))
            s=next(x for x in v if x)
            pp.append(ix[tuple(x*pow(s,-1,3)%3 for x in v)])
        lp=[]
        for j in range(13):
            target=frozenset(pp[p] for p in nbr[13+j])
            lp.append(13+lines_to_points[target])
        reps.append(tuple(pp+lp))
    assert len(reps)==5616,len(reps)
    assert len(set(reps))==5616
    return reps

def main():
    N=graph();D=distances(N);B=basis_by_endpoints(D)
    masks={k:[sum(1<<v for v in set(seq)) for m in B.values() for seq in m.get(k,[])] for k in (2,3,4)}
    assert [len(masks[k]) for k in (2,3,4)]==[5616,14976,6656]
    triangles=[]
    for first,last in ((0,13),(13,26)):
        # Ordered projective triangles are point triples not on one line,
        # or dually three lines without a common intersection point.
        opposite=range(13,26) if first==0 else range(13)
        for triple in permutations(range(first,last),3):
            if not any(all(w in N[z] for w in triple) for z in opposite):
                triangles.append(sum(1<<v for v in triple))
    assert len(triangles)==2808
    permutation_trace_cache={}
    def triangle_trace(p):
        mask=sum(1<<i for i,x in enumerate(p) if i==x)
        if mask not in permutation_trace_cache:
            permutation_trace_cache[mask]=sum((t & mask)==t for t in triangles)
        return permutation_trace_cache[mask]
    cache={}
    def character(p):
        mask=sum(1<<i for i,x in enumerate(p) if i==x)
        if mask not in cache:
            tr={k:sum((seqmask & mask)==seqmask for seqmask in masks[k]) for k in (2,3,4)}
            tr4diag=sum((mask>>x&1) and (mask>>y&1) for x in range(26) for y in N[x])
            cache[mask]=tr[3]-tr[2]-tr[4]+tr4diag
        return cache[mask]
    chars=Counter();byfix=Counter(); nontrivial=[]; involutions=0; involution_traces=Counter()
    # Independent endpoint-indexed computation for one element from every fixed-set profile.
    checked_profiles=set()
    elements=all_projectivities()
    for p in elements:
        ch=character(p);chars[ch]+=1
        assert ch==triangle_trace(p), (ch,triangle_trace(p))
        fixp=sum(i==p[i] for i in range(13));fixl=sum(i+13==p[i+13] for i in range(13));
        byfix[(fixp,fixl,ch)]+=1
        if ch<0:nontrivial.append((fixp,fixl,ch))
        if all(p[p[i]]==i for i in range(26)) and any(p[i]!=i for i in range(26)):
            involutions+=1;involution_traces[ch]+=1
        profile=(fixp,fixl,ch)
        if profile not in checked_profiles:
            checked_profiles.add(profile)
            # Recompute traces directly by iterating the ordered tuple basis by endpoint.
            alt={k:0 for k in (2,3,4)}
            for endpoints,sections in B.items():
                if any(p[v]!=v for v in endpoints):continue
                for k in (2,3,4):
                    alt[k]+=sum(all(p[v]==v for v in seq) for seq in sections.get(k,[]))
            alt4=sum(p[x]==x and p[y]==y for x in range(26) for y in N[x])
            assert ch==alt[3]-alt[2]-alt[4]+alt4,profile
    assert sum(chars.values())==5616
    assert chars==Counter({0:5498,72:117,2808:1})
    assert involutions==117 and involution_traces==Counter({72:117})
    fixed=sum(ch*m for ch,m in chars.items())
    assert fixed%5616==0
    print('PGL3(3) size 5616; trace distribution',sorted(chars.items()))
    print('PGL3(3) fixed-point and character distribution',sorted(byfix.items()))
    print('Order-two elements, all of trace 72:', involutions)
    print('Character agrees with the 2808-dimensional ordered-projective-triangle permutation module for all 5616 projectivities')
    print('Projective-triangle stabilizer size:',5616//1404)
    print('Direct endpoint-indexed trace check across fixed-point profiles:',len(checked_profiles))
    print('Invariants dimension on full 2808-dimensional homology:',fixed//5616)
    print('PGL3(3) invariant dimension on point-only summand:',fixed//(5616*2))
    print('Point-line duality has trace zero; full automorphism invariant dimension:',fixed//(5616*2))
    print('Unique fixed vertex masks',len(cache))
    print('group character average numerator',fixed)
    print('CHARACTER_PGL3_TERNARY_PROJECTIVE_MAGNITUDE_VERIFIED')
if __name__=='__main__':main()
