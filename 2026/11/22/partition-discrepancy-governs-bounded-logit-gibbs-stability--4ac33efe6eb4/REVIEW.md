# Review of the bounded-logit Gibbs stability theorem

## Correctness

**PASS.** The norm identity in (5) uses all cube vertices, not a guessed perturbation. Each proper subset has exactly the odds interval (6), reached by two-level scores; the balanced-subset discrepancy therefore gives the exact maximum derivative norm. Convex integration gives the upper bound, interior approximations give matching two-input lower bounds even when a maximizer is on the score-diameter boundary, and the degenerate zero-budget case is separated. The integer-partition reduction uses the strict logarithmic gap in (10). The included checker passes 10,099 supplementary finite tests, which are not substituted for proof.

## Originality

**PASS with residual historical-priority risk.** Gao–Pavel's 2017 softmax Lipschitz theorem is Euclidean; Kanai et al. 2020 analyze the role of bounded logits; Nair 2025 establishes sharp matched-\(\ell^p\) bounds. Most relevant is Cohen–Fausti 2023: its finite Hilbert-to-variation comparison, especially Lemma 5.2, yields a related fixed-base local derivative bound. That prior component is acknowledged, not claimed new. In contrast, the present statement optimizes the mixed-norm coefficient over *all* positive-weight score vectors subject to a fixed diameter, identifies a weighted-partition phase boundary, and proves exact saturation NP-hard for rational instances. No inspected theorem provides that combined sharp statement or a dominating parameterization. Hidden or implicitly equivalent results cannot be ruled out.

## Mathematical value

**PASS.** The saturated coefficient exactly determines when limiting the score spread cannot improve worst-case local probability robustness; the odd-versus-even class threshold is a natural consequence for balanced priors. For heterogeneous priors, the governing invariant is an exact subset-balance discrepancy, and the equality decision contains PARTITION, explaining an intrinsic combinatorial obstruction to exact certification. This is a meaningful finite-dimensional sharp stability law, independent of any proposed neural-network performance claim.

## Sources and limitations

Relevant primary full-text materials: Gao–Pavel, arXiv:1704.00805 (Proposition 4); Kanai et al., arXiv:2010.02558 (Sections 1 and 3); Cohen–Fausti, arXiv:2309.02413 (Theorem 5.1 and Lemma 5.2); Nair, arXiv:2510.23012 (Theorem 1, Proposition 2 and Appendix A.2). The proof concerns strictly positive weights, finite dimension and a positive score-diameter budget; zero diameter is an exceptional constant-map domain. It does not assert approximation hardness or certify any preceding network. Earlier equivalent treatments of local probability sensitivity remain a possible priority risk.

Self-review: passed. Independent audit: not yet performed.
