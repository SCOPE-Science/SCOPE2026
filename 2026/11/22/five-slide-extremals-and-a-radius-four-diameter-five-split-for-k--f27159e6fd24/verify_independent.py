"""Independent bitset/reachable-layers and direct propagation verifier.
Python 3 standard library. Does not import the first verifier."""
from itertools import combinations
from collections import Counter
import json

def build(n):
    labels=list(combinations(range(n),2))
    emask=[(1<<a)|(1<<b) for a,b in labels]
    neighbors=[0]*len(labels)
    for i,u in enumerate(emask):
        neighbors[i]=sum(1<<j for j,v in enumerate(emask) if not (u&v))
    return labels,emask,neighbors

def forcing_success(S,neighbors):
    full=(1<<len(neighbors))-1
    observed=0
    for i in S:observed |= (1<<i)|neighbors[i]
    while observed!=full:
        new=observed
        remaining=observed
        while remaining:
            bit=remaining&-remaining; remaining-=bit
            i=bit.bit_length()-1
            white=neighbors[i]&(~observed)
            if white and white&(white-1)==0:new|=white
        if new==observed:return False
        observed=new
    return True

def root_states(n,labels):
    bylabel={p:i for i,p in enumerate(labels)}
    patterns={"triangle":((0,1),(0,2),(1,2)),
              "path4":((0,1),(1,2),(2,3)),
              "path2_and_edge":((0,1),(1,2),(3,4)),
              "matching":((0,1),(2,3),(4,5))}
    return {name:sum(1<<bylabel[e] for e in Edges)
            for name,Edges in patterns.items()}

def iter_bits(num):
    while num:
        bit=num&-num; num-=bit
        yield bit.bit_length()-1

def deficient(S,T,emasks):
    if S&T: return False
    s=list(iter_bits(S));t=list(iter_bits(T))
    # A matching of size two in the bipartite source-to-target disjointness relation
    for a,b in combinations(s,2):
        for c,d in combinations(t,2):
            if (emasks[a]&emasks[c]==0 and emasks[b]&emasks[d]==0) or (emasks[a]&emasks[d]==0 and emasks[b]&emasks[c]==0):
                return False
    return True

def check(n,fullprop=False):
    labels,emasks,neighbors=build(n)
    allstates=set()
    for a,b,c in combinations(range(len(labels)),3):
        v=emasks[a]&emasks[b]&emasks[c]
        if v:continue # three-edge star is excluded
        allstates.add((1<<a)|(1<<b)|(1<<c))
    if fullprop:
        assert all(not forcing_success(S,neighbors) for S in ((),))
        for a in range(len(labels)):
            assert not forcing_success((a,),neighbors)
        for a,b in combinations(range(len(labels)),2):
            assert not forcing_success((a,b),neighbors)
        for a,b,c in combinations(range(len(labels)),3):
            present=(1<<a)|(1<<b)|(1<<c) in allstates
            assert forcing_success((a,b,c),neighbors)==present,(n,a,b,c)
    # Recompute the 4 root reachability layers without preconstructing a graph.
    disjoint_options=[tuple(iter_bits(neighbors[e])) for e in range(len(labels))]
    evidence={}
    for name,root in root_states(n,labels).items():
        assert root in allstates
        reached={root}; frontier={root}; hist=[1]
        for depth in range(1,6):
            next_frontier=set()
            for state in frontier:
                for old in iter_bits(state):
                    left=state^(1<<old)
                    for new in disjoint_options[old]:
                        bit=1<<new
                        if left&bit:continue
                        moved=left|bit
                        if moved in allstates and moved not in reached:
                            next_frontier.add(moved)
            next_frontier-=reached
            reached|=next_frontier;frontier=next_frontier
            hist.append(len(frontier))
        assert reached==allstates,(n,name,len(reached),len(allstates))
        if name=='triangle':assert hist[5]==0
        else: assert hist[5]>0
        # The unreached layer after four moves must be the graph-theoretic matching deficit.
        # The depth-five frontier is precisely the complement of the radius-four ball.
        outside4=frontier
        actual={T for T in allstates if deficient(root,T,emasks)}
        assert outside4==actual,(n,name,len(outside4),len(actual))
        evidence[name]={'layer_sizes':hist,'deficient_pairs':len(actual)}
    return {'n':n,'power_domination_verified':fullprop,'states':len(allstates),
            'root_checks':evidence,'status':'PASS'}

if __name__=='__main__':
    print(json.dumps({'independent_checks':[check(n,fullprop=(n in (8,9,10))) for n in (8,9,10,11,12)],'status':'PASS'},sort_keys=True,separators=(',',':')))
