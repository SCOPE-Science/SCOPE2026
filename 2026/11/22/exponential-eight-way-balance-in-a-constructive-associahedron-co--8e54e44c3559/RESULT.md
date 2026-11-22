# Exponential eight-way balance in a constructive associahedron colouring

## Finding

Let \(n\ge 2\), and let \(\mathcal T_n\) be the set of all plane full binary trees with exactly \(n\) leaves. The standard tree-rotation bijection identifies \(\mathcal T_n\) with the vertices of the associahedron graph \(\mathcal A_{n+1}\). Endow \(\mathcal T_n\) with the explicit eight-colouring \(\kappa(T)=(\lambda(T),d(T))\in\mathbb F_2^2\times\mathbb F_2\) introduced by Wood [1], with all leaf labels \((0,0)\).

For \(s\in\mathbb F_2^2\), \(b\in\mathbb F_2\), put \(N_n(s,b)=|\{T\in\mathcal T_n:\kappa(T)=(s,b)\}|\), and let \(C_{n-1}=\frac1n\binom{2n-2}{n-1}\). Let \(a_j(n)\) be the coefficient of \(z^n\) in the formal power series

\[
A_j(z)=\frac{1-\sqrt{1-4z+4jz^5}}2,\qquad j\in\{2,4\},
\]

where the square root has constant term \(1\). Then **every one of the eight actual colour classes** satisfies the all-order quantitative inequality

\[
\left|N_n(s,b)-\frac{C_{n-1}}8\right|
\le\frac38a_4(n)+\frac12a_2(n)
\le\frac78a_2(n).
\]

For the explicit rational number \(r=251/1000\), both \(A_2(r)\) and \(A_4(r)\) are finite, and hence

\[
\left|N_n(s,b)-\frac{C_{n-1}}8\right|
\le \frac78 A_2(r)r^{-n},
\qquad
\frac{N_n(s,b)}{C_{n-1}}=\frac18+O\!\left(n^{3/2}\left(\frac{250}{251}\right)^n\right).
\]

The implied constant is absolute and uniform over the eight colours. In particular, each colour occurs for all sufficiently large \(n\), and all eight classes have asymptotic density exactly \(1/8\). This concerns the distribution of Wood's particular construction, **not** an improvement to the known bound on the chromatic number.

## Assumptions and scope

A plane full binary tree is either a leaf, denoted `*`, or an ordered pair of trees, denoted `(UV)`. A subtree is a *fringe subtree* if it consists of one vertex and all its descendants. All binary trees and colour labels are distinguished by left/right order; no quotient by symmetries is taken. All arithmetic in the definitions of labels and parity is modulo two.

For child labels \(a=(a_0,a_1)\) and \(b=(b_0,b_1)\), Wood's quasigroup is
\[
Q(a,b)=(a_0+a_1+b_0,\ a_1+b_0+b_1+1).
\]
The root label is \(\lambda(*)=(0,0)\) and \(\lambda((U,V))=Q(\lambda(U),\lambda(V))\). At an internal node, the preferred child is left when \(a_1+b_0=0\), and right otherwise. Preferred edges decompose the tree into descending paths. The bit \(d(T)\) is the parity of the preferred left edges whose parent has even distance from the top of its preferred path; the root of each path has depth zero.

## Proof

**1. Label-substitution bijection.** For each fixed \(c\), both maps \(a\mapsto Q(a,c)\) and \(a\mapsto Q(c,a)\) are bijections of \(\mathbb F_2^2\), since their linear parts are invertible. Consequently, holding all of a tree outside one rooted subtree fixed, its full root label is a bijective function of the replacement subtree's root label.

Choose the following four distinct five-leaf trees (the strings use the grammar above):

| Required root label | Five-leaf tree |
|---|---|
| \((0,0)\) | `(*(*(*(**))))` |
| \((0,1)\) | `((**)((**)*))` |
| \((1,0)\) | `(*(*((**)*)))` |
| \((1,1)\) | `(*((**)(**)))` |

Direct substitution into \(Q\) gives the displayed root labels. For every large tree containing one of these four fringe shapes, select its **first** occurrence in preorder and replace that fringe subtree by any of the four shapes. This forms a four-element orbit, and the four resulting full root labels are distinct. The selection is unchanged by replacement: all four shapes have five leaves, so neither an ancestor nor a proper descendant can be another occurrence of the selected size; earlier disjoint fringe subtrees are untouched. Let \(B_4(n)\) count trees avoiding these four shapes. Thus the number \(N_n(s)=\sum_bN_n(s,b)\) obeys
\[
\left|N_n(s)-C_{n-1}/4\right|\le3B_4(n)/4.
\]

**2. Sign-reversing parity substitution.** For an arbitrary tree \(T\), define \(d_p(T)\) for \(p\in\{0,1\}\) by computing the same preferred-left-edge parity with the root assigned preferred-path depth of parity \(p\); a nonpreferred child always starts a new path at depth zero. In particular, \(d(T)=d_0(T)\), and \(d_0(*)=d_1(*)=0\).

