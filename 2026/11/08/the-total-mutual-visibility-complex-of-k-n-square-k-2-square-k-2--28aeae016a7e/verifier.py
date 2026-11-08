"""Independent finite tests for total mutual-visibility on K_n square K_2 square K_2.
All computations use integer bitsets and Python's standard library.
"""
from itertools import combinations
from collections import Counter, deque
from math import comb


def graph(n):
    v=[(i,a,b) for i in range(n) for a in range(2) for b in range(2)]
    ad=[]
    for x in v:
        ad.append({j for j,y in enumerate(v) if sum(a!=b for a,b in zip(x,y))==1})
    return v,ad

def forbidden_middle_pairs(n):
    v,adj=graph(n)
    obs=set()
    for i in range(len(v)):
        for j in range(i+1,len(v)):
            common=adj[i]&adj[j]
            if common and j not in adj[i]:
                assert len(common)==2
                obs.add(sum(1<<k for k in common))
    return sorted(obs)

def direct_visibility(n, selected):
    vertices,adj=graph(n)
    N=len(vertices)
    for u in range(N):
        for v in range(u+1,N):
            dist=sum(a!=b for a,b in zip(vertices[u],vertices[v]))
            reached={u}
            frontier={u}
            for _ in range(dist):
                frontier={w for x in frontier for w in adj[x] if w==v or not selected>>w&1}
                reached|=frontier
            if v not in frontier:
                return False
    return True

def accepted_sets(n):
    vertices,adj=graph(n)
    bad=forbidden_middle_pairs(n)
    N=len(vertices)
    ban=[0]*N
    for p in bad:
        i,j=[b for b in range(N) if p>>b&1]
        ban[i]|=1<<j
        ban[j]|=1<<i
    acc=[]
    def rec(i, mask, excluded):
        if i==N:
            acc.append(mask)
            return
        rec(i+1,mask,excluded)
        if not (excluded>>i)&1:
            rec(i+1,mask|1<<i,excluded|ban[i])
    rec(0,0,0)
    return acc,bad

def classification(n,mask):
    cols=[]
    for a in range(n):
        cols.append([b for b in range(4) if mask>>(4*a+b)&1])
    active=[c for c in cols if c]
    if not active:return True
    if len(active)==1:
        one=active[0]
        return len(one)==1 or (len(one)==2 and (one[0]^one[1]).bit_count()==1)
    return all(len(c)==1 for c in active) and len({(c[0].bit_count()%2) for c in active})==1

def components(masks):
    idx=set(masks)
    cc=0
    while idx:
        cc+=1
        start=idx.pop(); q=[start]
        while q:
            s=q.pop()
            one=[i for i in range(s.bit_length()) if s>>i&1]
            for i in one:
                t=s^(1<<i)
                for j in range(max(1,max(masks).bit_length())):
                    if t>>j&1:continue
                    u=t|(1<<j)
                    if u in idx:
                        idx.remove(u);q.append(u)
    return cc

def rank_binary(vectors):
    piv={}
    for u in vectors:
        while u:
            p=u.bit_length()-1
            if p not in piv:
                piv[p]=u; break
            u^=piv[p]
    return len(piv)

def bettis(faces):
    groups={k:sorted(m for m in faces if m.bit_count()==k) for k in range(max(m.bit_count() for m in faces)+1)}
    ranks={0:0}
    for k in range(2,max(groups)+1):
        index={m:i for i,m in enumerate(groups[k-1])}
        columns=[]
        for s in groups[k]:
            col=0
            for a in range(s.bit_length()):
                if s>>a&1:
                    t=s^(1<<a)
                    col^=1<<index[t]
            columns.append(col)
        ranks[k]=rank_binary(columns)
    return {k-1:len(groups[k])-ranks.get(k,0)-ranks.get(k+1,0) for k in groups if k>0}


def verify():
    total=0
    for n in range(2,7):
        faces,obs=accepted_sets(n)
        counter=Counter(s.bit_count() for s in faces)
        expected={0:1,1:4*n}
        for k in range(2,n+1):
            expected[k]=2*comb(n,k)*2**k + (4*n if k==2 else 0)
        assert dict(counter)==expected,(n,counter,expected)
        face_set=set(faces)
        facets=[s for s in faces if all((s|1<<a) not in face_set for a in range(4*n) if not (s>>a)&1)]
        f=Counter(s.bit_count() for s in facets)
        assert f==({2:4*n, n:2**(n+1)} if n>2 else {2:4*n+2**(n+1)}),(n,f)
        if n<=3:
            for s in range(1<<(4*n)):
                assert (s in face_set)==direct_visibility(n,s),(n,s,'direct_geodesic')
        if n<=4:
            for s in range(1<<(4*n)):
                brute=all((s&bad)!=bad for bad in obs)
                assert brute==classification(n,s),(n,s)
            b={i:r for i,r in bettis(faces).items() if r}
            if n==2:
                assert b=={0:1,1:9},(n,b)
            else:
                assert b=={0:1,1:4*n-1,n-1:2},(n,b)
        for k in range(1,n+1):
            group=[s for s in faces if s.bit_count()==k]
            cc=components(group)
            want=1 if k<=2 else 2
            assert cc==want,(n,k,cc,want)
        total+=len(faces)
        print(f'n={n} vertices={4*n} forbidden_pairs={len(obs)} faces={len(faces)} facets={len(facets)} coeffs={sorted(counter.items())} TJ=PASS')
    print(f'VERIFY_OK n=2..6 total_faces={total} exact_enumerators=PASS maximal_spectrum=PASS exhaustive_masks_n2..4=PASS mod2_homology_n2..4=PASS direct_shortest_paths_n2..3=PASS all_token_jumping_components=PASS')
if __name__=='__main__': verify()
