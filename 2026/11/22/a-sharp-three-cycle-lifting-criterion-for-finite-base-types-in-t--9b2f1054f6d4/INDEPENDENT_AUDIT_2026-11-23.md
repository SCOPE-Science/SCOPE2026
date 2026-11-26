# Independent mathematical audit

## correctness

PASS

Over a finite individually named induced base in the countable dense local order, homogeneity makes the orientation vector a complete realized nonalgebraic one-type. The 2n base points and antipodes cut the circle into nonempty cells and each direction changes at its two opposite boundary points. Distinct cells cannot have the same vector: a traversal between them would have crossed either both or neither boundary for every label; crossing both for any label makes the traversal longer than a half-turn, hence crosses at least one for every label and would have to cross all marks, contrary to the cells being distinct. For different cells the clockwise edge is forced if their index gap is below n, forbidden if above n, and selectable at n by ordering the points' relative positions after antipodal translation. Within a cell either binary direction is possible but a cycle is not. For three distinct types passing the binary tests, their three positive residues sum to 2n, not 4n since the sum is at most 3n, so they are in clockwise order. At most one gap equals n: choose that edge by the relative-position test, with the other directions forced. If exactly two types coincide the remaining type must be antipodal; choose the two points in the repeated arc in the required cyclic order and place the third with its antipodally translated position between them. Density realizes these strict choices with distinct new vertices. The distinct-type count is 2n times the positive gap compositions with sum 2n and maximum n, i.e. 2n[binom(2n-1,2)-3binom(n-1,2)] (zero if n=1); the repeated-type count is 6n. This yields n(n+1)(n+2), including n=1. Read RESULT.md lines 23–39 and inspected verify.py and the archived output. Finite samples for n=1–8 are diagnostics, not the general proof; the uploaded script was not run.

## originality

PASS

Circular coordinates, local transitivity and enumeration of locally transitive tournaments are known. The checked finding concerns the support of a directed triangle after projecting each new vertex to its unary type over a named base, and the exact cardinality of that ordered support. The closest older indexed result works with the same one-types but different invariants; the strongest same-date relative result treats configurations in two transitive blocks. Neither states or gives the triangle-profile classification by a change of notation or direct restriction.

## value

PASS

This is a natural local-to-global test in a classical homogeneous tournament: the quotient by one-types makes all three binary tests individually pass in some profiles that do not lift, and the theorem determines exactly when that happens. The exact uniform count is a reusable description of the first cyclic extension support over arbitrary finite named bases, not a count of sampled vertices or a re-evaluation of a unary score invariant. It is not a classification of all triple types or longer directed cycles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
