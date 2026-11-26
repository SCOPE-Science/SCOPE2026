# Independent mathematical audit

## correctness

PASS

The original conclusions are correct, but the supporting-line argument at t=m asserted a false unique contact: H_m is zero throughout [0,m]. The complete corrected RESULT.md in /workspace/repairs/4/ proves the boundary case separately. Independent reconstruction: the signed Bessel radial coordinate |X|^k/(sqrt(2) k), k=(alpha+2)/2, has dimension 2-1/k=2-2 mu, giving the known last-zero Beta(mu,1-mu) free law. Conditional on touching zero between the two observation times, the product of signs has zero expectation by the strong Markov property and symmetry; without a zero it is one. A reset likewise destroys sign correlation. In equilibrium, the unnormalized measure of elapsed age a in a cycle remaining free of resets through t is P(W>a+t) da/m, also for atomic clocks by length bias and the uniform position within the covering cycle. Combining gives the exact incomplete-beta integral, or E[H_t(W)]/m. For w>t, H_t'(w)=I_(1-t/w) increases strictly while for w<=t the function is zero. When t<m, the tangent at m lies strictly below the graph at every other w, including w<=t because H_t(m)<(m-t)H'_t(m); Jensen is strict for a nonconstant clock. At t=m a nonconstant positive W of mean m necessarily has mass above m, on which H_m>0, proving strictness despite the entire contact segment. For t>m there may be equality, e.g. W<=t almost surely. The variance is (1/(2T^2)) integral_0^T (T-t) C_W(t) dt, because the indicator covariance is C_W/4; strict comparison holds at each positive horizon by integrating over 0<t<min(m,T). For the mass, substituting u=a+t and v=a/u inside one reset interval w gives Jacobian u and integral (w^2/2) E[1-B] with B~Beta(mu,1-mu); Tonelli includes infinite second moments. This implies the stated finite-moment variance coefficient. For the heavy tail, scale a=tx; the tail equivalence at t(1+x) holds with uniform relative error over x>=0 as t increases. Interchange the Beta probability and the x integral to obtain E[(1-B)^(beta-1)]/(beta-1), evaluating to the displayed Q. Rescaling the variance integral at 1<beta<2 gives the factors (2-beta)(3-beta) by integration of (1-s)s^(1-beta). At beta=2, Q=1-mu, integral_0^T C_W(t)dt~c(1-mu)log(T)/m and integral_0^T tC_W(t)dt=O(T), giving the logarithmic coefficient. The Poisson case also checks independently: the correlation is E exp(-rt/(1-B)); after differentiating with respect to rt and using z=B/(1-B), its derivative is -exp(-rt)(rt)^(-mu)/Gamma(1-mu), the Gamma survival derivative with the correct boundary. No claim of a CLT is made from variance alone.

## originality

PASS

Pass the sharp fixed-mean all-lag sign decorrelation and model-specific exact occupation variance constants, including the critical logarithmic term. The prior comparison in the corrected result now gives explicit credit for substantial structural coverage: the Beta last-zero law is prior, general complete renewal resetting already gives the underlying correlation formula, and equilibrium alternating renewal signals already exhibit related anomalous occupation variances. Neither the generic formula alone nor the inspected specialization/other model covers the full sharp optimum and constants for the specified diffusion. Pass the supported distinction, not standalone originality for renewal averaging, the Poisson reduction, or the anomalous power law as a phenomenon.

## value

PASS

The sign observable gives a unit-free measure of memory and a directly linked cumulative occupation noise. Comparing clocks of the same mean removes mere rate tuning. A single deterministic clock attaining every lag minimum (and every finite-window variance minimum), together with exact dependence on the reset tail and a logarithmic boundary, is a useful sharp benchmark, not merely an evaluation of the prior free Beta law or a generic renewal correlation formula. The proof resolves genuine equality and moment-regime boundaries and specifies the effect of long externally reset cycles that may themselves contain sign changes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
