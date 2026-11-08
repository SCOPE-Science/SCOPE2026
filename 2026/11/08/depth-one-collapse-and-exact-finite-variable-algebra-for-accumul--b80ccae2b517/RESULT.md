# Depth-one collapse and exact finite-variable algebra for accumulation logic on a convergent sequence

## Finding

Let \(k\ge 0\) be an integer, let \(m=2^k\), and write \(\Omega=\{0,1\}^k\). The formula algebra of the \(\omega\)-accumulation modality on the fixed convergent-sequence space \(X=\mathbb N\cup\{\infty\}\), modulo agreement at every point in every valuation, is the full Boolean algebra of functions on a set of \(m2^m\) coordinates. Equivalently, it has exactly
\[
2^{m2^m}
\]
elements, and every equivalence class has a representative of modal nesting depth at most one. The bound one is sharp. For zero, one, and two variables the respective numbers of formula classes are \(4\), \(256\), and \(2^{64}\).

## Assumptions and scope

The topology consists of all subsets of \(\mathbb N\) together with those subsets containing \(\infty\) whose complements in \(\mathbb N\) are finite. In the propositional language with \(k\) atoms, Boolean connectives and constants, interpret
\[
\lVert\Diamond\varphi\rVert=\omega(\lVert\varphi\rVert),\qquad
\omega(A)=\{x\in X:\text{every open neighborhood of }x\text{ meets }A\text{ infinitely}\}.
\]
The formula equivalence relation quantifies over **all** assignments of arbitrary subsets of \(X\) to the atoms and over **all** points of \(X\). No continuity, openness, or clopen restriction is placed on valuations. Modal depth counts nested occurrences of \(\Diamond\); \(\Box\) is defined as \(\neg\Diamond\neg\).

For each valuation, let \(a\in\Omega\) be the atomic truth vector at \(\infty\), and let \(I\subseteq\Omega\) be the nonempty set of atomic truth vectors appearing at infinitely many isolated points. Every \((a,I)\) with \(I\ne\varnothing\) is realizable: take a periodic infinite sequence using every type in \(I\), and choose the type of \(\infty\) independently. A specified isolated type \(t\in\Omega\) is also realizable at a specified finite point, regardless of \(I\), by changing finitely many isolated assignments.

## Proof

**1. The modal operator.** Every finite natural-number point is isolated, hence cannot be an accumulation point of any subset. Every neighborhood of \(\infty\) contains all but finitely many natural numbers. Therefore for each \(A\subseteq X\),
\[
\omega(A)=\begin{cases}\{\infty\},& |A\cap\mathbb N|=\infty,\\
\varnothing,& |A\cap\mathbb N|<\infty.\end{cases}
\]
In particular, \(\delta:=\Diamond\top\) holds precisely at \(\infty\), while every modal subformula is false at every isolated point.

**2. Complete semantic coordinates.** For any formula \(\varphi\), define its *isolated skeleton* \(b_\varphi\) by replacing every subformula \(\Diamond\psi\) by \(\bot\), retaining Boolean operations and atoms. At isolated points of type \(t\), formula \(\varphi\) has truth value \(b_\varphi(t)\). At the limit point define \(F_\varphi(a,I)\) recursively: atomic variables read the corresponding bit of \(a\); Boolean operations act pointwise; and
\[
F_{\Diamond\psi}(a,I)=1\quad\Longleftrightarrow\quad
I\cap\{t\in\Omega:b_\psi(t)=1\}\ne\varnothing.
\]
This is proved by induction on formulas, because an infinite union of occurrences drawn from a finite type set exists exactly when some type occurring infinitely often satisfies \(b_\psi\). The isolated and limit-point coordinates therefore completely determine every formula under all valuations.

