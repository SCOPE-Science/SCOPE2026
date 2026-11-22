# Scientific review: orthogonal prefix modes in a free left regular band

## Correctness — PASS

The finite word product is explicitly defined, and equality of \(uv\) and \(vu\) forces prefix comparability. The graph therefore is the transitive ancestor closure of the permutation-prefix tree. The key proof constructs mutually orthogonal **invariant** radial and child-difference spaces, not just an equitable quotient. Their exact dimensions add to the full vertex space, and the induced adjacency operators are the explicitly normalized quotient matrices \(H_k\). This proves the full polynomial, without extrapolating finite experiments. For each \(k\), the coincident final two rows and columns of \(H_k+I\), and a nonzero leading minor, give the exact derivative \(P'_k(-1)=-2(k-1)!\). The resulting factorial multiplicity follows by telescoping. Direct full adjacency characteristic polynomials were independently recomputed through \(n=4\); symbolic minor, derivative, degree, and exponent checks extend farther. Finite checks are corroboration, not general proof.

## Originality — PASS, with residual risk

The relevant source for the algebra is Saliola's 2006 treatment of the free left regular band, whose quiver and Cartan invariants concern a distinct operator. Brown's 2000 Markov-chain spectrum likewise concerns a different matrix. Generic cograph spectral algorithms (Jacobs–Trevisan–Tura, 2016) and a later trivially-perfect-graph resolvent recurrence (Conde–Dratman–Grippo, 2026) can compute graph eigenvalues in principle; a previously known cograph formula can also help deduce the \(-1\) corollary. These facts are **not** claimed independently new. The contribution remaining after those comparisons is the closed all-parameter **semigroup-specific orthogonal decomposition** with exact copies of every small quotient and factorial exponents, not merely an algorithm to locate eigenvalues. A related published free-left-legal-semigroup result concerns a non-idempotent variety and gives a different commuting graph and its Laplacian spectrum. The most significant residual risk is a generic cograph or spherically homogeneous-tree decomposition implicitly equivalent to the new one; no independent priority certification has been performed.

## Value — PASS

The commuting graph has \(\sum_{d=0}^{n}n!/(n-d)!\) vertices, and its full spectrum is nevertheless described by only \(n\) determinant factors of orders at most \(n+1\) and explicit integer multiplicities. This gives a meaningful unbounded structural classification of an algebraically natural semigroup invariant, including all noncentral graph components. The exact decomposition and polynomial handle every eigenvalue, not an arbitrary small finite instance or numerical improvement.

## Scientific scope and evidence

The checker reconstructs operations and adjacency from definitions rather than using the theoretical quotient construction for its input, compares exact characteristic polynomials for \(n\le4\), and tests the exceptional root and degree identities separately. Exact proofs are in `RESULT.md`. The findings are only for the free idempotent left regular band with the stated full or noncentral graph conventions. An earlier general equivalent eigenspace decomposition remains a live priority risk.

Self-review: passed. Independent audit: not yet performed.
