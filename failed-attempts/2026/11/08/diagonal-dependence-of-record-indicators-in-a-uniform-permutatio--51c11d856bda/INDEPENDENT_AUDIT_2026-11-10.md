# Independent mathematical audit

## correctness

PASS

Condition on the unordered first-i value set S_i. The original prefix record R_i has conditional probability 1/i independent of S_i. For i<j, either j is in the prefix and Q_j is impossible, or Q_j depends on the suffix ordering only; inversion symmetry handles i>j. For i=j the only conditional covariance occurs when S_i={1,...,i}, of probability 1/binom(n,i), on which both indicators equal 1 exactly when pi(i)=i; the conditional variance is (i-1)/i². This proves diagonal entry (i-1)/(i² binom(n,i)), zero off-diagonal, aggregate covariance and correlation. Independently exhaustively checked all n² joint equations over every permutation for n=2 through 7; these finite tests corroborate, not replace, the all-n conditional proof.

## originality

FAIL

EXACT PRIOR COVERAGE: earlier 2026-10-26 published record Diagonal forward–inverse record covariance for uniform permutations states the SAME covariance matrix and off-diagonal independence with identical indicator definitions and combinatorial proof. It also states the full weighted covariance identity and sharper total-covariance expansion 1/n+1/(2n²)+O(n^-3), strictly dominating the later 1/n+O(n^-2). The current submission does not contain an independent result beyond this antecedent.

## value

FAIL

The diagonal dependence law is an interesting exact refinement beyond aggregate Euler–Stirling statistics, but the precise refined fact and stronger asymptotic are already published; repeating the known theorem with equivalent conditioning is not a new valuable contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