**3. Every coordinate function is definable.** For each type \(t\in\Omega\), let \(\chi_t\) be the conjunction of positive or negative atoms specifying exactly \(t\) (the empty conjunction is \(\top\) for \(k=0\)). At the limit point, \(\Diamond\chi_t\) holds exactly when \(t\in I\). Thus for each nonempty \(J\subseteq\Omega\), the depth-one formula
\[
\eta_J:=\bigwedge_{t\in J}\Diamond\chi_t\ \land\!
\bigwedge_{t\in\Omega\setminus J}\neg\Diamond\chi_t
\]
holds at \(\infty\) exactly when \(I=J\). Given any Boolean function \(F\) on \(\Omega\times(\mathcal P(\Omega)\setminus\{\varnothing\})\), the depth-one formula
\[
G_F:=\bigvee_{(a,J):F(a,J)=1}(\chi_a\land\eta_J)
\]
attains exactly \(F\) at \(\infty\); an empty disjunction means \(\bot\). Given any Boolean function \(b\) on \(\Omega\), choose a propositional disjunction \(B_b\) of the \(\chi_t\) for which \(b(t)=1\). Then
\[
(\neg\delta\land B_b)\lor(\delta\land G_F)
\]
represents the prescribed pair \((b,F)\), has modal depth at most one, and works for every valuation.

**4. Distinctness and counting.** If two isolated functions differ at \(t\), realize \(t\) at a natural-number point to distinguish them. If two limit functions differ at \((a,J)\), realize that pair by a periodic tail and an independent limit-point assignment. Thus *all* function pairs are distinct and all are realized. The number of independent Boolean coordinates is
\[
|\Omega|+|\Omega|(2^{|\Omega|}-1)=m2^m.
\]
Hence the Boolean formula algebra is exactly \(\mathcal P(E_k)\) for a coordinate set \(E_k\) of size \(m2^m\), and has \(2^{m2^m}\) elements. Finally, \(\delta=\Diamond\top\) cannot be equivalent to any propositional formula: assign all atoms the same type at \(\infty\) and at a natural point, where propositional formulas agree but \(\delta\) differs. This proves sharp modal depth one, including \(k=0\).

## Verification

The standalone standard-library Python checker `checker.py` performs 1,680 seeded random formula/periodic-model comparisons for variable counts zero through three, directly interpreting all formula occurrences against the periodic infinite tail and comparing them to the recursive summary. It verifies all eight single-variable semantic coordinates are separated by four depth-one generators (two isolated, six limit types), and checks the explicit counts for zero, one, and two variables. These tests are finite corroboration; the preceding inductive argument supplies the all-formulas proof.

## Relationship to prior work

Montacute's *Halo Semantics for Modal Logic* (first posted June 30, 2026, arXiv:2606.31885) identifies its purely nonstandard diamond with the \(\omega\)-accumulation operator and establishes completeness theorems for classes of spaces. The operator and its topological characterization are therefore **prior mathematics**; the result here instead determines the exact all-variable finite quotient of formulas on the one-point compactification of a countable discrete space. On this Hausdorff space, the operator also coincides with the classical Cantor derivative. Bezhanishvili, Esakia, and Gabelaia (2010) prove results about derivative logics of classes of Stone spaces and ordinals; these broader topological tools are acknowledged. Their inspected article does not state the fixed-convergent-sequence finite-variable Boolean algebra count or depth-one classification. The result makes no assertion of a new modal operator or a novel general completeness theorem.

## Limitations

The classification is for one specific topology and unrestricted valuations. It does not classify arbitrary ordinal spaces, multi-modal languages, predicate/modal languages, or spaces with additional limit-point levels. The claim of absence from previously published work rests on the inspected sources and searches, not a proof of historical uniqueness. The finite test cannot substitute for the proof. Independent external review has not been performed.

## References

1. Yoàv Montacute, *Halo Semantics for Modal Logic*, EPTCS 447 (2026), 623–635, arXiv:2606.31885, DOI 10.4204/EPTCS.447.35. First public arXiv posting June 30, 2026. Definition and analysis of the purely nonstandard \(\omega\)-accumulation modality, in particular Theorem 6.4 and the completeness results in Section 6.
2. Guram Bezhanishvili, Leo Esakia, and David Gabelaia, *The Modal Logic of Stone Spaces: Diamond as Derivative*, Review of Symbolic Logic 3(1) (2010), 26–40, DOI 10.1017/S1755020309990335. Derivative interpretations and modal logics of Stone spaces, ordinals, and compact Hausdorff spaces.
3. David Fernández-Duque et al., *Dynamic Cantor Derivative Logic*, 2023, University of Cambridge repository. Background on the broader derivative-logic setting; its abstract concerns dynamical topological logic rather than this fixed-space finite-variable enumeration.
