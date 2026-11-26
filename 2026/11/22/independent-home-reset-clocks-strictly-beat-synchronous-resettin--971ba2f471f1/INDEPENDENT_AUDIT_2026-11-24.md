# Independent mathematical audit

## correctness

PASS

The ordinary collision intensity is a constant 2q, q=1/(n-1); common alarms cannot kill. With independent clocks the integrating-factor derivative for e^(2qt)S(t) is minus e^(2qt) times the expected extra reset killing intensity on live states. At every t>0 the live path (A,B) to (A,C) to (B,C) followed by no further events has positive probability, so this derivative is strictly negative. For the mean the five classes and their rates follow by counting ordinary jump destinations and lethal versus nonlethal resets. An independent algebraic elimination uses x=r/q, m=n-2 and d_i=1-2q*t_i in the backward equations. The H, X and W rows give d_U=(m+1)d_H/m, d_X=(m*d_V+x)/(m+1+x), and d_W=((1+x)d_U+d_V)/(3+x) when W is present. Substitution in the U row gives d_V=(x+2m+5)d_H/m; this holds also at m=1 with the W coefficient zero. Subtracting the U row from the V row then gives d_H=m*x/[2x^2+2(2m+5)x+(m+2)(m+4)], yielding the boxed mean and gain. Differentiation leaves the sign of 2(n-1)^2*r^2-n(n+2), proving the unique optimum and the stated maximal gain and limit. For n=2 with home start, any ordinary jump is lethal and the resets before it are ineffective. Matching total alarm rate simply sets r=lambda/2. Independent exact ordered-pair computations at four rational rates for n=3 through 6 matched 16 means, corroborating but not replacing elimination.

## originality

PASS

The exponential non-reset law is established and neutrality of resetting both walkers to distinct homes follows from its constant-hazard mechanism. The distinct contribution is the strict survival ordering for independently timed home resets, together with the exact mean and unique rate optimizer in this all-site continuous-time setting.

## value

PASS

For a basic encounter process, the law-level comparison separates clock architecture from total reset-event rate. The exact formula further explains why makespan improvement is not monotone in separate-clock rate: ineffective slow resets and near pinning at distinct homes for rapid resets leave an interior optimum with a nonzero large-graph gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
