# Boolean-cube decomposition of confluent relations on finite chains

## Finding

Let \(m,n\geq 1\), let \(A_m=\{0<1<\cdots<m-1\}\) and \(B_n=\{0<1<\cdots<n-1\}\), and let \(R\subseteq A_m\times B_n\) satisfy both forward and backward confluence as defined below. Write \(r_i\) for the largest \(R\)-successor of row \(i\), or \(-1\) for an empty row, and \(c_j\) for the largest \(R\)-predecessor of column \(j\), or \(-1\) for an empty column.

**Theorem (exact normal form, enumeration and sparsification).** Both confluences hold if and only if \((r_i)_{i<m}\) and \((c_j)_{j<n}\) are weakly increasing. A weakly increasing pair \((r,c)\), with \(-1\le r_i<n\) and \(-1\le c_j<m\), is realized by a relation if and only if
\[
\bigl(\forall i<m\;[r_i\geq0\Rightarrow c_{r_i}\geq i]\bigr)
\quad\text{and}\quad
\bigl(\forall j<n\;[c_j\geq0\Rightarrow r_{c_j}\geq j]\bigr).
\]
For every such pair put
\[
L(r,c)=\{(i,r_i):r_i\geq0\}\cup\{(c_j,j):c_j\geq0\},\qquad
U(r,c)=\{(i,j):j\leq r_i,\ i\leq c_j\}.
\]
Its entire fiber is precisely the Boolean interval \(\{R:L(r,c)\subseteq R\subseteq U(r,c)\}\). Every member satisfies both confluences, and every such relation belongs to exactly one interval. Thus the full arrow enumerator is
\[
F_{m,n}(q)=\sum_{\substack{r,c\text{ weakly increasing}\\\text{jointly feasible}}}
q^{|L(r,c)|}(1+q)^{d(r,c)},
\qquad d(r,c)=\#\{(i,j):j<r_i,\ i<c_j\}.
\]
Here the coefficient of \(q^k\) counts confluent relations with exactly \(k\) arrows. In each fiber, \(L(r,c)\) is its **unique minimum-arrow representative**. If \(R\neq\varnothing\), then \((m-1,n-1)\in R\), so its canonical representative has at most \(m+n-1\) arrows; this universal bound is attained. The largest Boolean-cube dimension is \((m-1)(n-1)\), attained by the all-last profiles; if \(m,n\ge2\), that maximizing profile pair is unique.

For \(m=n\), the numbers \(F_{n,n}(1)\), for \(n=1,2,3,4,5,6\), are respectively
\[
2,\quad9,\quad118,\quad4849,\quad697066,\quad378458905.
\]
These are exact consequences of the all-size formula, not an asymptotic extrapolation.

## Assumptions and scope

All orders are finite, nonempty, linearly ordered, and indexed starting at zero. No reflexivity, seriality, transitivity, or symmetry is assumed for \(R\). Forward confluence (FC) means that for every \(i\leq i'\) and \(iRj\) there is \(j'\geq j\) with \(i'Rj'\). Backward confluence (BC) means that for every \(j\leq j'\) and \(iRj\) there is \(i'\geq i\) with \(i'Rj'\). On a single carrier, the case \(m=n\) is the ordinary finite-chain specialization of the birelational intuitionistic modal-frame conditions. Rectangular carriers provide a typed combinatorial generalization. The profiles describe extremal incidence, not equivalence of the full modal theories of two relations.

## Proof

**1. Confluence and monotonicity.** Assume FC. Fix \(i\leq i'\). If row \(i\) is empty there is nothing to show; otherwise its maximal edge \(iRr_i\) has an FC witness \(i'Rj'\) with \(j'\geq r_i\). Thus \(r_{i'}\geq r_i\). Conversely, if all row maxima are weakly increasing, an edge \(iRj\) implies \(j\leq r_i\leq r_{i'}\); the edge \((i',r_{i'})\) witnesses FC. The same argument, transposed, proves that BC holds precisely when the column maxima \(c_j\) are weakly increasing, including empty rows or columns represented by \(-1\).

**2. Which profiles occur.** Necessity of the two feasibility inequalities is immediate: every row maximum \((i,r_i)\) belongs to column \(r_i\), and every column maximum \((c_j,j)\) belongs to row \(c_j\). Conversely, suppose the two feasibility conditions hold. Every requested row-maximum edge lies in \(U(r,c)\), since \(c_{r_i}\ge i\), and every requested column-maximum edge lies in \(U(r,c)\), since \(r_{c_j}\ge j\). Hence \(L(r,c)\subseteq U(r,c)\). Its designated edge in each nonempty row attains row maximum \(r_i\), and its designated edge in each nonempty column attains column maximum \(c_j\); the envelope allows no larger entry. Therefore \(L(r,c)\) realizes the profiles. Any relation realizing the profiles must contain their maxima \(L(r,c)\) and lie within \(U(r,c)\), and conversely any intermediate relation preserves the extrema. By step 1 all such intermediate relations satisfy FC and BC, because the common profiles are weakly increasing. Every relation determines a unique profile pair, so the intervals are disjoint and exhaustive.

