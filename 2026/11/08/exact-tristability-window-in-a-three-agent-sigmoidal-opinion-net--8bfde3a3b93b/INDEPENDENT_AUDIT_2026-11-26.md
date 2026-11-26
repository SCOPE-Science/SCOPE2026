# Independent mathematical audit

## correctness

PASS

The stated normalized flow is a positive-weight mean of the two zealot opinions minus x. It is smooth and odd, points strictly inward at +/-1 and outside, and has at most linear growth. The time to reach the interval from an exterior point is finite by compactness of the segment from that point to the nearest endpoint and the strict nonzero drift there. Clearing the positive denominator gives drift sign on 0<x<=1 equal to the sign of Q(x)-exp(delta-1). Direct differentiation gives Q' with the sign of H=2x(1-x^2)-tanh(2x). The derivative of tanh(2x)/x is strictly negative by sinh(4x)>4x, and its values go from 2 to tanh(2)<sqrt(3). Hence H'=2(tanh^2(2x)-3x^2) goes from positive to negative exactly once. With H(0)=0 and H(1)<0, its only positive zero on (0,1) is m, on the decreasing branch. Thus Q increases from 1 to Q(m)>1, then falls to -exp(-1), with Q''(m)<0. The level comparison gives exactly the four stated censuses and sign charts. At delta=1 the slope vanishes but the positive cubic x^3/6 repels; at delta*=1+log Q(m) the nonzero double roots attract from the exterior only, with nonzero parameter derivative in the cleared factor. Global uniqueness prevents trajectories crossing equilibria; bounded monotone trajectories limit to the adjoining equilibrium, with the threshold initial states staying fixed. The two square-root scalings follow from the expansion at zero and the nondegenerate maximum. Independent replay: python3 /workspace/independent_checks.py 1 used 85-digit decimal arithmetic and maximized the parameter root derived directly from the two logistic weights; it gave m=0.457314620422500064758 and delta*=1.037743156221737164794, with direct drift checks including the cubic and fold. Sampling does not establish the global result. The accepted claim is the autonomous classification for gamma=1, not a theorem for a time-varying sweep or a transcendence assertion about delta*.

## originality

PASS

The normalized sigmoid and local criterion are established prior work on the very same model. The full scalar phase line and sharp upper threshold, including semistability and all basins, are distinct from the established statements inspected. This is a bounded comparison, not a priority certification.

## value

PASS

A local test at neutrality leaves open whether a stable neutral state can coexist with other attracting opinions. The exact interval, terminating saddle-node pair and separatrices settle that question on the smallest network with two fixed sources and one flexible node, including the distinction between the two boundary values. This is useful as a complete baseline for the established model. The supported hysteresis interpretation is the autonomous coexistence mechanism, not a claim about any specified nonautonomous sweep.

The dated certificate retains the supplied scientific assessment, sources and limitations.
