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

Separated Jacobians yield the tensor product of finite Milnor algebras. Rank-nullity equates the Tjurina cokernel dimension with the kernel of the Kronecker sum. The square-zero operator has c length-two and s length-one blocks. The diagonal raising operator on k standard sl2 factors has one kernel vector per irreducible, counted in weight 0 for even k and weight 1 for odd k. This gives the exact sum, including k=0 and c=0. The sum of the two middle coefficients equals the integral with amplitude 1+cos(theta); near zero the normalized base is 1-(c/mu)theta^2+O(theta^4), so the leading Gaussian integral is sqrt(mu/(pi c r)) and the absolute remainder is O_h(r^(-3/2)). If s=0, the contribution near pi is O(r^(-3/2)) because the amplitude vanishes quadratically, so there is no missing parity factor. The plane-curve square-zero conclusion follows from h being integral over its Jacobian ideal and the Jacobian-ideal Briancon–Skoda bound in two variables; the zero-defect case is the classical quasihomogeneity criterion. Direct substitution reproduces 226 and 1363 for the two examples.

## originality

FAIL

A distinct same-day indexed record states the stronger arbitrary-Jordan-length repeated-sum formula and the identical relative error. Specializing gives both the exact square-zero formula and its sharp asymptotic, including the zero case; the frozen result is therefore covered. This is an equivalence/coverage decision, not a claim about order of publication within the day.

## value

PASS

As mathematics the exact count and the sharp decay law answer a natural structural question: how much of the Milnor algebra survives the Tjurina quotient under repeated joins. The decay distinguishes the nonquasihomogeneous plane-curve case from equality for every tensor power, with a coefficient depending on the Tjurina defect and a parity-robust error. This assessment of the significance of the general structural statement does not credit duplicate coverage as a new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
