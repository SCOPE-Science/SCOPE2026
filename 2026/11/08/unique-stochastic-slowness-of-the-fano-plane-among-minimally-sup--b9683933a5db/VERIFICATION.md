---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Read entire frozen RESULT.md and verify.py. The inclusion-exclusion identity for uncovered coupons gives 7^-t Σ_{k=1}^4 c_k k^t for t>=1, with signed avoidance coefficients from all 127 nonempty vertex subsets. Independently reimplemented the finite combinatorial census via monotone 7-block incidence recursion over the 35 triples: exactly 11,205 admissible labeled families and exactly the eight specified coefficient profiles with multiplicities 30,630,1680,3780,3360,360,1260,105. Independently verified the 30 Fano maximizers form exactly its full vertex-permutation orbit, and recomputed rational means 163/30 and 16/3 and strict tail differences for t=3..99. The proof reduces all integer t>=3 to exact symbolic formulas b(3^t-3·2^t+3), 4^t+3·3^t-15·2^t+17, and 2(2^t-2)(2^t-4), each strictly positive; finite times alone would not suffice. The seven-block degree-three requirement and sampling with replacement were honored.

## originality

PASS

Best-of-knowledge distinct claim after actual primary-source and published-record comparisons. The strict ordering of Fano against the complete 35-triple scheme is not a monotonicity statement over arbitrary seven-edge fair hypergraphs, so it does not imply unique minimal-support optimum.

## value

PASS

A complete sharp stochastic-order classification in the smallest-support fair triple-draw coupon model is naturally motivated by the question of worst fair coverage delay. It classifies all 11,205 labeled admissible mechanisms, identifies the unique extremal isomorphism type, and separates mean and distributional optimality, not merely one constructed Fano-versus-uniform comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
