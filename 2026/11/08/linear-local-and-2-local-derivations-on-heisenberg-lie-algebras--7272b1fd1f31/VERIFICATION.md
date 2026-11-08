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

# Verification record

Execute `python3 verify.py` with Python 3 (standard library only). The recorded stdout in `verify_output.txt` was obtained by execution of that checker. It tests the original derivation identity, witnesses at all ordered input pairs in the three-dimensional characteristic-two case, random characteristic-three cases, isotropic-pair constraints in a four-dimensional symplectic quotient, and Gaussian rank counts. See the final line `ALL_CHECKS_PASS`.

The verification program exhausts the finite cases it labels exhaustive. Its random tests do not establish universal statements; the standalone proof in `RESULT.md` supplies the unrestricted quantifiers. No independent audit has been performed.
