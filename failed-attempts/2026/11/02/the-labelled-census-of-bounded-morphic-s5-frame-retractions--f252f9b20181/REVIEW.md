# Independent mathematical audit

## correctness

PASS

For an equivalence relation, forth confines each source class to a target class and back makes it onto that entire class. Idempotence fixes every point of each image class; conversely, any such classwise-onto assignment with target classes fixed is idempotent. Thus each omitted class independently selects a target and a labelled surjection. A minimum-size class must be retained, and retaining any minimum makes every omitted class feasible. This proves the fixed-partition sum, minimum-class count, and equal-size specialization. For the all-partition count, a root block of size t is a labelled t-set and each satellite is a t-tuple of nonempty labelled fibers indexed by its root points. Taking a set of satellites and then a set of root components gives the displayed formal EGF, with empty frame counted once. An independent integer recurrence checks the coefficients: on m labels, for each t choose the root block and sum onto(m−t,tj)/j! over satellite multiplicities j, since the j freely permutable satellite indices partition the onto targets into t-tuples. Assemble by the component of a distinguished label. This reproduces 1,1,4,17,107,747,6365,61196 from n=0 through 7.

## originality

FAIL

The frozen relation to prior work omits the exact block-surjective monoid Γ(X,P), as distinct from the larger partition-preserving T(X,P). Sarkar–Singh Theorems 5.9 and 6.6 and Proposition 6.7 give the same fixed-partition classification and counts, including the equal-block case; Resultary 5ce12a321daf gives the finer actual image polynomial. No claim that the all-partition EGF is printed by those sources is made. It follows by a direct labelled exponential-formula resummation of the stronger image-refined product: distribute its sums to assign each nonimage block to one image block; these weights already factor by roots. Each root of size t then receives a SET of satellites with weight EGF Σ_s (t!S(s,t)) z^s/s! = (e^z−1)^t. The SET of these components yields exactly the stated EGF. This does not require a new restriction, classification, or enumeration beyond the standard fibre and SET rules applied to the known factorization.

## value

FAIL

A global EGF is a convenient way to encode this census, and the minimum-class obstruction is meaningful. But the obstruction and the full image weights are already known; the only remaining change is the routine labelled SET resummation with no new enumerative difficulty or independently obtained conclusion. On this evidence the exact series alone is not a substantive surviving repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
