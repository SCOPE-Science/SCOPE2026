# Independent mathematical audit

## correctness

PASS

For d=gcd(n,k), including d=n when k=0, the subgroup is exactly translation by multiples of d. Each of the two types of edge orbits is indexed by a residue class mod d. A point is fixed iff its simplex coordinates are constant on each orbit; summing on each orbit and distributing each orbit-coordinate uniformly are inverse linear maps on each fixed simplex. Thus one must check the forest property for whole orbit unions, not just for edges individually. When all rim edges are selected both graphs contain the rim cycle, including a loop or two-edge cycle in the small wheels. Otherwise the smaller selected rim has path and isolated-vertex components, each with disjoint path lifts indexed by the n/d sheets. An attached hub produces a cycle iff one path has at least two incident selected spokes, and this condition is the same in the projection and in every path lift. This proves the canonical PL correspondence in all cases. For d=2 only the pair of parallel rim edges is forbidden among pairs, with no 3-face, so the connected four-vertex five-edge graph has rank-two H1. For d=1 the sole available vertex is the spoke. In general graphic matroid shellability gives spheres in dimension rank-1=d-1, and the unsigned reduced Euler characteristic is T(0,1) by the independent-set sum. Wheel self-duality interchanges T(0,1) and T(1,0); the cycle chromatic polynomial with one color removed for the hub yields (-1)^d P'(0)=2^d-2. A proper divisor d>1 occurs for a nonidentity rotation iff n is composite, and its wedge has nonzero top homology. The uploaded verify_wheel.py was inspected, not executed; enumerations for 3≤n≤9 and the incidental reflection checks are not needed for this proof.

## originality

PASS

The supported distinction is the PL fixed-space identification for rotations fixing a hub, including the literal small multigraphs. The general orbit-coordinate construction, ordinary wheel homology, and matroid homology representation are not new. The closest indexed regular-cover result was compared at summary level only; its stated regular graph covering hypothesis does not apply.

## value

PASS

For every rotation of a standard graphic matroid family the result replaces an orbit-union feasibility problem by a canonical smaller-wheel PL model, even when the hub is fixed and the quotient graph is not a cover there. It identifies a natural arithmetic distinction and actual geometric fixed spaces, not just a trace, and the multigraph boundary cases are essential to the classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
