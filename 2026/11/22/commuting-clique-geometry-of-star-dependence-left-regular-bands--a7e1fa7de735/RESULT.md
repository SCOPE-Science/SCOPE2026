# Commuting-clique geometry of star-dependence left regular bands

## Finding

**Theorem.** Fix an integer \(m\ge1\). Let \(B_m\) be the graph product of \(m+1\) one-generator, two-element semilattices, with generators \(h,\ell_1,\ldots,\ell_m\). Require each generator to be idempotent and impose commutation between every two distinct leaf generators \(\ell_i,\ell_j\), but **not** between \(h\) and any leaf. In addition impose the left-regular-band relations \(xyx=xy\) for all words \(x,y\). Equivalently, \(B_m\) is the quotient of the free left regular band by mutual commutation of the leaves: its independence graph is the disjoint union of an isolated hub and a leaf clique; its dependence graph is a star. The empty word is the monoid identity.

Write \(e_S\) for the product of the leaves indexed by \(S\subseteq[m]\), and write \(x_{A,B}=e_A h e_B\), where \(A,B\subseteq[m]\) and \(A\cap B=\varnothing\). Then the \(2^m+3^m\) listed elements are pairwise distinct and exhaust \(B_m\). Their commuting graph includes **all** elements as vertices and edges between distinct commuting elements. Its clique polynomial, with the empty clique included, is
\[
\boxed{F_m(z)=(1+z)^{2^m}+\sum_{k=0}^m\binom{m}{k}(1+z)^{2^k}\big((1+z)^{2^{m-k}}-1\big).}
\]
The inclusion-maximal commuting families are exactly the \(2^m\) distinct commutative submonoids
\[
\boxed{M_A=\{e_S:S\subseteq A\}\ \cup\ \{x_{A,B}:B\subseteq[m]\setminus A\},\quad A\subseteq[m].}
\]
Each has size \(2^{|A|}+2^{m-|A|}\); precisely \(\binom mk\) are indexed by subsets of size \(k\), and coincident cardinalities are to be combined. The smallest maximal-family cardinality is \(2^{\lfloor m/2\rfloor}+2^{\lceil m/2\rceil}\), and the largest is \(2^m+1\).

All multiplicative centralizers are determined by
\[
\boxed{|C(e_S)|=2^m+3^{m-|S|},\qquad |C(x_{A,B})|=2^{|A|}+2^{m-|A|}.}
\]
Consequently the number of ordered commuting pairs, including diagonal pairs, is \(3\cdot4^m+5^m\), and their probability under independent uniform sampling satisfies
\[
\boxed{\operatorname{cp}(B_m)=\frac{3\cdot4^m+5^m}{(2^m+3^m)^2}\sim(5/9)^m\qquad(m\longrightarrow\infty).}
\]

## Assumptions and scope

Throughout \(m\) is a positive integer and the multiplication is the finite left-regular-band multiplication, not the (generally infinite) graph product subject **only** to generator idempotence. In particular, the identities \(u^2=u\) and \(uvu=uv\) hold for arbitrary monoid words. All subsets of \([m]=\{1,\ldots,m\}\) are labeled. Products \(e_S\) are unambiguously defined because leaf generators commute. Two elements with a hub are represented using disjoint subsets because letters seen before their first hub occurrence never need to be repeated. The definition retains identity \(e_\varnothing\), which is a vertex of the commuting graph and belongs to every maximal family.

A clique means a *set* of pairwise commuting distinct elements, with the empty set counted; a maximal clique is inclusion-maximal. A maximal commutative submonoid is maximal under inclusion among submonoids all of whose elements commute. These two notions coincide in this theorem because all maximal cliques are proved closed under multiplication. Centralizers include the element itself.

## Proof

