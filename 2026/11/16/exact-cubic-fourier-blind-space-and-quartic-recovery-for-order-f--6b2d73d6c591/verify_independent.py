"""Independent monotone-triangle enumeration and modular Gram verification.

Requires Python 3 and NumPy. It constructs alternating-sign matrices by their
interlacing monotone triangles, not by row-by-row alternating-sign patterns.
"""
from itertools import product
from math import comb
import numpy as np

def from_triangles(n):
    answer = []
    def rec(chain):
        upper = chain[-1]
        if len(upper) == 1:
            rows = list(reversed(chain))
            previous = set()
            entries = []
            for row in rows:
                current = set(row)
                for j in range(n):
                    entries.append(int(j in current) - int(j in previous))
                previous = current
            answer.append(tuple(entries))
            return
        intervals = [range(upper[i], upper[i+1] + 1) for i in range(len(upper)-1)]
        for row in product(*intervals):
            if all(row[i] < row[i+1] for i in range(len(row)-1)):
                rec(chain + [row])
    rec([tuple(range(n))])
    return answer

def rank_field(a, prime):
    a = np.asarray(a, dtype=np.int64).copy() % prime
    n = a.shape[0]
    rank = 0
    for col in range(n):
        valid = np.flatnonzero(a[rank:, col])
        if valid.size == 0:
            continue
        pos = rank + int(valid[-1])
        a[[pos, rank]] = a[[rank, pos]]
        a[rank] = a[rank] * pow(int(a[rank, col]), -1, prime) % prime
        factors = a[rank+1:, col].copy()
        a[rank+1:] = (a[rank+1:] - factors[:, None] * a[rank]) % prime
        rank += 1
        if rank == n:
            break
    return rank

def main():
    expected = {2:2,3:7,4:42,5:429}
    for n,c in expected.items():
        rows = from_triangles(n)
        assert len(rows) == len(set(rows)) == c
    a=np.asarray(from_triangles(5),dtype=np.int8)
    overlap=np.count_nonzero(a[:,None,:]==a[None,:,:],axis=2)
    for d,r in [(3,425),(4,429)]:
        # A pair agrees on exactly binomial(overlap,k) value-specific
        # k-site cylinder indicators; their sum is the Gram product.
        gram=np.zeros((429,429),dtype=np.int64)
        for k in range(d+1):
            gram+=np.frompyfunc(lambda x: comb(int(x), k), 1,1)(overlap).astype(np.int64)
        assert rank_field(gram, 1009)==r
    print('PASS: independent monotone-triangle enumeration 429; ranks 425,429 modulo 1009')

if __name__=='__main__':main()
