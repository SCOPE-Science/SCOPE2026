from collections import deque
import itertools, time

def rt_bfs(a, b):
    n = len(a)
    full = (1 << n) - 1
    # precompute images under a,b for all masks? 2^n=256, cheap
    dist = [-1] * (1 << n)
    dist[full] = 0
    dq = deque([full])
    # image function via bit tricks with precomputed per-state bits
    while dq:
        s = dq.popleft()
        if s & (s - 1) == 0:
            return dist[s]
        # image under a
        t1 = 0; m = s
        while m:
            lsb = m & (-m)
            q = lsb.bit_length() - 1
            t1 |= (1 << a[q])
            m ^= lsb
        if dist[t1] < 0:
            dist[t1] = dist[s] + 1
            dq.append(t1)
        t2 = 0; m = s
        while m:
            lsb = m & (-m)
            q = lsb.bit_length() - 1
            t2 |= (1 << b[q])
            m ^= lsb
        if dist[t2] < 0:
            dist[t2] = dist[s] + 1
            dq.append(t2)
    return None

def fiber_exhaust(a):
    n = len(a)
    da = [0]*n
    for q in range(n):
        da[q] += 0
    indeg_a = [0]*n
    for q in range(n):
        indeg_a[a[q]] += 1
    need = [2 - indeg_a[q] for q in range(n)]
    # slots: multiset of targets with multiplicity need[q]
    slots = []
    for q in range(n):
        slots.extend([q]*need[q])
    assert len(slots) == n
    best = -1
    best_b = None
    count = 0
    sync_count = 0
    from math import factorial
    # enumerate distinct permutations of multiset via itertools.permutations + set? 8!/2=20160 distinct; permutations gives 40320 with dup. Use more-itertools style distinct permutations:
    t0 = time.time()
    for perm in set(itertools.permutations(slots)):
        count += 1
        r = rt_bfs(a, perm)
        if r is not None:
            sync_count += 1
            if r > best:
                best = r
                best_b = perm
    dt = time.time() - t0
    return best, best_b, count, sync_count, dt

if __name__ == '__main__':
    a = (1,2,3,4,5,0,7,7)
    best, best_b, count, sync_count, dt = fiber_exhaust(a)
    print("fiber size:", count, "sync:", sync_count, "max rt:", best, "b:", best_b, "time:", round(dt,2))
