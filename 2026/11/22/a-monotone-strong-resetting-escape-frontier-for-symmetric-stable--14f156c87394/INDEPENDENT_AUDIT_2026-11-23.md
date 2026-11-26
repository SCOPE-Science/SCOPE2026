# Independent mathematical audit

## correctness

PASS

For a fixed interior x, integrate the stable Lévy density over both exit tails to obtain lambda_x=(c_alpha sigma^alpha/alpha)[(L-x)^(-alpha)+(L+x)^(-alpha)], with c_alpha=Gamma(1+alpha)sin(pi alpha/2)/pi by reflection and duplication. The unconditioned exit asymptotic P_x(tau<=t)~lambda_x t is directly stated with this coefficient by Żbik–Palmowski Sec. III.A Eq. (5) and surrounding text; the Figueroa–López–Tankov Theorem 2.1 cited as provenance is instead a conditional Lévy-bridge theorem and is not the direct unconditioned statement. Independently, fix a positive boundary margin delta smaller than both initial distances and split off jumps above h<delta/4 in absolute value. Their process is compound Poisson; two such jumps by t have probability O(t^2). For the bounded-jump symmetric remainder, its exponential martingale has log compensator bounded by const*t*theta^2*exp(theta*h) at time t (finite truncated second moment). With theta=log(1/t)/(2h), Doob's bound makes an excursion of the remainder outside [-delta,delta] by t have probability o(t), using both signs. Squeezing exit by the one-jump events with thresholds shifted by plus or minus delta and letting delta down to zero proves the short-time coefficient, including possible boundary hits. Integrating the exit CDF against r e^(-rt) gives q(r)~lambda_x/r, and the expected duration of one attempt is (1-q)/r with success probability q. The renewable mean is (1-q)/(r q) and converges to 1/lambda_x. Żbik–Dybiec Eq. (2) with Eq. (7)'s sigma^alpha normalization verifies the unreset denominator. Cancellation of scale and the two reciprocal tails yield C_alpha/cosh(alpha artanh v); the denominator runs strictly from 1 to infinity, so one threshold exists and strict inequalities persist for sufficiently large finite r (no sign claimed at equality). For t=pi alpha/2 and h=log(t/sin t), Euler's sine product gives h/t^2 as a convergent sum of strictly increasing positive terms via -log(1-u)/u. Hence h also increases. With z=arcosh(e^h), the derivative of z/sqrt(log cosh z) has the sign of 2 log cosh z-z tanh z, positive since its derivative is tanh z-z sech^2 z>0. The product of increasing positive factors gives strict ordering of the frontier throughout (0,2). Expanding t/sin t=1+t^2/6+O(t^4) gives the small-index value; alpha=1 gives sqrt(1-4/pi^2). With epsilon=2-alpha, arcosh C_alpha=log(4/epsilon)+o(1) and (2/alpha-1)log(4/epsilon)=o(1), so 1-v_c~epsilon/2. Independent quadrature of the two jump tails at nonunit L and sigma, plus endpoint checks, can be replayed with python3 /tmp/opencode/stable-frontier-replay.py; it reproduces 0.7711778429329054 at alpha=1 and the limiting 0.719640870292547089, with the upper-end slope tending to 0.5. The deposited 6,359 checks are finite consistency checks, not an exit-process simulation or a proof.

## originality

PASS

The earlier stable-flight strong-reset and free means (and even their direct comparison) are not novel. Their equations imply the pointwise ratio, explicit threshold formula and strict finite-high-rate corollary after elementary algebra; the supported increment is the strict all-index order of this threshold, its sharp endpoint laws and distinction from the weak-rate crossover, not the limiting mean or the existence of helpful fast resetting.

## value

PASS

The strict stability-index ordering and sharp singular endpoint constants give an interpretable comparative design rule from two known asymptotic means, clarifying how close to a boundary the start must be for fast resets to help. This is an all-index analytic result, not a replot or isolated numerical example. Its value is limited to sufficiently high Poisson rates at fixed interior starting conditions. It does not determine intermediate-rate optima or either-sided finite-rate behavior at the critical equality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
