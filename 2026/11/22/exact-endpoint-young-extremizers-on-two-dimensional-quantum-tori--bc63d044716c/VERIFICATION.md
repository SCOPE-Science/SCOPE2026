---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and limitations

Run `python3 VERIFY.py` from the extracted file directory; no third-party packages are required. The script checks bounded exact cocycle and lattice identities and the arithmetic in the half-deformation example, and prints a `VERIFY_OK` marker. The half-deformation example in `RESULT.md` obtains the canonical torus norms by comparing all central phases. The nonisotropic support has norm \(\sqrt6\), not the norm \(1+\sqrt2\) of its single unshifted Pauli fiber. The isotropic support has norm \(3\).

The analytical proof in `RESULT.md` is essential: finite checks do not prove the asserted equivalence for all finite supports, real deformation parameters, or coefficient values. In particular, commutator isotropy is established through a norm-attaining state/GNS argument; sufficiency uses Haar joint spectral support under the canonical faithful trace.
