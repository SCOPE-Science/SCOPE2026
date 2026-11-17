#!/usr/bin/env python3
"""Independent exhaustive graph witness check for two-step periodic points of ECAs.
Requires only the Python 3 standard library. May be run with: python verify_scc.py
"""
from collections import Counter

def local(rule, left, center, right):
    return (rule >> (4*left + 2*center + right)) & 1

def step(rule, word):
    n = len(word)
    return tuple(local(rule, word[(i-1)%n], word[i], word[(i+1)%n]) for i in range(n))

def direct_first(rule):
    for n in range(1,7):
        for v in range(1<<n):
            word=tuple((v>>j)&1 for j in range(n))
            first=step(rule, word)
            if first!=word and step(rule, first)==word:
                return n, ''.join(map(str,word))
    return None, ''

def graph(rule):
    edges = [[] for _ in range(16)]
    for vertex in range(16):
        a,b,c,d=((vertex>>k)&1 for k in (3,2,1,0))
        for e in (0,1):
            y0=local(rule,a,b,c)
            y1=local(rule,b,c,d)
            y2=local(rule,c,d,e)
            if local(rule,y0,y1,y2)==c:
                edges[vertex].append(((2*vertex+e)&15, y1!=c))
    return edges

def cyclic_bad_edge(edges):
    # Kosaraju identifies exactly those edges contained in directed cycles.
    adj=[[target for target,bad in edges[i]] for i in range(16)]
    reverse=[[] for _ in range(16)]
    for i, out in enumerate(adj):
        for j in out: reverse[j].append(i)
    seen=set(); order=[]
    def visit(v):
        seen.add(v)
        for w in adj[v]:
            if w not in seen: visit(w)
        order.append(v)
    for i in range(16):
        if i not in seen: visit(i)
    comps=[-1]*16
    def assign(v,index):
        comps[v]=index
        for w in reverse[v]:
            if comps[w]==-1:assign(w,index)
    index=0
    for v in reversed(order):
        if comps[v]<0:assign(v,index);index+=1
    return any(bad and comps[i]==comps[j]
               for i in range(16) for j,bad in edges[i])

def main():
    counts=Counter()
    failures=[]
    sharp=[]
    for rule in range(256):
        n,witness=direct_first(rule)
        possible=cyclic_bad_edge(graph(rule))
        if possible!=(n is not None):failures.append(rule)
        counts['none' if n is None else n]+=1
        if n==6:sharp.append((rule,witness))
    assert not failures, ('Failed rule comparisons:',failures)
    assert counts==Counter({'none':107,1:64,2:48,3:6,4:17,5:2,6:12}),counts
    assert [r for r,w in sharp]==[26,82,90,154,164,165,166,167,180,181,210,218]
    print('rules=256; graph-witness equivalence=256/256')
    print('first-period-two ring lengths: none=107; 1=64; 2=48; 3=6; 4=17; 5=2; 6=12')
    print('sharp-six rules: '+','.join(str(r) for r,w in sharp))
    print('sharp-six witnesses: '+ ' '.join(f'{r}:{w}' for r,w in sharp))
    print('PASS')

if __name__=='__main__':main()
