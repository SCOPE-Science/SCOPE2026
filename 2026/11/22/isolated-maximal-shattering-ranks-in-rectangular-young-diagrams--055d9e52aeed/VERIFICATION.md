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

Run `python3 verify.py` from the directory containing this document; no external package or network connection is necessary.

The checker separately enumerates weakly decreasing row lengths for all Young diagrams in the \(m\times(2m-2)\) rectangle and constructs their actual bit-vector incidences. For \(m=3,4,5\), every candidate antichain of size \(m-1\) or \(m\) is checked at every rank by direct trace projection. Each result is compared with an separately evaluated geometric down/up closure criterion; the program tests 19,307 support-rank combinations. For \(m=6,7,8\), the program enumerates all 39,441 candidate antichains of these two sizes, computes their down and up closures cell-by-cell, and checks the exact area/support spectrum.

Expected output begins with `PASS direct rank-by-rank traces` and ends with `PASS unique top support at each isolated rank for m=3,...,8`. The enumerations only test finite examples. The theorem for every \(m\ge3\) rests on the proof in `RESULT.md`, which gives the complete rank-interval argument and the omitted-row rigidity classification.
