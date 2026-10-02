# FAILED ATTEMPT — NOT A VALIDATED FINDING

## Scientific reason

The retained mathematical derivation was reassessed on correctness, originality, and value.

- Correctness: PASS. The exponential-tilt calculation was reconstructed. For the lower tail, writing \(m=\lfloor nr\rfloor\), \(\theta=\{nr\}\), and tilting to mean \(nr\) gives an exact factor \(e^{-nI_n(r)}e^{t_n(\theta+j)}\) at \(S_n=m-j\). A uniform lattice local limit theorem under probabilities bounded away from 0 and 1 then yields the weighted geometric coefficient \(e^{t\theta}[\theta/(1-e^t)+e^t/(1-e^t)^2]\); the remote tail is geometrically negligible. Weak convergence of empirical parameter measures gives the profile limit by uniform continuity/strict convexity. Finally, evaluating the heterogeneous Legendre transform at the homogeneous saddle and using strong concavity of \(x\mapsto\log(1-(1-e^t)x)\) gives exactly the displayed variance penalty. Complementation gives the upper-tail case.
- Originality: FAIL. The final claim does not clear the required originality bar. Chaganty–Sethuraman give strong large-deviation and local-limit theorems for lattice-valued arbitrary random variables under moment-generating-function conditions; bounded heterogeneous Bernoulli arrays are a direct specialization. Madsen et al. explicitly treat the Poisson-binomial law by saddlepoint approximation and report uniform relative error under regularity conditions. Elezović's full 2026 paper explains that a stop-loss weighted tail is obtained from the same saddlepoint/local-tail machinery and that complete weighted-tail expansions follow from tail expansions. The package's leading weighted geometric coefficient is therefore a routine lattice specialization of that general theory. Its profile limit is continuity of the cumulant generating functions, and its explicit heterogeneity-rate inequality is an elementary strong-concavity refinement evaluated at the homogeneous saddle. Combining these standard implications does not create an original theorem under the user's C/O/V rule.
- Value: FAIL. The formulas are correct and potentially useful, but the audited contribution is a specialization of established strong saddlepoint/local-limit machinery plus an elementary strong-concavity inequality. Under the required value bar, correctness, explicitness, and a quantitative restatement of Hoeffding-type heterogeneity do not by themselves make this a substantive new mathematical gap.

Acceptance requires all three axes to pass, so this package is not publication-ready.

## Preserved evidence

The original result, slogan, metadata history, and reproducibility files remain preserved with this failed attempt. The dated audit files record the literature comparisons, source inspections, and residual risks.
