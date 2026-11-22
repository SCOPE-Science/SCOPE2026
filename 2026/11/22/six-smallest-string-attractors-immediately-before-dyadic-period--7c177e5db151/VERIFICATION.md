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

Run the two standalone programs from their enclosing package root:

```sh
python3 verification/local_parity_certificate.py
python3 verification/attractor_direct_check.py
```

The recorded outputs are in `verification/local_parity_certificate.txt` and `verification/attractor_direct_check.txt`. The first establishes an exhaustive mask obstruction by listing every centered length-nine context via two adjacent level-four substitution blocks, including truncated left-boundary contexts. The second independently builds every distinct factor, its occurrence-position mask, and every minimum two-position hitting set at five finite orders.

No finite test by itself proves the infinite classification. The proof uses morphic lifting and reverse projection in addition to the exhaustively justified local certificate. No external formal certification or independent audit has been performed.
