# Independent mathematical audit

## correctness

PASS

Convolving the two independent exponentials and differencing their survival at successive unit bins gives p_n=A u^n−B v^n for unequal rates, with u=e^(−a)>v=e^(−b), A,B>0 and p_0>0. The displayed normalized PGF has denominator (1−uz)(1−vz) and numerator 1+rz; r>0 by strict increase of (e^x−1)/x. The log coefficients are (u^n+v^n+(−1)^{n−1}r^n)/n. If r≤u they are positive and summable, including at equality; otherwise sufficiently large even coefficients are negative. The discrete and real-line notions agree here: any iid real convolution roots of this nonnegative law must themselves be nonnegative (otherwise all copies can be negative), must have an atom at zero, and must be integer-supported because the other copies can all be zero. For q=e^(−a) and t=b/a>1, clearing positive denominators reduces r≤u to F_q(t)≥0. The identities F_q(1)=F_q(2)=0 and −log q>2(1−q)/(1+q) imply strict convexity on t≥1, so this holds exactly for t≥2 outside the diagonal. On the diagonal, differencing the Erlang survival gives a squared pole and r/u=(a+u−1)/(1−u−au)>1 by the same inequality. The discrete Bilal survival is exactly the 3:2 rate case; its mass is strictly log-concave since p_n²−p_{n−1}p_{n+1}=AB(uv)^{n−1}(u−v)²>0 for n≥1. At an even index the obstruction is ((2+p)/(1+2p))^n>1+p^n. There is a unique positive continuous crossing; the strictly larger next even integer is within two, including an even crossing. Rescaling the crossing by 1−p gives monotone bracketing at the unique root of e^(c/3)=1+e^(−c), yielding the asserted limit. The independent exponential Laplace factors give the two zero-based geometric counts for Poisson observation, one factor per stage, even when the rates agree.

## originality

PASS

The exact rate-ratio classification and moving first obstructing coefficient are the contributions under review, not the discrete Bilal mass, general compound-Poisson criterion, or the always divisible geometric-convolution representation. The strongest distinct indexed matches were compared at their original rational PGFs: neither is the same law or gives the binned two-distinct-rate phase boundary. The highly relevant earlier discretized hypoexponential paper has an inaccessible original full text; its abstract establishes a closely related object, not affirmative coverage of the criterion. The conclusion is qualified accordingly.

## value

PASS

The rate threshold characterizes exactly when an operationally natural integer-time observation retains an ordinary compound-Poisson description. The same two-stage lifetime under Poisson observation always has this description, so the contrast is attributable to the observation rule rather than the existence of a mixing representation. The Bilal coefficient delay is a quantitative mechanism for why checking an arbitrary fixed finite list can miss failure, even in a strictly log-concave count family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
