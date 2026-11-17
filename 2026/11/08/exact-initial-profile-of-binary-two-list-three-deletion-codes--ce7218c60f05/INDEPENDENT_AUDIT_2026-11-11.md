# Independent mathematical audit

## correctness

PASS

The three-deletion channel relation is A_yx=1 iff y is a length-(n-3) subsequence of binary source x. Each given witness has at most two sources containing any output, and rational dual weights w_y plus s_x=max(0,1-sum_y A_yx w_y) obey 1<=sum_y A_yx w_y+s_x for every binary source. Thus any feasible code has size <=2 sum_y w_y+sum_x s_x. For n=3..10 the exact certificate provides upper bounds 2,3,4,4,4,22/3,659/60,2693/180, whose floors equal the witness sizes 2,3,4,4,4,7,10,14. Independent BigInt exact enumeration of every source x and received word y and all eight certificate datasets verified all list capacities, rational upper-bound identities, and rounding gaps. These exhaustive finite checks prove the precise finite claim via duality; no unbounded n is asserted.

## originality

PASS

Lin arxiv:2609.26650 concerns the same t-list k-deletion predicate and proves asymptotic bounds. A substantial accessible rendered portion of Lin paper was examined; it gives parameter-general asymptotics but no listed exact n=3..10 optima. Other Resultary prior findings concern 1- or 2-deletions and different list capacities, not three-deletion list two. No exact table matching all eight values appeared in Resultary searches. This is best-of-knowledge priority, not proof no prior unindexed finite computational census exists.

## value

PASS

Two-list three-deletion codes are a natural adversarial channel problem; the short-length optimal profile and the first length eight that exceeds four codewords supply exact finite cutoffs for coding design. The eight integers include genuinely nontrivial n=8..10 bounds proved by independently checkable rational packing certificates and are not merely recomputed standard tables. No asymptotic or long-length claim is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
