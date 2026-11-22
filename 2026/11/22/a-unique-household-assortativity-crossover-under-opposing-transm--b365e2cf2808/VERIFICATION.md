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

# Reproduction and scope

The self-contained standard-library program `verification.py` was executed with `python3 verification.py` and returned `PASS`. It checks the identity \(F_4(x)=(x-1)^2Q(x)\), exact rational values and strict comparisons of two calibrated epidemic thresholds, an interval bracketing the unique crossing, and additional floating-point consistency cases for several trait contrasts.

The witness at \(x=3/4\) has \(R_{\mathrm{same}}=431/416\) and \(R_{\mathrm{mixed}}=1-(3/4)^{16}/13\) for global multiplier \(2/13\). At \(x=1/2\), \(R_{\mathrm{same}}=31/32\) and \(R_{\mathrm{mixed}}=17/16-2^{-20}\) for global multiplier \(1/8\). The root is bracketed in \((13/20,2/3)\).

The universal theorem for every real \(r>1\) is **not** inferred from experiments: the proof in `RESULT.md` establishes it analytically using the strict convexity of \(h_r(y)=1-2y+y^{r+1}\). Source Eq. (4.1) is assumed as a published premise. No finite-population stochastic simulations or independent audit were performed. Historical priority is subject to the explicit limitations in `REVIEW.md`.
