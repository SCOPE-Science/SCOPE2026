# Independent mathematical audit

## correctness

PASS

The two colors are ordered, and a coincident pair of edges is a two-edge cycle, not a single path. Each block for a path has a unit triangular minor of order min(r,s); each cycle block is equivalent to I+C, with exactly one free kernel coordinate if and only if p=2 or the half-length is even. A balanced path has a unique row starting endpoint, k!^2 admissible label orders and two alternating colorings, hence 2k!^2 colored paths (the wording of RESULT.md line 37 understates the count in its explanatory sentence, not in the component term). In an unbalanced path reversal cancels the factor of two for starting colors. A labeled balanced cycle is a choice of one perfect matching and a relative k-cycle, giving k!(k-1)!. Independent labels and additive rank give the exponential. Rank n forces each block to be square and full rank, not merely total balance; odd-half-length cycles survive precisely in odd characteristic. For the asymptotic coefficient, the circle r satisfying ar/(1-r)^2=n gives real exponent 2 sqrt(an)-a/2+o(1) and angular curvature ar(1+r)/(1-r)^3 asymptotic to 2n^(3/2)/sqrt(a). With rho=1-r, the real exponent loss is ar(1+r)(1-cos(theta))/(rho*(rho^2+2r(1-cos(theta)))); hence outside |theta|<n^(-3/4+1/24) there is exponential suppression. Inside, the cubic error is o(1) and the prefactor can be held at the saddle. This reproduces the Gaussian factor and both stated constants after division by L_n(-1)^2. The independent rectangular replay matched all rank coefficients for 0<=a,b<=4 in both F_2 and F_3, 56,877 pairs per field, including the zero-size conventions.

## originality

PASS

The supported distinct result is the combined rectangular all-rank enumeration and characteristic-sensitive full-rank asymptotic for two independent partial injections. Perfect-matching cycle ranks, rook order, labeled-set enumeration and the saddle method are not claimed as new. The nearest distinct inspected records concern a different rank or a product of projections; their results cannot be reinterpreted as the submitted rank statistic.

## value

PASS

The exact labeled spectrum resolves every rank for natural constrained random matrices, not just a computation at fixed n. It explains which component types generate rank loss and yields a sharp difference in invertibility probabilities (a factor asymptotic to 2^(1/4)n^(1/4)) that full permutation results do not capture. The singularity-rate constants and characteristic dependence are useful independent of the novelty of the enumeration method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
