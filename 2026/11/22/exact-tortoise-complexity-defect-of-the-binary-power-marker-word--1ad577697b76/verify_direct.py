"""Independent finite-window factor and one-step tortoise-image checks."""

def tortoise(word):
    chunks = word.split('1')
    number_of_ones = len(chunks) - 1
    if not number_of_ones:
        return word
    output = chunks[0] + chunks[1]
    for chunk in chunks[2:]:
        output += '1' + chunk
    return output + '1'

def marker_prefix(length):
    w = ['0'] * length
    j = 0
    while (1 << j) - 1 < length:
        w[(1 << j) - 1] = '1'
        j += 1
    return ''.join(w)

def predict(n):
    if n == 1:
        return (2, 2)
    k = n.bit_length() - 1
    rich = min(n - (1 << (k - 1)), 1 << k)
    return (n + 1 + rich, 2 + rich)

factor_tests = 0
max_n = 160
for n in range(1, max_n+1):
    # Markers from 2^j-1, through a prefix exceeding 16 n. Beyond that
    # threshold, all length-n windows contain at most one 1.
    p = marker_prefix(16*n+1)
    factors = {p[i:i+n] for i in range(len(p)-n+1)}
    images = {tortoise(w) for w in factors}
    expected = predict(n)
    actual = (len(factors), len(images))
    if actual != expected:
        raise AssertionError((n,actual,expected))
    assert all(len(tortoise(w)) == n and tortoise(w).count('1') == w.count('1') for w in factors)
    assert sum(w.count('1') == 1 for w in factors) == n
    assert len({tortoise(w) for w in factors if w.count('1') >= 2}) == sum(w.count('1') >= 2 for w in factors)
    factor_tests += len(factors)
print(f'PASS: n=1..{max_n}; {factor_tests} distinct factor instances; exact ordinary and tortoise counts; all nontrivial fibers')
