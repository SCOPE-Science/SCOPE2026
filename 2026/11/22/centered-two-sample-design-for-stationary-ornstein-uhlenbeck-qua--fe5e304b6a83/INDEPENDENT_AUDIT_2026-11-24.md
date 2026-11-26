# Independent mathematical audit

## correctness

PASS

Gaussian conditioning followed by whitening gives a quadratic form in two independent standard normals plus a constant. Wick's identity gives the claimed explained variance and the dimensionless change of variable contributes exactly lambda^(-2). An independent way to check the margin identity is to start from the whole-line whitened Gram matrix and subtract the two tails. These are z/2 and v/2 times rank-one projections onto K^(1/2)e_1 and K^(1/2)e_2, respectively. The vectors have norm one, inner product r, and whole-line Gram quadratic form one in both directions. Squaring and taking the trace gives the stated margin penalty; at fixed gap only U=z+v matters and minimizing it strictly favors equal margins. In the centered eigenbasis the collision score is (1-exp(-L))^2 with the same strictly positive right derivative; at the endpoint both eigenvalue derivatives are strictly negative (the weaker sign uses sinh L>L) and both eigenvalues are positive. Thus every optimum is strictly interior. For the limiting log-concavity certificate the hyperbolic numerator reduces to (cosh(4d)-1)/8+2d sinh(2d)-d^2 cosh(2d)-2(cosh(2d)-1); its Taylor expansion gives the displayed coefficients, starting positive at n=2 with strictly increasing bracket. The positive excess above 2 therefore has strictly concave log and tends to zero at either end of its positive interval. A fixed competitor with limiting score above 2 rules out subsequences of finite-horizon maximizing gaps tending to zero or infinity; along any remaining convergent subsequence the boundary correction vanishes. The limiting maximizer is unique, not claimed unique at finite L. Independent bisection of 1/d+h'(d)/h(d)-2/(1-exp(-2d)) on [2.4,2.8] gives 2.5549289500952668 and limiting score 2.0181855560856614 in double precision. This corroborates, but does not certify all digits of, the quoted decimal.

## originality

PASS

Best of current knowledge: the distinct result is exact centering/interiority and the limiting separation for the stationary exponential kernel and the integrated-square conditional-variance objective. The Gaussian quadratic-form identity and related designs in other sampling models are not novel parts of the claim.

## value

PASS

The nonlinear integrated energy is a natural measurement target. A global reduction from unconstrained two-site placement to one scalar gap is useful independently of the long-horizon theorem; the latter shows that optimal sites keep a finite separation in correlation-length units even on arbitrarily long intervals, and quantifies the absolute risk reduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
