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

The attached Python standard-library checker is `covariance_check.py`. Execute `python3 covariance_check.py` in a directory containing it.

It uses exact rational arithmetic to compare the closed covariance formula with direct interval and simplex-polygon integration for \(n=2\) and \(n=3\), certifies the exact signs at sample sizes \(5,6,13,14\), and checks the complete example through \(n=120\). It also numerically samples the hyperbolic-sine inequality used by the proof. The expected output terminates with `PASS 627 exact assertions or diagnostic inequalities`.

Analytic verification: the simplex translation formula supplies the joint probabilities, and strict log-concavity of \(g(x)=x(1-e^{-\delta x})/(e^{\alpha x}-1)\) follows for every real \(x>0\) from \(\sinh y>y\). Its superlevel set above one is one bounded interval or empty; no finite checker substitutes for that infinite-domain argument.

Limitations: small-\(n\) geometric integration is independent of the general algebra but does not certify arbitrarily large \(n\). Published spacings literature can contain equivalent results under different terminology. No independent audit was performed.
