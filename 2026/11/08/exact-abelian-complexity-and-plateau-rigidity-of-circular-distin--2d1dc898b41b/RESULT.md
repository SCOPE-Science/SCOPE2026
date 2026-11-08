# Exact Abelian complexity and plateau rigidity of circular distinct-run words

## Finding
Let \(q\ge3\), let \(c_0,\ldots,c_{q-1}\) be distinct letters, and let each \(a_i\ge1\). Put \(p=\sum_{i=0}^{q-1}a_i\) and consider the infinite purely periodic word
\[
X=(c_0^{a_0}c_1^{a_1}\cdots c_{q-1}^{a_{q-1}})^\omega.
\]
For every integer \(n\ge1\), let \(A_X(n)\) be the number of different Parikh vectors of contiguous length-\(n\) factors of \(X\). Write \(r=n\bmod p\). Then
\[
A_X(n)=\begin{cases}
1,&r=0,\\
p-\displaystyle\sum_{i=0}^{q-1}\bigl[(a_i-r)_++(a_i-p+r)_+\bigr],&1\le r<p,
\end{cases}
\qquad (t)_+=\max(t,0).
\]
For nonzero residues the profile is symmetric and discretely concave; it depends on the run lengths only as a multiset. In particular, with \(M=\max_i a_i\),
\[
\max_{1\le r<p}A_X(r)=\min\{p,2(p-M)\},
\]
and the maximizing residues are **exactly** the integers satisfying
\[
\min\{M,p-M\}\le r\le\max\{M,p-M\}.
\]
Thus the full-periodic abelian-complexity spectrum and all its maxima admit closed formulas independent of the cyclic ordering of distinct run labels.

## Assumptions and scope
All run lengths are strictly positive integers; each symbol occurs in exactly one run per displayed period, and there are at least three distinct symbols. The word is one-sided infinite but every cyclic phase of its displayed period occurs as a factor start. A *Parikh vector* lists the number of copies of each distinct symbol. The period \(p\) is minimal because the cyclic sequence contains a single run of each distinct symbol. The theorem counts equivalence classes, not numbers of starting positions. It is not asserted for two symbols, repeated symbol labels in different runs, or noncontiguous subsequences.

## Proof
**Step 1: remove whole periods.** Write \(n=mp+r\) with \(m\ge0\) and \(0\le r<p\). At each phase, a length-\(n\) factor has Parikh vector \(m(a_0,\ldots,a_{q-1})\) plus that of the cyclic interval of length \(r\) beginning at the phase. Hence its distinct vectors depend only on \(r\), with value one for \(r=0\).

**Step 2: rigidity of equal-composition cyclic intervals.** Fix \(1\le r<p\) and orient the displayed runs around a circle. Consider a cyclic interval whose Parikh support is proper and contains at least two letters. Since each letter occupies one run, its support is a proper consecutive set of runs; because \(q\ge3\), the circular order and omitted run(s) determine its unique first and last supported run. The positive counts of those two endpoint letters determine the start and end positions. Thus this Parikh vector occurs at exactly one start phase. If the support contains only one letter, its phases are precisely the contiguous set of positions inside the corresponding run at which a length-\(r\) interval fits.

If instead the interval uses all \(q\) letters, consider the complementary circular interval of length \(p-r\). It contains at most two letters: the original interval visits every run but is shorter than one full turn, so the complement lies entirely between its last and first visited run, which are consecutive around the circle. Since its Parikh vector is the fixed total vector \((a_0,\ldots,a_{q-1})\) minus the original vector, the same preceding argument applies to the complement. Translation by \(r\) between complementary start phases preserves contiguity. **Consequently, for each Parikh vector the start phases realizing it constitute one nonempty connected block of the cyclic phase circle.** In particular two different such blocks cannot carry the same vector.

