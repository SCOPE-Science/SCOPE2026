# Self-review

## Correctness — PASS

The theorem concerns one infinite binary right-infinite word with unbounded nondecreasing positive complete gaps. Its rotation-complete classes are classified exhaustively. In an arbitrary fully realized necklace with at least two ones, each consecutive pair of circular zero gaps satisfies an inequality imposed by monotonicity of source gaps; the cycle of inequalities forces one common gap size. A rotation beginning with a full preceding zero run then proves the plateau multiplicity lower bound, and consecutive equal gaps construct all required rotations. Unbounded gaps supply the two baseline classes. The resulting divisor sum is finite, and all class representatives are distinct.

The packaged checker enumerated 8,788 finite factor-language cases against the explicit formula, with 5,120 exhaustive small profiles and 3,668 pseudorandom/family comparisons. These are reproducibility checks, not substitutes for the quantified proof.

## Originality — PASS, with bibliographic qualification

Bell and Shallit (arXiv:2102.03821) define Lie complexity, prove general upper bounds, and already construct words with unbounded Lie complexity. De Luca and Fici (arXiv:2206.00995) classify the Sturmian case, while Li (arXiv:2207.05859) studies general divisor decompositions and extended variants. The older cyclic-complexity notion (arXiv:1402.5843) uses a weaker criterion. None of the inspected texts gives an equal-gap plateau criterion or an exact formula for **every** nondecreasing unbounded zero-gap sequence.

The closest previously available explicit special cases concern geometric marker positions and period-doubling words. The geometric case has fixed, usually distinct gaps and can have exceptional initial prefixes, so its assertion does not imply the new multiplicity-profile formula; the period-doubling sequence is structurally different. Actual searches for aliases and broader formulations returned no decisive covering result. Unindexed equivalent literature remains a residual risk.

## Mathematical value — PASS

The formula classifies every realized cyclic conjugacy class and determines the full Lie-complexity sequence from the plateau multiplicities without enumerating factor languages. It distinguishes constant and unbounded behaviors inside the same natural sparse monotone-gap family, and \(m_a=a\) yields the quantitative unbounded subsequence \(L(t!)\ge t+1\). The value lies in the all-parameter classification and sharp structural threshold; no claim of a new existence theorem for unbounded Lie complexity is made.

## Boundaries and verification status

The proof excludes zero or nonmonotone gaps, altered initial prefixes, and bounded gap sequences. It does not assert recurrence, automaticity or the value of ordinary cyclic complexity. The finite enumerations have stated bounds and no extrapolative role. Independent mathematical validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
