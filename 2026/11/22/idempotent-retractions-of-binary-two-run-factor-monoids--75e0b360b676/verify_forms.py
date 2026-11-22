#!/usr/bin/env python3
"""Independent run-state DFA and constructive characterization of idempotents.

No packages needed. This implementation uses the explicit run transition table,
not prefix matching. It compares all generated idempotent maps as a set with
an independently constructed catalogue of idempotent retractions.
"""
from collections import deque


def run_transition(r,s):
    Z=r+s; N=Z+1
    zero=[]; one=[]
    for v in range(N):
        if v == Z:
            zero.append(Z); one.append(Z)
        elif v <= r:
            zero.append(min(v+1,r))
            if v<r: one.append(0)
            else: one.append(r+1 if s>1 else Z)
        else:
            j=v-r
            zero.append(1)
            one.append(v+1 if j<s-1 else Z)
    return (tuple(zero), tuple(one))


def closure(generators):
    n=len(generators[0]); identity=tuple(range(n)); q=deque([identity]); out={identity}
    while q:
        a=q.popleft()
        for g in generators:
            b=tuple(g[v] for v in a)
            if b not in out: out.add(b); q.append(b)
    return out


def form_catalogue(r,s):
    n=r+s; Z=n; identity=tuple(range(n+1)); all_sink=(Z,)*(n+1)
    out={identity,all_sink}
    def create(dead, fixed):
        dead=set(dead)
        assert fixed not in dead
        return tuple(Z if j in dead or j==Z else fixed for j in range(n+1))
    if s>=2 and r>=2:
        for p in range(n): out.add(create([],p))
        for k in range(1,r):
            H=range(r-k,r+1)
            for p in range(n):
                if p not in H: out.add(create(H,p))
        for k in range(1,s):
            K=range(r+s-k, r+s)
            for p in range(n):
                if p not in K: out.add(create(K,p))
        K=range(r,r+s)
        for p in range(r): out.add(create(K,p))
    elif s==1:
        out.add(create([],r))
        for k in range(1,r):
            H=range(r-k,r+1)
            for p in range(r-k): out.add(create(H,p))
        for p in range(r): out.add(create([r],p))
    else:
        # r=1, s>=2: one-step zero input immediately coalesces survivors;
        # pure ones and killed-tail classes give a reflected catalogue.
        for p in range(1,n): out.add(create([],p))
        for k in range(1,s):
            K=range(n-k,n)
            for p in range(1,n-k): out.add(create(K,p))
        out.add(create(range(1,n),0))
    return out


def run():
    trials=0
    for r in range(1,11):
        for s in range(1,11):
            M=closure(run_transition(r,s))
            idem={t for t in M if all(t[t[v]]==t[v] for v in range(r+s+1))}
            candidate=form_catalogue(r,s)
            assert idem==candidate, ('catalogue mismatch',r,s,len(idem),len(candidate),len(idem-candidate),len(candidate-idem))
            trials+=1
    print('PASS: 100 run-state monoids; exact set equality with explicit idempotent retraction forms')

if __name__=='__main__':run()
