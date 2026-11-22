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

# Verification evidence

Run `python verify.py` with the dependency version in `requirements.txt`. The script carries out exact symbolic expansion of the invariant relation, the three generator invariance checks, conic nondegeneracy, line/conic restrictions, and the five branch crossing coordinates. The output must be `PASS: all exact invariant, relation and five-node branch checks`.

The proof separately establishes no common zero for the three invariant quadrics on the K3 quartic, hence a finite degree-sixteen map, and quotient degree two because the group has order eight. The nonsquare branch polynomial and normalization identify the full quotient. The local analytic A1 classification and the double-cover canonical formula are standard geometric arguments; the script does not purport to establish them. No exhaustive historical novelty test or independent mathematical audit was performed.
