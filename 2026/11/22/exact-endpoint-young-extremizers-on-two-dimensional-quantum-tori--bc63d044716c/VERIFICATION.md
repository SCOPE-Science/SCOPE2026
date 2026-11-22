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

Run `python VERIFY.py` from the extracted file directory with Python 3.11 or later; no third-party packages are required. The script checks 4,257 finite exact integer/cocycle and illustrative phase identities and prints a `VERIFY_OK` marker. The half-deformation two-generator witness is also derived exactly from Pauli anticommutation, yielding norms \(1+\sqrt2\) and \(3\) for the nonisotropic and isotropic three-point supports respectively.

The independent analytical proof in `RESULT.md` is essential: finite checks do not prove the asserted equivalence for all finite supports, real deformation parameters, or coefficient values. In particular, commutator isotropy is established through a norm-attaining state/GNS argument; sufficiency uses Haar joint spectral support under the canonical faithful trace. No independent mathematical audit has been performed.
