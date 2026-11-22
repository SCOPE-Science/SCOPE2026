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

# Verification record

To rerun the finite checks, execute `python3 verify.py` in the directory containing the included standalone checker. It uses only Python's standard library. It separately evaluates the recurrence, the generalized-derangement finite-sum formula, and the ordinary-derangement expression, and verifies the integral formal-polynomial congruences on both parity branches. It also checks complete residue bijections, periods, sample pair valuations, and exact initial three-square obstruction classes.

These tests establish only finitely many arithmetic instances. The general result follows from coefficientwise convergence of restricted power series, the leading-unit difference law for both parity branches, and Legendre's three-square characterization. An independent mathematical audit has not been performed.
