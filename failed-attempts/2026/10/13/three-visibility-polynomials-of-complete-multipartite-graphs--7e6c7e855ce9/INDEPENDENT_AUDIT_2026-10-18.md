# Independent mathematical audit

## correctness

PASS

PASS: For u,v inside the same multipartite part Vi, the distance-two geodesic has an unselected internal vertex exactly when Y=V\X has an element outside Vi; all cross-part pairs are adjacent. Thus if Y intersects two parts, all 3 visibility predicates hold. When Y is nonempty in one part, ordinary requires at most one selected vertex remaining in that part; outer requires Y to be the whole part; dual requires Y singleton in a part of size <=2. Y empty is valid only in complete graphs. Disjoint nonempty single-part complements give exactly the three stated binomial-subtraction polynomials. Independently enumerated all vertex subsets of K(1,2), K(1,1,3), K(1,2,3), K(2,2,2), K(1,1,1), K(3,3,1) and each predicate, matching every coefficient. Correct for r>=2 nonempty parts and excludes the separate total predicate.

## originality

FAIL

FAIL (decisive prior implication). Before this 2026-10-13 submission, published Resultary 2026-10-04 'Coefficientwise extremals for visibility polynomials of complete multipartite graphs' states exact ordinary coefficient r_{N-t}=C(N,t)-Σ_{i:n_i>=t+2}C(n_i,t) for 1<=t<=N−1; this is the first claimed polynomial verbatim after reindexing t=N−k. Another published Resultary 2026-10-04 'Dual, outer, and total mutual-visibility colorings of complete multipartite graphs' proves EXACT outer and dual iff-characterizations for all subsets by the same complement Y two-part/single-part cases as the claim. These prior stronger all-set characterizations imply every outer/dual polynomial coefficient by immediate binomial counting. The special-case and corollary coverage defeats originality without requiring identical polynomial formatting. This is not merely matching topic names: the full earlier RESULT.md proofs were read and their conditions matched word-for-word mathematically.

## value

FAIL

FAIL: Although the formulas are correct and useful as an organized reference, all three asserted new cardinality enumerators are immediate counting consequences of two already-published complete-multipartite coefficient/valid-subset theorems. The proposed work is a direct recomputation of a known ordinary table and binomial packaging of known outer/dual predicate classes, without a nonroutine further invariant, new extremal boundary, or motivated obstruction. Under the shared C/O/V bar this is not an independent mathematically valuable advance, even if no earlier paper displays the outer/dual polynomials in exactly these symbols.

The dated certificate retains the supplied scientific assessment, sources and limitations.
