# Independent mathematical audit

## correctness

PASS

For h>0 take z_j=hw_j and k=3+i sqrt(3). The hub Schur complement in hL+kI is kE with E=1+sum z_j/(k+z_j); E=(U+3V)-i sqrt(3)V in the source notation. Partial fractions give the off-diagonals of T as -12 Im(k(hL+kI)^{-1})/sqrt(3). Multiplying denominators recovers the stated sign factors U-z_j V and (z_i+z_j+6)U+(12-z_i z_j)V. Since V>0, the minimum hub factor is at the largest weight. If it is nonnegative then V<=U/z_*, so the leaf factor is at least (max(z_i,z_j)+6)U+12V>0. Diagonals are positive by scalar spectral positivity and row sums are one. The maximal-weight factor is 1 minus a nonnegative combination of strictly increasing functions x^2/(x^2+6x+12); its limit is 1-Delta, yielding a unique finite zero exactly for Delta>1. Delta=1 gives no finite zero; tied maxima vanish simultaneously at H, no other entries do, and T(0)=I. For N=m+1 and the projection P onto the vector space of zero sums, the independent formula L^+=sum_j (1/w_j)(P e_j)(P e_j)^T follows by multiplication with L. Its hub and leaf off-diagonals agree with the source and give exactly w_* sum_j 1/w_j<=N. The frozen verifier was inspected but not executed; the reported exact-rational tests are finite corroboration only.

## originality

FAIL

The distinct earlier Resultary record 2f77824b8f6c gives the full arbitrary-positive-weight theorem on the same stars for the same completed fourth-order Gauss endpoint, including the sharp finite cutoff, the first-zero entries, ties and nonreentry. The pseudoinverse equivalence is a correct algebraic reformulation obtained from the elementary pseudoinverse formula on stars and the already available reciprocal-weight criterion. The prior coverage is materially stronger than the one-exceptional-spoke comparison made in the submission.

## value

FAIL

The sharp sign-change horizon, endpoint zero pattern and nonreentry law are meaningful exact data, but this submission already has a covering earlier theorem for all of them. On this family the extra Laplacian-pseudoinverse description is an elementary translation of the same criterion and is not made into a further independently useful result. No genuine substantive remainder warrants repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
