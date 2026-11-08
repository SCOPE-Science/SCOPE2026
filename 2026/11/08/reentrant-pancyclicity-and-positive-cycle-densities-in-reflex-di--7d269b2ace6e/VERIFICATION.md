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

# Finite checks and analytic verification scope

The embedded `checker.py` constructs a directed simple cycle of every tested length from three through fifty, using the explicit horizontal-chain witness from the proof at sector apertures close to both phase boundaries and at representative interior values. It enumerates all candidate outgoing neighbors, checks the intended cycle, and repeats under small random perturbations. It also checks that independent finite random point samples have no directed cycles longer than two at full aperture and no directed cycles at half-plane aperture.

The exact numerical output is captured by running `python checker.py`. These finite tests are diagnostics for the strict witness inequalities only, not proofs of Poisson-positive density, Palm integral, continuity, or almost-sure ergodic limits.

The analytic proof is organized around: (i) the cone-projection and nearest-neighbor descent obstructions at the endpoints, (ii) a finite configuration with a strict sector-angle and distance margin, (iii) a positive-probability tile event and independent tile strong law, (iv) spatial point-process ergodicity, (v) local stability under aperture perturbations, and (vi) multivariate Campbell-Mecke with a union-of-sector-discs void probability.

Remaining scientific scope: no evaluated scalar formula for the integral, no sharp threshold exponents for cycle frequencies, and no independent validation.
