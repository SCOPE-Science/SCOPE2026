# Cycle-index orbit census of doubly confluent modal frames on rooted stars

## Finding

For every integer \(m\ge2\), take the finite **rooted star** \(P_m=\{r\}\cup L\), with \(|L|=m\), where \(r<\ell\) for all \(\ell\in L\), and distinct leaves are incomparable. An accessibility relation \(R\subseteq P_m\times P_m\) is **forward confluent** if
\[
x\le y\ \land\ xRu\ \Longrightarrow\ \exists v\,(yRv\land u\le v),\]
and **downward confluent** if
\[
x\le y\ \land\ yRu\ \Longrightarrow\ \exists v\,(xRv\land v\le u).\]
No seriality, reflexivity, transitivity, or symmetry is imposed on \(R\).

For an integer partition \(\lambda=(\ell_1,\ldots,\ell_k)\vdash m\), put
\[
g_i=\sum_{j=1}^k\gcd(\ell_i,\ell_j),\qquad z_\lambda=\prod_{a\ge1}a^{m_a(\lambda)}m_a(\lambda)!,\]
where \(m_a(\lambda)\) is the multiplicity of the part \(a\). Define
\[
F(\lambda)=2^k+\prod_{i=1}^k(2^{1+g_i}-1)
+2^k\left(\prod_{i=1}^k(1+2^{g_i})-2^{\sum_i g_i}\right).
\]
**The exact number of isomorphism classes** of forward-and-downward-confluent accessibility relations on this rooted star is
\[
\boxed{U_m=\sum_{\lambda\vdash m}\frac{F(\lambda)}{z_\lambda}}.
\]
Isomorphisms preserve both the order and the accessibility relation, not the names of the leaves. The counts for \(m=2,3,4,5,6\) are
\[
\boxed{50,\ 940,\ 53170,\ 9968880,\ 6472894706}.
\]
For comparison, the counts of **labelled** relations for those sizes are \(89,5119,1211297,1171027327,4624635403649\); these labelled counts and the underlying confluence case structure are not claimed as new. The result is the exact **unlabelled** orbit enumeration and its cycle-type formula.

## Assumptions and scope

The root \(r\) is the unique minimal point. Consequently the order-automorphism group is exactly \(S_m\), acting on the leaves, and its action on relations is \(R\mapsto\sigma R\sigma^{-1}\). No valuation is chosen in the enumeration.

In the four-connective semantics of Balbiani and Gencer, for any persistent atomic valuation assigning an upset \(U\subseteq P_m\), at any world \(x\), the Přenosil and Wijesekera possibility operations on \(U\) are respectively
\[
P(U)(x)\iff\exists y\le x\ \exists u\,(yRu\land u\in U),
\]
\[
W(U)(x)\iff\forall y\ge x\ \exists u\,(yRu\land u\in U).
\]
Their paired necessity operations are
\[
B(U)(x)\iff\forall y\ge x\ \forall u\,(yRu\Rightarrow u\in U),
\]
\[
D(U)(x)\iff\exists y\le x\ \forall u\,(yRu\Rightarrow u\in U).
\]
On rooted stars, \(P(U)=W(U)\) for all upsets \(U\) if and only if forward confluence holds, while \(B(U)=D(U)\) for all upsets if and only if downward confluence holds. Indeed, one can test these equivalences on all the upsets of the rooted star. When both hold, substitution and induction also identify the corresponding operations inside arbitrary nested formulas. Operator coincidence is contextual motivation; the enumerated object is the confluence frame class itself.

## Proof

Write \(S=R[r]=\{u:rRu\}\) for the root row. For each leaf \(\ell\), write \(R[\ell]\) for its row. As \(r\le\ell\) are the only nonidentity order comparisons, forward confluence is equivalent to
\[
\downarrow S\subseteq\downarrow R[\ell]\quad\text{for every leaf }\ell,
\]
and downward confluence is equivalent to
\[
\uparrow R[\ell]\subseteq\uparrow S\quad\text{for every leaf }\ell.
\]
(Here \(\downarrow\) and \(\uparrow\) refer to the order on the **target** set.) These are equivalent to the original universal-existential conditions by choosing a witness for each row element.

Split into four disjoint cases.

**Case E.** If \(S=\varnothing\), downward confluence forces every leaf row to be empty, so exactly one relation occurs.

**Case R.** If \(S=\{r\}\), forward confluence forces each leaf row to be nonempty. Conversely any nonempty row works, because the root is below every possible target, so downward confluence is automatic.

**Case A.** If \(S=A\) with \(\varnothing\ne A\subseteq L\), forward confluence requires \(A\subseteq R[\ell]\); downward confluence forbids \(r\) or leaves outside \(A\) in \(R[\ell]\). Hence every leaf row is exactly \(A\).

**Case RA.** If \(S=\{r\}\cup A\) with \(\varnothing\ne A\subseteq L\), each leaf row must include \(A\), while the root target and the remaining leaves may be selected freely. These four cases exhaust the possibilities for \(S\), and every displayed relation is doubly confluent.

Now fix a permutation \(\sigma\in S_m\), with cycle lengths \(\lambda=(\ell_1,\ldots,\ell_k)\). A fixed relation must have a \(\sigma\)-invariant root row, and its leaf rows must satisfy \(R[\sigma\ell]=\sigma R[\ell]\). The nonempty invariant subsets \(A\subseteq L\) are unions of the \(k\) cycles.

Cases E and A together contribute \(1+(2^k-1)=2^k\) fixed relations.

