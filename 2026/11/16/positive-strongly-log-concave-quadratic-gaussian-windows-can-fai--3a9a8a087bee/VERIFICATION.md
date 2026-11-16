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

The accompanying `verify.py` is standalone under Python 3 with `mpmath` installed. Run `python3 verify.py`. The high-precision finite checks use independent direct and Poisson-dual expressions for the alternating theta series and its logarithmic derivative, compare strict coefficient and curvature inequalities at six parameters, check cancellation at eleven half-grid nodes per parameter, and verify a nonzero off-node value. The script passed 132 checks.

These numerical checks are diagnostics and do not prove the theorem for a continuum of parameters. The infinite proof is in `RESULT.md`: Poisson positivity plus a dual-moment lower bound, an exact alternating translate identity and symmetry, and the Zak-fiber Parseval obstruction. The shape interval is not asserted sharp. Publication priority is supported only to the extent of the listed inspected sources; an independent audit has not been performed.
