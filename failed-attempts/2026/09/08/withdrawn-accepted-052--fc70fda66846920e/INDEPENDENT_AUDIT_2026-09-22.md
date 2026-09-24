# Independent audit — 2026-09-22 campaign

**Record:** `SCOPE-20260908-052` / `2026/09/08/052`  
**Reviewed UTC date:** 2026-09-24  
**Audited public commit:** `f1bee63e7115a5c2a8df4210f09faab70a83c26b`  
**Source tree:** `175c0491e967895461062472a136d4d895238a8f`  
**RESULT.md blob:** `1ba4be6f20c2f5eab253a6b17cb56fc38a2df0d9`

## Claim audited

For `lambda=(4,2,0,0)` and `mu=(4,2,1,0)`, the record gives the complete base Littlewood-Richardson decomposition, identifies `nu*=(5,4,2,2)` with coefficient 2 and `nu_max=(6,4,2,1)` with coefficient 4, and claims the stretched formulas
`P(t)=t+1` and `Q(t)=(t+1)^2` for all integers `t>=0`. It presents the first ray as explicit KTT test data and says general theorems imply polynomiality but "give no explicit coefficients for any concrete ray."

## Correctness — PASS for the mathematics

I independently implemented the Littlewood-Richardson tableau rule with exact dynamic programming, rather than using the record's hive or Steinberg code.

At `t=1` it reproduces the first constituents and multiplicities, `c(lambda,mu;nu*)=2`, `c(lambda,mu;nu_max)=4`, exactly 25 nonzero constituents among the 39 partitions of 13 with at most four parts, a unique maximum multiplicity 4 at `nu_max`, and the Weyl-dimension identity
`sum_nu c(lambda,mu;nu) dim(V_nu)=17640=126*140`.

For `t=0,...,8`, the independent tableau counter gives:
`P(t)=1,2,3,...,9` and `Q(t)=1,4,9,...,81`, exactly matching `t+1` and `(t+1)^2`. The record's displayed all-t hive reductions are algebraically consistent with those formulas.

The mathematical coefficient formulas are therefore supported. The record's literature/novelty sentence is not mathematically correct as a statement about prior knowledge, and is handled under originality below.

## Originality — FAIL

A decisive prior theorem was omitted. Cass Sherman's *Geometric Proof of a Conjecture of King, Tollu, and Toumazet* explains that the conjecture "if a Littlewood-Richardson coefficient of value 2 is stretched by a factor of N, the resulting coefficient has value N+1" had already been proved by Ikenmeyer; Sherman gives a geometric generalization. The paper states explicitly that when `c(lambda,mu;nu)=2`, one has `c(N lambda,N mu;N nu)=N+1` for every `N>=1`.

Full text inspected at:
https://arxiv.org/abs/1505.06551
See the introduction, especially the discussion around Theorem 0.1 and Remark 0.1.

Because this record's `nu*` is defined precisely by `c(lambda,mu;nu*)=2`, its headline formula `P(t)=t+1` is an immediate instance of the pre-existing theorem, contrary to the record's assertion that general results give no explicit coefficients for concrete rays.

The companion formula `Q(t)=(t+1)^2` may be a previously untabulated exact ray; targeted exact-partition searches did not locate that specific identity. But the record packages P and Q as one novelty claim, and one central all-t formula is already wholly covered by prior theory.

## Scientific value — FAIL

The P ray is prior art. The remaining Q ray is a single low-rank, hand-selected hive fiber with a two-dimensional elementary lattice count; it introduces no new general method, chamber theorem, coefficient bound, or structural classification. By the record's publication date, general polynomiality was long known, and current rank-four work also addresses positivity structurally rather than by isolated ray examples (e.g. arXiv:2607.22301).

The exact Q computation can be useful as a unit test for LR/hive software, but paired with a prior-art P formula it does not meet the campaign's scientific-value threshold.

## Final disposition

**FAILED.** The coefficient computations are correct, but originality fails because `P(t)=t+1` is a direct known theorem for every multiplicity-two LR coefficient, and the residual single-ray Q calculation does not supply sufficient scientific value.
