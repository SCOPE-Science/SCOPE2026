#!/usr/bin/env python3
"""Exact local and finite-state checks for Rule 184 finite-time image languages.
Python 3 standard library; no external packages.
"""
from collections import deque
from itertools import product
from fractions import Fraction

def F(a,b,c): return (a & (1-b)) | (b & c)
def G(a,b,c): return (c & (1-b)) | (b & a)

def local_checks():
    fA=[];fB=[];gA=[];gB=[]
    for x in product((0,1),repeat=4):
        a=F(*x[:3]);b=F(*x[1:]);c=G(*x[:3]);d=G(*x[1:])
        code=''.join(map(str,x))
        if a==b==1: fA.append(code)
        if a==b==0: fB.append(code)
        if c==d==1: gA.append(code)
        if c==d==0: gB.append(code)
    assert fA == ['0111','1011','1111'],fA
    assert fB == ['0000','0001','0010'],fB
    assert gA == ['1101','1110','1111'],gA
    assert gB == ['0000','0100','1000'],gB
    discrepancies=[]
    for x in product((0,1),repeat=5):
        y=[G(*x[k:k+3]) for k in range(3)]
        if F(*y)!=x[2]: discrepancies.append(''.join(map(str,x)))
    assert discrepancies == ['01100','11000','11001','11100'],discrepancies
    # Cyclic checks complement the complete local context tests.
    for n in range(6,14):
        for bits in product((0,1), repeat=n):
            input_word=''.join(map(str,bits))
            if '1100' not in input_word+input_word[:3]:
                y=[G(bits[(i-1)%n],bits[i],bits[(i+1)%n]) for i in range(n)]
                z=[F(y[(i-1)%n],y[i],y[(i+1)%n]) for i in range(n)]
                assert z==list(bits)
    return (fA,fB,gA,gB,discrepancies)

def local_t(bits,t):
    a=bits
    for _ in range(t):a=tuple(F(*a[k:k+3]) for k in range(len(a)-2))
    assert len(a)==1
    return a[0]

def automaton_image(t):
    v=1<<(2*t); mask=v-1
    edges=[[0,0] for _ in range(v)]
    for s in range(v):
        for b in (0,1):
            initial=tuple((s>>k)&1 for k in range(2*t-1,-1,-1))+(b,)
            c=local_t(initial,t)
            edges[s][c] |= 1<<(((s<<1)|b)&mask)
    start=(1<<v)-1
    states=[start]; lookup={start:0}; trans=[]
    for state in states:
        row=[]
        for c in (0,1):
            nxt=0; s=state
            while s:
                bit=s&-s; idx=bit.bit_length()-1;s-=bit
                nxt |= edges[idx][c]
            if nxt and nxt not in lookup:
                lookup[nxt]=len(states);states.append(nxt)
            row.append(lookup.get(nxt,-1))
        trans.append(row)
    return states,trans

def automaton_avoid(t):
    words=['11'+'01'*k+'00' for k in range(t)]
    prefixes=['']+sorted({w[:j] for w in words for j in range(1,len(w))},key=lambda s:(len(s),s))
    transitions=[]
    for p in prefixes:
        row=[]
        for c in '01':
            s=p+c
            if any(w in s for w in words): row.append(-1)
            else:row.append(max((len(q),i) for i,q in enumerate(prefixes) if s.endswith(q))[1])
        transitions.append(row)
    return prefixes,transitions

def check_same(A,B):
    todo=deque([(0,0,'')]);seen={(0,0)}
    while todo:
        a,b,w=todo.popleft()
        for c in (0,1):
            aa=A[a][c];bb=B[b][c]
            if (aa==-1)!=(bb==-1):raise AssertionError('mismatch '+w+str(c))
            if aa!=-1 and (aa,bb) not in seen:
                seen.add((aa,bb));todo.append((aa,bb,w+str(c)))
    return len(seen)

def prefix_matrix(t):
    _,T=automaton_avoid(t);n=len(T)
    return [[sum(T[i][c]==j for c in (0,1)) for j in range(n)] for i in range(n)]

def characteristic(A):
    # Exact characteristic polynomial via formal log of determinant (Newton identities).
    n=len(A)
    def mul(B,C):
        return [[sum(B[i][k]*C[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    # Trace identity and exact Newton coefficients.
    M=[[int(i==j) for j in range(n)] for i in range(n)]
    traces=[]
    for k in range(1,n+1):
        M=mul(M,A); traces.append(sum(M[i][i] for i in range(n)))
    coeff=[Fraction(1)]
    for k in range(1,n+1):
        coeff.append(-sum(coeff[k-j]*traces[j-1] for j in range(1,k+1))/k)
    assert all(c.denominator==1 for c in coeff)
    return [int(x) for x in coeff]

def direct_language(n,t):
    outputs=set()
    for bits in product((0,1),repeat=n+2*t):
        x=list(bits)
        for _ in range(t):x=[F(*x[k:k+3]) for k in range(len(x)-2)]
        outputs.add(''.join(map(str,x)))
    return outputs

def verify():
    local_checks()
    for t,expected in [(1,6),(2,17),(3,46),(4,122)]:
        states,A=automaton_image(t); prefixes,B=automaton_avoid(t)
        count=check_same(A,B)
        assert len(states)==expected,(t,len(states))
        print('t=',t,'nonempty subset states',len(states),'prefix states',len(prefixes),'checked product states',count)
    assert characteristic(prefix_matrix(1))==[1,-2,0,0,1]
    p2=characteristic(prefix_matrix(2))
    assert p2 == [1,-2,0,0,1,0,1],p2
    for t in (1,2,3):
        for n in range(1,10 if t==1 else 9 if t==2 else 7):
            language=direct_language(n,t)
            words=['11'+'01'*j+'00' for j in range(t)]
            target={''.join(w) for w in product('01',repeat=n) if not any(b in ''.join(w) for b in words)}
            assert language==target, (t,n,len(language),len(target))
    print('VERIFY_OK')
if __name__=='__main__':verify()
