"""Independent direct prefix/morphism test of factor and aligned-window counts.

This is finite experimental cross-checking, not a substitute for the
all-length combinatorial and Chinese-remainder proofs.
"""

def deficiency(n):
    if n == 1: return 0
    a = 1 << (n.bit_length() - 1)
    return max(a//2, n-a)

def expected(q, n):
    return q*n-deficiency(n)

def oddpart(n):
    while n%2==0:
        n//=2
    return n

def main():
    n_checks = 0
    w_checks = 0
    for q in range(2, 7):
        word = bytes([0])
        while len(word) < (1 << 15):
            out = bytearray()
            for a in word:
                out.extend((0, (a+1)%q))
            word = bytes(out)
        for length in range(1, 25):
            fact = {word[i:i+length] for i in range(len(word)-length+1)}
            windows = {word[i:i+length] for i in range(0,len(word)-length+1,length)}
            assert len(fact) == expected(q, length), (q,length,'factor',len(fact),expected(q,length))
            assert len(windows) == expected(q,oddpart(length)), (q,length,'window',len(windows),expected(q,oddpart(length)))
            n_checks += 1
            w_checks += 1
    print(f'PASS: {n_checks} direct prefix factor-cardinality checks (q=2..6, n=1..24).')
    print(f'PASS: {w_checks} direct disjoint aligned-window checks (same parameters).')
    print('Each q generated via its independent uniform morphism to length 32768.')

if __name__=='__main__':
    main()
