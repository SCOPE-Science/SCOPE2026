---
audit_date: 2026-10-01
status: failed
---

# Scientific audit

## Final claim

For uniformly nondegenerate heterogeneous Bernoulli triangular arrays at a prescribed center separated from the mean, the Poisson-binomial stop-loss has the stated lattice saddlepoint asymptotic; empirical probability profiles give limiting saddle/rate/prefactor data; and, at fixed mean, the heterogeneous large-deviation rate exceeds the equal-probability binomial rate by the stated explicit multiple of the empirical variance.

## Correctness — PASS

The exponential-tilt calculation was reconstructed. For the lower tail, writing \(m=\lfloor nr\rfloor\), \(\theta=\{nr\}\), and tilting to mean \(nr\) gives an exact factor \(e^{-nI_n(r)}e^{t_n(\theta+j)}\) at \(S_n=m-j\). A uniform lattice local limit theorem under probabilities bounded away from 0 and 1 then yields the weighted geometric coefficient \(e^{t\theta}[\theta/(1-e^t)+e^t/(1-e^t)^2]\); the remote tail is geometrically negligible. Weak convergence of empirical parameter measures gives the profile limit by uniform continuity/strict convexity. Finally, evaluating the heterogeneous Legendre transform at the homogeneous saddle and using strong concavity of \(x\mapsto\log(1-(1-e^t)x)\) gives exactly the displayed variance penalty. Complementation gives the upper-tail case.

**Evidence.** RESULT.md; Chaganty–Sethuraman, Annals of Probability 21 (1993); Madsen et al., BMC Bioinformatics 18 (2017); Elezović, arXiv:2609.19064

**Residual risk.** The first-order asymptotic assumes the stated uniform nondegeneracy and fixed separation from the mean; moderate-deviation and sparse regimes are not covered.

## Originality — FAIL

The final claim does not clear the required originality bar. Chaganty–Sethuraman give strong large-deviation and local-limit theorems for lattice-valued arbitrary random variables under moment-generating-function conditions; bounded heterogeneous Bernoulli arrays are a direct specialization. Madsen et al. explicitly treat the Poisson-binomial law by saddlepoint approximation and report uniform relative error under regularity conditions. Elezović's full 2026 paper explains that a stop-loss weighted tail is obtained from the same saddlepoint/local-tail machinery and that complete weighted-tail expansions follow from tail expansions. The package's leading weighted geometric coefficient is therefore a routine lattice specialization of that general theory. Its profile limit is continuity of the cumulant generating functions, and its explicit heterogeneity-rate inequality is an elementary strong-concavity refinement evaluated at the homogeneous saddle. Combining these standard implications does not create an original theorem under the user's C/O/V rule.

**Equivalent formulations.** The package notation rewrites the standard exponential tilt and lattice prefactor for the specific stop-loss weight.

**Broader coverage.** Those results dominate the first theorem's probabilistic mechanism; the package adds only the immediate linear-weight summation.

**Exact database or table.** Coverage is theorem-level.

**Claim versus prior implication.** Each component of the final claim is mechanically implied by established general asymptotics plus elementary calculus, even if the exact heterogeneous formula is not printed verbatim in one source.

### Source inspections

- **Elezović, arXiv:2609.19064** — full paper through the prescribed-center stop-loss expansion and discussion of prior saddlepoint/weighted-tail theory. Explicitly states that weighted stop-loss expansions follow from known tail expansions; its new contribution is closed-form higher coefficients in the homogeneous binomial case.
- **Chaganty and Sethuraman, DOI 10.1214/aop/1176989136** — abstract plus institutional PDF retrieval; scanned PDF text beyond the cover was not extractable in this audit. Abstract states strong large-deviation and local-limit theorems for arbitrary lattice-valued random variables, broader than Poisson-binomial sums.
- **Madsen et al., DOI 10.1186/s12859-017-1614-z** — full open article sections on the Poisson-binomial example and saddlepoint relative error. Directly applies saddlepoint approximation to heterogeneous Bernoulli sums and states relative-error control under regularity conditions.

**Checked sources.** https://arxiv.org/abs/2609.19064; https://doi.org/10.1214/aop/1176989136; https://doi.org/10.1186/s12859-017-1614-z; https://doi.org/10.1007/BF02465434; semantic search of the public findings corpus

**Residual risk.** The rejection does not assert that every displayed coefficient appears verbatim in an older paper; it rests on the stronger general-theorem implication required by the audit rule.

## Value — FAIL

The formulas are correct and potentially useful, but the audited contribution is a specialization of established strong saddlepoint/local-limit machinery plus an elementary strong-concavity inequality. Under the required value bar, correctness, explicitness, and a quantitative restatement of Hoeffding-type heterogeneity do not by themselves make this a substantive new mathematical gap.

**Residual risk.** A genuinely new optimal heterogeneity inequality, a regime beyond existing saddlepoint hypotheses, or a nontrivial higher-order heterogeneous expansion could warrant a new audit, but those are not the final claim here.

## Disposition

FAILED. Acceptance requires PASS on correctness, originality, and value.
