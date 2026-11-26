# Independent mathematical audit

## correctness

PASS

For the prey-only equation, u=1/x satisfies u′+ru=r/K. Convolution with the positive exponential kernel gives a unique positive periodic solution; all positive initial conditions converge to it in the prey-only system. Integrating over a period gives mean(u)=1/K_H; the decoupled scalar predator variational equation gives the stated Floquet exponent. For g(u)=A/(Bu²+Cu+D), direct differentiation gives the curvature numerator 2A(3B²u²+3BCu+C²−BD), with a positive denominator. At C²=BD it is still strictly positive for all u>0; nonconstant K gives nonconstant u, so Jensen is strict. For C²<BD choose a reciprocal trajectory u=u₀+δ cos(ωt) wholly inside its concavity interval, and set 1/K=u+u′/r. Choosing δ√(1+(ω/r)²)<u₀ makes K strictly positive even at an arbitrary prescribed finite frequency. Its harmonic mean is 1/u₀, and strict concave Jensen reverses the sign. The latter is an existential, not universal, reversal. At u₀=1/4 the explicit static intakes 16/69 and 16/21 follow by substitution; the example interval is strictly concave for D=4 and strictly convex for D=1. At neutrality the strict signs govern linear predator invasion only, not global nonlinear fate. Inspected VERIFICATION.md and verify.py without execution; the finite checks are supplementary to RESULT.md lines 15–68.

## originality

PASS

Credit the generalized response law, reciprocal logistic substitution, Jensen and Floquet machinery. The assessed claim is their sharp model-specific consequence: an exact necessary and sufficient coefficient boundary for the universal equal-harmonic-capacity comparison, with physically admissible smooth reversals showing necessity. The verified near neighbors do not cover this comparison.

## value

PASS

The boundary tells when a constant-capacity control with the same harmonic capacity is a rigorous lower invasion benchmark uniformly over amplitudes, shapes and periods, and when even a smooth periodic treatment can reverse that judgment. Exact sharpness from a realizable prey trajectory, rather than a formal Jensen curvature observation or a small-amplitude approximation, is useful for interpreting a neutral static control. The contribution is restricted to rare-predator invasion in the stated deterministic model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
