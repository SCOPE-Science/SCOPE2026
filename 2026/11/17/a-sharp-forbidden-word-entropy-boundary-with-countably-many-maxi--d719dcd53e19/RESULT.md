# A sharp forbidden-word entropy boundary with countably many maximal-entropy phases

## Finding
Fix an integer \(q\ge2\), and take two disjoint alphabets \(B,C\) each containing exactly \(q\) symbols. Let \(X_q\subseteq(B\cup C)^{\mathbb Z}\) contain exactly the bi-infinite sequences for which either the set of positions occupied by \(C\) is empty or a singleton, or it equals one complete residue class modulo some integer \(k\ge2\). At all positions the choice of the actual symbol within the designated alphabet is arbitrary. Let \(\sigma\) denote the left shift. Then \(X_q\) is a compact subshift, and for every integer \(n\ge2\) its exact number of length-\(n\) words is
\[
 |\mathcal L_n(X_q)|=q^n\left(n+\left\lfloor n^2/4\right\rfloor\right).
\]
In particular, \(h_{\rm top}(X_q)=\log q>0\). There are precisely countably infinitely many ergodic measures of maximal entropy: one uniform Bernoulli measure supported on \(B^{\mathbb Z}\), and for each \(k\ge2\), one measure supported on the component whose \(C\)-positions form a residue class modulo \(k\). The latter is uniform over its \(k\) phases, with independent uniform symbol choices conditioned on the phase.

Writing \(M_n(X_q)\) for the set of minimal forbidden length-\(n\) words, their *exact* census is
\[
 |M_n(X_q)|=\begin{cases}q^2,&n=2,\\2q^n,&n=2k+1\text{ for an integer }k\ge2,\\0,&\text{otherwise}.\end{cases}
\]
Thus the minimal-forbidden-word entropy defined by the limsup exponential growth rate is \(h_M(X_q)=\log q=h_{\rm top}(X_q)\). The strict inequality hypothesis in the finite-maximal-measure criterion therefore cannot be weakened to a non-strict inequality, even for a positive-entropy finite-alphabet subshift with a completely explicit antidictionary.

Finally, letting \(\sigma_1(n)=\sum_{d\mid n}d\), the exact periodic-point count and Artin–Mazur zeta function are
\[
 |\operatorname{Fix}(\sigma^n)|=q^n\sigma_1(n),\qquad
 \zeta_{X_q}(z)=\exp\left(\sum_{n\ge1}\frac{q^n\sigma_1(n)}n z^n\right)=\prod_{k\ge1}\frac1{1-(qz)^k}.
\]
The Euler product holds as a formal power series and analytically for \(|z|<1/q\).

## Assumptions and scope
The space is the *two-sided* full shift on a finite alphabet of \(2q\) symbols, with product topology. The components comprise \(X_k\) for each integer \(k\ge2\), whose marker positions occupy exactly one congruence class modulo \(k\), together with \(X_\infty\), whose members have at most one marker. A word is minimal forbidden when it is absent but all its proper contiguous factors occur. All logarithms are natural. An ergodic maximal-entropy measure is a \(\sigma\)-ergodic invariant Borel probability measure of entropy \(h_{\rm top}(X_q)\).

## Proof
**Compactness.** Each \(X_k\) and \(X_\infty\) is shift invariant and closed. In any convergent sequence of points selected from the components, either a fixed period \(k\) occurs along a subsequence or the selected periods tend to infinity. In the latter case, any finite coordinate window eventually contains at most one marker. The limit therefore belongs to \(X_\infty\). Conversely, every at-most-one-marker point belongs by definition. Hence \(X_q=X_\infty\cup\bigcup_{k\ge2}X_k\) is closed, so it is compact.

**Exact language.** Project every symbol to the indicator \(1\) for membership in \(C\) and \(0\) for membership in \(B\). A binary length-\(n\) pattern occurs precisely when it contains at most one \(1\), or its \(1\)-positions form an arithmetic progression with a common spacing \(k\ge2\), whose first position is strictly less than \(k\) and whose number of trailing zeros is also strictly less than \(k\). The latter two restrictions are necessary and sufficient for extension to a complete period-\(k\) marker class on both sides. There are \(n+1\) binary patterns with zero or one marker. For each \(2\le k\le n-1\), there are exactly \(\min\{k,n-k\}\) patterns with at least two markers and spacing \(k\), since the first marker may occupy any of those many initial positions. Their total is \(\sum_{k=2}^{n-1}\min\{k,n-k\}=\lfloor n^2/4\rfloor-1\). This yields \(n+\lfloor n^2/4\rfloor\) binary indicator patterns. Every such pattern admits exactly \(q^n\) distinct colorings because ordinary and marker alphabets both have cardinality \(q\). The exponential growth rate is \(\log q\).

