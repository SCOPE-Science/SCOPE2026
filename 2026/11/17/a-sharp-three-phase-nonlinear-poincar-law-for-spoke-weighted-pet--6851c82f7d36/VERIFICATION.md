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
The asserted inequality is proved for every real \(t>0\) by two explicitly counted graph-path routings, positive convex interpolation for \(1\le t\le9/4\), and three equality witnesses. The symbolic proof is in RESULT.md.

The standalone script `verify_petersen.py` uses Python 3 and only its standard library. It checks the seven dihedral pair-orbit sizes, both route-type signatures for all orbit representatives, total edge-type routing loads \((25,25,25)\) and \((20,20,45)\), and exact metric equality at nine rational conductance values including the two transition endpoints. The script explicitly checks all metric triangle inequalities for each ten-vertex witness. Run `python3 verify_petersen.py` from this directory.

The finite script checks do not substitute for the proof of the universal upper bound or for a full bibliographic priority review. No independent mathematical audit has been performed.
