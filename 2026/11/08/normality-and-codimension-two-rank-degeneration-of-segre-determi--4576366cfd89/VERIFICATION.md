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

# Verification and mathematical scope

**Main proof checks:** The hyperplane incidence has pure dimension \(M+n(d-1)\) and is irreducible by connected generic hyperplane sections and fiber-dimension purity. Full rank \(M\) is explicitly attained using coordinate Segre points. Over rank \(M\), projection from incidence has a regular inverse given locally by maximal nonzero minors. The rank-defect inverse image is proper and has fibers of dimension at least one, hence its image has codimension at least two. The tangency conormal has dimension \(M-1\), and the locus where a selected point is tangent to its containing hyperplane has codimension at least \(d\ge2\). This ensures \((R_1)\); source-proved Cohen--Macaulayness supplies \((S_2)\).

**Finite replay:** Run `python3 verify.py` to verify, in exact rational arithmetic, the rank-\(M\) coordinate-witness construction and dimension formulas on six finite parameter choices. This replay does not establish Bertini irreducibility, Cohen--Macaulayness, or infinite normality, all of which depend on the written mathematical proof and stated published premise.

**Unverified extensions:** Normality of the full affine multicone, a complete singular-locus description, and any independent audit or historical uniqueness certification are not claimed.
