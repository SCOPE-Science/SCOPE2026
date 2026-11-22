# Scientific review: genealogical decay alias and sampling repair

## Correctness — PASS

For depth-three binary genealogical reinforcement with conditional independent Binomial offspring, the explicit depth-five rooted binary tree has three sample kinship-count vectors whose determinant is one. The first three logit predictors reduce to a rational shape ratio \(R(t)=(1+t)/(1+2t^2)\), whose complete two-root factorization yields the necessary and sufficient alias map \(F(t)=(1-2t)/(2(1+t))\). The positive reconstruction of reinforcement strength and baseline gives equality of the entire conditional offspring distribution, not merely an approximation. The Jacobian determinant vanishes at the unique fold, and the strictly decreasing fourth-observation ratio establishes identification globally. Symbolic calculations and the standalone exact-arithmetic checker support the critical identities.

## Originality — PASS, bounded by identified literature

The closest primary source is Kochocki (2026), arXiv:2611.08548v1, Section 4, Theorem 1(b) and Appendix A. That text asserts, rather than establishes or supplies, the proposed two-fold alias under a full-rank three-distance count design. It states sufficient conditions that the explicitly realized design meets, while the present proof exhibits equal conditional distributions at distinct admissible decay rates. Alsammani (2026) discusses generic local/global aliases and observation design in other mathematical biology systems but not this finite-depth genealogy. Targeted searches of mathematical records and literature did not reveal the same count design or alias; an unindexed equivalent nonlinear-regression example remains possible. No claim is made to discovering general identifiability or symmetry arguments.

## Value — PASS

Three selected events are the proposed minimal data budget for estimating three reinforcement parameters. A biologically realizable open-set alias is a consequential obstruction to interpreting those estimates, not an arbitrary numerical exception. The sharp two-branch description identifies exactly which rates are ambiguous; the singular Fisher-information fold explains local instability; and the fourth sibling-only sample gives an actionable and mathematically sufficient observational repair. No conclusion about full population-history identification or finite-sample statistical accuracy follows.

## Scientific limits

All statements are conditional on the known pre-branching genealogy and the selected three- or four-event likelihood, with positive reinforcement and decay. The full unobserved genealogical process, incomplete genealogy measurement, and estimator variance have not been analyzed. Historical equivalence beyond inspected primary sources cannot be ruled out.

Self-review: passed. Independent audit: not yet performed.
