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

## Reproducibility
Run `python3 verify_bandwidth.py` from the directory containing this file. No external libraries or files are used. It enumerates feasible small cross-boundary partial matchings by sorted endpoint pairing, checks the sharp operator seminorm for thirty small parameter combinations, and generates additional all-integer exact involution witnesses. Expected terminating line: `ALL_LOCAL_SYMMETRIC_STOCHASTIC_VARIATION_CHECKS_PASS`.

## Proof and limits
The general theorem follows from (i) the step decomposition, (ii) integrality of bipartite matching polytopes, (iii) the sharp hole/island run bound including the even-bandwidth obstruction, and (iv) explicit feasible involutions. Finite enumeration establishes only the cases it enumerates; it is not a substitute for the all-integer proof. Mathematical novelty remains subject to independent literature review. Independent audit has not been performed.
