#!/usr/bin/env python3
"""Self-contained exact verifier for the open-neighborhood complex of Shrikhande's graph.
All integer operations and face choices are deterministic. Python 3 standard library only.
"""
from collections import Counter
from itertools import combinations

V = range(16)
STEPS = {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}

def graph_masks():
    N=[]
    for i in V:
        a,b=divmod(i,4)
        ns={4*((a+da)%4)+(b+db)%4 for da,db in STEPS}
        assert len(ns)==6 and i not in ns
        N.append(sum(1<<j for j in ns))
    # Independent pair-difference construction.
    for i in V:
        a,b=divmod(i,4)
        for j in V:
            c,d=divmod(j,4)
            assert bool(N[i] & (1<<j)) == (((c-a)%4,(d-b)%4) in STEPS)
            assert bool(N[i] & (1<<j)) == bool(N[j] & (1<<i))
    assert sum(x.bit_count() for x in N)==96
    assert all((N[i]&N[j]).bit_count()==2 for i in V for j in range(i))
    return N

def faces_from_facets(N):
    fs={0}
    for mask in N:
        vv=[i for i in V if mask>>i&1]
        for k in range(1,7):
            for comb in combinations(vv,k):
                fs.add(sum(1<<i for i in comb))
    return fs

def faces_direct(N):
    fs=set()
    for mask in range(1<<16):
        if mask==0 or any((mask & ~neigh)==0 for neigh in N):fs.add(mask)
    return fs

def collapse(fs,reverse=False):
    fs=set(fs); pairs=[]
    while True:
        incidence=Counter()
        for upper in fs:
            if not upper:continue
            for i in V:
                if upper>>i&1:
                    lower=upper^(1<<i)
                    if lower:incidence[lower]+=1
        choices=[]
        for lower,c in incidence.items():
            if c!=1:continue
            supers=[lower | (1<<i) for i in V
                    if not (lower>>i&1) and (lower|(1<<i)) in fs]
            assert len(supers)==1
            choices.append((lower,supers[0]))
        if not choices:break
        lower,upper=min(choices,key=lambda p:(-p[0].bit_count(),-p[0] if reverse else p[0]))
        assert upper.bit_count()==lower.bit_count()+1 and lower&upper==lower
        fs.remove(lower);fs.remove(upper);pairs.append((lower,upper))
    assert all(not ((x>>i)&1) or (x^(1<<i)) in fs for x in fs for i in V)
    return fs,pairs

def red(w,cyclic=True):
    st=[]
    for x in w:
        if st and st[-1]==-x:st.pop()
        else:st.append(x)
    if cyclic:
        while len(st)>1 and st[0]==-st[-1]:st=st[1:-1]
    return st

def inv(w):return [-x for x in w[::-1]]

def presentation_reduction(fs):
    # Contract the 15 edges {0,i} of the star tree in the complete 1-skeleton.
    edges={f for f in fs if f.bit_count()==2}
    assert len(edges)==120 and all(1+(1<<i) in edges for i in range(1,16))
    non_tree=sorted(f for f in edges if not (f&1))
    ix={e:j+1 for j,e in enumerate(non_tree)}
    def e(a,b):
        if a==0 or b==0:return []
        z=ix[(1<<a)|(1<<b)]
        return [z if a<b else -z]
    tris=sorted(f for f in fs if f.bit_count()==3)
    assert len(tris)==160
    rels=[]
    for t in tris:
        a,b,c=[i for i in V if t>>i&1]
        rels.append(red(e(a,b)+e(b,c)+e(c,a)))
    assert len(rels)==160
    eliminated=set(); steps=[]
    for iteration in range(105):
        occurrences=Counter(abs(x) for w in rels for x in w)
        options=[]
        for ri,w in enumerate(rels):
            within=Counter(abs(x) for x in w)
            for j,x in enumerate(w):
                if within[abs(x)]==1:
                    options.append((len(w)-1,occurrences[abs(x)],ri,j))
        if not options:break
        _,_,ri,j=min(options)
        w=rels[ri]; x=w[j]
        # A*x*B=1 implies x=(B*A)^-1. A*x^-1*B=1 implies x=B*A.
        body=red(w[j+1:]+w[:j],False)
        sub=inv(body) if x>0 else body
        assert abs(x) not in eliminated
        new=[]
        for k,old in enumerate(rels):
            if k==ri:continue
            z=[]
            for letter in old:
                z.extend((sub if letter>0 else inv(sub)) if abs(letter)==abs(x) else [letter])
            new.append(red(z))
        rels=new; eliminated.add(abs(x));steps.append((abs(x),len(w),len(sub)))
    remaining=set(ix.values())-eliminated
    assert len(eliminated)==104 and len(remaining)==1 and len(rels)==56
    g=next(iter(remaining))
    hist=Counter(len(w) for w in rels)
    assert all((not w) or w in ([g,g],[-g,-g]) for w in rels)
    assert hist[0]+hist[2]==56 and hist[2]>=1
    return len(steps),g,hist

