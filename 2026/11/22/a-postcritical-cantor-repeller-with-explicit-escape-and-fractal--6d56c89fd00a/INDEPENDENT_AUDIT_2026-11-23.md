# Independent mathematical audit

## correctness

PASS

Solving K_μ(x)=y yields two inverse branches separated by the level-one hole when μ>3+2√2. Differentiating Q=(3μ−y)/sqrt(μ²−6μy+y²) gives positive derivative, so inverse derivative magnitudes attain their exact minima at 0 and maxima at 1, with the right branch controlling the maximum. The inequality U_+<1 has positive sides before squaring; the difference of squares is 4μ(μ³−7μ²+5μ−1). The cubic is negative at the hole threshold and increasing thereafter (its derivative is positive there and increasing), so the root is the sharp strict one-step boundary. Above it, the disjoint inverse contractions give the full one-sided two-shift, exactly 2^n fixed points of the nth iterate among survivors (including smaller periods), and derivative magnitude at least U_+^(−n)>1 there. The log-derivative Lipschitz bound summed over contracting suffixes gives uniform distortion C; applying it to S_m yields C^(−1)A_nA_m≤A_(n+m)≤CA_nA_m. Subadditivity gives the limit, and the lower distortion bound for the hole removes a fixed positive volume fraction at every stage. The displayed slope-sum lower bound on the escape exponent can be negative near threshold; strict positivity correctly uses the hole-loss argument instead. Exact inverse slope bounds give the finite-time inequalities and the O(1/μ) gap about log(μ/3). For dimension, upper word-wise derivative products bound a covering sum. The Bernoulli weights from the lower-slope root give a Frostman bound via disjoint stopping cylinders whose sizes are comparable to the observation scale by distortion. Since each level-n cylinder has length ≥μ^(−n), exponential volume loss also bounds the sum of t-powers for some t<1. For L=log μ, inverse slope asymptotics and the mean-value theorem give a root bracket gap O(1/(μ L²)); expanding sL=log(1+exp(s log 2)) then yields the three displayed coefficients. Independent exact checks of the threshold factorization and endpoint signs bracket the root by 6.2222625231203986 and 6.2222625231203987. Diagnostic Decimal checks of 410 inverse/derivative cases and survival lengths through n=10 at μ=7 agree; they are not proofs of the infinite conclusions. Inspected source support without executing uploads. Replay: python3 /workspace/branches/b52825f2-caac-40ec-9e12-730049f18193/ordinal4_numeric_check.py. No first threshold for eventual expansion, no fixed-gain closed form for dimension or escape exponent, and no assertion about post-exit returns or the full real dynamics.

## originality

PASS

Best-of-knowledge pass for the map-specific one-step threshold and postcritical quantitative laws. Neither the rational map nor standard Cantor coding, distortion, or inverse-slope dimension comparison is new. A prior three-symbol result also exemplifies multi-term dimension asymptotics from unequal contractions, but is not the same family or the same survivor statistic.

## value

PASS

Once the motivating model loses interval invariance, it is natural to ask what never leaves and how the surviving fraction decays. The exact branch threshold, quantitative survival bounds, and diverging escape exponent with explicit leading constant answer that question on a provable whole gain range. Unequal branch slopes contribute specific higher-order dimension terms; the value is this quantitative description of a natural open system, not generic symbolic coding or a claim about every gain above the hole-opening point.

The dated certificate retains the supplied scientific assessment, sources and limitations.
