# Independent mathematical audit

## correctness

PASS

For the exact iid inverse-normal multiplier, Gaussian convolution of log|x| has H'(t)=w(t), w'=1-tw. The crossing g=tw=1 is unique: g(0)=0, w~1/t, and at every crossing g'=1/t>0; if no crossing w would stay nondecreasing against w→0. Therefore F_a(s)=log s+H(a/s) has unique strict minimum at s=a/t*, with minimum log(a/a*). Independent high-precision Dawson evaluation gave t*=1.3069297277192810 and a*=1.2780775875261037, and correctly signed minima at a=1.1,1.2,1.4. Endpoints F_a(0+)=log a>0 and F_a(infinity)=infinity yield the two-boundary classification. Strong law controls nonzero Lyapunov exponents; law of iterated logarithm controls mean-zero boundaries. A positive normal density at the denominator pole forces E|U_j|^p=infinity for p>=1; log-MGF derivative and Jensen prove the p in (0,1) equivalence.

## originality

PASS

General iid-product Lyapunov stability is classical, as are Gaussian logarithmic potentials and inverse-normal moments. Bosch studies probabilistic ODE filters with stochastic covariance, not iid Gaussian drift coefficients inside implicit inverses. Bochacik–Przybyłowicz treats random-time Euler with exact information in its stability section; Higham–Mao–Yuan treats Itô SDE forcing with deterministic implicit drift denominator. The universal random-denominator two-root phase and quantified a* remain unmatched by inspected literature and Resultary. No claim of new SLLN or Dawson functions.

## value

PASS

The analytically sharp reentrant intermediate-noise instability while all absolute moments >=1 are divergent is a meaningful operator-error stability benchmark distinct from Itô forcing; its closed universal threshold helps distinguish almost-sure stability from moment stability rather than trivial numerical sampling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
