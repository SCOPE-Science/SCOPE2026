# Independent mathematical audit

## correctness

PASS

The displayed convex combination at t=max x_i lies in the two specified cube faces, and the endpoint cases t=0 and 1 lie in the corresponding faces. This is an exact hull description because both faces lie in the polytope. Their support maximum yields E h(G)=(d mu+E|D|)/2, since the positive and reflected negative parts from the two levels are independent. Gaussian radius is independent of the direction, with the stated expectation, so spherical full mean width is 2 E h(G)/c_d, not the unnormalized Gaussian width. The first-moment Fourier integral follows from the characteristic function of D; its integrand has a finite limit at 0 and is O(t^(-2)) at infinity. For fixed d, moving one element from q to p for p>=q>=2 compares the absolute values S0+T+Y and S0+T−Y with S0 symmetric, T nonnegative and positive with positive probability. The difference averaged over Y is an odd strictly increasing function of S0+T: for nonnegative s it is 2 E min(s,Y), strictly increasing because Y has a positive upper tail at every finite s. Thus every permitted outward transfer is strict; the two middle configurations at odd d are swaps, and d=2,3 have no distinct imbalance classes. The centered signed sum satisfies Lyapunov since the sum of third moments divided by (dv)^(3/2) is O(d^(-1/2)); bounded second moments give first-moment convergence in the critical window. Folded-normal integration and differentiation give the displayed profile, value at zero and strict convexity; the L² limit of D/d gives the macroscopic result even at s=0 or 1. Independent checks covered 474 vertex support computations, the planar width 1.08677793045 equal to (2+sqrt(2))/pi, and 49 strict comparisons through d=16. The sampled critical widths corroborate but do not prove the limit.

## originality

FAIL

Two distinct indexed findings together cover the claims. The affine map (x,y)→(x,1−y) has orthogonal linear part and maps this order polytope exactly onto the ordinary chain polytope, the stable-set polytope of K_{p,q}. Thus the different polytope name does not separate the width claims. Resultary 47503e85bfda gives the exact directional-width formula and a stronger joint distributional critical-window limit for that body. The fixed-dimension strict law is covered independently by the explicit strict transfer lemma in 34f994ef99fd with C=0; although its multiblock Finding emphasizes r>=3, the proof explicitly includes the no-other-blocks case. The catalogue dates are later path dates; this establishes mathematical coverage, not first-discovery priority or dependence.

## value

FAIL

This is a natural geometric family and the balanced extremizers and critical correction would be useful mathematical facts. As a distinct finding in the presence of the verified comparisons, the exact mean and both limits are consequences for the very same isometric body, and the strict balancing remainder is already a proved transfer case. The moved-coordinate derivation and numerical integral are useful expositions but not a distinct valuable claim to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
