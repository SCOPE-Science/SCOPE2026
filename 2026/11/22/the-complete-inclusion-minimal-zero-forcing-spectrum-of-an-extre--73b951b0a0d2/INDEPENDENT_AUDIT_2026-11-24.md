# Independent mathematical audit

## correctness

PASS

A path vertex is blocked by two or more white core vertices. With no blue core vertex the process cannot start; with only one, an edge endpoint succeeds precisely from the full blue path, while the isolate can at best fill the path without unlocking the core. With two blue core vertices and at least two white path vertices, no core vertex can start; a path vertex can force the remaining core vertex iff all its path neighbours are blue. This is exactly an endpoint pair or an interior triple, and the same condition is automatic with at most one white path vertex because the endpoint pairs are disjoint. The resulting all-blue core and an adjacent path pair finish the path. With three blue core vertices the criterion is a blue endpoint or adjacent blue pair: if neither exists, every blue path vertex and every core vertex has at least two white neighbours. The listed minimal path patterns follow, and deleting a core vertex from any such pattern fails the next lower-core criterion. Counting gives 8, 4m−15 and 2, with the last two contributions combined at m=4. An independent fort-based exhaustive check gave the same polynomials for m=4–12; the case proof supplies the unbounded result.

## originality

PASS

The family, extremal gap and both endpoint sizes are known. The distinct claim is the complete labelled classification, multiplicities and absence of other sizes. The inspected same-family proposition does not give that classification and no independent equivalent or broader covering enumeration was found.

## value

PASS

The family is motivated by a known extremal discrepancy, not an arbitrary graph slice. The exact cardinality distribution exposes a linearly growing gap: for m≥6 almost all labelled minimal sets have only four or five vertices, two have m+1, and there are none in between. That stronger fact can be used in comparing minimal-set distributions on extremal families and does not follow from the extreme parameters alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
