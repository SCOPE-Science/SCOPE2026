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

# Reproducibility of the finite-field synthesis calculation

Execute `python checker.py` with Python 3 standard library, from the directory containing this file. The program directly forms Fourier transforms for supports on two coordinate axes over fields of orders \(2,3,5,7,9,11\). The nine-element field is implemented as \(\mathbb F_3[t]/(t^2+1)\); no arithmetic assumptions beyond character orthogonality are needed in the analytic proof. The check compares the predicted three-value Fourier spectrum, the exact synthesis quotient, 720 seeded random complex-supported functions, and rational order-nine identities. The recorded result was `PASS 734 supplementary checks; prime-field and nine-element-field cases`.

For an independent hand computation at \(q=9\), the optimizer equals \(-1/15\) at the origin and \(1/15\) at each of the other sixteen support points. The unnormalized Fourier spectrum has one value \(1\), sixteen values \(2/5\), and sixty-four values \(-1/5\). Their fourth powers sum to \(189/125\), giving \(\mathcal C_4=(125/189)^{1/4}\).

The infinite family is established by the explicit two-orbit averaging and strictly convex one-variable polynomial proof in RESULT.md, not by finite numerical experimentation. No external independent audit is claimed.
