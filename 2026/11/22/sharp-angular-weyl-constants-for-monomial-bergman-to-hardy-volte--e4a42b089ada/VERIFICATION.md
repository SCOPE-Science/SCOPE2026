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
The precise operator, normalized norms and scope are those in `RESULT.md`. The proof uses exact orthogonal output monomials, integer-shift gamma ratios, uniform asymptotics off coordinate faces, simplex-volume lattice counting, and monotone sequence inversion. The numerical tests below are finite diagnostics and do not prove an infinite asymptotic or global priority.

Run `python checker.py` using Python 3 (standard library only). Exact factorial/gamma comparisons passed for the stated dimension and monomial examples. Cutoff counts for the disk/ball monomial examples are below their continuum coefficient at moderate thresholds and approach their predicted asymptotic constants as thresholds decrease. The algorithm does not enumerate the infinite tail; this is handled by the uniform analytic estimates in the proof.

The core Weyl coefficient is obtained by an ordinary Dirichlet simplex integral, not by a fitted numerical constant. Earlier general Schatten membership criteria and boundedness results are credited, and unindexed equivalent general spectral results are a remaining priority risk. The independent mathematical audit has not been performed.
