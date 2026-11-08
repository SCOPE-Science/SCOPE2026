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
# Verification and limits

`verify.py` uses exact finite-field arithmetic and enumerates \(\mathbb F_p\)- and \(\mathbb F_{p^2}\)-points for \(p\in\{3,5,7,11\}\). Its recorded output in `verification_output.txt` ends in `ALL_CHECKS_PASSED`. It verifies explicit \(\mathbb F_p\)-square-class counts and extension-degree trace identity, using the two rational points above the poles on the quotient curves and the \(2p\) rational points on the Artin–Mumford curve above its two singular points in the affine plane closure.

The all-prime theorem and the finite group-scheme kernel claim are derived algebraically from Artin–Schreier ramification, cross norm–pullback vanishing, and principal-polarization duality; they are not certified by finite enumeration. The checker does not classify the group-scheme type, test complex/independent literature priority, or prove nonexistence of other isogenies.
