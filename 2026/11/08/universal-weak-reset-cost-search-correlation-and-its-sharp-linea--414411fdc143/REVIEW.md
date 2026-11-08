# Review of the weak-reset cost–search correlation theorem

## Correctness

**PASS.** The stopped Brownian resolvent and absorption transform are explicit. Differentiating the geometric renewal transform gives exact finite-rate first- and second-moment expressions and a strictly positive covariance identity. Splitting the resolvent at the reset point isolates a Laplace integral of the cost, whose regularly varying asymptotics and weighted derivative give the claimed universal Pearson limit. Strict logarithmic concavity of the gamma expression is proved by the trigamma duplication relation and monotonicity. The standalone numerical checker reconstructs the moment identities at finite rates. Numerical testing is not substituted for the all-parameters proof.

## Originality

**PASS, qualified.** Sunil et al. (arXiv:2304.09348, Sections 2–6 and Appendices A–D) already derive the full joint renewal transform and study cost means and cost tails. The present claim is not that transform, but the specific regularly varying cost–time correlation limit and its sharp maximizing growth exponent. The inspected text does not state a corresponding Pearson theorem; mathematical implication requires additional asymptotics and a nontrivial optimization. Related finite-return papers (arXiv:2201.01829, arXiv:2407.02071) analyze different clocks and mean-cost tradeoffs. The largest residual novelty risk is a result implicit in a general joint-transform or regular-variation treatment not located by the searches.

## Mathematical value

**PASS.** Cost and search duration are simultaneously random, and minimizing either mean alone does not quantify their dependence. The correlation limit distinguishes cost-growth universality classes, gives a sharp dimensionless maximum for the physically natural linear-return cost exponent, and identifies universal strict positive finite-rate association. The result is a structural, parameter-independent statement, rather than an arbitrary numeric specialization.

## Boundaries

Only instantaneous-reset search time is considered; the cost is recorded but not added to the clock. The gamma profile is asymptotic as the reset rate goes to zero, not a uniform finite-rate bound. Regular variation is essential for the stated universality. General unindexed equivalent work remains a publication-priority risk.

Self-review: passed. Independent audit: not yet performed.
