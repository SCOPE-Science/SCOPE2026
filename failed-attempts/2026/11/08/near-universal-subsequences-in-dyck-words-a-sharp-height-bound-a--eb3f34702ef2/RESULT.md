# Near-universal subsequences in Dyck words: a sharp height bound and the first three exact layers

## Finding
Let \(\mathcal D_n\) be all length-\(2n\) Dyck words: binary words with \(n\) zeroes, \(n\) ones, and at least as many zeroes as ones in each prefix. Put \(\iota(w)\) equal to the greatest \(k\) for which **every** binary length-\(k\) word is a scattered subsequence of \(w\). Let \(H(w)\) be the maximum prefix excess of zeroes over ones.

**Theorem.** For every \(n\ge1\) and \(w\in\mathcal D_n\),
\[
\iota(w)\le n-H(w)+1.
\]
For every feasible height \(1\le h\le n\), this upper bound is attained by \(0^h1^h(01)^{n-h}\). Define \(D_{n,k}=|\{w\in\mathcal D_n:\iota(w)=k\}|\). Then
\[
D_{n,n}=1\quad(n\ge1),\qquad D_{n,n-1}=2^{n-1}-1\quad(n\ge2),
\]
\[
\boxed{D_{n,n-2}=(n-2)(n+1)2^{n-5}}\qquad(n\ge3).
\]
The union of the two highest-index layers consists **exactly** of the height-at-most-two Dyck paths, equivalently the words
\[
0B_1B_2\cdots B_{n-1}1,\qquad B_j\in\{01,10\}.
\]
Among these words, the number with exactly \(p\) peaks (factors `01`) is \(\binom n{2p-n}\) for \(\lceil n/2\rceil\le p\le n\) and zero otherwise. The peak enumerator is a classical refinement of bounded-height Dyck paths; the new claim is its relation to the universality index and especially the complete third-layer count.

## Assumptions and scope
The ambient subsequence alphabet is fixed to \(\{0,1\}\); subsequences need not be contiguous. Empty words belong to the Dyck language for generating functions; all enumerated claims involving \(n\) above specify \(n\ge1\). The parameter \(H(w)\) is maximum prefix balance, not number of returns or maximum run length. The theorem concerns every Dyck word of given semilength, not just Dyck factors appearing in one infinite word. In the third-layer formula, \(n\ge3\) is essential.

## Proof
**1. Arch matching and height.** Greedy binary arch factorization repeatedly takes the shortest prefix containing both letters. Each completed arch has shape \(a^r\bar a\), \(r\ge1\), and contributes one to the universality index (the standard arch theorem). Its last two positions form adjacent unequal letters. Conversely, any ordered family of \(k\) disjoint neighboring unequal-letter pairs forces the greedy arch process to complete at least \(k\) arches: choosing the earliest finishing adjacent unequal pair never reduces the maximum number of disjoint such pairs. Therefore \(\iota(w)\) equals the maximum size of a matching of adjacent unequal-letter edges in the positional path.

Take an optimal matching of size \(k\) in a Dyck word. Each matched pair has one zero and one one, leaving exactly \(n-k\) unmatched zeroes and \(n-k\) unmatched ones. At any prefix, all fully included matched pairs contribute zero balance; at most one matched edge crosses the prefix boundary and contributes at most \(1\). The unmatched letters contribute balance at most \(n-k\). Hence \(H(w)\le n-k+1\), proving the bound. For \(w=0^h1^h(01)^{n-h}\), the greedy arch process completes one arch within the initial hills and \(n-h\) after them (the first unmatched one can be absorbed into the first arch), hence \(\iota=n-h+1\), establishing sharpness.

**2. The two top layers.** A Dyck word has \(\iota=n\) exactly when it admits a perfect adjacent-unlike matching. Such a matching must use the pairs of positions \((1,2),(3,4),\ldots,(2n-1,2n)\); the Dyck prefix condition forces each pair to be `01`. Thus only \((01)^n\) qualifies. For any \(\iota\ge n-1\), the height bound gives \(H\le2\). Conversely, every height-at-most-two path has the unique form \(0B_1\cdots B_{n-1}1\) with \(B_j\in\{01,10\}\). The interior \(n-1\) blocks give an explicit matching of unlike neighboring positions. Thus \(D_{n,n}+D_{n,n-1}=2^{n-1}\). The peak polynomial of these words is obtained by recording contributions at block junctions (or by diagonalizing the two-state peak transfer), giving \(\sum_p\binom n{2p-n}v^p\).

