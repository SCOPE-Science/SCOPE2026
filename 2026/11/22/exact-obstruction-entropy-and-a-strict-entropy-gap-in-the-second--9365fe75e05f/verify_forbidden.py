#!/usr/bin/env python3
"""All-length minimal-forbidden-word series certificate for second-image Rule 126."""
from collections import deque
import json
from pathlib import Path
from verify import deterministic_graph, charpoly, sturm, variations
from fractions import Fraction


def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out


def pair_machine():
    _,start,tr=deterministic_graph(2)
    initial=[]
    for letter in (0,1):
        a=tr[start][letter]
        if a>=0:initial.append((a,start))
    seen={p:i for i,p in enumerate(initial)};queue=deque(initial)
    states=[]; rows=[]; ends=[]
    while queue:
        a,b=queue.popleft();states.append([a,b]);row=[];count=0
        for letter in (0,1):
            na,nb=tr[a][letter],tr[b][letter]
            if na==-1 and nb>=0:
                count+=1;row.append(-2)  # final letter completes a minimal obstruction
            elif na>=0 and nb>=0:
                pair=(na,nb)
                if pair not in seen:
                    seen[pair]=len(seen);queue.append(pair)
                row.append(seen[pair])
            else:row.append(-1)
        rows.append(row);ends.append(count)
    assert len(rows)==29
    productive=set(i for i,v in enumerate(ends) if v)
    queue=deque(productive)
    while queue:
        v=queue.popleft()
        for i,row in enumerate(rows):
            if i not in productive and v in row:
                productive.add(i);queue.append(i)
    ids=sorted(productive)
    assert len(ids)==16
    renumber={v:i for i,v in enumerate(ids)}
    p_rows=[[renumber[j] if j in productive else -1 for j in rows[i]] for i in ids]
    p_ends=[ends[i] for i in ids]
    p_states=[states[i] for i in ids]
    starts=[renumber[i] for i in range(len(initial)) if i in productive]
    assert starts==[0]
    return p_states,p_rows,p_ends,starts


def reachable(rows,start,within):
    seen={start};todo=[start]
    while todo:
        for nxt in rows[todo.pop()]:
            if nxt in within and nxt not in seen:seen.add(nxt);todo.append(nxt)
    return seen


def counts(rows, ends, start, max_n):
    v=[0]*len(rows)
    for i in start:v[i]+=1
    out=[0,0]
    for n in range(2,max_n+1):
        out.append(sum(c*t for c,t in zip(v,ends)))
        nxt=[0]*len(rows)
        for i,c in enumerate(v):
            for j in rows[i]:
                if j>=0:nxt[j]+=c
        v=nxt
    return out


def compute_certificate():
    states,rows,ends,starts=pair_machine()
    active=set(range(2,16))
    assert all(reachable(rows,i,active)==active for i in active)
    assert 4 in rows[4]  # a self-loop makes this unique dominant component aperiodic
    assert set(range(2,16))==active
    # The pair-machine's two other states are transient, and each can reach a terminal.
    cp=charpoly([[j for j in row if j>=0] for row in rows])
    denominator=mul([1,0,0,0,1],[1,-2,1,0,-1,0,0,0,-1])
    assert cp==denominator+[0]*4
    root_polynomial=[1,-2,1,0,-1,0,0,0,-1]
    s=sturm(root_polynomial)
    assert [variations(s,Fraction(j,1000000)) for j in (1647072,1647073,2000000)]==[4,3,3]
    numerator=[0]*13
    for i,v in ((3,1),(4,-2),(5,1),(8,-2),(9,1),(11,-2),(12,1)):
        numerator[i]=v
    word_counts=counts(rows,ends,starts,43)
    # M(z)=z^2*u*(I-zA)^(-1)*terminal.  det(I-zA) M(z) has degree at most 17,
    # since the 16x16 adjugate has entries of degree at most 15.
    for k in range(18):
        left=sum(denominator[j]*word_counts[k-j] for j in range(min(k,len(denominator)-1)+1))
        assert left==(numerator[k] if k<len(numerator) else 0),(k,left)
    return {'states':states,'transitions':rows,'terminals':ends,
            'initial_states':starts,'charpoly':cp,'denominator':denominator,
            'numerator':numerator,'minimal_forbidden_counts':word_counts}


def main():
    actual=compute_certificate()
    expected=json.loads((Path(__file__).parent/'forbidden_certificate.json').read_text())
    assert actual==expected
    print('FORBIDDEN_VERIFY_OK: 16 productive states, primitive SCC, exact infinite rational series')

if __name__=='__main__':main()
