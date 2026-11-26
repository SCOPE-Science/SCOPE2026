# Universal composition-commutation of nuclei on finite Heyting frames

## Finding

Let \(P\) be a finite poset and \(H(P)=\operatorname{Up}(P)\) the Heyting algebra of its upsets. For each \(S\subseteq P\), put
\[
j_S(U)=\{x\in P:\uparrow x\cap S\subseteq U\},\qquad U\in H(P).
\]
The following conditions are equivalent for every \(S\subseteq P\):

1. \(j_S\circ j_T=j_T\circ j_S\) for every \(T\subseteq P\).
2. \(j_S\circ j_{\{p\}}=j_{\{p\}}\circ j_S\) for every \(p\in P\).
3. \(j_S(j_{\{p\}}(\varnothing))=j_{\{p\}}(j_S(\varnothing))\) for every \(p\in P\).
4. \(S\) is a union of connected components in the undirected comparability graph of \(P\).

Every nucleus on \(H(P)\) has a unique representation \(j_S\). Consequently, if \(c(P)\) is the number of comparability-connected components, the exact number of nuclei commuting with **every** nucleus is
\[
\boxed{2^{c(P)}}.
\]
For distinct points \(p,q\), their singleton nuclei commute if and only if \(p\) and \(q\) are incomparable. Thus the pairwise commutation relation of canonical singleton nuclei detects the entire comparability graph, while testing the single input \(\varnothing\) for each singleton detects the universal commutant.

## Assumptions and scope

The poset \(P\) is finite (possibly empty); no connectedness, greatest element, or rootedness condition is imposed. An upset \(U\) satisfies \(x\in U,\ x\le y\Rightarrow y\in U\), and \(\uparrow x=\{y:x\le y\}\). A nucleus on \(H(P)\) is an extensive, monotone, idempotent, finite-meet-preserving self-map. Two nuclei *commute* precisely when their two function compositions agree pointwise on every upset. Although the nuclei form an ordered frame under pointwise comparison, compositions of arbitrary nuclei need not themselves be nuclei. No monoid-of-nuclei assumption is made.

The comparability graph has vertices \(P\) and joins distinct comparable points by an undirected edge. By convention \(c(\varnothing)=0\), and the one-element algebra of upsets of the empty poset has one nucleus. For a connected nonempty poset, there are exactly two universally commuting nuclei (the identity and constant-top maps); for an antichain of cardinality \(n\), every one of the \(2^n\) nuclei commutes with every other.

## Proof

**1. Exhaustive subset normal form.** For any \(S\subseteq P\), the formula for \(j_S\) maps upsets to upsets and is extensive, monotone, and intersection-preserving. If \(s\in S\), then \(s\in j_S(U)\) exactly when \(s\in U\), since \(U\) is an upset. Hence \(j_S(U)\cap S=U\cap S\), proving idempotence.

Conversely, given any nucleus \(j\), define
\[
S_j=\{s\in P:s\notin j(\uparrow s\setminus\{s\})\}.
\]
Suppose \(p\in j(U)\) but some \(s\ge p\) lies in \(S_j\setminus U\). By upward closure of \(j(U)\), one has \(s\in j(U)\). By extensivity, \(s\in j(\uparrow s)\). Meet preservation therefore gives
\[
s\in j(U\cap\uparrow s)\subseteq j(\uparrow s\setminus\{s\}),
\]
a contradiction. Thus \(p\in j_{S_j}(U)\). Conversely, if \(p\notin j(U)\), finiteness permits choosing a maximal \(s\in\uparrow p\setminus j(U)\). Its strict upper points all lie in \(j(U)\), so \(\uparrow s\setminus\{s\}\subseteq j(U)\). If \(s\in j(\uparrow s\setminus\{s\})\), then idempotence yields \(s\in j(j(U))=j(U)\), a contradiction. Hence \(s\in S_j\setminus U\) and \(s\ge p\), showing \(p\notin j_{S_j}(U)\). We have proved \(j=j_{S_j}\). Finally,
\[
p\in j_S(\uparrow p\setminus\{p\})\quad\Longleftrightarrow\quad p\notin S,
\]
so the representation is unique. The normal form agrees with the established finite-poset subset/nucleus correspondence in the cited literature; it is not asserted as new.