**1. Unique normal forms.** In the ordinary free left regular band, first occurrences of letters determine a unique normal form. Here every leaf commutes with every other leaf. If a word contains no hub, all letters can be rearranged and repetitions removed, leaving a unique \(e_S\). If the word contains a hub, keep its first occurrence. Every first-occurring leaf before that hub can be put in a sorted prefix \(e_A\), and every leaf not already in \(A\) whose first occurrence follows the hub can be put in a sorted suffix \(e_B\). Removing all later repetitions gives \(x_{A,B}\) with disjoint sets. Uniqueness follows either from the standard acyclic-orientation model of partially commutative left regular bands or directly by projecting to each two-letter noncommuting subband \(\{h,\ell_i\}\): this projection records whether \(\ell_i\) is absent, before \(h\), or after \(h\). These are three distinct possibilities per leaf. Elements without a hub are distinguished by leaf support. Thus there are exactly \(2^m+3^m\) normal forms.

**2. The complete commutation criterion.** Multiplication of normal forms consists of concatenation, deletion of all occurrences after each letter's first appearance, and reordering leaves within either side of the first hub. Therefore
\[
 e_S e_T=e_{S\cup T},\qquad
 x_{A,B}x_{C,D}=x_{A,(B\cup C\cup D)\setminus A}.
\]
Similarly \(e_Sx_{A,B}\) has before-hub leaf set \(S\cup A\), while \(x_{A,B}e_S\) has before-hub set \(A\). The products agree precisely when \(S\subseteq A\). Finally, the two products \(x_{A,B}x_{C,D}\) and \(x_{C,D}x_{A,B}\) agree precisely when \(A=C\); if these sets agree, both products have the same after-hub set \(B\cup D\). Hence
\[
 e_S\leftrightarrow e_T\ \text{always},\quad
 e_S\leftrightarrow x_{A,B}\Longleftrightarrow S\subseteq A,\quad
 x_{A,B}\leftrightarrow x_{C,D}\Longleftrightarrow A=C,
\]
where \(\leftrightarrow\) means multiplicative commutation.

**3. Maximal commuting submonoids.** Every pairwise commuting family containing a hub element \(x_{A,B}\) can contain only other hub elements with precisely the same before-hub set \(A\), and can contain only hubless elements \(e_S\) with \(S\subseteq A\). It therefore lies in the displayed \(M_A\). Each \(M_A\) is pairwise commuting by Step 2 and is closed under multiplication: leaf-only products are unions of subsets of \(A\); hub-hub products union suffix subsets of the complement of \(A\); and mixed products equal the hub element because \(S\subseteq A\). Thus \(M_A\) is a commutative submonoid. It cannot be enlarged by any element not in it. Every hubless commuting family lies in at least one \(M_A\), namely \(M_{[m]}\). All maximal cliques and maximal commutative submonoids are therefore precisely these \(M_A\). Distinct \(A\) produce distinct hub-element families, so the number is \(2^m\). The size and extremal statements follow from convexity and symmetry of \(2^k+2^{m-k}\) in the integer variable \(0\le k\le m\).

**4. All-arity clique enumerator.** Partition cliques according to whether they contain any hub element. A hubless clique is any subset of the \(2^m\) elements \(e_S\), contributing \((1+z)^{2^m}\). If a clique contains a hub element, it has a uniquely determined common before-hub leaf set \(A\); it may choose any nonempty subset of the \(2^{m-|A|}\) hub elements \(x_{A,B}\), and independently any subset of the \(2^{|A|}\) allowed leaf-only elements. The contribution for this \(A\) is \((1+z)^{2^{|A|}}((1+z)^{2^{m-|A|}}-1)\). Summing over the \(\binom mk\) choices with \(|A|=k\) proves the polynomial.

