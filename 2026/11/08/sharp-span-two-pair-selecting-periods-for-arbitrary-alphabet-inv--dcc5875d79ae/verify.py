#!/usr/bin/env python3
"""Exact constructive and finite checks for pair-selecting cycles of span two.
Uses only the Python standard library. All alphabets are canonical relabelings.
"""
from collections import Counter,defaultdict
from itertools import product


def target(f,r):
    if r<1 or f<0: raise ValueError('need at least one transposition')
    m=2*r*(f+r)
    return m-(f==0 and r%2==1)

def sigma(f,r):
    return tuple(list(range(f))+[f+2*i+(1-b) for i in range(r) for b in (0,1)])

def make_quotient(f,r):
    """Vertices F0..F(f-1),P0..P(r-1); arcs (src,dst,voltage), voltage=None at fixed endpoint."""
    E=[]
    for i in range(r):
        for j in range(r):
            for d in range(2):
                if not (f==0 and r%2 and i==j==0 and d==1):
                    E.append((f+i,f+j,d))
    for a in range(f):
        for i in range(r):
            E.append((a,f+i,None)); E.append((f+i,a,None))
    assert len(E)==target(f,r)
    return E

def euler_arc_order(f,r):
    E=make_quotient(f,r)
    outs=defaultdict(list)
    for t,(a,b,d) in enumerate(E):outs[a].append(t)
    start=0
    stack=[(start,None)]
    trail=[]
    while stack:
        v,_=stack[-1]
        if outs[v]:
            t=outs[v].pop()
            stack.append((E[t][1],t))
        else:
            _,t=stack.pop()
            if t is not None:trail.append(t)
    trail=trail[::-1]
    assert len(trail)==len(E)
    v=start
    for t in trail:
        assert E[t][0]==v
        v=E[t][1]
    assert v==start
    return E,trail

def construct(f,r):
    E,trail=euler_arc_order(f,r)
    current=0
    bit=0 # when current is a pair vertex; arbitrary reset to 0 when leaving fixed vertex
    W=[]
    for t in trail:
        a,b,d=E[t]
        assert a==current
        W.append(a if a<f else f+2*(a-f)+bit)
        if b<f:
            bit=0
        elif a<f:
            bit=0
        else:
            bit^=d
        current=b
    assert current==0
    assert current<f or bit==0
    assert len(W)==target(f,r)
    return W

def validate(W,f,r):
    assert len(W)==target(f,r)
    k=f+2*r
    assert all(0<=x<k for x in W)
    p=sigma(f,r)
    pairs=[(W[i],W[(i+1)%len(W)]) for i in range(len(W))]
    s=set(pairs)
    assert len(s)==len(pairs),('duplicate',f,r)
    assert not any((p[a],p[b]) in s for a,b in s),('involution pair',f,r)
    fixed=f*f
    assert len(s)<= (k*k-fixed)//2
    return True

def independent_exhaustion(f,r):
    """No use of quotient graph; DFS directly over binary/ternary/quaternary cyclic words."""
    k=f+2*r
    if k>4: return None
    p=sigma(f,r)
    # Upper bound, DFS cyclic words with no duplicate/reversed-transformed pairs.
    U=(k*k-f*f)//2
    for m in range(U,0,-1):
        # Fix first letter only for f=0 canonical complement symmetry; otherwise try all.
        for start in range(k):
            def rec(word,seen):
                if len(word)==m:
                    edge=(word[-1],word[0])
                    return tuple(word) if edge not in seen and (p[edge[0]],p[edge[1]]) not in seen and (edge[0],edge[1]) != (p[edge[0]],p[edge[1]]) else None
                for x in range(k):
                    edge=(word[-1],x)
                    if edge== (p[edge[0]],p[edge[1]]) or edge in seen or (p[edge[0]],p[edge[1]]) in seen:
                        continue
                    ans=rec(word+[x],seen|{edge})
                    if ans is not None: return ans
                return None
            ans=rec([start],set())
            if ans is not None:return len(ans),ans
    return 0,None

def main():
    cases=0
    for r in range(1,8):
        for f in range(0,8):
            W=construct(f,r)
            validate(W,f,r)
            cases+=1
    assert target(0,1)==1
    assert target(0,2)==8
    assert target(0,3)==17
    assert target(1,1)==4
    assert target(3,1)==8
    for f,r in [(0,1),(0,2),(1,1),(2,1)]:
        m,w=independent_exhaustion(f,r)
        assert m==target(f,r),(f,r,m,target(f,r))
    print('PAIR_SELECTING_SPAN_TWO_VERIFY_OK',cases)
    for f,r in [(0,1),(0,2),(0,3),(1,1),(2,1),(3,1),(1,2)]:
        W=construct(f,r)
        print('f=',f,'r=',r,'max=',len(W),'word=',','.join(map(str,W)))
if __name__=='__main__':main()
