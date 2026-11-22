# Self-review

## Correctness — PASS

The claim is for the zero-target spectral Kemeny objective with a *uniform stationary law*. On a tree, every edge is compulsory for irreducibility and the Kirchhoff-index decomposition is a strictly convex sum of cut-pair counts divided by independent edge transition probabilities. This proves the uniqueness and orbit invariance of the **unrestricted** optimum, not just a symmetric ansatz. Row constraints reduce to the root cap and one saturated child constraint. The resulting scalar objective has a strictly positive second derivative, an exact radical minimizer, and a completely evaluated boundary branch. For the proposed integer threshold \(t=k^2-3k+4\), polynomial substitution gives \(F_k(t)=4\) and \(F_k(t-1)=3-kt<0\); an upward quadratic with a unique positive zero therefore yields exactly the claimed integer activation set. The scaling and equal-edge comparison follow by direct asymptotics. The bundled Python verifier runs 1,484 finite checks, including independent Laplacian inversion, but the all-size proof is analytical.

## Originality — PASS on available inspected evidence

Hunter (2012) provides the Kemeny framework. Patel, Agharkar and Bullo (2015) treat general convex optimization over reversible transition matrices with prescribed stationary measure; their equations and examples do not state the exact two-level-tree allocation or the strict integer threshold. Zeng (2021) treats natural weighted random walks and fixed-multiset tree-shape extremization, which does not maintain uniform stationary measure when free weights vary. Durastante, Gnazzo and Meini (2026) develop reversible fixed-pattern optimization and general algorithms but do not classify this particular family in the inspected text. Searches of published mathematical records, aliases of this two-level tree, and closely related previous exact tree-walk claims did not reveal an implication establishing the quadratic threshold. Residual priority risks include unindexed papers, alternate names for two-level trees, and formulations not captured by the search terms.

## Value — PASS

The threshold answers a structural question about **where an optimal uniformly stationary walk should wait**, not merely about objective evaluation: although children never hold, the root changes from zero holding to strictly positive holding at the exact integer boundary \(m=k^2-3k+4\). Its joint scaling limit gives a nondegenerate profile \((1-\rho^{-1/2})_+\) across leaf densities of order \(k^2\). In addition, the asymptotic penalty \(2-1/k\) quantifies the cost of a standard feasible equal-edge alternative. These properties are natural family-design facts rather than arbitrary finite parameter samples. The result does not claim a theorem for arbitrary trees or policies.

## Closest literature and limitations

Relevant antecedents: J. J. Hunter, arXiv:1208.4716; R. Patel, P. Agharkar and F. Bullo, *IEEE Transactions on Automatic Control* 60 (2015); J. Zeng, arXiv:2109.09249; F. Durastante, M. Gnazzo and B. Meini, *BIT Numerical Mathematics* 66 (2026). The verified archival focal date is 2012-08-23, the arXiv posting of Hunter's Kemeny study. A specialist literature audit might find an equivalent theorem not captured by the inspected sources. No independent validation has been conducted.

Self-review: passed. Independent audit: not yet performed.
