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

Given the viability flags, the two total counts are independent Poisson variables with identical mean λS, S=ΣG_i x_i. Their conditional distribution depends only on S, so conditioning on S preserves the stated product detection probability (1−e^(−λS))². The Laplace transforms of S give the two products in the objective, which attains its maximum by compactness. For a pair of efforts x,y with positive fixed sum, the both-viable and both-failed cases are constant. In the exactly-one-viable cases, put u=e^(−λx), v=e^(−λy), r=uv, s=u+v; the varying conditional expectation, up to the positive multiplier p(1−p), is 2−2As+C(s²−2r), with C=E[e^(−2λR)]>0. Its strict convexity in s excludes every interior s, which corresponds precisely to unequal positive pair efforts. Endpoints are equal split or one zero. Thus every optimizer has all its positive entries equal; the finite maximum includes all such possibilities, including n=1. Independently recomputed the exact F3−F1 factorization −(12/125)(z²−1)²(3z⁴−1)(z⁴+2z²+2) at p=4/5, z=e^(−λB/6). At the sole interior crossing z=3^(−1/4), the F3−F2 gap is (8/675)(54z³−18z²−13). The bracket is strictly increasing for z>2/9 and is 120898933/500000000 at z=759/1000, below the crossing z. The sign reversal and strict gap, by continuity, prove the claimed local 1-to-3 jump and exactly the stated support sizes at the tie (up to permuting labels). Scope is two known-present targets with the same λ, shared within-sample viability, independent samples, and no opening charge; it neither assumes laboratory pooling nor claims absence of k=2 optima at all budgets. RESULT.md lines 15–47, VERIFICATION.md and check.py were inspected. The exact crossing calculation did not execute the frozen checker; the finite code tests cannot prove the global optimization statement.

## originality

PASS

The supported distinct result is strict equal-active reduction for the nonseparable Bernoulli-viability joint detection objective together with the skipped-support transition. Equal active allocations are known for additive sigmoid models and equal stakes also appear in Bernoulli weighted-sum threshold problems. The strongest examined precedents optimize different functions or assume laws that exclude Bernoulli variables; neither the strict reduction nor the crossing is mechanically implied. Same-day neighbor records were compared by their findings, without inferring priority from date.

## value

PASS

The proof turns a coupled continuous allocation problem into an exact finite choice, while the minimal three-sample case shows that equal active efforts do not imply consecutive activation. This matters for the design decision of how many replications to use when targeting joint detection under shared failures. The strict gap and signs certify a robust local transition rather than a numerically selected tie. The value is mathematical and conditional on the model, not empirical guidance for particular taxa or assays.

The dated certificate retains the supplied scientific assessment, sources and limitations.
