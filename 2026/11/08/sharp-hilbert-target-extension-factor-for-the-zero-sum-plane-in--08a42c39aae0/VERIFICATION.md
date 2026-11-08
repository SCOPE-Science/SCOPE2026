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

# Reproducibility and verification

Run `python3 checks/verify.py` from the extracted package directory. It makes 18,002 finite numerical assertions (three geometric inequalities over 6,000 test pairs and two equilateral sharpness assertions). The scalar center computation is built directly from pairwise distances and the circumcenter equations; there are no external Python dependencies.

Independent exact algebra confirms \(4t(1-9\|o-G\|^2)=-(t-z)(t-9z)\) after normalizing the longest side to length two. The target pair \(u=(1,0)\), \(v=(1/2,\sqrt3/2)\) gives an exact squared centroid radius \(4/3\). These checks are corroboration; the universal statement is proved analytically in `RESULT.md`.

No third-party mathematical audit or historical publication-priority certification has been performed.
