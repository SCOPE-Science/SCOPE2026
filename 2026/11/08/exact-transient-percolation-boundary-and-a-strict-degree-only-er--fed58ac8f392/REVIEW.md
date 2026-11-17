# Independent mathematical audit

## correctness

PASS

Poisson splitting shows independent vertex ages X_i=min(E_i,u), E_i~Exp(1), with atom e^{-u} at u, and conditionally independent pair edges of probability 1-exp(-c min(X_i,X_j)/(N-1)). BJR bounded irreducible inhomogeneous random graph theorem hence gives giant threshold c=1/||K_u|| at fixed u>0 including zero giant fraction at equality. For g(x)=K1=1-e^{-x}, moments m1=(1-e^{-2u})/2, m2=(1-3e^{-2u}+2e^{-3u})/3 reproduce Artime’s degree-only line m1/m2. K_u is compact injective positive-semidefinite since min(x,y)=integral indicators; strict m2<lambda*m1 follows from K1 nonconstant, giving exact c*<c_degree for EVERY u>0. Differentiation yields lambda f''= -e^{-x} f, f(0)=0, lambda f'(u)=e^{-u}f(u); the endpoint atom is essential. Common-space kernel monotonicity and HS convergence give c*(u) strictly decreasing, c*(u)~1/u near0 and limit j_0,1^2/4. Independent low-order quadrature checked u=.5,1,2 and strict comparison; 80-point quadrature at u=6 is insufficient for 6-decimal accuracy, so the stationary figure is justified analytically by Bessel, not by that finite grid.

## originality

PASS

PASS: The published degree-only transient line is strictly incorrect for the precisely defined resetting process; BJR general criterion and its stationary Turova Bessel example are credited. New finite-u age law (including endpoint atom), Robin eigenboundary and all-time strict discrepancy are not given by either inspected earlier statement.

## value

PASS

The exact positive-time phase boundary corrects a published macroscopic phase classification, showing a nonempty false-negative giant-component regime for EVERY u>0. The correct endpoint atom creates a nonstandard Robin boundary, and a strict all-parameter spectral inequality quantifies the error; this is not a routine application producing only a known limiting constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
