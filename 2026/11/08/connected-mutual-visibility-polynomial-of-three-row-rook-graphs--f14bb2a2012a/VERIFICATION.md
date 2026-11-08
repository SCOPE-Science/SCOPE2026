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

# Verification and reproducibility

Run `python3 verify.py` with Python 3 (standard library only). The script constructs every cell of each rook graph, generates induced adjacency directly, checks connectedness by graph traversal, and tests visibility using the two distinct length-two common neighbors of each nonadjacent cell pair. It compares all coefficients for each graph with one through five columns, enumerating all nonempty subsets (not merely subsets below the predicted maximum). The theorem itself starts at three columns. It then verifies exact highest-degree coefficients for column counts from three through thirty.

Observed final output includes `EXHAUSTIVE_OK 3`, `EXHAUSTIVE_OK 4`, `EXHAUSTIVE_OK 5`, `MAXIMUM_COEFFICIENT_OK 3..30`, and `VERIFY_OK`. Checks for five columns enumerate all 32,767 nonempty subsets of the 15-vertex graph. No software calculation is used as an infinite proof; the general result rests on the rectangle-and-connectivity classification in `RESULT.md`.

The first public source date is the initial public arXiv submission date, not a later journal date. Historical priority is provisional because the complete initiating paper could not be inspected. Independent validation has not been conducted.
