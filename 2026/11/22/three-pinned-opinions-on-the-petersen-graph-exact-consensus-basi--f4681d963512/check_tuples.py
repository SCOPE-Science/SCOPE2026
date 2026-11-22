"""Independent direct-vector implementation, with a separate 5-point edge model.
Run: python3 check_tuples.py. No third-party dependencies.
"""
import itertools
from collections import Counter,defaultdict
import json

EDGES=tuple(itertools.combinations('abcde',2))
NEIGHBORS={e:tuple(f for f in EDGES if e!=f and set(e).isdisjoint(f)) for e in EDGES}

def signature(seeds):
    count=Counter(p for e in seeds for p in e)
    m=tuple(sorted(count.values(),reverse=True))
    return {(3,1,1,1):'star',(2,2,2):'triangle',(2,2,1,1):'path',(2,1,1,1,1):'wedge_disjoint'}[m]

def evolve(bits,seedset):
    state=dict(zip(EDGES,bits))
    out={e:(1 if e in seedset else int(sum(state[f] for f in NEIGHBORS[e])>=2)) for e in EDGES}
    return tuple(out[e] for e in EDGES)

def classify(bits,seedset):
    seq=[]
    while bits not in seq:
        seq.append(bits)
        bits=evolve(bits,seedset)
    t=seq.index(bits);period=len(seq)-t
    return t,period,bits==tuple([1]*10)

EXPECTED={'star':(20,128,0,0,3),'triangle':(10,98,28,2,2),
          'path':(60,124,0,4,5),'wedge_disjoint':(30,94,30,4,4)}

def main():
    profiles=defaultdict(set)
    totals=Counter()
    for seeds in itertools.combinations(EDGES,3):
        typ=signature(seeds)
        rest=[e for e in EDGES if e not in seeds]
        result=Counter()
        profile=Counter()
        for values in itertools.product((0,1), repeat=7):
            active=set(seeds)|{e for e,b in zip(rest,values) if b}
            init=tuple(int(e in active) for e in EDGES)
            t,p,cons=classify(init,set(seeds))
            result['consensus' if cons else ('oscillation' if p==2 else 'other_fixed')]+=1
            profile[(t,p)]+=1
        profiles[typ].add((result['consensus'],result['oscillation'],result['other_fixed'],max(t for t,p in profile)))
        totals[typ]+=1
    for typ,num in EXPECTED.items():
        assert totals[typ]==num[0]
        assert profiles[typ]=={num[1:]},(typ,profiles[typ])
    # Independently derive universal forcing via monotonicity and worst-case all-negative free sites.
    forced={}
    for seeds in itertools.combinations(EDGES,3):
        init=tuple(int(e in seeds) for e in EDGES)
        t,p,cons=classify(init,set(seeds))
        forced[seeds]=cons
    assert sum(forced.values())==20
    assert {signature(s) for s,v in forced.items() if v}=={'star'}
    for seeds in itertools.combinations(EDGES,2):
        assert any(not forced[s] for s in itertools.combinations(EDGES,3) if set(seeds).issubset(s))
    print(json.dumps({'triple_class_counts':dict(totals),'distinct_profiles':{k:[list(x) for x in v] for k,v in profiles.items()},
                      'force_all_count':sum(forced.values()),'total_trajectories':120*128,'all_assertions':'passed'},sort_keys=True,indent=2))

if __name__=='__main__':main()
