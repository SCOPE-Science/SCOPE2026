---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The Laplacian diagonal retains degrees q and 2. The follower-part zero-sum spaces contribute those eigenvalues and the normalized two-constant block has off-diagonal minus the square root of the product of the follower-part counts. For a=0 its trace is q+2 and determinant 4, giving delta and q+2-delta; for a=1 it has eigenvalues 1 and q+1; for a=2 the whole matrix is 2I. The smaller root for a=0 decreases with q by delta=8/(q+2+sqrt((q+2)^2-16)) and is below 19/50. From the trace differences, at t=1/5 the two comparisons H0-H1 and H0-H2 are bounded above by negative quantities using the uniform bound on the fast modes. At 67/100, H0-H1 is positive even after dropping those fast positive terms and replacing delta by 19/50, whereas H1-H2 is negative from exp(t)<49/25 and exp(-(q-1)t)<1/25. At 1 both rivals have larger trace than H2. An independent rational replay (`python3 /workspace/branches/heat_trace_exact_bounds.py`) certified the sign estimates; the middle Taylor margin is 294177970312366399583/177187500000000000000000 > 1/1000. The frozen verifier was inspected, not run. At fixed t, the three limiting differences have crossings log(phi), log(2), and log(sqrt(3)) with log(sqrt(3)) strictly between the other two; at this nonoptimizing crossing both comparisons with a=1 remain strict. This gives eventual uniqueness on the stated open intervals, not the finite-q diagram or ties at the boundaries. The exact placement multiplicities count the two chosen leaders in their parts. For the initial-condition interpretation of the objective, covariance I should be accompanied by zero mean (or use second moment I); this does not alter the heat-trace theorem.

## originality

PASS

The distinct part is strict realization of all three winning placements at the stated positive times uniformly in q>=9, and the two exact fixed-time large-size boundaries. Neither grounded spectra in themselves nor stationary optimal placements are treated as new.

## value

PASS

This is a motivated exact witness that finite-time placement can select all three allocations, not just interpolate between a short-time and a steady-state choice. The witness holds uniformly across an infinite graph family and gives two explicitly separated limiting thresholds. Its utility is to distinguish pointwise diffusion performance from stationary and single-eigenvalue rankings, not to claim a complete phase diagram.

The dated certificate retains the supplied scientific assessment, sources and limitations.
