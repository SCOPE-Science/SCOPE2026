# Independent mathematical audit

## correctness

PASS

Each one-hit service probability is 1−exp(−μ); independence is needed for the product J, not for summing expectations in S. Outside the crop interval both means strictly decrease as one moves farther out, so neither objective has an exterior maximizer. Inside, for t=kx≥0, the means are qe^t and qe^(−t). Comparing the two positive terms in S'(t) by their log ratio gives 2(t−q sinh t). The function t/sinh t decreases strictly from 1, since the numerator of its derivative has derivative −t sinh t and starts at zero. Thus at q=1 the derivative is negative for every t>0, at q=D/sinh D it is positive on (0,D) with zero endpoint derivative, and between the thresholds there is a unique interior sign change. Reflection gives all maximizers. For J, h(s)=log(1−exp(−e^s)) has derivative u/(e^u−1), u=e^s; this is strictly decreasing in u because e^u(1−u)−1<0. Jensen's inequality at the two log means gives J(x)<J(0) whenever x≠0 inside the crop interval, and exterior monotonicity handles the rest. Multiplying the q-bounds by e^D gives e^D and 2D/(1−e^(−2D)); the latter is strictly between 1 and e^D and increases from 1 to infinity by e^(2D)>1+2D. This gives the fixed-strength transition order. Expanding t/sinh t=1−t²/6+O(t⁴) yields the claimed continuous onset; substituting t=log 2 and D=log 4 confirms the stated optimizer and numerical coverage example.

## originality

PASS

The inspected same-day records have meaningful overlaps in exponential placement or two-site Poisson optimization, but use different decision sets, success rules, or objectives. None supplies the two sharp S thresholds together with universal midpoint J for the stated model. The one-hit Poisson response, exponential attenuation and log-concavity argument are not credited as novel on their own. Some named literature could not be fully inspected; this is a bounded assessment, not a historical-priority claim.

## value

PASS

This exactly solvable spatial example distinguishes optimizing the expected served count from ensuring neither crop fails. The first objective has a nonempty phase with genuinely interior asymmetric maximizers between midpoint and crop-endpoint regimes; the second always strictly favors the midpoint. The sharp boundaries, equality cases and continuous onset give a meaningful benchmark beyond the standard Poisson success formula or an isolated parameter example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
