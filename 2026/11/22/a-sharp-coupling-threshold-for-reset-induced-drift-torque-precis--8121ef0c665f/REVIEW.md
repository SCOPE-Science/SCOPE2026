# Independent mathematical audit

## correctness

PASS

Independently derive the fourth moment from the stationary exponential reset age s: conditional on s, U,V are centered Gaussian with variances S(1−exp(−2(1±u)s))/(1±u) and cross covariance H(1−exp(−2s)). Wick's identity and E exp(−λs)=r/(r+λ) give E(UV)=2H/(r+2) and E(U²V²)=8S²(r+2)/[(r+4)((r+2)²−4w)]+16H²/[(r+2)(r+4)]. Subtracting the square of the mean and normalizing verifies the CV formula. With z=r+2 and D=z²−4w, the sign of the derivative is that of 2+k(z²/D²)(z²−4wz−12w). The final polynomial factor is strictly increasing for z≥2; z²/D² is positive strictly decreasing. Their product increases strictly wherever the polynomial is negative, and once it is nonnegative the derivative sign is strictly positive. The sign at zero is the sign of k(1−5w)+2(1−w)², strictly decreasing in w with a unique zero in (1/5,1), equal to the stated w_c. This independently verifies all cases, including no positive critical point at equality and a unique global minimum above threshold. Applying the generator to the centered UV gives eigenvalue −(r+2), verifying the stationary autocovariance, and C(0⁺)=1+k/(1−w) diverges at fixed k while C(1) stays bounded. Independent bisection at k=4,u=0.8 gave r*=1.570592394486 and C(r*)=7.980004791317. Inspected the supplied symbolic/quadrature checker without executing it. These claims apply to the state observable only, for complete origin resets, unequal positive temperatures, and 0<|u|<1.

## originality

PASS

The reset generator, renewal age mixture and the mean of the drift term are established ingredients; the strongest inspected overlaps do not optimize the snapshot squared CV of that term. The sharp global regime switch and uniqueness claim go beyond those ingredients. This is a best-of-knowledge assessment, not a claim of priority over every resetting result.

## value

PASS

The physically specified finite conditional torque admits a well-posed precision comparison even when instantaneous white-noise-inclusive angular momentum does not. The result decides for all allowed temperatures and couplings when full resetting improves that precision, whether the optimum is interior, and why potential gain can be large near loss of confinement. It does not claim performance gains for integrated currents or thermodynamic efficiency.

The dated certificate retains the supplied scientific assessment, sources and limitations.
