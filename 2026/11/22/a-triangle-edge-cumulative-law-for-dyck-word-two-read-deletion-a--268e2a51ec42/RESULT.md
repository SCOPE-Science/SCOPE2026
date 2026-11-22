# A triangle–edge cumulative law for Dyck-word two-read deletion ambiguity

## Finding
Let \(\mathcal D_n\) consist of the binary Dyck words of length \(2n\), where \(1\) is an up-step and \(0\) a down-step. Write \(D_1(w)\) for the **set of distinct** words obtained by deleting one symbol of \(w\). Form a simple graph \(G_n\) on \(\mathcal D_n\), with an edge between distinct words exactly when their deletion sets have two common elements. Write \(E_n\) for its number of unordered edges and \(T_n\) for its number of unordered triangles (three distinct words that are pairwise adjacent).

**Theorem.** For every integer \(n\ge1\), with \(E_1=T_1=0\),
\[
T_n=2\sum_{k=2}^{n-1}(k-1)\binom{2(n-k)+1}{n-k-1},
\qquad T_{n+1}-T_n=2E_n.
\]
Here the sum is empty when \(n\le2\). Equivalently, with \(C(z)=\sum_{m\ge0}C_mz^m\), \(C_m=\binom{2m}{m}/(m+1)\), and \(H(z)=C(z)+2zC'(z)-C(z)^2\),
\[
\sum_{n\ge1}T_nz^n=\frac{2z^2H(z)}{(1-z)^2},
\qquad \sum_{n\ge1}E_nz^n=\frac{zH(z)}{1-z}.
\]
As \(n\to\infty\),
\[
T_n\sim\frac49 nC_n\sim\frac{4}{9\sqrt\pi}\frac{4^n}{\sqrt n},
\qquad \frac{3T_n}{E_n}\longrightarrow2.
\]
The latter quotient is the **mean number of graph triangles incident to an edge**. The first triangle counts, from semilength \(1\) through \(10\), are \(0,0,2,14,68,290,1172,4628,18094,70456\).

More precisely, each triangle is uniquely determined by a four-tuple: an alternating half-length \(k\ge2\), an outside Dyck word \(v\in\mathcal D_{n-k}\) with a marked positive-height vertex, a split \(j\in\{1,\ldots,k-1\}\), and a choice of one of the two splice phases. This is a canonical bijection; the formula counts such tuples.

## Assumptions and scope
For every prefix of \(w\in\mathcal D_n\), the number of \(1\)'s is at least the number of \(0\)'s, and both total counts equal \(n\). A path vertex is a point after any prefix, including the empty and complete prefixes. Its height is the prefix difference of ones minus zeros. Two words are adjacent only when they share **two distinct** one-deletion outputs; duplicates caused by deleting different positions are ignored. Every graph triangle has three distinct vertices, and adjacency is pairwise: no assertion is made that all three words have the same pair of deletion outputs. The empty word is allowed only as an outside context, not as a graph source; all main quantifiers have integer \(n\ge1\).

## Proof
**1. Published alternating-interval edge criterion.** The Type-A criterion of Cai–Kiah–Nguyen–Yaakobi (arXiv:2001.01376, Proposition 9) establishes that distinct binary words of equal length share two distinct single-deletion outputs precisely when they agree outside a unique first-to-last differing interval and have the opposite alternating phases on that interval. In a fixed-composition layer, this interval has even length \(2k\), as swapping an odd alternating interval changes the number of ones. Its two phases are \(A=(10)^k\) and \(B=(01)^k\). For both words to be Dyck, the common height at the insertion vertex must be positive, since phase \(B\) begins with a down-step. Conversely, at any positive-height vertex of an outside Dyck word, inserting either phase gives another Dyck word. This proves that edges are uniquely indexed by \(k\ge1\) and a positive-vertex marked outside Dyck word of semilength \(n-k\). It also recalls the previously established edge formula, without claiming it as new.

**2. Classification of every triangle.** For three distinct pairwise adjacent binary words \(x,y,z\), write \(I_{xy}, I_{xz}, I_{yz}\) for the intervals of positions where each pair differs. Every pair differs at *every* position of its interval, and nowhere else, because the phase words are complements. At every coordinate, binary XOR gives \(\mathbf1_{I_{xy}}\oplus\mathbf1_{I_{xz}}=\mathbf1_{I_{yz}}\). As each support is itself one contiguous nonempty interval, this forces two of the intervals to have disjoint interiors and meet consecutively at a cut, while the third equals their union: indeed, if two intervals overlap in a nonempty part but neither contains the other, their XOR has two separated components; if one is properly contained in the other away from an endpoint, their XOR again has two separated components. The only remaining possibility is two adjacent pieces or one shared endpoint with an interval being their difference; in either description the third support is the union. Since the three source words are distinct, all three supports are nonempty, and the longest interval is uniquely determined.

Let its length be \(2k\). The other two edge intervals each have even length, hence the unique cut is at some even internal position \(2j\), with \(1\le j<k\). The vertices at the endpoints of the long edge are \(pAq\) and \(pBq\), with \(A=(10)^k\), \(B=(01)^k\) and a common outside prefix and suffix. The third vertex agrees with one endpoint through the first piece and with the other through the second piece; it has exactly one of the two forms
\[
pA_{1:2j}B_{2j+1:2k}q\quad\text{or}\quad pB_{1:2j}A_{2j+1:2k}q.
\]
All three pairwise disagreements are therefore opposite-alternating intervals of even lengths \(2j\), \(2(k-j)\), and \(2k\). At the splice, both alternating blocks complete a balanced return to their starting height, so the third word is Dyck whenever the common insertion height is positive; conversely, the long edge's Dyck admissibility already forces that height to be positive. Thus every allowed tuple constructs exactly one unordered triangle, and the uniquely longest edge and its two interior intervals recover all tuple data, including the splice phase. No orientation or rotational multiplicity remains unaccounted for.

**3. Count the positive vertex marks.** Let \(H_r\) be the total number of positive-height marked vertices over every word in \(\mathcal D_r\). Since there are \((2r+1)C_r\) vertices in all, subtract the number of height-zero vertices. Cutting at a marked height-zero vertex uniquely yields an ordered pair of Dyck words whose semilengths sum to \(r\). Hence the number of such marks is \([z^r]C(z)^2=C_{r+1}\), using \(C(z)=1+zC(z)^2\). Therefore
\[
H_r=(2r+1)C_r-C_{r+1}=\binom{2r+1}{r-1} \quad (r\ge1),\qquad H_0=0.
\]
For a fixed \(k\), choose any one of the \(H_{n-k}\) positive context vertices, any one of the \(k-1\) internal even cuts, and one of two splice phases. Summing these disjoint cases gives \(T_n=2\sum_{k=2}^{n-1}(k-1)H_{n-k}\), i.e., the stated formula.

**4. The cumulative relation and series.** The edge bijection of Step 1 gives \(E_n=\sum_{r=1}^{n-1}H_r\). Consequently
\[
T_n=2\sum_{r=1}^{n-2}(n-r-1)H_r=2\sum_{j=1}^{n-1}E_j,
\]
which proves \(T_{n+1}-T_n=2E_n\), including boundary cases. Summing formally over nonnegative integers yields \(H(z)=C(z)+2zC'(z)-C(z)^2\) and the two rational-in-Catalan-function expressions in the theorem.

**5. Asymptotics.** The standard Catalan estimate \(C_r\sim4^r/(\sqrt\pi r^{3/2})\) implies \(H_r\sim2rC_r\). Since \(H_{r-1}/H_r\to1/4\), the reversed weighted sum has limiting geometric weight \(\sum_{a\ge1}a4^{-a}=4/9\). In detail, \(T_n=2\sum_{a\ge1}aH_{n-1-a}\) with absent negative-index terms; for fixed \(a\), \(H_{n-1-a}/(nC_n)\to 2\cdot4^{-(a+1)}\). A uniform eventual geometric bound on backward ratios provides dominated convergence; hence \(T_n/(nC_n)\to4/9\). Together with the established \(E_n\sim(2/3)nC_n\), the incident-triangle ratio tends to \(3(4/9)/(2/3)=2\).

## Verification
The two self-contained Python 3 programs `verify_direct.py` and `verify_motifs.py` are included. Execute each with the Python 3 standard library from the directory containing these files. The first constructs the full one-deletion-output sets independently, assembles the entire graph from exact pairwise intersections, checks that no pair has more than two common descendants, and counts every triangle through semilength eight. It matches \(0,0,2,14,68,290,1172,4628\), and independently checks edge counts. The second enumerates all positive-height marked contexts and the two splice-phase constructions, checks uniqueness and Dyck validity of the motifs, and checks the exact formula through semilength eight; it also verifies the positive-vertex binomial identity through semilength nine. These finite checks are consistency tests and do not extend the proof's quantifiers.

## Relationship to prior work
Sala–Gabrys–Schoeny–Dolecek (2016) investigated exact sequence reconstruction from synchronization edits, motivating the older archive-era setting but not the present Dyck-induced graph. Cai–Kiah–Nguyen–Yaakobi (2020) established the Type-A pairwise intersection criterion used in Step 1. Chrisnata–Kiah–Yaakobi (2020) studied two-read reconstruction codes and splice-based clique covers, but not an exact Dyck-restricted triangle count. An accessible mathematical result *Dyck-restricted two-read deletion graph: a vertex-marked bijection and sharp degree* establishes exactly \(E_n\), the positive-vertex edge bijection and extremal degrees; it does not count triangles. A separate result *Exact triangle spectrum of the two-read deletion-confusability graph* counts triangles over **all** unrestricted words (and alphabets), but its unrestricted count does not determine the Dyck-induced subgraph: the requisite height-positive condition is absent. The new assertion here is the exact Dyck triangle classification and the cumulative identity \(T_{n+1}-T_n=2E_n\), not the earlier edge statistics, the unrestricted triangle normal form, or the Catalan number sequence.

## Limitations
This is a count of **pairwise-confusable graph triangles**, not a count of triples sharing the same two deletion outputs and not a code-capacity theorem. It assumes the published Type-A deletion-intersection criterion. The proof and computations do not determine four-cycles, arbitrary cliques or independence numbers. The integral triangle sequence may occur in other combinatorial guises; no priority claim is made for its bare integer values, and unindexed or differently presented equivalent results remain possible. The verification programs are finite corroboration, not an independent validation of the proof.

## References
1. F. Sala, R. Gabrys, C. Schoeny, and L. Dolecek, *Exact Reconstruction from Insertions in Synchronization Codes*, arXiv:1604.03000v1, first public 2016-04-11, https://arxiv.org/abs/1604.03000.
2. K. Cai, H. M. Kiah, T. T. Nguyen, and E. Yaakobi, *Coding for Sequence Reconstruction for Single Edits*, arXiv:2001.01376, first public 2020-01-06, Proposition 9, https://arxiv.org/html/2001.01376v2.
3. J. Chrisnata, H. M. Kiah, and E. Yaakobi, *Optimal Reconstruction Codes for Deletion Channels*, arXiv:2004.06032v1, first public 2020-04-13, https://arxiv.org/html/2004.06032v1.
4. *Dyck-restricted two-read deletion graph: a vertex-marked bijection and sharp degree*, mathematical research record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-dyck-restricted-two-read-deletion-graph-a-vertex-marked-bijectio--3635f93f657f.
5. *Exact triangle spectrum of the two-read deletion-confusability graph*, mathematical research record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-triangle-spectrum-of-the-two-read-deletion-confusability-g--e753c7b5bfd6.
6. *Exact edge count of the finite-alphabet two-read single-deletion reconstruction graph*, mathematical research record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-edge-count-of-the-finite-alphabet-two-read-single-deletion--737fed325e91.
