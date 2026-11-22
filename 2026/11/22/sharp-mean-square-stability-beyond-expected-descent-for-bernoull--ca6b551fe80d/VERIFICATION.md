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

# Reproducibility and limits

Run `python verify.py` after installing the package listed in `requirements.txt` with a standard Python 3 environment. The script symbolically checks the covariance determinant, both exact stability-boundary identities, the strict expected-descent gap and three parameter derivatives. It independently constructs \(\mathcal T(T)\) and \(\mathcal T(U)\) by enumerating every mask with exact rational arithmetic across \(72\) sample parameter choices; it also checks spectral-radius inequalities in \(360\) numeric parameter/stepsize combinations. The masks are independent in coordinates and steps. All scientific conclusions outside these cases depend on the written analytic proof; finite checks are not extrapolated to an infinite certificate. Independent mathematical and historical-priority audit has not been performed.
