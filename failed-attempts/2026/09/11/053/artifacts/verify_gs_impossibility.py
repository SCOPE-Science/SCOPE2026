"""Verify the all-m GS-count impossibility lemma for the (48,12,l=2,T=32) window.
Claim: for every multiplicity m>=1, with (1,11)-weighted degree bound D=32m-1,
  DOF(D) = sum_{j: 11j<=D} (D-11j+1)  <  C = 48*m*(m+1) = n*l*m(m+1)/2.
Hence no uniform-multiplicity GS interpolation polynomial is guaranteed at T=32.
Proof strategy checked here:
  (1) closed form DOF = (32m+10-r)(32m+1+r)/22 with r=(32m-1)%11, exact for m=1..5000;
  (2) 22*(C-DOF) = 32m^2+704m-(10-r)(1+r), with (10-r)(1+r)<=30 for r in 0..10;
  (3) 32m^2+704m-30 > 0 for all m>=1 (holds at m=1, increasing in m).
Stdlib only. Prints VERIFY_OK on success.
"""
import sys

N, K, L_IN, T = 48, 12, 2, 32
KM1 = K - 1  # 11


def dof_bruteforce(D):
    s, j = 0, 0
    while D - KM1 * j >= 0:
        s += D - KM1 * j + 1
        j += 1
    return s


def check_closed_form(mlo=1, mhi=5000):
    for m in range(mlo, mhi + 1):
        D = T * m - 1
        r = D % KM1
        J = D // KM1
        assert D == KM1 * J + r and 0 <= r <= 10
        dof = dof_bruteforce(D)
        closed = (32 * m + 10 - r) * (32 * m + 1 + r)
        assert closed % 22 == 0, (m, closed)
        assert dof == closed // 22, (m, dof, closed // 22)
        C = N * L_IN * m * (m + 1) // 2
        assert dof < C, (m, dof, C)
        gap22 = 22 * (C - dof)
        ident = 32 * m * m + 704 * m - (10 - r) * (1 + r)
        assert gap22 == ident, (m, gap22, ident)
    return True


def check_residue_bound():
    assert max((10 - r) * (1 + r) for r in range(11)) == 30
    # r(m) relation: 32 = 10 mod 11 so r = (10m-1) mod 11
    for m in range(1, 2000):
        assert (32 * m - 1) % 11 == (10 * m - 1) % 11
    # base + monotonicity: positive at m=1 and strictly increasing in m
    assert 32 + 704 - 30 > 0
    return True


def main():
    check_residue_bound()
    check_closed_form(1, 5000)
    # spot values for the record
    for m in (1, 2, 3, 11, 100):
        D = T * m - 1
        print(f"m={m}: D={D} DOF={dof_bruteforce(D)} C={N * L_IN * m * (m + 1) // 2}")
    print("VERIFY_OK: DOF(32m-1) < 48m(m+1) for all checked m (1..5000); "
          "analytic identity + residue bound extend to all m>=1.")


if __name__ == "__main__":
    sys.exit(main())
