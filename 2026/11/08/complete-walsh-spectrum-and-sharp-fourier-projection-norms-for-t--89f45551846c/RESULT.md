# Complete Walsh spectrum and sharp Fourier projection norms for the spanning trees of \(K_{2,n}\)

## Finding
For every integer \(n\ge2\), let \(K_{2,n}\) have two vertices \(u,v\) on one side and \(n\) vertices \(w_1,\ldots,w_n\) on the other. Let \(E\) be its \(2n\)-edge set, let \(G=\mathbb F_2^E\), and let \(\mathcal T\subseteq G\) be the incidence vectors of all spanning trees. There are \(n2^{n-1}\) such vectors.

The full unnormalized Walsh transform \(W(x)=\sum_{T\in\mathcal T}(-1)^{\langle x,T\rangle}\) has the following disjoint accounting. Associate two signs \(a_i=(-1)^{x_{uw_i}}\) and \(b_i=(-1)^{x_{vw_i}}\) to each right vertex, and let \(t=\#\{i:a_i=-b_i\}\).

* For \(t\ge2\), \(W(x)=0\); this case has \(2^n(2^n-n-1)\) assignments.
* For \(t=1\), \(|W(x)|=2^{n-1}\); this case has \(n2^n\) assignments.
* For \(t=0\), if exactly \(j\) of the \(a_i\) are negative, then \(|W(x)|=2^{n-1}|n-2j|\); this case has \(\binom nj\) assignments, for each \(0\le j\le n\).

The cases are disjoint, although numerical Fourier magnitudes may coincide and must then have their multiplicities added. The exact support cardinality is
\[
|\operatorname{supp}W|=(n+1)2^n-\mathbf1_{2\mid n}\binom{n}{n/2}.
\]

Let \(P_{\mathcal T}\) be the additive Fourier multiplier with frequency mask \(\mathbf1_{\mathcal T}\), acting on functions on \(G\) with counting-measure \(\ell^p\) norms. Then the two sharp endpoint operator norms coincide and are
\[
\boxed{L_n=\|P_{\mathcal T}\|_{\ell^1\to\ell^1}=\|P_{\mathcal T}\|_{\ell^\infty\to\ell^\infty}=\frac n2+\frac{n}{2^n}\binom{n-1}{\lfloor(n-1)/2\rfloor}.}
\]
In particular \(L_n=\frac n2+\sqrt{\frac{n}{2\pi}}+O(n^{-1/2})\). For \(m\ge1\), its parity increments satisfy
\[
L_{2m+2}-L_{2m+1}=\frac12,\qquad L_{2m+1}-L_{2m}=\frac12+\frac{\binom{2m}{m}}{2^{2m+1}}.
\]
For the XOR circulant matrix \(M(x,y)=\mathbf1_{\mathcal T}(x+y)\) on \(G\times G\), its exact rank over \(\mathbb C\) equals \(|\operatorname{supp}W|\).

## Assumptions and scope
The graph is the simple complete bipartite graph \(K_{2,n}\), with \(n\ge2\), and the frequency set consists of distinct **edge-incidence vectors** of all spanning trees. The ambient group has order \(2^{2n}\); the Walsh transform is **unnormalized**, while Fourier inversion and convolution use the factor \(2^{-2n}\). The operator norms use counting measure. The statements concern the specific graphical-matroid basis family, not all graphic or binary matroids.

## Proof
**Spanning-tree parameterization.** Every right vertex \(w_i\) has degree at least one in a spanning tree. A tree has exactly \(n+1\) edges, so the sum of all right degrees is \(n+1\). Exactly one right vertex, say \(w_j\), therefore has degree two; each other \(w_i\) has degree one. Conversely, the two edges at \(w_j\) and an arbitrary choice of one incident edge at every other right vertex form a connected acyclic spanning graph. Distinct choices give distinct trees. Hence there are precisely \(n2^{n-1}\) trees.

**Exact transform.** The contribution of trees with the unique two-edge vertex \(w_j\) is \(a_jb_j\prod_{i\ne j}(a_i+b_i)\), because the remaining single-edge choices separate multiplicatively. Therefore
\[
W(a,b)=\sum_{j=1}^n a_jb_j\prod_{i\ne j}(a_i+b_i).
\]
If there are two or more opposing pairs, every summand contains a zero factor. If exactly one pair is opposed, the only surviving term is its own and has modulus \(2^{n-1}\). If no pair is opposed, then \(b_i=a_i\) for every \(i\), and
\[
W(a,b)=2^{n-1}\left(\prod_{i=1}^n a_i\right)\left(\sum_{j=1}^n a_j\right).
\]
Counting choices of the opposition set and the free signs \(a_i\) proves the full signed-case partition and the claimed absolute-magnitude spectrum. In particular the \(t\ge2\) case has \(2^n\sum_{t=2}^n\binom nt=2^n(2^n-n-1)\) frequencies. At \(t=0\), vanishing requires equal positive and negative signs, possible only for even \(n\) and at exactly \(\binom n{n/2}\) frequencies. Therefore the support count follows. The total spectral multiplicity is \(2^{2n}\), as required.

**Sharp norm.** Fourier inversion makes the projection a convolution with \(K(x)=2^{-2n}W(x)\) (the sign of the argument is immaterial, since Boolean characters are real). Thus \(\|P_{\mathcal T}\|_{1\to1}=\|P_{\mathcal T}\|_{\infty\to\infty}=\sum_x|K(x)|\). The \(\ell^1\) equality is attained on a point mass; the \(\ell^\infty\) equality is attained at the origin by signs matched to nonzero kernel values. By the spectrum count,
\[
L_n=\frac{2^{n-1}}{2^{2n}}\left[n2^n+\sum_{j=0}^n\binom nj|n-2j|\right].
\]
The telescoping identity \((n-2j)\binom nj=n[\binom{n-1}{j}-\binom{n-1}{j-1}]\), with out-of-range coefficients interpreted as zero, implies
\[
\sum_{j=0}^n\binom nj|n-2j|=2n\binom{n-1}{\lfloor(n-1)/2\rfloor}.
\]
Substitution proves the exact sharp norm.

**Parity and asymptotic.** Put \(B_m=2^{-2m}\binom{2m}m\). From the closed norm formula,
\[
L_{2m}=m+mB_m,\quad L_{2m+1}=m+\tfrac12+(m+\tfrac12)B_m,\quad L_{2m+2}=m+1+(m+\tfrac12)B_m.
\]
The two exact increment identities follow by subtraction. The central-binomial estimate \(\binom{2m}m=4^m(\pi m)^{-1/2}(1+O(m^{-1}))\) gives the asymptotic expansion with its stated error.

**XOR rank.** The characters of \(G\) diagonalize the matrix \(M(x,y)=\mathbf1_{\mathcal T}(x+y)\); its eigenvalues are the unnormalized coefficients \(W(x)\), up to indexing. Thus its rank is the number of nonzero Walsh coefficients, already evaluated.

## Verification
The standalone exact-integer program `checks/check_theta.py` creates spanning-tree incidence masks from the degree-two-vertex parameterization, builds their full \(2n\)-bit indicator, and performs an independently implemented Walsh–Hadamard transform. It verifies the complete absolute histograms, the exact first absolute moment, Parseval's identity, tree counts, and support formulas, for each \(2\le n\le8\). Its final success marker is `THETA_K2N_FULL_FOURIER_CERTIFICATE_PASS`. All-depth results above are proved symbolically; the finite tests are consistency checks only.

## Relationship to prior work
Kirchhoff's matrix-tree method and standard enumerations give the number of spanning trees, but a cardinality by itself cannot determine the absolute Walsh spectrum or a sharp Fourier projection norm. Goodall's survey develops Fourier analysis in graph theory and counts spanning trees of **Cayley graphs** through adjacency spectra; the present object instead Fourier-transforms the **set of spanning-tree incidence vectors** of one bipartite graph. Dong and Ge count spanning trees of complete bipartite graphs containing a prescribed forest; their general theorem can in principle enter an inclusion–exclusion calculation of any signed tree sum, but it does not evaluate the distribution of such sums over all signs or the sharp norm. Tsang and coauthors consider Fourier sparsity, spectral norm, and the rank of XOR matrices for general Boolean functions, but do not determine these quantities for the graphical basis indicator. The displayed distribution, endpoint norm, and parity increments are the distinct contribution compared against this background.

## Limitations
Only the complete bipartite family \(K_{2,n}\) is treated. The formula does not imply corresponding norms for \(K_{3,n}\), other theta networks, or arbitrary graphic matroids. It gives the exact XOR matrix rank, not its deterministic communication complexity. The proof is a self-review and has not received independent mathematical validation. Published-priority searches were bounded; an unlocated specialized weighted-tree enumeration could contain an equivalent result.

## References
1. Ronald de Wolf, *A Brief Introduction to Fourier Analysis on the Boolean Cube*, Theory of Computing Library, Graduate Surveys 1 (2008), published September 25, 2008. DOI: 10.4086/toc.gs.2008.001. https://toc1234.cs.uchicago.edu/articles/gs001/
2. Andrew Goodall, *Fourier Analysis on Finite Abelian Groups: Some Graphical Applications*, in *Surveys in Combinatorics* (2007), DOI: 10.1093/acprof:oso/9780198571278.003.0007. https://www.researchgate.net/publication/266250848_Fourier_Analysis_on_Finite_Abelian_Groups_Some_Graphical_Applications
3. Hing Yin Tsang, Chung Hoi Wong, Ning Xie, Shengyu Zhang, *Fourier sparsity, spectral norm, and the Log-rank conjecture*, arXiv:1304.1245, first submitted April 4, 2013. https://arxiv.org/abs/1304.1245
4. Fengming Dong and Jun Ge, *Counting spanning trees in a complete bipartite graph which contain a given spanning forest*, arXiv:2103.05294, first submitted March 9, 2021. https://arxiv.org/abs/2103.05294
