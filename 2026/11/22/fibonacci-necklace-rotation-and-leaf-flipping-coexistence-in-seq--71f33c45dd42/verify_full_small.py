#!/usr/bin/env python3
"""Independent finite functional-graph check; not an all-size proof."""
from collections import Counter


def transition(n, state):
    r = list(state[:n]); b = list(state[n:])
    for i in range(n):
        c = r[i] + r[(i - 1) % n] + r[(i + 1) % n] + b[i]
        r[i] = int(c >= (3 if r[i] else 1))
    for i in range(n):
        c = b[i] + r[i]
        b[i] = int(c >= (3 if b[i] else 1))
    return tuple(r+b)


def encode(n, bits):
    L = n-1
    a=[]; b=[]
    for i in range(n):
        j=i%L
        a.append(int(bits[j] or bits[(j-1)%L]))
        b.append(bits[j])
    return tuple(a+b)


def main():
    for n in range(3,10):
        states=[]
        for m in range(1<<(2*n)):
            states.append(tuple((m >> i) & 1 for i in range(2*n)))
        nxt={s:transition(n,s) for s in states}
        done=set(); recurrent=set(); periods=Counter()
        for start in states:
            if start in done:continue
            path=[]; seen={}; v=start
            while v not in done and v not in seen:
                seen[v]=len(path); path.append(v); v=nxt[v]
            if v in seen:
                orbit=path[seen[v]:]
                recurrent.update(orbit)
                periods[len(orbit)] += 1
            done.update(path)
        U={tuple([1]*n+[(w>>i)&1 for i in range(n)]) for w in range(1<<n)}
        E=set()
        L=n-1
        for w in range(1<<L):
            bits=tuple((w>>i)&1 for i in range(L))
            if not any(bits[i] and bits[(i+1)%L] for i in range(L)):
                E.add(encode(n,bits))
        assert E|U == recurrent, (n,len(E|U),len(recurrent))
        print(f'n={n}: configurations={len(states)} periodic={len(recurrent)} orbit_counts={dict(sorted(periods.items()))}; E union U matches all recurrent (finite check only)')
    print('PASS: independent exhaustive finite systems n=3..9')

if __name__=='__main__':main()
