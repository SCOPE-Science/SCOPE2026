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

# Verification summary

`checker.py` is a standalone Python standard-library program. Run `python checker.py` in the same directory. It enumerates all row tables compatible with the local conditions, combines them under P5 and then checks original P1–P5, ID and SC on every resulting T-operation, retaining those satisfying DNI. It recomputes all graph fibres and orbits under every automorphism. Expected output begins `F_PRECONDITIONAL_BOOLEAN3_OK` and includes `T= 7820 F= 1021` and `isomorphism_classes= 194`.

The all-carrier graph-polarity statement is proved in `RESULT.md` from self-adjoint antitone negation; finite exhaustive enumeration only verifies the three-atom carrier. For the finite row-count proof the four graph cases are analyzed explicitly. The orbit computation is independently reproducible from the embedded code, but no external verification or historical-priority audit has been performed.
