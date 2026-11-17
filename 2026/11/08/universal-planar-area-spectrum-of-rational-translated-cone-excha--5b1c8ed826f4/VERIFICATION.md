---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

At height y, direct three branch formulas identify the horizontal transformation as first return to J_y of circle rotation by λ on length 1+λ; the deleted circular interval has length c=λ y/y*. For λ=p/q, the primitive rotation period N=p+q forms N equispaced points of gap 1/q. In a deletion of length (k+θ)/q the grid loses k or k+1 points with phase fractions 1-θ,θ, giving return periods N-k,N-k-1. Lebesgue sampling of starting points requires size weighting by retained orbit size, so horizontal lengths are (1-θ)(N-k)/q and θ(N-k-1)/q. Uniform c scaling with y integrates each height band to weights 1/2 at endpoints, 1 in middle; total area y*(2q+p)/(2q) yields exact formula, with y* canceling all angles. Irrational rigid rotation and its induced interval exchange prove minimal/unique ergodic on each slice. Independent rational algebra checks p/q=1/2,2/5,3/7,4/9,5/11, including 2/5 fractions 7/24,1/2,5/24. These examples are not the all-p,q proof.

## originality

PASS

The original Cockram–Ashwin–Rodrigues 2023 paper (full relevant updated §3 inspected) supplies the invariant interpolation trapezium, exact 3-IET, and boundary map. Those are premises, not new results. General induced-circle-rotation theory explains periodicity, but the normalized planar law must weight each grid phase by retained number of points and integrate over heights; the primary source and Resultary searches did not show these explicit area proportions or angle independence. Unread broader IET period literature remains priority risk.

## value

PASS

The full natural-area least-period distribution is a genuine dynamical invariant of the invariant trapping polygon, not merely a small sample orbit census. Its exact angles-independence and universal p/q weighting give a reusable physical-space statistic beyond standard rational circle-return qualitative periodicity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
