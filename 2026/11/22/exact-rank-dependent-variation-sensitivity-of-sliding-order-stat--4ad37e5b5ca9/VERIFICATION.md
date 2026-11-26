---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

On a strict coordinate-order cone the filter is an index selector. Decomposing a perturbation into a constant plus cut steps reduces its TV operator norm to the maximum number of left/right selector transitions across a cut. Through the mixed region a shift removes a left entry and adds a right one, with clamped copies counted. The number k of right entries in the bottom q cannot decrease. At fixed 0<k<q the two bottom-group thresholds (left rank q−k and right rank k) move monotonically in opposite directions, so the selected side switches at most once, from right to left. This gives at most q between-block and q−1 within-block transitions; sign reversal gives the complementary bound. The proof may extend the centers beyond the sampled path to include the pure left/right windows for cuts near endpoints; restricting centers cannot increase variation. There are no left/right value ties under strict order, and the bound extends to any two inputs by integration along the segment and continuity. In the sharp construction, the low left values precede an increasing-value list alternating right and left. In the prefix windows the selecting rank in this list, when positive, is i−2s, with enough right entries already present (i such entries); in the late suffix windows deleting j of its initial left entries shifts the q-th survivor's original rank to q+j. Both count rules select right exactly at odd centers i>2s; q≤r+1 ensures that the suffix alone has enough entries even without extra copies of the maximum. A positive step of arbitrarily small size preserves the value order, so this pattern produces equality in TV. Negating the base values handles the complementary ranks, and constant continuation from n=2r+2 preserves the requisite first n outputs. Independent exact integer reproduction: python3 /workspace/checks/1.py; /workspace/checks/1.out. Exhausted strict orders and cuts in 60 (n,r,q) cells for n=4…7, checking equality where n≥2r+2, and checked 3264 exact positive-step witnesses for radii through 32 including longer paths. Frozen CHECKER.py was inspected, not executed. No extension of the claimed sharpness to shorter paths is inferred.

## originality

PASS

The exact attained median and end-rank coefficients are previous results on the relevant geometry (or the same min/max windows modulo repeated entries). Pass is for the noncentral intermediate ranks and their all-rank interpolation, not for those special cases, order-statistic representations, or single-input smoothing. The closest inspected findings do not supply the rank-dependent two-input transition bound and matching witness. Historical literature access is a residual risk, not negative coverage evidence.

## value

PASS

For running quantile filters the distance from an extreme, rather than just window size, controls two-input instability in TV. The exact transition law quantifies all intermediate ranks and shows in particular that going one place in from an extreme increases the factor to 3 independently of radius (with an arbitrarily small attaining perturbation). That is useful for comparing robust filters on a finite path and not implied by known median/min/max factors. No usefulness for cyclic, weighted, or multistage filters is assumed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
