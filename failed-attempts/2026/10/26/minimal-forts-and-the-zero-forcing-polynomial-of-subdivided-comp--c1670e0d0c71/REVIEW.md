# Independent mathematical audit

## correctness

PASS

The exact fort conditions are nonemptiness, inclusion of the original cut δ(A) among the selected edge-vertices, and no degree-one exterior original in the selected edge graph. In a minimal fort with A empty the edge graph is a simple cycle: a nonempty graph with no degree-one vertex contains a cycle, and any proper nonempty subset of a cycle has a leaf. When A is nonempty, a cycle would form a proper subfort, so the edge graph is acyclic. This rules out cuts having both sides of size ≥2 by a 4-cycle, and singleton A because its outside vertices all need a second incident edge and any added edge closes a triangle. For A=all originals or all but v the smallest allowed edge set is respectively empty or the star at v, and a proper nonempty subfort would either violate the smaller cut test or require a cycle inside the star. These arguments also cover n=3. Counting cycles by a choice of k labels followed by cyclic order modulo rotation and reflection gives n!/(2k(n−k)!), including sizes coinciding with those of the other families. Hitting these forts requires a nonempty original subset and a white forest; the only missed star fort occurs with one selected original v and its entire star white, excluding exactly n sets of size m−n+2. Cayley counts the remaining tree cases at the lowest degree. The optional forest EGF follows by taking a labeled set of tree components, each of size r with r−1 edges, including isolated vertices. Independent literal forcing and fort enumeration over all subsets for n=3,4,5 matched exact sets and size polynomials: fort totals 5,12,43; forcing totals 46,566,9016; minimum multiplicities 6,60,620. Replay: python3 /workspace/reproductions/check_subdivision.py 3 4 5. Finite tests corroborate those orders, not the unbounded claim.

## originality

FAIL

The same substantive claim, including the exact fort-size polynomial, appears in the indexed comparison and the core of the companion frozen result. Writing the forest sum in place of the equivalent Tutte specialization and applying the labeled-cycle and labeled-component counts do not separate the results. This does not establish which derivation came first.

## value

FAIL

The natural subdivision problem has a useful complete answer, but the exact indexed result supplies it already. The explicitly listed coefficients and forest EGF add numerical convenience by routine counting, not a separate unknown, motivated invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
