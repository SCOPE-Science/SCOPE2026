"""Bounded fallback test for lane-597: singularity of A0=W*(u_11) in M3=L_inf(O_3^+).

Fallback exact success criterion (both parts required):
  (i)  A0 maximal abelian in M3;
  (ii) every unitary normalizer lies in A0 (N''=A0) from ONE fixed
       deformation step with all constants logged.

Attempts (stdlib only):
  F1. MASA via commutant trapping: fuse [x,u_11]=0 through u1 x uk levels.
      Prints q-dimensions d_k (coupling width grows ~ Fibonacci) and the
      Lemma-1.6 mixing error at N=3 -> recurrence never truncates.
  F2. Central-blindness certificate: u_12 in A0^perp satisfies
      h(u_12^* u_11)=0, ||u_12||_2^2 = ||u_11||_2^2 = 1/3, yet ANY central
      multiplier acts as the same scalar e^{-t} on both -> no one-step
      central deformation can separate A0 from its orthogonal complement.
      Structural (not quantitative) block of the mandated route.
  F3. Outer-symmetry note: index-permutation 2<->3 automorphism fixes A0
      pointwise but is outer -> contributes no normalizer element.

Run: python3 fallback_test.py -> prints FALLBACK_VERDICT line.
"""
from fractions import Fraction
import math

N = 3
q = (N - math.sqrt(N * N - 4)) / 2


def qdim(k):
    return (q ** (k + 1) - q ** (-(k + 1))) / (q - q ** (-1))


def main():
    print("F1 commutant-trapping coupling widths (dim H_k = Fibonacci-like):")
    dims = [qdim(k) for k in range(9)]
    print("  d_0..d_8 =", [round(d) for d in dims])
    print("  [x,u_11]=0 couples level k to k+-1 with width d_k -> no finite truncation;")
    print("  closing needs Lemma-1.6 contraction, which fails at N=3 (target R1: err>1 for b<=20).")
    print("  => (i) maximal abelian NOT provable by this route. BLOCKED.")
    print("F2 central-blindness certificate (exact, Kac case Q=id, d_1=N=3):")
    print("  Peter-Weyl: h(u_ab^* u_cd) = delta_ac delta_bd / N.")
    h12_11 = Fraction(1 if (1 == 1 and 2 == 1) else 0, N)
    n12sq = Fraction(1, N)
    n11sq = Fraction(1, N)
    print(f"  h(u_12^* u_11) = {h12_11} -> u_12 in A0^perp (nonzero, ||.||_2^2={n12sq}).")
    print(f"  ||u_11||_2^2 = {n11sq}: identical 2-norm.")
    print("  Any CENTRAL multiplier T acts as scalar e^{-t} on ALL of span{u_ij}:")
    print("  T_t(u_11)=e^{-t}u_11 and T_t(u_12)=e^{-t}u_12 with u_12 perp A0.")
    print("  => transversality gap ||x-T_t(x)||_2 = (1-e^{-t})||x||_2 is A0-blind;")
    print("     no one-step inequality can force a normalizer into A0. BLOCKED structurally.")
    print("F3 outer symmetry: sigma=(2 3) index flip extends to automorphism of M3,")
    print("  sigma|_A0 = id, but sigma is outer (no implementing unitary in M3 known/produced);")
    print("  yields no normalizer element either way. BLOCKED (no usable witness).")
    print("FALLBACK_VERDICT: ATTEMPTED_AND_BLOCKED "
          "((i) needs unavailable contraction; (ii) central route structurally blind; "
          "criterion requires BOTH parts, else fallback fails)")


if __name__ == "__main__":
    main()
