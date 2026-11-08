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

# Verification record

Symbolic verification: run `python3 verify_howe_rank.py` with SymPy. It checks exact identities, all three normalized elliptic quotient models, three smooth reduced rank-one points, and geometric isomorphisms. Expected success line: `HOWE5_RANK_STRATIFICATION_PASS eigenvalues=3 rank1=3 reduced=3 classes=1 GF5= {1: 3, 2: 6, 3: 4}`.

Independent finite-field check: run `python3 verify_field25.py` using Python's standard library. It checks all 625 coefficient pairs over the quadratic field and confirms 553 smooth cases, distributed 3/60/490 over ranks 1/2/3, while comparing elliptic and genus-three point counts. Expected success line: `HOWE5_GF25_INDEPENDENT_PASS smooth= 553 rank_counts= {1: 3, 2: 60, 3: 490} rank_one= [(0, 0), (2, 0), (3, 0)]`.

All geometric assertions for the algebraic closure are established by exact characteristic-five polynomial calculations and the proof's semilinear stable-rank argument. Neither finite enumeration nor program output alone establishes infinite-field universality. The polynomial operations and the change of coordinates are included in the text and replayable code. Independent review and external validation have not been performed.
