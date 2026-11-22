"""Independent exhaustive ternary adjacent-pair reconstruction census, standard Python only."""
from collections import Counter
from itertools import product

expected = (3,9,27,69,135,207,273,345,423,507)
observed=[]
for n in range(1,11):
    buckets=Counter()
    for w in product(range(3),repeat=n):
        edges=[0]*9
        for k in range(n-1):
            edges[w[k]*3+w[k+1]] += 1
        buckets[(w[0],w[-1],*edges)]+=1
    observed.append(sum(m==1 for m in buckets.values()))
assert tuple(observed)==expected, observed
assert all(expected[n-1]==3*n*n+27*n-63 for n in range(6,11))
print('EXHAUSTIVE_PROFILE_CENSUS_1_THROUGH_10: PASS',observed)
