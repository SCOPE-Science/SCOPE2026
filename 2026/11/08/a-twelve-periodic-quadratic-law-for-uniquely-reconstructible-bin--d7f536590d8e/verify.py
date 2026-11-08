#!/usr/bin/env python3
"""Exact finite-state proof checker for binary 3-gram singleton reconstruction."""
import json
from collections import deque
from pathlib import Path

ROOT=Path(__file__).resolve().parent
C=(-88,-85,-108,-85,-88,-97,-96,-85,-100,-85,-96,-97)
SMALL=(None,None,None,8,14,26,46,74,92)


def transition(q, bit):
    start,previous,follow,black,multiple=q
    nxt=((previous<<1)|bit)&3
    f=list(follow)
    if f[previous]!=-1 and f[previous]!=nxt:
        vertex=previous
        visited=set()
        while True:
            assert vertex not in visited, 'successor loop is not rooted at current vertex'
            visited.add(vertex)
            black |= 1<<vertex
            vertex=f[vertex]
            assert vertex>=0
            if vertex==previous:
                break
    if black&(1<<nxt):
        return None
    f[previous]=nxt
    return (start,nxt,tuple(f),black,bool(multiple or nxt!=start))


def make_dfa():
    initial=[(s,s,(-1,-1,-1,-1),0,False) for s in range(4)]
    states=initial[:]
    ids={q:i for i,q in enumerate(states)}
    for q in states:
        for bit in (0,1):
            t=transition(q,bit)
            if t is not None and t not in ids:
                ids[t]=len(states)
                states.append(t)
    edges=[[ids[t] if (t:=transition(q,bit)) is not None else -1 for bit in (0,1)] for q in states]
    accept=[not (q[0]==q[1] and q[4]) for q in states]
    return states,edges,accept,[ids[q] for q in initial]


def count_vectors(edges,init,maxlen):
    k=len(edges)
    v=[0]*k
    for s in init:v[s]+=1
    out={2:v}
    for n in range(3,maxlen+1):
        u=[0]*k
        for i,a in enumerate(v):
            if a:
                for t in edges[i]:
                    if t!=-1:
                        u[t]+=a
        v=u
        out[n]=v
    return out


def main():
    states,edges,accept,init=make_dfa()
    assert len(states)==166,(len(states),'reachable states')
    dfa=json.loads((ROOT/'transition_table.json').read_text(encoding='utf8'))
    assert dfa=={'initial':init,'states':[list(q[:2])+[list(q[2]),q[3],q[4]] for q in states], 'edges':edges,'accept':accept}
    R=count_vectors(edges,init,65)
    S={n:sum(x for x,a in zip(R[n],accept) if a) for n in R}
    for n in range(3,9):assert S[n]==SMALL[n],(n,S[n])
    for n in range(9,45):
        expected=(n*n+28*n+C[n%12])//2
        assert 2*expected==n*n+28*n+C[n%12]
        assert S[n]==expected,(n,S[n],expected)
    # The exact identity is a *vector* equality, not merely agreement of scalar counts.
    assert all(R[45][j]-3*R[33][j]+3*R[21][j]-R[9][j]==0 for j in range(len(states)))
    cert=json.loads((ROOT/'recurrence_certificate.json').read_text(encoding='utf8'))
    assert cert=={'state_count':len(states),'initial_values':{str(n):SMALL[n] for n in range(3,9)},'periodic_constants':list(C),
                 'vectors':{str(n):R[n] for n in (9,21,33,45)}}
    # Additional, logically redundant direct-length checks.
    for n in range(45,66):assert S[n]==(n*n+28*n+C[n%12])//2
    print('VERIFY_OK states=166 recurrence_vector=zero n=3..65')

if __name__=='__main__':main()