**Minimal forbidden words.** Binary indicator patterns of length two first fail at \(11\). For \(k\ge2\), the two patterns
\[
 0^k 1 0^{k-1}1\quad\text{and}\quad1 0^{k-1}1 0^k
\]
are forbidden because a pair of markers has respectively too much leading or trailing space for its spacing \(k\); deleting either endpoint makes the pattern legal. They are the only minimal forbidden indicators. To see completeness, take an illegal indicator with both its length-\((n-1)\) prefix and suffix legal. If it contains exactly two markers, the only possibility beyond \(11\) is an excessive initial or terminal gap, and minimality forces the exact two displayed patterns. If it contains at least three markers, let the initial three markers have successive gaps \(d\) and \(e\). Legality of the one-letter prefix truncation forces \(e\le d\), while legality of the suffix truncation forces \(d\le e\), so \(d=e\). The same argument applied to successive triples forces all marker gaps equal; legality of the prefix and suffix then also forces both boundary gaps to be strictly shorter than that common spacing, making the full word legal, a contradiction. This also covers non-endpoint marker configurations (where prefix/suffix contain the same complete marker set). Thus the displayed list is exhaustive. Every binary indicator word of length \(n\) has precisely \(q^n\) colored lifts; legality depends only on its indicator. A colored forbidden word is minimal forbidden exactly when its indicator is. This proves the stated complete census and \(h_M(X_q)=\log q\) by taking the limsup along odd lengths.

**Ergodic maximal measures.** The pairwise disjoint shift-invariant Borel sets \(X_\infty,X_2,X_3,\ldots\) cover \(X_q\). Any ergodic invariant measure gives full mass to precisely one of them. On \(X_k\), the \(k\) marker phases are cyclically permuted by the shift. For the \(k\)-th iterate, the restriction to any phase is a full \(q^k\)-symbol Bernoulli shift and has a unique maximal-entropy measure, the uniform Bernoulli law, of entropy \(k\log q\) per block. Averaging over the phases gives the unique \(\sigma\)-invariant maximal-entropy measure on \(X_k\) and has entropy \(\log q\). For \(X_\infty\), the set of sequences with their unique marker at a specified coordinate has the same probability for every coordinate under an invariant measure; these countably many events are disjoint, so each has probability zero. Every invariant measure on \(X_\infty\) is therefore supported on \(B^{\mathbb Z}\), whose unique maximal-entropy measure is the uniform Bernoulli measure, again of entropy \(\log q\). No other ergodic maximal-entropy measures exist.

**Periodic points and zeta.** A non-marker periodic sequence belongs to the full \(q\)-shift on \(B\), contributing \(q^n\) points fixed by \(\sigma^n\). A sequence with markers of least spacing \(k\) can be fixed by \(\sigma^n\) only if \(k\mid n\) and \(k\ge2\). For each such \(k\), exactly \(k\) marker phases are possible, and independently \(q^n\) symbols may be chosen around a length-\(n\) period. Hence the count is \(q^n[1+\sum_{k\mid n,\,k\ge2}k]=q^n\sigma_1(n)\). Taking the logarithm of the Euler product, then expanding \(-\log(1-w^k)=\sum_{j\ge1}w^{kj}/j\), gives the zeta identity coefficient by coefficient.

## Verification
The standalone Python 3 script `verify_marker.py` independently enumerates every binary indicator pattern through length sixteen, checks both exact language and minimal-forbidden layers, and enumerates every periodic word over the colored alphabet at lengths one through six for \(q=2,3\). Its expected output ends with `VERIFY_OK indicator_languages=16 indicator_minimal_layers=16 fixed_period_censuses=12`. These finite checks are corroborative: the universal statements for every \(q\), length, and period follow from the preceding symbolic proof, not from enumeration.

## Relationship to prior work
Wu and Zhang (2026, arXiv:2611.03758v1) prove that a *strict* gap between minimal-forbidden-word entropy and topological entropy suffices for finitely many ergodic maximal-entropy measures, and exhibit examples differentiating related classes. Their Section 2 definitions and their Example 1 (a distinct four-letter construction with one binary full-shift component) do not state this complete period-marker family, its all-parameter antidictionary, its countably infinite maximal-entropy phase spectrum, or its exact partition Euler-product zeta. The current result is a sharp, explicit *equality-boundary example*, not an improvement to the strict-gap theorem. Pavlov (2018) studies entropy and intrinsic ergodicity of coded subshifts under coding assumptions; it does not state these arithmetic colored-marker formulas. Previously published results about finite-period marker shifts or spacing shifts concern different subshifts and do not imply the infinite-component simultaneous enumeration without additional construction and proof. The status of broader historical priority remains provisional.

## Limitations
The family is deliberately nontransitive and its ergodic maximal-entropy measures live on disjoint invariant components; it does not provide an intrinsically ergodic counterexample or solve any mixing/transitivity-constrained version of the entropy-boundary question. The theorem does not determine the infimal *generating*-forbidden-word entropy \(h_G\), and makes no assertion about it. Completeness of the historical literature search and independent mathematical validation are not claimed.

## References
- Xinxing Wu and Xu Zhang, *Generating Forbidden Words and Measures of Maximal Entropy for Subshifts*, arXiv:2611.03758v1, first posted 2026-11-02, especially Theorem A, Corollary 1, Section 2, and Example 1. https://arxiv.org/abs/2611.03758
- Ronnie Pavlov, *On entropy and intrinsic ergodicity of coded subshifts*, arXiv:1803.05966v1, first posted 2018-03-15, especially Section 1 and Theorems 1.1–1.5. https://arxiv.org/abs/1803.05966
