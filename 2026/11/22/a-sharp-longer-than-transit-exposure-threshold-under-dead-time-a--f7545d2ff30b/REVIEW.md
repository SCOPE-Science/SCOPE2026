# Independent mathematical audit

## correctness

PASS

Conditional on the lattice phase, independent Gaussian measurements with known variance contribute q_E^2/(v/E+w) each for the sole depth parameter. Integrating over phase and tiling the line divides the convolution energy by E+H; the finite-support overlap has a plateau of height min(E,L)/E and two linear ramps of width min(E,L), giving the two frozen pieces with the advertised normalization L/v. Direct differentiation gives sign numerators P_1=3h−2hx−(1+3r+hr)x² and P_2=h+2x−3x²+r(2hx−3hx²+3x²−6x³), each strictly decreasing on its own interval. Both give Q=h(1−r)−(1+3r) at x=1; P_1 starts positive and P_2 tends to minus infinity, allowing exactly one global optimum, including at Q=0. With J=F(x)/[(x+h)(1+rx)], the logarithmic derivative equals F'/F−1/(x+h)−r/(1+rx), strictly increasing in h and strictly decreasing in r pointwise. This proves strict comparative statics across the branch join as well as within branches. Rationalizing the positive quadratic root gives the short-branch formula and the small-h behavior. For r>=1 the optimizer stays at most one; for 0<r<1 eventually it is on the longer branch, bounded above by the positive root of 1+2rx−3rx² because P_2=0 requires that expression positive. Dividing the stationarity equations by h now gives the claimed limiting roots, including the limit one at r=1. At r=0 the long branch is an exact quadratic and grows like sqrt(h/3). These claims concern conditional-on-known-phase depth information averaged over designs, not Fisher information in an observation model marginalizing unknown timing. Read VERIFICATION.md and CHECKER.py without executing the uploaded code.

## originality

PASS

The box overlap and the entire r=0 boundary case already have exact coverage in equivalent variables. The distinct supported contribution is the joint effect of positive dead time and a positive independent per-exposure flux-variance floor: the two-parameter classification, disappearance of the long-exposure regime for r>=1, and finite saturation as dead time increases. The checked prior passages do not supply this extension. No priority inference is based on same-day dates or differing instrumentation terminology.

## value

PASS

The positive independent variance term changes the exposure decision qualitatively: it can preclude exposures longer than the event at every dead time, and it bounds the optimal exposure as overhead grows. The exact classification resolves feasibility and equality, gives unique implementable optimizers, and separates two competing effects in a natural ideal model. This is useful as a baseline, not a prescription for correlated noise, imperfect ephemerides, or limb-darkened joint transit fitting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
