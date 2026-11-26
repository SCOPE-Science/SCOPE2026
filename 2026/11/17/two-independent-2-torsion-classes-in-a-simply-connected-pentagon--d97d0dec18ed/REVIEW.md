# Independent mathematical audit

## correctness

PASS

The labeled sphere-wedge theorem makes the source simply connected. Every reflection fixes the barycenter of the non-2-connected star at its fixed label; reflections generate D5, so Armstrong's theorem for the finite action kills the whole orbit-space fundamental group. The rational quotient chain complex is the coinvariant chain complex of the inverted-free barycentric action, and rational averaging is exact. Independent Euler characteristics of the geometric fixed sets are −5, 0, 3 for identity, nonidentity rotations and reflections, respectively. These equal the Lefschetz numbers (the sign on an invariant face with k edges and j edge orbits is (−1)^(k−j), so the signed contribution is (−1)^(j−1)). The degree-five character is 6, 1, −2, with average zero. For mod two, the original flag quotient has no inversions and each deletion has a distinct face-rank pattern, so the described deletion boundary computes ordinary orbit-space homology. An independent reproduction uses the 35 maximal graphs obtained from the possible separations off a cut vertex. Taking the intersection of all facets above a nonempty face is an equivariant ascending idempotent poset map, hence retracts the order complex up to equivariant homotopy and also retracts on quotients. Enumeration by stabilizers of ascending flag prefixes in the 560-element closed-face poset gives orbit counts (72,1195,6272,13656,13044,4536,0) and mod-two ranks (0,71,1124,5148,8508,4534,0), with all boundary squares zero. This independently recovers (1,0,0,0,2,2,0), using a different CW model. Replay: python3 /workspace/audit-evidence/pentagon.py. Facets have at most seven edges, so the full quotient has dimension six. In positive degrees the integral groups are finitely generated with zero free rank. If t_i counts 2-primary cyclic summands, then b_i over F2 equals t_i+t_(i−1) for i>0 with t_0=0. Thus t_4=2 and all other t_i=0, exactly the claimed subgroup killed by two. This does not determine the exponents or odd-primary summands.

## originality

PASS

Credit the labeled sphere wedge and character to Babson et al. The rational calculation is an application of that character and finite rational averaging, and simple connectivity follows from the standard orbit-space theorem and reflection stabilizers. The distinct result supported here is the exact mod-two homology of this nonfree geometric quotient and hence its precise degree-four two-rank; the sources inspected do not determine it.

## value

PASS

The full pentagonal symmetry is a natural nonfree action on a classical small labeled graph complex. Its ordinary quotient is simply connected and rationally acyclic, so the exact two-rank is an informative obstruction to contractibility invisible to the classical labeled and rational results. It supplies a precise modular benchmark for studying such symmetry quotients, not just a recomputation of the parent space or an Euler characteristic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
