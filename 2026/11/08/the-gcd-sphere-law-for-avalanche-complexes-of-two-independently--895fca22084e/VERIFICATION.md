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

## Mathematical verification
The proof handles all integers \(a,b\ge3\). It proceeds through chip-firing rotation, the Chinese remainder theorem, identification of the complete bipartite omission graph, and a combinatorial Alexander-dual false-twin suspension lemma. The exceptional empty-realization base case for a single matching edge is proved separately.

## Finite independent checks
Run `python3 verify.py` with Python 3 standard library. It reconstructs 36 orbits, including periods and all omitted edges, and independently enumerates complete simplicial boundary complexes for 26 ordered parameter pairs. All nonzero reduced mod-two Betti numbers equal one in the predicted dimension; see `verification_output.txt`. No timeout, failure, or partial enumeration is used as an infinite proof.

## Limits
There is no independent external audit. The finite enumerations do not prove other parameter cases; the all-parameter proof is a separate argument.
