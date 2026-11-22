# Exact chirality-weighted ice partition functions and a seam-twist reversal on cubic ladders

## Finding

For every integer \(n\ge3\) and fugacity \(z\ge0\), let \(P_n=C_n\square K_2\) be the two-rail cubic prism and let \(M_n\) be its one-seam-twisted Möbius ladder. Form the four-regular line graphs \(L(P_n)\) and \(L(M_n)\). Orient each line-graph edge with the ice rule: exactly two arrows enter and two leave every vertex. At each of the \(2n\) original cubic vertices, the three incident original edges generate a designated triangular face in the line graph. Weight an ice orientation by \(z\) once for each such face whose three arrows are a directed 3-cycle (either chirality). Write \(Z_P(n,z)\) and \(Z_M(n,z)\) for the corresponding finite partition polynomials.

Define \(\lambda_{\pm}(z)=[4z^2+1\pm\sqrt{16z^4-8z^2+9}]/2\). Then the exact partition polynomials are

\[
Z_P(n,z)=\lambda_+(z)^n+\lambda_-(z)^n+2(2z+1)^n+2(2z-1)^n+3,
\]
\[
Z_M(n,z)=\lambda_+(z)^n+\lambda_-(z)^n+2(2z+1)^n-2(2z-1)^n+1.
\]

In particular, the **entire chiral seam response** has the exact simple form

\[
Z_P(n,z)-Z_M(n,z)=2+4(2z-1)^n.
\]

For even \(n\), the untwisted prism has strictly greater partition function for all \(z\ge0\). For odd \(n\), there is exactly one reversal at

\[
z_c(n)=\frac{1-2^{-1/n}}2,\qquad \lim_{n\to\infty} n z_c(n)=\frac{\log2}{2}.
\]

For odd \(n\), the Möbius boundary wins when \(0\le z<z_c(n)\), equality holds at the threshold, and the prism boundary wins when \(z>z_c(n)\). At unweighted ice fugacity \(z=1\), the prism has exactly **six additional ice states**, independent of \(n\), and both families have the same entropy per line-graph vertex

\[
\lim_{n\to\infty}\frac{\log Z_P(n,1)}{3n}
=\lim_{n\to\infty}\frac{\log Z_M(n,1)}{3n}
=\frac13\log\frac{5+\sqrt{17}}2.
\]

## Assumptions and scope

Each original graph is a simple cubic graph with \(2n\) vertices and \(3n\) edges, for integer \(n\ge3\). The Möbius seam swaps the two rails only at the closing pair of rail edges. The ice graph is the **line graph of this cubic graph**, not the original cubic ladder; it has \(3n\) vertices, \(6n\) edges, and degree four. Arrow orientations are counted on labelled edges, without quotienting by graph symmetries. The local cycle observable is defined on the \(2n\) triangles corresponding to original cubic vertices; it is not the count of every possible three-cycle in the line graph. Fugacity \(z\) weights each oriented local cycle once, with both possible directions each receiving weight \(z\). All statements hold for real \(z\ge0\), and the polynomial identities hold formally over the integers.

## Proof

At an original cubic vertex, the three corresponding incident edges are vertices of a triangle in the line graph. In a local orientation of this triangle, the indegrees at its three vertices are either a permutation of \((0,1,2)\) (one transitive orientation for each permutation) or \((1,1,1)\) (two directed cycles, each with weight \(z\)). Define the local polynomial factor \(f(a,b,c)\) to equal \(1\) if the three entries permute \((0,1,2)\), \(2z\) if all equal \(1\), and \(0\) otherwise. An original edge joins two such triangles, and the ice condition says that its endpoint local indegrees sum to \(2\). Therefore the local factor representation counts each and every ice orientation exactly once with the specified weight.

Cut each rail immediately before a prism column. The incoming state \((a_t,a_b)\) records the local indegrees contributed by its earlier endpoint to the two cut rail edges, with each component in \(\{0,1,2\}\). The outgoing state \((b_t,b_b)\) records the local indegrees contributed by the current column. On the rung, the two endpoint contributions are \(q\) and \(2-q\). This gives a nine-state transfer matrix

\[
T_{(a_t,a_b),(b_t,b_b)}(z)
=\sum_{q=0}^{2} f(2-a_t,b_t,q) f(2-a_b,b_b,2-q).
\]

Order states as \((0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)\). Evaluating this finite sum gives

\[
T=\begin{pmatrix}
1&0&0&0&0&0&0&0&0\\
0&2z&0&1&0&0&0&0&0\\
0&0&1&0&1&0&0&0&0\\
0&1&0&2z&0&0&0&0&0\\
0&0&1&0&4z^2&0&1&0&0\\
0&0&0&0&0&2z&0&1&0\\
0&0&0&0&1&0&1&0&0\\
0&0&0&0&0&1&0&2z&0\\
0&0&0&0&0&0&0&0&1
\end{pmatrix}.
\]

Let \(S\) swap the two rail coordinates of each state. Then \(S^2=I\), \(ST=TS\), and the two closing seams enforce

\[
Z_P(n,z)=\operatorname{tr}(T^n),\qquad
Z_M(n,z)=\operatorname{tr}(ST^n).
\]

Direct block reduction on the six-dimensional symmetric and three-dimensional antisymmetric sectors, or exact determinant expansion, gives

