#!/usr/bin/env python3
"""Finite reproducibility checks for the square root of the scattered 00 1^b ideal."""
from itertools import product
from collections import deque

def prefix_automaton(b):
    n=b+3
    def step(q,c):
        if q==n-1:return q
        if q<2 and c=='0':return q+1
        if q>=2 and c=='1':return q+1
        return q
    return tuple(tuple(step(q,c) for q in range(n)) for c in '01')

def reference_state_count(b):
    t0,t1=prefix_automaton(b)
    n=b+3
    ident=tuple(range(n));states=[ident]; lookup={ident:0};edges=[]
    for f in states:
        out=[]
        for letter in (t0,t1):
            nxt=tuple(letter[f[q]] for q in range(n))
            if nxt not in lookup:
                lookup[nxt]=len(states);states.append(nxt)
            out.append(lookup[nxt])
        edges.append(tuple(out))
    accepting=[int(f[f[0]]==n-1) for f in states]
    return minimize(edges,accepting),len(states)

def minimize(edges,accepting):
    classes=list(accepting)
    while True:
        signatures=[(accepting[i],classes[edges[i][0]],classes[edges[i][1]]) for i in range(len(edges))]
        unique={sig:k for k,sig in enumerate(sorted(set(signatures)))}
        fresh=[unique[sig] for sig in signatures]
        if len(set(fresh))==len(set(classes)):
            return len(set(fresh))
        classes=fresh

def states_for(b):
    def canonical(s):
        if s==('Q',1,1): return ('R',1)
        return s
    q=[('P',i) for i in range(b+1)]
    q += [('Q',a,beta) for a in range(1,b+1) for beta in range(a+1) if (a,beta)!=(1,1)]
    q += [('R',j) for j in range(1,(b+1)//2+1)]
    q += [('A',)]
    lookup={s:i for i,s in enumerate(q)}
    trans=[]
    for s in q:
        if s[0]=='P':
            p=s[1]
            nxt=(('Q',b,max(0,b-p)),('P',min(b,p+1)))
        elif s[0]=='Q':
            a,beta=s[1:]
            x=('A',) if beta==0 else ('R',(beta+1)//2)
            y=('A',) if a==1 else ('Q',a-1,max(0,beta-1))
            nxt=(x,y)
        elif s[0]=='R':
            j=s[1];nxt=(s,('A',) if j==1 else ('R',j-1))
        else:
            nxt=(s,s)
        trans.append(tuple(lookup[canonical(v)] for v in nxt))
    accepting=[int(s==('A',)) for s in q]
    assert len(q)==len(set(q))
    reach={lookup[('P',0)]};front=list(reach)
    for s in front:
        for t in trans[s]:
            if t not in reach:
                reach.add(t);front.append(t)
    assert len(reach)==len(q),(b,len(q),len(reach))
    return q,lookup,trans,accepting

def has_scattered_001b_double(w,b):
    stage=0
    for c in w+w:
        if stage<2 and c=='0':stage+=1
        elif 2<=stage<b+2 and c=='1':stage+=1
    return stage==b+2

def run():
    total_words=0
    for b in range(1,17):
        states,lookup,edges,accepting=states_for(b)
        want=(b*b+1)//2+3*b+1
        assert len(states)==want,(b,len(states),want)
        assert minimize(edges,accepting)==want,(b,'not minimal')
        for n in range(0,min(11,b+5)+1):
            for bits in product('01',repeat=n):
                word=''.join(bits)
                st=lookup[('P',0)]
                for c in word:st=edges[st][int(c)]
                assert bool(accepting[st])==has_scattered_001b_double(word,b),(b,word)
                total_words+=1
        if b<=8:
            reference,raw=reference_state_count(b)
            assert reference==want,(b,reference,want)
        print(f'b={b}: formula={want}, minimal={minimize(edges,accepting)}, direct-word checks completed',flush=True)
    print('PASS',{'parameters':16,'direct_word_comparisons':total_words,'independent_transform_monoid_minimizations':8})

if __name__=='__main__':run()
