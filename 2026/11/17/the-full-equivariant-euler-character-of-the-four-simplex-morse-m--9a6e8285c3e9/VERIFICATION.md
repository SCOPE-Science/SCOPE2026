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

# Exact finite verification

In a directory containing all included files, run:

```
python3 morse_equivariant_euler.py
python3 crosscheck_morse_kahn.py
```

Both programs use the Python standard library. The first constructs the face-poset cover graph on the nonempty faces of simplices with four and five labels, uses \(V\)-path digraph acyclicity, and exhaustively enumerates invariant orbit unions. The four-label case reproduces the known \(S_4\) character and complete face count. At five labels, its published identity input is the exact \(f\)-vector from Scoville (2026); every nonidentity class is computed from exhaustive finite enumeration. The second program uses a separate full-Hasse directed-acyclic-graph test based on Kahn's topological sort and independently enumerates compatible primitive-edge orbit unions before applying that test.

Recorded outputs: `CHECK_OUTPUT.txt` and `KAHN_CHECK_OUTPUT.txt`. Both were executed successfully, and matching totals and reduced Lefschetz characters agree for all six nonidentity conjugacy classes. The calculations do not determine graded homology or validate an uncomputed infinite family. The mathematical proof of the orbit formula is contained in `RESULT.md`.
