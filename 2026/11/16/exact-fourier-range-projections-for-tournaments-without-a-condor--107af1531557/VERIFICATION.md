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

The attached `check_tournaments.py` runs independent exact-integer orientation enumeration and full Walsh butterflies at orders \(3,4,5,6\). It separately calculates the projection kernel by Fourier inversion and by counting graph edges and isolates, checks rank and every nonzero multiplier's magnitude, and checks inclusion–exclusion for graphs without isolates. The last successful output line is `NO_CONDORCET_TOURNAMENT_WALSH_PASS`.

The direct butterfly checks cover \(2^3+2^6+2^{10}+2^{15}=33864\) frequency positions. The exact inclusion–exclusion expression is additionally evaluated through order \(20\) without enumerating all orientations. The infinite claims rely on the proof in `RESULT.md`, including the disjoint-face Fourier argument, translation averaging, exact inverse transform, and Gaussian limit; finite examples are not substitutes for those proofs. No independent audit or third-party certification is claimed.