def mod_rank_2faces(fs,p):
    es=sorted(x for x in fs if x.bit_count()==2)
    ts=sorted(x for x in fs if x.bit_count()==3)
    positions={e:i for i,e in enumerate(es)}
    pivots={}
    for t in ts:
        v=[j for j in V if t>>j&1]
        vec={positions[t^(1<<v[k])]: (1 if k%2==0 else p-1) for k in range(3)}
        while vec:
            i=max(vec)
            if i not in pivots:
                pivots[i]=vec;break
            q=vec[i]*pow(pivots[i][i],-1,p)%p
            for k,z in pivots[i].items():
                x=(vec.get(k,0)-q*z)%p
                if x:vec[k]=x
                elif k in vec:del vec[k]
    return len(pivots)

def main():
    N=graph_masks()
    F=faces_from_facets(N)
    assert F==faces_direct(N)
    f=Counter(m.bit_count()-1 for m in F)
    assert [f[i] for i in range(6)] == [16,120,320,240,96,16]
    assert len(F)==809 and len([x for x in F if x==0])==1
    cycles=set()
    for i in V:
        for j in range(i):
            common=[k for k in V if (N[i]&N[j])>>k&1]
            assert len(common)==2
            a,b=common
            cycle=frozenset(tuple(sorted(e)) for e in ((i,a),(a,j),(j,b),(b,i)))
            assert len(cycle)==4
            cycles.add(cycle)
    edge_incidence=Counter(edge for c in cycles for edge in c)
    assert len(cycles)==60 and len(edge_incidence)==48 and set(edge_incidence.values())=={5}
    print('GRAPH 16 vertices 48 edges, each pair has exactly two common neighbors')
    print('FACES 809 including empty; f=(16,120,320,240,96,16)')
    print('FOUR_CYCLES 60; every graph edge belongs to five cycles')
    for rev in [False,True]:
        R,pairs=collapse(F,reverse=rev)
        r=Counter(m.bit_count()-1 for m in R)
        assert len(pairs)==256 and len(R)==297
        assert (r[0],r[1],r[2])==(16,120,160) and max(r)==2
        steps,g,hist=presentation_reduction(R)
        ranks={p:mod_rank_2faces(R,p) for p in (2,3,5)}
        assert ranks=={2:104,3:105,5:105}
        print(('REVERSE' if rev else 'FORWARD')+' 256 elementary collapses; remaining f=(16,120,160)')
        print('CELLULAR 104 unit-generator eliminations; one circle generator')
        print(f'RELATORS {hist[0]} constant; {hist[2]} of degree +/-2; remaining generator {g}')
        print('CHECK mod 2/3/5 ranks d2=(104,105,105)')
    print('SHRIKHANDE_NEIGHBORHOOD_RP2_WEDGE55_S2_VERIFIED')
if __name__=='__main__':main()
