import cmath
import math


def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * math.log2(x) - (1.0 - x) * math.log2(1.0 - x)


def gp(p, q):
    d = math.sqrt(max(0.0, 1.0 - 4.0 * p * (1.0 - p) * q * q))
    return h2((1.0 + d) / 2.0)


def fp(p, q):
    return h2((1.0 - p) * q) - gp(p, q)


def qstar(p):
    lo, hi = 0.0, 1.0
    r = (math.sqrt(5.0) - 1.0) / 2.0
    x1 = hi - r * (hi - lo)
    x2 = lo + r * (hi - lo)
    f1, f2 = fp(p, x1), fp(p, x2)
    for _ in range(160):
        if f1 < f2:
            lo, x1, f1 = x1, x2, f2
            x2 = lo + r * (hi - lo)
            f2 = fp(p, x2)
        else:
            hi, x2, f2 = x2, x1, f1
            x1 = hi - r * (hi - lo)
            f1 = fp(p, x1)
    return (lo + hi) / 2.0


def out_det(p, q, zabs2):
    return (1.0 - p) * (q - (1.0 - p) * q * q - zabs2)


def entropy_from_det(det):
    d = math.sqrt(max(0.0, 1.0 - 4.0 * det))
    return h2((1.0 + d) / 2.0)


def check_balanced(p, weights, phases):
    q = qstar(p)
    ph = sum(w * cmath.exp(1j * t) for w, t in zip(weights, phases))
    assert abs(ph) < 2e-12
    avg_exc = q
    average_output_entropy = h2((1.0 - p) * avg_exc)
    letter_entropy = sum(w * gp(p, q) for w in weights)
    return average_output_entropy - letter_entropy, fp(p, q)


for p in (0.1, 0.3, 0.5, 0.8, 0.95):
    q = qstar(p)
    assert 0.0 < q < 1.0
    a = p * (1.0 - p)
    for u in (0.1, 0.3, 0.6, 0.9):
        qq = u
        d = math.sqrt(max(0.0, 1.0 - 4.0 * a * qq * qq))
        if d > 1e-9:
            sec = 4.0 * a / math.log(2.0) * (math.atanh(d) - d) / (d ** 3)
        else:
            sec = 4.0 * a / (3.0 * math.log(2.0))
        assert sec > 0.0
    pure_z2 = q * (1.0 - q)
    dpure = out_det(p, q, pure_z2)
    assert abs(dpure - p * (1.0 - p) * q * q) < 2e-14
    dmixed = out_det(p, q, 0.25 * pure_z2)
    assert dmixed > dpure
    assert entropy_from_det(dmixed) > entropy_from_det(dpure)

    for weights, phases in (
        ([0.5, 0.5], [0.0, math.pi]),
        ([1.0 / 3.0] * 3, [0.0, 2.0 * math.pi / 3.0, 4.0 * math.pi / 3.0]),
        ([0.25] * 4, [0.0, math.pi / 2.0, math.pi, 3.0 * math.pi / 2.0]),
    ):
        lhs, rhs = check_balanced(p, weights, phases)
        assert abs(lhs - rhs) < 2e-12

# A feasible nonuniform prior: 0.4, 0.3, 0.3 forms a triangle.
a, b, c = 0.4, 0.3, 0.3
# For b=c, symmetric angles +/-theta give resultant 2*b*cos(theta)=a.
theta = math.acos(a / (2.0 * b))
v = b * cmath.exp(1j * theta) + c * cmath.exp(-1j * theta)
# Rotate the two-vector resultant to oppose the longest side.
rot = cmath.exp(1j * (math.pi - cmath.phase(v)))
ph = a + rot * v
assert abs(ph) < 2e-12
assert max(a, b, c) <= 0.5
assert max(0.6, 0.2, 0.2) > 0.5

print('VERIFY_OK')
