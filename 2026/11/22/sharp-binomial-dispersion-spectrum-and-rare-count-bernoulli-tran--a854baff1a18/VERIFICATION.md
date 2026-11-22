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

# Verification notes

The analytical proof in `RESULT.md` establishes the range and all limits. To replay finite rational and asymptotic implementation checks, execute `python check_dispersion.py` using Python 3 and no external dependencies.

The checker evaluates rational rising-factorial beta-binomial masses; normalizes weighted probabilities with \(q=t\sigma\); tests exact variance ratios; and checks the coefficient of the fixed-tilt \(\beta^{-1/2}\) TV limit numerically for selected values. It passed 428 test groups. The rational identity
\[
R_2(1,100,50\sigma)=\frac{2329513809177953}{9120943935192402}
\]
was independently obtained from a finite exact rational sum in the checker. These checks do not replace proof of universal claims, uniform-in-parameter bounds, or historical originality. Asymptotic error terms are not claimed to be uniform in \(q\).
