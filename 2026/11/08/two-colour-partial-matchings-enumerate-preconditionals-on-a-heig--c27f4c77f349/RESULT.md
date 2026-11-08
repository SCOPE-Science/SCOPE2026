# Two-colour partial matchings enumerate preconditionals on a height-three coatom extension

## Finding
For each integer \(m\ge1\), let \(E_m=\{0,a_1,\ldots,a_m,c,1\}\) be the bounded lattice satisfying \(0<a_i<c<1\) for every \(i\), with distinct atoms incomparable, \(a_i\wedge a_j=0\), and \(a_i\vee a_j=c\) for \(i\ne j\). A \(\mathsf T\)-preconditional satisfies Holliday's five axioms (P1)--(P5), conditional identity, and semicomplementation; an \(\mathsf F\)-preconditional additionally satisfies double-negation inflation. Operations are counted on this fixed, labelled lattice.

**Normal form.** Every \(\mathsf T\)-preconditional is uniquely described by (i) a map \(h:\{1,\ldots,m\}\to\{0,a_1,\ldots,a_m\}\) with \(h(i)\ne a_i\); and (ii) a subset \(S\subseteq\{1,\ldots,m\}\) such that no atom indexed by \(S\) occurs as a nonzero value of \(h\). Its entire table is
\[
0\to x=1,\quad 1\to x=x,\quad
 a_i\to x=\begin{cases}1,&x\in\{a_i,c,1\},\\ h(i),&\text{otherwise},\end{cases}
\]
and
\[
c\to0=0,\qquad c\to a_j=\begin{cases}1,&j\in S,\\ a_j,&j\notin S,\end{cases}
\qquad c\to c=c\to1=1.
\]
It is \(\mathsf F\) precisely when the nonzero arrows of \(h\) form disjoint reciprocal pairs, i.e. a partial matching. Unmatched atoms have two independent colours according to membership in \(S\); endpoints of matched pairs cannot belong to \(S\).

**Exact enumeration.** If \(T_m\) and \(F_m\) are the numbers of labelled \(\mathsf T\)- and \(\mathsf F\)-preconditionals on \(E_m\), then
\[
T_m=\sum_{s=0}^m\binom ms(m-s+1)^s(m-s)^{m-s},\qquad
F_m=\sum_{j=0}^{\lfloor m/2\rfloor}\frac{m!\,2^{m-2j}}{2^j j!(m-2j)!}.
\]
Here \(0^0=1\). The exponential generating function for the latter numbers, with a formal \(m=0\) term, is
\[\sum_{m\ge0}\frac{F_m}{m!}z^m=\exp(2z+z^2/2).\]
Under the full automorphism group of \(E_m\), the \(\mathsf F\)-expansions have exactly
\[
\sum_{j=0}^{\lfloor m/2\rfloor}(m-2j+1)=\left\lfloor\frac{(m+2)^2}{4}\right\rfloor
\]
isomorphism classes, parametrized by the number of matched pairs and by the number of unmatched atoms in \(S\). For \(m=1,2,3,4,5\), the respective \(\mathsf F\)-counts are \(2,5,14,43,142\), while the \(\mathsf T\)-counts are \(2,9,76,937,15006\). In particular, \(E_2\) is the five-element non-chain distributive lattice having two atoms and one coatom; the formulas extend to the genuinely nondistributive lattices \(E_m\) for \(m\ge3\).

## Assumptions and scope
The exact axioms, for every \(x,y,z\), are
\[
\begin{array}{ll}
\mathrm{(P1)}&1\to x\le x,\\
\mathrm{(P2)}&x\wedge y\le x\to y,\\
\mathrm{(P3)}&x\to y\le x\to(x\wedge y),\\
\mathrm{(P4)}&x\to(y\wedge z)\le x\to y,\\
\mathrm{(P5)}&x\to((x\wedge y)\to z)\le (x\wedge y)\to z.
\end{array}
\]
Conditional identity states \(x\to x=1\), semicomplementation states \(x\wedge(x\to0)=0\), and double-negation inflation states \(x\le (x\to0)\to0\). No distributivity or residuation is assumed. All parameters are finite and positive; no inference about arbitrary finite lattices is made.

## Proof
**Forced rows.** (P1)--(P2) give \(1\to x=x\). Identity at \(0\), combined with (P3)--(P4), gives \(0\to x=1\). From (P3)--(P4), for every antecedent \(x\), the row \(q_x(y)=x\to y\) is monotone and satisfies \(q_x(y)=q_x(x\wedge y)\). For any atom \(a_i\), identity forces \(q_{a_i}(a_i)=q_{a_i}(c)=q_{a_i}(1)=1\), and all other consequents give one value \(h(i)=q_{a_i}(0)\). Semicomplementation forces \(h(i)\in\{0\}\cup\{a_j:j\ne i\}\). For the coatom \(c\), semicomplementation forces \(q_c(0)=0\), and identity gives \(q_c(c)=q_c(1)=1\). (P2) gives \(q_c(a_j)\ge a_j\), hence \(q_c(a_j)\in\{a_j,c,1\}\).

