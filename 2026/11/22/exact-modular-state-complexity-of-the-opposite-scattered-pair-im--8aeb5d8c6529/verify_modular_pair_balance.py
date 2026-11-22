"""Self-contained checks for a binary scattered-pair balance language.
Run: python3 verify_modular_pair_balance.py
Requires only the Python 3 standard library.
"""
from collections import deque
from itertools import product
from math import gcd


def imbalance(word):
    zeros = ones = zero_one = one_zero = 0
    for bit in word:
        if bit == '0':
            one_zero += ones
            zeros += 1
        else:
            zero_one += zeros
            ones += 1
    return zero_one - one_zero


def step(state, letter, mod):
    a,b,d=state
    return ((a+1)%mod,b,(d-b)%mod) if letter=='0' else (a,(b+1)%mod,(d+a)%mod)


def run(state, word, mod):
    for letter in word:
        state = step(state, letter, mod)
    return state


def make_word(A,B,k):
    """Exactly A zeros, B ones and k scattered 01 pairs, for 0<=k<=A*B."""
    if A==0:
        assert k==0
        return '1'*B
    q,r=divmod(k,A)
    extra=int(r>0)
    assert B-q-extra>=0
    w='1'*(B-q-extra)+'0'*r+'1'*extra+'0'*(A-r)+'1'*q
    assert len(w)==A+B
    return w


def suffix_for(s,t,m):
    """Return a witness accepting s but not t, via three algebraic count classes."""
    a,b,d=s
    g=gcd(m,2)
    cases=[((-a)%m,0),((-a)%m,1),((-a+1)%m,(-b)%m)]
    for ar,br in cases:
        if ((d - t[2] +(a-t[0])*br -(b-t[1])*ar)%m)==0:
            continue
        E=(-d-a*br+b*ar)%m
        A=ar+m
        B=br+m
        target=(E+A*B)%m
        assert target%g==0
        period=m//g
        k=((target//g)*pow(2//g,-1,period))%period if period>1 else 0
        w=make_word(A,B,k)
        assert (2*k-A*B-E)%m==0
        assert run(s,w,m)[2]==0 and run(t,w,m)[2]!=0
        return w
    raise AssertionError((m,s,t))


def minimize(states,mod):
    pos={s:i for i,s in enumerate(states)}
    nxt=[(pos[step(s,'0',mod)],pos[step(s,'1',mod)]) for s in states]
    labels=[int(s[2]==0) for s in states]
    rounds=0
    while True:
        signature=[(labels[i],labels[x],labels[y]) for i,(x,y) in enumerate(nxt)]
        ids={signature_value:k for k,signature_value in enumerate(sorted(set(signature)))}
        new=[ids[v] for v in signature]
        rounds+=1
        if len(set(new))==len(set(labels)):
            return len(set(new)),rounds
        labels=new


def main():
    words=0
    for n in range(0,13):
        for bits in product('01',repeat=n):
            w=''.join(bits)
            d=imbalance(w)
            for m in (2,3,4,5,6,7,9,11):
                assert run((0,0,0),w,m)[2]==d%m
            words+=1
    print('direct_subsequence_word_checks',words)
    examined=0
    for m in range(2,18):
        g=gcd(m,2)
        start=(0,0,0)
        seen={start}
        todo=deque([start])
        while todo:
            s=todo.popleft()
            for letter in '01':
                t=step(s,letter,m)
                if t not in seen:
                    seen.add(t)
                    todo.append(t)
        assert len(seen)==m**3//g
        assert all((d+a*b)%g==0 for a,b,d in seen)
        count, rounds=minimize(sorted(seen),m)
        assert count==len(seen)
        examined+=count
        print('modulus',m,'reachable_and_minimal',count,'partition_rounds',rounds)
    print('total_reachable_states_checked',examined)
    checked_pairs=0
    for m in range(2,7):
        g=gcd(m,2)
        states=[(a,b,d) for a in range(m) for b in range(m)
                for d in range(m) if (d+a*b)%g==0]
        for i,s in enumerate(states):
            for t in states[i+1:]:
                w=suffix_for(s,t,m)
                assert run(s,w,m)[2]==0
                assert run(t,w,m)[2]!=0
                checked_pairs+=1
    print('explicit_pair_separators',checked_pairs)
    print('ALL CHECKS PASSED')


if __name__=='__main__':
    main()
