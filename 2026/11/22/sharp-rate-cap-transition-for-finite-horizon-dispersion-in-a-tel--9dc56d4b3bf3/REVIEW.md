# Independent mathematical audit

## correctness

PASS

The initial sign symmetry makes the terminal mean zero; independent Poisson increments give the covariance exp(-2|Lambda(t)-Lambda(s)|). Pushing forward normalized time under the continuous nondecreasing cumulative rate Lambda makes the normalized terminal variance exponential-kernel energy on [0,B]. An interior interval of length x requires time at least x/R by the Lipschitz bound; disjoint open intervals and measure regularity then prove the full measure floor c dx, c=1/(RT), including for protocols with flat segments or singular excess occupation. The probability measure mu_c=c dx+(1-cB)(delta_0+delta_B)/2 has potential c+[1-(1+B)c](exp(-2x)+exp(-2(B-x)))/2. At c0=1/(1+B) this is constant, so mu_c0 is optimal whenever feasible. For c>c0 its potential is minimized at both endpoints: the exponential sum is strictly convex and maximal there, and its coefficient is negative. Any competitor's excess over c dx is nonnegative and has fixed mass; its first variation relative to excess mass at the endpoints is therefore nonnegative. Strict positive definiteness (Fourier transform 4/(4+xi^2), with uniqueness of Fourier transforms of finite signed measures) gives strict improvement over every different measure. The centered pulse realizes the optimizer at density max(c,c0), with endpoint atoms given by equal idle times. Monotone continuous maps of normalized time are determined by their pushforward (the quantile function a.e.), so the rate is unique a.e. The constant-potential expansion eliminates the linear term; integrating the signed direction dx-B(delta_0+delta_B)/2 gives B-(1-exp(-2B))/2-B(1-exp(-2B))+B^2(1+exp(-2B))/2=K(B)>0. Consequently the value has the exact positive-part quadratic penalty and saturation at R=(1+B)/T. At R=B/T the constant rate is forced; at R=(1+B)/T the cap equals the pulse height without increasing the minimum. A fresh bounded check propagated m'=v-2 gamma m and V'=2v m via elementary segment antiderivatives, not the provided matrix-exponential script. At B=T=v=1, R=1,1.5,2,3 it gave 0.5676676416183064, 0.5075186268464785, 0.5, 0.5, agreeing with the formula. The supplied script was inspected, not run; neither finite check proves global optimality.

## originality

PASS

Best-of-knowledge pass for the exact lower-density obstacle solution and the resulting active finite-horizon rate-cap law. The exponential-kernel equilibrium without the obstacle, the endpoint atoms and the resulting large-cap branch are not counted as new capacitary theory. Separate literature comparisons did not establish coverage of the active floor, the resulting sharp threshold and the exact variance penalty; the closest primary full texts remained inaccessible after bounded attempts.

## value

PASS

For a natural finite observation window and independently meaningful total and instantaneous reversal constraints, the result gives the pulse to use, when a faster actuator stops helping, and the exact penalty when the cap binds. The endpoint objective produces a materially different design from long-time diffusivity, and the global measure argument rules out any advantage from irregular deterministic rates. The scope excludes feedback, traps and changing the count model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
