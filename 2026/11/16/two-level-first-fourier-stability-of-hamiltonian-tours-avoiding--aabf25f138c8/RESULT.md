# Two-level first-Fourier stability of Hamiltonian tours avoiding one edge

## Finding

Let \(n\ge6\) be an integer and let \(f=\{a,b\}\) be any edge of the complete undirected graph \(K_n\). Choose uniformly from the undirected Hamiltonian cycles \(H\) not using \(f\). Write \(E'=E(K_n)\setminus\{f\}\), \(X_e(H)=\mathbf1_{\{e\in H\}}\), and \(\chi_e(H)=(-1)^{X_e(H)}=1-2X_e(H)\). Let \(G\) be the covariance Gram matrix of the centered first-coordinate Walsh characters \(\chi_e-\mathbb E\chi_e\), indexed by \(E'\), with the uniform probability inner product on these tours.

The complete spectrum of \(G\), counting multiplicities, is

\[
\begin{array}{c|c}
\text{eigenvalue} & \text{multiplicity}\\ \hline
0 & n\\[2pt]
\dfrac{8(n-4)}{(n-3)^2} & 2(n-3)\\[6pt]
\dfrac{8(n-4)}{(n-2)(n-3)} & \dfrac{(n-2)(n-5)}2.
\end{array}
\]

Consequently, the centered Walsh system has exactly the \(n\) independent deterministic vertex-degree constraints, and its **sharp squared frame condition number on the orthogonal complement of those constraints** equals

\[
\boxed{\kappa_n=\frac{n-2}{n-3}}.
\]

