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

# Verification scope

The sole externally executable artifact is the Python 3 standard-library program `checker.py`. Run `python checker.py` in the directory containing these files. Its deterministic recorded result was `EXACT_CASES_PASSED 29`. The checker enumerates small uniform-on-surjection words, checks Stirling-number factorial moments, and compares the actual complete-spell event against the precise finite discrepancy bound by enumerating every future draw for each tested small model.

Proof of the infinite-dimensional asymptotic is mathematical: Steps 1–6 of `RESULT.md` specify the conditioning, the finite counting identity, the zero-truncated-Poisson lattice local limit, convergence of singleton factorial moments, and the disappearing error for replacement draws. The local limit uses the usual Fourier inversion argument for a triangular array with increasing Poisson parameter and its adjacent shifted row; finite enumeration alone cannot verify this step.

The asserted domain is fixed \(0<\alpha<1\). No claims are made for the critical endpoint, general nonuniform arrivals, independent reproduction of the result, or complete historical novelty certification.