**2. Single-input singleton probes.** Write \(D_p=\downarrow p\). The normal form implies
\[
j_S(\varnothing)=P\setminus\downarrow S,\qquad
j_{\{p\}}(U)=\begin{cases}P,&p\in U,\\P\setminus D_p,&p\notin U.\end{cases}
\]
In particular,
\[
j_S(j_{\{p\}}(\varnothing))=P\setminus\downarrow(S\cap D_p),
\]
whereas
\[
j_{\{p\}}(j_S(\varnothing))=
\begin{cases}P,&p\notin\downarrow S,\\P\setminus D_p,&p\in\downarrow S.\end{cases}
\]
If \(p\in S\), the displayed outputs agree. Now suppose \(p\notin S\). If some \(s\in S\) lies above \(p\), the first output includes \(p\) but the second excludes it. If none lies above \(p\) but some \(s\in S\) lies below \(p\), the second output is all of \(P\), while the first excludes \(s\). Therefore equality at the bottom for every singleton probe is equivalent to **no comparable pair crossing from \(S\) to its complement**. This is precisely the condition that \(S\) be a union of comparability components.

**3. Sufficiency for all nuclei.** If the components are \(P_1,\ldots,P_c\), then every upset and every subset split uniquely across them. Each \(j_T\) acts componentwise. When \(S\) is a union of components, \(j_S\) acts on each component either as the identity (if that component lies in \(S\)) or as the constant-top map (if it does not). Both commute with every extensive map on their component, since extensivity forces the component top to be fixed. This proves condition 4 implies condition 1; conditions 1 implies 2 implies 3 are immediate. The subset normal form and uniqueness now show that the universal commutant has \(2^c\) members.

**4. Detecting comparability.** Fix distinct \(p,q\). If they are incomparable, then \(p\in j_{\{q\}}(U)\) for every upset \(U\); consequently \(j_{\{p\}}(j_{\{q\}}(U))=P\), and the reversed composition also equals \(P\). If \(p<q\), then
\[
j_{\{p\}}(j_{\{q\}}(\varnothing))=P\setminus\downarrow p
\ne P=j_{\{q\}}(j_{\{p\}}(\varnothing)).
\]
The case \(q<p\) is symmetric. This completes all claims.

## Verification

The included standard-library Python program `verify_universal_nuclei.py` independently exhausts every labelled poset of size at most four, checks the nucleus axioms and uniqueness of subset representation, compares the entire universal-commutation condition against the bottom-only singleton tests and comparability components, and checks singleton-pair commutativity. It covers respectively \(1,1,3,25,543\) labelled posets at sizes \(0,1,2,3,4\) and prints `VERIFY_OK` when all assertions hold. These finite experiments corroborate the formulas; the proof above establishes the unrestricted theorem for *every* finite poset.

## Relationship to prior work

Lindenhovius establishes the finite-poset correspondence among subsets, Grothendieck topologies, and nuclei; Ochs provides the inverse nucleus-to-subset formula, attributing its mathematical content to Lindenhovius. Ávila, Bezhanishvili, Morandi and Zaldívar study spatiality and Booleanity of the **pointwise-ordered assembly** of nuclei on Alexandrov spaces, including finite spaces. Erné studies nuclear ranges in implicative semilattices. The classification here concerns a different operation: **commutation under function composition** with *every* nucleus, characterized using only one bottom-element test per singleton probe, with an exact connected-component enumeration. Booleanity of the lattice of nuclei does not imply composition commutativity. The inspected primary texts did not state this classification; potential older equivalents under alternative language remain a scholarly risk.

## Limitations

The theorem is finite-poset-specific; it does not classify universally commuting nuclei for arbitrary infinite locales. It concerns all nuclei of the given frame rather than arbitrary meet-preserving endomorphisms. The experimental verification reaches only four points. Novelty comparisons were made against the named accessible primary texts, public indexed mathematical findings, and recoverable local finding titles/claims; they are not an exhaustive world-literature certificate. No independent external mathematical audit has been performed.

## References

1. F. Ávila, G. Bezhanishvili, P. J. Morandi, A. Zaldívar, *The Frame of Nuclei of an Alexandroff Space*, arXiv:1906.03640v1, posted 2019-06-09. https://arxiv.org/abs/1906.03640.
2. A. J. Lindenhovius, *Grothendieck Topologies on Posets*, arXiv:1405.4408v2, 2014, particularly Appendix C. https://arxiv.org/abs/1405.4408.
3. E. Ochs, *On a Formula That Is Not in “Grothendieck Topologies on Posets”*, arXiv:2107.08501v1, posted 2021-07-18; explicitly credits Lindenhovius for the mathematical content. https://arxiv.org/abs/2107.08501.
4. M. Erné, *Nuclear Ranges in Implicative Semilattices*, Algebra Universalis (2022), https://doi.org/10.1007/s00012-022-00768-3.
