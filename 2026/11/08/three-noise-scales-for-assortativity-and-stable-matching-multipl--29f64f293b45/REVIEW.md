# Review of finite Mallows stable-matching law

## Correctness — PASS

The proof fixes all quantifiers to a complete strict \(3\times3\) market with six independent, identically distributed Mallows preference rankings. It checks the exact blocking condition against all six possible matchings for each of the \(46{,}656\) labeled profiles. The Python and C++ standalone implementations independently recover the same coefficient vectors for one, two, and three stable matchings and for stability of the identity matching. Exact polynomial algebra verifies the three rational probability laws, derivative factorizations, their signs on \(0<\phi<1\), and the first-nonzero-degree counts \(4,4,6\). The finite exhaustive check is a proof for this finite domain only.

## Originality — PASS (with residual risk)

Wang (2026, arXiv:2603.24526) gives large-market rank-quantile assortativity for fixed dispersion, not finite exact probabilities. Hoffman, Levy and Mossel (2023, arXiv:2312.14813) give asymptotic exponential stable-matching growth, not the three-event \(3\times3\) laws or their sharp small-noise exponents. The graph-percolation model of Angel and colleagues (2018, arXiv:1802.07142) produces a Mallows-distributed *outcome* under deterministic rankings, unlike these random preference lists. The exhaustive counts of Borodin et al. (2021), and the later full-symmetry orbit census, agree with the \(\phi=1\) endpoint; their uniform counts and relabeling classes do not supply inversion-weighted exact parameter laws. The full web-accessible primary articles were inspected, but unindexed equivalent parameterized calculations remain possible.

## Mathematical value — PASS

The theorem quantifies an analytically meaningful gap between loss of perfect assortativity, the onset of multiple stable matchings, and three-way multiplicity. The three sharp inversion costs \(1,2,5\), accompanying leading coefficients, and strict monotonicity across the entire dispersion interval make the finite market a nontrivial benchmark for correlated-preference matching. No claim of polynomial-time algorithms for larger markets, market-size asymptotics, or heterogeneous-dispersion results is made.

Self-review: passed. Independent audit: not yet performed.
