"""Independent finite test of component rank composition, using simple graph components.
No dependency beyond Python's standard library; run python check_component_rank.py.
"""
from functools import lru_cache
from itertools import product


def graphs(n):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    for k in range(1<<len(pairs)):
        rows=[0]*n
        for t,(i,j) in enumerate(pairs):
            if k>>t&1:
                rows[i]|=1<<j
                rows[j]|=1<<i
        yield tuple(rows)


def local_rank(g,marked,threshold):
    if not threshold:return True
    n=len(g)
    present=[i for i in range(n) if marked>>i&1]
    for neighbor_choice in range(1<<len(present)):
        goal=sum((1<<x) for i,x in enumerate(present) if neighbor_choice>>i&1)
        witnesses=[j for j in range(n) if not(marked>>j&1) and (g[j]&marked)==goal]
        if not any(local_rank(g,marked|1<<j,threshold-1) for j in witnesses):return False
    return True


def game(gs,fs,threshold):
    if threshold==0:return True
    # Challenge: a new component (singleton local type).
    if not any(game(gs,tuple(fs[i]|1<<j if k==i else fs[k] for k in range(len(gs))),threshold-1)
               for i,g in enumerate(gs) if fs[i]==0 for j in range(len(g))):return False
    # Challenge: extend any existing marked component with every graph local type.
    for i,g in enumerate(gs):
        if not fs[i]:continue
        f=fs[i];pts=[j for j in range(len(g)) if f>>j&1]
        for bits in range(1<<len(pts)):
            goal=sum(1<<p for j,p in enumerate(pts) if bits>>j&1)
            if not any(game(gs,tuple(fs[k]|(1<<j) if k==i else fs[k] for k in range(len(gs))),threshold-1)
                       for j in range(len(g)) if not(f>>j&1) and g[j]&f==goal):return False
    return True


def predicted(gs,fs,threshold):
    if threshold==0:return True
    occupied=[i for i,f in enumerate(fs) if f]
    if any(not local_rank(gs[i],fs[i],threshold) for i in occupied):return False
    unused=sorted((max((r for r in range(len(gs[i])+1) if local_rank(gs[i],0,r)),default=0)
                   for i in range(len(gs)) if not fs[i]),reverse=True)
    return len(unused)>=threshold and all(unused[j]>=threshold-j for j in range(threshold))


def main():
    tested=0
    for sizes in ((1,),(2,),(3,),(1,1),(1,2),(2,2),(1,3),(2,3),(1,1,1),(1,1,2)):
        for gs in product(*(tuple(graphs(n)) for n in sizes)):
            for fs in product(*(range(1<<n) for n in sizes)):
                for r in range(min(4,sum(sizes)+1)):
                    a=game(gs,fs,r);b=predicted(gs,fs,r)
                    if a!=b:raise AssertionError((sizes,gs,fs,r,a,b))
                tested+=1
    print('GENERAL_COMPONENT_CHECK_OK',tested,'marked graph-component positions')


if __name__=='__main__':main()
