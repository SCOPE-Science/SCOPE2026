# Sharp subexponential complexity in power-bounded density shifts

## Finding

For each real \(0<\alpha<1\), define the binary subshift
\[
X_\alpha=\left\{x\in\{0,1\}^{\mathbb Z}:\ \sum_{i=j}^{j+k-1}x_i\le\lceil k^\alpha\rceil\quad\text{for every }j\in\mathbb Z,\ k\ge1\right\}.
\]
Let \(p_\alpha(n)\) be the number of length-\(n\) words occurring in \(X_\alpha\). Then the following sharp asymptotic holds for **every** \(\alpha\) in the stated open interval:
\[
\boxed{\displaystyle\lim_{n\to\infty}\frac{\log p_\alpha(n)}{n^\alpha\log n}=1-\alpha.}
\]
The same system is topologically mixing and uniquely ergodic, with its only invariant Borel probability measure supported on the all-zero fixed point. Its classical topological entropy is zero, while its upper and lower diagonal second entropy scales both equal \(\alpha\):
\[
D_2(X_\alpha)=\lim_{n\to\infty}\frac{\log\log p_\alpha(n)}{\log n}=\alpha.
\]
The nested invariant subsystems \(X_\beta\subset X_\alpha\), for \(0<\beta\le\alpha\), together with the zero fixed point, realize every value in \([0,\alpha]\) for the same diagonal scale. The **sharp leading coefficient** of the word-growth law, rather than the general existence of sparse or zero-entropy systems, is the main finding.

## Assumptions and scope

All logarithms are natural. The parameter \(\alpha\) is a fixed real number satisfying \(0<\alpha<1\); the asymptotic error can depend on this parameter. Words are binary and every finite consecutive window, including windows crossing either edge of a displayed word after extension, obeys its bound. A word is admissible exactly when all its internal windows obey the constraints; extension by infinite zeros preserves those constraints. The shift is bilateral, with its usual product topology and left shift map. The second diagonal entropy scale is the asymptotic ratio of the double logarithm of orbit covering counts to \(\log n\); for finite-alphabet subshifts it agrees with the stated double logarithm of word complexity.

## Proof

**1. Upper word count.** A length-\(n\) word has at most \(m_n=\lceil n^\alpha\rceil\) ones. Therefore
\[
p_\alpha(n)\le\sum_{j=0}^{m_n}\binom nj
\le(m_n+1)\left(\frac{en}{m_n}\right)^{m_n}
\]
for all sufficiently large \(n\), since \(m_n<n/2\) and the binomial coefficients increase to that index. Consequently
\[
\limsup_{n\to\infty}\frac{\log p_\alpha(n)}{n^\alpha\log n}\le 1-\alpha.
\]

**2. Block-separated lower family, respecting *every* window.** Fix \(0<\delta<1\). For each sufficiently large \(n\), set
\[
m=\lfloor(1-\delta)n^\alpha\rfloor,\qquad L=\lfloor n/m\rfloor.
\]
Use the first \(mL\) sites, grouped into \(m\) consecutive cells of length \(L\). In each cell, put one \(1\) at any site in its central half (for instance the integer sites with offsets between \(\lceil L/4\rceil\) and \(\lfloor3L/4\rfloor-1\)); set all other sites to zero, including outside the displayed block. Each cell has at least \(L/3\) available positions for large \(n\). Thus there are at least \((L/3)^m\) distinct constructed words.

It remains to verify *all* sliding-window inequalities. Distinct markers are separated by at least \(L/2-O(1)\) sites. For a window of length \(k\le n\), the number of cells it meets is at most \(k/L+2\), hence its number of markers is at most that value. Since \(m\sim(1-\delta)n^\alpha\), for sufficiently large \(n\),
\[
\frac{k}{L}\le(1-\delta/2)k^\alpha\qquad(1\le k\le n).
\]
Choose the fixed integer \(K\) so large that \(2\le(\delta/2)k^\alpha\) for all \(k\ge K\). Then every \(K\le k\le n\) window has at most \(k^\alpha\) markers. Every \(k<K\) window has at most one marker once \(n\) is large enough because \(L\to\infty\), and \(\lceil k^\alpha\rceil\ge1\). Finally, a window of length \(k>n\) contains at most \(m\le n^\alpha\le k^\alpha\) markers. Therefore **every constructed word, extended by zeros in both directions, lies in** \(X_\alpha\).

It follows that
\[
\log p_\alpha(n)\ge m\log(L/3)
=(1-\delta)(1-\alpha+o(1))n^\alpha\log n.
\]
Let \(\delta\downarrow0\) to match the upper bound.

