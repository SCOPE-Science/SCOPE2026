# Independent mathematical audit

## correctness

PASS

For intersecting targets {a,b} and {a,c}, an external distinguishing edge must contain one of b,c and exit {a,b,c}. For disjoint targets with union X, an external edge distinguishes exactly when it crosses the four-set cut: edges internal to X other than the targets meet each target once. These criteria are necessary and sufficient. The triple criterion rules out two isolates and a two-vertex tree component. In a larger tree, either there is a leaf at a degree-two neighbor, or every leaf attaches to a vertex of degree at least three. In the latter case the degree sum gives more leaves than degree-at-least-three vertices and hence sibling leaves. Both possibilities violate the triple criterion. Thus all nonisolated components have at least as many edges as vertices, giving the n−1 lower bound. Equality forces one isolate and no leaves, since a leaf, its neighbor, and the isolate violate the triple criterion. The edge count now makes every nonisolated vertex degree two; a triangle violates the triple criterion and a four-cycle violates the cut criterion. Conversely, two degree-two vertices having all their neighbors in a three-set would form a triangle there (and an isolate cannot be one of a cyclic vertex's neighbors); no four-set is a union of components in the proposed family. For n≥6 one can always use a single (n−1)-cycle. The undirected cycle factor is 1/(2ℓ), and the isolate factor z gives n! times the stated coefficient. At n=11 the two component types contribute 1,995,840 and 199,584. The independently written exact check exhausts subsets of size at most n−1 for n=4–7 using adjacency symmetric differences with both target bits removed. It reproduces the optimum counts 72 and 420 for n=6,7 and finds no successes at size ≤n−1 for n=4,5. The proof, not finite checking, gives the all-order result.

## originality

PASS

The definition and a boundary value are established earlier; the strongest inspected sources on the identical invariant do not give the n≥6 triangular-family minimum, structure, or labelled count. Related triangular classifications concern different predicates. Unavailable older material leaves a priority risk, not a negative finding about its contents.

## value

PASS

The distinction from ordinary metric dimension is substantive: forbidding self-witnesses yields an exact unbounded-family minimum and a rigid cycle-packing structure for all optimizers. The structure gives labelled counts and separates the first multi-cycle optimum at n=11 from the single-cycle regime. The reusable triple/four-cut criterion is useful beyond computing the minimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
