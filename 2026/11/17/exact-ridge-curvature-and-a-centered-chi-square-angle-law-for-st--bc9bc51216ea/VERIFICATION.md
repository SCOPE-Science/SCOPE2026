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

Run `python star_ridge_verify.py` in this directory (Python standard library only). The checker reconstructs facet normals independently with exact rational coordinates and rebuilds every ridge Gram determinant from the corresponding signed root vertices. It enumerates all \(768\) unoriented ridges for \(2\le d\le7\), checks their squared areas and exact exterior-angle tangents, and checks class multiplicities over \(15\) finite spectral classes. It separately evaluates the exact curvature sum for \(d=30,100,300\) and compares the calculated first-order coefficient with \(-5/6\).

Expected terminal line: `STAR_RIDGE_PASS exact_ridges= 768 exact_spectral_classes= 15 curvature_checks=3`. All such checks executed successfully before review. The checker tests finite cases and cannot prove the full theorem, the limiting chi-square distribution, or priority. The complete unrestricted argument is in `RESULT.md` using exact facet-normal and ridge-Gram identities, the ordinary central limit theorem, uniform moment bounds, and an exponentially small binomial-tail remainder. Independent audit has not been performed.
