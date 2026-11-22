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

# Verification of the positive escape-scattering theorem

The proof in `RESULT.md` is self-contained once the explicitly stated recurrence and elementary properties of exponentials are given. In particular, \(P'(x)=-k/(H+x)^2\) and \(P(x_*)=0\) reconstruct the unique positive equilibrium, and the strict wedge inequalities yield a bound of the form \(x_n\le x_0\exp(n-B(q^n-1))\) for an explicit \(B>0\), which implies the weighted summability needed for both amplitudes.

The series for the first amplitude is absolutely convergent because \(\sum x_n<\infty\). The delicate step for the second amplitude is not just \(y_n/(Le^{sn})\to1\): it is \(\sum|y_n-Le^{sn}|<\infty\), derived explicitly by reversing the order of the positive tail series and invoking \(\sum e^{sn}x_n<\infty\). This and \(\sum x_ny_n<\infty\) guarantee an absolutely summable error when the prey logarithmic recurrence is integrated. Therefore no finite experiment is used to justify an infinite limit.

Execute `python verify.py` from the extracted package. The diagnostic script uses exact rational arithmetic to verify the witness and Jacobian inequalities, and 90-digit arithmetic to compare finite approximations to the limiting amplitudes at two cutoffs. Successful execution prints `REFUGE_ESCAPE_VERIFY_OK`. A cutoff comparison is not an exhaustive proof. Independent audit has not been performed; the evaluation documented here is the self-review only.
