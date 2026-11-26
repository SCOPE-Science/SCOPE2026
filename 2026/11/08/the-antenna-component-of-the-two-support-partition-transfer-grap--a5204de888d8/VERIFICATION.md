---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1,
  "record_status": "passed"
}
---

# Verification and reproducibility

The unchanged source-package program `artifacts/verify.py` uses Python 3.10 or later and only the standard library. For each \(3\le n\le22\), it generates all partitions of \(n\), selects the support-two stratum, and compares indexed-row transfers and part-value transfers for each vertex of that stratum. It computes the component of \((n-1,1)\) by breadth-first search and checks its membership and size against the theorem. It also tests the connectivity or disconnection witness as applicable. For \(23\le n\le150\), the program instead generates the two-support stratum directly from its size and multiplicity parameters, and checks the closure, membership, cardinality and disconnection witness. Its success marker is `VERIFY_OK`.

Separate finite checks used full partition generation and indexed-row breadth-first search through \(n=24\), and confirmed closure by feasible donor and recipient sizes through \(n=250\). In particular, for \(n=7,8,24\) the total stratum and antenna-component sizes were respectively \((11,11)\), \((13,10)\), and \((112,42)\). These counts test the same vertex families before and after the proof correction; the theorem statement was unchanged.

The arbitrary-size proof is the complete transfer case analysis in `RESULT.md`; the finite calculations do not substitute for it or establish historical priority.
