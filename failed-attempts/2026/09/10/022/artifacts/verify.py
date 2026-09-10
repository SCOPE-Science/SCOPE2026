"""Auditable checks for lane-551 consolidation (stdlib only).

Checks:
  A. Normalized traces and 1/4-gap arithmetic: 5/18 + 1/4 = 19/36 < 20/36 = 10/18.
  B. Chern-ring computation for literal sum bundle E = L1+L2+L3+theta^2:
     c(E) = prod(1+u_i), u_i^2 = 0  =>  c(E)^{-1} = 1 - s1 + s2 - s3 exactly
     (no terms above degree 6), so no c_k (k>=6) contradiction with a rank-5
     complement: the literal Euler obstruction FAILS.
  C. Tensor-line alternative: (sum u)^6 != 0 over 6 coords (stage-2 obstruction OK),
     but stage-3 count: 12 coords vs complement rank 15 -> (sum u)^16 = 0 (wash-out).
"""
from fractions import Fraction
from itertools import combinations


def check_gap():
    tauP = Fraction(5, 18)
    tauQ = Fraction(10, 18)
    r = Fraction(1, 4)
    lhs = tauP + r
    assert lhs == Fraction(19, 36), lhs
    assert tauQ == Fraction(20, 36), tauQ
    assert lhs < tauQ
    print(f"GAP_OK: tauP=5/18 tauQ=10/18 tauP+1/4={lhs} < {tauQ}=tauQ")


class Trunc3:
    """Cohomology (truncated polynomial) ring Z[u1,u2,u3]/(u_i^2), degree <= 6."""

    def __init__(self, d=None):
        self.d = dict(d or {})

    def __add__(self, o):
        d = dict(self.d)
        for k, v in o.d.items():
            d[k] = d.get(k, 0) + v
            if d[k] == 0:
                del d[k]
        return Trunc3(d)

    def __neg__(self):
        return Trunc3({k: -v for k, v in self.d.items()})

    def __sub__(self, o):
        return self + (-o)

    def __mul__(self, o):
        if isinstance(o, int):
            return Trunc3({k: v * o for k, v in self.d.items() if v * o != 0})
        return self._mul(o)

    def __rmul__(self, o):
        return self.__mul__(o)

    def _mul(self, o):
        d = {}
        for a, va in self.d.items():
            for b, vb in o.d.items():
                if set(a) & set(b):
                    continue  # u_i^2 = 0
                k = tuple(sorted(set(a) | set(b)))
                d[k] = d.get(k, 0) + va * vb
        return Trunc3({k: v for k, v in d.items() if v != 0})

    def deg(self, k):
        return 2 * len(k)

    def __eq__(self, o):
        return self.d == o.d

    def __repr__(self):
        return f"Trunc3({self.d})"


def one():
    return Trunc3({(): 1})


def u(i):
    return Trunc3({(i,): 1})


def check_chern_sum_bundle():
    u1, u2, u3 = u(1), u(2), u(3)
    cE = (one() + u1) * (one() + u2) * (one() + u3)
    s1 = u1 + u2 + u3
    s2 = u1 * u2 + u1 * u3 + u2 * u3
    s3 = u1 * u2 * u3
    assert cE == one() + s1 + s2 + s3, cE
    # relations
    assert s1 * s1 == s2 + s2, s1 * s1            # s1^2 = 2 s2
    assert s1 * s1 * s1 == s3 * 6, s1 * s1 * s1  # s1^3 = 6 s3
    assert s1 * s2 == s3 * 3, s1 * s2            # s1 s2 = 3 s3
    # inverse: (1+s1+s2+s3)^{-1} = 1 - s1 + s2 - s3 (verify by multiplication = 1)
    cF = one() - s1 + s2 - s3
    assert cE * cF == one(), cE * cF
    # highest degree present is 6 (k=3 <= 5 = complement rank): no obstruction
    top = max((len(k) for k in cF.d), default=0)
    assert top == 3, top
    print("CHERN_SUM_OK: c(E)^{-1} = 1-s1+s2-s3, max k=3 <= 5 -> no c_k obstruction;"
          " literal Euler log FAILS (as claimed in worklog)")


def power_sum_nonzero(nvars, p):
    """Coefficient of u_{i1}...u_{ip} in (u_1+...+u_n)^p is p! if p <= n else 0."""
    from math import factorial
    if p <= nvars:
        return factorial(p)
    return 0


def check_tensor_washout():
    c6_stage2 = power_sum_nonzero(6, 6)   # 720 != 0 -> stage-2 tensor obstruction present
    assert c6_stage2 == 720 and c6_stage2 != 0
    c16_stage3 = power_sum_nonzero(12, 16)  # 0 -> stage-3 wash-out
    assert c16_stage3 == 0
    print(f"WASHOUT_OK: stage2 s^6 coeff={c6_stage2} (obstructs rank-5 complement);"
          f" stage3 s^16 coeff={c16_stage3} (12 coords < 16 -> washed out)")


if __name__ == "__main__":
    check_gap()
    check_chern_sum_bundle()
    check_tensor_washout()
    print("VERIFY_OK")
