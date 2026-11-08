"""Standalone ordinary finite-variable colour-refinement checker for balanced complete bipartite and crown graphs.
No counting: replacement-neighbourhood information is represented by sets, not multisets.
"""
import itertools
import sys
from functools import lru_cache


def graph(n, crown):
    v = 2 * n
    a = [[False]*v for _ in range(v)]
    for i in range(n):
        for j in range(n):
            if not crown or i != j:
                a[i][n+j] = a[n+j][i] = True
    return a


def compare(n1, crown1, n2, crown2, width, cap=25):
    gs = (graph(n1, crown1), graph(n2, crown2))
    sizes = [len(g) for g in gs]
    tuples = [list(itertools.product(range(v), repeat=width)) for v in sizes]
    indices = [{t: i for i, t in enumerate(ts)} for ts in tuples]
    base = []
    for g, ts in zip(gs, tuples):
        out=[]
        for t in ts:
            eq=tuple(t[i]==t[j] for i in range(width) for j in range(i+1,width))
            edges=tuple(g[t[i]][t[j]] for i in range(width) for j in range(i+1,width))
            out.append((eq,edges))
        base.append(out)
    palette={v:i for i,v in enumerate(sorted(set(base[0]+base[1])))}
    colors=[[palette[x] for x in a] for a in base]
    for round_id in range(cap+1):
        left=set(colors[0]);right=set(colors[1]);
        if left != right:
            return False,round_id,len(left),len(right)
        if round_id==cap:
            raise RuntimeError('iteration limit reached')
        signatures=[]
        for g, ts, ix, cs in zip(gs, tuples, indices, colors):
            sig=[]; v=len(g)
            for t, c in zip(ts,cs):
                new=[]
                for pos in range(width):
                    arr=list(t)
                    newset=set()
                    for x in range(v):
                        arr[pos]=x
                        newset.add(cs[ix[tuple(arr)]])
                    new.append(tuple(sorted(newset)))
                sig.append((c, tuple(new)))
            signatures.append(sig)
        palette={sig:i for i,sig in enumerate(sorted(set(signatures[0]+signatures[1])))}
        newcolors=[[palette[s] for s in seq] for seq in signatures]
        if newcolors == colors:
            return True,round_id,len(left),len(right)
        colors=newcolors


def predicted(n1,c1,n2,c2,k):
    return k<=2 or (c1==c2 and min(n1,k)==min(n2,k))


def run():
    cases=[]
    for k in (1,2,3,4):
        for n in range(2,7 if k<=3 else 6):
            for m in range(n,7 if k<=3 else 6):
                for c in (False,True):
                    for d in (False,True):
                        if n==m and c and not d: continue
                        cases.append((n,c,m,d,k))
    # width five: representative cross-category and threshold cases only.
    cases.extend((n,c,m,d,5) for n,m in [(2,2),(2,3),(3,4),(4,5),(5,5)] for c in (False,True) for d in (False,True))
    print('Standalone finite-variable refinement with replacement COLOR SETS; no counting')
    count=0; largest=0
    for n,c,m,d,k in cases:
        if k==5 and max(n,m)>4 and not (n,m)==(4,5):continue
        actual,step,p,q=compare(n,c,m,d,k)
        expect=predicted(n,c,m,d,k)
        if actual!=expect:
            raise AssertionError((n,c,m,d,k,actual,expect,step))
        count+=1
        largest=max(largest,step)
    print('comparisons:',count)
    print('maximum refinement rounds:',largest)
    print('all predictions matched: PASS')
    for k in (2,3,4,5):
        n=k-1 if k>=3 else 2
        if k==5: n=4
        print(f'example width={k}: crown({n}) vs crown({n+1}) =>',compare(n,True,n+1,True,k)[0])
    print('cross-family width=2 n=2 and n=4:',compare(2,True,4,False,2)[0])
    print('cross-family width=3 n=2 and n=2:',compare(2,True,2,False,3)[0])


if __name__=='__main__':run()
