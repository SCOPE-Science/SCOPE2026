"""Exact finite-state census for pinned synchronous majority on KG(5,2).
Run: python3 check_bitmask.py. No third-party dependencies.
"""
from itertools import combinations
from collections import Counter,defaultdict
import json

VERTICES=tuple(combinations(range(5),2))
MASKS=tuple(sum(1<<j for j,b in enumerate(VERTICES) if not (set(a)&set(b))) for a in VERTICES)
ALL=(1<<10)-1

def advance(state,pins):
    ans=pins
    for i,nb in enumerate(MASKS):
        if not (pins>>i)&1 and (state&nb).bit_count()>=2:
            ans|=1<<i
    return ans

def kind(indices):
    degrees=Counter(j for i in indices for j in VERTICES[i])
    signature=tuple(sorted(degrees.values(),reverse=True))
    labels={(3,1,1,1):'star', (2,2,2):'triangle',
            (2,2,1,1):'path', (2,1,1,1,1):'wedge_disjoint'}
    return labels[signature]

def classify(state,pins):
    seen={}; path=[]
    while state not in seen:
        seen[state]=len(path)
        path.append(state)
        state=advance(state,pins)
    return seen[state], len(path)-seen[state], state

def census(indices):
    pins=sum(1<<i for i in indices)
    others=[i for i in range(10) if i not in indices]
    counts=Counter(); outcomes=Counter()
    for b in range(1<<len(others)):
        state=pins|sum(((b>>j)&1)<<i for j,i in enumerate(others))
        depth,period,cyc=classify(state,pins)
        counts[(depth,period)]+=1
        outcomes['consensus' if cyc==ALL else ('oscillation' if period==2 else 'other_fixed')]+=1
    return dict(counts),dict(outcomes)

EXPECTED={
 'star':(20,128,0,0,3),
 'triangle':(10,98,28,2,2),
 'path':(60,124,0,4,5),
 'wedge_disjoint':(30,94,30,4,4)
}

def main():
    groups=defaultdict(list)
    for pins in combinations(range(10),3):
        k=kind(pins)
        profile,outcomes=census(pins)
        vals=(outcomes.get('consensus',0),outcomes.get('oscillation',0),outcomes.get('other_fixed',0),max(t for t,p in profile))
        groups[k].append((pins,vals,profile))
    report={}
    for k,rows in sorted(groups.items()):
        assert len({r[1] for r in rows})==1,(k,rows)
        cons,osc,other,cutoff=rows[0][1]
        assert (len(rows),cons,osc,other,cutoff)==EXPECTED[k]
        report[k]={'number_of_pin_sets':len(rows),'consensus':cons,'oscillatory':osc,'other_fixed':other,'max_entry':cutoff,
                   'entry_period_profile':{f'{t},{p}':v for (t,p),v in sorted(rows[0][2].items())}}
    assert sum(v['number_of_pin_sets'] for v in report.values())==120
    # Distinct size-two pin layouts, for the sharp three-pin minimum.
    pair_report={}
    for pins in combinations(range(10),2):
        c,p=census(pins)
        label='adjacent' if (MASKS[pins[0]]>>pins[1])&1 else 'nonadjacent'
        row=(p.get('consensus',0),p.get('oscillation',0),p.get('other_fixed',0),max(t for t,per in c))
        pair_report.setdefault(label,[]).append(row)
    assert len(pair_report['adjacent'])==15 and set(pair_report['adjacent'])=={(141,104,11,4)}
    assert len(pair_report['nonadjacent'])==30 and set(pair_report['nonadjacent'])=={(188,60,8,5)}
    assert all(census((i,))[1]['consensus']==212 for i in range(10))
    assert census(tuple())[1]['consensus']==226
    print(json.dumps({'triple_classes':report,'two_pin_types':{key:{'number_of_pin_sets':len(v),'census':v[0]} for key,v in sorted(pair_report.items())},
                      'total_pinned_triple_initial_states':120*128,'all_assertions':'passed'},sort_keys=True,indent=2))

if __name__=='__main__':main()
