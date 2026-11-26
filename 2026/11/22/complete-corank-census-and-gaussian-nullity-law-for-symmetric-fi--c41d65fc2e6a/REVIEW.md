# Independent mathematical audit

## correctness

PASS

The repaired finding is the fixed-q Gaussian law with explicit linear mean and variance. The supporting finite formula is correct: each zero offdiagonal splits the matrix, and a block with nonzero internal offdiagonals has kernel dimension at most one by forward substitution. If S and T are the positive-dimension generating series for invertible and all matrices with constant term 1, respectively, then 1/S=1−B0 and 1/T=1−B0−B1 for the two block types. Hence the repaired series is 1/((1−t)/S+t/T). Inserting the inspected recurrence for S and T=(1−q(q−1)z)/(1−q²z) gives the original rational polynomial. Independently, the three end-pivot cases give the same recurrence: a nonzero end diagonal gives q(q−1) smaller problems with unchanged nullity; a zero end diagonal and zero joining edge gives one free kernel coordinate; a zero diagonal and nonzero joining edge yields an invertible 2-by-2 pivot with inverse entry zero at the vertex connecting to the rest, in q²(q−1) ways for n>=3. At n=2 the extra joining edge is absent. In the repaired proof the two-root expansion is explicitly restricted to n>=1, since a constant part of the rational function affects n=0. Near t=1 the dominant root q² is separated from −(q−1) and its coefficient is 1/q at t=1. The uniform analytic remainder permits termwise first and second derivatives of the log moment generating function. The logarithmic t-derivatives of the dominant root are 1/D(t) and −a(t)/D(t)^3; the t=exp(s) chain rule gives the two asserted coefficients, and a centered characteristic-function expansion proves the normalized limit. The variance is strictly positive for q>=2. Recorded finite rank checks are not a proof of the limit.

## originality

PASS

This passes only the repaired asymptotic finding, not the frozen presentation of the finite corank census as a separate original claim. The frozen prior-implication comparison was materially wrong: the published invertible census implies the full marked census by elementary block decomposition and formal series inversion, even though determinant-zero fibers alone do not distinguish coranks. The repair makes that implication explicit. The inspected earlier sources do not give the fixed-field Gaussian law and both explicit slopes for this sparse symmetric ensemble. It takes an additional asymptotic argument beyond the invertible counts or block compositions.

## value

PASS

For a natural sparse symmetric finite-field ensemble, the remaining theorem exhibits positive linear nullity with an explicit density and variance, sharply distinguishing it from the tight dense model and the bounded nullity of a connected block. It characterizes the fluctuations for every fixed field size, rather than just providing an extra finite count or a numerical fit. The corrected exact census serves the proof, not the value argument on its own.

The dated certificate retains the supplied scientific assessment, sources and limitations.
