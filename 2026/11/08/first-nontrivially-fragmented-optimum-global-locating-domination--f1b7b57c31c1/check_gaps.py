#!/usr/bin/env python3
"""Independent rim-gap classification and local-move enumeration for wheels."""
from itertools import product
from collections import Counter


def gaps_ok(d):
    # For at least 3 chosen rim vertices on a rim of >= 6 vertices.
    p=len(d)
    return (all(1<=x<=4 for x in d) and d.count(4)<=1
        and all(not(d[i]>=3 and d[(i+1)%p]>=3) for i in range(p)))


def compositions(r,p):
    if p==1:
        if 1<=r<=4:yield (r,)
        return
    for j in range(1,min(r-p+1,4)+1):
        for rest in compositions(r-j,p-1):yield (j,)+rest


def states_of_length(r,p):
    states=set()
    for d in compositions(r,p):
        if not gaps_ok(d):continue
        start=0;chosen=[0]
        for gap in d[:-1]:
            start+=gap;chosen.append(start)
        assert start+d[-1]==r
        for shift in range(r):
            state=frozenset((v+shift)%r for v in chosen)
            assert len(state)==p
            states.add(state)
    return states


def exchange_graph(r,states):
    nbr={s:set() for s in states}
    for s in states:
        for u in s:
            for v in {(u-1)%r,(u+1)%r} - s:
                t=frozenset((s-{u})|{v})
                if t in states:nbr[s].add(t)
    assert all(s in nbr[t] for s in states for t in nbr[s])
    unseen=set(states);components=[]
    while unseen:
        x=unseen.pop();todo=[x];component={x}
        while todo:
            for y in nbr[todo.pop()]&unseen:
                unseen.remove(y);component.add(y);todo.append(y)
        components.append(component)
    return nbr, Counter(map(len,components))


def run():
    expected={7:(3,20,{20:1}),8:(3,21,{21:1}),9:(3,8,{1:8}),
              10:(4,54,{54:1}),11:(4,35,{35:1}),12:(4,11,{1:11}),
              13:(5,96,{96:1}),14:(5,26,{2:13})}
    for n in range(7,15):
        r=n-1
        for p in range(3,r):
            states=states_of_length(r,p)
            if states:break
        nbr,comps=exchange_graph(r,states)
        assert (p,len(states),dict(comps))==expected[n]
        if n==14:
            assert set(map(len,nbr.values()))=={1}
            rep=frozenset([0,2,4,7,9])
            assert rep in states
            def image(s,shift,refl):
                return frozenset(((sign*v+shift)%r) for v in s for sign in ([(-1 if refl else 1)]))
            assert {image(rep,t,refl) for t in range(r) for refl in [False,True]}==states
            # Exactly two rotational orbits, interchanged by the legal edge.
            orbit={image(rep,t,False) for t in range(r)}
            assert len(orbit)==13 and all(next(iter(nbr[s])) not in orbit for s in orbit)
            assert set(tuple(sorted(d)) for d in compositions(r,p) if gaps_ok(d))=={(2,2,2,3,4)}
        print(f'W_{n}: selected_rim={p}, states={len(states)}, components={dict(sorted(comps.items()))}')
    print('PASS: independent gap-word classification for W_7 through W_14')

if __name__=='__main__':run()
