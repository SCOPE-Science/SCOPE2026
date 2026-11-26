# Independent mathematical audit

## correctness

PASS

Uniform positive damping gives a unique stationary solution by the backward stochastic convolution and contraction with a shared switching chain. Given the chain history its coordinates are independent centered Gaussians with variances A and B, satisfying A'=2D-2(k+aS)A and B'=2D-2(k-aS)B. Sign and exchange symmetry give the claimed second-order isotropy. Put L=A+B, J=A-B, and m=E A=E B. The first moment balances give E(SJ)=-2am/(k+sigma) and m=D(k+sigma)/T. From (AB)'=2DL-4kAB one gets E AB=Dm/k, hence the stated negative covariance E AB-m^2. The stationary J^2 and L^2 balances give E(SLJ)=-k E(J^2)/a and E L^2=4Dm/k+E J^2. Substituting these into the SLJ balance, including its -2 sigma switching term, gives E J^2=4D^2 a^2(2k+sigma)/(kUT). Conditional Gaussian fourth moments give H_4=3 E J^2, with the specified R^4 weight, not an unweighted angular average. Both expressions are nonzero. The derivative of the covariance is positive since 2k(k+sigma)-T>0, and the log derivative of H_4 is negative because U<k(2k+sigma) and T>0. The fast-switching coefficients, and the two one-sided slow-switching limits, follow directly from the rational functions. At zero switching the switching state no longer has a unique stationary law.

## originality

FAIL

The opposite-stiffness effect is not contained in the cited scalar common-variance model. Nevertheless, the earlier published multivariate Markov-modulated OU theorem supplies an explicit inverse-matrix formula for the exact mixed moments of this same model class. In this specialization only its (2,0), (0,2), (2,2), (4,0), and (0,4) recurrences are needed; the projection and factorization below give the entire frozen package by two-state matrix inversion, subtraction, and differentiation, without an extra probabilistic or asymptotic result. The distinct later indexed counter-switching theorem additionally gives the exact negative covariance by direct substitution. That later index date is not used to establish earlier priority.

## value

PASS

The measurable distinction between equal covariance in every direction and a positive radius-weighted angular harmonic is physically motivated. The negative energy covariance gives an opposite sign to the all-axes common scalar switch, and rate attenuation describes how the effect can become hidden. This is informative as a diagnostic even though the exact formulas are covered as a scientific contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
