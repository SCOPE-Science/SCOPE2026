"""Exhaustive independent restrained-domination enumeration on M_(2n)."""
from collections import Counter


def profile(n):
    N = 2*n
    nbr = [((i-1)%N,(i+1)%N,(i+n)%N) for i in range(N)]
    # The three neighbors must be distinct for all n >= 3.
    assert all(len(set(a)) == 3 for a in nbr)
    result = Counter()
    for s in range(1 << N):
        valid = True
        for i in range(N):
            if not (s >> i) & 1:
                k = sum((s >> j) & 1 for j in nbr[i])
                if k == 0 or k == 3:
                    valid = False
                    break
        if valid:
            result[s.bit_count()] += 1
    return result


def target(n):
    if n % 4 == 2:
        return n//2, 4
    if n % 4 == 0:
        return n//2+1,n*n
    if n == 3:
        return 2,9
    return (n+1)//2,2*n


def main():
    for n in range(3,11):
        p=profile(n)
        minimum=min(p)
        count=p[minimum]
        assert (minimum,count)==target(n), (n,minimum,count,target(n))
        print(f'n={n} min={minimum} optima={count} all={sum(p.values())}')
    print('direct exhaustive verification PASSED')

if __name__=='__main__': main()
