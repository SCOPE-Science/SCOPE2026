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

# Verification of the exact paired-epoch variance law

The analytic chain is: explicit affine one-epoch composition; exact without-replacement covariance; strict rearrangement of geometric positional weights; arithmetic-geometric mean for strict negative covariance; uniform-position central moments for small steps; Riemann sums for the epoch-scale crossover; affine centered second-moment recurrence for independent epochs. The argument assumes nonidentical centers and strictly positive component contraction factor.

Run `python3 verify.py` in this directory. The program uses only standard Python modules, checks rational identities for complete samples through seven observations, exhaustive fixed-position pairing optimality through five observations, exact affine stationary recurrences, and numerical large-size limits. The executed program returned `PASS 460 exact/numerical assertions`; the checks are not proofs for arbitrary dimension or stepsize. No separate or independent mathematical audit has been undertaken. The two-pass implementation cost is not modeled in a wall-clock comparison.
