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

# Verification

The proof uses: (i) uniqueness of affine extensions at rank at least two; (ii) extension-multiplicity correction for empty maps and rank-one maps; (iii) forest edge count for translations; (iv) disjoint 2-orbit count for reflections; (v) an independent-bit suppression bound for nonidempotent commuting pairs. These are written and proved in `RESULT.md`.

Run `python check_commutation.py`. The script enumerates every distinct finite-chain partial isometry for sizes \(2\le n\le7\), computes every partial-map composition, counts all commuting pairs and idempotents, and checks the exact idempotent-containing census and known total size. `check_output.txt` is the actual recorded standard output of the run, including all checked values. Finite enumeration does not prove any statement for arbitrary \(n\); the general proof is combinatorial.

No theorem about exact nonidempotent–nonidempotent commuting counts, best exponential rate, or all symmetric inverse monoids is asserted. Independent review has not been conducted.
