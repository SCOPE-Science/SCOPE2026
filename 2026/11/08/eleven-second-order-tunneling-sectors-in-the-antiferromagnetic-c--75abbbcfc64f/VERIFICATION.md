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

# Reproduction and limits

Run `python3 verify_c60_components.py` with a standard Python 3 interpreter (version 3.9+). It requires no packages beyond the standard library and no source files other than the embedded verifier.

The actual package source was executed and returned `VERIFY_OK` for the \(60\)-vertex, \(90\)-edge fullerene, all \(125\) icosahedral perfect matchings, all \(16{,}000\) distinct ground spins, every one of the \(1770\) unordered two-site flips from each of the \(16{,}000\) states, the \(15{,}360+10(64)\) connected-component partition, ten explicit hypercube coordinate maps, and all degree values. The giant degree sum is exactly \(111{,}360\), giving Rayleigh quotient \(29/4\).

The enumerator is exhaustive because face parity and the twelve edge-disjoint pentagonal constraints prove that every minimizing configuration is uniquely encoded by an icosahedral perfect matching, one of two triangular faces per matching edge, and a global spin orientation. The program computes the finite count and component graph; the accompanying text proves the perturbative coefficients and spectral selection. No infinite-family claim, experimental validation, finite-field dynamics or independent scientific audit is asserted.
