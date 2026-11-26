# Independent mathematical audit

## correctness

PASS

Under identical positive pulse sizes, an initially empty linear store and the exponent-two response, integrate on the two segments with antiderivative −log(1+C² exp(−2kt))/(2k). With u=a² and x=exp(−kτ), the derivative of the dimensionless logarithmic score divided by 2u simplifies to −[u x(1+x)−1]/[(1+ux²)(1+u(1+x)²)] + q²(1+x)/[x(x²+u q²(1+x)²)]. Combining the fractions independently gives N=x³[u x(1+x)−1] and D=(1+x)[1+u(3x²+3x+1)], exactly the stated polynomials. On the feasible x∈[q,1], H'(q)>0 since q²D(q)−N(q)=q²(2q+1)[1+u(q+1)²]. If u≤1/2, N≤0 everywhere. Otherwise N>0 precisely above the positive root ρ_a, where xN'/N>3>xD'/D. Thus N/D is strictly increasing on its positive branch and the derivative can switch only from positive to negative. Its right-end comparison is q² versus (2u−1)/(14u+2), proving the unique maximum including equality and the correct feasible interval for the interior root. The positive-branch inverse decreases in T and converges to ρ_a, giving strictly increasing delay only in the staggered regime and a finite limiting delay as claimed. An independent bounded numerical bisection at a=k=1,T=2 gave τ*=0.235356202245 and scores 0.769367392875 and 0.777192014422. RESULT.md, VERIFICATION.md and check.py were inspected; uploaded code was not run. The checker brackets but does not test exact horizon equality, and its 7,500 count combines 1,500 quadrature checks with 6,000 candidate comparisons, not an exhaustive optimization test.

## originality

PASS

The closest distinct indexed finding solves the exponent-one scheduling problem; the closest inspected Hill-two dosing comparison fixes the times. Neither theorem yields the response-dependent finite-horizon transition and bounded optimal lag for these controls. Historical irrigation overlap remains a stated access risk, not evidence of coverage.

## value

PASS

The timing question is motivated by the competition between beneficial concentration overlap at low stores, saturation at high stores, and truncation by the observation deadline. The result gives the exact onset of staggering, proves it is globally unique, and shows the optimal spacing saturates rather than scaling with horizon. This is useful as a closed-form benchmark for scheduling under cooperative response, not empirical advice about plant growth or dose timing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
