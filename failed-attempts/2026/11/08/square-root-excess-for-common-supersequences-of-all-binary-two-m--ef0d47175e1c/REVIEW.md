# Independent mathematical audit

## correctness

PASS

For every binary host with r ones and Z=k-2+q zeros, each chosen pair of ones covers at most binom(q+2,2) two-marker targets; union over binom(r,2) pairs gives the triangular lower bound. The spaced-marker host W=(0^h1)^{ceil((k-2)/h)+1}0^e, e=k-2-(ceil((k-2)/h)-1)h, covers all targets by choosing marker indices to cover prefix/middle and leaving >=c zeros after; count its length. Direct independent subsequence checks for all k=3..19 and h=1..5 and exact comparison of old/new lower bounds confirm finite instances. This proves only Θ(sqrt k) with lower constant 2*2^{1/4}, upper 2sqrt2, not a sharp limit.

## originality

FAIL

The 2026-11-02 prior theorem studies literally the same full binary weight-two target language under scattered subsequence containment. It proves k-3+ceil(2sqrt(2(k-1)))<=L_k<=k-1+ceil(2sqrt(2(k-1))) for ALL k>=2, implying the sharp limit 2sqrt2. Both submitted weaker asymptotic constants and the Θ(sqrt k) claim are already dominated; its assertion that the leading constant remains open is incorrect as a literature-position statement.

## value

FAIL

A complete two-marker subsequence universality bound is a motivated combinatorial problem, but the submitted weaker square-root bracket provides no surviving unknown sharp fact: the earlier two-unit envelope fixes the leading constant exactly and dominates the new pair-counting inequality. The new spaced-marker construction is a less efficient re-solution of the same known optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
