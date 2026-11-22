# Self-review

## Correctness — PASS

The object is the symmetric exclusion adjacency Hamiltonian on the \(\binom{2m+1}{2}\)-dimensional occupation-pair space, with \(m\ge3\) and every nonzero hop equal to one. Independent swapping of the leaves within each petal decomposes its Hilbert space orthogonally into \(\binom m2\) one-dimensional antisymmetric-pair modes, \(m\) antisymmetric single-petal sectors, and a fully leaf-symmetric sector. The latter is reduced by the unsigned incidence matrix of \(K_m\), whose Gram spectrum \(2(m-1),m-2\) determines the final two cubic factors. The block dimensions add to \(m(2m+1)\) and yield exactly the displayed factorization. Their fixed-energy multiplicities prove the limiting spectral measure. Exact integer full-matrix characteristic polynomials agree for \(3\le m\le7\), using the embedded standalone verifier. The proof is analytic for every integer \(m\ge3\); finite checks are not treated as infinite proof. The fixed \(2\)-energy flat sector is absent at \(m=3\) and present for \(m\ge4\), as expressly stated.

## Originality — PASS on examined evidence

The closest same-graph result is the complete **Laplacian**, not adjacency, spectrum of the two-token friendship graph (public record c081d2602b88). Its full result and proof were inspected. Since token degrees are \(2,4,2m\), the operator \(L=D-H\) is not a scalar shift of the hopping Hamiltonian; the prior integer Laplacian levels do not supply its adjacency factors, flat energies, or limiting spectral measure. The published proof shares useful incidence and symmetry ideas, which are credited. Audenaert–Godsil–Royle–Rudolph (2005) introduce the hard-core symmetric-square Hamiltonian, but do not evaluate this family. The friendship-graph single-particle spectrum (Cioabă et al., 2013) cannot in general be added to produce a hard-core two-particle spectrum on cyclic networks. Path-specific hard-core boson formulas (Large et al., 2014) and token graph spectral bounds (Reyes et al., 2023) do not cover the exact claim. Focused indexed searches and the accessible prior ledger found no exact identical or dominating claim. Absence from search results does not establish historical priority; a missed equivalent calculation remains possible.

## Mathematical value — PASS

The model is a canonical hub-coupled assembly of frustrated triangular quantum cells. Hard-core two-particle hopping is nontrivial even when the one-particle spectrum is known. The full factorization resolves an infinite family of interacting two-excitation Hamiltonians, identifies three explicit compact localized mode mechanisms, and gives the macroscopic universal \(1:2:1\) fixed-energy spectral-weight limit. This directly informs degeneracy and spectral-response analysis of two-excitation quantum networks and is not merely a normalization or isolated parameter substitution.

## Closest literature and risks

- Audenaert et al., *Symmetric Squares of Graphs*, https://arxiv.org/abs/math/0507251, first public 2005-07-12, complete primary text inspected.
- *Integral Laplacian spectrum and spanning-tree complexity of two-token friendship graphs*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-integral-laplacian-spectrum-and-spanning-tree-complexity-of-two--c081d2602b88, complete primary result and proof inspected; same graph but different operator.
- Cioabă et al., https://arxiv.org/abs/1310.6529, single-particle adjacency spectrum; full HTML inspected.
- Large et al., https://arxiv.org/abs/1412.1022, hard-core bosons on weighted paths; full HTML inspected.
- Reyes et al., https://arxiv.org/abs/2310.16929, token-graph spectral bounds; full HTML inspected.
- Residual risk: an equivalent unpublished or unlocated prior adjacency formula may exist, especially under token-graph, symmetric-square or many-body terminology. The work has not undergone independent scholarly review.

Self-review: passed. Independent audit: not yet performed.
