#!/usr/bin/env python3
"""Exhaustive exact verification of the three exceptional lengths."""
from collections import defaultdict

def admissible(n):
    def visit(prefix, last):
        if len(prefix) == n:
            yield prefix
            return
        yield from visit(prefix+'0', '0')
        if last!='1':
            yield from visit(prefix+'1','1')
    yield from visit('','')

def signature(w):
    n=len(w)
    counts=[]
    for L in range(1,n+1):
        block=[0]*(L+1)
        for i in range(n-L+1):
            total=sum(c=='1' for c in w[i:i+L])
            block[total]+=1
        counts.extend(block)
    return tuple(counts)

def run(n):
    groups=defaultdict(list)
    for word in admissible(n):
        groups[signature(word)].append(word)
    assert sum(map(len,groups.values())) == {8:55,11:233,15:1597}[n]
    for fiber in groups.values():
        for word in fiber:
            assert set(fiber)=={word,word[::-1]}, (n,fiber)
    print('WINDOW_OK',n,'words',sum(map(len,groups.values())),'fibers',len(groups),'max_fiber',max(map(len,groups.values())))

if __name__=='__main__':
    for n in (8,11,15):run(n)
