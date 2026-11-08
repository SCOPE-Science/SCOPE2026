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

# Reproduction of the mathematical checks

Run `python verify.py` with Python 3, SymPy, NumPy and SciPy. The script verifies algebraic identities at arbitrary positive symbolic parameters and the strict rational wedge inequalities for the printed concrete example. It integrates one admissible trajectory as a diagnostic and prints normalized quantities; this diagnostic does not prove existence, exactness or convergence of an infinite-time limit.

The analytic proof uses the exact predator coordinate \(H(y)=c/(sy)+c^2/(2sy^2)\) and the integrable-error prey identity. The critical assumptions are \(m=c\), \(r>e\), and \(p/a>r-e\). The asymptotic holds only for sufficiently small positive initial conditions within a cone; neither full-basin inclusion nor global attraction is claimed.

Self-review: passed. Independent audit: not yet performed.
