# Independent mathematical audit

## correctness

PASS

For an idempotent projection the weight-minus-one identity is equivalent to closure under multiplication of both image and kernel, in either characteristic. After splitting, each nonunital subalgebra of a coordinate algebra has a basis of indicators of disjoint supported blocks: these are the primitive idempotents on its support. A complementary ordered pair gives a red/blue block incidence graph with one extra root for missing support, n labelled coordinate edges and n+1 vertices. Its indicator matrix, with column signs changed on one color, is the incidence matrix with the root column removed. This is full rank exactly when the graph is connected, hence a tree; for a tree one may see full rank over any characteristic by successively removing leaves. Labelling each non-root vertex by its parent edge is equivariant. Over a finite splitting field, Frobenius descent therefore amounts to invariance of this tree and its colors. A parent of a d-cycle maps to the root or to a distinct e-cycle with e|d, with e equivariant choices in the latter case. A cycle in the quotient cannot reach root, and if the quotient reaches root then so does every coordinate. Alternating colors contributes exactly two choices for each quotient edge into the root. The directed matrix-tree determinant hence has the stated row Laplacian; its degree-ordered diagonal block is (2+s_d+d*r_d)I-dJ, with determinant (2+s_d)(2+s_d+d*r_d)^(r_d-1). This integer argument is independent of the base characteristic and counts operators, not conjugacy classes. A fresh finite check enumerated all linear maps and tested the identities on basis elements, obtaining F2 counts 432, 12, 32 for degrees (1,1,1,1), (2,2), (1,1,2), and F3 counts 50, 6, 2 at (1,1,1), (1,2), (2). Replay with python3 /workspace/branches/independent_checks.py 5. These tests corroborate the proof; the uploaded checker was inspected, not run.

## originality

FAIL

The full product, not just the split case, follows from the known split colored-tree classification and Labelle's exact fixed-tree cycle-index formula (Wagner 2006, Theorem 1), by Frobenius descent and adjoining two fixed root labels. This is positive prior-coverage evidence for the enumerated invariant, not an inference from a search miss or a later split record. The count is correct, but the frozen record omits the stronger combinatorial antecedent.

## value

FAIL

Finite étale Rota–Baxter splitting counts are a natural invariant, and the short matrix-tree proof can be useful exposition. But the asserted contribution is the exact count, which imports no new enumerative data beyond the known fixed-tree formula once the prior equivariant split correspondence is descended. The two fixed root labels and elementary fixed-edge averaging recover every factor. The record does not establish another distinct structural or quantitative result beyond this consequence, so it does not supply an independently valuable new exact invariant as framed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
