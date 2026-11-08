# Scientific review

## Correctness — PASS

The analytic proof derives the cross-moment from differentiated Dirichlet gamma moments, explicitly states the mixed moment for each coordinate, and reduces the sign to a sum of positive weighted pair contributions. The digamma derivative is strictly positive for each positive argument, and there is at least one pair since \(m\ge2\). Equality characterization is exact. Raw-moment and pairwise formulas agree on all 1,360 integer vectors in the verifier; four independent high-precision beta integrals include noninteger asymmetric concentrations. Finite checks are corroboration and are not used to infer the universal assertion.

## Originality — PASS, with residual historical risk

Cerquetti's 2014 arXiv:1404.3441, Theorem 1 on Tsallis indices and Theorem 2 on Shannon, computes marginal moments, not the mixed Shannon–Simpson index covariance or its universal sign for arbitrary heterogeneous finite Dirichlet parameters. Wolpert and Wolf's 1994 arXiv:comp-gas/9403001 develops Bayesian beta-integral methods and entropy moments; it does not display the stated pairwise sign decomposition. Cerquetti's 2012 arXiv:1203.1666 treats Simpson evenness separately. A published result about empirical sample richness and unbiased Gini–Simpson diversity concerns distinct observables and a distinct probability space, so it does not imply this statement. Generic differentiated moment identities do provide a route to the formula and are explicitly acknowledged. A hidden specialization or earlier inequality remains possible; finite searches do not certify global uniqueness.

## Value — PASS

Shannon and Gini–Simpson diversity are standard complementary measures of ecosystem evenness and Bayesian predictive uncertainty. Their joint uncertainty under an arbitrary nonsymmetric Dirichlet posterior is not determined by separate marginal moments. The exact sign theorem, a sharp explicit concentration-parameter baseline, and the equality characterization give usable structural information for every posterior pseudo-count vector, not just symmetric examples. Heterogeneity contributes an interpretable nonnegative term rather than an uncontrolled correction.

## Scope and verification limits

The claim is solely the displayed exact cross-covariance/sign theorem for finite Dirichlet laws. It makes no stochastic association claim, no result for non-Dirichlet laws, and no independent validation claim. Arithmetic experiments are finite, with analytic proof establishing all real positive parameters. Historical implicit coverage is the principal remaining originality risk.

Self-review: passed. Independent audit: not yet performed.
