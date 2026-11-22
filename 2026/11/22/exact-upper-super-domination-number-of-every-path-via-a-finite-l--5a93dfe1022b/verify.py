#!/usr/bin/env python3
"""Independent finite-state certificate for the upper super-domination number of paths."""
from collections import deque
from itertools import product

BOUNDARY = '#'
BLOCK = (0, 0, 1, 0, 1, 0, 0)
TAILS = ((), (1,), (0,1), (0,0,1), (0,1,1,0), (0,0,1,1,0), (0,0,1,0,1,0))


def private_witness(w, j):
    if w[j] != 1:
        return True
    for k in (j-1, j+1):
        if 0 <= k < len(w) and w[k] == 0:
            other = 2*k-j
            if not (0 <= other < len(w)) or w[other] == '#':
                return True
            if w[other] == 0:
                return True
    return False


def valid_center(window):
    assert len(window) == 9
    if window[4] == '#':
        return True
    if window[4] == 1:
        return private_witness(window, 4)
    changed = list(window)
    changed[4] = 1
    return any(changed[j] == 1 and not private_witness(changed, j)
               for j in (2,3,4,5,6))


def path_is_maximal_open_irredundant(bits):
    n = len(bits)
    def oi(a):
        return all(any(0 <= v < n and a[v] == 0 and
                       (not 0 <= 2*v-u < n or a[2*v-u] == 0)
                       for v in (u-1,u+1)) for u in range(n) if a[u] == 1)
    if not oi(bits):
        return False
    return all(not oi(bits[:i] + (1,) + bits[i+1:])
               for i in range(n) if bits[i] == 0)


def super_dom(S):
    n = len(S)
    for u in range(n):
        if S[u]:
            continue
        if not any(0 <= v < n and S[v] and
                   all(not (0 <= w < n and not S[w]) or w == u for w in (v-1, v+1))
                   for v in (u-1, u+1)):
            return False
    return True


def path_is_minimal_super_dom(S):
    if not super_dom(S): return False
    for i, b in enumerate(S):
        if b:
            T = S[:i] + (0,) + S[i+1:]
            if super_dom(T):return False
    return True


def append(st, a):
    seq = st + (a,)
    if len(seq) >= 9 and not valid_center(seq[-9:]):
        return None
    return seq[-8:]


def terminate(st):
    for _ in range(4):
        st = append(st, '#')
        if st is None:return False
    return True


def certificate():
    start = (('#',)*4, 0)
    ids = {start:0}; states=[start]; queue=deque([start]); edges=[]
    while queue:
        state = queue.popleft()
        st, phase=state
        for bit in (0,1):
            nxt = append(st, bit)
            if nxt is None:continue
            new=(nxt,min(phase+1,2))
            if new not in ids:
                ids[new]=len(states)
                states.append(new)
                queue.append(new)
            edges.append((ids[state], ids[new], 7*bit-2))
    sink=len(states)
    for state in states:
        if state[1]>=2 and terminate(state[0]):
            edges.append((ids[state], sink, 0))
    assert (len(states),len(edges),sum(v==sink for _,v,_ in edges)) == (232,403,58)
    INF=10**30
    ds=[INF]*(sink+1)
    ds[0]=0
    for _ in range(sink+1):
        changed=False
        for u,v,w in edges:
            if ds[u]!=INF and ds[v]>ds[u]+w:
                ds[v]=ds[u]+w;changed=True
        if not changed:break
    else:raise AssertionError('reachable negative cycle or unverified potential')
    assert ds[sink]==0
    assert all(ds[u]==INF or ds[v]<=ds[u]+w for u,v,w in edges)
    assert all(v < sink or w==0 for u,v,w in edges)
    print('BELLMAN_FORD_CERTIFICATE_PASS states=233 edges=403 termination_edges=58 minimum_cost=0')


def constructive():
    for r in range(7):
        for q in range(0,5):
            bits=BLOCK*q+TAILS[r]
            if len(bits)<2: continue
            assert sum(bits)==(2*len(bits)+6)//7
            assert path_is_maximal_open_irredundant(bits), (q,r)
            p=('#',)*4+bits+('#',)*4
            assert all(valid_center(p[k:k+9]) for k in range(len(p)-8))
        # No new length-9 local factors can appear beyond q=3; periodic block has length 7,
        # and the two fixed ends affect windows only within distance four of each end.
        reference=set()
        for q in range(3,5):
            b=('#',)*4+BLOCK*q+TAILS[r]+('#',)*4
            reference.update(b[k:k+9] for k in range(len(b)-8))
        for q in range(5,9):
            b=('#',)*4+BLOCK*q+TAILS[r]+('#',)*4
            factors={b[k:k+9] for k in range(len(b)-8)}
            assert factors <= reference
    print('SEVEN_RESIDUE_CONSTRUCTION_PASS block=0010100 tails=1,01,001,0110,00110,001010')


def independent_small_cases():
    num=0
    for n in range(2,14):
        maxS=-1
        for bits in product((0,1),repeat=n):
            opt=path_is_maximal_open_irredundant(bits)
            asserted=path_is_minimal_super_dom(tuple(1-b for b in bits))
            assert opt==asserted,(n,bits)
            if opt:maxS=max(maxS,n-sum(bits))
            num+=1
        assert maxS==5*n//7, (n,maxS)
    print('INDEPENDENT_DIRECT_GRAPH_CHECK_PASS n=2..13 cases=',num)

if __name__=='__main__':
    independent_small_cases()
    constructive()
    certificate()
    print('VERIFY_OK')
