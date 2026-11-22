#!/usr/bin/env python3
"""Exact integer certificate for majority dynamics on the three (9_3) incidence graphs.
Requires only the Python 3 standard library. All vertex/line labels are zero based.
"""
from collections import Counter
from itertools import combinations, permutations, product

REPS = [
 [(0,1,2),(0,3,4),(0,5,6),(1,3,7),(1,6,8),(2,4,6),(2,7,8),(3,5,8),(4,5,7)],
 [(0,1,2),(0,3,4),(0,5,6),(1,4,8),(1,6,7),(2,3,7),(2,6,8),(3,5,8),(4,5,7)],
 [(0,1,2),(0,3,4),(0,5,6),(1,3,8),(1,5,7),(2,4,7),(2,6,8),(3,6,7),(4,5,8)],
]
EXPECTED = [
 (98,4,{1:18,2:18,3:36,4:24,127:2}),
 (96,4,{1:16,2:30,3:12,4:36,128:2}),
 (92,3,{2:54,4:36,130:2})
]

def pairs_in(blocks):
    return {tuple(sorted(ab)) for b in blocks for ab in combinations(b,2)}

def verify_configuration(blocks):
    assert len(blocks)==9 and len(set(blocks))==9
    assert all(len(set(b))==3 and all(0<=v<9 for v in b) for b in blocks)
    assert all(sum(v in b for b in blocks)==3 for v in range(9))
    assert len(pairs_in(blocks))==27

def components_as_cycles(blocks):
    paired=pairs_in(blocks)
    nei={v: set() for v in range(9)}
    for a,b in combinations(range(9),2):
        if (a,b) not in paired:nei[a].add(b);nei[b].add(a)
    assert all(len(nei[v])==2 for v in range(9))
    used=set();out=[]
    for start in range(9):
        if start in used:continue
        cycle=[start];prev=-1;curr=start
        while True:
            nxt=min(nei[curr] - ({prev} if prev>=0 else set()))
            if nxt==start:break
            assert nxt not in used and nxt not in cycle
            cycle.append(nxt);prev,curr=curr,nxt
        used.update(cycle);out.append(tuple(cycle))
    return sorted(out,key=lambda a:(len(a),a))

def iso_by_cycle_type(a,b):
    sa=components_as_cycles(a);sb=components_as_cycles(b)
    if sorted(map(len,sa))!=sorted(map(len,sb)):return False
    target={tuple(sorted(t)) for t in b}
    # Every incidence-isomorphism must preserve the complement collinearity cycles.
    for ordering in permutations(range(len(sb))):
        if any(len(sa[i])!=len(sb[ordering[i]]) for i in range(len(sa))):continue
        opts=[[(shift,sgn) for shift in range(len(sa[i])) for sgn in (1,-1)] for i in range(len(sa))]
        for orient in product(*opts):
            perm={}
            for i,s in enumerate(sa):
                t=sb[ordering[i]];offset,sgn=orient[i]
                perm.update({v:t[(offset+sgn*k)%len(t)] for k,v in enumerate(s)})
            if {tuple(sorted(perm[x] for x in triple)) for triple in a}==target:return True
    return False

def normalized_all():
    fixed=((0,1,2),(0,3,4),(0,5,6))
    existing=pairs_in(fixed)
    valid=[(b,set(combinations(b,2))) for b in combinations(range(1,9),3)
           if not (set(combinations(b,2)) & existing)]
    seen=set()
    def dfs(chosen,rem,paired):
        if sum(rem)==0:
            assert len(chosen)==6
            seen.add(tuple(chosen));return
        if len(chosen)==6:return
        for triple,ps in valid:
            if chosen and triple<=chosen[-1]:continue
            if any(rem[v]==0 for v in triple) or ps & paired:continue
            rem2=list(rem)
            for v in triple:rem2[v]-=1
            dfs(chosen+(triple,),rem2,paired|ps)
    dfs((),(0,2,2,2,2,2,2,3,3),existing)
    return [list(fixed)+list(rem) for rem in sorted(seen)]

