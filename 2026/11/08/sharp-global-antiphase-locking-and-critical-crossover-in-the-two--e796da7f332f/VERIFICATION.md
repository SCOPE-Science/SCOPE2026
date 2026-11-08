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

Run `python verify.py` with Python 3 and SymPy. The checker verifies by exact symbolic series that the reciprocal-square increment is \(2/3+3v^2/10+O(v^4)\), hence the logarithmic coefficient is \(9/20\); it additionally checks strict distance contraction at 4,995 sampled phase/parameter pairs, four large-iteration critical trajectories, and four near-critical crossover sequences. A successful execution prints:

`VERIFY_OK exact_critical_coefficients=3 global_mesh_checks=4995 critical_orbits=4 crossover_sequences=4`

The numerical checks are not proofs of uniform contraction or infinite-time asymptotics. The independent mathematical arguments are the strict analytic sine inequality, a summable reciprocal-square recurrence remainder, and the uniform precritical linear-recurrence comparison in `RESULT.md`. The \(o(1)\) critical remainder excludes finite-hitting seeds; the crossover concerns fixed initial errors in \((0,1]\). No external independent assessment has been performed.
