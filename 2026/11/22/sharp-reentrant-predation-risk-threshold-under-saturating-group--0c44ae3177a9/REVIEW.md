# Independent mathematical audit

## correctness

PASS

On x>0 the hazard is positive and logarithmic differentiation gives H−b, with H=G(x^p)/[x(x^p+a)(1+x^p)] and G(z)=−z²+Bz−a. For p≤1, G<0; otherwise G has a positive interval iff B>2√a, equivalently √a<(p−1)/(p+1). At equality G has one isolated double zero, compatible with strict functional decrease when b=0. In the positive interval, writing y=log x gives log H as log(e^(py)−z_−)+log(z_+−e^(py))−y−log(e^(py)+a)−log(e^(py)+1); each nonlinear term after incorporating its sign has strictly negative second derivative. With log H going to −∞ at both ends there is a unique unimodal positive hump. This implies exactly the two intersections for 0<b<b_c (two support endpoints for b=0), and the −,+,− derivative signs. At b=b_c the second derivative of H at its maximum is strictly negative, so R′ has a quadratic zero, R‴<0 there and the point is a horizontal inflection. At a↑a_c, the two z-roots coalesce at t, the vertex value is p(a_c−a)+O((a_c−a)^2), and the denominator converges uniformly to t^(1+1/p)(1+t)^2 across the hump. For a↓0 with p>1 fixed set x=a^(1/p)u; positivity requires u^p>1/(p−1), and the rescaled positive value is bounded by (p−1)/u. Together with local uniform convergence to F_p and an interior positive test value, these exclude escaping maximizers. Differentiating F_p in w=u^p gives the stated quadratic with one positive root. Independent `python /workspace/replay_checks.py 2` verifies that quadratic symbolically and isolates the two exact positive roots in the p=2 example, numerically reproducing the peak and both stationary coordinates. Conditional capture success is nonincreasing, constant at b=0; the assertions concern the continuous model, not integer or empirical estimates.

## originality

PASS

Combined attraction/avoidance, dilution and group-size risk thresholds are not new. The distinct supported contribution is the exact sharp and unique attenuation threshold, complete continuous critical-point diagram and two endpoint laws for the specified Hill factor and separate exponential capture term. Available ecological statements do not cover that mathematical combination; the underlying attack-abatement literature has residual full-text uncertainty.

## value

PASS

For a model motivated by separately observed encounter, capture and dilution effects, a unique bounded adverse-risk interval is a meaningful structural alternative to universal dilution protection. The two sharp thresholds indicate when a reversal can exist, and the asymptotics quantify how its attenuation tolerance varies near baseline extremes. This is useful model behavior, not a claim of fitted capture rates, a discrete ecological optimum or field verification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
