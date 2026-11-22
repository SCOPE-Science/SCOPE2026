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

# Exact finite verification

Run `python3 transposition_morse.py` from the directory containing this file. The program builds the unordered transposition choices, the ordered-word face set, all incidences, a deterministic matching and an integral chain cancellation without external packages or precomputed matrices.

Actual checks: the five-letter face vector is `(5,20,48,41,10)`, 124 cells; exactly 60 matched pairs; four critical cells with dimensions `(0,2,2,3)`; every matched incidence is a unit integral pivot; the directed Hasse graph is acyclic; the critical Morse boundary is zero. The smaller values 2, 3 and 4 give the claimed critical counts and the same zero differential.

The independent `rational_rank_check.py` reconstructs the face set and all boundary matrices separately, then performs exact Fraction-based Gaussian elimination; actual boundary ranks in degrees one through four were 4, 16, 30, and 10. These corroborate but do not replace the integral Morse proof.

The accompanying `MORSE_MATCHING.json` contains the complete five-letter pairing with explicit ordered words, and is not a replacement for the generated differential or acyclicity checks. Finite exact checks provide no theorem for every alphabet size. The homotopy conclusion additionally uses the standard discrete-Morse, Hurewicz and CW attaching-map arguments in `RESULT.md`.

Independent mathematical validation has not been performed.