**The extra layer eliminates middle values.** Use (P5) with outer antecedent \(x=c\), \(y=c\), and \(z=a_j\). It gives \(q_c(q_c(a_j))\le q_c(a_j)\). If \(q_c(a_j)=c\), the left side is \(q_c(c)=1\), a contradiction. Hence each coatom-row value is either \(a_j\) or \(1\). Define \(S=\{j:q_c(a_j)=1\}\). Now use (P5) with \(x=c\), \(y=a_i\) and \(z=0\): it gives \(q_c(h(i))\le h(i)\). If \(h(i)=a_j\), this forces \(q_c(a_j)=a_j\), i.e. \(j\notin S\). Thus \(S\) avoids the nonzero image of \(h\).

**Sufficiency.** Conversely choose any allowed \((h,S)\) and define the stated table. Every row is monotone and constant on equal meets with its antecedent. This proves (P3)--(P4), while (P1)--(P2), conditional identity, and semicomplementation follow directly from the table. It remains to prove (P5). If the outer antecedent is \(0\) or \(1\), the inequality is immediate. If it is \(a_i\), the inner antecedent is either \(0\), producing the value \(1\), or \(a_i\), whose row takes only the fixed values \(1\) and \(h(i)\); the atomic row fixes both. For outer antecedent \(c\), the inner antecedent is \(0\), an atom \(a_i\), or \(c\). In the first case the inner value is \(1\). In the second case it is \(1\) or \(h(i)\), and the image-exclusion rule ensures that \(q_c\) fixes \(h(i)\). In the third case, \(q_c\) takes values only in \(\{0,a_1,\ldots,a_m,1\}\) and fixes every value in its image, so (P5) holds. This proves the claimed \(\mathsf T\)-normal form.

**Double negation and enumeration.** The negation \(\neg x=x\to0\) satisfies \(\neg0=1\), \(\neg1=0\), \(\neg c=0\), and \(\neg a_i=h(i)\). The inflation condition at \(a_i\) is automatic when \(h(i)=0\), and when \(h(i)=a_j\) it is equivalent to \(h(j)=a_i\). Hence the nonzero arrows are disjoint two-cycles. This gives the partial-matching description of \(\mathsf F\).

Fix a subset \(S\) of size \(s\). For each \(i\in S\), the allowed \(h(i)\) values are \(0\) or one of the \(m-s\) atoms outside \(S\), giving \(m-s+1\) choices. For \(i\notin S\), exclude its own atom as well, leaving \(m-s\) choices. Multiplying and summing over \(S\) proves the formula for \(T_m\). For \(\mathsf F\), choose \(j\) disjoint pairs in \(m!/(2^j j!(m-2j)!)\) ways; each of the \(m-2j\) unmatched atoms can freely lie in or out of \(S\), giving the stated \(F_m\) and exponential generating function. Every lattice automorphism permutes the \(m\) atoms, fixing \(0,c,1\). Consequently two \(\mathsf F\)-operations are isomorphic exactly when the number \(j\) of matched pairs and the number \(s\) of coloured unmatched atoms agree. Summing \(m-2j+1\) gives the claimed class count.

## Verification
Run `python3 checker.py` in this directory. For each \(1\le m\le4\), it explicitly constructs all pairs \((h,S)\), directly checks each of (P1)--(P5), conditional identity, semicomplementation and double-negation inflation over the full finite lattice, and verifies \(T_m\), \(F_m\) and the isomorphism parameters. Its final output is `POINTED_COATOM_PRECONDITIONAL_CHECKS_OK`. An independent exhaustive row-candidate enumeration, based only on the elementary row inequalities, additionally produced \((T_m,F_m)=(2,2),(9,5),(76,14)\) for \(m=1,2,3\). These finite calculations test but do not prove the formulas for all \(m\).

## Relationship to prior work
Holliday's *Preconditionals* (arXiv:2402.02296; Definition 1) introduces (P1)--(P5). Chen's July 22, 2026 paper (arXiv:2607.20221v1; Section 3) defines the corresponding \(\mathsf T\)- and \(\mathsf F\)-algebra classes. Earlier specific classifications include finite chains, Boolean lattices of small rank, long pentagon lattices, and height-two diamond lattices. In the height-two case, partial matchings give the uncoloured telephone numbers. The added common coatom in \(E_m\), however, introduces nontrivial coatom-row choices constrained by (P5); the resulting two-colour matching normal form, its weighted involution count, and orbit spectrum are not statements of those classifications. The comparison concerns claims and inclusion of carrier classes, not merely different titles. The general literature on involutions and matchings supplies counting methods but does not assert this algebraic classification.

## Limitations
The formulas apply to these particular height-three lattices and the stated signatures only. The finite checker is corroborative, not a proof of the infinite family. Historical-priority uncertainty remains for any uninspected specialist papers or general ordinal-sum preconditional classifications. No independent audit has been performed.

## References
1. W. H. Holliday, *Preconditionals*, arXiv:2402.02296, https://arxiv.org/pdf/2402.02296 (primary text inspected).
2. Z. Chen, *Fundamental Propositional Logic with Preconditional: Strong Completeness, Finite Model Property, and Modal Translations*, arXiv:2607.20221v1, first posted July 22, 2026, https://arxiv.org/html/2607.20221 (primary text inspected).
3. *Fixed-point normal form for finite-chain preconditionals*, October 4, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-fixed-point-normal-form-for-finite-chain-preconditionals--3d55c0067825 (published summary compared for scope; not a full-text inspection).
