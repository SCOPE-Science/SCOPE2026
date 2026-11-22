# Square-order Walsh resonances for unicyclic \(K_{2,n}\) subgraphs and fixed-excess spectra

## Finding
For integers \(n\ge 2\) and \(2\le j\le n\), let \(B_{n,j}\) be the edge-incidence vectors of connected spanning subgraphs of the labelled complete bipartite graph \(K_{2,n}\) having exactly \(n+j\) edges. A member thus has cycle-space dimension \(j-1\). Let \(f_{n,j}=\mathbf1_{B_{n,j}}\) on \(G_n=(\mathbb F_2)^{2n}\), and use the **unnormalized** Walsh transform \(W_{n,j}(\xi)=\sum_{x\in G_n}f_{n,j}(x)(-1)^{\langle \xi,x\rangle}\).

For each frequency, write the signs on the two edges incident with right vertex \(i\) as \(a_i,b_i\in\{-1,1\}\). Let \(d\) be the number of indices with \(a_i\ne b_i\), and let \(h\) be the number of indices with \(a_i=b_i=-1\). Define the binary Krawtchouk polynomial by
\[
K_r(h;m)=\sum_{t=0}^{r}(-1)^t\binom{h}{t}\binom{m-h}{r-t},
\]
with out-of-range binomial coefficients zero. Then the **complete signed spectrum** is
\[
W_{n,j}(\xi)=
\begin{cases}
(-1)^{d+h}2^{n-j}K_{j-d}(h;n-d),&0\le d\le j,\\
0,&d>j.
\end{cases}
\]
Every signed value specified by \((d,h)\) has parameter multiplicity \(2^d\binom nd\binom{n-d}{h}\); values coinciding numerically have their multiplicities added. Equivalently, the exact rank of convolution by \(f_{n,j}\) is
\[
\operatorname{rank}T_{n,j}
=\sum_{d=0}^{j}2^d\binom nd\sum_{h=0}^{n-d}\binom{n-d}{h}\mathbf1_{\{K_{j-d}(h;n-d)\ne0\}}.
\]
Its smallest strictly positive singular value is **exactly** \(2^{n-j}\), its largest is \(2^{n-j}\binom nj\), and its sharp condition number on the nonzero Fourier subspace is \(\binom nj\). In particular \(T_{n,j}\) is invertible precisely at the full-edge endpoint \(j=n\).

For the first genuinely cyclic extension beyond spanning trees, \(j=2\), the nullity has a closed arithmetic formula. With \(s=\sqrt n\) only when \(n\) is a perfect square,
\[
\boxed{\begin{aligned}
\operatorname{rank}T_{n,2}
={}&2^n\left(1+n+\binom n2\right)\\
&-\mathbf1_{\{n\ \mathrm{odd}\}}\,2n\binom{n-1}{(n-1)/2}\\
&-\mathbf1_{\{n\ \mathrm{square}\}}\,2\binom{n}{(n-s)/2},\\
\operatorname{nullity}T_{n,2}={}&4^n-\operatorname{rank}T_{n,2}.
\end{aligned}}
\]
Beyond the forced zeros with \(d\ge3\), there are *exactly two independent arithmetic resonance mechanisms*: \(d=1\) contributes zeros precisely for odd \(n\), whereas \(d=0\) contributes additional zeros precisely at perfect-square \(n\). The square resonance has multiplicity \(2\binom{n}{(n-\sqrt n)/2}\), even when \(n\) is also odd. At every \(n\ge2\), the positive spectral condition number for these unicyclic graph supports is \(\binom n2\).

## Assumptions and scope
The graph has two labelled vertices on one side and \(n\) labelled vertices on the other, with one edge between each opposite-side pair. Its ambient Boolean edge space has size \(4^n\). Each incidence vector represents a different subgraph. Convolution is counting-measure convolution \((T_{n,j}g)(x)=\sum_{y\in G_n}f_{n,j}(y)g(x-y)\). As it is diagonalized by the unitary character basis, its singular values are the absolute unnormalized Walsh multipliers. The \(j=1\) spanning-tree case is previously known and is **not** claimed as new; the result asserts \(j\ge2\).

## Proof
**Connected fixed-excess subgraphs.** Every right vertex must have degree one or two in any connected spanning subgraph. If exactly \(j\) right vertices have degree two, the graph has \(n+j\) edges. Since \(j\ge1\), the two left vertices are joined by a two-edge path, and every other right vertex attaches to one of them, so the subgraph is connected. Conversely every connected spanning subgraph with \(n+j\) edges arises uniquely this way. Thus \(|B_{n,j}|=\binom nj2^{n-j}\).

**Signed multiplier.** Fix the set \(J\) of doubled right vertices, \(|J|=j\). Summing the single-edge choices at the other vertices gives
\[
W_{n,j}(a,b)=\sum_{\substack{J\subseteq\{1,\ldots,n\}\\|J|=j}}\prod_{i\in J}a_ib_i\prod_{i\notin J}(a_i+b_i).
\]
A discordant index \(a_i=-b_i\) must belong to \(J\), hence the sum is zero if \(d>j\). If \(d\le j\), let \(D\) be the set of discordant indices and write \(J=D\cup L\), where \(L\) is a \((j-d)\)-subset of the concordant indices. At discordant indices \(a_ib_i=-1\); at concordant ones \(a_i=b_i\) and \(a_ib_i=1\). The \(n-j\) remaining single-edge indices each contribute \(2a_i\). Consequently
\[
W_{n,j}=(-1)^d2^{n-j}\left(\prod_{i\notin D}a_i\right)
\sum_{\substack{L\subseteq D^c\\|L|=j-d}}\prod_{i\in L}a_i.
\]
There are \(h\) negative concordant signs, so the product is \((-1)^h\), and the last sum is precisely \(K_{j-d}(h;n-d)\). This proves the displayed multiplier formula. For given \((d,h)\), choose the \(d\) discordant positions, their \(2^d\) sign orientations, and the \(h\) negative concordant positions; this proves the multiplicities and exact rank formula.

