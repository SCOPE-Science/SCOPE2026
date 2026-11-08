# Six-periodic rigidity of neighborhood \(3\)-balanced colorings on prisms and Möbius ladders

## Finding
Let \(n\ge3\). The prism \(P_n=C_n\square K_2\) has vertices \((r,i)\) for \(r\in\{0,1\}\), \(i\in\mathbb Z/n\mathbb Z\), with edges along each cyclic row and across each rung. The Möbius ladder \(M_{2n}\) has two paths of length \(n-1\), matching rungs, and two closing edges \((0,n-1)(1,0)\) and \((1,n-1)(0,0)\). All these graphs are cubic, including \(n=3\).

A *neighborhood \(3\)-balanced coloring* assigns one of three **labelled** colors \(\mathbb F_3=\{0,1,2\}\) to each vertex, so that the three neighbors of every vertex receive three different colors. Write \(B_P(n)\) and \(B_M(n)\) for the number of these colorings on the specifically labelled graphs above. Then
\[
(B_P(n),B_M(n))=\begin{cases}
(0,0),&3\nmid n,\\
(6,36),&n\equiv3\pmod6,\\
(36,6),&n\equiv0\pmod6.
\end{cases}
\]
The colorings are completely classified: every valid coloring lifts to the infinite two-row ladder as a \(6\)-periodic coloring \(x_i=(a_i,b_i)\) satisfying \(x_{i+3}=(b_i,a_i)\). The \(36\) possible infinite-strip colorings correspond bijectively to quadruples \((a_0,a_1,a_2,a_3)\in\mathbb F_3^4\) with \(a_0\ne a_2\) and \(a_1\ne a_3\), extended by \(a_{i+2}=-a_i-a_{i-2}\) and \(b_i=a_{i+3}\). Exactly six strip colorings have period dividing three.

Each coloring determines an unordered partition into three disjoint total dominating sets, and each such partition corresponds to exactly \(6\) labelled colorings. Thus the corresponding partition counts are obtained by dividing each displayed entry by \(6\). In both families the total domatic number is \(3\) exactly when \(3\mid n\), and \(2\) otherwise. The existence part of this last statement is prior work; the new result is the complete coloring census and periodic classification.

## Assumptions and scope
All graphs are finite, simple, undirected, and vertex-labelled by their indicated two-row coordinates. The index \(n\) is an integer at least three; no quotient by graph automorphisms is taken. Color names are fixed, and the count of unordered total-domatic partitions divides by permutations of these names, *not* by automorphisms of the underlying graph.

On the infinite strip, each vertex \((r,i)\) has rung neighbor \((1-r,i)\) and horizontal neighbors \((r,i-1)\), \((r,i+1)\). A prism coloring is a strip coloring satisfying \(x_{i+n}=x_i\); a Möbius coloring instead satisfies \(x_{i+n}=Sx_i\), where \(S(a,b)=(b,a)\). These periodic or twisted lifts are bijective to colorings of the respective finite graphs.

## Proof
**Step 1: algebraic necessity.** In the field \(\mathbb F_3\), three values are pairwise distinct precisely when their sum is zero and they are not all equal. For a balanced strip coloring, the neighborhood equations give
\[
b_i=-a_{i-1}-a_{i+1},\qquad a_i=-b_{i-1}-b_{i+1}.
\]
Substituting the first into the second yields, for all integers \(i\),
\[
a_{i-2}+a_i+a_{i+2}=0.
\]
Since \(-1=2\) in \(\mathbb F_3\), successive differences along each parity class satisfy
\[
a_{i+2}-a_i=a_i-a_{i-2}.
\]
Thus the even-index and odd-index subsequences each form arithmetic progressions in \(\mathbb F_3\). Their steps are nonzero because \(a_{i-1}\ne a_{i+1}\) is required at every top vertex. Every such progression has period three, so \(a_{i+6}=a_i\).

Applying the constant-difference identity twice and using the first neighborhood equation,
\[
a_{i+3}=a_{i-1}+2(a_{i+1}-a_{i-1})=-a_{i-1}-a_{i+1}=b_i.
\]
Consequently \(b_{i+3}=a_{i+6}=a_i\), giving \(x_{i+3}=Sx_i\) and \(x_{i+6}=x_i\).

**Step 2: sufficiency and strip count.** Choose \(a_0,a_1,a_2,a_3\in\mathbb F_3\) with \(a_0\ne a_2\) and \(a_1\ne a_3\). Extend in both directions by the above second-order recurrence and put \(b_i=a_{i+3}\). There are \(3\cdot2\cdot3\cdot2=36\) such choices. The two parity-class differences remain nonzero everywhere, so \(a_{i-1}\ne a_{i+1}\). The recurrence and the shifted recurrence imply the top and bottom neighborhood sums vanish in \(\mathbb F_3\); their two horizontal colors differ. A triple of field elements with zero sum and two different elements must be \(\{0,1,2\}\). Hence every chosen quadruple gives a balanced coloring; distinct quadruples produce distinct strip colorings.

