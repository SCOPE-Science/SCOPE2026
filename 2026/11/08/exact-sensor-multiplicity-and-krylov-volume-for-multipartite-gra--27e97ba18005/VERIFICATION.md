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

`python3 CHECK.py` (Python standard library only) returns `PASS 15308 exact assertions`. Its exact rational calculations reconstruct the quotient matrix directly, compute its powers, test observation ranks by fraction-preserving elimination, verify one-sensor determinants by independent elimination, and count optimal vertex-sensor choices from all part-index subsets. Cases have two through five parts, each with size one, two or three, plus five six-part examples.

The unbounded theorem is proved in RESULT.md through the complete eigenvalue decomposition of the rank-one quotient and a monic-polynomial Vandermonde determinant. Finite calculations are supportive only and do not certify arbitrary sizes. The proof assumes noiseless discrete time samples; no noisy minimax bound or general full-graph observability is established.
