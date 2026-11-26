from itertools import product

def weight(bits):
    return sum((1 if b else -1)*(1<<i) for i,b in enumerate(bits))

weight_cases = 0
for n in range(4,19):
    ws = [weight(bits) for bits in product((0,1), repeat=n)]
    assert len(ws) == 2**n
    assert len(set(ws)) == 2**n
    weight_cases += len(ws)

def exp_order(n, I, J):
    return n - len(J) + 2*len(J-I)

degeneration_pairs = 0
for n in range(4,10):
    subsets = []
    for mask in range(1<<n):
        subsets.append({i for i in range(n) if (mask>>i)&1})
    for I in subsets:
        base = exp_order(n,I,I)
        for J in subsets:
            gap = exp_order(n,I,J)-base
            assert gap == len(I-J)+len(J-I)
            assert (gap == 0) == (I == J)
            degeneration_pairs += 1

print('VERIFY_OK', weight_cases, degeneration_pairs)
