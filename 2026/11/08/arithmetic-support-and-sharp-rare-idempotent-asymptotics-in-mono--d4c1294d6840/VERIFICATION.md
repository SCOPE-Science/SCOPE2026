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

# Reproducibility and limits

Run `python verify.py` with Python 3 and its standard library. Expected final line: `VERIFY_OK`.

The program verifies independently, through literal substitution and finite-field arithmetic, every weighted-permutation algebra in the tested dimensions: \(q=4\), \(1\le n\le4\); \(q=8\), \(1\le n\le3\); and \(q=16\), \(1\le n\le2\). It also compares two different exact rational-power-series constructions of the probabilities up to dimension \(28\) for twelve prime-power field orders. This includes the finite product with both positive and negative divisor exponents in the \(q=64\) case. A numerical check illustrates convergence to the predicted leading term at dimension \(1200\), with slow correction expected from other singularities. No finite program certifies the asymptotic statement for all dimensions; the complex-singularity proof is given in `RESULT.md`.

This document records only the present checks; independent audit remains unperformed.
