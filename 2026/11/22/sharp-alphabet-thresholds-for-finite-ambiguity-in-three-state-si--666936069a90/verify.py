#!/usr/bin/env python3
"""Exact finite-matrix closure certificate for a three-state NFA ambiguity bound."""
from collections import Counter, deque
from pathlib import Path

def mat(t):
    return ((t>>0)&1, (t>>1)&1, 0, (t>>2)&1, (t>>3)&1, (t>>4)&1)

def multiply(x,y):
    a,b,c,d,e,f=x
    A,B,C,D,E,F=y
    return (a*A, a*B+b*D, a*C+b*E+c*F, d*D, d*E+e*F, f*F)

def valid(t, side):
    l1,b12,l2,b23,l3=((t>>i)&1 for i in range(5))
    if (l1 and l2 and b12) or (l2 and l3 and b23): return False
    return not (l1 and l3 and (b12 if side=='X' else b23))

def closure(types):
    identity=(1,0,0,1,0,1)
    reached={identity}; todo=deque([identity])
    while todo:
        m=todo.popleft()
        for t in types:
            n=multiply(m, mat(t))
            if n not in reached:
                reached.add(n);todo.append(n)
    return reached

def main():
    certs={}
    for side in 'XY':
        types=[t for t in range(32) if valid(t,side)]
        assert len(types)==23
        computed=closure(types)
        path=Path(__file__).with_name('matrices_'+side+'.csv')
        supplied={tuple(int(s) for s in line.split(',')) for line in path.read_text().splitlines()}
        assert len(supplied)==48 and computed==supplied
        assert (1,0,0,1,0,1) in supplied
        assert all(mat(t) in supplied for t in types)
        assert all(multiply(m,mat(t)) in supplied for m in supplied for t in types)
        assert max(m[2] for m in supplied)==4
        certs[side]=types
        print('SIDE',side,'GENERATORS',len(types),'PRODUCT_MATRICES',len(supplied),'MAX_ACCEPTING_RUNS',max(m[2] for m in supplied))
    counts=Counter()
    for a in range(32):
        for b in range(32):
            if not ((a|b)&2 and (a|b)&8): continue
            if not any(a in certs[s] and b in certs[s] for s in 'XY'):continue
            runs=closure((a,b))
            degree=max(m[2] for m in runs)
            assert 1<=degree<=3
            counts[degree]+=1
    assert counts=={1:216,2:28,3:2}
    assert max(m[2] for m in closure([10]))==1
    for types,word,wanted in [([10],'aa',1),([11,26],'aabb',3),([3,14,24],'abbc',4)]:
        m=(1,0,0,1,0,1)
        for c in word:m=multiply(m,mat(types[ord(c)-ord('a')]))
        assert m[2]==wanted,(types,word,m)
    print('BINARY_ORDERED_TRIM_FINITE_DEGREE_DISTRIBUTION',sorted(counts.items()))
    print('WITNESSES unary=1 binary=3 ternary=4')
    print('VERIFY_OK')
if __name__=='__main__': main()
