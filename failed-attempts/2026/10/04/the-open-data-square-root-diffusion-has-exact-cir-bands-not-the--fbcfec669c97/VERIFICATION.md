---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Substituting constant equilibrium controls gives \(dK_t=(A-\delta K_t)dt+\sigma\sqrt{K_t}\,dW_t=\delta(A/\delta-K_t)dt+\sigma\sqrt{K_t}\,dW_t\), exactly the classical CIR form. Gordy's primary full text states the conditional transition is noncentral chi-square and the stationary univariate law is Gamma with shape \(\theta/\nu\) and scale \(\nu=\sigma^2/(2\kappa)\). Under \(\kappa=\delta,\theta=A/\delta\), this gives shape \(2A/\sigma^2\) and scale \(\sigma^2/(2\delta)\). The source's printed formula is independently evidenced as assuming Normality and using \(1.96D[K_t]\) after defining \(D\) as variance. Fresh SciPy evaluation at the paper's Nash parameters gave \(A=2.4\), Gamma\((30,0.8)\), mean 24, variance 19.2, quantiles 16.1926992171 and 33.3190699509, and source-band exact coverage 0.999999999676259. The frozen standard-library verifier independently agrees.

## originality

FAIL

The source-specific diagnosis is correct, but the mathematical content is directly covered by stronger classical theory. Gordy's full primary text states the exact CIR SDE, the noncentral-chi-square transition law, and the Gamma stationary law for every process of this form. The Fan et al. equilibrium state equation is literally obtained by parameter substitution into that general theorem. Once this identification is made, the stationary parameters and exact interval are routine specialization, while replacing variance by standard deviation in a Gaussian interval is elementary. Under the required implication-based originality rule, the final mathematical claim is therefore a direct application of prior general coverage, even though it exposes an error in the applied paper.

## value

FAIL

Correcting an applied paper's uncertainty band is useful, but the mathematical work here is a direct textbook identification of a standard CIR SDE, application of its classical distribution theorem, and routine Gamma quantile evaluation; the second error is the elementary distinction between variance and standard deviation. Under the common value bar, this does not supply a new structural lemma, boundary phenomenon, classification, or nontrivial invariant beyond the covered general theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
