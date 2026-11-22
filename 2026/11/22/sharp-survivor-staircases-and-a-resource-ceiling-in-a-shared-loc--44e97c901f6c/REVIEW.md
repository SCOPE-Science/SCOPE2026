# Scientific review: exact survivor staircases in a shared/local nutrient community

## Correctness — PASS

The theorem is reconstructed directly from the positive stationary equations of the one-nutrient model. A present consumer forces its niche concentration to \([q_i-(1-\theta)R]/\theta\), and its positive density then has a unique expression in \(R\). Mass conservation reduces all candidate attracting equilibria to a scalar equation \(R_0=H(R)\) with positive derivative on every support interval. The resource ceiling, exact entry supplies, and full support selection follow. The missing-species invasion eigenvalues are \(\alpha_i(R-q_i)\). The displayed quadratic form cancels active consumer/resource cross terms; all nutrient transfer blocks are positive semidefinite and active blocks have strictly positive determinant. The zero-dissipation invariant set is trivial, establishing a Hurwitz active subsystem and strict stability for omitted invaders with \(q_i>R\). Exact rational stationarity and transfer-matrix checks passed in `checker.py`, including 800 additional parameter samples. Those samples are not substituted for the analytic proof. The excluded threshold supplies are stated, with no nonlinear boundary claim.

## Originality — PASS, subject to historical-priority limits

ElGamel–Mugler, arXiv:2611.00222v1, main section III.1 and supplemental section VI, analyze the same model but derive two-species coexistence conditions only at \(\theta=0\) and \(\theta=1\). Supplemental section VII treats a *multi-resource* lower bound for complete separation, not the exact arbitrary-species, single-resource, intermediate-\(\theta\) support staircase or its local stability. Source S4–S24 and S35–S41 were inspected rather than inferred from title or abstract. Other chemostat work demonstrates coexistence through crowding, consumer dispersal, or resource patches, not the same global/local fixed-niche reaction equations. Semantic searches of published mathematical findings for local/global nutrient equilibria, resource-supply thresholds, chemostat coexistence and patch-allocation staircases did not return an equivalent or stronger statement. The nearest patch-allocation staircase concerned *optimal investment under a budget*, not endogenous equilibrium species survival. The inaccessible full text of one 2022 source-sink article is a residual comparison risk, not affirmative novelty evidence.

## Value — PASS

The originating paper explicitly leaves intermediate isolation and multiple-species analytical coexistence difficult, while using numerical diversity curves. This result gives exact finite supply levels at which each additional break-even class can be supported, proves that each selected equilibrium is locally exponentially stable, and establishes a supply-independent impossibility of recruiting sufficiently demanding species when isolation is incomplete. This distinguishes structural failure of coexistence from merely insufficient nutrient provisioning. The statement concerns the new model's natural parameters and arbitrary species counts rather than an arbitrary numerical slice. The local nature and biological-detection limitations are disclosed.

## Closest literature and limitations

- M. ElGamel and A. Mugler, *Spatial structure promotes coexistence, resilience, and synergy in microbial communities*, arXiv:2611.00222v1 (2026-10-30); full relevant mathematical sections examined, especially supplement VI–VII.
- P. De Leenheer, D. Angeli and E. D. Sontag, *Crowding effects promote coexistence in the chemostat*, JMAA 319 (2006); different density-dependent self-limitation, not species-specific local nutrient pools.
- F. Yu, W. Song and Y. Wang, *Effect of diffusion on a consumer-resource system with source-sink patches* (2022 early access); journal abstract and example/method available, full article access restricted. The paper concerns movement among source-sink patches, not the specified common-pool plus private-pool consumption mechanism in the new model.
- Published published-finding corpus record *Sharp resource-allocation staircases under uniform patch dispersal*, 2026-11-02; optimization of investment allocation, not ecological survivor support.

No global attractor theorem, finite-noise claim, adaptive-geometry extension, complete historical novelty guarantee, or independent validation is asserted.

Self-review: passed. Independent audit: not yet performed.
