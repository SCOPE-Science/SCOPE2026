# Independent mathematical audit

## correctness

PASS

The b+1 ordered gaps of ones give a bijection with weak compositions of a into b+1 parts, including both endpoint gaps. Fixing one or two distinct gaps gives the two binomial probability ratios in the proof. Counts at distinct lengths have no same-gap cross term. For x_b=a/b and u=r+s, the first-order relative coefficient of p_j about g_j(x_b) is -j(j-1)/(2x_b)+j(j+1)/(2(1+x_b)); the coefficient of p_{r,s} about g_r g_s is -1-u(u-1)/(2x_b)+(u+2)(u+1)/(2(1+x_b)). Accounting for (b+1)b versus (b+1)^2 yields -2-rs/x_b+(rs+r+s+1)/(1+x_b), the stated kernel after putting over a common denominator. Fixed lengths and x_b bounded away from zero and infinity control the remainder. The upward quadratic has two positive roots iff its discriminant is strictly positive, since its sum and product of roots are positive. At total length u<=9 the bound rs>=u-1 excludes the positive phase; at u=10 the discriminant is positive only at (1,9). For those lengths the ratio of the mixed moment to the product of the means has positive denominator (b+1)a(n-10)(n-11) on the claimed domain. Subtraction gives the polynomial F, whose three specializations are -4t(t^2+3t+32), t(t+13)(3t-19), and -5t(5t^2-54t+97). The last bracket is positive at t=10 and increasing thereafter, and the other signs are strict. Independent replay: python3 /workspace/branches/run_independent.py checks 476 exact comparisons by extracting runs from complete small word populations and 123 signs by integer binomial counts; the frozen checker was read, not executed. The finite checks do not prove the limit or all-t signs, and no finite sign claim at the limiting roots is made.

## originality

FAIL

A distinct indexed fixed-composition theorem gives the same entire limiting covariance phase diagram after changing normalization and deleting endpoint terms. The known conditional multivariate run PGF also covers the finite moments for endpoint-inclusive runs. The exact three-family sign assertion is not stated in the inspected sources, but in the stated regime it is a direct sign evaluation of these finite moments, not a new finite distribution or a separate phase boundary. The indexed record's later date is not evidence of priority; the comparison is about mathematical coverage.

## value

FAIL

The reentrant covariance phase is a meaningful property, but its complete limiting classification and least pair are already covered. The remaining finite witness tests three deliberately off-boundary ratios for that pair and falls out of the known conditional law and a short sign calculation. It resolves no unknown finite boundary (in particular no sign at either critical ratio) and establishes no general finite classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
