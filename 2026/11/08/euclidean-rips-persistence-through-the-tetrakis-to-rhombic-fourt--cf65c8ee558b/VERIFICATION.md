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

# Reproducibility
Run `python verify.py` in this directory with Python 3 (standard library only). The script reads the standalone `collapse_certificate.json`, reconstructs all 14 vertices and their 91 squared distances, enumerates nonempty flag faces, and checks both explicit relative collapses face by face. The 32-pair collapse ends exactly at the preceding two-sphere; the 80-pair collapse ends at the induced eight-corner four-fold join. It separately verifies the sphere vertex links, complete join at the fifth shell, cone at the axial-antipodal shell, and mod-two boundary ranks at all five nontrivial stages.

`verification_output.txt` stores the exact output of the packaged checker. Algebraic ordering inequalities in `RESULT.md` extend the combinatorial certificates from the representative rational point \(t=3/2\) to all real \(3/2\le t\le2\); at \(t=2\) the third and fourth shells coincide, and at \(t=\sqrt3\) the last two death shells coincide. Finite computation alone is not presented as a proof for the continuum. No independent audit or arbitrary-perturbation validation has been performed.
