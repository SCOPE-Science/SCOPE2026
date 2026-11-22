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

# Exact reproducibility and proof dependency

Execute `python3 verification/check_king_cuts.py` from a directory containing the extracted file. Python 3 standard library only; no downloaded data or packages. The script constructs strong-grid edges independently of the algebraic proof, then enumerates all cuts with one anchor spin fixed on eleven small grids, counts maximizing cuts using a separate column transfer recurrence on 69 rectangles, and checks 87,376 local two-row assignments used in the lemma. Its tested ranges are explicit in the source. Replayed output:

```text
LOCAL_EXTENSION_EQUALITY_CASES_PASS 87376
DIRECT_ALL_VERTEX_COLORINGS_PASS 11
TRANSFER_MATRIX_EXACT_MAXCUT_AND_DEGENERACY_PASS 69
VERIFY_OK
```

The unrestricted theorem is not inferred from finite samples. It follows from (a) the cited exact minimum-uncut formula for strong products of bipartite graphs with paths, (b) the explicit local triangle-packing inequality and sharp equality characterization, (c) the alternating-row increment identity, (d) the monochromatic-boundary rigidity lemma, and (e) the two-stage induction on rectangular dimensions. In particular, the two-dimensional boundary at side length two and the equal-side case are proved explicitly.

The prior maximum-cut magnitude is acknowledged as prior work. Independent mathematical audit and broad historical priority verification have not been performed.
