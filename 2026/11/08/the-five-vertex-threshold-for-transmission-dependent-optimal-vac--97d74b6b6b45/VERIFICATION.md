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

# Reproducibility and limits

Run `python3 verify.py` with Python 3; no external libraries or files are required. The verifier enumerates all labeled graphs with two to five vertices and all edge-subset realizations of their post-vaccination graphs. Exact permutation canonicalization gives connected graph counts 1, 2, 6, 21. For the 28 classes with a permanent optimum, 127 comparisons are certified by nonnegative integer coefficients after the substitution \(p=t/(1+t)\). The two remaining classes match the theorem's exact edge lists, and their factorized polynomial differences are checked coefficient-by-coefficient.

The full run completed successfully and independently compared the cluster-square risk formula with the ordered-connected-pair risk formula on 147 vertex instances, all using integer arithmetic. This is exhaustive for the stated size bound; it does not certify any larger graph, different epidemic mechanism or independent publication priority.
