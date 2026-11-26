# Independent mathematical audit

## correctness

PASS

The model uses n symbols, n-1 dependent windows, exact normalized Zipf with fixed s>1, and distinct nonloop transitions. For a fixed ordered nonloop pattern, adjacent occurrences are impossible; for its unordered version the adjacent joint probability is p_i p_j(p_i+p_j). The dependency neighborhood has size at most three and the conditional-dependence term is zero; applying the zero-event Poisson bound and splitting off finitely many heavy rows and columns makes the summed error o(n^gamma log n). The divisor count for ij indexed by (nc^2)^gamma gives the coefficient gamma c^(2gamma), and the integral of 1-exp(-a u^-s) is a^gamma Gamma(1-gamma). The factor 1/2 for unordered pairs then gives 2^(gamma-1). In the variance step a fixed disjoint pairing of positions loses at most three windows when t-1,t,t+1 are excluded, leaving at least n/3 independent windows for large n. A change in the count requires one of at most four old/new pairs to be absent in those windows. The resulting weighted divisor estimate yields Var=O(n^gamma log n). Summable Chebyshev bounds on geometric grids and monotone interpolation prove the strong laws; the variance also gives L2. The linear identities transfer both limit modes and the positive denominator limits justify the two different reciprocity fractions. RESULT.md lines 26–99 suffice; the recorded 7,030 tests in VERIFICATION.md are finite checks, not a reproduction of any limit, and the attached script was inspected, not run.

## originality

FAIL

A distinct indexed finding gives both leading Zipf adjacent-edge laws with the same constants, model, and convergence modes, and a sharper directed expectation. Its loops are negligible in both modes; the orientation conclusions then follow algebraically. This is demonstrable coverage of the complete frozen claim, not a finding that the later-dated catalogue entry had historical priority. The result is not shown false; no unavailable search is the basis for the decision.

## value

PASS

As a scientific statement, a sharp joint edge-growth law in the actual overlapping-transition model fills a natural gap left by fixed-degree limits, and the limiting fractions distinguish two genuine graph observables. This assessment credits the substantive aggregate laws, not a separate advance from the algebraic reciprocity conversion; the latter is not a surviving originality repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
