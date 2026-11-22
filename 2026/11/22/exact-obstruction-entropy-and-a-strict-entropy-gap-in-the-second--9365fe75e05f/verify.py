#!/usr/bin/env python3
"""Exact finite-state certificate for the second spatial image of binary Rule 126."""
from collections import deque
from fractions import Fraction
import json
from pathlib import Path

RULE = 126
ROOTS = {1: (1754877, 1754878), 2: (1732101, 1732102)}
EXPECTED = {
    1: {
        'raw_states': 3, 'minimal_states': 3, 'start': 2,
        'transitions': [[-1,2],[1,0],[1,2]],
        'polynomial': [1,-2,1,-1],
        'counts': [1,2,4,7,12,21,37,65,114,200,351,616,1081,1897,3329,5842]
    },
    2: {
        'raw_states': 17, 'minimal_states': 13, 'start': 12,
        'transitions': [[-1,4],[-1,6],[-1,11],[3,1],[3,8],[3,11],
                        [6,0],[6,5],[6,7],[6,12],[10,2],[10,9],[10,12]],
        'polynomial': [1,-4,6,-5,3,-3,5,-3,-1,4,-2,1,-1,1],
        'counts': [1,2,4,7,12,21,37,65,114,200,351,616,1080,1891,3308,5783]
    },
}

def local_rule(bits):
    a=list(bits)
    while len(a)>1:
        a=[int((a[i],a[i+1],a[i+2]) not in ((0,0,0),(1,1,1)))
           for i in range(len(a)-2)]
    return a[0]

def deterministic_graph(t):
    width=2*t
    vertices=1<<width
    outgoing=[[0,0] for _ in range(vertices)]
    for s in range(vertices):
        for bit in (0,1):
            bits=tuple((s>>j)&1 for j in range(width-1,-1,-1))+(bit,)
            output=local_rule(bits)
            target=((s<<1)|bit)%(1<<width)
            outgoing[s][output] |= 1<<target
    initial=(1<<vertices)-1
    seen={initial:0}; queue=deque([initial]); transitions=[]
    while queue:
        subset=queue.popleft()
        row=[]
        for out in (0,1):
            image=0; m=subset
            while m:
                b=m&-m; i=b.bit_length()-1; image |= outgoing[i][out]; m-=b
            if image and image not in seen:
                seen[image]=len(seen);queue.append(image)
            row.append(seen.get(image,-1))
        transitions.append(tuple(row))
    # All nonempty subset states are accepting. The empty subset is an excluded dead state.
    block=[0]*len(transitions)
    for _ in range(1+len(transitions)):
        signatures=[tuple(-1 if j==-1 else block[j] for j in row) for row in transitions]
        class_id={v:i for i,v in enumerate(sorted(set(signatures)))}
        new=[class_id[s] for s in signatures]
        if new==block:break
        block=new
    else:raise AssertionError('Partition refinement did not stabilize')
    reduced={block[i]:tuple(-1 if j==-1 else block[j] for j in row)
             for i,row in enumerate(transitions)}
    assert len(reduced)==max(block)+1
    return len(transitions), block[0], [list(reduced[i]) for i in range(len(reduced))]

def counts(transitions, start, limit):
    v=[1]*len(transitions); result=[]
    for _ in range(limit):
        result.append(v[start]);v=[sum(v[j] for j in row if j>=0) for row in transitions]
    return result

def charpoly(transitions):
    n=len(transitions)
    A=[[0]*n for _ in range(n)]
    for i,row in enumerate(transitions):
        for j in row:
            if j>=0:A[i][j]+=1
    C=[[int(i==j) for j in range(n)] for i in range(n)]
    traces=[]
    for _ in range(n):
        C=[[sum(C[i][k]*A[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
        traces.append(sum(C[i][i] for i in range(n)))
    coeff=[1]
    for k in range(1,n+1):
        raw=sum(coeff[k-j]*traces[j-1] for j in range(1,k+1))
        assert raw%k==0
        coeff.append(-raw//k)
    return coeff

def trim(p):
    while len(p)>1 and p[-1]==0:p.pop()
    return p

def rem(p,q):
    p=trim(list(p));q=trim(list(q)); assert q[-1]
    while len(p)>=len(q) and any(p):
        c=p[-1]/q[-1];d=len(p)-len(q)
        for i,a in enumerate(q):p[d+i]-=c*a
        p=trim(p)
    return p

def sturm(p):
    # ascending rational coefficients
    p=trim([Fraction(x) for x in p[::-1]])
    derivative=[p[i]*i for i in range(1,len(p))]
    seq=[p,trim(derivative)]
    while len(seq[-1])>1:
        r=trim([-x for x in rem(seq[-2],seq[-1])])
        if len(r)==1 and r[0]==0:break
        seq.append(r)
    return seq

def variations(seq, x):
    signs=[]
    for p in seq:
        a=Fraction(0)
        for c in p[::-1]:a=a*x+c
        assert a!=0, 'choose another endpoint away from a root'
        signs.append(1 if a>0 else -1)
    return sum(a!=b for a,b in zip(signs,signs[1:]))

def verify():
    cert={}
    for t in (1,2):
        raw,start,tr=deterministic_graph(t)
        actual={'raw_states':raw,'minimal_states':len(tr),'start':start,
                'transitions':tr,
                'polynomial':charpoly(tr),
                'counts':counts(tr,start,16)}
        assert actual==EXPECTED[t],f'graph/characteristic/count mismatch at time={t}'
        factor=actual['polynomial']
        while factor[-1]==0:factor=factor[:-1]
        lo,hi=ROOTS[t]
        seq=sturm(factor)
        assert variations(seq,Fraction(lo,1000000))-variations(seq,Fraction(hi,1000000))==1
        assert variations(seq,Fraction(hi,1000000))-variations(seq,Fraction(2))==0
        cert[str(t)]={**actual,'positive_perron_bracket':[lo,hi,1000000],
                      'sturm_variations':[variations(seq,Fraction(lo,1000000)),
                                          variations(seq,Fraction(hi,1000000)),
                                          variations(seq,Fraction(2))]}
    assert cert['1']['counts'][:12]==cert['2']['counts'][:12]
    assert cert['1']['counts'][12]==1081 and cert['2']['counts'][12]==1080
    file_data=json.loads((Path(__file__).parent/'certificate.json').read_text())
    assert file_data==cert
    print('VERIFY_OK: exact deterministic automata, 13-degree characteristic, root isolation, word counts')

if __name__=='__main__':verify()
