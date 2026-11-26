"""Independent finite checks for the Proth-semigroup Wilf inequality.

Run: python3 verify.py
The infinite theorem relies on the proof, not finite enumeration.
"""
import heapq


def parameters(n, m):
    assert n >= 3 and m >= 3 and m % 2 and m < 2**n
    r = m.bit_length()-1
    k = n+r
    M = m*2**n
    return r, k, M


def greedy_sum(j, k):
    ans = 0
    for i in range(k, 0, -1):
        d, j = divmod(j, 2**i-1)
        ans += d
    assert j == 0
    return ans


def apery_by_dijkstra(n, m):
    r, k, M = parameters(n, m)
    a = M+1
    gens = [m*2**(n+i)+1 for i in range(k+1)]
    distances = [None]*a
    distances[0] = 0
    h = [(0, 0)]
    while h:
        dist, residue = heapq.heappop(h)
        if dist != distances[residue]:
            continue
        for gen in gens[1:]:
            res2 = (residue+gen)%a
            d2 = dist+gen
            if distances[res2] is None or d2 < distances[res2]:
                distances[res2] = d2
                heapq.heappush(h,(d2,res2))
    assert all(x is not None for x in distances)
    genus = sum(distances)//a-(a-1)//2
    frobenius = max(distances)-a
    return genus, frobenius, distances


def verify():
    tested = greedy_tested = 0
    sample = None
    for n in range(3, 8):
        for m in range(3, 2**n, 2):
            r,k,M=parameters(n,m)
            genus,frob,apery=apery_by_dijkstra(n,m)
            digit_sums=[greedy_sum(j,k) for j in range(M+1)]
            assert max(digit_sums) <= k+1
            assert M < 2*(2**k-1)
            for j in range(M+1):
                assert apery[(-j)%(M+1)] == digit_sums[j]*(M+1)+j*M
            expected_g = M*(M-1)//2+sum(digit_sums[1:])
            assert genus == expected_g
            c=frob+1
            e=k+1
            actual=e*(c-genus)-c
            bound=( (k-1)*M*M - (k+1)*(2*k+1)*M +2*k)//2
            assert c >= M*M+1
            assert genus <= M*(M-1)//2+(k+1)*M
            assert actual>=bound and bound>0
            assert 3*2**n>4*n+5
            tested += 1
            greedy_tested += M+1
            if n==3 and m==3: sample=(n,m,k,M,genus,frob,actual,bound)
    print('PASS:', tested, 'distinct semigroups,',greedy_tested,'Apéry-element comparisons')
    print('Sample (n,m,k,M,genus,F,Wilf-margin,certified lower bound):',sample)

if __name__ == '__main__':
    verify()
