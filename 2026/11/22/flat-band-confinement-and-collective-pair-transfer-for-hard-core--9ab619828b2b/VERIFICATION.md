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

# Verification

The direct Hamiltonian checker `VERIFY.py` constructs an independent basis for two occupied sites of \(K_{p,q}\), applies a unit-weight hop only between distinct occupied-site configurations differing by one graph edge, and checks spectral Gram factors without assuming their claimed eigenvectors. It then computes the first four nonzero even moments for localized opposite-shore pairs and between localized same-shore and opposite-shore pairs, for every integer \(3\le p,q\le7\). It also includes a small boundary smoke test for \(K_{2,2}\), outside the theorem. Exact rational and algebraic arithmetic is used throughout, with no floating-point tolerance. The observed output from the actual packaged checker was `ALL_EXACT_CHECKS_PASSED 251`.

These finite checks do not prove any universal quantifier, establish global literature novelty, or constitute an independent audit. The analytic proof in `RESULT.md` is the primary evidence for all sizes. No numerical data, nonlocal input files, or externally hosted scripts are needed beyond Python 3 and SymPy. Neither an independent proof review nor an external reproducibility audit has been conducted.
