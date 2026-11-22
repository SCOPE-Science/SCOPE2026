# Review: A zeta-moment limit law for Wilf surplus in reflective numerical semigroups

## Correctness — PASS
Shor's full-text Proposition 3.4 and Corollaries 3.6 and 3.8 fix the exact admissible multiplicities, Frobenius numbers and embedding dimensions. The displayed two-branch Wilf-surplus identity follows by algebra from those results. The error from the explicit model \(f(a/g)\) is at most \(4/g\), apart from one ordinary semigroup, and the model has summable derivative variation and jumps. Hence Lipschitz-observable means converge at the claimed \(O((1+\tau(g))/g)\) rate. Splitting \([0,1]\) into reciprocal intervals gives the CDF and each zeta moment by an absolutely convergent expansion. The delivered `verify.py` passed 4,116 independent finite semigroup enumerations and three truncated moment comparisons. Finite checks cannot establish the limit and are not presented as doing so.

## Originality — PASS within inspected evidence
The closest and strongest source is Shor, *Reflective numerical semigroups* (arXiv:2207.00051v1): its results directly imply the one-semigroup Wilf formula, and this formula is **not** claimed new. Shor proves Wilf's inequality (Corollary 4.20), gives the count of genus-fixed semigroups, and computes several asymptotics for fixed-Frobenius counts. The inspected full text does not identify a normalized Wilf-surplus limit distribution, a full CDF, zeta moments, or a quantitative fixed-genus Lipschitz-discrepancy statement. A published isolated-gap distribution for reflective semigroups addresses a different invariant and gives no implication to the Wilf-surplus law; its available research summary was checked but not treated as whole-paper inspection. Search of research records and primary literature did not locate an equivalent theorem. Earlier implicit or unindexed equivalent calculations remain a genuine residual risk. A failed search is not proof of novelty.

## Mathematical value — PASS
Wilf surplus is a canonical numerical-semigroup invariant central to the Wilf conjecture. This theorem gives the complete nondegenerate limiting *distribution*, full support, exact CDF, every positive integer moment in zeta values, and a quantitative rate for the entire classified fixed-genus family. It goes beyond verifying the known nonnegative bound or simply tabulating small genera. The new arithmetic-statistical law may serve as a benchmark for comparing restricted families to the general semigroup population; no extension to all semigroups is asserted.

## Scope and residual risk
The source's structural formulas are assumed and accurately attributed; all novel conclusions are asymptotic deductions. Mathematical correctness has no independent external certification. Possible unindexed equivalent results are not ruled out by database searching.

Self-review: passed. Independent audit: not yet performed.
