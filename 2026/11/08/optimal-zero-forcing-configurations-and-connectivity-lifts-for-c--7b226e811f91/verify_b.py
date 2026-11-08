"""Set-based independent graph enumeration for structural zero-forcing corona theorem."""
from itertools import combinations
from math import comb
from collections import defaultdict

def is_forcing(links, initial):
    active=set(initial)
    while True:
        new=set()
        for a in list(active):
            unseen=links[a]-active
            if len(unseen)==1:new.update(unseen)
        if not (new-active):return len(active)==len(links)
        active.update(new)

def all_min(links):
    verts=tuple(links)
    for k in range(len(verts)+1):
        good={frozenset(t) for t in combinations(verts,k) if is_forcing(links,t)}
        if good:return good

def graph(n,edges,r):
    pairs=set(tuple(sorted(e)) for e in edges)
    verts=[('v',i) for i in range(n)]
    if r:
        verts +=[('c',i,j) for i in range(n) for j in range(r)]
    E=set()
    for u,v in combinations(verts,2):
        if u[0]=='v' and v[0]=='v' and tuple(sorted((u[1],v[1]))) in pairs:E.add((u,v))
        elif r and u[0]=='c' and v[0]=='c' and u[1]==v[1]:E.add((u,v))
        elif r and u[1]==v[1] and u[0]!=v[0]:E.add((u,v))
    links={a:set() for a in verts}
    for u,v in E:links[u].add(v);links[v].add(u)
    return links

def predicted(base,n,r):
    solutions=set()
    for B in base:
        bset={v[1] for v in B}
        for active_modes in __import__('itertools').product(*[(list(range(r))+['full'] if i in bset else list(range(r))) for i in range(n)]):
            state=set()
            for i,mode in enumerate(active_modes):
                if mode=='full':
                    state.update(('c',i,j) for j in range(r))
                else:
                    state.update(('c',i,j) for j in range(r) if j!=mode)
                    if i in bset:state.add(('v',i))
            solutions.add(frozenset(state))
    return solutions

def edges_reconfig(allstates):
    states=list(allstates)
    return {(i,j) for i in range(len(states)) for j in range(i) if len(states[i]^states[j])==2}

def connected(n,edges):
    reached={0}
    while 1:
        new=reached|{b for a,b in edges if a in reached}|{a for a,b in edges if b in reached}
        if new==reached:return len(reached)==n
        reached=new

def test(n,r):
    checked=0; basecount=0;coronacount=0
    possible=list(combinations(range(n),2))
    for k in range(len(possible)+1):
        for chosen in combinations(possible,k):
            if not connected(n,chosen):continue
            base=all_min(graph(n,chosen,0))
            cor=all_min(graph(n,chosen,r))
            pred=predicted(base,n,r)
            assert cor==pred,(n,chosen,r,len(cor),len(pred),cor^pred)
            checked+=1;basecount+=len(base);coronacount+=len(cor)
    print(f'all connected labelled graphs n={n}, r={r}: {checked} cases; {basecount} base minimum sets; {coronacount} corona minimum sets; exact-set equality PASS')

if __name__=='__main__':
    test(2,2)
    test(3,2)
    test(4,2)
    test(3,3)
    print('verify_b all checks passed')
