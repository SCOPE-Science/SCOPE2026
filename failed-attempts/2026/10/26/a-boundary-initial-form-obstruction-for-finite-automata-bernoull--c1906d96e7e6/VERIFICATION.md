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

For the open simplex, P_d and Q_d-P_d are strictly positive, and Q_d<=2 gives min(f_d,1-f_d)>= (p_1 p_2 p_3)^d/2. The function is continuous there, so the general-factory characterization as stated in Paes Leme–Schneider, Theorem 2.1, applies. Neither p_1 nor p_2 divides Q_d, which proves coprimality. A Bernstein ratio can be taken with numerator and denominator of the same homogeneous degree, by multiplying by powers of the coordinate sum if needed. After cross multiplication with P/Q, homogeneity extends the identity from the open simplex to the positive cone, hence to a polynomial identity. Coprimality implies B=QR. The multiplier is homogeneous and nonzero, so setting the chart coordinate to 1 cannot annihilate it. The initial homogeneous component of the product is the product of the two nonzero initial components, since the coefficient ring is a domain. If the denominator initial component vanishes at a strictly positive vector, the product does too, impossible for a nonzero component with nonnegative coefficients. For d>=4 the degree-two component is (x-y)^2 and the other summand starts in degree d-1, so the obstruction applies at (1,1). Nonexistence uses the necessary block-simulation representation, not the invalid multivariate rational-simulability claim. Morina's original thesis was not directly read; the criterion was checked in the explicit accessible theorem.

## originality

FAIL

The mathematical obstruction is covered by Handelman's stronger positive-multiple theorem, in the exact nonnegative-coefficient convention verified in De Angelis–Tuncel. The degree-four member and the corresponding denominator proof already appear verbatim in substance in Paes Leme–Schneider. The all-d family follows from these known criteria without a new obstruction: the very same exposed-face square persists when the degree of the correction is increased. No evidence was found that all members had previously been listed, but exact prior listing is unnecessary for mechanical coverage.

## value

FAIL

The separation between general and finite-state factories is meaningful, and the chart argument is a clear exposition of a practical test. But the record adds neither a new test nor a distinct boundary phenomenon: every family member uses the previously exhibited square at the same positive direction, and varying the degree of the higher-order perturbation adds no demonstrated new range of factory behavior, sharp threshold, or classification. With the established stronger positivity theorem and exact d=4 precedent, the unmotivated degree extension and restatement are not a surviving scientific contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
