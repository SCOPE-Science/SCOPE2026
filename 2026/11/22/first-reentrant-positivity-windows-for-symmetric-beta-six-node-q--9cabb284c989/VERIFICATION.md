---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproduction of the algebraic checks

Run `python verify.py` with the Python 3 standard library; no downloaded dataset or external mathematical package is required. It constructs the six Lagrange basis polynomials from exact `fractions.Fraction` arithmetic, computes their even centered coefficients, checks all three universal moment formulas and normalization, and verifies all three symmetric-Beta denominator-cleared numerator identities. It also reconstructs directly the weights for panel counts 1, 2, 3, 4 and 5 for fourteen positive rational shape parameters using independent raw rising-factorial Beta moments. Every monomial of degree at most the panel count is integrated exactly at each parameter, giving 280 exact-rational moment equalities. Four rational Beta shape examples witness the distinct sign phases, and integer arithmetic checks the discriminant and root brackets.

These program checks were executed successfully from the delivered standalone source. The infinite quantifiers over measures and real positive Beta shapes, the feasibility lemma, and the classification of all signs rely on the written proof in RESULT.md, not the sample count. Historical priority has been compared against accessible literature but is not independently audited; incomplete access to an older Jacobi-weight article is explicitly noted in AUDIT.json.
