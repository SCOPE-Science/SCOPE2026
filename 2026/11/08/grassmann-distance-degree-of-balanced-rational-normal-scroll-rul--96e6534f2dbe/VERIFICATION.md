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

# Computational checks and mathematical limits

`python3 CHECK.py` uses standard-library modular polynomial arithmetic and no network access. It tests 21 deterministic genuine Grassmannian-data witnesses for parameters \(2\leq n\leq8\) and \(2\leq d\leq4\). In each case the rational objective numerator and denominator are computed from normalized orthogonal rank-one block projectors. The script checks:

- the critical polynomial has degree \(4n-2\) and is squarefree;
- its roots do not coincide with poles or zeros of any pairing polynomial defining the algebraic cut boundary;
- the numerator and denominator are coprime; and
- the full-rank tangent Jacobian formula holds for the seven tested values of \(n\).

These modular calculations are exact for each displayed rational witness because reduction preserves the required polynomial degrees and gives unit gcds. They do not establish the unrestricted theorem: the full argument uses the Jacobian identity in arbitrary degree, dominance of a family of genuine projector data, Bertini's theorem and generic cut-locus avoidance. No independent validation has been conducted.