**3. Free positions and generating polynomial.** A position in the envelope is not forced precisely when it is neither a row maximum nor a column maximum. As both envelope inequalities are weak and both forced alternatives are equalities, the free positions are exactly \(\{(i,j):j<r_i,\ i<c_j\}\). Every subset may be selected independently. Consequently a fiber has \(2^{d(r,c)}\) members, and its full arrow-count polynomial is \(q^{|L(r,c)|}(1+q)^{d(r,c)}\). Summing over all admissible profiles proves the formula. All expressions involve finite summation over sequences chosen with repetition from \(n+1\) and \(m+1\) symbols, so this also supplies a terminating exact enumeration procedure for any specified \(m,n\).

**4. Sharp structural bounds.** Given a nonempty relation, choose an edge \((i,j)\). FC from \(i\) to \(m-1\) yields some \((m-1,j')\) with \(j'\ge j\); BC from \(j'\) to \(n-1\) then yields \((i'',n-1)\) with \(i''\ge m-1\), forcing \(i''=m-1\). Thus the bottom-right edge is present. Its row and column both have a designated maximum at \((m-1,n-1)\), so \(L(r,c)\) contains at most \(m+n-1\) distinct edges (at most one per row plus one per column, with this overlap). The all-last profile pair \(r_i=n-1\) and \(c_j=m-1\) is realizable; its skeleton is the last row united with the last column and has exactly \(m+n-1\) edges. It is minimum in its own fiber by step 2; hence no smaller universal guarantee is possible. Every free position has \(i\leq m-2\) and \(j\leq n-2\), so \(d\leq(m-1)(n-1)\), with equality for all-last profiles. If \(m,n\ge2\), equality requires every cell of the \((m-1)\times(n-1)\) northwest rectangle to be free, forcing \(r_i=n-1\) for all \(i<m-1\) and \(c_j=m-1\) for all \(j<n-1\); monotonicity forces the remaining extrema to be last as well. When \(m=1\) or \(n=1\), the maximum dimension zero is attained by multiple profiles, so uniqueness is not asserted there.

## Verification

Two standalone, executable, standard-library source files accompany this result. Run `python3 verify.py` to enumerate weakly increasing profile pairs, test the feasibility conditions, reconstruct the exact arrow-count polynomials, and independently compare them against the quantified FC/BC definition on **74,650** Boolean relation matrices across ten rectangular shapes of size at most \(4\times4\). It also calculates all six stated square counts from the profile formula. Run `c++ -O3 -std=c++17 verify_exhaustive.cpp -o verify_exhaustive` followed by `./verify_exhaustive` for a separately implemented exhaustive count of all Boolean square matrices through size \(5\times5\), including \(2^{25}\) matrices at the largest size. Both programs passed in the recorded local execution. The all-size claim rests on the proof, not on these finite computations.

## Relationship to prior work

Marin, Padhiar and Shillito [1, Definition 2.3] use exactly the FC and BC frame requirements in the semantics of intuitionistic justification logic; their subsequent results concern soundness, completeness, modular models and semantic realisation. Balbiani, Gao, Gencer and Olivetti [2] study frames requiring FC alone, with axiomatization and a bi-nested calculus. De Groot, Shillito and Clouston [3] analyze related intuitionistic modal semantics between CK and IK. These sources motivate the frame class but do not state the two-sided finite-chain profile-fiber decomposition, all-size arrow-count enumerator or sharp canonical-sparsification bounds. The elementary equivalence of confluence with monotone maxima follows directly from the definitions; the asserted complete decomposition and enumerator are the contribution, not the confluence axioms themselves. No claim is made that the different relations in one profile fiber satisfy precisely the same modal formulas.

## Limitations

The characterization requires **finite linear orders**; it does not assert a corresponding result for branching preorders or infinite orders without attained maxima. The typed rectangular extension is combinatorial and does not itself give a Kripke model on a single carrier. The canonical representative preserves FC/BC and extrema only, not arbitrary modal truth. The numbers above are exact evaluations of the formula, not a closed elementary product or asymptotic law. Earlier equivalent combinatorial classifications under different matrix terminology remain possible and should be checked independently before presenting this as a historically first result.

## References

[1] S. Marin, P. Padhiar, I. Shillito, *Intuitionistic Justification Logic, Semantically*, Advances in Modal Logic 2026, EPTCS 447 (2026), 603–622, Definition 2.3. DOI: 10.4204/EPTCS.447.34; arXiv:2606.31884 (initial public preprint 2026-06-30). Full text: https://paaraspadhiar.com/works/aiml26.pdf.

[2] P. Balbiani, H. Gao, Ç. Gencer, N. Olivetti, *A Natural Intuitionistic Modal Logic: Axiomatization and Bi-Nested Calculus*, CSL 2024, LIPIcs 288, Article 13, DOI: 10.4230/LIPIcs.CSL.2024.13. Full text: https://drops.dagstuhl.de/storage/00lipics/lipics-vol288-csl2024/LIPIcs.CSL.2024.13/LIPIcs.CSL.2024.13.pdf.

[3] J. de Groot, I. Shillito, R. Clouston, *Semantical Analysis of Intuitionistic Modal Logics between CK and IK*, LICS 2025. Preprint: https://www.ti.inf.uni-due.de/misc/lics2025/preprints/deGroot-Shillito-Clouston.pdf.