**Sharp singular bounds.** Every Krawtchouk value is an integer, so every nonzero Walsh coefficient has modulus at least \(2^{n-j}\). Taking \(d=j\) forces \(K_0=1\), giving equality. The triangle inequality bounds every coefficient by the number \(|B_{n,j}|=\binom nj2^{n-j}\), and the trivial character attains equality. Therefore the smallest and largest positive singular values and their ratio are exact. If \(j<n\), there exist characters with \(d=j+1\), hence zero coefficients; if \(j=n\), the indicator is that of the sole full-edge graph and its Walsh transform has modulus one everywhere. This proves the invertibility statement, including the endpoint.

**Square and parity zero sets when \(j=2\).** For \(d=2\), \(K_0=1\). For \(d=1\), \(K_1(h;n-1)=n-1-2h\), whose unique integer root exists precisely when \(n\) is odd; it has \(2n\binom{n-1}{(n-1)/2}\) corresponding frequencies. For \(d=0\),
\[
K_2(h;n)=\frac{(n-2h)^2-n}{2}.
\]
It vanishes exactly when \(n=s^2\) and \(h=(n\pm s)/2\); these are two distinct valid integers for every square \(n\ge4\), producing \(2\binom{n}{(n-s)/2}\) frequencies. The cases \(d=0\) and \(d=1\) are disjoint even for odd squares. In each fixed \(d\), all \(2^d\binom nd2^{n-d}=2^n\binom nd\) sign assignments occur, so the initial nonforced count for \(d\le2\) is \(2^n(1+n+\binom n2)\). Subtraction gives the rank and nullity formulas. The \(n=2\) boundary has no square correction and is invertible, as the only admissible support vector is the complete edge set.

## Verification
The standalone standard-library program `checks/check_unicyclic.py` builds the actual incidence-set indicator for every \(2\le n\le8\) and every \(1\le j\le n\), performs an independently coded integer Walsh–Hadamard transform, and verifies the signed multiplier formula at every one of its \(4^n\) frequencies. It also checks divisibility, the sharp two positive spectral extrema, and the unicyclic rank formula. The program reported 2,009,837 successful assertions. Its \(j=1\) tests serve only as normalization regression against known results, not as a novel claim. The unrestricted results are established by the preceding algebraic proof; finite checks are corroborative only.

## Relationship to prior work
Goodall's 2007 graphical Fourier survey supplies the basic finite-group character calculus and the Krawtchouk transform of a Hamming shell. Mizukawa's 2010 work develops orthogonality of multivariate Krawtchouk polynomials. The prior published published-finding corpus theorem *Complete Walsh spectrum and sharp Fourier projection norms for the spanning trees of \(K_{2,n}\)* gives the \(j=1\) slice, including its support size and endpoint norm; the present \(j\ge2\) statement is not a relabeling of that slice. The general Krawtchouk machinery is used openly, rather than claimed as a new family of polynomials. The new contribution is its uniform fixed-cycle-excess graph-spectrum identification, exact all-\(j\) positive conditioning and full unicyclic nullity classification with separate odd-order and square-order resonances. The ordinary network-reliability count \(|B_{n,j}|\) is classical and by itself does not determine signed multipliers or their zeros.

## Limitations
The theorem concerns only \(K_{2,n}\) and the Boolean additive edge-incidence group. The general rank formula still involves integer zeros of Krawtchouk polynomials when \(j\ge3\); a closed arithmetic characterization for every such \(j\) is not claimed. This is not an assertion about graph-theoretic adjacency eigenvalues or arbitrary bipartite graphs. The derivation uses elementary identities, and a differently phrased classical signed enumeration may already imply the specialization; historical priority has only been checked against the specifically inspected sources. No independent audit has been performed.

## References
1. Andrew Goodall, *Fourier analysis on finite Abelian groups: some graphical applications*, in *Combinatorics, Complexity, and Chance*, Oxford University Press, chapter 7 (publicly published January 18, 2007), DOI: 10.1093/acprof:oso/9780198571278.003.0007. Author manuscript: https://iuuk.mff.cuni.cz/~andrew/dwajgApr06.pdf
2. Ronald de Wolf, *A Brief Introduction to Fourier Analysis on the Boolean Cube*, Theory of Computing Library Graduate Surveys 1, public September 25, 2008, DOI: 10.4086/toc.gs.2008.001. https://theoryofcomputing.org/articles/gs001/
3. Hiroshi Mizukawa, *Orthogonality Relations for Multivariate Krawtchouk Polynomials*, arXiv:1009.1203, first posted September 7, 2010. https://arxiv.org/abs/1009.1203
4. *Complete Walsh spectrum and sharp Fourier projection norms for the spanning trees of \(K_{2,n}\)*, archived published result, November 8, 2026. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-complete-walsh-spectrum-and-sharp-fourier-projection-norms-for-t--89f45551846c/RESULT.md
