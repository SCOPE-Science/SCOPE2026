#!/usr/bin/env python3
"""Finite checks for the period-doubling binary lag-six difference lift.
All infinite assertions require the accompanying mathematical proof.
"""
from collections import Counter, deque

def subst(word):
    return ''.join('10' if a == '1' else '11' for a in word)

def phase_vectors(count=30):
    # T,H record the parity of substitution-word symbols by residue modulo six.
    T = [1, 0, 0, 0, 0, 0]  # tau_0 = '1'
    H = [0] * 6           # theta_0 = '0'
    result = []
    for n in range(count):
        s = pow(2, n, 6)
        result.append((s, tuple(T), tuple(H)))
        T, H = ([T[j] ^ H[(j-s) % 6] for j in range(6)],
                [T[j] ^ T[(j-s) % 6] for j in range(6)])
    return result

def prefix_map(state, s, parity):
    u = [(state >> j) & 1 for j in range(6)]
    return sum((u[(s+j) % 6] ^ parity[(s+j) % 6]) << j
               for j in range(6))

def orbits(permutations):
    unseen = set(range(64))
    partition = []
    while unseen:
        seed = min(unseen)
        orbit = {seed}
        queue = deque([seed])
        while queue:
            u = queue.popleft()
            for perm in permutations:
                v = perm[u]
                if v not in orbit:
                    orbit.add(v)
                    queue.append(v)
        partition.append(frozenset(orbit))
        unseen -= orbit
    return frozenset(partition)

def run():
    vec = phase_vectors()
    # Initial substitution words, tested independently of residue recurrence.
    tau = '1'; theta = '0'
    for n in range(11):
        s, T, H = vec[n]
        calc_T = tuple(sum(int(tau[k]) for k in range(j, len(tau), 6)) % 2 for j in range(6))
        calc_H = tuple(sum(int(theta[k]) for k in range(j, len(theta), 6)) % 2 for j in range(6))
        assert T == calc_T and H == calc_H and s == len(tau) % 6, n
        tau, theta = tau + theta, tau + tau
    for n in range(2, 26):
        assert vec[n] == vec[2 + (n-2) % 4], n
    assert vec[2][:2] == (4, (1,0,1,1,0,0))
    assert vec[4][:2] == (4, (1,0,1,0,0,1))
    p = tuple(prefix_map(u, *vec[2][:2]) for u in range(64))
    q = tuple(prefix_map(u, *vec[4][:2]) for u in range(64))
    assert sorted(p) == sorted(q) == list(range(64))
    groups = orbits([p,q])
    assert sorted(map(len, groups)) == [8, 8, 24, 24]
    def R(e):
        a,b,c = (e & 1), (e>>1)&1, (e>>2)&1
        return c + ((a^1)<<1) + ((b^1)<<2)
    assert all(R(R(R(e))) == e for e in range(8))
    expected = []
    unused = set(range(8))
    while unused:
        e = min(unused)
        E = {e, R(e), R(R(e))}
        unused -= E
        expected.append(frozenset(u for u in range(64)
                                  if sum(((u>>(2*j))&1)<<j for j in range(3)) in E))
    assert groups == frozenset(expected)
    # Directly test many cylinder returns independently of the phase recurrence.
    big = '1'
    for _ in range(16): big = subst(big)
    for n in (5, 6, 7, 8):
        w = '1'
        for _ in range(n): w = subst(w)
        w = w[:-1]
        starts = []
        pos = 0
        while (found := big.find(w, pos)) != -1:
            starts.append(found)
            pos = found + 1
        assert starts and starts[0] == 0
        residue_parity = [0]*6
        last = 0
        return_maps = []
        for t in starts:
            for k in range(last, t): residue_parity[k%6] ^= int(big[k])
            last=t
            s = t%6
            perm = tuple(prefix_map(u,s,tuple(residue_parity)) for u in range(64))
            return_maps.append(perm)
        assert orbits(return_maps) == groups, (n,len(starts))
        print(f'cylinder n={n}: {len(starts)} returns, 4 classes')
    print('PASS: substitution parity, four-periodicity, group orbits and independent cylinder returns')
    print('component fiber ranks:', sorted(map(len,groups)))

if __name__ == '__main__': run()
