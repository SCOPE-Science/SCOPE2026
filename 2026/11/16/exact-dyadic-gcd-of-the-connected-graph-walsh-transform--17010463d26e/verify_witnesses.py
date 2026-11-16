"""Check the short matching-complement sharpness witness family with exact integers.
This is a finite stress-test only; the manuscript proves all positive orders.
Run: python3 verify_witnesses.py
"""
from math import comb, factorial

def valuation2(z):
    if z == 0:
        return None
    return (abs(z) & -abs(z)).bit_length() - 1

for n in range(1, 201):
    L = n.bit_length() - 1
    t = n - (1 << L)
    d = n - 1 - L
    # For j disjoint positive edges, all other edges negative:
    # the only compatible vertex partitions are submatchings.
    values = [sum(comb(j, a) * (-1)**(n-a-1)
                  * factorial(n-a-1) * 2**a for a in range(j+1))
              for j in range(t+1)]
    assert all(x == 0 or valuation2(x) >= d for x in values)
    assert any(valuation2(x) == d for x in values)
    # Check partition-weight lower bound for every possible block number.
    for k in range(1,n+1):
        q,r = divmod(n,k)
        e_min = (k-r)*comb(q,2) + r*comb(q+1,2)
        val = k-1-(k-1).bit_count() + e_min
        assert val >= d
print("MATCHING_WITNESS_VALUATIONS_PASS orders=1..200")
