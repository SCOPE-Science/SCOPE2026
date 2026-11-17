# Independent mathematical audit

## correctness

PASS

For component curvatures A=m(1±delta), B=m(1±delta), uniform marginals force P(--)=P(++)=(1−q)/2 and P(+-)=P(-+)=q/2. Scalar Heun multiplier 1−h(A+B)/2+h²AB/2 yields exactly M_q=R_cross²+(1−q)t²delta²[2(t−1)²+1]. Excess strictly positive for all t>0,delta>0; independence in time gives E X_k²=M_q^k X0². R_cross zero iff 1−delta² times t²−2t+2=0, discriminant 4(2delta²−1); positive roots exactly delta>=1/sqrt2. Fraction/symbolic independent algebra and rational witness checked. Does not claim any finite-step result for nonlinear or high-dimensional models.

## originality

PASS

PASS best of knowledge: This is a complete uniform-marginal coupling classification for a two-component positive-curvature scalar Heun predictor/corrector. Earlier antithetic averaged gradients at the same point lack the h²AB stage term; SRKCD uses a same-batch stage convention; bilinear extragradient and randomized time-stage Runge–Kutta concern different update maps. None of the actually inspected source statements implies its strict all-step antithetic optimum and exact one-update termination contrast frontier.

## value

PASS

PASS: The sharp contrast threshold delta=1/sqrt2 and exact rational example in which antithetic Heun terminates in one update while independent-stage sampling and even full-gradient Heun amplify constitute a motivated sharp boundary and mechanism for sample-coupling design. Limited to natural positive scalar finite-sum interpolating quadratics, but complete within that domain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
