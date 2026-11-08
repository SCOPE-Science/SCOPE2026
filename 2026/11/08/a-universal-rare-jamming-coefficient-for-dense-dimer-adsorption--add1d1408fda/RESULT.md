# A universal rare-jamming coefficient for dense dimer adsorption with bounded-degree exclusions

## Finding
Let \(\Delta\ge 1\) be fixed. For every even integer \(N\) let \(H_N\) be a simple triangle-free graph on \(N\) labeled vertices, with maximum degree at most \(\Delta\), and set \(m_N=|E(H_N)|\). Perform unit-edge-rate irreversible dimer random sequential adsorption on the complement \(G_N=K_N\setminus E(H_N)\), from all vertices vacant. Equivalently, repeatedly select an edge uniformly from those whose endpoints are still vacant and occupy both endpoints, until no such edge exists. If \(R_N\) is the terminal number of vacant vertices, then \(R_N\in\{0,2\}\) and, uniformly over these forbidden-edge graphs,

\[
\Pr(R_N=2)=\frac{3m_N}{N^2-1}\left(1+O_{\Delta}\!\left(\frac{\log N}{N}\right)\right).
\]

For \(m_N=0\), the left side vanishes exactly and the displayed formula is interpreted as zero, without dividing by \(m_N\). In particular, if \(m_N/N\to\alpha\), then \(N\Pr(R_N=2)\to 3\alpha\). For the even cycle \(H_N=C_N\), \(N\Pr(R_N=2)\to3\); for an excluded perfect matching, the limit is \(3/2\). The coefficient is independent of the geometry of the bounded-degree exclusion graph, not merely its regularity.

## Assumptions and scope
All vertices are distinct and labeled. Every allowable unordered edge receives an independent continuous arrival clock with the same distribution; accepted dimers occupy both endpoints irreversibly. The equivalent uniform-choice-on-available-edges construction follows because the order of available edge arrivals is exchangeable. The graph \(H_N\) is *forbidden*: its edges are absent from the adsorption substrate. The graph may be disconnected, irregular, and may depend arbitrarily on \(N\), subject to a common fixed degree bound and triangle-freeness. The asymptotic \(O_\Delta\) constant depends only on this degree bound, not on the particular forbidden graph or its number of edges. The claim makes no statement for degree bounds growing with \(N\), for weighted nonuniform arrival rates, or for an exclusion graph containing triangles.

## Proof
Write \(U_k\) for the set of the \(k\) currently vacant vertices, at the stage with \(k=N,N-2,\ldots,2\). Because any set of at least three vertices contains an allowable pair (\(H_N\) has no triangle), the process reaches the two-vacancy stage. The last pair remains vacant precisely when it forms an edge of \(H_N\). These last-pair events are disjoint. It therefore suffices to show, *uniformly for each fixed forbidden edge* \(e=\{u,v\}\),

\[
\Pr(e\subseteq U_2)=\frac{3}{N^2-1}\left(1+O_\Delta\left(\frac{\log N}{N}\right)\right). \tag{1}
\]

**Uniform survival bounds for a finite marked set.** Fix \(r\in\{2,3,4\}\) and a marked \(r\)-set \(T\). For any current set \(U\supseteq T\) of size \(k\), let \(Q(U)\) count allowable pairs of \(U\), and \(D_T(U)\) count allowable pairs meeting \(T\). The missing-edge degree bound gives

\[
\binom{k}{2}-\frac{\Delta k}{2}\le Q(U)\le\binom{k}{2},\qquad
r(k-r-\Delta)\le D_T(U)\le rk.
\]

Conditional on \(T\subseteq U_k\), the chance that all marks survive the next adsorption is \(1-D_T(U_k)/Q(U_k)\). Consequently, for \(k\ge L\), with a sufficiently large even integer \(L=L(\Delta)\), these one-step probabilities differ from the corresponding complete-graph probabilities

\[
b_r(k)=\frac{\binom{k-r}{2}}{\binom{k}{2}}
\]

by a multiplicative factor \(1+O_\Delta(k^{-2})\). More explicitly, the displayed degree bounds sandwich the survival probability between \(1-2r/(k-1-\Delta)\) and \(1-2r(k-r-\Delta)/(k(k-1))\); both are \(b_r(k)+O_\Delta(k^{-2})\). The ratios can be taken positive and uniformly bounded by choosing \(L\) large. Iterating over even levels and using the convergent sum \(\sum_{k\ge L,\;k\text{ even}}k^{-2}\), while the complete-graph product equals \((k)_r/(N)_r\), proves constants \(0<c_\Delta<C_\Delta<\infty\) for which

\[
c_\Delta(k/N)^r\le\Pr(T\subseteq U_k)\le C_\Delta(k/N)^r
\quad(L\le k\le N,\ k\equiv N\pmod2). \tag{2}
\]

Here \((a)_r=a(a-1)\cdots(a-r+1)\). The constants are uniform in the identities of all marked vertices.

**Survival of one forbidden pair.** Fix \(e=\{u,v\}\in E(H_N)\). Given \(e\subseteq U_k\), let \(h_0\) be the number of forbidden pairs wholly within \(U_k\setminus e\), and let \(h_1\) be the number of forbidden pairs joining exactly one endpoint of \(e\) to an outside vertex. Set \(A=\binom{k-2}{2}\), \(B=\binom{k}{2}\). The exact one-step conditional survival probability is

