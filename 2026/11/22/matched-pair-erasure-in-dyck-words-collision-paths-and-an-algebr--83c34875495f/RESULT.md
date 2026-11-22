# Matched-pair erasure in Dyck words: collision paths and an algebraic spectrum

## Finding

For every indexed Dyck word \(w\) of semilength \(n\), delete the two endpoints of **one originally matched parenthesis pair**, retaining the order of all other symbols. Let \(D(w)\) be the number of distinct resulting Dyck words, with \(D(\epsilon)=0\). Under the usual correspondence with rooted plane trees with \(n\) nonroot vertices, let \(U(w)\) count nonroot vertices with exactly one child; let \(L(w)\) count consecutive *pairs* of leaf children of the same parent, including the root. Then
\[
D(w)=n-U(w)-L(w).
\]
More strongly, two matching-pair deletions have identical output precisely when the deleted vertices belong to the same connected chain obtained from (i) parent-to-only-child links and (ii) adjacent leaf-sibling links. These chains are the complete output-equivalence classes.

Let
\[
F(z,u)=\sum_{n\ge0} z^n\sum_{w\in\mathcal D_n}u^{n-D(w)}.
\]
The unique formal power series with constant term \(1\) is characterized by
\[
\boxed{zF^2-\bigl(1+z+z^2-uz(1+z)\bigr)F+(1+z-uz)=0.}
\]
In particular, for every \(n\ge2\), the maximum value of \(D(w)\) is \(n-1\), attained by exactly \(F_{n+1}\) Dyck words, where \(F_1=F_2=1\) are Fibonacci numbers. The minimum is \(1\), attained only by the fully nested word \(\mathtt{(}^n\mathtt{)}^n\) and the flat word \(\mathtt{()}^n\).

## Assumptions and scope

A Dyck word uses the symbols \(\mathtt{(}\) and \(\mathtt{)}\), with equal totals and nonnegative prefix height. The two erased positions are the unique matching opening and closing parentheses in the *source*, not an arbitrary up-step/down-step pair. Words are linear, with position indices; resulting words are compared literally, not modulo cyclic rotation or reversal. A plane tree has one additional undeletable root. For each parent, a run of \(r\) consecutive leaf children contributes \(r-1\) to \(L\), with a contribution of zero if \(r\le1\). The empty source is included only to normalize the generating function.

## Proof

**Collision classification.** Fix two distinct matching pairs, ordered by the position of their openings. If the pairs are disjoint, write the source as
\[
P\,\mathtt{(}A\mathtt{)}\,Q\,\mathtt{(}B\mathtt{)}\,R,
\]
where \(A,B\) are Dyck words, while \(Q\) need not be a Dyck word. Cancelling the unchanged prefix and suffix, equality of outputs gives the ordinary word equation
\[
A Q\mathtt{(}B\mathtt{)}=\mathtt{(}A\mathtt{)}Q B.
\]
If \(A\) is nonempty, the left side has a Dyck return before or at the end of \(A\), while the right side begins with the irreducible Dyck factor \(\mathtt{(}A\mathtt{)}\), whose first return is two symbols later. Hence \(A\) is empty. If \(B\) is nonempty, comparison of the final \(|B|\) symbols requires \(B=B_{2}\cdots B_{|B|}\mathtt{)}\), forcing every symbol of \(B\) to be a closing parenthesis, which is impossible for nonempty Dyck \(B\). Thus \(B\) is empty. The equation becomes \(Q\mathtt{()}=\mathtt{()}Q\), so the elementary commutation theorem for finite words (or cancellation of each two-character prefix) gives \(Q=\mathtt{()}^r\) for \(r\ge0\). Therefore the erased vertices are leaf siblings with only leaf siblings between them. The converse is immediate: deleting any leaf from such a consecutive run produces the same word.

If the second pair is nested in the first, let \(x\) be the outer vertex and \(y\) its descendant. When \(x\) is erased, its child forest replaces its subtree. When \(y\) is erased, \(x\) remains as a single irreducible parenthesized tree. Literal equality, after cancelling the common outer context, forces the child forest of \(x\) to consist of precisely one tree, so \(x\) has a unique child \(c\). Cancelling the outer parentheses then reduces equality of erasures at \(x\) and \(y\) to equality of erasures at \(c\) and \(y\) within the subtree at \(c\). Induction on their ancestor distance shows that every vertex from \(x\) to the parent of \(y\) has exactly one child. Conversely, removal of any member of such a unary chain produces the same plane tree. These are all the possibilities because matching parentheses are either nested or disjoint.

