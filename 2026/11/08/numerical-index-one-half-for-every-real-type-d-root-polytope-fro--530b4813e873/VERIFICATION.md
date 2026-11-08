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
# Mathematical verification

The all-dimensional proof checks a finite set of norming-functional types symbolically, not by enumeration in bounded dimensions. For each signed-pair vertex and generator, the proof constructs either a directly norming pair or two root vertices of total sum equal to the chosen vertex, each normed up to sign by the generator. The rank-one witness is checked on every class of signed-pair vertex and norming generator. The polyhedral reduction is justified by convex decomposition of both exposed faces.

The standalone standard-library program `check_type_d_index.py` replays exact integer sign and decomposition assertions on every root vertex and norm generator for dimensions \(d=4,5,6,7\), and checks the witness's operator norm and spatial numerical radius. Run `python3 check_type_d_index.py`; expected output: `TYPE_D_NUMERICAL_INDEX_EXACT_OK 18744`.

These finite checks do not prove the theorem for arbitrary \(d\); the all-dimensional proof in RESULT.md is the necessary evidence. External auditing was not performed.
