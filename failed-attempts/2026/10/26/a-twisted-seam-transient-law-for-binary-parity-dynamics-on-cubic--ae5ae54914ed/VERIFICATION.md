---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For the stated distinct open neighbors the ladder multiplies by z⁻¹(1+z²+z^(n+1)) modulo z^(2n)+1. At modulus roots only Φ=z²+z+1 can divide the numerator, and precisely if 3 divides n. Its exponent in the modulus is 2k; the numerator has exponent one for even n by its ordinary derivative and exactly two for odd n by the second Hasse derivative, which at a primitive cube root is either 1 or the root itself. On the prism, B²=(Φ/z)²I and local Smith factors (1,(Φ/z)²) give binary kernel dimensions 4 min(2r,k) at time 2r and 2[min(2r,k)+min(2r+2,k)] at 2r+1. These reduce to the claimed parity-specific growth and sharp entry times. The nilpotent part is 4k-dimensional in both graphs when present; its complement is invertible and recurrent, so each specified recurrent state has a fibre of cardinality 2^(4k) at a fixed sufficiently late time. For ladder fixed points, multiplying F^r−I by the unit z^r gives the stated gcd; divisor inversion counts primitive cycles. Independent direct finite-state checks at n=3 and 6 verified the odd and even shell distributions. Invertibility was checked at n=4,5 and the ladder gcd formula was checked by direct fixed-state counts for 3≤n≤6 and 1≤r≤8. The all-size conclusions come from the algebra, not the finite checks.

## originality

FAIL

The published Resultary result 812449181a9b covers the same open-neighbor maps, including the prism–Möbius seam comparison, and gives the nilpotent Jordan partitions for both. It also states exactly the Möbius fixed-power gcd and primitive-cycle inversion, and goes further with explicit special cases. The frozen cumulative formulas and stable fibre counts follow from the matching partitions. This is demonstrable coverage by a distinct record, not a claim about which was proved first.

## value

FAIL

Comparing nilpotent chains under a crossed seam is a motivated problem. Here, however, the same opposite odd/even transient response and every claimed dynamical invariant are already supplied by or mechanically implied by the stronger comparison of these exact maps. Repackaging Jordan data as cumulative counts or fixed-time fibre sizes does not leave a distinct scientific contribution to accept.

The dated certificate retains the supplied scientific assessment, sources and limitations.
