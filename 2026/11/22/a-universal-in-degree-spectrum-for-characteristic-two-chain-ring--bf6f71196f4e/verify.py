"""Direct forward-map fiber enumeration for a characteristic-two Vieta map.
Run: python verify.py. No external dependencies.
"""
from collections import Counter

def field_mul(a, b, f):
    # GF(2^f) via irreducible polynomials x+1, x^2+x+1, x^3+x+1.
    primitive = {1: 0b11, 2: 0b111, 3: 0b1011}[f]
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & (1 << f):
            a ^= primitive
    return out

def multiply(a, b, f, k):
    q = 1 << f
    ac = [(a >> (f*i)) & (q-1) for i in range(k)]
    bc = [(b >> (f*i)) & (q-1) for i in range(k)]
    rc = [0] * k
    for i, x in enumerate(ac):
        if x:
            for j in range(k-i):
                if bc[j]:
                    rc[i+j] ^= field_mul(x, bc[j], f)
    return sum(c << (f*i) for i,c in enumerate(rc))

def theoretical(q, k):
    h = (k+1)//2
    counts = Counter()
    for v in range(h):
        degree = 2*q**v
        counts[degree] += (q-1)*q**(2*k-2*v-1)//2
    counts[q**(k//2)] += q**k
    counts[0] = q**(2*k) - sum(counts.values())
    assert sum(degree*number for degree,number in counts.items()) == q**(2*k)
    return counts

def verify(f, k):
    q = 2**f
    size = q**k
    target = Counter()
    # Completely independent forward image enumeration, not kernel counts.
    for a in range(size):
        for b in range(size):
            s = a ^ b
            p = multiply(a,b,f,k)
            target[s*size+p] += 1
    hist = Counter(target.values())
    hist[0] = size*size-len(target)
    expected = theoretical(q,k)
    assert hist == expected, f'MISMATCH q={q},k={k}: observed={hist}, predicted={expected}'
    assert sum(hist.values()) == size*size
    print(f'q={q}, k={k}, indegrees={sorted(hist.items())}, OK')

if __name__ == '__main__':
    for k in range(1, 10):
        verify(1,k)
    for k in range(1, 5):
        verify(2,k)
    for k in range(1, 4):
        verify(3,k)
    print('VERIFY_OK')
