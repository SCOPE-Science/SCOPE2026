"""Finite obstruction-hypergraph certificate, affine orbits, exchange graph.
All indices i=4*r+c on Z_4 times Z_4; S is the 6-element Cayley step set.
The test on omitted 7-sets proves the minimum because feasibility is monotone.
"""
from itertools import combinations,permutations
from collections import Counter

U=set(range(16)); ALL=(1<<16)-1
STEPS={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}

def graph(name):
    result=[]
    for i in range(16):
        r,c=divmod(i,4)
        if name=='rook':
            result.append({j for j in range(16) if j!=i and ((j//4)==r or (j%4)==c)})
        else:
            result.append({(4*((r+a)%4)+(c+b)%4) for a,b in STEPS})
    return result

def bits(a):
    return sum(1<<i for i in a)

def group(name):
    if name=='rook':
        perm4=list(permutations(range(4)))
        out=[]
        for p in perm4:
            for q in perm4:
                out.append(tuple(4*p[i//4]+q[i%4] for i in range(16)))
                out.append(tuple(4*p[i%4]+q[i//4] for i in range(16)))
        assert len(out)==len(set(out))==1152
        return out
    maps=[]
    for a in range(4):
      for b in range(4):
       for c in range(4):
        for d in range(4):
         if {((a*x+b*y)%4,(c*x+d*y)%4) for x,y in STEPS}==STEPS:
          maps.append((a,b,c,d))
    assert len(maps)==12
    out=[]
    for u in range(4):
      for v in range(4):
       for a,b,c,d in maps:
        out.append(tuple(4*((a*(i//4)+b*(i%4)+u)%4)+
                         (c*(i//4)+d*(i%4)+v)%4 for i in range(16)))
    assert len(out)==len(set(out))==192
    return out

def image(mask,p):
    return sum(1<<p[i] for i in range(16) if mask>>i&1)

def obstruction(name):
    adj=graph(name)
    N=[a|{i} for i,a in enumerate(adj)]
    B=set()
    edges=0
    for u in range(16):
        for v in range(u+1,16):
            if v not in adj[u]:continue
            edges+=1
            A=N[u]-N[v];C=N[v]-N[u]
            assert len(A)==len(C)==3
            for x in combinations(sorted(A),2):
                for y in combinations(sorted(C),2):
                    B.add(bits(x+y))
    assert edges==48
    B=sorted(B)
    print(name, 'distinct minimal four-omission separation obstructions',len(B))
    # Compare every cardinality of omitted vertices through seven.
    candidates=Counter();valid=Counter(); minima=[]; sep_seven=set(); sep_six=set()
    for k in range(8):
        for subset in combinations(range(16),k):
            O=bits(subset)
            if any((O&f)==f for f in B):continue
            candidates[k]+=1
            if k==7:sep_seven.add(O)
            if k==6:sep_six.add(O)
            if any(len(set(subset)&v)>=6 for v in N):continue
            valid[k]+=1
            if k==6: minima.append(ALL^O)
    print(name, 'separation survivors by omission count',sorted(candidates.items()))
    print(name, 'valid by omission count',sorted(valid.items()))
    assert valid[7]==0 and valid[6]>0
    if name=='rook':
        assert sep_seven=={bits(x) for x in N}
        assert len(sep_six - {bits(tuple(t)) for v in N for t in combinations(sorted(v),6)})==720
    else:
        assert sep_seven==set()
    assert valid[4]==(1496 if name=='rook' else 1424)
    assert valid[5]==(1920 if name=='rook' else 1392)
    assert valid[6]==(720 if name=='rook' else 256)
    assert len(B)==(324 if name=='rook' else 396)
    # The full generating polynomial has coefficients from the valid table;
    # no k >= 7 omitted set is feasible by monotonicity.
    aut=group(name)
    for p in aut:
        for u in range(16):
            assert {p[v] for v in adj[u]}==adj[p[u]]
    unseen=set(minima);orbits=[]
    while unseen:
        r=min(unseen)
        orbit={image(r,p) for p in aut}
        assert orbit<=set(minima)
        unseen.difference_update(orbit)
        orbits.append((len(orbit),r))
    orbits.sort()
    print(name,'automorphisms',len(aut),'optimum_orbits',[(k,hex(rep)) for k,rep in orbits])
    opt=set(minima); adjacency={}
    for C in opt:
        adjacent=set()
        for a in range(16):
            if not (C>>a)&1:continue
            for b in range(16):
                if (C>>b)&1:continue
                nxt=C^(1<<a)^(1<<b)
                if nxt in opt:adjacent.add(nxt)
        adjacency[C]=adjacent
    assert all(C in adjacency[D] for C,A in adjacency.items() for D in A)
    seen=set(); component_sizes=[];component_degrees=[]; components=[]
    for C in opt:
        if C in seen:continue
        comp={C};queue=[C];seen.add(C)
        for x in queue:
            for y in adjacency[x]:
                if y not in seen:seen.add(y);comp.add(y);queue.append(y)
        components.append(frozenset(comp))
        component_sizes.append(len(comp))
        component_degrees.append((len(comp),tuple(sorted(Counter(len(adjacency[x]) for x in comp).items()))))
    print(name,'exchange degree distribution',sorted(Counter(map(len,adjacency.values())).items()))
    print(name,'exchange components',sorted(Counter(component_sizes).items()), 'edge_count',sum(map(len,adjacency.values()))//2)
    print(name,'component degree patterns', sorted(Counter(component_degrees).items()))
    target=([720] if name=='rook' else [1]*16+[16]*6+[144])
    assert sorted(component_sizes)==target
    if name=='rook':
        diameters=set()
        for base in sorted(opt):
            dist={base:0};queue=[base]
            for vertex in queue:
                for nxt in adjacency[vertex]:
                    if nxt not in dist:
                        dist[nxt]=dist[vertex]+1
                        queue.append(nxt)
            assert len(dist)==720
            diameters.add(max(dist.values()))
        assert diameters=={6}
        print('rook exchange graph diameter',6)
    if name=='shrikhande':
        # An explicit adjacency-preserving bijection from the 4x4 rook graph
        # onto one 16-vertex component; the group moves it to the other five.
        witness=[0x1f4f,0x0f6f,0x0fcf,0x4f4f,
                 0x3f0f,0x2f2f,0x2f8f,0x6f0f,
                 0x9f0f,0x8f2f,0x8f8f,0xcf0f,
                 0x1f1f,0x0f3f,0x0f9f,0x4f1f]
        assert len(set(witness))==16 and all(C in opt for C in witness)
        rook=graph('rook')
        for i in range(16):
            for j in range(16):
                if i!=j:
                    assert (witness[j] in adjacency[witness[i]])==(j in rook[i])
        component_orbit={frozenset(image(C,p) for C in witness) for p in aut}
        small_components={c for c in components if len(c)==16}
        assert component_orbit==small_components and len(component_orbit)==6
        print('shrikhande six sixteen-state components are all 4x4 rook graphs (explicit map)')
    return valid

if __name__=='__main__':
    obstruction('rook');obstruction('shrikhande')