The elementary collision links form vertex-disjoint paths: unary parent-child links cannot branch, adjacent leaf-sibling links form paths, and no leaf in a sibling run is incident to a unary link. Thus their connected components are precisely the equivalence classes proved above. With \(n\) vertices and \(U+L\) edges, the number of components is \(n-U-L\), proving the pointwise formula.

**Algebraic enumeration.** Weight each nonroot tree vertex by \(z\), each unary parent by an extra \(u\), and every adjacent pair of leaf siblings, including among children of the undeletable root, by an extra \(u\). Let \(T\) enumerate one nonroot rooted plane tree with its descendants, and let \(F\) enumerate forests. The empty forest has weight \(1\); a leaf tree has weight \(z\). The root-of-tree unary penalty modifies just the one-child forest, so
\[
T=z\bigl(F+(u-1)T\bigr).
\]
Split nonempty forests by whether their final child is a leaf. Writing \(F_{\mathrm L}\) and \(F_{\mathrm N}\) for leaf-ending and nonleaf-ending forests respectively gives
\[
F_{\mathrm L}=z\bigl(F+(u-1)F_{\mathrm L}\bigr),\qquad
F_{\mathrm N}=(T-z)F,\qquad F=1+F_{\mathrm L}+F_{\mathrm N}.
\]
Comparison with the tree equation gives \(F_{\mathrm L}=T\), whence \(F=(1+T)/(1-T+z)\). Eliminating \(T\) yields the displayed quadratic for \(F\). The solution is fixed uniquely by \(F(0,u)=1\); at \(u=1\) it becomes the ordinary Catalan generating function.

**Extremes.** If \(n\ge2\), pick any deepest leaf. Its parent is either a nonroot unary vertex, or has at least two consecutive leaf children; the sole exception would be a one-vertex tree. Hence \(U+L\ge1\), so \(D\le n-1\). The coefficient of \(u\) in the quadratic at \(u=0\), using \(F(z,0)=1+z\), gives
\[
[u]F(z,u)=\frac{z^2(2+z)}{1-z-z^2}
=2z^2+3z^3+5z^4+8z^5+\cdots.
\]
Its coefficient of \(z^n\) is \(F_{n+1}\) for all \(n\ge2\), so the upper bound is attained exactly that often. At the other extreme, \(D=1\) means every vertex belongs to a single collision path. Such a path can only be one full unary ancestral chain or one run of root-level leaf siblings, giving the two stated words. Both attain \(1\).

## Verification

The standalone `verify_matching.py` generates every Dyck word up to semilength \(10\) (23,713 nonempty words). It independently computes the literal descendants by stack-matched position erasure, the local statistic \(n-U-L\) from an independently parsed plane-tree forest, and the coefficient polynomials from the quadratic recurrence. It checks equality of all three data sets and the stated Fibonacci/extremal counts. Running `python3 verify_matching.py` gives `VERIFY_OK sizes=1..10 words=23713 quadratic=OK collision=OK extrema=OK`. These finite checks are corroboration; the collision analysis and grammar prove the all-length statements.

## Relationship to prior work

Bernini, Ferrari, Pinzani, and West study the Dyck **scattered-subword** pattern poset and count all rank-one predecessors (arXiv:1303.3785, Proposition 2.1). That operation permits deleting an unmatched up/down pair whenever the result is Dyck. It strictly contains the matched-pair operation: for \(w=\mathtt{()()()}\), the general predecessor set has two members while the matched-pair deletion set has just one. Their formula therefore does not give the present matched-erasure collision classes or distribution. Chen, Li, and Shapiro (arXiv:math/0511045) provide the standard plane-tree/Dyck correspondence and related tree enumerations, not this erasure statistic. Related published work on two-read single-symbol deletion of Dyck words concerns a different channel (one erased position per read and intersections across sources), with no implication for the matched-pair erasure polynomial. The new claim is solely the channel-specific collision classification, algebraic spectrum, and its extremal consequences.

## Limitations

The source is an unlabeled plane-tree/Dyck-word structure, not a general binary word; arbitrary balanced two-symbol deletions, multiple matched-pair deletions, unordered rooted trees and error-correcting code capacity are not analyzed. The independent verification is finite and does not certify originality. Possible equivalent formulations in unindexed tree-contraction literature remain a residual originality risk.

## References

1. W. Y. C. Chen, N. Y. Li, L. W. Shapiro, *The Butterfly Decomposition of Plane Trees*, arXiv:math/0511045, first public 2005-11-02, https://arxiv.org/abs/math/0511045.
2. A. Bernini, L. Ferrari, R. Pinzani, J. West, *The Dyck pattern poset*, arXiv:1303.3785, first public 2013-03-15, https://arxiv.org/abs/1303.3785. See especially the definition and Proposition 2.1 on rank-one scattered-subword predecessors.
