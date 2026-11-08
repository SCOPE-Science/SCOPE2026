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

The exact finite proof is independently reproducible with Python's standard library. `verify_gp.py` builds the twenty-vertex generalized Petersen graph directly, calculates open and exact-distance-two neighborhoods, enumerates all subsets of sizes one through four and matches the resulting fifteen optimum configurations to the fifteen antipodal lifts of quotient edges. It checks the fifteen optimum states, zero one-token transitions, thirty two-token transitions, four regular neighbors per state, and exact eccentricity three for all states. `verify_icosahedral_dual.py` instead enumerates the twenty triangular faces of the icosahedral graph, constructs their dual face-adjacency graph, discovers the distance-five antipodal involution, and independently enumerates and checks all DTD optimum sets and move graphs.

The embedded outputs `verify_gp.output.txt` and `verify_icosahedral_dual.output.txt` record the observed values from direct execution. The different constructions independently cover the most critical possible graph-labeling and predicate errors. Both check all \(\binom{20}{4}=4845\) candidate sets and all \(\binom{15}{2}=105\) pairs of optimum states. No sampling, timeout-as-impossibility, or extrapolation beyond this finite graph is used. The lower bound and isomorphism explanation are mathematical arguments in `RESULT.md`; the scripts are a fully exhaustive finite certificate for the otherwise nonstructural fifteen-set completeness step.

Independent mathematical audit has not been performed.
