"""Independent direct extension census for the three-distance ultrametric type spectrum.
Public scientific verification only. Standard-library Python 3.10+.
"""
from collections import defaultdict, Counter
from functools import lru_cache
from itertools import product
from math import ceil, log, pi

@lru_cache(None)
def partitions(n, smallest=1):
    if n == 0:
        return ((),)
    return tuple((j,) + tail for j in range(smallest, n+1)
                 for tail in partitions(n-j, j))

@lru_cache(None)
def hierarchies(n, min_cluster=()):
    if n == 0:
        return ((),)
    result = []
    for size in range(1, n+1):
        for cluster in partitions(size):
            if cluster < min_cluster:
                continue
            for tail in hierarchies(n-size, cluster):
                result.append((cluster,) + tail)
    return tuple(result)

def signature(h):
    # Each outer cluster is a radius-two ball; its entries are sizes of radius-one balls.
    level_one = Counter(a for outer in h for a in outer)
    level_two = Counter(sum(outer) for outer in h)
    n = sum(sum(outer) for outer in h)
    return (tuple(sorted(level_one.items())),tuple(sorted(level_two.items())), n)

def distance_matrix(h):
    n = sum(sum(outer) for outer in h)
    matrix = [[0 if i==j else 3 for j in range(n)] for i in range(n)]
    idx = 0
    for outer in h:
        start_outer = idx
        for size in outer:
            for i in range(idx,idx+size):
                for j in range(i+1,idx+size):
                    matrix[i][j] = matrix[j][i] = 1
            idx += size
        for i in range(start_outer,idx):
            for j in range(i+1,idx):
                if matrix[i][j] == 3:
                    matrix[i][j] = matrix[j][i] = 2
    assert idx==n
    return matrix

def direct_types(h):
    D = distance_matrix(h)
    n=len(D)
    pairs=[(i,j,D[i][j]) for i in range(n) for j in range(i+1,n)]
    counts=Counter()
    for f in product((1,2,3),repeat=n):
        if all(a<=max(b,d) and b<=max(a,d) and d<=max(a,b)
               for i,j,d in pairs for a,b in [(f[i],f[j])]):
            t=min(f)
            counts[t,sum(v==t for v in f)]+=1
    return counts

def predicted_types(h):
    cnt=Counter()
    for outer in h:
        cnt[2,sum(outer)] += 1
        for size in outer:
            cnt[1,size] += 1
    cnt[3,sum(sum(outer) for outer in h)]+=1
    return cnt

def check():
    total=0
    for n in range(1,9):
        H=hierarchies(n)
        sig=defaultdict(list)
        for h in H:
            s=signature(h)
            sig[s].append(h)
            if n <= 7:
                a,b=predicted_types(h),direct_types(h)
                assert a==b, (n,h,a,b)
                total+=1
        amb=[f for f in sig.values() if len(f)>1]
        print(f'order={n} isometry_types={len(H)} signatures={len(sig)} colliding_fibres={len(amb)} max_fibre={max(map(len,sig.values()))}')
        assert not amb if n<=4 else bool(amb)
        if n==5:
            assert len(amb)==1 and len(amb[0])==2
            print('first_collision=',amb[0], 'signature=',signature(amb[0][0]))
            assert set(amb[0]) == {((1,1),(1,2)),((1,1,1),(2,))}
    print('directly_verified_isometry_types=',total)
    # A finite numerical audit of the symbolic counting lower bound, not an asymptotic proof.
    n=1000000
    k=ceil(2*log(n,2))
    t=sum(range(2,k+2))
    m=n//t
    log_lower=m*log(n)-pi*(2*n/3)**0.5
    print(f'construction_example_n={n} k={k} t={t} m={m} lower_bound_log_fibre={log_lower:.1f}')
    assert 2**k>=n*n and log_lower>1000
    print('VERIFY_OK')

if __name__ == '__main__':
    check()
