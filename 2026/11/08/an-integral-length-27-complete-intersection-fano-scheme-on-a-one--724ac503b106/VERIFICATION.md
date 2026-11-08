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

# Verification and mathematical limits

Run `python3 verify.py` in the directory containing the extracted standalone verifier. It requires only the Python 3 standard library and uses exact rational arithmetic for the Sylvester determinant. It also checks the complete 17-term weighted Hilbert function (sum \(27\)), verifies the four Grassmann-chart coefficient expressions, and enumerates all projective line subspaces over fields of orders \(2,3,5,7\). The expected terminal line is `ALL_CHECKS_PASSED`; see `verification_output.txt` for actual recorded execution.

The assertion over \(\mathbf Z\) is established by the proof in `RESULT.md`. The independent determinant identity \(\operatorname{Res}(u^3+9u^2+6u+1,3u^2+6u+2)=-1\) and the direct characteristic-three ideal reduction are critical. Computations over four small fields are corroboration only, not an infinite proof. Historical priority of the integral structure has not been independently determined.
