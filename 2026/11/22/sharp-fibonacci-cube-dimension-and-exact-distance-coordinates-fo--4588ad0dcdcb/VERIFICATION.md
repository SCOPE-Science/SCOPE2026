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

# Verification and scope

Run `python3 verify.py` in the directory containing the script. It uses only Python's standard library, enumerates all monomer/dimer words, reconstructs the graph directly from its allowed transitions, computes all-pairs shortest-path lengths by BFS, and compares them against the exact binary labels. It checks forbidden consecutive ones, injectivity, edge preservation, and the presence of all coordinate directions. The unbounded proof is in `RESULT.md`.

The tested parameter grid comprises \(k=2\), \(1\le n\le6\); \(k=4\), \(1\le n\le4\); \(k=6\), \(1\le n\le3\); and \(k=8\), \(1\le n\le2\). Observed largest cases have \(305\), \(228\), and \(65\) vertices for \((n,k)=(4,4),(3,6),(2,8)\), respectively. Finite tests cannot establish universal claims; the mathematical proof gives the all-parameter result. Historical novelty is subject to possible unindexed equivalences. Independent audit was not performed.
