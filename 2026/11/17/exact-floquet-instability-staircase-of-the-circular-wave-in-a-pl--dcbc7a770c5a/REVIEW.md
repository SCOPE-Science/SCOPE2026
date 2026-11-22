# Independent mathematical audit

## correctness

PASS

Recomputed the rotating-frame equation xdot=-beta(y-y_lag), ydot=beta(x-x_lag)+2(alpha-beta)x and F(lambda,k)=lambda²+beta²(1-exp(-lambda))²+beta*k*(1-exp(-lambda)). The lambda=0 root is simple for k>0 with derivative beta*k. At k=0, each factor lambda±i beta(1-e^-lambda) has no nonzero closed-right-half-plane root for beta<pi/2: imaginary crossing requires odd pi=2beta and no roots can arrive from infinity since |lambda|<=2beta; for small beta the integral h(lambda)=lambda int_0^1 e^-s lambda ds excludes them, and continuity completes the full beta interval. For k>0 the imaginary part at i omega equals beta sin omega[2beta(1-cos omega)+k], so nonzero imaginary roots require odd omega=(2j+1)pi and then k=((2j+1)^2 pi²-4beta²)/(2beta). Direct F_lambda at crossing = -((omega²+4beta²)/2)+2i omega; d lambda/d alpha has strictly positive real part. Right-half-plane roots obey |lambda|²<=4beta²+2beta*k and cannot appear from infinity on bounded k intervals; hence exact root count. The RFDE linearization principle gives attraction modulo S1, and positive eigenvalues instability, not Hopf branch type. Independent direct determinant and derivative substitutions tested beta pi/6, pi/3,1.3 with j=0..3; source script read, its finite Newton continuations are not proof.

## originality

PASS

Best-of-knowledge originality; four explicit comparisons and actual primary-source material inspections below. Existence of the circular orbit and of separately certified noncircular orbits does not imply its transverse spectral root count. Root identities and crossing direction are an additional result, although Hara 1997 full text remains inaccessible.

## value

PASS

The original nonlinear delay equation has a distinguished natural periodic orbit whose stability threshold was expressly left open in the 2026 primary study. An exact first threshold, all higher crossings, algebraic multiplicities and unbounded unstable dimension staircase settle a motivated stability question in the same infinite-dimensional model; no unsupported claim about global attraction or secondary periodic solutions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
