# Independent mathematical audit

## correctness

PASS

The count of nonempty disjoint shadows rules out zero markers for n≥2 and forces all shadows to be singletons with one marker. For two adjacent deleted positions, the surviving entries outside those positions keep their positions in both outputs; their ranks differ exactly when their values are strictly between the two deleted values. If no such value exists, the remaining member of the adjacent pair also has the same rank in both outputs. Thus a singleton shadow forces every adjacent pair to differ by 1; a permutation cannot reverse such a walk without repeating a value, so only the two monotone words qualify. This rules out one marker for n≥3. I independently enumerated the displayed codebooks (RESULT.md lines 29–46), not by executing the uploaded checker: for each deletion I replaced each surviving entry by one plus the number of smaller survivors, deduplicated within its parent, and checked cross-parent disjointness, alphabet, and exact coverage by restricting each parent to labels ≤n. For n=1,2,3,4 there were respectively 1,2,6,24 distinct messages and 1,2,16,97 disjoint outputs, agreeing with VERIFY.txt. For n=4 the shadow-size histogram is {1:1,2:1,3:5,4:9,5:5,6:3}. VERIFY.py lines 6–45 is the frozen replay path for the finite certificates; no finite test is needed for the infinite lower bound. No upper bound for n≥5 is certified.

## originality

FAIL

A distinct published Resultary record has the identical model and covers the entire nontrivial profile and the general lower bound. Its codebooks differ, but certify the same extrema. The omitted n=1 case follows immediately from the sole possible message and is not a meaningful distinct remainder. This is demonstrable claim coverage, not a conclusion about who had the result first.

## value

FAIL

The first nontrivial optima in this systematic channel are naturally motivated and useful as benchmarks. Here those precise values and a general lower bound already have explicit coverage, with finite certificates. The different codebooks are corroboration of the same result; no newly optimized secondary invariant, new coverage regime, or structural construction is established. The unit case is immediate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
