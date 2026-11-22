# Independent mathematical audit

## correctness

PASS

Reconstructed the invariant one-time marginal from the linear Volterra marginal equation and the equilibrium initial law, hence E[f]=0 and E[f^2]=v. For J_t=int_0^t f(X_s)ds, the continuous additive functional and jump/Dynkin product rule give S'=2C and C'=v-(lambda+r)C+(r/t)S, with S=E[J^2], C=E[Jf(X_t)]; no stationarity of full paths was assumed. The resulting singular ODE S''+(lambda+r)S'-(2r/t)S=2v has regular solution S=vt^2 sum_{n>=0} [(2-p)_n/((2)_n(3)_n)]*(-at)^n; coefficient recurrence and initial normalization checked. Beta(2-p,1+p) has moments (2-p)_n/(3)_n and positive shapes for all finite r>=0, lambda>0; this proves the exact Beta formula. Inverse moment E[1/B]=2/(1-p) for p<1, Beta(1,2) endpoint log at p=1, and the Mellin endpoint integral Gamma(2-p)/(p-1) for 1<p<2 give all three sharp coefficients and powers. Five independent 40-digit quadratures matched the prior Kummer forms, including r=0 and critical p=1; reconstructed Git tree from the seven independently read Git blob identities exactly equals assigned SHA 12775a68344d961ec110ed1644b896137fbbb20e. The analytic argument, not these finite checks, proves all times and long-time limits. The statement explicitly assumes valid integrability and Dynkin product identities, excluding pathological generator domains.

## originality

FAIL

The exact three-regime time-average variance, complete finite-time Kummer representation, sharp constants, and threshold were already established in the 2026-10-26 result and repeated twice on 2026-11-02 for this identical uniform-history relocation process. The present Beta(2-p,1+p) mixture is algebraically equal to their Kummer expression for p != 1 and has the same critical continuation. The only new quantifiers replace the OU coordinate by a real generator eigenobservable and OU eigenvalue mu by lambda. The earlier proofs use just the invariant second moment and the eigenfunction identity Lx=-mu*x in the same jump-product calculation; replacing that line by Lf=-lambda*f yields literally the same closed ODE. Prior OU theorem statements alone do not logically prove every general-diffusion instance, but this extension is an immediate standard generator substitution of the published proof with no distinct new nonstandard lemma, coefficient, phase, or construction. Thus the claim is not a substantively original scientific finding.

## value

FAIL

The equilibrium-with-anomalous-averaging phenomenon, exact finite-time variance and all three sharp phase laws already appear in the earlier 2026-10-26 and 2026-11-02 published OU works. Although spectral generalization to arbitrary real eigenobservables is a natural framing, the submitted final formula is obtained from the published two-moment proof by the sole replacement Lx=-mu*x to Lf=-lambda*f; the assumed Dynkin identities do the remaining work. No new nontrivial structural lemma, new example with different qualitative behavior, composite spectrum, or independent invariant is established. The Beta representation is a standard transform of the prior Kummer formula. This narrow routine generalization lacks a substantively new mathematical result under the same value bar, irrespective of its correctness and reproducibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
