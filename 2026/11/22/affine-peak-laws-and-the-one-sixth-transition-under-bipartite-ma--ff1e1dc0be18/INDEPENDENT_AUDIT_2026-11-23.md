# Independent mathematical audit

## correctness

PASS

The descending-order side sequence gives q_{n,k} by sampling without replacement. Given initial run k, the first opposite-shore vertex is matched to a vertex outside the run with probability m(n-k)/n², and its mate wins the ensuing relative-order race against the other n−1 opposite-shore vertices with probability 1/n. The possible opposite-shore extra peak instead has unconditional (given starting shore) probability m/n² and forces k=1. To make disjointness explicit: if this opposite-shore peak is the first vertex of its shore, its unique mate is the globally first vertex and cannot be a late peak; otherwise each extra peak would have to precede the other. This fills the terse argument in the frozen proof without altering the result. The exact pgf and mixture follow. Expanding factors 1−j/(2n−j) using a quadratic bound in the sum of deficits gives the stated uniform polynomial remainder times 2^−k for k≤n/2; beyond there S≤L+1 and the geometric tail bound applies. The positive correction mass is 1/8+11ρ/8+max(1/4−3ρ/2,0), giving 17/48 at ρ=1/6. The degree mean follows by the probability 1/(degree+1) that a vertex is highest in its closed neighborhood. Direct independent permutation counts for all m at n=2,3,4 matched; the uploaded verifier was inspected, not run.

## originality

PASS

The supported distinct claims are the exact all-m matching-deletion law and its uniformly sharp total-variation correction and transition. Neither the local-maximum reduction, general moments, nor the C6 special case is distinct.

## value

PASS

An exact finite all-order law for a natural deterministic perturbation of a familiar graph gives more than a moment or a limiting distribution: deletion interpolates the entire law, and the sharp error quantifies a nonmonotone choice of density for geometric approximation. This is useful independently of its colouring interpretation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
