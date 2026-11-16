# Parity-sharp Walsh gaps for complete-graph edge covers and a seven-vertex nullspace census

## Finding

Let \(n\ge 2\), \(m=\binom n2\), and let \(\mathcal E_n\subseteq\mathbb F_2^m\) be the binary incidence vectors of all edge-covering subsets of the labelled complete graph \(K_n\). The unnormalized Walsh transform of the edge-cover indicator, at the frequency corresponding to a graph \(H\subseteq K_n\), is
\[
W_n(H)=(-1)^n\sum_{S\in\operatorname{Ind}(H)}(-1)^{|S|}2^{\binom{|S|}{2}},
\]
where \(\operatorname{Ind}(H)\) is the family of independent vertex sets of \(H\), including the empty set. The complete spectral gap is
\[
\min_{H:W_n(H)\ne0}|W_n(H)|=\begin{cases}1&\text{if }n\text{ is even},\\2&\text{if }n\text{ is odd}.\end{cases}
\]
Every multiplier is nonzero when \(n\) is even. For odd \(n\), at least half of the multipliers are nonzero and exactly half have two-adic valuation one. There are also vanishing multipliers for every odd \(n\ge3\).

An exhaustive seven-vertex result supplements the all-order theorem: of the \(2^{21}=2{,}097{,}152\) Walsh frequencies, exactly \(73{,}115\) vanish, falling into exactly \(39\) isomorphism classes of frequency graphs. Their edge counts are \(6,10,14,18\), with labelled multiplicities \(840,17{,}220,53{,}760,1{,}295\), respectively. Thus the convolution rank is exactly \(2{,}024{,}037\) in this first seven-vertex census. The orbit-level certificate is `edge_cover_zero_orbits.csv`.

## Assumptions and scope

All graphs are finite, undirected, simple and labelled on vertex set \([n]\). A set of edges is an **edge cover** if every vertex is incident to at least one chosen edge. Set \(G_n=(\mathbb F_2)^{E(K_n)}\). With counting measure, the convolution operator is
\[
(C_nf)(x)=\sum_{y\in G_n}\mathbf1_{\mathcal E_n}(y)f(x-y),
\]
and the Walsh character at \(H\subseteq K_n\) is \(\chi_H(y)=(-1)^{|H\cap y|}\). Fourier multipliers are **unnormalized**. Ranks and pseudoinverses use the usual finite-dimensional \(\ell^2\) norm, and the positive spectral condition number is the largest divided by the smallest nonzero multiplier magnitude.

## Proof

**Signed inclusion-exclusion.** For each vertex \(v\), exclude edge sets not incident to \(v\). Expanding this intersection complement by inclusion-exclusion gives
\[
W_n(H)=\sum_{T\subseteq[n]}(-1)^{n-|T|}\sum_{F\subseteq E(K_n[T])}(-1)^{|F\cap H|}.
\]
For a given \(T\), the inner sum factors over its edges as \(\prod_{e\in E(K_n[T])}(1+(-1)^{\mathbf1_{e\in H}})\). It is zero whenever \(H[T]\) contains an edge; otherwise it equals \(2^{\binom{|T|}{2}}\). Hence only independent vertex sets of \(H\) survive, proving the displayed multiplier formula for every frequency.

**Universal parity and sharp gaps.** The terms of sizes zero and one give \(1-n\); all terms of size at least two are even, so
\[
W_n(H)\equiv (-1)^n(1-n)\pmod2.
\]
For even \(n\), every multiplier is odd. For odd \(n\), every multiplier is even. Let \(H\) be the graph obtained from \(K_n\) by removing a matching of \(a\) edges. Its independent-set polynomial is \(1+nt+at^2\); therefore
\[
W_n(H)=(-1)^n(1-n+2a).
\]
For even \(n\), take \(a=(n-2)/2\) to obtain magnitude \(1\). For odd \(n\), take \(a=(n-3)/2\) to obtain magnitude \(2\), and take \(a=(n-1)/2\) to obtain zero. These matching sizes are nonnegative integers within the maximum possible matching size for all stated \(n\). This establishes both gap sharpness and the invertibility parity dichotomy without relying on finite experiments.

