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

The proof's infinite-lattice quantifiers are justified by Bloch diagonalization, strict positive-definite resolvent Hessians, exact walk-lifting and a norm-controlled dimer perturbation; they are not inferred from finite sampling.

Run `python3 verify.py` after extracting this complete package. The program uses only the Python 3 standard library and includes: an exact-rational bracket via a positive walk-count series and a rigorous geometric tail bound; independent finite-torus rational matrix inversions and Fourier evaluation; positivity checks of the resolvent; sample strict anisotropy comparisons and weak-edge asymptotics. The actual replay reports `PASS 537 supplementary checks`.

Limits: sampled positive weights and torus sizes do not exhaust all cases. The independently unaudited analytic proof is the sole basis for the all-parameter result. No external or independent certification is claimed.
