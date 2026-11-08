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

# Reproducibility and scope

From the directory containing this document, run `python3 checks/check_complex_cesaro.py` with Python 3. The checker uses the standard library only and verifies all entries in finite phase-normalized Gram matrices for several real and nonreal shifts, and strictly negative real and complex-shift test vectors. On the reviewed inputs, all 3,888 finite assertions passed.

The infinite negative index uses arbitrarily large and numerous harmonic blocks: their existence is proved by divergence of the harmonic series, not by finite enumeration. The proof that the self-commutator is Hilbert–Schmidt uses absolute convergence of a double inverse-square series. The full operator-to-form inertia transfer uses dense range and finite-dimensional negative-subspace approximation. None of these conclusions is certified by finite tests or by an independent mathematical audit.
