#!/usr/bin/env python3
"""Reproduce the Franklin graph's graph-metric Rips homotopy and symmetry result.
Standard-library Python (3.9+); no external files or packages.
"""
from collections import Counter, deque
from itertools import combinations
from fractions import Fraction

N = 12
LCF = (5, -5)


def graph():
    e = [set() for _ in range(N)]
    for i in range(N):
        for j in ((i+1)%N, (i+LCF[i%2])%N):
            e[i].add(j); e[j].add(i)
    assert all(len(s)==3 for s in e)
    assert sum(map(len,e))==36
    return e


def distances(e):
    D = [[N+1]*N for _ in range(N)]
    for root in range(N):
        D[root][root]=0
        queue=deque([root])
        while queue:
            i=queue.popleft()
            for j in e[i]:
                if D[root][j]>D[root][i]+1:
                    D[root][j]=D[root][i]+1
                    queue.append(j)
    assert all(D[i][j]==D[j][i] for i in range(N) for j in range(N))
    return D


def face_brute(D,scale):
    return {mask for mask in range(1<<N) if all(D[i][j] <= scale
            for i,j in combinations([k for k in range(N) if (mask>>k)&1],2))}


def maximal_cliques(neighbors):
    result=[]
    def bronk(R,P,X):
        if not P and not X:
            result.append(sum(1<<v for v in R)); return
        U=P|X
        p=max(sorted(U),key=lambda x:len(neighbors[x]&P)) if U else None
        for v in sorted(P-(neighbors[p] if p is not None else set())):
            bronk(R|{v},P&neighbors[v],X&neighbors[v])
            P.remove(v); X.add(v)
    bronk(set(),set(range(N)),set())
    return result


def verify_clique_faces(D,r,reference):
    neighborhoods=[{j for j in range(N) if i!=j and D[i][j]<=r} for i in range(N)]
    facets=maximal_cliques(neighborhoods)
    recovered={0}
    for f in facets:
        b=f
        while b:
            recovered.add(b)
            b=(b-1)&f
    assert recovered==reference
    return len(facets)


def discrete_morse(faces,order):
    remaining=set(faces); pair={}
    for v in order:
        for a in sorted(remaining,key=lambda a:(a.bit_count(),a)):
            b=a | (1<<v)
            if not (a>>v)&1 and a in remaining and b in remaining:
                remaining.remove(a); remaining.remove(b)
                pair[a]=b
    return remaining,pair


def verify_morse(faces,critical,pair):
    assert len(faces)==len(critical)+2*len(pair)
    used=set(pair)|set(pair.values())
    assert len(used)==2*len(pair) and used.isdisjoint(critical)
    assert used|critical==faces
    for a,b in pair.items():
        assert (b^a).bit_count()==1 and a.bit_count()+1==b.bit_count()
        assert a in faces and b in faces
    out={s:[] for s in faces}; indeg={s:0 for s in faces}; hasse=0
    for s in faces:
        for v in range(N):
            if not ((s>>v)&1):continue
            t=s^(1<<v)
            assert t in faces
            hasse+=1
            if pair.get(t)==s:a,b=t,s
            else:a,b=s,t
            out[a].append(b);indeg[b]+=1
    q=deque(sorted(s for s in faces if not indeg[s]));nseen=0
    while q:
        s=q.popleft();nseen+=1
        for t in out[s]:
            indeg[t]-=1
            if not indeg[t]:q.append(t)
    assert nseen==len(faces),'cyclic face-poset matching'
    return hasse


def all_automorphisms(e):
    result=[]
    def rec(p,used):
        if len(p)==N:
            result.append(tuple(p[i] for i in range(N)));return
        u=max((i for i in range(N) if i not in p),
              key=lambda i:(len(e[i]&p.keys()),-i))
        for v in range(N):
            if v in used:continue
            if all((u in e[w])==(v in e[p[w]]) for w in p):
                p[u]=v
                rec(p,used|{v})
                del p[u]
    rec({},set())
    assert len(result)==len(set(result))
    assert all(all(((i in e[j])==(p[i] in e[p[j]])) for i in range(N) for j in range(N)) for p in result)
    return result


def compose(a,b):
    return tuple(a[b[i]] for i in range(N))


def perm_order(p):
    k=1;z=p;I=tuple(range(N))
    while z!=I:
        z=compose(p,z);k+=1
        assert k<100
    return k


