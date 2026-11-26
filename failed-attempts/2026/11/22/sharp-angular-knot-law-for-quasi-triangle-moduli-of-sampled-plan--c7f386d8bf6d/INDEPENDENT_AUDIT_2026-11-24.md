# Independent mathematical audit

## correctness

PASS

On each quadrant cone the l1 norm and the interpolant are linear, so the nodal bounds l1<=Q<=M l1, M=max_r q_p(r)/l1(r), propagate by nonnegative interpolation. The l1 triangle inequality gives C<=M. If any nonaxis knot is present, its ratio exceeds one; a maximizing ray then has both coordinates nonzero, so splitting it into its coordinate vectors gives exact equality. In the axis-only case the source's splitting witness uses a zero vector, outside the displayed supremum, but Q=l1 and x=y=(1,0) gives an admissible equality witness. Folding the nodal direction into [0,pi/4], the normalized absolute coordinate sizes are (1+tan(delta))/2 and (1-tan(delta))/2. Strict concavity of t^p proves strict decrease away from the diagonal, and the even binomial expansion gives F_p=2^(1/p-1)[1+(p-1)delta^2/2+O_p(delta^4)] at fixed p. This checks the endpoints, exact condition and asymptotic for all stipulated fans. Replay: RESULT.md, Steps 1–4, with the separate nonzero axis-only witness above. The frozen CHECK.py was read, not run; its sampled fans repeat their knots by quarter-turn and finite tests cannot establish the nonuniform continuum claim.

## originality

FAIL

The earlier octagonal record proves the exact maximal convexification-distortion formula for any positive absolutely homogeneous planar gauge, not only for its eight rays. Combined with the existing conic interpolation construction, the present exact constant is a direct specialization: the convexified unit ball here is the l1 diamond (all four vertices are present and the unit ball lies in it), and each fan sector cuts that diamond in a triangle with its nonzero vertices on the knot rays. A linear function on each triangle has its maximum at a knot vertex. This mechanically gives the nodal ratio formula on every permitted fan. Folding and an even Taylor expansion of the explicit l_p profile give the angular statements without a further extremal theorem. Not a failure based on a self-match or an empty search.

## value

FAIL

The exact modulus is a sensible mesh-design invariant, but here it is mechanically obtained from an earlier exact planar theorem by identifying the l1 diamond and evaluating a piecewise-linear maximum at its knots. The angular Taylor coefficient evaluates the same elementary profile and does not leave a separately useful unknown exact assertion under the stated acceptance standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
