"""Verification of the stated finite epistemic peeling formulas.
Run: python3 verify_ignorance.py [--extended]. Only Python standard library.
"""
from itertools import product
import sys

def partitions(n):
    def walk(a, bound):
        if len(a)==n:
            yield tuple(a)
            return
        for v in range(bound+2):
            yield from walk(a+[v], max(bound,v))
    yield from walk([0],0)

def announcement_sequence(left,right,bit):
    n=len(left); mask=(1<<n)-1; sequence=[mask]
    for _ in range(n+2):
        left_vals={};right_vals={}
        for e in range(n):
            if mask>>e&1:
                left_vals[left[e]]=left_vals.get(left[e],0)|(1<<bit[e])
                right_vals[right[e]]=right_vals.get(right[e],0)|(1<<bit[e])
        nxt=0
        for e in range(n):
            if mask>>e&1 and left_vals[left[e]]==3 and right_vals[right[e]]==3:
                nxt |= 1<<e
        if nxt==mask:
            return sequence
        mask=nxt;sequence.append(mask)
    raise AssertionError('no stabilization')

def walk_formula(left,right,bit):
    n=len(left)
    nr=max(right)+1; size=max(left)+1+nr; shift=max(left)+1
    arc=[(left[e],right[e]+shift) if bit[e] else (right[e]+shift,left[e]) for e in range(n)]
    incoming=[True]*size; outgoing=[True]*size
    ans=[]
    for t in range(n+2):
        mask=sum((1<<e) for e,(u,v) in enumerate(arc) if incoming[u] and outgoing[v]);ans.append(mask)
        incoming=[any(incoming[u] for u,v in arc if v==w) for w in range(size)]
        outgoing=[any(outgoing[v] for u,v in arc if u==w) for w in range(size)]
    return ans

def check(n, exhaustive=True):
    partitions_n=list(partitions(n));max_any=-1;max_simple=-1;checks=0
    examples=[]
    for i,L in enumerate(partitions_n):
        for j,R in enumerate(partitions_n):
            simple=len(set(zip(L,R)))==n
            # In extended mode cover all cases through size 6.
            if not exhaustive and (i*17+j*11)%191:continue
            for bits in product((0,1),repeat=n):
                obs=announcement_sequence(L,R,bits)
                rounds=len(obs)-1
                expected=walk_formula(L,R,bits)
                for t in range(n+2):
                    if expected[t]!=obs[min(t,rounds)]:
                        raise AssertionError((n,L,R,bits,t,expected[t],obs))
                checks+=1
                if rounds>max_any:max_any=rounds
                if simple and rounds>max_simple:max_simple=rounds
    claimed_any=max((n+1)//2,n-2)
    claimed_simple=max((n+1)//2,n-4)
    if exhaustive and (max_any,max_simple)!=(claimed_any,claimed_simple):
        raise AssertionError((n,max_any,max_simple,claimed_any,claimed_simple))
    print(f'n={n} cases={checks} max_rounds={max_any} proper_max={max_simple} predicted=({claimed_any},{claimed_simple})')

if __name__=='__main__':
    for n in range(1,6):check(n)
    check(6,exhaustive='--extended' in sys.argv)
    print('All direct PAL-versus-directed-walk checks passed.')

# Explicit extremal constructions: represent a directed bipartite graph by
# (side, index) endpoints, where side 0 denotes the first equivalence relation.
def edge(tail,head):
    assert tail[0]!=head[0]
    if tail[0]==0:return (tail[1],head[1],1)
    return (head[1],tail[1],0)

def path(n):
    vertices=[(i%2,i//2) for i in range(n+1)]
    return [edge(vertices[i],vertices[i+1]) for i in range(n)]

def cycle_tail(n,cycle):
    if cycle==2:
        assert n>=2
        edges=[edge((0,0),(1,0)),edge((1,0),(0,0))]
        start=(0,0); nextr=1; nextl=1
    else:
        assert cycle==4 and n>=4
        edges=[edge((0,0),(1,0)),edge((1,0),(0,1)),edge((0,1),(1,1)),edge((1,1),(0,0))]
        start=(0,0); nextr=2; nextl=2
    current=start
    for _ in range(n-cycle):
        if current[0]==0:
            nxt=(1,nextr);nextr+=1
        else:
            nxt=(0,nextl);nextl+=1
        edges.append(edge(current,nxt));current=nxt
    return edges

def test_witnesses():
    for n in range(1,41):
        ua=max((n+1)//2,n-2)
        sa=max((n+1)//2,n-4)
        for mode,raw,target in [('ordinary',path(n), (n+1)//2),
                                 ('multi-cycle',cycle_tail(n,2),n-2) if n>=2 else ('ordinary',path(n),(n+1)//2),
                                 ('simple-cycle',cycle_tail(n,4),n-4) if n>=4 else ('ordinary',path(n),(n+1)//2)]:
            ll=[e[0] for e in raw]; rr=[e[1] for e in raw];bits=[e[2] for e in raw]
            if len(set(zip(ll,rr)))!=n and mode!='multi-cycle':raise AssertionError(mode)
            rounds=len(announcement_sequence(ll,rr,bits))-1
            if rounds!=target:raise AssertionError((n,mode,target,rounds))
    print('All explicit path, two-cycle and four-cycle extremizers for n<=40 passed.')

if __name__=='__main__':test_witnesses()
