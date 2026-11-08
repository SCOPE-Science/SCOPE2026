# Scientific review: random idempotents of weighted-permutation evolution algebras

## Correctness — PASS

The claim is stated over every finite field and dimension with a precise uniform labeled monomial-matrix probability model. Multiplication makes the idempotent equation one quadratic recurrence per permutation cycle. Because the last edge weight enters the cycle product to the first power, its obstruction is uniform in the multiplicative group of the field. The number of solutions on one cycle is exactly one or one plus a cyclic-group kernel size. The total idempotent count is a **product**, not a sum; taking its complex powers makes a valid product of independent cycle moments. The permutation cycle index then gives the exact moment transform. An explicit finite cycle-type/binomial sum independently specifies each probability, without relying on moment determinacy alone.

Over the quaternary field, the binary logarithm of the count is a sum of cycle contributions; its polynomial generating function, probability of no nonzero idempotent, gamma-ratio asymptotic, and variance formula follow directly. The standalone checker exhaustively enumerates 6,559 labeled matrices over six small finite fields, including two nonprime fields, and independently checks every rational idempotent vector and the predicted probability histogram. The arbitrary-dimensional result comes from the symbolic proof, not extrapolation from the finite tests.

## Originality — PASS, qualified

Narkuziyev's permutation-evolution-algebra paper (arXiv:1803.11415, accessible author-uploaded full text) already derives the individual-cycle idempotent equation and cycle decomposition. Those facts are prior work, not the contribution. The 2026 evolution-algebra survey (arXiv:2610.22248, first submitted October 15, 2026) motivates random idempotent statistics, but concerns a distinct full-matrix model in the accessible material. The open-access full article on permutation representations and automorphisms by Costoya, Mayorga and Viruel (2025) concerns symmetry representations, not probabilistic rational-idempotent enumeration. The submitted claim instead gives the full weighted-cycle probability distribution in every finite field, an exact complex moment transform and the quaternary zero-idempotent and fluctuation laws.

Semantic mathematical-record searches for the distribution, equivalent cycle-index/moment statements, finite-field obstruction probabilities, and the quaternary asymptotic returned no directly covering result. Comparison is by statement and implication, not matching terminology alone. Historical priority remains qualified: the probability formulas may be obtainable by combining the old per-cycle theorem with standard permutation cycle indexing, and the complete text of the 2026 survey and the expanded 2020 permutation-algebra paper was not inspected. An undiscovered direct formulation would alter the originality assessment.

## Mathematical value — PASS

The exact idempotent-count distribution is a natural finite-field invariant of a graph-restricted ensemble of perfect evolution algebras and addresses a recent program of studying idempotent statistics. The result is not just a low-dimensional count: it handles every field size and dimension, sharply separates field arithmetic through the multiplicative cyclic obstruction, and gives a closed quaternary law with a power-law probability of having no nonzero idempotents in even dimensions. Its quartic variance growth is a substantive qualitative feature, not merely a minor numerical improvement. It provides a fully reproducible benchmark for broader sparse or random algebra models.

## Closest literature and limits

The individual-cycle root equation is covered by Narkuziyev (2018), and the symmetric-group cycle-index theorem is classical. Neither alone is represented as new. General full-matrix and triangular-matrix random ensembles are not interchangeable with the uniformly monomial ensemble. The result is for labeled matrices, not uniform isomorphism classes, and counts field-rational rather than geometric idempotents. Independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
