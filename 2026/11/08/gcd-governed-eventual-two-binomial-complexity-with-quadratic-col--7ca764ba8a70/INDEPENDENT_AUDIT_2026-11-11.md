# Independent mathematical audit

## correctness

PASS

For each starting phase s, the factor at n=mp+r is U_s^m T_{s,r}. Its two-binomial signature is determined by its ones count and scattered 01 count, and its 01 count equals m q(U_s)+binom(m,2)ab+ma c(T)+q(T). The full-period q(U_s) values on the zero and one branches are integer multiples b and a with exactly g-1 intersections; hence p-g+1 distinct signatures at r=0. For m>binom(p-1,2), any collision requires equal full-period q and equal tail one-count. The only interior r at which a cross-branch equal-q pair has equal prefix one-count yields tails 0^u1^(b-v) versus 1^(b-v)0^u with distinct 01 counts. This proves p signatures for each nonzero residue. The explicit a=2h+1,b=2h+3 witness has full-period q difference 1, tail q difference h(h+2), and collides at m=h(h+2)=p^2/16-1. Independent direct two-binomial signature enumeration verified 1152 stable residue cases a,b<=8, and 24 quadratic-delay witnesses h=1..24. No infinite result is inferred solely from these tests.

## originality

PASS

PASS best-of-knowledge: general Parikh-matrix power identities compute concatenation statistics but do not classify cyclic starting-phase coincidences; the published 2025 binary 1-balanced sufficient theorem covers boundary families with min(a,b)=1 but cannot imply gcd-dependent deficits for unbalanced two-long-run words or quadratic-delay collisions. Independent Resultary searches for cyclic two-binomial complexity, Parikh matrices, two-run periodic words and equivalent phase formulas found no earlier matching all-length eventual classification.

## value

PASS

The gcd-deficient number of cyclic 2-binomial profiles is an exact natural information-theoretic invariant of a simple periodic word, and the family of collisions persisting quadratically many complete periods proves the stabilization scale is genuinely nontrivial. This supplies more than a routine individual Parikh-matrix computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
