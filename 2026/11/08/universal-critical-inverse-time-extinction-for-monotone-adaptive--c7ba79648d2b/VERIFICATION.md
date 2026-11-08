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

Run `python verify.py` using SymPy and SciPy. Its actual execution printed `VERIFY_OK`. Exact symbolic checks verified the contact-response derivative, the critical amplitude identity, and the decoupled Riccati solution. Finite-time LSODA solutions were tested to time \(t=200000\) for five monotone feedback laws, including \(b(0)=0\). The observed relative errors in the predicted scaled prevalence amplitude were below \(2.4\times10^{-5}\), and each scaled contact-correction discrepancy was below \(0.005\).

These checks do not certify every function or infinite time. The theorem's universal and asymptotic claims follow from the comparison and tracking argument in `RESULT.md`, not from extrapolating finite simulations. No independent external audit has occurred.
