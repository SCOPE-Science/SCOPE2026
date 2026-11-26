# Independent mathematical audit

## correctness

PASS

Under exactly MK, Pos and Con, meet preservation is monotonicity and Pos at p=ceil((n-1)/2) is equivalent to f(p)>=p. For t<=floor((n-1)/2) and x<t, Con is automatic unless 2f(t)>n-1; in that case it forces f(x)=f(t). In even size the last lower input is either mapped below m or forces a constant raised prefix; in odd size the middle input is pinned at m or forces that prefix including itself. Counting weakly increasing tuples and summing over the raised prefix value gives the stated binomial squares and common additive term. Fixing the last output removes one free upper value; the dominant top-preserving proportion is m/(2m-1) in even size and 1/2 in odd size, with lower order corrections. The m=1 counts are (2,2) and (5,3). Inspected VERIFICATION.md and checker.py without executing the frozen code. Independent bounded replay: python3 /workspace/independent_checks.py tests all maps for n=2..7 and returns the stated pairs through (415,210); the structural argument proves the unrestricted result.

## originality

FAIL

Two distinct earlier indexed Resultary statements cover the same finite-chain operator class, midpoint/constant-prefix normal form and all four census formulas. The October 18 text also states the limiting top-preserving proportion. This is verified equivalent coverage rather than an inference from title similarity or an unavailable paper.

## value

FAIL

The census of a natural variety, including the prevalence of non-top-preserving maps, would be worthwhile if uncovered. This package repeats an already available full normal form, formulas and density without an additional invariant, explanation or application that resolves a distinct mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
