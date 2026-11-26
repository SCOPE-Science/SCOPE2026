# Independent mathematical audit

## correctness

PASS

The overlap graph has distinct triples of degree two and triples aba of degree d=q−2, with equal indegree and outdegree. Rotation and the route abc→bcb→cba generate all permutations of a support; the same route can replace a with any letter outside {b,c}, giving strong connectivity for all q≥3. With row adjacency, the three transfer actions are SQ=X, SRQ=Y, SR²Q=dJ. Each triple rotation orbit has size three, so the Schur complement has the stated power of A³−1, which is nonzero at z=0. The pair residual after constants and row/column letter functions has both row and column sums zero. Its symmetric and skew dimensions follow from unsigned complete-graph incidence of rank q (an odd triangle forces any left-kernel vector to vanish) and oriented incidence of rank q−1 (the left kernel is constant). On those spaces X=Y=−I, and J=±I. On the 2×2 letter block the determinant at zero is (3d+2)(5d+4)−(4−d)(2−d)=14dq, repeated q−1 times. The constant factor is z(z+d+1)(A²+A+1), so it contributes derivative 7(q−1); the symmetric and skew factors at zero are 6(q−1) and 2(4q−5). Divide the derivative of the full determinant by q(q−1)², since the balanced strongly connected graph has equal in-arborescence cofactors. BEST with a specified first edge multiplies this cofactor by ((q−3)!)^{q(q−1)}. Every cycle has exactly one rotation with that edge first; neither reversal nor relabeling was divided out. At q=3 the symmetric summand is zero-dimensional, the derivative is 144, and the cofactor and the cycle count are both 12. Independent bounded replay: /workspace/branches/f218a359-9602-4468-a856-831d0903ec75/independent_matrix_tree_replay.py with adjacent .out; direct cofactors at q=3,4,5 and pair-space checks through q=6. The exact q=4 and q=5 example counts agree. Universal validity rests on the proof, not the bounded replay; frozen code was inspected, not executed.

## originality

FAIL

The distinct indexed exact-count record 38157601ee92 has the same labeled language, the same equivalence relation, U_3=12, and the same all-q product. This is exact catalogue coverage, regardless of the unresolved ordering or provenance of the two records. The classical references alone do not give this specialization, but they cannot negate the exact indexed match. No substantive uncovered remainder warrants repair.

## value

FAIL

An exact labeled count for this natural overlap graph is a mathematically useful invariant, and the determinant calculation is nontrivial in isolation. But the exact count across the entire range is already available in the distinct catalogue record. The frozen claim identifies no additional invariant or case that resolves a separate gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
