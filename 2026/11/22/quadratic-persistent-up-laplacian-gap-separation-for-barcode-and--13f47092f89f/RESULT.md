# Quadratic persistent up-Laplacian gap separation for barcode-and-face-vector twins

## Finding
For every integer \(n\ge3\), set \(m=2n-1\). We give two two-level simplicial filtrations with the same integral persistence barcode and the same face counts at both levels, yet with a quadratic separation of the smallest positive eigenvalue of their degree-one persistent **up**-Laplacians. Their top nonzero eigenvalues also separate linearly. Specifically, for the book family the positive spectrum is \(\{2\text{ (multiplicity }m-1\text{)},\ m+2\}\), whereas for the punctured-bipyramid family the smallest positive eigenvalue \(\mu_n\) satisfies
\[
\frac{1}{n(2n-1)}\le\mu_n\le2\left(1-\cos\frac{\pi}{n}\right)\le\frac{\pi^2}{n^2}.
\]
Its largest eigenvalue is at most \(6\). Thus \(\mu_n=\Theta(n^{-2})\) and the gap ratio \(2/\mu_n=\Theta(n^2)\).

## Assumptions and scope
All simplicial chain groups have the standard Euclidean inner product in the oriented-simplex basis, and all eigenvalues refer to unweighted, unnormalized matrices. At level zero we include every vertex and edge, and no triangle. At level one we include the same one-skeleton and all specified triangles. An essential degree-zero bar starts at zero; a finite bar \([0,1)\) is born at level zero and dies at level one.

**Book family:** vertices \(u,v,w_1,\ldots,w_m\), edges \(uv,uw_i,vw_i\) and triangles \([u,v,w_i]\). The final complex is a union of triangles along the common edge \(uv\).

**Punctured-bipyramid family:** vertices \(a,b,r_0,\ldots,r_{n-1}\), cyclic rim edges \(r_ir_{i+1}\), and both apex-to-rim edge sets. Take all \(2n\) triangles \(ar_ir_{i+1}\), \(br_ir_{i+1}\) with indices modulo \(n\), but omit \(ar_0r_1\). Attach \(n-1\) new leaf vertices by \(n-1\) distinct edges to any fixed old vertex; no new triangles. The missing facet gives a triangulated closed disk, and leaf attachments preserve contractibility. There are \(m\) triangular faces.

For a pair \(P\subseteq Q\), define \(C_2^{P,Q}=\{z\in C_2(Q):\partial_2z\in C_1(P)\}\) and its induced boundary \(\partial_2^{P,Q}\); the up-Laplacian is \(\Delta_{1,+}^{P,Q}=\partial_2^{P,Q}(\partial_2^{P,Q})^*\). Since both constructions keep their entire one-skeleton, \(C_2^{P,Q}=C_2(Q)\) and the matrix is \(BB^\top\), with \(B=\partial_2(Q)\).

## Proof
**Face counts and persistence.** For the book, \(f_0=m+2\), \(f_1=2m+1\), \(f_2=m\). The bipyramid disk before leaves has \(n+2\) vertices, \(3n\) edges and \(2n-1=m\) triangles. Attaching \(n-1\) leaf edges produces \(2n+1=m+2\) vertices and \(4n-1=2m+1\) edges. At level zero, each graph is connected with integral first Betti number \(f_1-f_0+1=m\). At level one, both spaces are contractible: the book contracts to its shared edge, and the punctured sphere is a disk with trees attached. Thus their integral persistence modules coincide in every degree.

**Book spectrum.** Orient all triangles coherently along the common edge. Each boundary column has three entries of absolute value one, and distinct columns overlap in exactly one common edge with the same sign. Hence the triangular Gram matrix is
\[
B^\top B=2I_m+\mathbf1\mathbf1^\top.
\]
Its eigenvalues are \(2\) with multiplicity \(m-1\), and \(m+2\) with multiplicity one. Since the columns have full rank, these are exactly the strictly positive eigenvalues of \(BB^\top\).

**Disk spectrum.** The dual graph of all facets of the unpunctured bipyramid is the prism \(C_n\square K_2\): within either apex family consecutive facets share an edge, and paired apex facets meet along a rim edge. Orient the triangulated sphere coherently, so an interior edge has opposite incidence signs on its two faces. Consequently its complete triangle Gram matrix is the graph Laplacian of the prism. Removing one triangle corresponds to deleting one row and column, i.e. imposing zero potential at that dual vertex. The surviving Gram matrix is precisely the positive-definite Dirichlet principal submatrix \(L_D\) of that prism graph Laplacian. The extra leaf edges have zero rows in the triangle boundary, so do not change nonzero eigenvalues.

