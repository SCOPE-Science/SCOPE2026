# Independent mathematical audit

## correctness

PASS

Complete resetting makes excursions regenerative, so M'(0)=m^2-s/2. At a=0 the absorbing/reflected boundary conditions give the two stated passive moments, and the discriminant s-2m^2 has its unique interior zero c=1-1/sqrt(5) with slope -2sqrt(5)/15. At first order the joint generator sends the linear OU mode y to -eta*y. The linear coefficients solve (-d_x^2+eta)u=m_0' and (-d_x^2+eta)v=s_0'+2u with Dirichlet-Neumann conditions; thus differentiating the discriminant gives y(v-4m_0u) and the claimed implicit-root susceptibility. The moment expansion can be justified locally: for the passive path the drift likelihood is exp(zA_t-z^2 B_t/2), B_t=(1/2) integral_0^t Y_s^2 ds, and A_t conditional on Y is centered Gaussian with variance B_t. Its complex second absolute moment is E exp(|z|^2 B_t). Testing the OU generator on exp(b y^2) bounds this by a compact-in-y constant times exp(2 eta b t) for small |z| and b=O_eta(|z|^2). Cauchy-Schwarz with the passive killed survival gap gives exponentially integrable survival expansions with the first two moment weights. Interior elliptic estimates on the backward equations give local mixed spatial/parameter regularity and hence the simple-root implicit function theorem. The zero-eta polynomial inverses give 4/125. At the interior point c the first resolvent terms are m_0'(c)/eta and s_0'(c)/eta, the iterated resolvent is O(eta^-2), and the bracket equals the passive discriminant slope divided by eta; this yields -1/eta. An independent polynomial Neumann-series replay with a uniform tail bound brackets a sign-changing zero between 0.21122136935 and 0.21122136945, without asserting uniqueness.

## originality

FAIL

The main theorem is covered exactly, and for a larger set of deterministic reset velocities, by the distinct indexed Resultary record 845ad3bf89f1. This is a conclusion about mathematical equivalence and lack of a distinct claim, not a finding of earlier publication, derivation, or misconduct. The additional elementary expression for one resolvent in the frozen record follows by integrating against the same Green kernel and does not yield a separate substantive result. In contrast, the motivating primary paper analytically treats Gaussian-averaged resets and probes the deterministic slope with numerical fits only.

## value

PASS

The exact sign reversal is a substantive structural answer to the motivating physical question: the same outward reset orientation can enlarge or shrink the region in which small-rate resetting helps. The two persistence limits and explicit intermediate response explain more than the numerical phase-boundary examples and give a testable local prediction. This assesses mathematical interest of the described phenomenon, not incremental contribution over the exact matching indexed theorem; there is no substantive repair on the remaining elementary-resolvent detail alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
