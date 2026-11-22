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

# Verification evidence

The self-contained program `verify_unipotent_toral.py` independently constructs matrices and tests the original derivation identity and \(D^2=D\), rather than accepting the simplified commutator equations as a substitute.

Full raw-matrix exhaustive checks: \((q,N)=(2,2),(3,2),(2,3)\), confirming respectively \(1+8\), \(1+9\), \(1+8\) solutions. Further coefficient and full matrix tests include \((2,4),(2,6),(4,2),(4,4)\), plus odd-characteristic checks at \((3,4),(5,2)\). These tests directly verify the rank spectra and bracket/image structure. The script prints `UNIPOTENT_TORAL_LIE_DERIVATIONS_VERIFIED` on success.

Finite checks do not establish infinite parameter ranges; the explicit proof in `RESULT.md` proves every statement for arbitrary field \(k\) and integer \(N\ge2\) as specified. No independent mathematical audit or formal verification was performed, and no uniqueness relative to inaccessible literature is claimed.