Every unpinned dual vertex has a path of length at most \(n\) to the pinned vertex. Along any such path, Cauchy–Schwarz gives \(|x_v|^2\le n\sum_{e}(\nabla_e x)^2\), with the pinned value zero. Summing over the \(2n-1\) surviving vertices proves
\[
\lambda_{\min}(L_D)\ge\frac1{n(2n-1)}.
\]
For the opposite inequality, label the dual prism's two rings by \(i\in\mathbb Z/n\mathbb Z\), pin vertex \((0,0)\), and put \(x_{(\epsilon,i)}=\sin(\pi i/n)\) on both rings. The two rings have identical values, so their cross edges contribute zero energy. On either cycle the energy-to-norm ratio equals the first Dirichlet eigenvalue of the \(n\)-edge path, \(2(1-\cos(\pi/n))\). Thus the stated upper bound follows by the Rayleigh principle. Finally, each facet has at most three neighbors in the prism and the Gram matrix has diagonal \(3\) and off-diagonal entries of magnitude at most \(1\), so Gershgorin's theorem gives \(\lambda_{\max}\le6\).

The book-to-disk ratio of smallest positive eigenvalues is at least \(2/[2(1-\cos(\pi/n))]=\Theta(n^2)\), and at most \(2n(2n-1)=O(n^2)\), proving sharp quadratic order. The ratio of largest eigenvalues is at least \((2n+1)/6\).

## Verification
The standalone file `checker.py` constructs both signed triangle boundary matrices from enumerated faces and checks their sizes, integral ranks, exact book Gram formula, positive eigenvalues, and disk spectral bounds for every integer \(3\le n\le12\). Run `python checker.py` using Python 3 and NumPy. These finite computations are independent consistency checks; the proof above establishes all \(n\ge3\).

## Relationship to prior work
Kirchner and Vittorietti (arXiv:2611.09610, first posted 6 November 2026) develop new persistent chain spaces and emphasize non-harmonic persistent spectral information beyond barcode data; they do not state a quantitative, same-face-vector two-family spectral separation of this kind. Botnan and Dong (arXiv:2408.16741) develop up-Laplacian algorithms and dual nonbranching geometry; the punctured-bipyramid side belongs to their nonbranching regime, whereas the book is branching along its common edge. Their general framework supplies background but does not supply the specified paired extremal bounds. Single-simplex spectral-stability work (arXiv:2506.21352) concerns local perturbations, not same-barcode, same-face-vector families with growing spectral gap ratios. General knowledge that persistent nonzero spectra detect information beyond persistent homology is prior art, **not** claimed as new here.

## Limitations
These are artificial two-stage, unweighted simplicial filtrations, not asserted to arise from Euclidean point clouds or from Vietoris–Rips filtrations. The gap claim concerns the **up**-Laplacian; it is not a claim about the smallest nonzero eigenvalue of the full Hodge Laplacian, whose down part may have other small eigenvalues. We establish a sharp asymptotic order, not an exact closed formula for the disk's smallest eigenvalue. No independent mathematical audit is claimed, and publication priority outside the checked literature remains uncertain.

## References
- J. Kirchner and M. Vittorietti, *New persistent chain spaces: identifying and computing the relevant persistent Laplacians of a filtration*, arXiv:2611.09610 (6 November 2026), https://arxiv.org/abs/2611.09610.
- M. B. Botnan and R. Dong, *The persistent Laplacian of non-branching complexes*, arXiv:2408.16741 (first public 29 August 2024), https://arxiv.org/abs/2408.16741.
- L. V. Anh, M. Dik, and N. V. Anh, *Lipschitz Bounds for Persistent Laplacian Eigenvalues under One-Simplex Insertions*, arXiv:2506.21352 (26 June 2025), https://arxiv.org/abs/2506.21352.
- F. Mémoli, Z. Wan, and Y. Wang, *Persistent Laplacians: Properties, Algorithms and Implications*, SIAM J. Math. Data Sci. 4 (2022), DOI:10.1137/21M1435471.
