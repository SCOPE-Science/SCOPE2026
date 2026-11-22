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

# Reproducible verification

Run `python3 CHECK.py` in this directory. Python 3 standard library suffices. It compares direct enumeration against every predicted fiber (including omitted targets) at all thirty combinations of \(p\), \(s\) and \(k\) described in RESULT.md. For each case the checker also tests image size and the sum of fiber multiplicities. All thirty combinations passed at preparation.

Finite enumeration is not a proof for arbitrarily large exponents or moduli. The complete proof relies instead on the normalized binomial expansion, the isometry on noncritical residue classes, the explicit critical square normal form, and exact quadratic-root counts. No external independent mathematical audit has been performed.
