# Independent mathematical audit

## correctness

PASS

Correctness PASS. With H=diag(-lambda,lambda), v2/v1=u0 exp(-2 gamma lambda t) except v1=0. The exact position generator is (beta lambda/(1+u²))[(u²-1)I + 2uJ] with J a skew quarter-turn; its radial logarithmic derivative is beta lambda (u²-1)/(1+u²). Exact integration gives exp(-beta lambda t)[(1+u0²)/(1+u0² exp(-4gamma lambda t))]^(beta/(2gamma)), hence a hyperbolic-cosine peak at t*=log|u0|/(2gamma lambda) when |u0|>1, gain ((|u0|+|u0|^-1)/2)^(beta/(2gamma)), and return at 2t*. Direction v1=0 instead makes X'=beta lambda X; the zero position and u0=0 boundaries are explicit. Haar RP1 initial acute angle uniform on [0,pi/2]; for gain >z, theta exceeds (pi-arcsin(z^-2gamma/beta))/2, giving exact arcsin/pi tail and p-moment threshold p<2gamma/beta. Independently checked radial identity, peak and random-tail quadrature for three parameter triples; all-parameter conclusion follows from integration.

## originality

PASS

Originality PASS (bounded literature). Gentlest-ascent search dynamics originate with E–Zhou (2011), and Shi et al. (2026) investigate general local high-index saddle stability; neither inspected result yields the balanced planar global basin, arbitrary transient peak, or Haar random-initialization distribution. Published related sharp angle thresholds concern fixed inexact projectors/momentum or different gradient algorithms; they do not imply this self-adjusting projective-slope ODE. The exact solvable-case restriction is openly credited.

## value

PASS

Value PASS. The exact basin and unbounded transient amplification reveal a genuine numerical stability risk that local asymptotic convergence conceals. A closed pulse, sharp misalignment law, and exact random-start moments clarify what uncontrolled initialization may cost despite almost-sure convergence; significant mathematically motivated boundary case of a standard saddle search method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