Writing \(U,V\) for left and right subtrees, the two parity recurrences are, when the root prefers left,
\[
(d_0(T),d_1(T))=(1+d_1(U)+d_0(V),\ d_0(U)+d_0(V)),
\]
and when it prefers right,
\[
(d_0(T),d_1(T))=(d_0(U)+d_1(V),\ d_0(U)+d_0(V)).
\]
All sums here are in \(\mathbb F_2\). Two different five-leaf shapes are

`((((**)*)*)*)` and `((*(**))(**))`.

Recursion yields \(\lambda=(0,0)\) for both, while their pairs \((d_0,d_1)\) are respectively \((0,0)\) and \((1,1)\). Replacing either by the other at a fixed rooted location therefore leaves every ancestor label, all external preferred-child choices and all external preferred-path depths unchanged, while toggling the parity *regardless of the incoming depth*. Selecting the first preorder occurrence of either shape defines a sign-reversing involution on all trees containing one of them. It preserves the full root label and interchanges \(d=0\) and \(d=1\). Thus if \(B_2(n)\) counts trees avoiding this pair, then
\[
|N_n(s,0)-N_n(s,1)|\le B_2(n).
\]
Combining this with step 1 gives
\[
\left|N_n(s,b)-C_{n-1}/8\right|\le3B_4(n)/8+B_2(n)/2.
\]

**3. Fringe avoidance and exponential decay.** For any fixed collection of \(j\) distinct five-leaf patterns, a tree avoiding all of them is either a leaf or the ordered pair of two avoiding trees, except that precisely \(j\) forbidden five-leaf root trees must be excluded. Every proper fringe subtree of a five-leaf pattern has fewer than five leaves, so these excluded trees do arise from avoiding children. Therefore its ordinary leaf-count generating series \(A_j\) satisfies
\[
A_j(z)=z+A_j(z)^2-jz^5,
\]
which gives exactly the displayed square-root expression. The count depends only on \(j\), not on which patterns are chosen. Hence \(B_j(n)=a_j(n)\), and \(a_4(n)\le a_2(n)\): a four-pattern avoidance class is contained in the avoidance class for any two of its patterns, whose size is \(a_2(n)\).

For \(r=251/1000>1/4\), both discriminants \(1-4r+4jr^5\), for \(j=2,4\), are strictly positive; their derivatives remain strictly negative on \([0,r]\), so there is no positive-real branch singularity up to \(r\). The coefficients count combinatorial objects and are nonnegative; Pringsheim's theorem, or monotone convergence for the nonnegative series up to the first positive singularity, shows convergence at \(r\). Therefore \(a_2(n)\le A_2(r)r^{-n}\). Finally \(C_{n-1}\sim4^{n-1}/(\sqrt\pi n^{3/2})\), proving the uniform exponential relative-error estimate. \(\square\)

## Verification

The accompanying `verify.py` implements the labels and preferred-path parity in two independent ways. It checks the five-leaf witnesses, all one-leaf replacement contexts of up to seven leaves, all full trees of up to ten leaves, their avoidance counts and balance inequalities, and the proper-colouring condition for every rotation on trees with up to eight leaves. Run `python3 verify.py` using Python 3 and no external dependencies. These checks corroborate, but do not substitute for, the unrestricted proof above.

## Relationship to prior work

Wood [1] constructed and proved proper the specific eight-colouring analysed here. Its properness and the eight-colour upper bound are therefore *prior work*, not new conclusions. Wood's text discusses a methodological lower bound for quasigroup label-parity colourings, but does not give a quantitative colour-class distribution. Tan [2] independently developed an earlier twelve-colouring with three-state root labels and two parity bits; its distinct map does not determine this distribution. Lehtonen and Waldhauser [3] study equivalences among bracketings under linear quasigroup operations, not the preferred-path parity statistic or eight colour-class counts. The present argument applies explicit fringe substitutions and a pattern-avoidance series to Wood's map, a question not answered by those results. The balance is for this particular construction, not for arbitrary optimal proper colourings.

## Limitations

This is a quantitative asymptotic with a conservative, nonsharp explicit exponential rate. It does not determine exact colour-class sizes in closed form for arbitrary \(n\), claim optimality of the eight-colouring, or prove an independent originality certificate. Small associahedra may fail to use all eight colours, as the explicit tests show. Possible older formulations of the same asymptotic under coloured-tree statistics remain a historical-priority risk.

## References

[1] D. R. Wood, *Associahedra are 8-colourable*, arXiv:2611.19659v1 (first public version 2026-11-14), https://arxiv.org/html/2611.19659v1.

[2] J. Tan, *Associahedra are 12-colourable*, arXiv:2611.05323v1 (2026-11-03), https://arxiv.org/html/2611.05323v1.

[3] E. Lehtonen and T. Waldhauser, *Associativity conditions for linear quasigroups and equivalence relations on binary trees*, arXiv:2310.09184 (first public version 2023-10-13), https://arxiv.org/abs/2310.09184.
