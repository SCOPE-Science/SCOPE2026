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

The proof is all-dimensional and uses the standard parabolic-double-coset maximal-representative lemma. The following finite computations are checks, not a substitute for that lemma or the infinite proof.

- `python3 check_hecke.py` exhaustively enumerates each permutation in \(S_n\) for \(3\le n\le9\).
- Left and right products with each relevant generator are computed directly by bubble antisorting of values versus positions.
- Independently, each permutation is classified into the two allowed one-generator cases; the direct products and classification are compared for every permutation and relevant index.
- The four two-generator strata are counted separately and matched against the factorial/double-coset formulas.
- The checker output is in `checker_output.txt` and was actually produced by replaying the included script.

No external independent audit has been performed. The exhaustive checks do not cover \(n>9\); validity for all sizes rests on the stated combinatorial proof.