**5. Centralizers and commuting probability.** By Step 2, the centralizer of \(e_S\) contains all \(2^m\) hubless forms and exactly those hub forms whose before-hub subset contains \(S\), of which there are \(3^{m-|S|}\) (the leaves outside \(S\) are independently before, after or absent). The centralizer of \(x_{A,B}\) contains the \(2^{|A|}\) leaf-only elements with support in \(A\) and the \(2^{m-|A|}\) hub elements with before-hub set \(A\). This proves both formulas. Summing centralizer sizes over all elements gives
\[
\sum_{S\subseteq[m]}\big(2^m+3^{m-|S|}\big)+\sum_{A\subseteq[m]}2^{m-|A|}\big(2^{|A|}+2^{m-|A|}\big)
=2\cdot4^m+4^m+5^m.
\]
Division by \((2^m+3^m)^2\) gives the exact commuting probability. Since \(5^m\) dominates \(4^m\) and \(3^m\) dominates \(2^m\), the stated asymptotic follows.

## Verification

The companion `check_star_band.py` uses the full normal-form enumeration and **separately implemented concatenation-and-reduction multiplication** rather than the displayed commutation formulas. It checks all ordered products and centralizer sizes for each \(m\) from one through six; the largest case has \(793\) elements and \(628{,}849\) ordered-pair tests. It verifies closure and maximality of every proposed \(M_A\), and compares the full clique polynomial by literal clique enumeration for \(m\le3\) and maximal clique enumeration for \(m\le4\). Its recorded output is included in `check_star_band_output.txt`; execution finishes with `ALL CHECKS PASSED`. This finite test is supporting evidence only; Steps 1–5 prove the unrestricted family.

## Relationship to prior work

Margolis, Saliola and Steinberg describe graph-indexed partially commutative left regular bands and identify them with acyclic orientations of induced subgraphs of the graph complement. Their 2012 paper (Section 3.6, Theorem 3.7) supplies the general construction, and their 2015 monograph (Section 2.3) supplies the MSC-aligned left-regular-band treatment. Their work is on topology, homology and representation theory, and its normal-form construction is not claimed here as novel.

More general centralizer theory for **graph products of semigroups** exists (Yang and Li, 2022/2023). Such work can provide a route to individual centralizer descriptions and is not claimed to be superseded. This result concerns the **finite left-regular-band quotient with arbitrary-word absorption**: a graph product in which only generators are idempotent is generally infinite and has different normal forms. The claimed new content is the all-arity commuting-clique polynomial, complete maximal commuting-submonoid classification, and exact global commuting probability in the star-dependence family, rather than the general word-reduction or centralizer framework.

Other studies of commuting graphs of free *left legal semigroups* involve identity \(xyx=xy\) without imposing idempotence on all elements and hence have doubled-generator normal forms; their maximal-family enumerations do not apply to this left regular band.

## Limitations

The theorem addresses the specific, natural star-dependence graph family and makes no assertion about arbitrary graph-indexed left regular bands. The formula for a centralizer is a specialization in a field with stronger generic centralizer results and is not claimed separately as a priority discovery. The general normal form is prior knowledge. The entire clique polynomial and maximal-family spectrum are established by direct argument, but an obscure equivalent enumeration or an easy corollary implicit in broader published work might exist. A broader published theorem may imply part of the counting result; priority requires further comparison.

## References

1. S. Margolis, F. Saliola and B. Steinberg, *Combinatorial Topology and the Global Dimension of Algebras Arising in Combinatorics*, arXiv:1205.1159v1, first posted 5 May 2012; Section 3.6 and Theorem 3.7. https://arxiv.org/abs/1205.1159
2. S. Margolis, F. Saliola and B. Steinberg, *Cell complexes, poset topology and the representation theory of algebras arising in algebraic combinatorics and discrete geometry*, arXiv:1508.05446v1, first posted 22 August 2015; Section 2.3, primary MSC 20M30. https://arxiv.org/abs/1508.05446
3. D. Yang and H. Li, *Centralizers in graph products of semigroups*, *Semigroup Forum* 106 (2023), 285–326; first published online 13 December 2022. DOI: 10.1007/s00233-022-10331-0.
4. A. Nagy, *On left legal semigroups*, arXiv:2301.08793 (2023), for comparison with a distinct non-band variety. https://arxiv.org/abs/2301.08793
