"""Independent exhaustive checks for defective colourings of matching-deleted cliques.
Only Python standard library is required: python verify.py
"""
from itertools import product
from math import factorial, comb


def count_by_definition(n, t, k, d):
    # Deleted edges are (0,1), (2,3), ..., (2*t-2,2*t-1).
    adjacency = [[i != j and not (i // 2 == j // 2 and i < 2*t)
                  for j in range(n)] for i in range(n)]
    ans = 0
    for col in product(range(k), repeat=n):
        if all(sum(adjacency[v][w] and col[w] == col[v]
                   for w in range(n)) <= d for v in range(n)):
            ans += 1
    return ans


def bounded_fibre_count(N, k, maxsize):
    # Counts named-colour maps on N labelled vertices with fibres <= maxsize.
    # Dynamic programming allocates a new colour class of size j at each step.
    dp = [0] * (N+1)
    dp[0] = 1
    for _ in range(k):
        new = [0] * (N+1)
        for a, val in enumerate(dp):
            if not val: continue
            for j in range(min(maxsize, N-a)+1):
                new[a+j] += val * comb(N-a, j)
        dp = new
    return dp[N]


def count_by_formula(n, t, k, d):
    if d % 2:
        return bounded_fibre_count(n, k, d+1)
    s = (d+2)//2
    total = 0
    for r in range(min(t//s, k)+1):
        distributed_pairs = factorial(t)//(factorial(t-r*s)*factorial(s)**r)
        total += comb(k,r) * distributed_pairs * bounded_fibre_count(n-2*r*s, k-r, d+1)
    return total


def main():
    total = 0
    for n in range(2,9):
        for t in range(n//2+1):
            for d in range(n+1):
                for k in range(1,5):
                    actual = count_by_definition(n,t,k,d)
                    predicted = count_by_formula(n,t,k,d)
                    assert actual == predicted, (n,t,k,d,actual,predicted)
                    total += 1
        print('FULL_GRAPH_CHECK_OK',n)
    print('DIRECT_COLOURING_PROFILES_OK',total)
    # Parity and exact-degree leading coefficient, via finite differences in k.
    # The proof, not these finite tests, establishes unrestricted results.
    for n in range(4,11):
        for t in range(n//2+1):
            for d in range(n):
                values = [count_by_formula(n,t,k,d) - count_by_formula(n,0,k,d)
                          for k in range(n+2)]
                if d % 2 == 1 or t < (d+2)//2:
                    assert not any(values), (n,t,d,values)
                elif d % 2 == 0:
                    degree = n-d-1
                    differences = values[:]
                    for _ in range(degree):
                        differences = [b-a for a,b in zip(differences,differences[1:])]
                    assert differences[0] == factorial(degree)*comb(t,(d+2)//2), (n,t,d,differences[0])
    print('PARITY_AND_LEADING_COEFFICIENT_CHECK_OK')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
