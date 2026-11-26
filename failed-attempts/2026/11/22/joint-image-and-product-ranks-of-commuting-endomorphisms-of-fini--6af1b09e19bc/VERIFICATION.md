---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The quandle identity with x=k−1 and y=k makes consecutive differences of any endomorphism constant; conversely every ax+b preserves the operation, including at p=2. Commutation is the vanishing of the minors of the two-row matrix (u;b), where u_i=a_i−1. With h the minimum truncated valuation of u, dividing u by p^h and reducing b modulo p^{e−h} gives a unit pivot if h<e. The reduced b is one scalar multiple of the reduced u and there are p^{ht} lifts; for h=e all translations are free. This yields p^{e+(t−1)h}. A nonunit slope forces h=0. The valuation counts c_ν and the capped sum of valuations of the product give the asserted weights. Summing the translation count over h gives the stated total; subtraction of the baseline p^{e(t+1)} puts the excess entirely in the all-unit cell. This also gives the identity at t=1, the 9153-example, and the multiplicative rank exponents under Chinese remaindering. Separate pointwise enumeration for (2,2,3) matched all 27 nonzero rank profiles with total 400 and all-unit count 176, and sampled h=0,1,2 fibers had respective sizes 4,16,64.

## originality

FAIL

The prior two-pole determinantal record already proves both the exact unweighted count and the unit-entry-pivot structural lemma that computes every singular-slope rank cell here. Although the rank-marked polynomial is not printed in the prior result, it is mechanically determined by these prior statements and ordinary slope valuation. The independently correct extension of the fixed-row count to h>0 is itself the same pivot lemma after a quotient and counting independent lifts, and is not needed for any new cell in the claimed polynomial.

## value

FAIL

The joint image ranks are natural, and the explicit polynomial can be a convenient reference. The claimed new information, however, is a mechanical weighting of the established unit-pivot stratum plus residual subtraction in one cell. Product rank is determined by the individual valuations and adds no independent invariant. No further nonmechanical surviving claim is established for the frozen result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