**Step 3: count phase transitions.** Let \(V_s\) be the Parikh vector of the circular length-\(r\) interval beginning at phase \(s\in\mathbb Z/p\mathbb Z\). As the interval slides one step,
\[
V_{s+1}-V_s=e_{x_{s+r}}-e_{x_s},
\]
where \(x_s\) is the letter at phase \(s\) and \(e_c\) is the unit vector of letter \(c\). Thus \(V_{s+1}=V_s\) exactly when \(x_s=x_{s+r}\). For a run of length \(a_i\), this happens either if the clockwise distance \(r\) stays inside the run, contributing \((a_i-r)_+\) phase starts, or if the counterclockwise distance \(p-r\) stays inside it, contributing \((a_i-p+r)_+\). These alternatives count disjoint ordered phase pairs when \(0<r<p\), including when both are possible in a long run. Thus precisely
\[
E(r)=\sum_i\bigl[(a_i-r)_++(a_i-p+r)_+\bigr]
\]
of the \(p\) consecutive phase edges have equal vectors. Since the phase-vector sequence is not constant for \(0<r<p\) (any change in the run labels forces some change), its equal-vector blocks number \(p-E(r)\). By Step 2 each block is one **different** Parikh vector. This yields the formula.

**Step 4: shape and exact plateau.** Each positive-part summand \((a_i-r)_++(a_i-p+r)_+\) is a convex, nonnegative, symmetric function of the real variable \(r\) about \(p/2\). Therefore \(p-E(r)\) is symmetric and concave (also on the integer residues). Let \(M=\max_i a_i\). When \(M\le p/2\), every summand vanishes exactly throughout \(M\le r\le p-M\); outside this interval the summand from a longest run is positive. Hence the maximum is \(p\), with exactly those maximizing residues. When \(M>p/2\), the summand of the (necessarily unique) longest run is at least \(2M-p\), attaining this minimum precisely for \(p-M\le r\le M\). The other runs have lengths at most \(p-M\), so their summands vanish throughout this interval. Outside it the longest-run contribution strictly increases. The maximum is therefore \(p-(2M-p)=2(p-M)\), with exactly the stated maximizers. Both cases are summarized by the displayed expressions. \(\square\)

## Verification
The supplied standalone Python checker independently enumerates every phase and Parikh vector for positive run lengths in the exhaustive ranges \(q=3,a_i\le6\), \(q=4,a_i\le5\), \(q=5,a_i\le4\), \(q=6,a_i\le3\). It also checks \(750\) seeded larger profiles up to eight distinct run symbols. It tests the exact formula, symmetry, discrete concavity, maximum value and **full set** of maximizing residues. There are \(3344\) tested profiles. These finite checks corroborate, but do not replace, the general proof in Steps 1–4.

Run with Python 3: `python verification/check.py`.

## Relationship to prior work
Fici and Puzynina's survey [1], Sections 3.1–3.2, defines abelian factor complexity and explains bounded complexity for periodic words; it does not state the exact distinct-run cyclic formula or the phase-block rigidity and plateau theorem shown here. Chen and Wen [2], Theorems 1–2, compute abelian complexities for generalized Thue–Morse morphic sequences and prove an automaticity conclusion for related sequences; those objects are not the distinct-run periodic words here. The common general observation that a periodic word has bounded abelian complexity does not determine its exact spectrum. A known complete coordinate-permutation symmetry classification for related cyclic languages addresses coordinate group actions, not the cardinality of Parikh-vector images of every length; neither conclusion implies the other without additional classification.

## Limitations
The distinct-run-label and three-letter assumptions are essential to Step 2; for binary cycles with two runs, a given two-symbol composition may be achieved through both oriented boundaries, so this proof does not apply. No formula is claimed for arbitrary periodic words with repeated labels in nonadjacent runs. Exact bibliographic uniqueness cannot be guaranteed; there remains a possibility of an unindexed equivalent formula. Computational checks are bounded, and independent validation has not been performed.

## References
[1] Gabriele Fici and Svetlana Puzynina, *Abelian Combinatorics on Words: a Survey*, arXiv:2207.09937, first posted 2022-07-20, Sections 3.1–3.2, https://arxiv.org/abs/2207.09937 (full text: https://arxiv.org/html/2207.09937v2).

[2] Jin Chen and Zhi-Xiong Wen, *On the abelian complexity of generalized Thue-Morse sequences*, arXiv:1809.06554, Theorems 1–2, https://arxiv.org/html/1809.06554v2.
