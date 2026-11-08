# Scientific review

## Correctness — PASS

The theorem is restricted to the three-class game explicitly defined in the result and integers \(m\geq9\). The upper classifier \((22,15,12)\) at quota \(60.5\) makes errors precisely on profile \((3,0,0)\); the source of every other profile is checked by the inequalities in the proof. Class-uniform optimum follows from the four critical profiles and their orbit sizes. For arbitrary weights, the 60-winning/59-losing balanced incidence certificate gives a wrong classification under every relabeling, and averaging yields an error count at least \(\binom m3/20\). The comparisons of coefficients hold for \(m\geq9\), and rules with nonpositive quotas are treated separately. Standalone code checks 56 small profiles, 3,575,656 weighted class-profile cases, 294,912 individual coalitions, and 300 relabeling certificates. Finite checks are corroboration, not an infinite proof.

## Originality — PASS, with residual risks

Einy and Haimanko, arXiv:2610.08968v1, introduced this exact game and proved its distinct \(\varepsilon^*\) threshold; Sections 4, 6, 7 and Appendix 8.6–8.7 have been examined. Their Section 6 states a universal \(O(m^{-1/2})\) misclassification bound rather than this specific exponential-polynomial order. The four profile types are already in their proof of the weight-excess result and are credited. The new comparison is of *minimum misclassified coalition count*, not of the already published weight gap. Targeted indexed searches for the game, flipped quotas, outlier counts and the derived exponential order found no stronger directly covering statement. This is not a proof against unindexed or otherwise unavailable work. Albareda-Sambola et al. (2025) establish a related outlier framework, but only bibliographic/abstract material was accessible for that paper; the exact family originated later in 2026.

## Value — PASS

The two distance-from-weightedness measures are central objects in the motivating paper, which gives a polynomial upper bound on this misclassification probability but no family-level sharp rate. For the paper's canonical example witnessing tightness of the other measure, the result proves an exponential rather than polynomial misclassification probability, including the exact optimum under symmetry and a robust unrestricted-order lower bound. It clarifies how a game may be unrepresentable by any weighted rule yet almost perfectly representable on uniformly random coalitions. The precise unrestricted leading constant is not established.

Self-review: passed. Independent audit: not yet performed.
