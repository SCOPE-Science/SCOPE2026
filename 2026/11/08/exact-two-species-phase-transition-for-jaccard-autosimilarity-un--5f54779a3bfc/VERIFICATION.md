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

# Reproduction notes

Run `python3 check_autosimilarity.py` from the directory containing this file and the source. Standard-library Python is sufficient. The checker calculates incidence-set distributions directly from all ordered pairs of iid draw sequences for seven exact rational two-species compositions through eight observations per sample, independently verifies the closed formula, and tests algebraic increment identities and an explicit rational witness. It also checks a factor identity and exhibits strictly positive abundance vectors of three, four, five and seven species with the prescribed two-reversal sign pattern.

The completed check reports `PASS: 512 exact/equality and witness checks`. These calculations support the finite identities and give reproducible witnesses. They are **not** a certificate for the infinitely many sample sizes and continuous abundances in the theorem. That part is the analytic proof using the normalized increment's monotonicity and the positive factorization in `RESULT.md`.

The comparison with prior research is historically provisional because a highly relevant ecological autosimilarity paper could be inspected only in abstract. The mathematical results refer to the exact models and assumptions in the proof, not to field measurements or detection-error models.