**3. Height-three arch enumerator.** Any \(w\) with \(\iota(w)=n-2\) has \(H(w)\le3\), so a bounded-height generating function is exhaustive for this entire layer. Introduce formal variables \(x\) for each `0` step (thus semilength in a Dyck path) and \(u\) for each finished greedy arch. The automaton states `e,z,o` respectively mean no letter currently seen in an unfinished arch, only zeroes seen, and only ones seen. The weighted transition matrices (row source, column destination) are
\[
A=\begin{pmatrix}0&1&0\\0&1&0\\u&0&0\end{pmatrix},\qquad
B=\begin{pmatrix}0&0&1\\u&0&0\\0&0&1\end{pmatrix}.
\]
These matrices record completed arches exactly, independent of Dyck height. Set \(M_0=I_3\) and, recursively for \(j=1,2,3\),
\[
M_j=(I_3-xAM_{j-1}B)^{-1}
\]
in the ring of formal power-series matrices. Every height-at-most-\(j\) Dyck path is uniquely a sequence of primitive factors `0` (height-at-most-\(j-1\) Dyck path) `1`. Consequently \(M_j\) counts those paths together with initial/final arch states; this is a formal geometric series, not a numerical limit. Summing the first row of \(M_3\) over all final states gives
\[
F_3(x,u)=\frac{1-4ux+ux^2+ux^3+4u^2x^2-3u^2x^3}{(1-ux)(1-4ux+4u^2x^2-u^2x^3)}.
\]
The formula follows by ordinary finite \(3\times3\) matrix inversion, with every denominator having constant coefficient \(1\) as a series in \(x\). Substitute \(x=zt\) and \(u=t^{-1}\); \(z\) marks semilength and \(t\) marks deficit \(n-\iota\). Simplification gives
\[
G_3(z,t)=\frac{(1-2z)^2+t(z^2-3z^3)+t^2z^3}{(1-z)((1-2z)^2-tz^3)}.
\]
Extracting \(t^2\) yields
\[
[t^2]G_3(z,t)=\frac{z^3(1-z)}{(1-2z)^3},
\]
and the coefficient of \(z^n\), for \(n\ge3\), is \((n-2)(n+1)2^{n-5}\). The height bound ensures no omitted path of height above three can contribute. This proves the third layer for **all** semilengths, not just the finite test range.

## Verification
Run `python3 verify.py` (Python standard library only) in the same directory. The verifier independently enumerates all \(82{,}499\) nonempty Dyck paths through semilength \(11\), reconstructs the universality index greedily, checks the subsequence-definition test through semilength \(6\), and verifies every displayed counting, height, and peak claim. The observed output is `VERIFY_OK n=1..11 dyck_words=82499 direct_definition_n=1..6 height_bound=PASS peak_distribution=PASS`. Separately, exact symbolic matrix inversion confirmed both displayed rational generating functions and their \(t^2\) coefficient. Exhaustive computation up to \(11\) is diagnostic; infinite completeness is furnished by the matching proof and formal matrix identities.

## Relationship to prior work
Barker, Fleischmann, Harwardt, Manea and Nowotka established the arch-based characterization of subsequence universality; this is expressly used, not claimed as new. Adamson et al. provided counting procedures for \(k\)-universal words accepted by **regular** languages (arXiv:2311.10658v1); the unrestricted Dyck language here is context-free and the theorem gives specific closed formulas for its near-maximal universality index. Adamson's earlier work covers ranking and counting words without the Dyck constraint. The published-finding corpus finding *Closed-form law for binary subsequence universality* gives \((1+z)/(1-z-2uz^2)\) for **all binary words**, not the Dyck-refined generating function or third-layer count. Barcucci et al. discuss the classical height-two Dyck family and restrictions thereof; the height-two \(2^{n-1}\) count and peak refinements are not presented as new independent enumerations. Mol, Rampersad and Shallit examine Dyck factors, power avoidance, and automatic sequences, rather than subsequence-universality-index counts over the entire Dyck language. In particular, a bound on height cannot by itself imply the exact third-layer formula: height-three paths can belong to lower index layers.

## Limitations
The count \(D_{n,n-2}\) is not a closed formula for every universality index; deeper-deficit layers require further height-state analysis. Prior unrestricted-word formulas, classical height-two enumeration and the standard arch theorem remain prior results. Literature and indexed mathematical-record searches found no statement equivalent to the full Dyck third-layer formula, but an unindexed, differently phrased result remains possible. No independent scientific validation or publication-priority claim is made.

## References
1. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, D. Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629v1 (2020-03-10), https://arxiv.org/abs/2003.04629.
2. D. Adamson et al., *\(k\)-Universality of Regular Languages*, arXiv:2311.10658v1 (2023-11-17), https://arxiv.org/abs/2311.10658.
3. D. Adamson, *Ranking and Unranking \(k\)-subsequence universal words*, arXiv:2304.04583v1 (2023-04-10), https://arxiv.org/abs/2304.04583.
4. E. Barcucci, A. Bernini, S. Bilotta, R. Pinzani, *Dyck Paths Enumerated by the Q-bonacci Numbers*, arXiv:2406.16394v1 (2024-06-24), https://arxiv.org/abs/2406.16394.
5. L. Mol, N. Rampersad, J. Shallit, *Dyck Words, Pattern Avoidance, and Automatic Sequences*, arXiv:2301.06145 (first posted 2023-01-15), https://arxiv.org/abs/2301.06145.
6. *Closed-form law for binary subsequence universality*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-closed-form-law-for-binary-subsequence-universality--e77c4e8d9f37.
