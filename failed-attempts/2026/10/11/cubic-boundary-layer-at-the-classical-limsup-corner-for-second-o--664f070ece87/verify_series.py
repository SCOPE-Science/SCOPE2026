from fractions import Fraction as F

N = 7

def add(a, b):
    return [(a[i] if i < len(a) else F(0)) + (b[i] if i < len(b) else F(0)) for i in range(N)]

def scale(a, c):
    return [c * (a[i] if i < len(a) else F(0)) for i in range(N)]

def mul(a, b):
    out = [F(0) for _ in range(N)]
    for i, ai in enumerate(a[:N]):
        for j, bj in enumerate(b[:N-i]):
            out[i+j] += ai * bj
    return out

def inv(a):
    assert a[0] != 0
    out = [F(0) for _ in range(N)]
    out[0] = 1 / a[0]
    for n in range(1, N):
        out[n] = -sum(a[k] * out[n-k] for k in range(1, min(n, len(a)-1)+1)) / a[0]
    return out

def log_series(a):
    assert a[0] == 1
    u = a[:]
    u[0] = F(0)
    out = [F(0) for _ in range(N)]
    p = [F(1)] + [F(0)] * (N-1)
    for k in range(1, N):
        p = mul(p, u)
        out = add(out, scale(p, F((-1)**(k+1), k)))
    return out

def shift_a(a):
    return [F(0)] + a[:N-1]

r = [F(1), F(1,2), F(3,8), F(1,3), F(125,384), F(27,80), F(16807,46080)]
s = [F(1), F(-1,2), F(3,8), F(-1,3), F(125,384), F(-27,80), F(16807,46080)]

eq_r = add(scale(log_series(r), F(2)), scale(shift_a(r), F(-1)))
eq_s = add(scale(log_series(s), F(2)), shift_a(s))
assert eq_r[:7] == [F(0)] * 7
assert eq_s[:7] == [F(0)] * 7

d = add(inv(s), scale(inv(r), F(-1)))
rs = mul(r, s)
irs = inv(rs)
h = add(scale(mul(d, d), F(2)), add(scale(irs, F(4)), [F(-2)] + [F(0)]*(N-1)))

assert d[:6] == [F(0), F(1), F(0), F(1,6), F(0), F(2,15)]
assert rs[:7] == [F(1), F(0), F(1,2), F(0), F(11,24), F(0), F(21,40)]
assert irs[:7] == [F(1), F(0), F(-1,2), F(0), F(-5,24), F(0), F(-23,120)]
assert h[:7] == [F(2), F(0), F(0), F(0), F(-1,6), F(0), F(-8,45)]

print("VERIFY_OK")
