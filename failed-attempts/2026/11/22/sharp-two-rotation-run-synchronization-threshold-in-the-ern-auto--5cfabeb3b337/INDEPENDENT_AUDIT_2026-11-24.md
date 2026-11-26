# Independent mathematical audit

## correctness

PASS

For words with no aa, once b occurs, the only possible images are S={1,…,n−1} and T=Q∖{1}, with Sb=S, Sa=T, and Tb=S; after reaching T another a is forbidden. Hence the minimum rank is exactly n−1 and cannot be one for n≥3. On S, x=ab is increment modulo N=n−1. The block y=aab acts as x² except at N, which maps to 1 instead of 2. Therefore e=yx^(N−2) fixes 1,…,N−1 and maps N to N−1, also when N=2 and the exponent is zero. After be, xe shrinks the interval [j,N−1] to [j+1,N−1] until singleton. All blocks end in b, with runs of at most two rotations. Direct counting gives 2n²−5n+1. The classical unconstrained lower bound gives quadratic growth, not exact optimality of this word. Independent bit-mask subset/constraint BFS (python3 /workspace/branches/independent_checks.py 4) found no cap-one reset for n=3,…,12, verified the witness for those sizes, and found cap-two minima 4,11,20,33,48,67,88,113,140,171. This range also independently agrees with the closest indexed stronger formula, not a proof of that formula for all n. Frozen verify.py inspected, not executed.

## originality

FAIL

The strongest distinct indexed record explicitly solves the same all-n no-triple rotation problem, with an optimal witness and strictly smaller lengths for n≥4. It covers the substantive positive existence and quadratic construction-length claim; the stated uniform dichotomy appends a direct no-aa invariant, not an established distinct substantial finding. The exact displayed word is verified here but is not asserted identical to another word. This is a coverage decision, not a priority or authorship decision based on a shared date.

## value

FAIL

Bounded-run reset length is a worthwhile problem, but its substantive existence and length component is covered by a sharp constructive all-n result. The surviving direct observation that the normalized block ab is a permutation (no-aa obstruction) and a longer elementary witness are not shown to address a separate useful gap, e.g. a different invariant or control objective. No demonstrated independent valuable remainder justifies a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
