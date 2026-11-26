---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Conditioning on the chosen parent of degree d, the edge increment is an independent Bernoulli(r) plus Binomial(d,p). The mean gives the a_n recurrence and centered martingale. The old-vertex contribution to the degree-square increment has conditional mean r(2d+1)+p sum_{w~parent}(2deg(w)+1); the newborn square contributes r+[p(1-p)+2rp]d+p^2d^2. Uniform averaging gives exactly the d_n recurrence. Total variance over the parent and then the old graph cancels the two terms in 4p^2 v_n/n^2, giving the displayed b_n. The pointwise mean-square inequality for degrees, followed by Jensen, ensures b_n>=r(1-r)+2p(1-p)a_n/n. The forcing is nonzero by n=2 for r<1 in the variance itself, or by n=3 for r=1, where the variance is p(1-p). For p<=1/4 the first two moment exponents are below one; normalizing the linear recurrences by n gives c and D, hence positive forcing limit sigma^2. Summing the variance recurrence with exponent 4p<1 or at 4p=1 gives the stated n and n log n limits. For p>1/4 the forcing grows at most as n^max(0,2p+p^2-1) times a squared logarithm by iteration. After division by F_(n+1) the exponent is less than -1 since 4p>1 and 2p+p^2<4p. The product solution and gamma asymptotics give the positive supercritical constant. The squared L^2 norm is v_n/H_n^2, giving convergence by the L^2 martingale theorem above the threshold and unbounded second moments at and below it. As a hand check at p=1/4,r=1, the step from the one-edge graph yields a path or triangle with probabilities 3/4,1/4, so (a_3,d_3,v_3)=(9/4,15/2,3/16), matching the recurrences. checker.py was inspected, not executed; python3 checker.py replays the reported finite checks, not the infinite proof.

## originality

PASS

The quarter boundary, the three predicted r=1 scales, and the r=1 subcritical/critical coefficient are credited to Bhat et al. Their variance equation already uses the same degree-square input, and their degree evolution supplies the related r=1 degree-moment machinery. The distinct result is a rigorous closed recurrence treatment in the whole stated interior copying range with variable parent-link probability, yielding positive sharp variance limits, an exact supercritical amplitude series and the nondegenerate L^2 limit for the corresponding centered martingale. The strongest inspected same-process rates are for bounded statistics and do not give these sharp edge-count limits.

## value

PASS

For a natural global statistic of a copying graph, a rate prediction and bounded-observable inequalities leave open whether the leading variance is positive and whether normalized historical fluctuations persist. The exact closure and summable forcing settle both questions for the immigration model, including the logarithmic threshold, with a computable leading series in the supercritical regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
