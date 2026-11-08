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
# Reproducibility and limitations

Run `python3 check.py` with Python 3.9 or later, standard library only. It reconstructs the exact four circles from three-point systems, verifies positive crossings and the exact fractions, and proves the nontrivial multiplier exceeds \(24\) with a conservative bound obtained from \(\psi_i<2\pi\). The additional approximate angle calculation is illustrative, not a proof substitute. No original-time trajectory integration or independent audit is claimed. The formal source article's extra admissible-strip premise was not verified, so the consequence is carefully restricted to local transverse repulsion of the exact crossing orbit.
