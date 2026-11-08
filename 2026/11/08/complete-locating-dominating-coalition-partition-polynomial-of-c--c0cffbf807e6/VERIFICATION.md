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

# Reproduction and scope

The complete proof, including all quantifiers and boundary cases, is in `RESULT.md`. The included `verify.py` is an independent finite checker using graph adjacency-neighborhood traces and restricted-growth enumeration of unordered vertex partitions. Run `python3 verify.py` using Python 3; no third-party modules are required.

The checker exhaustively tests every \(K_{m,n}\) with \(2\le m\le n\) and \(m+n\le10\). It compares every partition size and the number of triangular three-class coalition graphs to the stated formulas. Direct tests on all constructed three-class partitions also cover \((m,n)=(2,9),(3,8),(5,6),(6,7),(7,8)\). The replay ends in `VERIFY_OK` if every test passes. In particular, the small boundary profiles \(K_{2,2}\), \(K_{2,3}\), \(K_{2,4}\), and \(K_{3,3}\) are covered exhaustively.

These are finite computations only. The unrestricted theorem depends on the false-twin complement criterion, the general obstruction to four blocks, the three-block transversal characterization, and the analytic counts in the proof. Independent mathematical validation has not been performed.
