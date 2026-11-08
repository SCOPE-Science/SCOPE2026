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

# Reproduction and limits

With Python 3, from this package directory run:

```sh
python3 artifacts/verify_direct.py
python3 artifacts/verify_state.py
```

The actual outputs are supplied in `artifacts/direct_output.txt` and `artifacts/state_output.txt`. The original-graph verifier exhaustively checks every subset with size at most \(n-1\) for \(3\le n\le7\); it independently constructs the crown edges and vertex distances, tests resolving sets, and reconstructs adjacency-restricted slides. The separate vacancy-state verifier computes all-pairs shortest distances in the complete state graphs for \(3\le n\le8\), samples states at \(9\le n\le11\), and exhaustively exercises two explicit routing schemes on their relevant finite inputs for \(4\le n\le11\). The two scripts do not share an implementation or a generated table.

The connectedness and diameter assertions for arbitrarily large \(n\) rest on the inductive proof in `RESULT.md`, **not** on extrapolation of the finite checks. Historic originality remains qualified by unavailable possible covering texts; no independent mathematical audit has been performed.
