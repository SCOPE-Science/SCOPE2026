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
# Verification

The result is proved symbolically for every integer \(n\ge3\) and real \(\theta>0\) in `RESULT.md`, using exact Ewens contraction/deletion identities and rational factorization. Its fixed-index and inversion-pair covariance claims are each reduced to explicit conditional probabilities. A polynomial sign argument establishes strict aggregate negativity; rational asymptotic expansions establish the stated fixed-parameter and near-uniform scaling limits.

For an independent finite check of algebraic specializations, run `python3 verify.py` with standard Python 3. It enumerates all permutations up to \(n=7\) and checks Ewens-weighted means and location-resolved covariances at six rational parameters; an additional enumeration up to \(n=6\) verifies every selected-fixed-point/inversion-indicator covariance at four rational parameters. The actual run printed `VERIFY_OK 1672 exact assertions`. No external packages or machine-generated proof certificates are needed. Since finite enumeration cannot establish all \(n\), the analytic proof remains essential.

**Limits.** No claim of a new inversion marginal formula, probabilistic independence or complete historical priority is made. At the vanishing leading crossover coefficient, consult the exact finite-n formula rather than inferring a sign from the limit. Independent evaluation has not been performed.
