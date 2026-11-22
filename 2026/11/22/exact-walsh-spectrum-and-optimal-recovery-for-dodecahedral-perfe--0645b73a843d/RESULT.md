# Exact Walsh spectrum and optimal recovery for dodecahedral perfect matchings

## Finding
Let \(D\) be the dodecahedral graph, with \(20\) vertices and \(30\) edges, and let \(\mathcal M(D)\) be its \(36\) perfect matchings. Identify each matching with its edge-incidence vector in \(H=\mathbb F_2^{30}\), set \(f=\mathbf1_{\mathcal M(D)}\), and let \(Tg=f*g\) denote **unnormalized** convolution on \(H\). Its Walsh multiplier at a frequency \(S\subseteq E(D)\) is
\[
\Lambda(S)=\sum_{M\in\mathcal M(D)}(-1)^{|M\cap S|}.
\]
The absolute multiplier spectrum, after normalization of signs on the edges of any spanning tree, consists of exactly \(2^{11}=2048\) entries with the following multiplicities:

| \(\lvert\Lambda\rvert\) | Number of normalized frequency classes |
|---:|---:|
| 0 | 700 |
| 4 | 882 |
| 8 | 240 |
| 12 | 140 |
| 16 | 84 |
| 36 | 2 |

Every entry in this table corresponds to \(2^{19}\) frequencies in the full Boolean cube. Consequently,
\[
\operatorname{rank}T=706740224,\qquad
\operatorname{nullity}T=367001600,
\]
and every multiplier is divisible by \(4\), with the sharp nonzero gap \(\min_{\Lambda(S)\ne0}|\Lambda(S)|=4\). The first vanishing characters have frequency support size exactly \(2\): precisely \(60\) of the \(\binom{30}{2}=435\) two-edge supports vanish, whereas no singleton support vanishes.

If \(R=\operatorname{ran}T\), then for **all** complex or real linear projections \(Q\colon\ell^p(H)\to R\), not necessarily translation-invariant, the sharp endpoint norms satisfy
\[
\min_Q\|Q\|_{\ell^1\to\ell^1}
=\min_Q\|Q\|_{\ell^\infty\to\ell^\infty}
=\frac{83}{8}.
\]
The translation-invariant optimal projector kernel is supported at exactly \(1024\) elements of the binary cycle space. On \(R\), the optimal inverse in Hilbert norm has norm \(1/4\) and spectral condition number \(9\).

## Assumptions and scope
Here \(D\) is the **simple, labelled** generalized Petersen graph \(\operatorname{GP}(10,2)\): outer edges join successive vertices of a ten-cycle, spokes join corresponding outer and inner vertices, and inner edges join inner indices differing by two modulo ten. All \(36\) matchings have unit multiplicity and cover each vertex once. Frequencies are arbitrary subsets of all \(30\) edges. No infinite-family statement or extension to other cubic graphs is intended.

The underlying matching count \(36\) is established in prior literature. This finding concerns signed incidence sums, their entire spectrum, exact recovery and sharp projection constants, which are different invariants.

