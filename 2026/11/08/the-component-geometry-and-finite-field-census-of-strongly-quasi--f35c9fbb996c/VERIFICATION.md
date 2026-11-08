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

The symbolic proof of the geometric classification is in `RESULT.md`: it checks the spectral projection equivalence, closed finite coefficient curve, irreducible parameterization, companion-orbit/flag dimension bounds, and unique nonnilpotent eigenvalue multiplicity. The finite-field formula is derived using the classical nilpotent-matrix count and Gaussian coefficients; the fixed-field asymptotic uses uniformly summable product estimates.

`verify.py` is standalone Python using exact integers and arithmetic modulo prime fields. Execute it with `python verify.py`; the expected exact output is stored in `verification_output.txt`. It enumerates every matrix at \((q,n)=(2,1),(2,2),(2,3),(2,4),(3,2),(3,3),(5,2)\), comparing direct annihilating-polynomial tests with a separately evaluated Gaussian-binomial formula. All seven cases agree; the last line must be `VERIFY_OK`. This checker was executed again from its actual package path and its output matched the stored file byte-for-byte.

The computational tests are not a substitute for the proof, and do not verify the geometry, full prime-power range, or the asymptotic limit. Reiner's older prescribed-characteristic-polynomial enumeration dominates the numerical corollary; originality is asserted only for the component geometry and is not independently certified.
