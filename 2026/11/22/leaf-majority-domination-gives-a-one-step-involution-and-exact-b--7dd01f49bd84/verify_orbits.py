"""Independent tuple-state orbit tracing for leaf-supported majority networks.

Builds the graph with explicit named vertices, follows trajectories, and
counts each eventual orbit's full basin without using the closed formula.
"""
from itertools import product
from collections import Counter


def build(k, links, mantle):
    core = [('core',v) for v in range(k)]
    leaves = [('leaf',v,j) for v in range(k) for j in range(mantle[v])]
    names = core + leaves
    near = {v:[] for v in names}
    for u,v in links:
        near[core[u]].append(core[v]);near[core[v]].append(core[u])
    for v in range(k):
        for j in range(mantle[v]):
            w=('leaf',v,j)
            near[core[v]].append(w)
            near[w].append(core[v])
    return names,near


def update(state,names,near):
    current=dict(zip(names,state))
    nxt=[]
    for v in names:
        votes=[current[w] for w in near[v]]
        s=sum(votes)
        if s*2>len(votes): nxt.append(1)
        elif s*2<len(votes): nxt.append(0)
        else: nxt.append(current[v])
    return tuple(nxt)


def check(k, links, mantle):
    names,near=build(k,links,mantle)
    full=list(product((0,1),repeat=len(names)))
    periods=Counter()
    basins=Counter()
    first=Counter()
    for state in full:
        trajectory=[state]
        for _ in range(6):
            trajectory.append(update(trajectory[-1],names,near))
        entry=next(t for t in range(3) if trajectory[t]==trajectory[t+2])
        assert entry<=1
        first[entry]+=1
        a=trajectory[entry]
        b=trajectory[entry+1]
        orbit=tuple(sorted({a,b}))
        periods[orbit]=len(orbit)
        basins[orbit]+=1
    assert len(basins)==(4**k+2**k)//2
    assert sum(t==1 for t in periods.values())==2**k
    assert sum(t==2 for t in periods.values())==(4**k-2**k)//2
    assert first[0]==4**k
    assert first[1]==len(full)-4**k
    assert sum(basins.values())==len(full)
    return len(full),len(basins),max(basins.values())


def boundary():
    names,near=build(2,[(0,1)],[1,1])
    counterexample=None
    for state in product((0,1),repeat=len(names)):
        a=update(state,names,near)
        b=update(a,names,near)
        c=update(b,names,near)
        if c!=a:
            counterexample=(state,a,b,c)
            break
    assert counterexample is not None
    return counterexample


def main():
    cases=[
       (1,[],[1]),
       (2,[(0,1)],[2,2]),
       (3,[(0,1),(1,2)],[2,3,2]),
       (3,[(0,1),(1,2),(0,2)],[3,3,3]),
       (4,[(0,1),(0,2),(0,3)],[4,2,2,2]),
       (4,[(0,1),(1,2),(2,3)],[2,3,3,2]),
    ]
    total=0
    for k,links,mantle in cases:
        n,orbits,largest=check(k,links,mantle)
        total+=n
        print(f'case={k}/{len(links)} leaves={mantle}: states={n} orbits={orbits} largest_basin={largest}')
    witness=boundary()
    print('BOUNDARY_WITNESS',witness)
    print(f'ORBIT_VERIFY_OK cases={len(cases)} states={total}')


if __name__=='__main__':
    main()
