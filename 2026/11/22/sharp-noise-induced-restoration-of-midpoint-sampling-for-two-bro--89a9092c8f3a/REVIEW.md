# Independent mathematical audit

## correctness

PASS

The bridge Green equations −g''=1 and −g''=2t−1, with zero endpoint values, give the two observation covariances u/2 and u(2t−1)/6 for u=t(1−t). Integrating against their target weights gives prior variances 1/12 and 1/180, hence normalized loss uses w=15. Gaussian conditioning gives the reduction F=u²(9+w−4wu)/[36(u+η)], with zero at deterministic endpoints. The derivative for u>0 has the sign of P=2η(9+w)+(9+w−12wη)u−8wu². For η>0 the roots have opposite signs, and for η=0 the factorization u(9+w−8wu) gives the same sign change on the positive axis. Hence the unique maximizing u is the positive root clipped at 1/4. The sign of P(1/4)=[9−w+4η(18−w)]/4 gives the full boundary and uniqueness at equality; a smaller positive u corresponds to exactly two reflected sites. The derivative of w_c is 36/(1+4η)², with endpoints 9 and limiting 18. At w=15 one obtains u_*=1/5 with no noise and the transition at η=1/2. There P_u=−126 and P_η=3, giving 1/4−u_*=(1/2−η)/42+O((1/2−η)²). Since 1/4−u=(t−1/2)², this gives the claimed displacement. The general w-boundary expansion follows from P_u=−18(1+12η) and P_w=−(1+4η)/4.

## originality

PASS

The inspected work supplies conditioning, polynomial coordinates, or related but different designs. It does not give or imply the complete global one-point phase boundary and boundary layer for these two jointly estimated moments. The exact-index match is the frozen record itself.

## value

PASS

The loss compares the ordinary bridge integral with the natural first antisymmetric polynomial moment on equal relative scales, so concentrating on the midpoint can discard information about an entire target. The exact threshold shows when the noise cost of moving away overwhelms that second gain. The arbitrary-weight phase diagram, global uniqueness counts and square-root coalescence give precise design information beyond a local instability calculation or a generic Gaussian conditioning identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
