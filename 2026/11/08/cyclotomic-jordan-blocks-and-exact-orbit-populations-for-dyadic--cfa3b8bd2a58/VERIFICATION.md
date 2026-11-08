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

Two reproducibility scripts require only the Python 3 standard library:

```sh
python3 artifacts/check_matrix.py
python3 artifacts/check_states.py
```

The first uses exact binary row-bit arithmetic to compute the nullities of powers of the shifted ladder adjacency and wave matrix, checking every positive iterate through the asserted global permutation order on ladders with 3, 7, 15, and 31 rungs. This tests the Jordan ranks and the entire fixed-space formula over the binary field at these sizes.

The second is implemented as explicit graph-neighbor XOR dynamics rather than matrix powers. It exhaustively iterates all 4096 states on the 3-rung ladder and obtains populations 1, 15, 240, 3840 at least periods 1, 3, 6, 12. It additionally checks reproducible pseudorandom states on two larger ladders.

Captured outputs for both commands are embedded with the scripts. The source proof, not these finite checks, supplies the universal quantifiers and the extension to all finite characteristic-two fields. No external independent audit is claimed.
