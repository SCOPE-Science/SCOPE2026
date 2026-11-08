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

# Verification scope

The analytic proof in `RESULT.md` establishes all claimed infinite-time limits. The attached `verify.py` is independently executable with Python 3, SymPy and SciPy; execution command: `python verify.py`.

The program checked the Taylor coefficients \(-cy^3+dy^5\) with \(c=1/3-k_x\), \(d=2/15-k_x\), the mixed linear coefficient \(k_ppy\), and exact rational identities for the example \(\beta=1/2\), \(k_p=1/2\), \(k_x=1/6\), \(\tau_x=1\). It integrates the original smooth \((y,\log p)\) equations with controlled tolerances as a finite-time consistency check. The recorded output includes `VERIFY_OK`, asymptotically stabilizing estimates of the finite \(K\), and the expected \(\sqrt3\) coefficient in \(\log p\).

The finite integration does not prove asymptotic convergence, globality, existence of the positive prefactor, or novelty. Those scientific limits are addressed by the proof and literature comparison, respectively. Independent external validation has not been performed.
