# Exact dedicated controllability of the four-dimensional ternary point–line network

## Finding

Let \(P=\{0,1,2\}^{4}\) be the \(81\) points of a four-dimensional ternary grid. Let \(\mathcal L\) be its \(108\) coordinate-axis lines: for each axis \(a\in\{0,1,2,3\}\) and each triple of fixed coordinates \(b\in\{0,1,2\}^{3}\), there is one line \((a,b)\). Let \(G\) be the bipartite point–line incidence graph with \(189\) vertices, point degrees \(4\), and line degrees \(3\). For its unit-edge combinatorial Laplacian \(L\), let \(\kappa(G)\) denote the smallest number of distinct vertices each receiving one independent scalar input for the fixed system \(\dot z=-Lz+B_Su\), where the columns of \(B_S\) are the corresponding coordinate vectors.

**The exact answer is \(\kappa(G)=59\)**. Every controllable placement uses at least \(16\) point vertices and at least \(43\) line vertices. One placement with exactly these counts is given below and is controllable. In contrast, the largest Laplacian eigenspace has dimension only \(43\); hence the maximum-eigenvalue-multiplicity lower bound for arbitrary input matrices is not sharp for dedicated coordinate inputs on this network. The constructed minimum placement is not a zero-forcing set.

## Assumptions and scope

This is a fixed finite, simple, unweighted, undirected graph, *not* a general statement for arbitrary weighted incidence graphs. Points are ordered lexicographically as tuples in \(\{0,1,2\}^4\). Lines are ordered first by the free coordinate \(a=0,1,2,3\), then lexicographically by the remaining three coordinates. Indices start at zero. For the explicit placement, actuate the \(16\) point vertices with all four coordinates in \(\{0,1\}\). Form the binary incidence matrix \(N\) of size \(81\times108\). Scan its line columns in the stated order over the finite field \(\mathbb F_{101}\), retaining a column if it increases the span of the previously retained columns. The scan retains \(65\) columns; actuate the \(43\) line vertices corresponding to *all remaining* columns. The full index list and exact-rank verifier are in `verify.py`.

## Proof

Write the Laplacian in point–line blocks:

\[
L=\begin{pmatrix}4I_{81}&-N\\-N^{\mathsf T}&3I_{108}\end{pmatrix}.
\]

Two distinct grid points lie on a common axis line exactly when they differ in precisely one coordinate; each point lies on four axis lines. Therefore

\[
M:=NN^{\mathsf T}=4I_{81}+A_{H(4,3)},
\]

where \(H(4,3)\) is the Cartesian product of four triangles. Decomposing each coordinate space as the one-dimensional constant subspace plus the two-dimensional coordinate-sum-zero subspace gives the exact spectrum

\[
\operatorname{spec}(M)=\{12^{[1]},9^{[8]},6^{[24]},3^{[32]},0^{[16]}\},
\]

where brackets indicate multiplicity. In particular, \(\operatorname{rank}N=65\), \(\dim\ker N^{\mathsf T}=16\), and \(\dim\ker N=43\).

The \(\mu=4\) Laplacian eigenspace is precisely \(\{(x,0):x\in\ker N^{\mathsf T}\}\); the \(\mu=3\) eigenspace is precisely \(\{(0,y):y\in\ker N\}\). For every nonzero eigenvalue \(\lambda\in\{3,6,9,12\}\) of \(M\), the two Laplacian eigenvalues are the distinct roots of \((4-\mu)(3-\mu)=\lambda\), namely \(\mu=(7\pm\sqrt{1+4\lambda})/2\). A corresponding eigenvector has the form

\[
\left(x,\frac{N^{\mathsf T}x}{3-\mu}\right),\qquad Mx=\lambda x.
\]

These roots for different positive \(\lambda\) do not coincide with one another or with \(3,4\). Thus the largest Laplacian eigenvalue multiplicity is \(43\). The Popov–Belevitch–Hautus criterion applied to the disjoint-support eigenspaces at \(3\) and \(4\) forces at least \(43\) line-coordinate inputs and at least \(16\) point-coordinate inputs, respectively. Thus \(\kappa(G)\ge59\).

For the upper bound, define integer matrices

\[
P_\lambda=\prod_{\nu\in\{0,3,6,9,12\}\setminus\{\lambda\}}(M-\nu I),
\qquad \lambda\in\{0,3,6,9,12\}.
\]

Each has image exactly the \(\lambda\)-eigenspace of \(M\) over \(\mathbb Q\). For the chosen point set \(U\) and line set \(V\), the accompanying exact finite-field certificate verifies

