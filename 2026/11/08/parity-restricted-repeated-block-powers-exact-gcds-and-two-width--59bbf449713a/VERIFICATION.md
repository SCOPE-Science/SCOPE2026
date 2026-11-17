---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For every b,k≥2 write k=2^s t (t odd), U=(b^t−1)/(b−1), H=(b^k−1)/(b^t−1). Fixed-width leading block coefficients include consecutive integers (or 1), so gcd reduces to gcd of R_{b,k}(h). For odd h each b^(2^i t)+1 divides b^(2^i t h)+1, giving H; KSS unrestricted gcd for the odd t-part supplies gcd(t,U). Since U is odd, H≡2^s (mod U) is a unit, and widths 1,t give the matching upper bound. For t=1 the coincident witness is handled separately. Even widths reduce exactly to base b² KSS. The independent exact-integer diagnostic passed 161 (b,k) pairs with all necessary witness widths; earlier fixed bounded-width tester was corrected, not used to draw mathematical conclusions.

## originality

PASS

Kane–Sanna–Shallit Theorem 1 determines unrestricted-width gcd and gives two witnesses at widths 1,k. It already implies the odd-k odd-width result and the even-width b² result, both credited as prior. For even k the new odd-width gcd H*gcd(t,U), certified at widths 1,t, can differ arbitrarily from unrestricted gcd. No equivalent odd-width restriction was found in targeted original-text/Resultary/database searches; unindexed number-theoretic coverage remains possible.

## value

PASS

The gcd of k-fold repeated digit blocks is a natural additive congruence invariant. Restricting block width to odd values, for even k, changes it by an arbitrarily large factor; exact closed form plus two specific witness widths gives a reusable arithmetic obstruction for parity-constrained digit powers. This is not an arbitrary slice or just the base-four corollary; those preexisting branches are expressly excluded from the originality claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
