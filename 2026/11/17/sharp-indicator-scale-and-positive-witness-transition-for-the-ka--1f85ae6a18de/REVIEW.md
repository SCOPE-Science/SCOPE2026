# Review of the indicator-gauge theorem

## Correctness — PASS

The unrestricted theorem follows from a pointwise Lambert-envelope inequality for nonnegative magnitudes and a separate bounded negative-logarithmic branch. It correctly retains arbitrary signs and complex phases through the inequality \(|1-z|\ge1-\min(1,|z|)\). The critical derivative is \(1-W^2/(1+W)-t/e\), nonpositive when \(W\ge\varphi\), establishing the two-sided estimate at masses \(0<t\le e^{-\varphi}\). The explicit full-support witness attains the upper bound. The positive restriction is a separate optimization: the support-mass reduction provides matching analytic lower bounds and actual measurable minimizers. All endpoint assumptions and the normalized centralizer have been checked. The supplementary finite-cell checker runs without external packages; finite tests are not used as an infinite proof.

## Originality — PASS (with residual bibliographic risk)

Example 6.1 of Cabello Sánchez, Castillo, Martínez-Bohórquez and Navarro Garmendia, *The Serre closure of Banach spaces* (2026), defines the same quotient gauge and establishes only \(\rho(\mathbf1_A)\le t/\log(1/t)\). The present bound goes in the missing lower direction for arbitrary witnesses, and establishes a quantitative sharp coefficient. The source's space-level equivalence with \(L\log^{-1}L\) does not force a coefficient for the fixed quotient gauge. The positive-support phase transition is another new precise claim, not a restatement of the source's upper witness. The 2023 accessible study *Group Actions on Twisted Sums of Banach Spaces* concerns group-compatible centralizers. The 2016 Lorentz-factorization paper and 2013 nonlinear-centralizer paper are relevant but could only be inspected in part, and an equivalent earlier gauge calculation cannot be completely ruled out. Indexed related work on concave Orlicz *sequence* gauges uses a different object. Scientific implication comparisons and exact searches are recorded in `AUDIT.json`.

## Mathematical value — PASS

The indicator quasi-norm is the natural fundamental gauge of a canonical quotient in a nonlocally convex construction. A sharp coefficient with quantified relative error is stronger than identifying the associated function space only up to quasi-norm equivalence. The auxiliary exact optimization describes the mechanism of support concentration and the precise point where optimal positive witnesses cease covering the entire target. This is a motivated structural computation, not an arbitrary parameter slice; the restricted formula is explicitly distinguished from the unrestricted gauge.

## Scope, evidence and limitations

The unrestricted estimate is a small-mass theorem, not an exact all-mass classification. Exact all-mass values concern only nonnegative real witnesses. The full minimizer or its uniqueness is not characterized, and uninspected older full texts create a limited bibliographic uncertainty. Scientific proof steps and reproducibility instructions appear in `RESULT.md` and `CHECK.py`. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
