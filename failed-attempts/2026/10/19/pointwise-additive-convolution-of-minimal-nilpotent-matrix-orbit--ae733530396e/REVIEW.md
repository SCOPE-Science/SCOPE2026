# Independent mathematical audit

## correctness

PASS

For A=uφ, A²=φ(u)A, so the orbit size follows by counting nonzero φ in the annihilator of u and dividing by q−1. Negation gives the zero fiber. In rank one, independent image vectors and independent row functionals would give rank two; the common-image and common-row counts are each q^(n−1)−2 and intersect in q−2 scalar splittings. In rank two, each ordered pair of complementary image lines uniquely gives the summands by projection of C. Their squares vanish exactly when T=C restricted to its image has zero diagonal in these lines. For T=0 all (q+1)q pairs work; in the nonzero nilpotent case one line must be the kernel, giving 2q. Invertible T gives one complement T(L) for each non-eigenline L. This includes scalar exclusion in characteristic two and zero rank-one fiber at n=q=2. The 3-by-3 F3 example checks independently from GL3 order 11232: centralizer orders 18, 16 and 8 give the nilpotent, nonsplit, and split rank-two class sizes 624, 702 and 1404 respectively; adding the zero and rank-one fibers gives total mass 10816. Inspected RESULT.md lines 35–64, VERIFICATION.md and verify_fibers.py; the shipped checker is finite, and was not executed in this review.

## originality

FAIL

The exact ordered convolution is already covered by a distinct earlier Resultary record. The explicit expansion by square class or Jordan type and the numerical illustration do not give a new structural claim.

## value

FAIL

The natural pointwise invariant would be useful if undetermined, but this version re-expresses the already known exact eigenline formula by its elementary two-dimensional cases. The small illustrative histogram does not fill an independent gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
