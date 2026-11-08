# Universal Poisson extinction windows for fixed-size components of high-degree regular percolation

## Finding

Fix an integer \(k\ge1\) and a real \(c\). Let \(G_n\) be **any** deterministic simple \(d_n\)-regular graph with exactly \(n\) vertices, where \(d_n/\log n\to\infty\). Let \(H_n\) be its independent bond-percolation subgraph and set

\[
L_n=\log n+(k-1)\log\log n+c,\qquad
p_n=1-\exp(-L_n/(k d_n)).
\]

For sufficiently large \(n\), \(L_n>0\) and \(0<p_n<1\). Denote by \(Z_{n,k}\) the **number of connected components** of \(H_n\) with exactly \(k\) vertices, regardless of their internal cycle structure. Then

\[
\boxed{Z_{n,k}\ \xrightarrow{\mathrm d}\ \operatorname{Poisson}\!\left(\frac{e^{-c}}{k\,k!}\right).}
\]

Consequently,

\[
\boxed{\Pr\{Z_{n,k}=0\}\to \exp\!\left(-\frac{e^{-c}}{k\,k!}\right).}
\]

In particular, at the \(k=2\) window, if \(I_n\) denotes the number of isolated vertices, then

\[
\boxed{\frac{I_n}{e^{-c/2}\sqrt{n/\log n}}\xrightarrow{\mathbb P}1.}
\]

The coefficient \(1/(k\,k!)\), the centering \((k-1)\log\log n\), and the limits do not depend on the geometry, connectivity, expansion, or short cycles of the regular host graph. The case \(k=1\) recovers a universal isolated-vertex Poisson limit; each fixed \(k\ge2\) yields a distinct, earlier extinction window for components of that size.

## Assumptions and scope

The host graphs are simple, undirected, deterministic and regular, with one vertex count parameter \(n\to\infty\) and integer degrees \(1\le d_n\le n-1\) satisfying \(d_n/\log n\to\infty\). The integer \(k\ge1\) and real \(c\) are fixed as \(n\) grows; the result does **not** assert uniformity in growing \(k\). Every host edge is retained independently with the displayed \(p_n\). No other edges are added. No connected-host, transitivity, girth or expansion assumptions are imposed. Disconnected unions of equal-degree blocks are included. All logarithms are natural.

A *tree embedding* means a distinct subgraph with \(k\) distinct host vertices and exactly \(k-1\) host edges forming a tree; embeddings differing only by abstract labels are identified. Let \(q_n=1-p_n\), and let \(T_{n,k}\) count components of \(H_n\) that are trees on exactly \(k\) vertices.

## Proof

**1. Embedded-tree count.** Assume first \(k\ge2\). Cayley's identity gives \(k^{k-2}\) trees on abstract labeled vertices \(1,\ldots,k\). For each such tree, choose the image of one root in \(n\) ways; in tree-order, each next image has between \(d_n-(k-1)\) and \(d_n\) allowed host neighbors, because at most \(k-1\) already-used vertices must be avoided. Thus the number of injective edge-preserving maps is

\[
n d_n^{k-1}\bigl(1+O_k(d_n^{-1})\bigr).
\]

Every embedded (unlabeled) edge-tree has exactly \(k!\) abstract labelings when summed over the abstract labeled trees. The number of distinct host tree embeddings therefore is

\[
B_{n,k}=\frac{k^{k-2}}{k!}\,n d_n^{k-1}\bigl(1+O_k(d_n^{-1})\bigr).
\tag{1}
\]

This argument also holds when finitely many prescribed vertices are excluded: for an excluded set of size at most \(rk\), the same lower and upper root-and-neighbor bounds give \(B_{n,k}(1+O_{k,r}(d_n^{-1}+n^{-1}))\). Hence for every fixed \(r\), the number of ordered \(r\)-tuples of vertex-disjoint tree embeddings is \(B_{n,k}^{r}(1+o(1))\).

