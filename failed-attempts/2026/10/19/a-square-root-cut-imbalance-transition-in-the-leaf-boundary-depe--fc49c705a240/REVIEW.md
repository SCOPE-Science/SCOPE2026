# Independent mathematical audit

## correctness

PASS

The claimed covariances are correct. One independent check averages the fixed cut over all a-subsets by label symmetry. Given the tree, E[C] under this averaging is constant, proving Cov(L,C)=0. For C² the only shape-dependent term is 2W(P_adj−P_dis), where W=∑ᵥ binom(deg v,2), P_adj=ab/[n(n−1)] for two adjacent edges both crossing, and P_dis=4a(a−1)b(b−1)/[n(n−1)(n−2)(n−3)] for two disjoint edges both crossing (n≥4). Writing m=n−2 for the Prüfer word length gives E[W]=m+m(m−1)/(2n). Conditional on any specified vertex being a leaf, the word avoids that label and n in the denominator changes to n−1. Summing over labels yields Cov(L,W)=p_n m(m−1)/[2(n−1)], where p_n=((n−1)/n)^(n−2). Multiplying gives exactly the frozen formula; its prefactor is positive, giving the stated signs. For n=3, L is constant and the claimed factor is zero for both possible cut sizes. Singleton and balanced cuts need no extra hypotheses. The inspected frozen Prüfer script checks only n=3 through 8 and was not executed.

## originality

FAIL

The exact cut covariances and transition are a direct corollary of earlier Resultary leaf–degree identities, by exchangeability and the deterministic totals of one- and two-edge subsets of a tree. This is demonstrated coverage, not a conjectured overlap or a claim that the earlier source printed the cut formula.

## value

FAIL

The sign boundary is a useful interpretation, but the claimed contribution consists entirely of orbit-counting and sign simplification applied to a known exact invariant. No independently useful unknown moment or nontrivial new mechanism survives the reduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
