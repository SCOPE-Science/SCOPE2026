# Complete signed-matching Fourier spectrum and sharp range projection for the McGee cage

## Finding

Let \(G\) be the McGee \((3,7)\)-cage with \(24\) vertices and \(36\) edges. Identify its edge subsets with \(H=\mathbb F_2^{E(G)}\). Let \(f:H\to\{0,1\}\) be the indicator of perfect-matchings' edge-incidence vectors, and let \(T_f h=f*h\) be unnormalized counting convolution on \(H\). Its integer Walsh multipliers are
\[
W(s)=\sum_{M\in\mathcal M(G)}(-1)^{|s\cap M|},\qquad s\subseteq E(G).
\]
There are exactly \(60\) perfect matchings. All \(2^{36}\) Walsh multipliers have the following **complete absolute spectrum**, expressed first as multiplicities among the \(2^{13}\) vertex-switching sign classes:

| \(|W|\) | Switching-class multiplicity |
|---:|---:|
| 0 | 2112 |
| 4 | 2954 |
| 8 | 1728 |
| 12 | 896 |
| 16 | 192 |
| 20 | 208 |
| 24 | 64 |
| 28 | 36 |
| 60 | 2 |

Each row's multiplicity is multiplied by \(2^{23}\) to obtain its full Walsh-frequency multiplicity. In particular,
\[
\operatorname{rank}T_f=51\,002\,736\,640,\quad
\dim\ker T_f=17\,716\,740\,096,
\]
and the least positive absolute multiplier is \(4\); the ratio of largest to smallest nonzero absolute multipliers is exactly \(15\).

Let \(R=\operatorname{ran}T_f\). For **every** real or complex linear projection \(Q\) from \(\ell^1(H)\) onto \(R\), respectively from \(\ell^\infty(H)\) onto \(R\),
\[
\|Q\|\ge\frac{939}{64},
\]
and equality is attained in each case by the canonical Fourier range projection. Its convolution kernel has precisely \(2412\) nonzero positions, contained in the graph's binary cycle space. Among characters supported on one or two original graph edges, no weight-one Walsh multiplier vanishes; exactly \(128\) distinct weight-two multipliers vanish. Hence the first cancellation support size is two.

## Assumptions and scope

Use the explicit labeling \(V(G)=\{0,1,\ldots,23\}\), with indices modulo \(24\): take cycle edges \(\{i,i+1\}\) and chords \(\{i,i+s_i\}\), where the length-\(24\) shift list is the triple \((-12,7,-7)\) repeated eight times; deduplicate undirected edges. The resulting connected cubic graph has \(36\) edges and girth seven. A perfect matching covers every vertex exactly once with \(12\) distinct edges. Characters are the unnormalized signs \(\chi_s(x)=(-1)^{\langle s,x\rangle}\), so the trivial Walsh multiplier is \(60\); all norms count with the ordinary, unweighted finite-group \(\ell^p\) convention. The projection is onto the full range \(R\), not an inverse on the kernel, and the optimized class comprises all linear projections, whether or not translation-invariant.

## Proof

**Complete matching and Fourier reduction.** Choose an arbitrary spanning tree \(T\) of \(G\); it has \(23\) edges, leaving \(13\) chords \(C=E(G)\setminus T\). For each vertex \(v\), toggling all signs incident to \(v\) changes the product of signs on **every** perfect matching by exactly \(-1\), because each matching has one edge at \(v\). More generally, adding a graph cut to a signing multiplies every signed matching count by the same sign. For a connected graph, the cut space has dimension \(|V|-1=23\); every signing therefore has a unique representative with all tree edges positive, and there are exactly \(2^{13}=8192\) representatives. Their absolute multipliers and zero sets are identical across their respective \(2^{23}\)-member switching cosets.

Enumerate matchings recursively: on a nonempty set \(U\) of uncovered vertices, choose its least vertex \(u\) and pair \(u\) with every adjacent \(v\in U\), recursing on \(U\setminus\{u,v\}\). This is a disjoint, exhaustive partition of the perfect matchings. It returns \(60\) distinct matchings. For each \(x\in\mathbb F_2^{13}\), let \(B(x)\) count enumerated matchings whose restriction to \(C\) is \(x\). Then the complete reduced signed spectrum is obtained from the **integer** Fourier transform
\[
W_C(s)=\sum_{x\in\mathbb F_2^{13}} B(x)(-1)^{\langle s,x\rangle}.
\]
The supplied exact verifier implements this transform by the butterfly identity \((a,b)\mapsto(a+b,a-b)\), visits all \(8192\) signings, and derives precisely the nine entries of the table. It separately evaluates each one of the \(8192\) multipliers by the signed matching recurrence
\[
F_s(U)=\sum_{\substack{v\sim u\\v\in U}}\epsilon_s(uv)F_s(U\setminus\{u,v\}),\qquad F_s(\varnothing)=1,
\]
with least \(u\in U\), positive tree-edge signs and independently selected negative chord-edge signs. The two integer methods agree at every signing. All branching choices are exhaustive, with the empty vertex set as base case, and no approximation or unverified interpolation occurs. The table and rank/nullity follow by counting and the \(2^{23}\) switching multiplicity.