\[
s(U_k)=\frac{A-h_0}{B-1-h_0-h_1}.
\]

If \(e\) were the *only* forbidden edge, it would instead be \(s_0(k)=A/(B-1)=(k-3)/(k+1)\). For \(k\ge L\) a direct denominator comparison, using \(h_0\le\Delta(k-2)/2\), \(h_1\le2(\Delta-1)\), and \(B-1-A=2(k-2)\), yields

\[
\left|\frac{s(U_k)}{s_0(k)}-1\right|
\le C_\Delta\left(\frac{h_0}{k^3}+\frac{h_1}{k^2}\right). \tag{3}
\]

There are at most \(\Delta N/2\) possible extra forbidden edges disjoint from \(e\). By the marked-set estimate (2), the joint survival probability of \(e\) and any such extra edge is at most \(C_\Delta(k/N)^4\), whereas the survival probability of \(e\) is at least \(c_\Delta(k/N)^2\). Likewise each of the at most \(2(\Delta-1)\) forbidden edges meeting \(e\) involves three specified vertices and has joint survival probability at most \(C_\Delta(k/N)^3\). Therefore

\[
\mathbb E[h_0\mid e\subseteq U_k]\le C_\Delta k^2/N,
\qquad
\mathbb E[h_1\mid e\subseteq U_k]\le C_\Delta k/N. \tag{4}
\]

Combining (3)--(4) gives

\[
\left|\frac{\Pr(e\subseteq U_{k-2}\mid e\subseteq U_k)}{s_0(k)}-1\right|
\le\frac{C_\Delta}{Nk},\quad k\ge L+2. \tag{5}
\]

Multiplying (5) from \(N\) down to \(L\), and summing \(1/k\), proves

\[
\Pr(e\subseteq U_L)
=\frac{L^2-1}{N^2-1}
\left(1+O_\Delta\left(\frac{\log N}{N}\right)\right). \tag{6}
\]

The rational factor is exact for the one-forbidden-edge process, by telescoping \(\prod_{k=N,N-2,\ldots,L+2}(k-3)/(k+1)\).

**Final bounded-size stage.** At \(k=L\), the same estimates (4) and Markov's inequality imply

\[
\Pr(h_0+h_1>0\mid e\subseteq U_L)=O_\Delta(1/N),
\]

since \(L\) depends only on \(\Delta\). On the complementary event, \(e\) is the only forbidden edge induced on \(U_L\), and no other forbidden edge can appear as vertices are subsequently removed. The conditional probability of retaining \(e\) through the final two vacancies is then exactly

\[
\prod_{k=L,L-2,\ldots,4}\frac{k-3}{k+1}=\frac{3}{L^2-1}.
\]

The exceptional stage configurations have total conditional probability \(O_\Delta(1/N)\), so the same expression holds with relative error \(O_\Delta(1/N)\). Multiplying by (6) proves (1). Finally sum (1) over the \(m_N\) disjoint possible final forbidden pairs, giving the theorem. \(\square\)

## Verification
The companion `verify.py` uses exact rational arithmetic and memoization over vacant-vertex subsets to calculate finite dimer-RSA probabilities independently of the tag-survival proof. It verifies the isolated-forbidden-edge identity for six sizes, exact cycle values through \(N=14\), and selected exhaustive small-graph and matching-deletion cases. Run with `python verify.py` in the same directory. These finite checks are not used to infer (1), its uniformity, or its limit.

## Relationship to prior work
Penrose and Sudbury (2005) formulate dimer RSA on general graphs, establish its edge-order representation and study vacancy and occupation probabilities for bounded-degree substrates and regular trees. The present dense substrate \(K_N\setminus H_N\) has degree growing like \(N\), and the claimed rare-terminal-pair coefficient is different from their site-occupation formulas and bounded-degree central limit theorems. Pippenger (1989) established fundamental graph RSA methods, including dimer adsorption, but his accessible abstract concerns regular or low-short-cycle substrates; the inaccessible full paper remains an explicit historical-comparison risk. Dyer and Frieze (1991) consider randomized greedy edge selection on fixed graphs, focusing on approximation performance, including sparse classes rather than this refined dense-graph probability. The previously analyzed deleted-perfect-matching family is recovered here as a proper special case; its known \(3/(2N)\) asymptotic does not imply the uniform theorem or the new cycle constant \(3/N\).

## Limitations
The result is a first-order rare-event asymptotic, not an exact finite formula for arbitrary forbidden graphs. The constants in the error bound are not numerically optimized. The degree cutoff is fixed as \(N\to\infty\), and triangle-freeness is used to prohibit terminal vacant sets of size at least three. Weighted arrivals and growing-degree exclusions are outside scope. Broader historical statements not accessible in full may affect priority; no independent audit or independent publication certification is asserted.

## References
1. M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, Annals of Applied Probability 15 (2005), 853–889; first public arXiv version 2005-03-24, [arXiv:math/0503519](https://arxiv.org/abs/math/0503519), DOI: 10.1214/105051604000000765.
2. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM J. Discrete Math. 2 (1989), 393–401, [DOI:10.1137/0402034](https://doi.org/10.1137/0402034).
3. M. Dyer and A. Frieze, *Randomized greedy matching*, Random Structures & Algorithms 2 (1991), 29–45, [DOI:10.1002/rsa.3240020104](https://doi.org/10.1002/rsa.3240020104).
