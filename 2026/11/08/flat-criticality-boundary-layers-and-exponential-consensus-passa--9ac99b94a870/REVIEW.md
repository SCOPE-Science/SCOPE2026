# Independent mathematical audit

## correctness

PASS

PASS. Independently reconstructed the finite birth-death transitions for m susceptibles and two opposite zealots: p_k=(m-k)/m F_alpha((k+1)/(m+1)) and q_k=k/m F_alpha((m-k+1)/(m+1)), where F_alpha(x)=[1+sgn(2x-1)|2x-1|^alpha]/2. Detailed balance gives consecutive weight ratio [(1-x)/x]*F_alpha(x)/[1-F_alpha(x)] at x=j/(m+1), and exact symmetry. For alpha=1 ratios are one and the stationary distribution is exactly uniform; telescoping the first-hit birth-death recurrence gives E_0 tau_m=m(m+1)H_m under one-update clock. Verified by an independent Fraction-valued absorbing linear-system calculation for m=2,...,9. For alpha<1 the potential maximum lies at two endpoints, with geometric fixed-distance limits (1-alpha)alpha^j/2; for alpha>1 its unique nondegenerate quadratic potential maximum has local curvature -2, yielding Gaussian variance m/4. The exact positive mean first-passage sum and Laplace principle give logarithmic barrier |int_0^{1/2} log r_alpha(x) dx| for fixed alpha != 1. Endpoint expansions F_alpha(x)=alpha x+o(x) and reflection justify the finite integral. Checked source verify.py and the mathematical proof rather than trusting output.

## originality

PASS

PASS qualified. Reina/Njougouo's polling response is acknowledged but their original studies have one-sided zealots or heterogeneity; Mobilia's equal-zealot nonlinear q-voter draws unanimity groups and uses different rates, so its bimodal stationary and switching assertions do not force this exact F_alpha-specific finite law, critical harmonic formula or explicit all-alpha barrier. General one-dimensional birth-death reversibility is an established technique, not itself novel; exact evaluation for the specified model remains a differentiated result.

## value

PASS

PASS. Distinguishes finite-population critical flatness, boundary-localized versus Gaussian stationary fluctuations and exponential first-entrance barrier in a concrete nonlinear response model. The exact clock normalization and m(m+1)H_m crossover offer a usable quantitative benchmark for competing zealot models. The structural response-dependence makes this more than a generic invocation of known metastability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
