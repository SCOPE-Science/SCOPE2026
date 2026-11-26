# Independent mathematical audit

## correctness

PASS

For t>0 use x−z∈t∂f(z). At any differentiability point z of nonzero slope p, set x=z+(s+t)p; exact composition and the singleton ∂f(z) force the intermediate point to be z+sp. Inner-step optimality then gives p∈∂f(z+sp) for every s>0. Subgradient inequalities at two points on that ray show f is affine there; derivative monotonicity and local absolute continuity yield only a constant negative ray, a possible flat interval, and a constant positive ray, with missing rays allowed. This also handles nonattainment: the no-flat, one-signed case on the full line is affine. The outward hinge form gives clipped translations with total time s+t; affine functions give translations everywhere. For positive kink slopes the composite minus direct map is −min(sa,x−ta) on [ta,tb] and −min(tb+sa−x,t(b−a)) on [tb,tb+sa], and zero elsewhere. These formulas agree at tb and yield the sharp error there. Reflection handles both negative slopes and x=ta, and the zero-containing subgradient case is a minimizer hinge with zero error. Zero times and equal slopes give zero directly. Inspected the frozen supporting files; the loop count is (325)(16)(2)+(9)(6)(16)(7)+(3)(9)(3)=16,529, matching the reported count, not a new execution. Exact grid tests are only corroboration; the arbitrary finite convex proof is analytic.

## originality

PASS

Standard subdifferential resolvents, scalar piecewise proximal formulas, and one-homogeneous settings overlap in ingredients and special cases. The inspected sources do not supply the all-finite-scalar necessity or the explicit sharp two-time kink envelope.

## value

PASS

Gives a complete scalar classification at a natural boundary between an implicit time step and an exact flow, with no smoothness or attainment hypothesis, and a sharp input-uniform obstruction at the first nonminimizing kink. This identifies precisely when a nonlinear time discretization is exact, rather than only testing families of examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
