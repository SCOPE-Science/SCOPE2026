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

The theorem was checked by direct exhaustive matrix calculations, not merely by sampling the state-sum formula. The provided `check_adjoint.py` builds each algebra from its idempotent-arrow multiplication table, enumerates all elements for 11 small quiver/field combinations, computes the full adjoint matrix and its rank, and uses a polynomial of the matrix to isolate the zero-primary size-two Jordan blocks. It compares them with the graphic incidence prediction and checks all resulting population counts. Cases include disconnected edgeless graphs, different tree shapes, triangles, a four-cycle, and parallel arrows, over prime fields of sizes two and three. Each case is exhaustive for its stated finite input; it does not establish a classification for arbitrary finite fields.

The second script, `check_tutte.py`, independently sums the two nested edge subsets at seven pairs of integer evaluation points for four examples and compares with the matrix census. Run from the directory containing the scripts and outputs:

```
python3 check_adjoint.py > replay_adjoint.txt
python3 check_tutte.py > replay_tutte.txt
cmp replay_adjoint.txt check_output.txt
cmp replay_tutte.txt check_tutte_output.txt
```

The expected terminal markers are `DIRECT_ADJOINT_AND_JORDAN_PASS` and `TUTTE_JORDAN_BIVARIATE_PASS`. The proof is purely algebraic and applies to all finite fields; no independent audit has been performed.