**Projection and optimality.** Fourier diagonalization shows that the canonical projection \(P\) onto \(R\) is the convolution multiplier \(1_{W\ne0}\). Let \(b(s)=1_{W_C(s)\ne0}\) on the \(13\) representative chord-sign coordinates, and write its unnormalized Walsh transform as \(\widehat b(x)\). By switching invariance, the full projection kernel is supported in the orthogonal complement of the graph's cut space, namely the \(13\)-dimensional binary cycle space. Up to the natural tree/chord coordinates, its nonzero possible coefficients are \(2^{-13}\widehat b(x)\). The exact second transform gives
\[
\sum_{x\in\mathbb F_2^{13}}|\widehat b(x)|=120192,
\quad \#\{x:\widehat b(x)\ne0\}=2412.
\]
The operator norms of a convolution on either finite-group \(\ell^1\) or \(\ell^\infty\) equal the sum of the absolute values of its kernel; hence \(\|P\|=120192/8192=939/64\).

To see **unrestricted** sharpness, let \(Q\) be any projection onto \(R\), and average its conjugates by the \(2^{36}\) translation isometries on \(H\). Since \(R\) is translation invariant and \(Q\) acts identically there, the averaged operator is a translation-invariant projection onto \(R\), and its norm cannot exceed \(\|Q\|\). The unique such projection has Fourier multiplier one on the frequencies spanning \(R\) and zero off them, hence equals \(P\). This proves the stated minimum for both real and complex projections and both endpoint norms.

**First Walsh cancellation.** The exhaustive matching list has exactly \(20\) matchings containing each of the \(36\) graph edges. Thus every singleton character has multiplier \(60-2\cdot20=20\). For distinct edges \(e,f\), the inclusion-exclusion identity
\[
W(\{e,f\})=60-2(20+20)+4\#\{M:e,f\in M\}=4(N_{ef}-5)
\]
shows it vanishes exactly when \(N_{ef}=5\). The complete loop over the \(630\) unordered edge pairs finds exactly \(128\) such pairs, each consisting of disjoint edges. Hence the first zero support size is exactly two.

## Verification

Run `python3 mcgee_verify.py` using standard Python 3.10 or later without third-party dependencies. The verifier builds and checks the graph (connectedness, cubic degrees, girth seven), enumerates every perfect matching, builds the \(8192\)-point unsigned frequency input, and checks the entire reduced Walsh spectrum against a separately memoized signed-matching recurrence. It checks all stated frequencies, multiplicities, ranks, gaps, the exact second Walsh projection sum, kernel support and the \(630\) low-weight edge pairs. It raises an exception on any disagreement and prints `PASS` only on completion. The loops are finite and complete by the displayed recurrences and the cut-space reduction; numerical experiments are not used as proofs of an infinite statement.

## Relationship to prior work

McGee's original 1960 article constructs the smallest \((3,7)\)-cage; Exoo and Jajcay's 2008 survey documents its 24-vertex structure and automorphism group. Earlier published exact enumerations establish the same graph's 60 perfect matchings, its complete two-factor profiles and its anti-forcing-number distribution. Those unsigned and optimization invariants do **not** determine individual signed matching counts, the entire Walsh zero locus, or the optimum endpoint projection norm. General perfect-matching and Fourier inversion methods are standard and are not claimed as new; the contribution is their complete exact evaluation for this canonical graph. Some previously studied graphs have analogous signed spectra but different incidence families. The source comparisons in the accompanying review cover the closest inspected records; they do not prove absolute historical priority.

## Limitations

This is a completely specified, finite, computer-assisted theorem about the McGee cage, not a classification for all cubic cages or a uniform all-order family. The claimed spectrum and norm rely on finite exhaustive integer computations with readable and independently structured recurrences; they are not a machine-checked formal proof. An unindexed equivalent under signed matching, hafnian, or dimer terminology may exist. No independent mathematical audit is claimed.

## References

1. W. F. McGee, *A Minimal Cubic Graph of Girth Seven*, Canadian Mathematical Bulletin 3 (1960), 149–152, doi:10.4153/CMB-1960-018-1. Open paper: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B6AF32607F85BC1B3D1159BE3F0A601E/S0008439500050463a.pdf/a-minimal-cubic-graph-of-girth-seven.pdf.
2. G. Exoo and R. Jajcay, *Dynamic Cage Survey*, Electronic Journal of Combinatorics, DS16 (first published 2008-09-29), §2.1.3. https://www.combinatorics.org/files/Surveys/ds16/ds16v1-2008.pdf.
3. A. Björklund, T. Husfeldt, P. Kaski and M. Koivisto, *Computing the Tutte polynomial in vertex-exponential time*, arXiv:0711.2585 (first posted 2007-11-16); McGee graph Tutte coefficients in revised full-text appendix. https://arxiv.org/abs/0711.2585.
4. *The complete 2-factor spectrum of the McGee graph and its eight symmetry classes*, exact graph census (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-the-complete-2-factor-spectrum-of-the-mcgee-graph-and-its-eight--434d398b5fa9.
5. *Anti-forcing spectrum of the McGee cage and a two-factor-profile obstruction*, exact graph census (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-anti-forcing-spectrum-of-the-mcgee-cage-and-a-two-factor-profile--586cf7e5211d.
