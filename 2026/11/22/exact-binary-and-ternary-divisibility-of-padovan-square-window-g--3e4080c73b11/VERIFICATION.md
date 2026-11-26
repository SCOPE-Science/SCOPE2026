---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the squared sequence u_n, the characteristic multipliers are squares and pairwise products of the roots of X³−X−1. The products are reciprocal roots; the corresponding cubics are X³+X²−1 for the products and X³−2X²+X−1 for the squares. Their product Q is a monic integer annihilator of u and of the windows, with Q(1)=−1. The one-step difference of the windows is u_(n+k)−u_n; conversely if this difference vanishes mod m, the windows are constant, and applying Q makes that constant vanish because Q(1) is a unit. So m divides G(k) iff k is a period mod m. The first six windows determine the infinite gcd. The invertible state matrix A satisfies A³=A+I; reducing powers in this basis gives A⁷=I+2(A²+A), A¹³=I+3H, A¹⁴=I+4H, with H=3A²+4A+2I. At 2 the prime base period is seven by nonconstancy and A⁷≡I mod 2; equal parity gives the same period mod 4. The witness u_10−u_3=140 excludes shift seven mod 8, while shift fourteen works. At shifts 7·2^s m (s≥1, m odd), successive squaring and the binomial expansion give A^shift≡I+2^(s+1)mH mod 2^(s+2). Squaring the coordinate difference adds one level exactly at n=0 because H≡A² mod 2 and both P_0 and P_2 are odd. At 3 the prime base period is thirteen by nonconstancy; for shifts 13·3^s m, 3∤m, the lift is I+3^(s+1)mH mod 3^(s+2), so the squared difference has a sharp witness at n=2, as H≡A+2I mod 3 and P_2(P_3+2P_2)≡1 mod 3. These witnesses give the exact period lifts and valuations for all k,r≥1. Separately I generated the true modular state orbits until return and found each square word's least period with a prefix algorithm. All periods agree for binary r≤11 and ternary r≤8; direct integer gcds of six windows agree at both primes for k≤1000. Those finite checks corroborate rather than replace the lifting proof.

## originality

PASS

The exact seven-term square identity is already recorded, and the binary answer is a short consequence of prior dyadic state lifts plus a square-cancellation and low-precision witness check. These ingredients are not separate originality credits. The reviewed distinct result is the precise two-prime square-window law, notably the sharp all-precision ternary square period and its exact contrast with dyadic cancellation. No inspected prior statement or domination supplied this combined conclusion.

## value

PASS

The standard-seed Padovan recurrence and first two primes give a natural controlled comparison of divisibility in squared windows. Exact GCD exponents across all lengths make the claims usable as arithmetic invariants, not just individual modular coincidences. The sharp ternary witnesses and the contrast with the lost binary lifting level add information beyond the prior dyadic state census and the known square relation. The value is this exact local comparison, not a claim to the full gcd factorization or a new general lifting technique.

The dated certificate retains the supplied scientific assessment, sources and limitations.
