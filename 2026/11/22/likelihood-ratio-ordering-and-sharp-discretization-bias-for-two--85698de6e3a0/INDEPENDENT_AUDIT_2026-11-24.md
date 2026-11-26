# Independent mathematical audit

## correctness

PASS

Writing S(n)=2q^n/(1+q^n) gives a_n=S(n)-S(n+1) and exact normalization. The positive density sample weights are geometrically summable. The normalized ratio a_n/b_n is 2(1-q)Z times (1+q^n)/(1+q^(n+1)), strictly decreasing in n. Its b-weighted average is one so its first value exceeds one and its limit is below one. There is one crossing, allowing a tie at at most one integer, and TV is exactly the sum of the positive differences. For h=theta, the composite trapezoid estimate h sum_{n>=0} f(nh)=int f+h f(0)/2+O(h^2) applies to g, yg and the survival profile because their second derivatives are integrable. It gives Z=1/(2h)+1/8+O(h) and prefactor 1-h/4+O(h^2). The exact ratio expands with uniform error O(h^2) for e^(-nh) in [0,1], with first-order profile d(y)=1/(1+exp(y))-1/4 and zero log 3. Its strict opposite signs on either side give h k_h -> log 3. The positive-part map is 1-Lipschitz, so replacing the ratio minus one by h d in the b-weighted TV sum costs O(h^2) including the crossing cell. The density normalization and the Riemann-sum estimate for the integrable Lipschitz-on-pieces function 2g d_+ (with integrable derivative) reduce TV to h times its integral plus O(h^2). Substituting z=1/(1+exp y) gives 2 integral from 1/4 to 1/2 of z-1/4, which is 1/16. The integrals of g and yg are 1/2 and log 2; the survival sum starts at n=1 and contributes -1/2, while the sampled mean denominator contributes -(log 2)/2. The positive mean gap is E[B]-E[A], tending to (1-log 2)/2. For q down to zero, the n>=2 tails and their first moments are O(q^2) by geometric domination. At n=1, a_1=2q+O(q^2), b_1=4q+O(q^2); at zero, a_0-b_0=2q+O(q^2), the sole positive difference for sufficiently small q by the exact order. Both discrepancies are therefore 2q+O(q^2).

## originality

PASS

The two masses, normalization formulas and separate mean series are known, and the LR ordering itself is an immediate consequence of the defining masses or of strict continuous log-concavity. The accepted distinction is the sharp quantitative comparison of these two different same-rate discretizations, especially the scaled mass crossing and leading TV and mean-bias coefficients. No covering published comparison was identified in the inspected primary and catalogue passages.

## value

PASS

These are two independently proposed, naturally comparable count laws for the same continuous parent and parameter. The joint limits quantify when they can be close in probability yet differ in mean counts by a constant, and locate where their mass bias reverses. The independently useful quantitative discrepancy, rather than the routine ratio monotonicity alone, supports value for discretization and risk calibration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
