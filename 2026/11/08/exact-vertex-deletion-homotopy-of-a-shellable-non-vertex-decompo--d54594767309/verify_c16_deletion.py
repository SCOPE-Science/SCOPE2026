#!/usr/bin/env python3
"""Exact finite verification for the local independence-complex homotopy of C16(1,4,8).
Python 3 standard library only. All matrices are signed integer except explicit GF(2) checks.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache

N = 16
STEPS = (1,4,8)


def graph():
    adj = [0]*N
    edges = set()
    for u in range(N):
        for s in STEPS:
            v = (u+s)%N
            a,b = sorted((u,v))
            edges.add((a,b))
    for a,b in edges:
        adj[a] |= 1<<b
        adj[b] |= 1<<a
    assert len(edges) == 40 and all(z.bit_count() == 5 for z in adj)
    return adj,edges


def independent(S,adj):
    return all(not (S>>u&1) or not (S&adj[u]) for u in range(N))


def all_faces(adj):
    exhaustive = {s for s in range(1<<N) if independent(s,adj)}
    inductive={0}
    for v in range(N):
        inductive |= {s|(1<<v) for s in tuple(inductive) if (s & adj[v]) == 0}
    assert exhaustive == inductive
    return exhaustive


def facecounts(F):
    return tuple(Counter(s.bit_count()-1 for s in F).get(d,0) for d in range(-1,4))


def reduce_matching(F):
    # Simultaneous toggles at selected pivot; all choices determined by sorted maxima.
    remaining=set(F);lower_to_upper={};stages=[]
    while True:
        counts=[(sum(1 for s in remaining if not (s>>v&1) and (s|1<<v) in remaining),v)
                for v in range(N)]
        m,v=max(counts)
        if m == 0:break
        candidates=[s for s in remaining if not (s>>v&1) and (s|1<<v) in remaining]
        assert len(candidates)==m
        for low in candidates:
            high=low|(1<<v)
            remaining.remove(low);remaining.remove(high)
            lower_to_upper[low]=high
        stages.append((v,m))
    assert len(F) == 2*len(lower_to_upper)+len(remaining)
    # Since the empty face was matched, removing its matching edge makes one
    # formerly paired singleton a critical 0-cell, for ordinary CW theory.
    root=lower_to_upper.get(0)
    assert root is not None and root.bit_count()==1
    assert 0 not in remaining
    critical=set(remaining)|{root}
    lower_to_upper.pop(0)
    # All nonempty matched covering relations reversed, all others downward.
    indeg=defaultdict(int); arrows=defaultdict(list);incidences=0
    for s in F:
        if s==0:continue
        for v in range(N):
            if s>>v&1:
                t=s^(1<<v)
                if t==0:continue
                a,b=(t,s) if lower_to_upper.get(t)==s else (s,t)
                arrows[a].append(b);indeg[b]+=1;incidences+=1
    q=deque(s for s in F if s!=0 and indeg[s]==0)
    seen=0
    while q:
        s=q.popleft();seen+=1
        for t in arrows[s]:
            indeg[t]-=1
            if indeg[t]==0:q.append(t)
    assert seen == len(F)-1, 'directed Hasse cycle'
    assert (len(F)-1) == 2*len(lower_to_upper)+len(critical)
    return critical,lower_to_upper,stages,incidences


def boundary_faces(s):
    bits=[v for v in range(N) if s>>v&1]
    return [(s^(1<<v),(-1 if i%2 else 1)) for i,v in enumerate(bits)]


def signed_morse_matrix(critical,pairing,degree):
    # Integral elementary cancellation of matched face/one-higher-face pairs.
    upper_to_lower={u:l for l,u in pairing.items()}
    @lru_cache(None)
    def projection(cell):
        if cell in critical:return {cell:1}
        if cell in upper_to_lower:return {}
        if cell not in pairing:raise ValueError(('unclassified',cell))
        top=pairing[cell]
        coeff=dict(boundary_faces(top))[cell]
        assert abs(coeff)==1
        out=defaultdict(int)
        for other,a in boundary_faces(top):
            if other==cell:continue
            for c,b in projection(other).items():out[c]-=coeff*a*b
        return {c:b for c,b in out.items() if b}
    sources=sorted(s for s in critical if s.bit_count()==degree+1)
    targets=sorted(s for s in critical if s.bit_count()==degree)
    matrix=[]
    for target in targets:
        matrix.append([sum(sign*projection(t).get(target,0)
                        for t,sign in boundary_faces(source)) for source in sources])
    return targets,sources,matrix


def rank2(columns):
    pivots={}
    for col in columns:
        x=col
        while x:
            i=x.bit_length()-1
            if i in pivots:x^=pivots[i]
            else:pivots[i]=x;break
    return len(pivots)


def mod2_bettis(F):
    bydim={d:sorted(s for s in F if s.bit_count()-1==d) for d in range(4)}
    ranks={}
    for d in (1,2,3):
        rows={s:i for i,s in enumerate(bydim[d-1])}
        cols=[]
        for s in bydim[d]:
            col=0
            for t,_ in boundary_faces(s):col^=1<<rows[t]
            cols.append(col)
        ranks[d]=rank2(cols)
    betti={0:len(bydim[0])-ranks[1]-1}
    for d in (1,2):betti[d]=len(bydim[d])-ranks[d]-ranks[d+1]
    betti[3]=len(bydim[3])-ranks[3]
    return ranks,betti


def main():
    adj,edges=graph()
    allF=all_faces(adj)
    assert facecounts(allF)==(1,16,80,144,80)
    deletion={s for s in allF if not s&1}
    link={s^1 for s in allF if s&1}
    # Independently, the graph formula for the link uses closed neighborhoods.
    assert link=={s for s in allF if not(s&(adj[0]|1))}
    expected={
        'deletion':((1,15,70,117,60),{0:1,2:2,3:1},(2,3,[[-1],[0]]),{0:0,1:0,2:1,3:0}),
        'link':((1,10,27,20,0),{0:1,1:1,2:3},(1,2,[[1,0,1]]),{0:0,1:0,2:2,3:0})
    }
    for name,F in [('deletion',deletion),('link',link)]:
        fvec,crit_expected,degree_data,betti_expected=expected[name]
        critical,pairs,stages,inc=reduce_matching(F)
        counts=dict(Counter(s.bit_count()-1 for s in critical))
        assert facecounts(F)==fvec
        assert counts==crit_expected
        target_deg,source_deg,wanted=degree_data
        targets,sources,M=signed_morse_matrix(critical,pairs,source_deg)
        assert target_deg+1==source_deg and M==wanted
        ranks,betti=mod2_bettis(F)
        assert betti==betti_expected
        # Exact signed matrices have a ±1 pivot, hence no integral torsion.
        assert any(abs(v)==1 for row in M for v in row)
        print(name, 'f_vector',fvec,'matching_pairs',len(pairs),
              'critical_dimensions',dict(sorted(counts.items())),
              'Hasse_incidences',inc,'Morse_matrix',M,
              'GF2_boundary_ranks',ranks,'GF2_reduced_Betti',betti,
              'pivot_stages',stages)
    # rotations give simplicial isomorphisms and transitive vertex action
    for shift in range(N):
        def rotate(s):
            return sum(1<<((i+shift)%N) for i in range(N) if s>>i&1)
        assert {rotate(s) for s in deletion}=={s for s in allF if not(s>>shift&1)}
    # Published shellability of the full 3-dimensional complex + chi=-1 -> S^3.
    chi=sum((-1)**(i-1)*f for i,f in enumerate(facecounts(allF)))
    assert chi == -1
    print('full_complex_face_vector',facecounts(allF),'reduced_Euler',chi)
    print('ROTATION_SYMMETRY_PASS')
    print('ALL_CHECKS_PASS')

if __name__=='__main__':main()
