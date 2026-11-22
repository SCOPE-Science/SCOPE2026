# Review of exact inverse-square adaptive-reset clock moments

## Correctness — PASS

The model is precisely specified by a Brownian diffusivity \(D\), regularized inverse-square hazard and an independent exponential threshold. Reflection at \(b\) gives the killed Green kernel \(G(b,y)=b^{\eta+1}y^{-\eta}/(D\eta)\). A Brownian-scale lower survival bound proves moment divergence at and below \(\eta=2m-1\); a Neumann supersolution and comparison establish finiteness above it for every integer \(m\ge1\). The exact mean, second moment and excess dispersion follow from the same Green recursion, independently checked by symbolic and truncated-domain computations. The renewal-count Fano limit uses the standard renewal variance theorem, only in the finite-second-moment regime. No finite simulation is presented as an infinite proof.

## Originality — PASS, with residual risk

Keidar–Reuveni (2026) already derive the inverse-square stationary spatial-tail exponent and the mean-reset-time localization boundary; their spatial moment hierarchy is explicitly prior work. The final claim instead gives the exact **reset-interval temporal** moment hierarchy and an exact finite-noise expression with strictly positive excess dispersion. Full text of Keidar–Reuveni (including end matter), Roldán–Gupta, and Pinsky was materially checked; the closest target first-passage literature has a different stopping event. Semantic published-finding corpus searches found no equivalently implied temporal result. Generic Feynman–Kac and Kac recursions are covered classical techniques; an unindexed specialized calculation could still exist.

## Value — PASS

The strength at which a normalizable stationary state first appears differs sharply from the strength at which its renewal clock has finite variance. For \(2<a/D\le12\), average resetting is finite while reset-time variance is infinite; when \(a/D>12\), a closed, strictly super-Poissonian count-noise law quantifies irregularity and strictly decreases with hazard strength. This gives an exact reliability benchmark for a physically motivated marginal localization protocol, rather than simply reproducing its known spatial tails.

## Closest literature and scope

Keidar and Reuveni, arXiv:2608.27090; Roldán and Gupta, arXiv:1703.10615; Pinsky, arXiv:1805.00320; Aspman et al., DOI 10.1103/w2yj-91m8. The exact formulas are for the specific nonsingular rate; no universal finite-moment constants, finite-sample inference, or independent audit is asserted.

Self-review: passed. Independent audit: not yet performed.
