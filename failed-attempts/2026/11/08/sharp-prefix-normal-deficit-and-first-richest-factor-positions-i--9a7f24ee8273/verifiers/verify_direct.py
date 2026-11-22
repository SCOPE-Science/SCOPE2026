"""Direct finite checks of factor extremizers in the period-doubling word."""

def morph(w):
    return ''.join('01' if c == '0' else '00' for c in w)

w = '0'
while len(w) < (1 << 15):
    w = morph(w)
pref = [0]
for c in w:
    pref.append(pref[-1] + (c == '1'))

lo = [0, 0]
hi = [0, 1]
for n in range(2, 513):
    if n % 2 == 0:
        k = n // 2
        hi.append(k - lo[k])
        lo.append(k - hi[k])
    else:
        k = n // 2
        hi.append(k + 1 - lo[k + 1])
        lo.append(k - hi[k])

for n in range(1, 513):
    vals = [pref[i+n] - pref[i] for i in range(len(w)-n+1)]
    assert (min(vals), max(vals)) == (lo[n], hi[n]), (n, lo[n], hi[n], min(vals), max(vals))

for j in range(1, 8):
    n = (4**j - 1) // 3
    vals = [pref[t+n] - pref[t] for t in range(n+1)]
    assert vals[n] == max(vals)
    assert vals.count(max(vals)) == 1
    assert vals[n] == hi[n] if n <= 512 else vals[n] == (n + 2*j)//3
    assert pref[n] == (n - j)//3
    assert vals[n] - pref[n] == j
print('DIRECT_OK extrema n=1..512, special positions j=1..7, length', len(w))
