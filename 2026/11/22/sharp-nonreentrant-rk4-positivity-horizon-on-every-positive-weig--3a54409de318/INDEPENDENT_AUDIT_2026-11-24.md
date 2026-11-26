# Independent mathematical audit

## correctness

PASS

Bipartite conjugation turns Laplacian powers into weighted walk sums with the sign set by distance parity. Uniqueness of paths gives the distance-three coefficient and the positive distance-four entry. For distance two, the contribution of two stays alone gives a quadratic coefficient at least 2s²/3; its discriminant with the lower-order terms is strictly negative. For an edge, enumerate the one-edge walk with stays and the three possible backtracking families (across the edge, or via a neighbor on either side). In the weighted degree notation x,y,s=x+y, these give 3xy ≤ c ≤ 2s²−3xy and b ≥ s(c−xy). Thus c²/(c−xy) ≤ c+3xy/2 < 2s², which gives a strictly negative discriminant for g′ and hence a unique positive zero of g. The scalar RK4 sum-of-squares identity gives positive diagonals, entries beyond distance four are zero, and L annihilates the constant vector. This proves the inclusive minimum horizon and permanent failure past it, including trees with no three-edge path. Independently computing the matrix polynomial at the path threshold confirmed the (1,1,1) and (4,1,1) examples and the latter's cubic; (2,1,1) also gives a genuinely nonuniform path-controlled example, with all three edge polynomials positive at h=1/2. Replay: python3 /workspace/replay/checks.py 5. The frozen log is only a finite supplementary check.

## originality

PASS

The local formula and nonreentry mechanism for unit weights are already covered. The supported increment is the sharp all-step theorem including arbitrary heterogeneous symmetric conductances and the conductance-dependent edge bound, not the first identification of edges and three-edge paths. The best-of-knowledge comparison uses the matching catalog statements; unavailable full texts do not certify noncoverage.

## value

PASS

Heterogeneous conductances arise naturally in graph diffusion. An exact row-stochasticity horizon, expressed by finite local scalar tests and excluding any recovery of positivity, answers more than a sufficient initial step bound. The checked nonuniform paths demonstrate that the active obstruction can change with weights on fixed topology. The result makes no claim about internal stages, stability radii or cyclic weighted networks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
