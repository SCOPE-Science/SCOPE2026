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

# Verification and reproducibility

`CHECK.py` constructs the complete trace-free symmetric matrix space in even dimensions \(4\), \(6\), \(8\), and \(10\). It evaluates each conditional fourth moment using a direct enumeration of balanced sign configurations and independent Dirichlet magnitude moments, rather than the four-band formula, then compares all computed Gram eigenvalues and multiplicities with the theoretical spectrum. The observed maximum absolute eigenvalue discrepancy was below \(3	imes10^{-15}\) in these dimensions.

Run `python CHECK.py` after installing the dependency listed in `requirements.txt`. The checker asserts positive eigenvalues, dimensions and strict sector ordering in the tested dimensions. It does not evaluate all dimensions and is not used as evidence for an infinite statement. Exact identities and the all-even-dimensional proof are in `RESULT.md`; the minimizing sector transition follows from a factored polynomial determinant and elementary rational bounds on \(\pi\). Independent validation was not performed.