\[
\operatorname{rank}(P_0|_{U\times P})=16
\]

and, for \(\lambda=3,6,9,12\), respectively,

\[
\operatorname{rank}\!\begin{pmatrix}
P_\lambda|_{U\times P}\\
(N^{\mathsf T}P_\lambda)|_{V\times P}
\end{pmatrix}=32,24,8,1.
\]

The unactuated \(65\) line columns of \(N\) have rank \(65\), so any \(y\in\ker N\) vanishing on the \(43\) actuated line coordinates must vanish everywhere. The first displayed rank likewise ensures every nonzero \(x\in\ker N^{\mathsf T}\) has a nonzero actuated point coordinate. For every nonzero \(\lambda\), the second rank statement detects every nonzero eigenvector for both corresponding Laplacian eigenvalues; scaling all line measurements by \((3-\mu)^{-1}\) does not alter their rank. PBH therefore establishes controllability with \(59\) actuators and proves equality.

The verifier performs exact integer polynomial construction followed by Gaussian elimination modulo the prime \(101\). A nonzero minor modulo a prime is a nonzero integer minor, so each asserted lower rank over \(\mathbb F_{101}\) certifies at least that rank over \(\mathbb Q\); the tensor eigenspace dimensions above provide the corresponding upper bounds. These are exact finite proofs for this fixed graph, not floating-point experiments.

Finally, for the same set of initially marked vertices, no marked vertex has exactly one unmarked neighbor; therefore the standard zero-forcing procedure cannot even begin. This confirms that the exhibited coordinate-controllable placement is not a zero-forcing set.

## Verification

Run `python3 verify.py` with an ordinary standard-library Python 3 interpreter. The program constructs all \(189\) vertices and their incidence relations, checks the Gram matrix and degree identities, chooses the specified \(65\) independent incidence columns, and verifies all required modular ranks. It also tests the zero-forcing first step. The observed output is `VERIFY_OK`, the incidence rank is \(65\), and the nonzero-mode rank vector for \(\lambda=3,6,9,12\) is \((32,24,8,1)\). The method requires neither external mathematics libraries nor trust in a prerecorded log.

## Relationship to prior work

The classical Gray configuration uses the \(27\) points and \(27\) axis-parallel lines of a three-dimensional ternary grid; its cubic incidence graph is the Gray graph. The graph here is its first higher-dimensional, nonregular point–axis-line extension. Bouwer's 1968 graph paper and the standard Gray-graph references describe the earlier \(54\)-vertex graph, not the present dedicated-control count. Burgarth, D'Alessandro, Hogben, Severini, and Young (2011) show that zero forcing suffices for linear network controllability, but they explicitly note that the converse is false. Yuan and collaborators (2013) establish the eigenvalue-multiplicity bound for unrestricted control matrices; that bound by itself does not establish coordinate attainability, as the present \(43\)-versus-\(59\) distinction shows. Triantafillou's 2014 thesis discusses maximum nullity and zero forcing for the ordinary Gray graph; only its public abstract was inspectable, so full-thesis priority remains a caveat. No assertion is made about all four-dimensional actuator placements, arbitrary weights, or higher dimensions.

## Limitations

This proves one exact finite-graph optimum and supplies one attaining placement. It does not classify every optimum or prove a formula for all higher-dimensional point–line incidence graphs. Literature search is not a proof of worldwide novelty; an inaccessible thesis and unindexed specialist treatments remain possible priority risks. The rank checks are algebraic certificates for the stated \(189\)-vertex graph, not a substitute for a parameter-uniform infinite-family theorem.

## References

- D. Burgarth, D. D'Alessandro, L. Hogben, S. Severini, and M. Young, *Zero forcing, linear and quantum controllability for systems evolving on networks*, first public preprint 7 November 2011, https://arxiv.org/abs/1111.1475.
- Z. Yuan, C. Zhao, Z. Di, W.-X. Wang, and Y.-C. Lai, *Exact controllability of complex networks*, *Nature Communications* 4 (2013), 2447, published 12 September 2013, https://doi.org/10.1038/ncomms3447.
- I. Z. Bouwer, *An edge but not vertex transitive cubic graph*, *Canadian Mathematical Bulletin* 11 (1968), 533–535, https://doi.org/10.4153/CMB-1968-063-0.
- I. G. Triantafillou, *Singular graphs and the energy of singular graphs*, doctoral thesis, 2014, https://doi.org/10.26240/heal.ntua.1353.
- *Gray graph*, graph construction and spectrum, https://jaanos.github.io/tables/graphs/Gray.html.
