# Independent mathematical audit

## correctness

PASS

On the orthogonal complement of the constants the Laplacian is positive definite for a connected design; in the disconnected limit a positive eigenvalue tends to zero, so the trace of the inverse diverges. For any nonzero symmetric Laplacian variation H on that subspace the second derivative of the inverse trace is twice the trace of L^(-1/2)(L^(-1/2) H L^(-1/2))²L^(-1/2), which is strictly positive. Off-diagonal entries identify weights, so compactness with blowup at disconnection gives a unique full-space minimizer, fixed by class permutations. Clique contrasts, independent contrasts and the class contrast give eigenvalues qb+pc, pb and (p+q)b with multiplicities p-1,q-1,1. For fixed b the optimum has c=(1-qb)/(p-1); the resulting objective is A/b+(p-1)²/(p-qb), A=(q-1)/p+1/(p+q). It is strictly convex. At b=1/q for q≥p, qA≥q-1+q/(p+q)>1, so its derivative is negative. At b=1/p for p>q, the positive term of the derivative is less than q since p²-q>p(p-1), while Ap²>p(q-1)≥q. This proves endpoint optimality, including p=q. With c=0 the objective is a positive constant divided by b, so the endpoint is again optimal; subtracting the minima gives exactly the stated piecewise penalty. At fixed q the two orders are p²/q+O_q(p) and p+O_q(1), giving the ratio. The argument also allows period two and uses the specified zero-diagonal hitting-time convention.

## originality

PASS

The supported distinct claim is the exact full symmetric Kemeny optimizer for all complete split sizes, including forced clique-edge deletion at q=p and the sharp deletion penalty. The closest indexed same-graph results treat the second-largest eigenvalue modulus and admit both supports at q=p. The primary Kemeny literature inspected gives directed minima, completion results, a general convex model, or different budgets/regularization. These do not provide the exact endpoint proof or penalty in the frozen feasible set. This is a best-of-knowledge conclusion, not a priority assertion.

## value

PASS

For a natural graph family in a fixed-stationary design problem the result gives an exact support boundary for the full feasible set, including forced loss of an entire clique at the critical size. The sharp penalty on the other side quantifies when deleting the same edges is arbitrarily costly. The explicit optimizer and penalty are useful benchmarks beyond merely applying the general formulation or computing isolated small graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
