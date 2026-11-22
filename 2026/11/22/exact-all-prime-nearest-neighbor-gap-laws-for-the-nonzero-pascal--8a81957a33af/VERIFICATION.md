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

Run `python3 verify_gap.py` after extracting the file from its parent scientific package. The standalone script builds exact modular Pascal rows by additive recurrence, scans successive nondivisible positions, and compares the resulting complete `Counter` with the mathematical formula. It checks the exact support size, the telescoping total distance, prime-power threshold counts at each tested depth, and independently samples original `math.comb` values up to row 159. The checker does not use the digit-pivot derivation to generate the observed histograms.

Observed command outcome: `CHECK_OK`. Test matrix: \(p=2\) with \(1\le r\le9\); \(p=3\) with \(1\le r\le6\); \(p=5\) with \(1\le r\le4\); \(p=7\) with \(1\le r\le3\); \(p=11\) with \(1\le r\le3\). Total 25 prime/depth cases. No check extrapolates finite enumeration to the unrestricted theorem. The infinite theorem follows from Lucas's congruence theorem and the exhaustive digital-successor proof in `RESULT.md`.

The verification does not test larger moduli or the threshold for all real moment exponents numerically; those are derived symbolically from the proven geometric shell law. Historical priority remains provisional. Independent audit has not been performed.
