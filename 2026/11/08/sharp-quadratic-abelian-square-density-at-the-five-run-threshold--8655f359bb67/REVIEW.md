# Self-review

## Correctness — PASS

The exact five-run count follows by balancing the ones across the midpoint, then balancing zeros. Equal interior one-run lengths yield the parity-restricted diagonal band; unequal lengths yield at most a one-dimensional endpoint family. Lower-run factors are bounded directly by their possible middle complete runs, and the area lemma is proved by elementary geometric integration for both possible size regimes. The universal upper bound and explicit lower witness give exactly the coefficient \(1/16\) at all large lengths. A standalone factor enumerator passed 11,628 complete five-run words through length 19, 16,807 additional run tuples, and 50 witness cases. This does not extend a finite computation to infinite lengths: the proof is analytic.

## Originality — PASS (qualified)

Closest source: Kociumaka, Radoszewski, Rytter and Waleń, arXiv:1604.02238, §2 Fact 2.1, show \(\Theta(n^2)\) distinct Abelian squares using an explicit five-run word. Their §3 Theorem 3.6 bounds *inequivalent* Abelian squares, not the literal distinct-factor count. Fici and Mignosi, arXiv:1506.03562, §3 Proposition 1, and Fici, Mignosi and Shallit, arXiv:1701.00948, §3 Proposition 1, use another five-run witness to prove quadratic growth. Neither inspected full-text result states the five-run sharp coefficient, its upper bound, or the exact parameter classification. OEIS A262249 is an unrestricted finite table and A262265 counts inequivalent factors. Targeted scientific-record searches and comparisons against accessible published statements found no dominating exact theorem. Equivalence or priority in inaccessible and unindexed literature remains a risk.

## Value — PASS

Exactly five runs is the smallest run complexity at which the distinct Abelian-square count becomes quadratic, and its optimum rate is the nontrivial value \(1/16\). This resolves the sharpness of the basic finite-run witnesses used to establish quadratic growth. The all-parameter five-run classification is the structural content supporting the density bound, not a routine substitution into a general theorem.

## Boundaries

The paper does not establish an exact finite-length optimum or characterize every finite-length five-run maximizing word. It does not assert a sharp upper constant for arbitrary binary words, or independent historical priority. Source comparison is best-knowledge and the external literature is not exhaustively indexed.

Self-review: passed. Independent audit: not yet performed.
