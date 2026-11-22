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
# Exact reproducibility

Run `python3 verify_peak.py` in the same directory as this file. No input files, third-party packages or random seeds are required. The checker enumerates every odd monic polynomial mask of degrees two through five, retains exactly those whose state-one orbit runs through all nonzero residues, compares independent direct-window and sliding-window score ranges for all relevant horizons, and asserts the exact full per-polynomial peak table and first-degree threshold.

The final output must include `LFSR_EXHAUSTIVE_DEGREE_FIVE_OK: 111 primitive-polynomial/horizon pairs; direct + sliding independently agree`. The proof of complement identity in `RESULT.md` justifies restricting to the half-period. Finite exact enumeration proves the finite theorem but does not imply any behavior for larger degrees.

The review here is a self-review. An independent audit has not been performed.
