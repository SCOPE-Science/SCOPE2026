# Scientific review

## Correctness — PASS

The vertex set is exact because each ordered one-hot pair is uniquely exposed by a sum of two coordinate functionals. The moment matrix is obtained by uniform enumeration over the \(N=p^2+2pq+q\) directed edge-or-loop pairs. An orthogonal symmetric/antisymmetric change of variables gives the graph Laplacian block and a centered signless block. The resulting clique, independent, and class-contrast eigenspaces form an orthogonal basis of the intrinsic tangent space, giving all eigenvalues with their multiplicities and two null directions. Comparing the only two least-eigenvalue candidates gives the exact polynomial \(H_p(q)\); its discriminant and endpoint signs prove every claimed integer phase including the two ties. The standalone standard-library checker separately reconstructs exact covariance matrices from vertices for 85 parameter pairs and tests the full proposed eigenbasis.

## Originality — PASS with priority caveat

Primary full-text comparisons include Davis–Chen (arXiv:2007.11051), Ohsugi–Tsuchiya (arXiv:2103.15045), and Davis–Jakovleski–Pan (arXiv:2202.09853). These papers study the PQ polytope construction, Ehrhart theory and normalized volumes; none of their inspected statements identifies the vertex-uniform covariance spectrum or the two changes of its least-variance mode. The classical complete-split Laplacian spectrum is an input to only the antisymmetric block and does not itself determine the centered symmetric block. Published geometric work on balanced complete-bipartite PQ adjacency polytopes concerns a different polytope family and a minimum-volume enclosing ellipsoid, not the stated covariance distribution. A broader undiscovered equivalent statement remains possible; searches do not certify historical uniqueness.

## Mathematical value — PASS

The result computes an intrinsic vertex-distribution geometric invariant for every member of a natural two-parameter lattice-polytope family already studied for volume and applications in network power-flow equations. It establishes a genuinely reentrant change in principal eigenaxis type, all tie parameters and multiplicities, and a quadratic threshold for the second change. These structural facts are not determined by vertex counts, normalized volumes, or graph-Laplacian eigenvalues alone. The precise smallest eigenmode and condition number matter for geometric sampling and covariance ellipsoid comparisons; no downstream theorem is claimed.

## Closest sources and limitations

The full-text join-graph PQ paper (arXiv:2103.15045, Section 4) is the closest source on exactly the underlying graph family; its Theorem 4.1 computes different invariants. The earlier volume paper arXiv:2007.11051 defines the same polytope construction. Existing complete-split spectral graph results give related block eigenvalues but not the covariance decomposition and threshold polynomial. The work concerns the standard-coordinate embedding and the uniform distribution on distinct polytope vertices, not the volume-uniform law or arbitrary affine images. Independent historical priority and independent proof validation remain open.

Self-review: passed. Independent audit: not yet performed.
