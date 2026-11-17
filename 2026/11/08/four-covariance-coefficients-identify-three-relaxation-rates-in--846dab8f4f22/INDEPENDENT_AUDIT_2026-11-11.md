# Independent mathematical audit

## correctness

PASS

For joint position-orientation Poisson reset at r, harmonic beta, angular diffusion d, fixed known v,D>0, generator moment identities give q=2d/(r+4d), h=vq/(beta+d+r), V=(2D+2vh)/(2beta+r). Stationary transverse lag covariance solves C' =-(r+beta)C+vH and H'=-(r+d)H. Universal stationary right slope c1=-D-rV/2 determines r. If Delta=c0c2-c1^2!=0, a two-exponential/degenerate-Prony ODE and c0..c3 recover the two unordered rates r+beta and r+d, while strict inequality in the calibrated variance under swapping beta and d resolves their assignment. Repeated rates beta=d give a t exp term and Delta=-(vh)^2<0. If Delta=0 the nonzero h forces cancellation of the beta pole, yielding visible r+d; beta is the unique root >d of (beta-d)(beta+d+r)=2v^2d/[V(r+4d)]. All rates positive, all degenerate cases handled. Rational cancellation (r,beta,d,v,D)=(1,3,1,5,3/2) yields C(t)=exp(-2t), recovered uniquely. This is exact structural identifiability, not numerically stable estimation.

## originality

PASS

Best-of-knowledge originality follows from statement-level and implication-level comparisons; no identified complete earlier theorem covers the stated surviving exact result. See structured checks, inspected source material and risks.

## value

PASS

A complete parameter-identifiability theorem from only the first four right derivatives of a single stationary positional observable, especially the otherwise-hidden exponential cancellation case, fills a meaningful inverse problem in active-reset stochastic dynamics. Explicit identifiability domains and exceptional algebraic cases are useful to future inference theory; instability in finite/noisy samples is explicitly outside scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