**2. A single isolated tree.** For a host tree embedding \(A\) with vertex set \(S\) of size \(k\), let \(h(A)\) be the number of host edges induced by \(S\) in addition to the \(k-1\) tree edges. Always \(0\le h(A)\le\binom{k}{2}-(k-1)\). Since a \(d_n\)-regular host has \(k d_n-(k-1)-h(A)\) distinct edges incident to \(S\), exactly \(k d_n-2(k-1)-h(A)\) other incident edges must be closed to make \(A\) an entire tree component. Its probability is

\[
\Pr(E_A)=p_n^{k-1}q_n^{k d_n-2(k-1)-h(A)}
=p_n^{k-1}q_n^{k d_n}(1+o(1)),
\tag{2}
\]

uniformly in \(A\), since \(p_n\to0\) and \(k\) is fixed. By exact exponential centering,

\[
q_n^{k d_n}=e^{-L_n}
=\frac{e^{-c}}{n(\log n)^{k-1}},
\qquad
\frac{d_n p_n}{\log n}\longrightarrow\frac1k.
\tag{3}
\]

Combining (1)–(3),

\[
\mathbb E[T_{n,k}]
\longrightarrow
\frac{k^{k-2}}{k!}\,k^{-(k-1)}e^{-c}
=\lambda_k:=\frac{e^{-c}}{k\,k!}.
\tag{4}
\]

**3. All factorial moments.** Distinct exact tree-component events cannot occur on overlapping vertex sets: two different connected components are necessarily disjoint, and on the same vertex set two different edge-trees are mutually exclusive. For fixed \(r\), consider any ordered vertex-disjoint tree embeddings \(A_1,\ldots,A_r\). Every host edge between two of their vertex sets was required closed by both separate events but only once jointly. At most \(\binom r2 k^2\) such cross-edges exist. Therefore

\[
\Pr\left(\bigcap_{i=1}^r E_{A_i}\right)
=\prod_{i=1}^r\Pr(E_{A_i})\cdot q_n^{-b},
\qquad 0\le b\le \binom r2 k^2.
\]

Uniformly over the tuple, \(q_n^{-b}=1+o(1)\). By the disjoint-embedding count in Step 1 and the uniform single-embedding estimate, for every fixed \(r\ge1\),

\[
\mathbb E[(T_{n,k})_r]\longrightarrow \lambda_k^r,
\qquad (x)_r=x(x-1)\cdots(x-r+1).
\tag{5}
\]

The factorial-moment criterion for nonnegative integer counts gives \(T_{n,k}\Rightarrow\operatorname{Poisson}(\lambda_k)\).

**4. Cyclic components are negligible.** For any tree embedding \(A\) on \(S\), consider the weaker witness event that its \(k-1\) edges are present and all host edges from \(S\) to its complement are absent, without constraining the other host edges *inside* \(S\). Because the boundary has \(k d_n-2(k-1)-2h(A)\) edges, the expected number of such witnesses is asymptotic to the right-hand side of (4), and in particular is \(O_{k,c}(1)\). Conditional on such a witness, the probability that any of its at most \(\binom{k}{2}\) non-tree internal edges is present is at most \(\binom{k}{2}p_n\). Every cyclic component of order \(k\) possesses at least one tree witness with an extra open internal edge. Therefore

\[
0\le \mathbb E[Z_{n,k}-T_{n,k}]
\le \binom{k}{2}p_n\,O_{k,c}(1)=o(1).
\tag{6}
\]

Thus \(Z_{n,k}-T_{n,k}\to0\) in probability, and Step 3 yields the asserted Poisson limit.

**5. The case \(k=1\).** Now \(L_n=\log n+c\), and the isolation indicator of a vertex has mean \(q_n^{d_n}=e^{-c}/n\). For an ordered \(r\)-tuple of distinct vertices with \(b\le\binom r2\) host edges among them, the probability of simultaneous isolation is \(q_n^{r d_n-b}=n^{-r}e^{-rc}(1+o(1))\), uniformly. Hence every fixed factorial moment of \(Z_{n,1}\) tends to \(e^{-rc}\), proving the \(k=1\) statement.