## Proof
**Matching incidence and divisibility.** Every perfect matching contains ten edges. The dodecahedral graph is edge-transitive; hence each of its thirty edges belongs to the same number \(c\) of matchings. Double counting gives \(30c=36\cdot10\), so \(c=12\). The inclusion-exclusion expansion
\[
\Lambda(S)=36-2\sum_{e\in S}12
+4\sum_{\{e_1,e_2\}\subseteq S}\#\{M:e_1,e_2\in M\}-8(\cdots)
\]
shows \(\Lambda(S)\equiv0\pmod4\). In particular, for a singleton \(S=\{e\}\), \(\Lambda(S)=12\). For two different edges,
\[
\Lambda(\{e,f\})=4\bigl(\#\{M:e,f\in M\}-3\bigr).
\]
The exhaustive incidence enumeration in `verify.py` finds precisely sixty unordered pairs occurring together in three matchings, proving the first-zero claim.

**Exhaustive reduction to \(2048\) signed sums.** For each vertex \(v\), let \(\delta_v\in\mathbb F_2^{E(D)}\) be the indicator of its incident edges. For every matching \(M\), \(\langle\delta_v,M\rangle=1\). Thus for a sum of vertex stars \(u=\sum_{v\in A}\delta_v\), one has \(\Lambda(S+u)=(-1)^{|A|}\Lambda(S)\), and hence the absolute value and zero/nonzero status are unchanged. Since the graph is connected, the vertex-star subspace has dimension \(19\), and every class modulo this subspace has a unique representative zero on a fixed spanning tree's nineteen edges. The remaining eleven cotree signs range independently. Each such class contains \(2^{19}\) full frequencies.

For a fixed signing, the weighted matching recurrence on a remaining vertex set \(U\) is
\[
F_\sigma(\varnothing)=1,\qquad
F_\sigma(U)=\sum_{u\in N(v)\cap U}\sigma_{vu}\,F_\sigma(U\setminus\{v,u\}),
\]
where \(v\) is the lowest indexed vertex of \(U\). Each matching is counted exactly once, by induction on \(|U|\). All \(2048\) choices of cotree signs were evaluated using this recurrence on the published dodecahedron edge list. Independently, all matchings were generated recursively in the generalized Petersen representation, projected onto cotree bits, and their signed sums obtained both by direct parity counting and by an exact integer Walsh-Hadamard transform. The independent constructions agree after comparison of their absolute-frequency histograms, which give exactly the table above. The recurrence establishes exhaustive, rather than sampled, coverage. Nonzero magnitude four occurs, so divisibility gives the sharp spectral gap. The trivial frequency has value \(36\), proving the largest multiplier magnitude, and the Hilbert condition number is \(36/4=9\).

**Sharp endpoint projection norm.** The Fourier range consists exactly of the nonzero-multiplier characters. The orthogonal Fourier projection \(P\) onto this range has multiplier \(\mathbf1_{\Lambda\ne0}\). Translation averaging of *any* bounded projection onto this translation-invariant range yields the unique translation-invariant projection \(P\), without increasing its \(\ell^1\) or \(\ell^\infty\) operator norm. Thus both endpoint minima are attained by \(P\). The multiplier indicator is invariant under the nineteen-dimensional vertex-star subspace, so Fourier inversion puts the kernel of \(P\) entirely in the orthogonal eleven-dimensional cycle space.

Write \(\Xi=\mathbb F_2^{11}\) for cotree frequency coordinates, and set \(a(\xi)=\mathbf1_{\Lambda(\xi)\ne0}\). For cycle-space coordinates \(z\in\Xi\), define
\[
B(z)=\sum_{\xi\in\Xi}a(\xi)(-1)^{\langle\xi,z\rangle}.
\]
The projector's cycle-space kernel equals \(2^{-11}B(z)\). Exact integer inversion of the \(2048\)-entry zero/nonzero table gives \(\sum_z|B(z)|=21248\), with exactly \(1024\) nonzero \(B(z)\). It follows that
\[
\|P\|_{\ell^1\to\ell^1}
=\|P\|_{\ell^\infty\to\ell^\infty}
=\frac{21248}{2048}=\frac{83}{8},
\]
where equality is the row/column absolute-sum norm of convolution. This establishes optimality even over arbitrary projections.

## Verification
Run `python3 verify.py` with Python 3.9 or newer; no third-party packages, remote resources, or external files are needed. The certificate (i) checks an explicit isomorphism between the published edge list and \(\operatorname{GP}(10,2)\), (ii) independently enumerates all thirty-six perfect matchings in both encodings, (iii) computes all \(2048\) cotree sign assignments by signed dynamic programming and independently by a Walsh transform of the matching indicator, (iv) checks all thirty edge marginals and \(435\) unordered pairs, and (v) independently Walsh-inverts the recovery multiplier indicator, checks Parseval and reports the exact \(\ell^1\) sum. All computations use integers, except the displayed exact rational normalization. The mathematical reduction above, not the finite output alone, justifies the statements concerning all \(2^{30}\) frequencies and all linear endpoint projections.

## Relationship to prior work
Fujita's 2013 paper supplies a complete dodecahedral edge list and derives the unsigned perfect-matching number \(36\) using restricted-subduced cycle indices (Section 4.1 and equation (50)); this number is **not new**. The January 2015 public discussion of dodecahedral perfect matchings gives independent combinatorial explanations of the same number. Deza and Dutour Sikirić analyze the dodecahedral *cut polytope*, rather than signed perfect-matching Fourier sums. The general symmetry/switching technique and Boolean harmonic analysis are standard tools. Published finite matching-Fourier calculations for different graphs supply methodological comparisons, but do not imply these dodecahedral numerical values without new graph-specific matching data.

## Limitations
The classification concerns one fixed finite graph. It does not prove a pattern for larger fullerenes, determine the entire spectrum of a weighted non-binary dimer system, or supply independent external audit. The novelty comparison is bounded to accessible and indexed sources; an unpublished, unindexed, or differently phrased earlier computation could coincide. The 2013 journal source provides a publication year but no verified exact first-access day; the date field associated with the archival input uses an independently day-stamped January 2015 public explanation, not an invented day for the earlier article.

## References
1. S. Fujita, “Restricted Enumerations by the Unit-Subduced-Cycle-Index (USCI) Approach. IV. The Restricted-Subduced-Cycle-Index (RSCI) Method for Enumeration of Kekulé Structures and of Perfect Matchings of Graphs,” *MATCH Communications in Mathematical and in Computer Chemistry* **69** (2013), 333–354, Section 4.1. https://match.pmf.kg.ac.rs/electronic_versions/Match69/n2/match69n2_333-354.pdf
2. “Number of perfect matchings of the Dodecahedron,” public discussion initiated 5 January 2015, including explanations of the 36 matchings. https://mathoverflow.net/questions/192159/number-of-perfect-matchings-of-the-dodecahedron
3. M. Deza and M. Dutour Sikirić, “Enumeration of the facets of cut polytopes over some highly symmetric graphs,” arXiv:1501.05407 (first posted 22 January 2015), including the dodecahedral cut polytope. https://arxiv.org/abs/1501.05407
