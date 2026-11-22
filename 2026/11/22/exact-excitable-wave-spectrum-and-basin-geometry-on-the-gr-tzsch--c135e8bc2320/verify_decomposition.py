#!/usr/bin/env python3
"""Exact finite-state census, independently rerunnable with Python standard library."""
import json
from collections import Counter,deque
from pathlib import Path

N=11
Q=3**N
P=[3**i for i in range(N+1)]
EDGES=[]
for i in range(5):
    EDGES.append((i,(i+1)%5))
    EDGES.append((i,5+(i+1)%5))
    EDGES.append((i,5+(i-1)%5))
    EDGES.append((5+i,10))
assert len(EDGES)==20 and len({tuple(sorted(e)) for e in EDGES})==20
adj=[set() for _ in range(N)]
for a,b in EDGES:
    adj[a].add(b);adj[b].add(a)
assert list(map(len,adj))==[4]*5+[3]*5+[5]

def update(s):
    col=[(s//P[i])%3 for i in range(N)]
    excited={j for j in range(N) if col[j]==1}
    ans=0
    for i in range(N):
        v=col[i]
        w=(v+1)%3 if v else int(not excited.isdisjoint(adj[i]))
        ans+=P[i]*w
    return ans

def census():
    F=[update(x) for x in range(Q)]
    indegree=[0]*Q
    for z in F:indegree[z]+=1
    pending=deque(i for i,z in enumerate(indegree) if z==0)
    peel=[]
    while pending:
        s=pending.popleft();peel.append(s)
        t=F[s];indegree[t]-=1
        if indegree[t]==0:pending.append(t)
    entry=[-1]*Q; cid=[-1]*Q; cycles=[]
    for s in range(Q):
        if indegree[s]>0 and cid[s]<0:
            t=s;cy=[];label=len(cycles)
            while cid[t]<0:
                cid[t]=label;entry[t]=0;cy.append(t);t=F[t]
            assert t==s
            cycles.append(cy)
    for s in reversed(peel):
        target=F[s];cid[s]=cid[target];entry[s]=entry[target]+1
    assert all(z>=0 for z in cid) and all(z>=0 for z in entry)
    periods=[len(c) for c in cycles]
    basins=Counter(cid)
    rows=Counter((entry[s],periods[cid[s]]) for s in range(Q))
    period_orbits=Counter(periods)
    depths=Counter(entry)
    basin_hist=Counter((periods[i],basins[i]) for i in range(len(cycles)))
    mx=max(entry); witness=next(s for s,d in enumerate(entry) if d==mx)
    wseq=[witness]
    for _ in range(mx+10):wseq.append(F[wseq[-1]])
    result={
        'graph':'Mycielski(C5) or Grotzsch graph',
        'graph_vertices':N,'graph_edges':len(EDGES),
        'total_states':Q,
        'period_orbit_counts':{str(k):v for k,v in sorted(period_orbits.items())},
        'periodic_state_count':sum(len(c) for c in cycles),
        'first_entry_counts':{str(k):v for k,v in sorted(depths.items())},
        'first_entry_by_period':{str(t):{str(p):rows.get((t,p),0) for p in sorted(period_orbits)} for t in range(mx+1)},
        'basin_size_histogram_by_period': {str(p):{str(b):v for (pp,b),v in sorted(basin_hist.items()) if pp==p} for p in sorted(period_orbits)},
        'max_first_entry':mx,
        'max_entry_count':depths[mx],
        'max_entry_witness_decimal':witness,
        'max_entry_witness_initial_colors':[witness//P[i]%3 for i in range(N)],
        'max_entry_witness_path_decimal':wseq[:mx+5],
        'zero_fixed_point_basin':basins[cid[0]],
        'first_entry_max_periods':{str(p):rows.get((mx,p),0) for p in sorted(period_orbits)},
        'all_cycle_basins_sum':sum(basins.values()),
    }
    assert result['period_orbit_counts']=={'1':1,'3':700,'4':190,'7':330,'10':70}
    assert result['max_first_entry']==9 and result['max_entry_count']==120
    assert result['zero_fixed_point_basin']==13887
    assert sum(period_orbits[p]*p for p in period_orbits)==result['periodic_state_count']
    assert sum(rows.values())==Q
    assert sum(v*b for (p,b),v in basin_hist.items())==Q
    target=Path(__file__).with_name('COUNTS.json')
    if target.exists():
        assert json.loads(target.read_text(encoding='utf-8'))==result, 'COUNTS.json mismatch'
    print('PASS decomposition',Q,'cycles',len(cycles),'maxentry',mx,'witness',witness,'basin zero',result['zero_fixed_point_basin'])
    return result

if __name__=='__main__':
    print(json.dumps(census(),ensure_ascii=False,indent=2,sort_keys=True))
