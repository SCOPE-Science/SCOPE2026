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

Run `python3 verify_generating_idempotents.py` using Python 3.9 or later, from the directory containing the code. No external Python packages, network, or additional data are needed. The companion `verification_output.txt` is the exact recorded standard output.

The checker independently constructs upper triangular matrices, multiplies them using field operations, and tests \(P^2=P\). For each idempotent tuple it computes the span of all words under repeated multiplication until stable. All tuples for \((n,q,m)=(2,2,2),(2,3,2),(2,4,2),(3,2,3)\) are exhausted. The extension field with four elements is implemented by reduction modulo the irreducible polynomial \(x^2+x+1\). For \((n,q,m)=(4,2,3)\), only 320 reproducibly seeded tuples are checked against the structural generation criterion; this is **not exhaustive**. Weighted binary-word enumeration checks the displayed special polynomial identities for dimensions three through five by **exact symbolic coefficient comparison**, as well as numerical evaluations at field orders two through five. The polynomial comparisons are exhaustive finite identities in a formal variable; checks of specific matrix instances are not universal proofs.

The unrestricted exact formula is supported by the proof in RESULT.md. Independent mathematical validation and independent audit have not been performed.
