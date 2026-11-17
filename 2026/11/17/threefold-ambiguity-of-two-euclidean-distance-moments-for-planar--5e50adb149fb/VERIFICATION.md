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

# Reproducible checks
Execute `python3 check_sector.py` using Python 3 and no third-party packages. The program constructs rational enclosures for π using Machin’s formula and alternating arctangent series, then bounds exactly the three expressions for the dimensionless moment ratio at angle endpoints. They lie respectively inside the intervals (1.793393860208, 1.793393860209), (1.959702103564, 1.959702103566), and (1.768939697155, 1.768939697157), safely on the required sides of 9/5 and 39/20. The code checks sample numerical roots for three interior ratios, as well as direct independent polar sampling for four angles. The expected marker is `CIRCULAR_SECTOR_TRIPLE_MOMENT_AMBIGUITY_OK`.

The moment derivation and intermediate-value argument are analytic. Exact rational bounds certify the nonstandard endpoint comparisons. Floating-point roots and finite random samples are diagnostic only, do not prove uniqueness or the continuum of solutions, and do not substitute for an independent audit.
