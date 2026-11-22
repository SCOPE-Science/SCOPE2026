# Parity classification and sharp Fourier gaps for spanning trees of generalized theta graphs

## Finding
Let \(k\ge3\), and let \(G=\Theta_{\ell_1,\ldots,\ell_k}\) be the **simple** graph formed from two distinct terminals joined by \(k\) internally vertex-disjoint paths \(P_i\), each containing \(\ell_i\ge2\) edges. Put \(m=\sum_i\ell_i\) and \(B=\mathbb F_2^{E(G)}\). Let \(f:B\to\{0,1\}\) indicate the edge-incidence vectors of the spanning trees of \(G\). Convolution is unnormalized: \(Tg(x)=\sum_{y\in B} f(y)g(x+y)\).

For a frequency \(\xi\in B\), put \(j_i=|\{e\in P_i:\xi_e=1\}|\) and \(u_i=\ell_i-2j_i\). Define the elementary symmetric expression
\[
e_{k-1}(u_1,\ldots,u_k)=\sum_{i=1}^k\prod_{h\ne i}u_h.
\]
The **complete signed Fourier multiplier** is
\[
\boxed{\widehat f(\xi)=(-1)^{\sum_i j_i}e_{k-1}(u_1,\ldots,u_k).}
\tag{1}
\]
Let \(s=|\{i:\ell_i\text{ is even}\}|\). Then
\[
\boxed{T\text{ is invertible}\quad\Longleftrightarrow\quad s=1\ \text{or}\ (s=0\text{ and }k\text{ is odd}).}
\tag{2}
\]
The smallest **strictly positive singular value** of \(T\), including when \(T\) is singular, is exactly
\[
\boxed{\sigma^+_{\min}(T)=
\begin{cases}
1,&s=1\text{ or }(s=0\text{ and }k\text{ odd}),\\
2,&s=0\text{ and }k\text{ even},\\
2^{s-1},&s\ge2.
\end{cases}}
\tag{3}
\]
Its largest singular value equals the number of spanning trees,
\[
\tau(G)=e_{k-1}(\ell_1,\ldots,\ell_k),
\]
so its sharp spectral condition number on the recoverable Fourier subspace is \(\tau(G)/\sigma^+_{\min}(T)\).

The **complete multiplier multiplicity function**, with no assumption of distinct values, is the exact finite formula
\[
M_t=\sum_{j_1=0}^{\ell_1}\cdots\sum_{j_k=0}^{\ell_k}
\left(\prod_{i=1}^k\binom{\ell_i}{j_i}\right)
\mathbf 1\left\{(-1)^{\sum_i j_i}e_{k-1}(\ell_1-2j_1,\ldots,\ell_k-2j_k)=t\right\}.
\tag{4}
\]
In particular \(\operatorname{nullity}(T)=M_0\) and \(\operatorname{rank}(T)=2^m-M_0\). These are exact finite all-parameter formulas; no further closed expression for arbitrary path lengths is asserted.

## Assumptions and scope
All graphs are finite, undirected, loopless and simple. The path interiors are pairwise disjoint and no path is a direct terminal edge. Edges are distinctly labelled. All spanning-tree incidence vectors and Fourier frequencies live in the **full** group \(B\), not in a quotient by graph automorphisms, the cycle space, or the spanning-tree affine hull. Fourier coefficients are unnormalized, with character \((-1)^{\langle\xi,x\rangle}\). Singular values are for counting-measure \(\ell^2(B)\). No statement is made about the communication complexity of the associated XOR function.

## Proof
**1. Enumerate spanning trees by deleted edges.** The graph has \(m-k+2\) vertices, hence a spanning tree has \(m-k+1\) edges and deletes exactly \(k-1\) edges. Since internal vertices of each path have degree two and must remain connected, at most one edge can be deleted from a given path. Two intact paths would create a cycle; no intact path would disconnect the two terminals. Thus exactly one entire path is retained and exactly one edge is deleted from each other path. Conversely, every such deletion pattern produces a spanning tree. Therefore the total number is \(\tau(G)=\sum_i\prod_{h\ne i}\ell_h\).

**2. Evaluate every character.** Give edge \(e\) the sign \(w_e=(-1)^{\xi_e}\). The sign of a spanning-tree incidence vector is \(\prod_{e\in T}w_e\). Let \(W=\prod_{e\in E(G)}w_e=(-1)^{\sum_i j_i}\). Deleting one edge of a path replaces \(W\) by \(W/w_e=Ww_e\). Independence of the deletion choices in the previous paragraph gives
\[
\widehat f(\xi)=W\sum_{i=1}^{k}\prod_{h\ne i}\left(\sum_{e\in P_h}w_e\right)
=(-1)^{\sum_i j_i}e_{k-1}(u_1,\ldots,u_k),
\]
proving (1). There are \(\binom{\ell_i}{j_i}\) possible edge sign patterns with the designated \(j_i\) in arm \(i\); grouping all frequencies accordingly gives (4).

**3. Determine precisely when a Fourier zero exists.** If \(s=1\), every summand of \(e_{k-1}\) contains the other \(k-1\) odd \(u_i\) except the single summand omitting the even \(u_i\); therefore \(e_{k-1}\) is odd, never zero. If \(s=0\), every \(u_i\) is odd and each of the \(k\) summands is odd. When \(k\) is odd their sum is odd and cannot vanish. When \(k\) is even, choose \(u_i\in\{1,-1\}\) with equally many signs of either kind. This is possible because each \(\ell_i\) is odd. Then
\[
e_{k-1}(u)=\left(\prod_i u_i\right)\sum_i u_i=0.
\]
If \(s\ge2\), choose \(u_i=0\) for two even-length arms (possible by putting exactly half of their edge frequencies equal to one). Every product of \(k-1\) arms includes at least one zero and hence vanishes. These cases prove (2).

