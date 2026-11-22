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

The included `check_tolerance.py` independently generates faces from the deletion condition and computes simplicial incidence-matrix ranks over prime fields of characteristics 2, 3 and 5, without using the claimed graph-of-spaces decomposition as a subroutine. Ten block-size configurations (all block sizes positive) were tested, yielding 30 exact field homology comparisons and no discrepancies. In each test, all nonzero homology occurs in dimensions zero, one and two, in the predicted ranks. Run `python3 check_tolerance.py` in the extracted package.

The proof of the infinite and integral homotopy assertions is the explicit cone-cover and CW homotopy-pushout proof in `RESULT.md`, not finite enumeration. Equivariance is asserted only for integral homology under permutations within blocks, not for an equivariant wedge splitting. Priority comparison is based on inspected literature and searchable records; no claim of independent external certification is made.
