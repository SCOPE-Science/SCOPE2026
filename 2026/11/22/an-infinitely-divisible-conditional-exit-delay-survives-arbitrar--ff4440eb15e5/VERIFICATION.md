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

Run `python verify.py` in a directory containing the embedded script. Python 3 standard library is sufficient; the script prints a final PASS count only if its numeric identities satisfy the stated tolerances. It verifies 120 checks concerning renewal cancellation, the conditioned first-hitting-time transform, finite hyperbolic-product approximations, positivity of the cumulant expressions, and known \(r\downarrow0\) limits. The first-moment spectral approximation is finite and uses an explicit nonzero truncation tolerance. A numerical truncation is not proof of an infinite identity.

The mathematical proof of the claim relies instead on a killed-diffusion Dirichlet problem, exact renewal summation, a conditioned Brownian hitting-time law, the convergent Euler product for hyperbolic sine, Tonelli's theorem, and a positive Lévy–Khintchine representation. The independent series has finite expected total size, guaranteeing almost-sure convergence; no computation is used to assert that fact. Testing finitely many parameter choices cannot prove universality. Nonexponential resetting and nonregenerative returns are not covered. Literature priority remains subject to further human inspection, especially where full text was unavailable.