**6. Remaining isolated vertices at the two-component window.** Put \(k=2\), \(L_n=\log n+\log\log n+c\). The isolate count \(I_n\) has exact expectation

\[
\mu_n=n q_n^{d_n}=e^{-c/2}\sqrt{n/\log n}\longrightarrow\infty.
\]

If distinct vertices are adjacent in the host, their joint isolation probability is \(q_n^{2d_n-1}\), and otherwise it is \(q_n^{2d_n}\). Summing the \(n d_n\) ordered adjacent pairs gives the exact variance

\[
\operatorname{Var}(I_n)=\mu_n(1-q_n^{d_n})
+n d_n p_n q_n^{2d_n-1}.
\]

Divide by \(\mu_n^2\): the result is at most \(1/\mu_n+d_n p_n/(n q_n)\to0\), since \(d_n p_n=O(\log n)\) and \(q_n\to1\). Chebyshev's inequality gives \(I_n/\mu_n\to1\) in probability.

## Verification

The standalone script `verify_regular_components.py` performs exhaustive rational bond-percolation enumeration on four finite regular host graphs (including a disconnected host), independently enumerates tree witnesses, checks matching expected counts, and evaluates the exact tree-component mean for complete graphs at large finite orders. It passed 96 finite assertions. These computational checks test finite identities only; the infinite-family Poisson limit follows from the factorial-moment proof above. Run with `python verify_regular_components.py` using Python 3.9 or later, with no third-party packages.

## Relationship to prior work

Chakraborty–Luh–Singh (2026, arXiv:2610.42107, Theorem 4 and Section 4.1) prove an isolated-vertex Poisson limit **at connectivity** for percolation on a power of a cycle with \(d_n=2m_n\gg\log n\). The present result identifies fixed-order component windows \(k\ge2\), at smaller retention probabilities, and extends the fixed-order Poisson law to **all** deterministic regular hosts of growing degree without geometric/expansion hypotheses. The case \(k=1\) overlaps their isolated-vertex assertion for cycle powers and is included for the exact all-\(k\) pattern, not as an independent novelty claim.

Penrose (2015, arXiv:1507.07132, Theorem 2.2) gives Poisson approximation for components of fixed order in a **randomly sampled-vertex inhomogeneous connection model**, under its stated conditions. That result is relevant prior coverage of the general Poisson phenomenon but does not directly assert the stated universal constants and extinction centering for percolation on **arbitrary prescribed finite regular host graphs**. The respective models and assumptions must not be conflated.

Diskin–Krivelevich (2024, arXiv:2408.04597) study the much earlier giant-component regime \(d_n p_n\approx1\) under expansion/small-set conditions; they do not furnish the fixed-order extinction windows in the sparse-edge, logarithmic-degree regime \(d_n p_n\asymp\log n/k\).

## Limitations

Only fixed component sizes are treated. The result does not classify all components, establish host-graph connectivity, or produce a coupling across all critical windows simultaneously. The proof assumes full host regularity and \(d_n/\log n\to\infty\); it does not address arbitrary nonregular degree profiles or the boundary \(d_n\asymp\log n\). Finite numerical verification cannot establish asymptotic statements. Definitive historical priority has not been independently determined; related random-connection-model theory may provide partial or reducible coverage.

## References

1. S. Chakraborty, K. Luh, R. P. Singh, *Band Random Graphs: Connectivity, Geometry, and Transport*, arXiv:2610.42107v1 (first public 2026-10-30), https://arxiv.org/html/2610.42107v1.
2. M. D. Penrose, *Inhomogeneous random graphs, isolated vertices, and Poisson approximation*, arXiv:1507.07132 (2015); *Journal of Applied Probability* 55 (2018), https://arxiv.org/abs/1507.07132.
3. S. Diskin, M. Krivelevich, *Components, large and small, are as they should be I: supercritical percolation on regular graphs of growing degree*, arXiv:2408.04597 (2024), https://arxiv.org/abs/2408.04597.
4. A. Cayley, *A theorem on trees*, *Quarterly Journal of Mathematics* 23 (1889), 376–378 (labeled-tree enumeration).
