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

The standalone `verify_fixed_rips.py` was run directly using Python 3. Its exact recorded stdout appears in `verification_output.txt`. It independently enumerates binary cube words by Hamming weight for every \(1\leq n\leq10\) and every \(0\leq r<n\), directly tests within-orbit and between-orbit distances, and compares the resulting complete compatible weight-layer graph with the closed formula. It enumerates the fixed-orbit simplicial complexes, calculates augmented mod-two boundary ranks, and checks that their unique nonzero reduced Betti number is in dimension \(\lfloor\lfloor r/2\rfloor/(n-r)\rfloor\). Separately, every prescribed neighborhood inclusion and final matching is checked for \(0\leq a\leq60\), \(1\leq t\leq20\), and complete free-pair collapse sequences are replayed for \(0\leq a\leq6\), \(1\leq t\leq4\).

The program reports `FULL_WEIGHT_ORBIT_COMPARISONS_OK 55`, `EXACT_MOD2_FIXED_HOMOLOGY_CHECKS_OK 55`, `ALL_CANONICAL_BAND_FOLD_SEQUENCES_OK 1220`, `EXPLICIT_ELEMENTARY_INDEPENDENCE_COLLAPSES_OK 28`, and `ALL_SCALE_COORDINATE_FIXED_SPHERES_VERIFIED`. No numerical result is extrapolated to infinite parameters: the proof's orbit-distance identities and recursive neighborhood domination establish the full classification. The complement-degree conclusion uses the Lefschetz theorem and the established integral sphere homotopy, not merely a mod-two check. Independent audit has not been performed.
