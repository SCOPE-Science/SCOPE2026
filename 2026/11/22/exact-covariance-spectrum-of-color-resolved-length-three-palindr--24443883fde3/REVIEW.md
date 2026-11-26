# Independent mathematical audit

## correctness

PASS

For n≥5 the five shifts 0, ±1, ±2 are distinct; their joint events constrain respectively three identical-position letters, four letters with reversed ordered pairs, or five letters with the same outer color. All other shifts use disjoint letters. This gives the exact kernel including n=5. In the edge array space the symmetric row-sum map has rank q (a vector in the left nullspace would have x_a+x_b=0 for every a≠b, hence is zero for q≥3), while the skew row-sum map has rank q−1 (its left nullspace consists of constants). Their kernels give the two circulation multiplicities, with zero symmetric multiplicity at q=3. The constant and both centered color contrasts form their orthogonal complement. In the row/column contrast coordinates, multiplying the action by q^5 gives a 2×2 block with entries q²+2(q−1), 2q−2, 2q, q² in row-major order. Its midpoint is q²+q−1 and its half-gap is Δ=√((q−1)(5q−1)). The other modes act by scalars; comparing Δ with q+1, 2q−4 and 3q−1 proves the ordering and positive least eigenvalue. Their ratio yields the stated condition number and expansion. The usual fixed-q 2-dependent CLT on a line gives Σ_q as long-run covariance; wrapping changes at most two counts per coordinate, and whitening the limiting Gaussian gives the chi-square law. Independent replay: python3 /workspace/review_checks/3.py computes exact covariance matrices from full circular word enumeration and compares their exact characteristic polynomials for (q,n)=(3,5),(3,6),(4,5),(5,5). The all-q and asymptotic claims rely on the proof, not the finite tests.

## originality

PASS

The contribution is the complete explicit finite-circle spectrum, including dimensions, ordering and conditioning for ordered color motifs. General overlap-covariance methodology, the positivity-to-whitening step, and a fixed-q finite-dependence CLT are not independent novelty claims. Closely related triple-count spectra concern different statistics. The general word-occurrence paper remains a bounded access risk.

## value

PASS

Counting by ordered outer and inner colors makes the covariance a nontrivial operator rather than a single palindrome total. The decomposition separates coupled color contrasts from symmetric and skew circulation, establishes invertibility even on the smallest supported circle, and quantifies stability as the alphabet grows. This directly supplies a fixed-q omnibus null calibration without estimating a nuisance covariance; it does not assert exact finite-sample chi-square behavior or power.

The dated certificate retains the supplied scientific assessment, sources and limitations.
