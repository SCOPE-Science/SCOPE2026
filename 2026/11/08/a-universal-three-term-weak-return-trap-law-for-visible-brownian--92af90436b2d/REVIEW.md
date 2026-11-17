# Independent mathematical audit

## correctness

PASS

The actual protocol uses driftless search Brownian motion to L, reset clock R independent with E[R²]<∞ and P(R>0)>0, and a target-visible OU return that ends at 0 or L. Renewal gives Mκ=[E(T∧R)+E(1_{R<T}uκ(B_R))]/pκ. The negative-return OU hitting-time derivative is c_D κ^-1/2 erfcx(a sqrt(κ/(2D))), with a globally controlled cubic expansion; bounded-domain return solves regular perturbation equations. Stopped Brownian first and second moments give leading Lc_D/√κ and clock-independent constant L²/(2D). The stopped cubic martingale and E[B_t 1(T>t)]=-L P(T≤t) give E[(T∧R)-stopped B³]=-6DL H with H=E[(R-T)_+]; the sqrtκ coefficient is c_D[L³/(6D)+L H/p0] and strictly exceeds permanent OU. ER² controls fourth stopped moments and the O(κ) remainder. Poisson clocks give p0=(1-e^-2q)/(2q), H=e^-q/r and coefficient factor 1+6/(q sinh q). Independently checked erfcx Taylor derivatives and exponential identities (14 assertions). The theorem is pointwise for fixed clocks, no uniform r-limits or optimal resetting.

## originality

PASS

Best-knowledge assessment against mathematically matching and broader prior claims; explicit boundaries and uninspected-source risks retained. The exact cancellation of all clock dependence through the leading and constant MFPT terms, with a universal strictly positive first renewal-clock penalty at order sqrtκ, is a natural weak-trap singular-limit fact. It differentiates target-visible stochastic home-return protocols and is useful for cost comparisons.

## value

PASS

The exact cancellation of all clock dependence through the leading and constant MFPT terms, with a universal strictly positive first renewal-clock penalty at order sqrtκ, is a natural weak-trap singular-limit fact. It differentiates target-visible stochastic home-return protocols and is useful for cost comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