For Case R, consider source cycle \(i\), of length \(\ell_i\). Its first leaf row must be a nonempty subset invariant under \(\sigma^{\ell_i}\). This power fixes the root and has exactly \(\gcd(\ell_i,\ell_j)\) orbits on target cycle \(j\), hence \(1+g_i\) orbits on all targets. Exactly \(2^{1+g_i}-1\) nonempty choices are possible, and all other rows on the same source cycle are forced by equivariance. Multiplication over source cycles gives \(\prod_i(2^{1+g_i}-1)\).

For Case RA, choose the nonempty set \(J\subseteq\{1,\ldots,k\}\) of target cycles comprising \(A\). A row for source cycle \(i\) must contain \(A\), with free choices on the \(\sigma^{\ell_i}\)-orbits outside \(A\); their number is
\[
1+\sum_{j\notin J}\gcd(\ell_i,\ell_j).
\]
The initial \(1\) accounts for the root target. Multiplying the row-choice counts over all source cycles yields
\[
2^{k+\sum_{j\notin J}g_j}.
\]
Summing over all nonempty \(J\) gives
\[
2^k\left(\prod_{j=1}^k(1+2^{g_j})-2^{\sum_jg_j}\right).
\]
Adding the disjoint contributions proves that the number of \(\sigma\)-fixed relations equals \(F(\lambda)\).

Finally, exactly \(m!/z_\lambda\) elements of \(S_m\) have cycle type \(\lambda\). Burnside's lemma gives
\[
U_m=\frac1{m!}\sum_{\sigma\in S_m}|\operatorname{Fix}(\sigma)|
=\sum_{\lambda\vdash m}\frac{F(\lambda)}{z_\lambda},
\]
for every \(m\ge2\), as claimed. The proof makes no inference from finite computation to arbitrary \(m\).

For the modal link, the inclusions above imply equality of each operator pair on upsets. For necessity, the only nontrivial comparison is at leaf or root, where \(\uparrow R[\ell]\subseteq\uparrow R[r]\) makes \(R[r]\subseteq U\) imply \(R[\ell]\subseteq U\); for possibility, \(\downarrow R[r]\subseteq\downarrow R[\ell]\) makes an intersection of \(R[r]\) with \(U\) imply an intersection of \(R[\ell]\) with \(U\). Conversely, choose \(U=\uparrow\{u\}\) for a failed forward-confluence witness, and \(U=\uparrow R[r]\) for a failed downward-confluence witness, to separate the corresponding operators. Thus both implications hold under all persistent valuations.

## Verification

Run the accompanying `checker.py` with Python 3; it has no external dependencies. It independently enumerates every binary relation on rooted stars with one, two and three leaves; it tests both quantified confluence conditions without invoking the normal-form proof. It separately compares the four published modal operators on every upset and asserts exact agreement with the confluence test for each relation.

It computes isomorphism orbits by an independent canonicalization under every permutation of leaves. It also directly counts relations fixed by every leaf permutation and compares with the cycle formula. Expected exact outputs include the direct pairs (labelled,unlabelled) \((7,7)\), \((89,50)\), \((5119,940)\), and `ROOTED_STAR_CONFLUENCE_ORBIT_OK`.

A separate exact-rational partition sum evaluates the displayed formula for \(1\le m\le8\), requiring the output integers and agreeing with independent enumeration wherever feasible. These are finite checks only; the all-size proof is the preceding case split and Burnside argument.

## Relationship to prior work

Balbiani and Gencer define the four modal operators, their confluence classes, and the modal collapse on the relevant classes. Their 2026 paper does not provide the leaf-permutation orbit count for a rooted star. The underlying frame conditions and modal coincidence are existing mathematics, not claimed as new here.

A prior general **labelled** census for relations between two complete height-two posets includes the rooted star as a special case; its labelled count does not determine cycle-type fixed-point statistics or isomorphism-class counts. The result here counts the conjugacy orbits rather than relabelled presentations and produces the new \(\gcd\)-weighted Burnside expression. The difference is substantive even for two leaves: \(89\) labelled relations give \(50\), rather than \(89/2\), isomorphism classes because some frames have nontrivial automorphisms.

Published chain-only counts for forward confluence and for simultaneous forward-and-downward confluence are on totally ordered worlds, so their endpoint normal forms and their counts do not determine the branching rooted-star orbit series. A search for exact orbit formulas, their initial counts, and synonymous frame conditions did not locate an equivalent classification; this is evidence of a gap, not a proof of worldwide novelty.

## Limitations

The theorem fixes the intuitionistic order to the rooted star; no enumeration for arbitrary two-level posets or all finite intuitionistic frames is claimed. Counts are up to order-preserving relational isomorphism; valuations and logical equivalence classes are not counted. General labelled two-level confluence counts are prior work. The computation checks only small rooted stars, and independent historical-priority review has not been performed. An unindexed equivalent Burnside count remains possible. No asymptotic orbit formula is asserted.

## References

[1] Philippe Balbiani and Çiğdem Gencer, “Four intuitionistic modal connectives,” arXiv:2606.07348, first posted June 5, 2026. https://arxiv.org/abs/2606.07348

[2] Philippe Balbiani, Han Gao, Çiğdem Gencer and Nicola Olivetti, “Local Intuitionistic Modal Logics and Their Calculi,” arXiv:2403.06772 (2024). https://arxiv.org/abs/2403.06772

[3] Han Gao and Nicola Olivetti, “Taming Complexity in Intuitionistic Modal Logic: The Case of FIK and Its Shallow Calculus,” arXiv:2606.31877, first posted June 30, 2026. https://arxiv.org/abs/2606.31877

[4] “Labelled two-level forward-and-downward confluence census,” unpublished mathematical note, record identifier `6bd1e200-ca4a-42d8-bc1d-791c874c1714`; its theorem gives labelled counts but no unlabelled orbit formula.