Equivalently, for every real coefficient vector \(c\) perpendicular to the vertex-star constraints, the sharp bounds are \(\lambda_{\min}\|c\|^2\le\mathbb E|\sum_{e\in E'}c_e(\chi_e-\mathbb E\chi_e)|^2\le\lambda_{\max}\|c\|^2\), where \(\lambda_{\min}\) and \(\lambda_{\max}\) are the two positive eigenvalues displayed above. The two positive eigenvalues coalesce asymptotically, with \(\kappa_n\searrow1\). More sharply, the larger eigenvalue has *two distinct* \((n-3)\)-dimensional symmetry sectors with exactly the same value, although exclusion of \(f\) breaks the full vertex-permutation symmetry. No statement concerns arbitrary weighted tour measures or nonuniform edge exclusions.

## Assumptions and scope

The vertex labels are fixed, but changing the particular excluded edge only permutes the Gram matrix. Hamiltonian cycles are undirected; each cycle is counted once, not with an orientation or a starting point. There are exactly \((n-2)!(n-3)/2\) such cycles. All norms and eigenvalues are real, and the Gram matrix is probability-normalized, without dividing by the number of features. The uncentered constant-plus-coordinate frame is a different operator; the theorem specifically concerns the centered first-order Fourier band on the Boolean edge cube, restricted to the forbidden-edge tour ensemble. The restriction \(n\ge6\) guarantees that both nonzero levels occur with positive multiplicity.

## Proof

**1. Exact tour moments from path contractions.** For \(n\ge4\), an edge set \(F\) with \(k\) edges forming a disjoint union of \(c\) nontrivial paths occurs in a uniformly chosen undirected Hamiltonian cycle with probability

\[
\Pr(F\subseteq H)=\frac{2^c(n-k-1)!}{(n-1)!},
\]

provided \(k<n\). To see this, contract each path component into one vertex; a Hamiltonian tour of the resulting \(n-k\) blocks has \((n-k-1)!/2\) undirected orders, and each contracted path admits two orientations. For forbidden stars or short cyclic components the joint occurrence probability is zero (the formulas used below involve only configurations of at most three edges). Conditioning on \(X_f=0\) yields, for every set \(F\) disjoint from \(f\),

\[
\Pr(F\subseteq H\mid X_f=0)=
\frac{\Pr(F\subseteq H)-\Pr(F\cup\{f\}\subseteq H)}{1-2/(n-1)}.
\]

Set \(r=n-2\), and let \(R=V(K_n)\setminus\{a,b\}\). Index the allowed edges as \(A_i=\{a,i\}\), \(B_i=\{b,i\}\) for \(i\in R\), and \(D_{ij}=\{i,j\}\) for distinct \(i,j\in R\). Direct substitution of the displayed contraction counts gives the following conditional first and second moments (all unspecified indices are distinct):

\[
\begin{aligned}
\mathbb EA_i&=\mathbb EB_i=\frac2r,
&\mathbb EA_iA_j&=\mathbb EA_iB_i=\frac2{r(r-1)},\\
\mathbb EA_iB_j&=\frac{4r-6}{r(r-1)^2}\quad(i\ne j),
&\mathbb ED_{ij}&=\frac{2(r-2)}{r(r-1)},\\
\mathbb ED_{ij}D_{i\ell}&=\frac{2(r-3)}{r(r-1)^2},
&\mathbb ED_{ij}D_{k\ell}&=\frac{4(r-3)}{r(r-1)^2}\quad(\{i,j\}\cap\{k,\ell\}=\varnothing).
\end{aligned}
\]

These exact moments, together with the deterministic degree identities, suffice to diagonalize the covariance; no sampling approximation is involved.

**2. Decompose the edge-coordinate space.** Let \(Q\) be the \(r\)-by-\(\binom r2\) unsigned vertex-edge incidence matrix of \(K_r\). For a vector of allowed edge coefficients write \((u,v,w)\), corresponding to the \(A\), \(B\), and \(D\) edges. For every tour,

\[
\sum_{i\in R}X_{A_i}=\sum_{i\in R}X_{B_i}=2,
\qquad X_{A_i}+X_{B_i}+\sum_{j\in R\setminus\{i\}}X_{D_{ij}}=2.
\]

Thus the \(n=r+2\) vertex-star coefficient vectors lie in the covariance kernel. They are linearly independent for \(n\ge6\), because the unsigned incidence matrix of the nonbipartite connected graph \(K_n-f\) has rank \(n\).

Put \(\mathbf1^\perp=\{u\in\mathbb R^r:\sum_i u_i=0\}\). Three mutually orthogonal coefficient subspaces, each perpendicular to all star vectors, are

\[
\begin{aligned}
W_-&=\{(u,-u,0):u\in\mathbf1^\perp\},\\
W_+&=\bigl\{(u,u,-\tfrac2{r-2}Q^{\mathsf T}u):u\in\mathbf1^\perp\bigr\},\\
W_D&=\{(0,0,w):Qw=0\}.
\end{aligned}
\]

The identity \(QQ^{\mathsf T}=(r-2)I+J\) shows that their dimensions are respectively \(r-1\), \(r-1\), and \(r(r-3)/2\). Together with the \(n\)-dimensional star space, they fill all \(2r+\binom r2=\binom n2-1\) allowed coordinates. The conditional law is invariant under permutations of \(R\) and under swapping \(a,b\); hence its symmetric covariance preserves the standard opposite/same endpoint contrast sectors \(W_-\) and \(W_+\). The last sector \(W_D\) is also invariant: for a fixed endpoint edge, its covariance with an internal edge depends only on whether the two edges meet, and both corresponding sums against a vector \(w\in\ker Q\) vanish. The internal edge block preserves \(\ker Q\) by its two intersection classes. No other nontrivial standard symmetry sector remains after quotienting the vertex stars, so the two displayed endpoint sectors are scalar covariance blocks. Their eigenvalues can thus be found from conditional moments and degree constraints.

**3. Identical endpoint-contrast eigenvalues.** On the zero-sum interior contrast space, the \(A\)-block covariance acts by

\[
\alpha=\mathbb EA_i-\mathbb EA_iA_j
=\frac{2(r-2)}{r(r-1)},
\]

while the \(A\)-to-\(B\) covariance acts by

\[
\beta=\mathbb EA_iB_i-\mathbb EA_iB_j
=-\frac{2(r-2)}{r(r-1)^2}.
\]

The \(W_-\) eigenvalue is \(\alpha-\beta=2(r-2)/(r-1)^2\). For \(u\in\mathbf1^\perp\), the degree constraints show that the score associated with a \(W_+\) coefficient vector is, up to a deterministic constant,

\[
\big\langle (u,u,-\tfrac2{r-2}Q^{\mathsf T}u),X\big\rangle
=\frac r{r-2}\langle u,A+B\rangle+\text{constant}.
\]

Its squared coefficient norm is \(2r\|u\|^2/(r-2)\), whereas \(\operatorname{Var}\langle u,A+B\rangle=2(\alpha+\beta)\|u\|^2\). Its covariance eigenvalue is therefore

\[
\frac{r(\alpha+\beta)}{r-2}=\frac{2(r-2)}{(r-1)^2},
\]

**exactly the same** as for \(W_-\). This unexpected equality is why the reduced spectrum has two rather than three positive levels.

**4. The internal edge-flow eigenvalue.** For \(w\in\ker Q\), every internal vertex sum is zero, so for a fixed internal edge \(e\) the sum of \(w\) over other internal edges sharing a vertex with \(e\) is \(-2w_e\), and the sum over edges disjoint from \(e\) is \(w_e\). Using the moment table and the zero total sum of \(w\), covariance acts on \(W_D\) by

\[
\frac{2(r-2)}{r(r-1)}
-2\frac{2(r-3)}{r(r-1)^2}
+\frac{4(r-3)}{r(r-1)^2}
=\frac{2(r-2)}{r(r-1)}.
\]

This is positive for \(r\ge4\). Both covariance values are therefore positive, and all \(n\) star constraints are the entire nullspace by the dimension count.

**5. Normalize Walsh characters and optimize.** Centering \(\chi_e=1-2X_e\) multiplies the entire covariance matrix by \(4\). Multiplying the two positive levels by four and replacing \(r=n-2\) gives the stated complete Walsh Gram spectrum and multiplicities. Their ratio is

\[
\kappa_n=
\frac{2(r-2)/(r-1)^2}{2(r-2)/(r(r-1))}
=\frac r{r-1}=\frac{n-2}{n-3},
\]

which is the exact largest-to-smallest positive squared-norm frame ratio; both extrema are realized by explicit nonzero vectors in the listed sectors. This completes the proof for all integers \(n\ge6\).

## Verification

Run `python3 checker.py` using only Python's standard library. The checker enumerates **every** undirected Hamiltonian cycle avoiding the fixed edge in each order \(n=6,7,8,9\), constructs the full covariance using `fractions.Fraction`, and verifies all star-null equations and all three families of exact eigenvector equations. It additionally checks the trace and the dimension count. Its final line is `FORBIDDEN_HAMILTONIAN_TOUR_FOURIER_FRAME_EXACT_PASS`; individual-order output gives the exact rational eigenvalues and multiplicities. This is finite corroboration of the separately supplied all-order proof, not a substitute for it.

## Relationship to prior work

Fickus and Schmitt [1] develop harmonic tight-frame constructions from finite difference sets; their Fourier-frame motivation does not give the incidence covariance of a restricted Hamiltonian-tour ensemble. Gutekunst and Williamson [2] develop inequalities for the symmetric traveling-salesperson polytope and cite its classical full dimension \(\binom n2-n\). These degree constraints and polyhedral dimensions are established prior work. They do not determine the conditional second-moment operator or its exact positive eigenvalues after excluding one edge.

A separately published result on **directed** Hamiltonian tours [3] analyzes unrestricted directed arc-Walsh covariance and determinant-optimal bases. Its sampling ensemble, feature set, and probability law differ: the present undirected single-edge-exclusion spectrum requires joint moments of up to three undirected edges and is not a consequence of that directed result's stated eigenvalues. A related complete first-Walsh Gram spectrum for **uniform labelled unicyclic graphs** [4] concerns graphs with arbitrary tree attachments, not a uniform Hamiltonian-cycle subensemble, and has only one fixed-edge-count null direction. Its spectral formulas cannot be specialized to the tours avoiding an edge merely by replacing parameters. Standard graph incidence theory underlies our decomposition, but the cancellation giving one common eigenvalue to two different standard symmetry sectors is the additional specific assertion here.

## Limitations

This theorem treats centered first-degree edge Walsh characters and **uniform** undirected Hamiltonian cycles avoiding exactly one edge. It does not describe the full higher-degree Fourier transform, arbitrary support weights, multiple forbidden edges, uncentered constant-plus-edge Gram matrices, or optimization over choice of a noncanonical feature subset. It establishes an exact internal Riesz/frame bound after quotienting deterministic constraints; including those constraints gives a singular matrix. The proof and finite rational tests are not an independent mathematical audit. Although searches located no identical conditional spectrum, historic incidence-moment or TSP covariance calculations may conceal an equivalent formula; historical priority is not independently certified.

## References

[1] M. Fickus and C. A. Schmitt, “Harmonic equiangular tight frames comprised of regular simplices,” arXiv:1903.09177, first public version 2019-03-21, MSC 42C15. https://arxiv.org/abs/1903.09177

[2] S. C. Gutekunst and D. P. Williamson, “The Circlet Inequalities: A New, Circulant-Based Facet-Defining Inequality for the TSP,” arXiv:2012.12363, first public version 2020-12-22. https://arxiv.org/abs/2012.12363

[3] “Equal-volume Walsh coordinate bases on directed Hamiltonian tours,” published published-finding corpus mathematical record, 2026-11-02. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-equal-volume-walsh-coordinate-bases-on-directed-hamiltonian-tour--984ab6d11231

[4] “Exact centered Walsh stability for uniform labelled unicyclic graphs,” published published-finding corpus mathematical record, 2026-11-01. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-centered-walsh-stability-for-uniform-labelled-unicyclic-gr--191cfc31fb25