\[
\det(tI-T)=(t-1)^3(t-2z-1)^2(t-2z+1)^2
\big[t^2-(4z^2+1)t+4z^2-2\big].
\]

The restriction to the \(S=-1\) sector has eigenvalues \(1,2z-1,2z-1\) (with multiplicity). Thus the seam difference is exactly \(2\operatorname{tr}(T^n|_{S=-1})=2+4(2z-1)^n\). Adding this to the two-sector sum yields the displayed expressions; polynomial identities extend across coincident eigenvalues by continuity or by traces.

For even \(n\), the seam difference is at least \(2\). For odd \(n\), it is strictly increasing in \(z\ge0\), starting at \(-2\), crossing zero once when \((1-2z)^n=1/2\), and then becoming positive. The stated limiting threshold follows from \(2^{-1/n}=e^{-(\log2)/n}\). At \(z=1\), \(2z-1=1\), so the difference is exactly six. The two roots of the quadratic at \(z=1\) are \((5\pm\sqrt{17})/2\); the positive root exceeds the absolute values of the other transfer eigenvalues, so it determines the common thermodynamic entropy density. This completes the proof for all indicated integers and fugacities.

## Verification

The reproducible standalone file `verify_ice.py` uses two separate exact-integer constructions. It exhaustively enumerates all balanced orientations of the explicit line graph, directly tallies the number of cyclic original-vertex triangles, and compares **every polynomial coefficient** with the transfer trace expressions for both seams at each \(n=3,4,5,6,7\). The resulting unweighted totals are respectively \((154,148)\), \((600,594)\), \((2466,2460)\), \((10472,10466)\), and \((45474,45468)\), in prism/Möbius order. A separate exact polynomial computation checks the all-fugacity seam identity at every integer \(3\le n\le100\). The proof of the infinite-family result is symbolic, not inferred from finite tests. Run `python3 verify_ice.py` with the Python standard library.

## Relationship to prior work

The classical ice rule and square-lattice entropy problem originate with Lieb [1]. Cyclic and Möbius strips of Potts antiferromagnets, including kagome strips, have exact chromatic polynomial transfer results [2], and lattice-strip flow polynomials are computed in [3]. Those quantities count proper colourings or nowhere-zero flows on their respective studied graph families, not the specific local three-cycle-weighted Eulerian orientations on the line graphs of these cubic ladders. Lin's kagome staggered ice-rule work [4] is a particularly relevant broader vertex-model precedent; its indexed description concerns Pfaffian thermodynamics and local vertex weights, and the examined material does not give this specific finite twisted-seam three-triangle-observable polynomial. Creed's work [5] discusses complexity and Markov chains for Eulerian orientations, rather than this exact family formula.

A published database result [6] counts \(148\) square-ice orientations on a \(3\times3\) periodic torus. This agrees with the \(n=3\) Möbius special case \(L(M_3)=L(K_{3,3})\), which is the \(3\times3\) rook graph; that single known coefficient is not represented as novel. A different published result [7] counts Tait three-edge-colourings of the underlying cubic prism and Möbius ladders; the edge-colouring problem has different local constraints and does not imply the above chiral-weighted ice polynomials. Historical priority for the general formulas is not independently certified.

## Limitations

The model is classical, finite, zero-disorder, and strictly on the four-regular line graphs of cubic ladders. The result concerns exactly defined triangle-chirality weights and not arbitrary local six-vertex Boltzmann weights, all aspect ratios of kagome lattices, or a phase transition in the two-dimensional bulk. The boundary preference reversal is finite-size and occurs at a fugacity scaling as inverse system length. The thermodynamic limit fixes the strip width. Independent external audit and exhaustive priority determination have not been performed.

## References

[1] E. H. Lieb, "Residual Entropy of Square Ice," *Physical Review* 162, 162–172 (1967), https://doi.org/10.1103/PhysRev.162.162.

[2] S.-C. Chang and R. Shrock, "Exact Partition Functions for Potts Antiferromagnets on Cyclic Lattice Strips," arXiv:cond-mat/9907403 (public preprint July 26, 1999), https://arxiv.org/abs/cond-mat/9907403.

[3] S.-C. Chang and R. Shrock, "Flow Polynomials and Their Asymptotic Limits for Lattice Strip Graphs," arXiv:cond-mat/0205424 (public preprint May 20, 2002), https://arxiv.org/abs/cond-mat/0205424.

[4] K. Y. Lin, "Staggered ice-rule vertex model on the Kagome lattice," *Journal of Physics A* 8, 1899–1919 (1975), https://doi.org/10.1088/0305-4470/8/12/008.

[5] P. J. Creed, *Counting and Sampling Problems on Eulerian Graphs*, University of Edinburgh PhD thesis (2010), https://era.ed.ac.uk/items/b57a1ce7-befd-4e98-bba4-ff24581273ea.

[6] "Complete Walsh spectrum and optimal range projections for the smallest simple periodic square-ice torus," published-finding corpus (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-complete-walsh-spectrum-and-optimal-range-projections-for-the-sm--fdbca339c304.

[7] "Tait colourings as primitive-three excitation on cubic line graphs, with a constant-six seam law," published-finding corpus (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-tait-colourings-as-primitive-three-excitation-on-cubic-line-grap--c4fb511b080a.