**3. Unique invariant probability and zero ordinary entropy.** If \(\mu\) is any shift-invariant probability on \(X_\alpha\), then for every integer \(k\ge1\),
\[
k\mu([1])=\int\sum_{i=0}^{k-1}x_i\,d\mu(x)\le\lceil k^\alpha\rceil.
\]
Sending \(k\to\infty\) gives \(\mu([1])=0\). By shift invariance and countable subadditivity, \(\mu\) is concentrated on the all-zero configuration. Furthermore \(\log p_\alpha(n)=o(n)\) gives \(h_{\rm top}(X_\alpha)=0\).

**4. Topological mixing.** Let \(u,v\) be arbitrary admissible words and let \(M\) be the sum of their numbers of ones. For every sufficiently long integer zero gap \(g\), the bi-infinite zero extension of \(u0^gv\) is admissible: intervals meeting at most one nonzero block obey the single-block constraints by monotonicity of \(k\mapsto\lceil k^\alpha\rceil\); intervals meeting both nonzero blocks have length at least \(g\) and at most \(M\) ones, which is permitted once \(\lceil g^\alpha\rceil\ge M\). This gives arbitrary sufficiently large connecting gaps, the mixing condition.

**5. Diagonal entropy dimension and invariant intermediate scales.** For any fixed cylinder resolution, separated orbit counts of length \(n\) are bounded above and below by \(p_\alpha(n+C)\) and \(p_\alpha(n)\) with fixed resolution-dependent \(C\). The first assertion yields \(\log\log p_\alpha(n)=\alpha\log n+\log\log n+O_\alpha(1)\). Thus both limsup and liminf in the second diagonal entropy scale equal \(\alpha\). For \(0<\beta\le\alpha\) we have \(\lceil k^\beta\rceil\le\lceil k^\alpha\rceil\), so \(X_\beta\) is a compact invariant subsystem with scale \(\beta\); the zero singleton gives scale zero.

## Verification

A standalone Python checker, `check.py`, performs integer-exact finite-window membership tests for the rational exponents \(1/2\), \(2/3\), and \(3/4\); exhaustive word counts for lengths up to 12; and randomized choices from the large-cell construction. It reports 468 passed cases on its recorded invocation. It also compares the exponent-dependent occupancy bounds. The checker is a finite consistency test, **not** the proof of an infinite asymptotic or the assertion that all possible finite parameters were enumerated. The decisive all-length bound is the three-range analytic window argument above.

## Relationship to prior work

Huang and Li (2026), motivating the study of diagonal scales, prove hereditary lowerability by **compact subsets without invariance requirements**. Their general theorem does not give a sharp coefficient for the word complexity of this bounded-density shift, or its nested invariant realizations. Bounded density shifts themselves were introduced by Stanley (2013). Gangloff and Hellouin de Menibus (2016) prove the zero-entropy upper-density implication by a binomial upper bound and show that zero extension preserves admissibility; both ingredients are credited here rather than presented as new. García-Ramos, Pavlov, and Reyes (2024; preprint 2023) prove general facts about maximal-entropy measures and the zero-versus-positive topological entropy dichotomy for bounded density shifts, not the above stretched-exponential coefficient. Distinct published sparse-shift and diagonal-entropy constructions concern other constraints or noninvariant compact sets, and were compared on their statements, not their titles. An earlier occurrence of an equivalent sharp power-density word-count law remains possible, particularly in the inaccessible original full text of Stanley (2013).

## Limitations

The leading coefficient is proved for fixed \(0<\alpha<1\), without a uniform error estimate approaching the endpoints. The result is not an exact finite-length formula, a complete classification of invariant subsets, or a new instance of positive ordinary topological entropy. The claimed invariant-scale spectrum is an explicit **realization** within one ambient shift, not a statement about the scales of *every* invariant subsystem. The mathematical novelty assessment is provisional and not independently audited.

## References

1. X. Huang and Z. Li, *Hereditary lowerability of diagonal entropy scales*, arXiv:2611.02638v1, first posted 2 November 2026. https://arxiv.org/abs/2611.02638
2. B. Stanley, *Bounded density shifts*, *Ergodic Theory and Dynamical Systems* **33** (2013), 1891–1928. https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/issue/7D43A8CC74494D0314ED9668951A4B2A
3. S. Gangloff and B. Hellouin de Menibus, *Computing the entropy of one-dimensional decidable subshifts*, sections 3.3.1–3.3.3, preprint available at https://www.researchgate.net/publication/301844380_Computing_the_entropy_of_one-dimensional_decidable_subshifts
4. F. García-Ramos, R. Pavlov, and C. Reyes, *Measures of maximal entropy of bounded density shifts*, *Ergodic Theory and Dynamical Systems* **44** (2024), 2960–2974; first arXiv posting 14 February 2023, https://arxiv.org/abs/2302.07307
