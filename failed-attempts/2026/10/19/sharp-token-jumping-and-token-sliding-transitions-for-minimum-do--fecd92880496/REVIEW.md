# Independent mathematical audit

## correctness

PASS

Any two selected edges admit a different edge intersecting both. For three edges, a matching and a triangle each dominate. If a pair is ab,ac, then a third edge through a gives a star and an external vertex supplies an unselected transversal through a; a third edge not through a either is bc (triangle) or has an endpoint outside {a,b,c}, again supplying a transversal through a. Triangles cannot share two edges with any other optimum. Removing one matching edge frees n−4 vertices for jumping and n−6 previously unmatched vertices for the disjoint replacement used in sliding. With one spare vertex one can free one end of a missing target edge by moving its current edge before installing the target, preserving all installed target edges. At n=8 the omitted pair completes a unique four-pair partition, and slides change only which pair is omitted, giving 8!/(2⁴4!)=105 four-cliques. With three spare vertices, an overlapping jump can use the pair of spare vertices not used by its target as an intermediate slide. These prove the components and degree/edge counts; use the combinatorial zero convention for out-of-range binomial counts, including n=5 where the matching layer is empty. An independent enumeration from closed domination and shared two-edge buckets matched both boundary transitions for n=5 through 9.

## originality

FAIL

The jumping connectivity is a special case of prior general fixed-cardinality matching reconfiguration. The whole nontrivial sliding layer is exactly represented by the k=2 reduction of the distinct indexed Roman-function theorem a3f3d09e0ceb, for the same disjoint-replacement move. The triangle isolates and degree/edge formulas left over are immediate from the known minimum-set classification and local counts. This is a decision about checked existing coverage, not a conclusion that the November catalogue finding preceded, was available to, or was derived independently of the October record.

## value

FAIL

The sharp K4 boundary is meaningful as a mobility invariant, but that meaningful part is already fully represented for the same move graph. The remainder—adding known frozen triangles and counting local neighbors—does not provide a new structural invariant or mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
