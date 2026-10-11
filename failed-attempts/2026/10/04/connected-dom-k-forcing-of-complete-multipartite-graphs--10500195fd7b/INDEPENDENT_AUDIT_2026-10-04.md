# Independent mathematical audit

## correctness

PASS

For a connected dominating initial set of size at least two, at least one initially black vertex lies both in and outside any witnessing part. At the first force from part \(i\), the outside white count is at most \(k\); after that force, the remaining inside white count must also be at most \(k\). Initial black vertices on both sides sharpen the capacities to \(n_i-1\) and \(N-n_i-1\), yielding the lower bound, and choosing whites attaining both capacities gives the two-step construction. The singleton universal-vertex exception is exact. The inspected verifier brute-forces every multipartite type through order nine and every admissible \(k\), matching the formula.

## originality

FAIL

A previously published SCOPE record already classifies every standard \(k\)-forcing set of a complete multipartite graph by the identical first-force argument. Imposing connected domination on that all-set classification is elementary: size at least two means the black set meets at least two parts, which changes only the outside capacity from \(N-n_i\) to \(N-n_i-1\), plus the obvious universal-singleton exception. Thus the assigned minimum formula is implication-level covered by the prior all-k-forcing theorem and basic complete-multipartite connectivity/domination.

## value

FAIL

Once the broader all-k-forcing classification is available, the connected-dom restriction is a routine support constraint and one-unit capacity adjustment. The formula is useful as a corollary but does not constitute a separate mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