def make_maps(blocks):
    p_to_l=[sum(1<<v for v in b) for b in blocks]
    l_to_p=[sum(1<<j for j,b in enumerate(blocks) if i in b) for i in range(9)]
    assert all(x.bit_count()==3 for x in p_to_l+l_to_p)
    def table(masks):
        return [sum(1<<i for i,nb in enumerate(masks) if (v&nb).bit_count()>=2) for v in range(512)]
    return table(p_to_l),table(l_to_p) # A: point bits -> line bits; B: reverse

def phase_data(blocks):
    A,B=make_maps(blocks)
    H=[B[A[x]] for x in range(512)]
    K=[A[B[y]] for y in range(512)]
    H2=[H[H[x]] for x in range(512)];K2=[K[K[y]] for y in range(512)]
    H3=[H[H2[x]] for x in range(512)];K3=[K[K2[y]] for y in range(512)]
    assert H3==H2 and K3==K2 # F^6 = F^4 on all 512*512 states
    X=set(H2);Y=set(K2)
    assert len(X)==len(Y)
    assert {A[x] for x in X}==Y and all(B[A[x]]==x for x in X)
    alpha=Counter(H2);beta=Counter(K2)
    assert all(alpha[x]==beta[A[x]] for x in X)
    hist=Counter(alpha.values())
    r=3 if all(B[K2[y]]==B[K[y]] for y in range(512)) and all(A[H2[x]]==A[H[x]] for x in range(512)) else 4
    def F(x,y):return B[y],A[x]
    witness=None
    for x in range(512):
        for y in (0,1,2,3):
            z=[(x,y)]
            for k in range(r+2):z.append(F(*z[-1]))
            if z[r+1]!=z[r-1]:witness=(x,y,z[r-1],z[r+1]);break
        if witness is not None:break
    assert witness is not None
    return len(X),r,dict(sorted(hist.items())),witness,alpha,A

def main():
    for b in REPS:verify_configuration(b)
    all_b=normalized_all()
    assert len(all_b)==176
    pattern_counts=Counter(tuple(sorted(map(len,components_as_cycles(b)))) for b in all_b)
    assert pattern_counts=={(9,):96,(3,6):72,(3,3,3):8},pattern_counts
    reps_by_type={tuple(sorted(map(len,components_as_cycles(b)))):b for b in REPS}
    assert len(reps_by_type)==3
    for b in all_b:
        typ=tuple(sorted(map(len,components_as_cycles(b))))
        assert iso_by_cycle_type(b,reps_by_type[typ])
    print('CONFIGURATIONS 176 normalized completions; all isomorphic to three representatives.')
    print('NONCOLLINEARITY COUNTS',dict(pattern_counts))
    for i,blocks in enumerate(REPS):
        S,depth,hist,witness,alpha,A=phase_data(blocks)
        assert (S,depth,hist)==EXPECTED[i],(i,S,depth,hist)
        assert sum(c*t for t,c in hist.items())==512
        attractors=Counter()
        for s in alpha:
            attractors[(1,alpha[s]**2)]+=1
        for x,y in combinations(sorted(alpha),2):
            attractors[(2,2*alpha[x]*alpha[y])]+=1
        assert sum(v *size for (p,size),v in attractors.items())==512**2
        assert sum(v for (p,size),v in attractors.items() if p==1)==S
        assert sum(v for (p,size),v in attractors.items() if p==2)==S*(S-1)//2
        print('CLASS',i,'missing_point_cycle_lengths',tuple(sorted(map(len,components_as_cycles(blocks)))))
        print('PHASE',S,'FIXED',S,'TWO_ORBITS',S*(S-1)//2,'SHARP_DEPTH',depth,'FIBERS',hist)
        print('DEPTH_WITNESS(x,y,F^(r-1),F^(r+1))',witness)
        print('BASIN_COUNTS',dict(sorted(attractors.items())))
    print('PASS')

if __name__=='__main__':main()