def reduced_lefschetz(p,faces):
    # Augmentation subtracts 1; reduced Lefschetz of wedge of 2-spheres
    # equals trace on the second rational homology.
    res=-1
    for mask in faces:
        if mask==0:continue
        verts=[v for v in range(N) if (mask>>v)&1]
        images=[p[v] for v in verts]
        if set(images)!=set(verts):continue
        inversions=sum(1 for i in range(len(images)) for j in range(i+1,len(images))
                       if images[i]>images[j])
        res+=(-1)**(len(verts)-1+inversions)
    return res


def main():
    E=graph();D=distances(E)
    assert max(map(max,D))==3
    cnt=Counter(D[i][j] for i in range(N) for j in range(i+1,N))
    assert cnt==Counter({1:18,2:30,3:18})
    f2=face_brute(D,2)
    assert len(f2)==196
    assert verify_clique_faces(D,2,f2)==17
    assert Counter(m.bit_count()-1 for m in f2)=={-1:1,0:12,1:48,2:76,3:45,4:12,5:2}
    for label,order in [('ascending',range(N)),('descending',reversed(range(N)))]:
        critical,pair=discrete_morse(f2,list(order))
        assert len(pair)==96
        assert Counter(m.bit_count()-1 for m in critical)=={2:4}
        assert 0 in pair and pair[0].bit_count()==1
        h=verify_morse(f2,critical,pair)
        assert h==sum(k*val for k,val in [(1,12),(2,48),(3,76),(4,45),(5,12),(6,2)])
        assert h==588
        print(f'morse_{label}: pairs=96 critical_2cells=4 hasse=588 acyclic=PASS')
    far=[{j for j in range(N) if D[i][j]==3} for i in range(N)]
    assert all(len(t)==3 for t in far)
    # VR_2 is literally the independence complex of the distance-three graph.
    for mask in range(1<<N):
        v=[i for i in range(N) if mask>>i&1]
        assert (mask in f2)==all(j not in far[i] for i,j in combinations(v,2))
    assert all_automorphisms(far) and len(all_automorphisms(far))==48
    # Check the distance-three graph is isomorphic to the original Franklin graph.
    def isomorphisms(e1,e2):
        ans=[]
        def rec(p,used):
            if len(p)==N:
                ans.append(tuple(p[i] for i in range(N)));return
            u=max((i for i in range(N) if i not in p),key=lambda i:(len(e1[i]&p.keys()),-i))
            for v in range(N):
                if v in used:continue
                if all((u in e1[w])==(v in e2[p[w]]) for w in p):
                    p[u]=v;rec(p,used|{v});del p[u]
        rec({},set());return ans
    assert isomorphisms(E,far)
    perms=all_automorphisms(E)
    assert len(perms)==48
    I=tuple(range(N));z=tuple((v+6)%N for v in range(N))
    assert z in perms
    center=[p for p in perms if all(compose(p,q)==compose(q,p) for q in perms)]
    assert set(center)=={I,z}
    chars={p:reduced_lefschetz(p,f2) for p in perms}
    assert chars[I]==4 and chars[z]==-2
    stat=Counter((perm_order(p),chars[p]) for p in perms)
    expected={(1,4):1,(2,-2):1,(2,2):9,(2,0):9,(3,1):8,(6,1):8,(4,2):6,(4,0):6}
    assert dict(stat)==expected
    plus={p:(chars[p]+chars[compose(z,p)])//2 for p in perms}
    minus={p:(chars[p]-chars[compose(z,p)])//2 for p in perms}
    assert all((chars[p]+chars[compose(z,p)])%2==0 for p in perms)
    assert all(v==1 for v in plus.values())
    assert minus[I]==3 and minus[z]==-3
    inner=Fraction(sum(v*v for v in minus.values()),len(perms))
    assert inner==1  # integer-valued character of absolutely irreducible 3D summand
    assert Fraction(sum(chars.values()),len(perms))==1
    print('graph: 12 vertices, 18 edges, diameter 3, distance distribution 18/30/18')
    print('rips2: faces_including_empty=196 facets=17 f_vector=12,48,76,45,12,2')
    print('distance3_graph: isomorphic_to_franklin=PASS; rips2_is_independence_complex=PASS')
    print('automorphisms=48 center_order2_shift6=PASS')
    print('character_histogram_by_order_and_trace='+repr(sorted(stat.items())))
    print('homology_character: trivial_plus_line=PASS, irreducible_minus_3space=PASS, norm='+str(inner))
    print('rips: r0=11*S0 r1=7*S1 r2=4*S2 r3=point')
    print('FRANKLIN_RIPS_SYMMETRY_VERIFIED')

if __name__=='__main__':main()
