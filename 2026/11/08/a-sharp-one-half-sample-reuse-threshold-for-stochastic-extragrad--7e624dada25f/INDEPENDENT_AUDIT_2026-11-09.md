# Independent mathematical audit

## correctness

PASS

Write z_(k+1)=((1-eta²A_kB_k)I-eta B_k J)z_k with J²=-I and J^T=-J. Orthogonality gives pathwise squared-norm multiplier 1+eta²(B²-2AB)+eta^4A²B²; iid pairs imply exact all-n expectation (1+eta²(m2-2c)+eta^4 d)^n. Because c>m2/2 implies d>=c²>0, strict contraction occurs iff 2c>m2 with 0<eta²<(2c-m2)/d, and all edge cases are handled. Under Bernoulli reuse rho, c=rho m2+(1-rho)mu² and d=rho m4+(1-rho)m2², giving a_rho=mu²+(2rho-1)(m2-mu²); every law with nonzero mean has a_rho>0 when rho>=1/2. For any rho<1/2 a rare positive two-point law makes m2/mu² large enough that a_rho<0 and all positive steps are unstable; perturbing the zero atom to a small strictly positive value preserves failure. Direct exact rational one-step/multistep enumeration independently confirmed representative formulas and the half-reuse example; universality follows algebraically, not from tests.

## originality

PASS

The exact scalar bilinear moment identity is elementary once the update is written, and same-sample stabilization versus independent divergence is established prior art. The substantive surviving original contribution is the sharp distribution-free rho=1/2 Bernoulli within-step reuse threshold for ALL scalar oracle laws with finite fourth moment, with strictly-positive rare two-point counterexamples and law-specific critical reuse. Prior published equally-likely two-component coupling phase theorems do not imply this rare-law universal quantifier. Primary Mishchenko and Chavdarova full paper material lacks the sharp rho threshold. Possible alternate correlated-oracle formulations remain an originality risk.

## value

PASS

It identifies the minimum fraction of costly reused stochastic oracle calls guaranteeing the *existence* of stable mean-square steps for all finite-fourth-moment scalar bilinear coefficient laws. The sharp half-fraction and strictly positive rare-event obstruction resolve a meaningful sampling-design robustness question beyond textbook deterministic extragradient algebra. It does not claim one universal stepsize or convergence on general matrix-valued games.

The dated certificate retains the supplied scientific assessment, sources and limitations.
