# Mathematical review: diagonal coincidence and Spearman rank envelopes

## Correctness (C): PASS

The exact domain is Lebesgue-measurable \(0\le f\le1\) with a nonnegative off-diagonal density \(h\); there is no hidden differentiability hypothesis on \(f\). The identity \(k'=h\) and the diagonal-line decomposition justify both necessity and sufficiency for the copula condition. Marginal integration yields one, and both quantities \(p=\int f\) and \(\rho_S=3\int t^2f\) follow directly from the same measure and from Tonelli's theorem.

The upper bound is the standard fixed-mass sign argument against the upper step function. The lower bound is an explicit identity with two nonnegative integrands: at \(a=\sqrt p\), their sum is \(\rho_S-p^2\). Equality analysis uses the strict positivity of both weights away from the breakpoint, the absolutely continuous equation \(k'=h\), and \(f=k-tk'\) to force the lower step generator. The upper step's uniqueness follows from strictness of the bathtub integrand off its breakpoint. Convex generator mixtures prove the full interval, with endpoints treated separately. The exact symbolic checker passed checks of the kernel decomposition, two extremizers, boundary integrals, and rational examples. Finite examples are not used as substitutes for analytic proof.

Remaining correctness risks: the result is restricted to this specified max-quotient family; no universal bound for arbitrary copulas or general quotient functions is asserted. The checker is a supporting algebra test, not a machine certificate of the quantifier-level proof.

## Originality (O): PASS, with explicit priority limitations

Cuadras (2024, DOI 10.3390/axioms13070433) defines the quotient construction and computes the decomposition into continuous and singular densities and \(p=\int f\). Durante (2007, DOI 10.1016/j.crma.2006.12.004) gives the related min-max generator criterion and the Spearman formula, as well as an ordinal-sum example which coincides with this theorem's **upper extremizer**. Those two articles were materially read, including proof statements and examples, and their contributions are acknowledged. No claim is made that the generator formula, separate rank formula, diagonal-mass identity, or upper-step copula itself is new.

The new claim is the exact *joint* feasible set for \((p,\rho_S)\), with two sharp bounds at each fixed \(p\), the lower extremizer's exact deficit certificate, equality rigidity, and all interior attainable pairs. Prior independent formulas and examples do not state these comparisons, and neither accessible primary text supplies the required fixed-mass optimization. Relevant published mathematical record summaries on other copula families, rank envelopes, and diagonal constraints were compared at the level of mathematical implication and do not cover this fixed diagonal-singularity problem.

Residual priority risk: Cuadras (2015, DOI 10.1016/j.jmva.2015.02.015) is a plausible broader antecedent on diagonal expansions; its abstract but not the full journal article was available, so coverage of the complete article could not be excluded absolutely. A failed literature or semantic search is not a proof of novelty. This qualification does not change the concrete claim-to-source distinction established by full-text comparison of the 2007 and 2024 articles.

## Value (V): PASS

In a natural statistical dependence model with a continuous component and exact ties, the point mass \(p=\Pr(U=V)\) quantifies a mechanism not captured by ordinary rank concordance. The full interval \([p^2,1-(1-p)^3]\) shows the sharp non-identifiability of \(\rho_S\) from \(p\), and identifies exactly which rank correlations are possible without leaving the family. For example, fixing \(p=1/4\) permits \(\rho_S\) between \(1/16\) and \(37/64\), with both extremes actually realized. The exact deficit decomposition and unique extremizers provide structural information for building extremal singular models, not an arbitrary discrete table or small numerical improvement.

## Compared primary sources and limitations

- C. M. Cuadras, *On Bivariate Distributions with Singular Part*, *Axioms* **13** (2024), article 433, https://www.mdpi.com/2075-1680/13/7/433 ; especially Definition 3, Theorem 1, Proposition 4, and discussion.
- F. Durante, *A new family of symmetric bivariate copulas*, *C. R. Math.* **344** (2007), 195–198, https://www.numdam.org/item/10.1016/j.crma.2006.12.004.pdf ; especially Theorem 2.1, Example 3, Proposition 3.4.
- C. M. Cuadras, *Contributions to the diagonal expansion of a bivariate copula with continuous extensions*, *J. Multivariate Anal.* **139** (2015), 28–44, https://doi.org/10.1016/j.jmva.2015.02.015 ; abstract inspected only; full text unavailable.

The finding has not undergone independent mathematical review.

Self-review: passed. Independent audit: not yet performed.