**4. Prove all sharp nonzero singular gaps.** In the two invertible regimes of (2), the multipliers are nonzero odd integers. If \(s=1\), take its even-length arm sum zero and all odd-length arm sums one; this makes \(e_{k-1}=1\). If \(s=0\) and \(k\) is odd, choose all \(u_i\in\{1,-1\}\) so their sum is one; the product-times-sum identity gives \(|e_{k-1}|=1\). If \(s=0\) and \(k\) is even, \(e_{k-1}\) is a sum of an even number of odd terms, hence is even; choose signs with \(\sum_i u_i=2\) to attain modulus two. Finally, if \(s\ge2\), each summand contains at least \(s-1\) even factors, so every multiplier is divisible by \(2^{s-1}\). Select one even arm sum zero, every other even arm sum two and every odd arm sum one; exactly one summand survives and has absolute value \(2^{s-1}\). Since all chosen values lie within the permitted parity/size ranges, all these constructions are valid frequencies. This proves (3).

**5. Spectral extrema and rank.** Characters form an orthogonal basis of \(\ell^2(B)\) and diagonalize convolution by \(f\), with eigenvalues \(\widehat f(\xi)\). Because these eigenvalues are real, their magnitudes are its singular values. The triangle inequality gives \(|\widehat f(\xi)|\le\tau(G)\), with equality at the zero frequency. Formula (4) counts all frequencies and therefore proves rank, nullity and the stated sharp recoverable-space condition number.

## Verification
The included standard-library program `verify_theta_spectrum.py` independently constructs generalized theta graphs and enumerates spanning trees using a disjoint-set connectivity and cycle test, rather than the deleted-edge formula. It Walsh–Hadamard transforms the entire incidence indicator, checks every coefficient against (1), checks the full signed multiplicities against the compressed formula (4), verifies Parseval's identity, and compares the exact ranks and least positive multipliers to (2)–(3). A total of **106** small path-length configurations passed, including \((2,2,2)\), \((2,2,3)\), \((2,3,3)\), \((3,3,3,3)\) and up to six arms. Run `python3 verify_theta_spectrum.py`. The general theorem is established by Steps 1–5, not by finite testing.

## Relationship to prior work
Brown, Hickman, Sokal and Wagner (2000) established chromatic-polynomial and chromatic-root theory of generalized theta graphs; their full Section 2 includes the graph definition and a chromatic-polynomial factorization, but does not evaluate the spanning-tree incidence Walsh transform. The weighted Potts/Tutte framework cited there and the general weighted matrix-tree theorem can, in principle, encode signed spanning-tree sums; the explicit **Fourier-zero parity classification and sharp positive gap** require the further integer argument in Steps 3–4.

Previously published analyses of the spanning trees of \(K_{2,n}\) give their complete Walsh spectrum for the **all-arms-length-two subfamily**, which is already covered and is not presented as separately new. Previously published generalized-theta orientation-flip results give the unweighted spanning-tree count and a deletion description; these are used as background rather than claimed as a new enumeration. Those works do not give the all-length and all-number-of-paths spectral criterion (2) or sharp gaps (3). General XOR-matrix rank identities supply the diagonalization bridge, not these graph-specific coefficients or their zero structure.

## Limitations
The analysis covers simple generalized theta networks with at least three paths, each of length at least two. It does not give an elementary one-line closed nullity expression for arbitrary unequal lengths beyond the finite multiplicity sum (4), nor does it provide full \(\ell^p\) Fourier-projection norms or any analogous theorem for general series-parallel graphs. The mathematical proof and exact checks here have not been independently validated. Published-priority inspection is bounded; an equivalent theorem could appear under signed spanning-tree or multivariate Tutte terminology.

## References
1. J. Brown, C. Hickman, A. D. Sokal, D. G. Wagner, *On the chromatic roots of generalized theta graphs*, arXiv:math/0012033v1, first public posting 2000-12-05. https://arxiv.org/html/math/0012033v1
2. A. Goodall, *Fourier Analysis on Finite Abelian Groups: Some Graphical Applications*, in *Combinatorics, Complexity, and Chance* (2007), DOI 10.1093/acprof:oso/9780198571278.003.0007. https://www.researchgate.net/publication/266250848_Fourier_Analysis_on_Finite_Abelian_Groups_Some_Graphical_Applications
3. H. Y. Tsang, C. H. Wong, N. Xie, S. Zhang, *Fourier sparsity, spectral norm, and the Log-rank conjecture*, arXiv:1304.1245v2 (2013). https://arxiv.org/html/1304.1245v2
4. *Complete Walsh spectrum and sharp Fourier projection norms for the spanning trees of \(K_{2,n}\)*, published result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-complete-walsh-spectrum-and-sharp-fourier-projection-norms-for-t--89f45551846c
5. *Local flip degrees and simple graphical-zonotope vertices of generalized theta graphs*, published result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-local-flip-degrees-and-simple-graphical-zonotope-vertices-of-gen--23a76ec8b64b
