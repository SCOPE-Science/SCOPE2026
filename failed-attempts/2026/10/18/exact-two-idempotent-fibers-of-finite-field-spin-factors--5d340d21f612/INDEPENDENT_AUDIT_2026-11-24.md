# Independent mathematical audit

## correctness

PASS

Idempotency gives a=1/2 and Q(u)=1/4 for any nontrivial idempotent. Such an idempotent cannot split into two nonzero orthogonal idempotents: nontrivial summands each have scalar part 1/2, and 1 cannot be an orthogonal summand of a proper idempotent. Writing u=w+z, v=w−z gives b(w,z)=0 and Q(z)=c−Q(w) and fixes the scalar part of the product at 2Q(w). Thus ordered pairs are counted once by z. For Q(w)≠0 the determinant of w-perp is Δ/Q(w); for nonzero isotropic w take a partner of pairing one and subtract Q(partner)w/2 to split off a determinant −1 hyperbolic plane. The orthogonal complement then has radical spanned by w, giving q lifts of each vector of a quotient of determinant −Δ. Diagonal Gauss sums with G²=χ(−1)q give the four parity/value subcases in the record; in odd rank the extra sum at nonzero t is χ(−t)G, fixing the sign. The counts are positive in rank ≥2; in the ternary isotropic case the rank-one count is 1+χ(−Δ), and the number of nonzero isotropic w is q²−1. Independent bounded replay (python3 /workspace/branches/independent_replays.py, function spin) checked constancy by norm and the missing locus in ten configurations, including both determinant classes in dimensions 3 and 4 over F9. VERIFICATION.md's description of an ‘anisotropic ternary case’ is imprecise: it is the rank-one quotient level c that fails, not absence of isotropic vectors in the ambient ternary form. This does not affect the stated or checked theorem.

## originality

FAIL

The frozen claim does not establish a distinct new enumerative result. Its entire square-determinant fiber profile and its headline ternary obstruction in both determinant classes are already determined by the published finite Euclidean association-scheme intersection data. The standard other determinant case in even dimension uses the very same intersection calculation with a determinant-character factor. The Jordan product interpretation is useful but is not a new enumeration: the exact translation is z in S_c(0)∩S_c(2w) paired with the unique partner 2w−z. This is a coverage/implication failure for the central claim, not a claim that a prior paper prints the complete Jordan-formatted table, and not a decision based on inaccessible literature or the later Resultary record.

## value

FAIL

The spin-factor restatement is explanatory but does not add a worthwhile exact invariant beyond the already determined equal-radius intersection numbers. In particular the apparently new, useful ternary saturation boundary is a forced entry/zero pattern in prior data after odd-dimensional rescaling. The only gap left by that particular published eigenmatrix's scope is the other even-dimensional determinant class; its computation is a standard determinant-sign substitution with no new obstruction. A narrowed claim of that substitution alone would not be a valuable repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