A strip coloring has period three precisely when \(x_{i+3}=x_i\), or equivalently when \(a_i=b_i\) for all \(i\). Its first three colors then form a permutation of \(0,1,2\) and repeat every three columns. Hence exactly \(3!=6\) strip colorings have period three. All other \(30\) have least period six, since a period one or two would violate \(a_i\ne a_{i+2}\).

**Step 3: close the strip.** In the prism, \(x_{i+n}=x_i\) is possible for all \(36\) patterns when \(n\equiv0\pmod6\), and only the six period-three patterns when \(n\equiv3\pmod6\). For other residues no pattern has period dividing \(n\). In the Möbius case, the closing relation is \(x_{i+n}=Sx_i=x_{i+3}\). It holds for all patterns when \(n\equiv3\pmod6\), only the six period-three patterns when \(n\equiv0\pmod6\), and none otherwise. This proves both displayed counting formulas.

**Step 4: total-domatic interpretation.** A three-class partition is a total-domatic partition exactly when every vertex has a neighbor in every class, which in a cubic graph is the neighborhood-balanced condition. Each class is nonempty because it occurs in every neighborhood, so no nontrivial color permutation fixes a coloring. Exactly six colorings therefore represent each unordered partition. A two-class total-domatic partition always exists: assign one color to each row on the finite two-row representation, giving both colors in every neighborhood, even across the Möbius seam. Since each graph has degree three, no total-domatic partition has more than three classes. This gives the stated domatic numbers, whose existence classification was already known.

## Verification
Run `python3 artifacts/verify.py` with Python 3 and only the standard library. This program independently constructs each graph and directly checks **all** ternary vertex assignments at \(3\le n\le6\), yielding prism/Möbius counts \((6,36),(0,0),(0,0),(36,6)\) for \(n=3,4,5,6\), respectively. Separately, a \(9^2=81\)-state local-neighborhood transfer computes ordinary and row-swap-twisted traces through \(n=72\), confirming the formulas. It also constructs all \(36\) described infinite-strip patterns and checks their closing conditions and every vertex neighborhood through \(n=120\).

These are finite corroborations; the unrestricted proof above is the algebraic recurrence and closure argument. No formal external certification or independent mathematical audit is claimed.

## Relationship to prior work
The 2026 preprint of Choi–Kwon–Park studies total domatic partitions through the det-extremal correspondence for cubic graphs, motivating the question of how rigid maximal total-domatic partitions can be on natural cubic families. The earlier Minyard–Sepanski study already proved the **existence** criterion for three-balanced colorings of generalized Petersen graphs, including prisms, and for Möbius ladders (its Sections 4 and 6, Theorems 4.2 and 6.1). Li–Shao–Zhu (2020) established the corresponding injective-chromatic-number criterion for generalized Petersen graphs. Neither the existence criteria nor the equivalence with three-class total-domatic partitions is claimed as new. The present claim is a full classification of every coloring and exact labelled/unordered counts for both closure types, including the six-column row-swap law.

## Limitations
The classification concerns cubic two-row cyclic strips with the untwisted or Möbius seam, not general cubic graphs or wider cylinders. It counts partitions with fixed vertex labels and does not quotient by all graph automorphisms. The 2020 Houston Journal full article was not readable through the available public access, so an implicit equivalent enumeration in its proofs cannot be ruled out; its published abstract and the 2026 full-text citations support an existence statement, not a verified enumeration. The relevant later 2026 det-extremal preprint was also available in abstract form only. Historical priority is provisional. Independent verification is not performed.

## References
1. M. Choi, H. Kwon and B. Park, *Det-extremal cubic graphs and the total domatic number*, arXiv:2609.33902, publicly submitted September 27, 2026. https://arxiv.org/abs/2609.33902
2. M. Minyard and M. R. Sepanski, *Neighborhood Balanced 3-Coloring*, arXiv:2410.05422, first submitted October 7, 2024; published as *Neighborhood 3-Balanced Graphs*, Graphs and Combinatorics **42** (2026), article 50. https://link.springer.com/article/10.1007/s00373-026-03038-4
3. Z. Li, Z. Shao and E. Zhu, *Injective coloring of generalized Petersen graphs*, Houston J. Math. **46** (2020), 1–12. https://www.math.uh.edu/~hjm/Vol46-1.html
4. H. Kwon, B. Park and Y. Sano, *Every cubic graph has four total dominating sets covering each vertex at most twice*, arXiv:2610.19450, submitted October 14, 2026. https://arxiv.org/abs/2610.19450
