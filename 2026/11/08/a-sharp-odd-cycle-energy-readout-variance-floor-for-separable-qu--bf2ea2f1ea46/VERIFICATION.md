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

# Reproducibility of the mathematical claim

Run `python3 verify.py` in the directory containing this document. The script uses only Python's standard library and deterministic random seeds. It independently forms Pauli matrix tensor products for three chargers; checks Born expectations against the closed Walsh formula; checks Walsh orthogonality for three- to five-vertex graphs; tests both constructive sharp optimizers for odd-cycle lengths three, five, seven, nine and eleven; samples general Bloch bases for numerical counterexamples; and verifies the three-charger variance and the explicit separable-mixture weights.

The exact reduction to a multi-affine problem in squared equatorial lengths proves that a global optimizer exists at endpoints. The discrete Fourier lower bound on an odd-cycle adjacency matrix proves the all-equatorial optimum and its attainability. These analytical arguments, not the bounded script, cover the full continuum of local axes and every odd cycle size. The script cannot establish any universal claim, rule out prior published equivalents, or certify physical realization by a specified dynamics.

A full independent validation has not been performed.