**Exactly half with two-adic valuation one for odd orders.** Terms of sizes at least three are divisible by \(8\), whence
\[
W_n(H)\equiv(-1)^n\left(1-n+2\left[\binom n2-|E(H)|\right]\right)\pmod4.
\]
If \(n\) is odd, this residue is \(2\) modulo \(4\) for one parity of \(|E(H)|\) and zero modulo \(4\) for the other. Flipping one fixed frequency edge pairs the two parities bijectively. Thus exactly \(2^{m-1}\) multipliers have valuation precisely one and the rank is at least \(2^{m-1}\).

**Spectral operator consequences.** All Walsh characters form an orthogonal eigenbasis. The maximum multiplier magnitude is attained at the zero frequency and equals the number of edge covers,
\[
A_n=\sum_{k=0}^n(-1)^{n-k}\binom nk2^{\binom k2},
\]
by the triangle inequality. Therefore \(\|C_n^\dagger\|_{2\to2}=1\) when \(n\) is even and \(1/2\) when \(n\) is odd; the positive spectral condition numbers are respectively \(A_n\) and \(A_n/2\). The invertibility statement applies only to even \(n\).

**Finite seven-vertex census.** The exact certificate algorithm (see `verify_edge_cover_spectrum.py`) builds the indicator of every edge subset and performs a full integer Walsh-butterfly transform. Independently, it assigns each vertex set \(T\) the weight \((-1)^{n+|T|}2^{\binom{|T|}{2}}\) at the clique-edge mask of \(T\), then takes a subset-zeta transform and complements the frequency mask. These independent recurrences agree at every one of the \(2^{21}\) frequencies, not merely at sample points. Exactly \(73{,}115\) of the resulting integer coefficients are zero. The 1,044 standard nonisomorphic seven-vertex graph representatives are filtered with the independent-set expression; counting each zero representative with multiplicity \(7!/|\operatorname{Aut}(H)|\) gives \(39\) classes whose multiplicities sum to \(73{,}115\). Each representative, its independent-set coefficients and automorphism count appear in `edge_cover_zero_orbits.csv`. The full direct transform provides an independent total-zero count and the zero-orbit weighted sum cross-checks it.

## Verification

From this directory run `python verify_edge_cover_spectrum.py` with Python 3, NumPy, and NetworkX installed. It writes `edge_cover_summary.csv` and `edge_cover_zero_orbits.csv` deterministically. The script checks all Walsh coefficients for \(2\le n\le7\) using two separate integer algorithms, Parseval's identity, the parity-class bound, gap witnesses, zero totals, and exact graph-orbit multiplicities. On completion it prints `EDGE_COVER_COMPLETE_GRAPH_FOURIER_EXACT_PASS n7_orbits=39 n7_zeros=73115`. For \(n=2,3,4,5,6,7\), the zero totals are respectively \(0,3,0,105,0,73115\). This is a finite certificate for the seven-vertex statistics and a corroboration, not a substitute, for the all-order proof.

## Relationship to prior work

Akbari and Oboudi prove the ordinary unsigned edge-cover polynomial by inclusion-exclusion in Theorem 3, and its complete-graph specialization in Corollary 2. The signed character-sum factorization above is a direct multivariate specialization of that existing inclusion-exclusion principle and is not presented as a novel general inclusion-exclusion method. Lin, Liu and Lu study approximation algorithms for counting edge covers, not Walsh-multiplier rank or gap. The assessed new output is the parity-sharp **all-frequency** spectral classification together with the exact seven-vertex zero set and symmetry-orbit census. An unlocated signed multivariate edge-cover formula could subsume parts of this finding; novelty claims are bounded by sources inspected.

## Limitations

There is no closed formula here for the exact number of zero multipliers for all odd orders. The \(39\) frequency-graph orbit classification is finite and specific to seven vertices, not a claim that larger cases behave identically. The rank and \(\ell^2\) pseudoinverse results do not establish sharp projection norms on \(\ell^1\), \(\ell^\infty\) or intermediate \(\ell^p\) spaces. The finite certificate relies on integer computation and independent comparison; independent mathematical audit and exhaustive historical-priority verification have not been performed.

## References

- S. Akbari and M. R. Oboudi, *On the edge cover polynomial of a graph*, European Journal of Combinatorics 34 (2013), 297–321. Available full text: https://janos.cs.technion.ac.il/COURSES/236603-11/oboudi.pdf ; Theorem 3 and Corollary 2.
- C. Lin, J. Liu and P. Lu, *A Simple FPTAS for Counting Edge Covers*, first posted 2013-09-24: https://arxiv.org/abs/1309.6115 .
