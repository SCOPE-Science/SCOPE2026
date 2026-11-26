# Independent mathematical audit

## correctness

PASS

Over C the weights n i+j (j indexed from 0 to n−1) define row/column scaling and are pairwise distinct, so the only projective fixed points are the mn matrix units, each of rank one. Euler localization on the compact, possibly singular rank locus gives χ=mn. Independently, an exact-rank-p stratum maps to the product of kernel and image Grassmannians with Zariski-locally trivial fiber PGL_p; p>1 contributes zero to compactly supported Euler characteristic, and p=1 is the Segre product with χ=mn. Transpose to the universal map O(−1)^m→O^n; the generic maximal-minor locus has codimension n−m+1, and the single Chern coefficient of (1−H)^−m in that codimension is binom(n,m−1). The adjacent ratio n/(n−m+2) strictly exceeds 1 for m≥3. At n=m,m+1,m+2 the ratios are 1/m, 1/2 and (m+1)/6. This settles m≥5; m=4 crosses between n=6 and n=7 (ratio 5/4 at 7), m=3 has ratio (n−1)/6, and m=2 is identically 1/2. Thus the two equality formats and every strict inequality range in the frozen Finding are correct. The verification file and checker were inspected read-only; its bounded tests do not prove the universal classification.

## originality

PASS

Only the precise all-size comparison is credited as a distinct statement on the evidence inspected. The constituent degree formula is covered by earlier general results, and the Euler formula is explicit in the square case and an unchanged fixed-point computation in the rectangular case. No inspected source shows the combined comparison stated as a classification. This narrow distinction does not meet the separate scientific value requirement.

## value

FAIL

The meaningful invariants are already computable by the unchanged coordinate fixed-point argument and the standard degree formula. Comparing their magnitudes has no mathematical motivation in the frozen record beyond juxtaposition: no geometric equality criterion, use of the threshold, or reason to single out these equalities is established. Once written as binom(n,m−1)/(mn), the whole crossover is immediate monotonicity plus three edge values and a small case check. The work mainly tabulates a mechanically implied comparison of two natural but unrelated numbers; no independently useful unknown exact fact is established. This is a value rejection, not a mathematical error or an access problem. No evidenced valuable remainder warrants a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
