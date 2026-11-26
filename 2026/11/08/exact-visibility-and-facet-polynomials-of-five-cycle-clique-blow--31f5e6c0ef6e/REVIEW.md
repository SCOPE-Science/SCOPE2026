# Independent mathematical audit

## correctness

PASS

The only nonadjacent endpoints lie in distance-two base fibers and have precisely the intervening fiber as their common neighborhood. Thus the forbidden configurations are exactly full-middle plus one endpoint on each flank. They are distinct (only the middle is full when m≥2), of equal size, and every nonface contains one, proving the minimal-nonface count. Encode an empty, proper nonempty, or full fiber by E, P or F. Every F needs an E neighbor. With one F the remaining weight is (1+A)^4−A²(1+A)^2; with two F the adjacent case contributes 1+A and the nonadjacent case (1+A)^2+A, each with five placements; with three, the two E must be nonadjacent and the five rotations of FFEFE result. Fewer than two E cannot support three or more F. A facet has m−1 selected vertices in each P, every P must have two nonempty neighbors, and every E must be sole empty neighbor of some F. These are necessary and sufficient by one-vertex augmentation. With one F an essential E next to it has a P on its other side, contradicting the P condition. Adjacent F force two exterior E and leave a remaining site that can grow whether E or P. For two nonadjacent F, the shared neighbor E requires P in both exterior positions, or the shared neighbor P requires E in both. No F leaves only all P; three F leave FFEFE. The four types give exactly the stated counts and sizes, with coincident exponents added. In particular sizes 3m−1 and 3m show nonpurity for every m≥2. The maximum is 6,10 at m=2,3, and 5m−5 for m≥4. An independent graph-based 243-state check reproduces the weighted state coefficients and the four facet orbits; the frozen verifier was inspected, not run.

## originality

PASS

Credit the complete ordinary-visibility distributions including those with full fibers, their additional facet types and the exact ordinary obstructions. The same-family total-visibility enumerators already recover the no-full-fiber sector and its P-only facets, so that sector and standard polynomial machinery are not distinct contributions. The additional ordinary configurations are not covered by the compared results.

## value

PASS

C5 supplies a natural nontrivial cyclic quotient with unique intermediate fibers. The complete ordinary obstructions and facet sizes show exactly where the ordinary complex diverges from the pure total complex, including extra maximal sets for all m and changes in the maximum-size type at small m. This supplies explicit building blocks and benchmarks for cyclic clique substitutions rather than a single unmotivated size check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
