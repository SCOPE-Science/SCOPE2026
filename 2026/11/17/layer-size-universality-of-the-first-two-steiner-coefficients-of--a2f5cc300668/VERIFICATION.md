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

# Reproduction and scientific scope

The identities are derived in `RESULT.md` from the complete facet-pair ridge classification, exact coarea/Dirichlet face measures, and standard angle-weighted Steiner valuation. The exterior angle is the angle between outward normals: \(\pi/2\) for coordinate-coordinate and eligible coordinate-chain pairs; \(\arccos((r-1)/r)\) for chain-chain ridges differing in one layer.

Run `python check_chain_ridges.py` (NumPy) and `python check_chain_metric.py` (NumPy/SciPy) after extracting both scripts beside the Markdown files. Recorded checks succeeded: 1,023 true ridges in nine profiles with every facet pair examined, and 268 independent Euclidean ridge measures over five profiles, including direct convex-hull volume checks. Computer verification is finite corroboration; the universal quantifiers are supplied only by the symbolic proof. Nonstandard assumptions: each rank has at least two elements and all coordinates use the canonical Euclidean metric. Absolute historical priority and independent audit are not established.
