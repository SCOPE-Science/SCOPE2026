# Sharp smallest inverse-incompatible dimensionalities of finite groups

## Finding

A **dimensionality** of an ordinary group \(G\), as in Jenča's definition, is an equivalence relation \(\sim\) such that \([1_G]=\{1_G\}\) and, for any two equivalence classes \(A,B\), the setwise product \(AB\) is a union of complete equivalence classes. It is *inverse-compatible* if inversion takes each class onto a class (equivalently, \(a\sim b\Rightarrow a^{-1}\sim b^{-1}\)).

The least order of any finite group admitting an inverse-incompatible dimensionality is **six**. On \(S_3\) there are exactly \(22\) dimensionalities with singleton identity class, of which exactly \(12\) are inverse-incompatible. The least order of any **finite abelian** group admitting one is **twelve**. On \(C_{12}\) there are exactly \(44\) such dimensionalities, exactly \(4\) inverse-incompatible, all in one orbit under \(\operatorname{Aut}(C_{12})\).

Moreover, the explicit examples below yield relational quotient monoids that are **not hypergroups**, showing that inverse compatibility is a genuine hypothesis in the polygroupoid-to-polygroupoid quotient theorem, even for abelian groups.

## Assumptions and scope

All groups in the extremal statements are finite and written multiplicatively unless \(C_{12}=\mathbb Z/12\mathbb Z\) is written additively. Each dimensionality must have singleton identity class. This is necessary for Jenča's unit condition for an ordinary group, because a group has just one unit.

For a partition \(\mathcal P\) of \(G\), the product \(AB=\{ab:a\in A,b\in B\}\) is setwise multiplication. The quotient relational monoid has hyperproduct \([a]*[b]=\{[xy]:x\in[a],y\in[b]\}\). No congruence assumption is imposed: the quotient multiplication may genuinely be multivalued.

## Proof

**1. Equivalence of the test and the dimensionality axiom.** For a group with singleton identity class, the lax-equivalence property is the condition
\[
\forall a,b,c\in G,\quad ab\sim c\Longrightarrow
\exists a'\sim a,\ b'\sim b:\ a'b'=c.
\]
Fixing classes \(A=[a]\), \(B=[b]\), this says that every member of the class of any element of \(AB\) already lies in \(AB\). Thus it is exactly the requirement that every class product \(AB\) be a union of classes. The singleton identity block guarantees the unit condition. Therefore the explicit products and exhaustive checker use precisely the original definition, not a stronger congruence condition.

**2. Six-element witness.** Let \(G=S_3\), with blocks
\[
E=\{1\},\quad X=\{(12),(23),(123)\},\quad Y=\{(13),(132)\}.
\]
Their setwise products satisfy \(EX=XE=X\), \(EY=YE=Y\), and
\[
XX=XY=YX=G,\qquad YY=E\cup X.
\]
These identities can also be checked directly using the six permutations. Every block product is a union of blocks, so the partition is a dimensionality. Inversion fails to preserve classes: the inverse of \((123)\in X\) is \((132)\in Y\), while the two transpositions in \(X\) are self-inverse. The quotient has \(E\in X*X\) and \(E\in X*Y\). A hypergroup requires that the identity occur in \(A*B\) precisely when \(B\) is the unique inverse of \(A\); therefore this quotient is not a hypergroup.

**3. Twelve-element abelian witness.** Let \(G=C_{12}\) be residues modulo twelve under addition, and take
\[
E=\{0\},\quad X=\{1,2,3,5,6,8\},\quad Y=\{4,7,9,10,11\}.
\]
Direct modular addition yields
\[
X+X=X+Y=G,\qquad Y+Y=X\cup Y.
\]
Thus the partition is a dimensionality. The additive inverses of elements of \(X\) include \(6\in X\) and \(11\in Y\); inversion is not compatible. Also \(0\in X+X\) and \(0\in X+Y\), so the quotient cannot be a hypergroup by the same unique-inverse criterion.

**4. Exhaustive sharp minimality and finite counts.** Every partition with identity block \(\{0\}\) of an \(n\)-element group occurs exactly once as a *restricted-growth word*: the identity has label zero, the first nonidentity element label one, and each subsequent label is an existing positive label or the next unused positive label. Hence there are exactly \(B_{n-1}\) candidates, where \(B_j\) is the \(j\)-th Bell number. The standalone Python checker exhaustively generates all these words and tests each class product using the full multiplication table. For every accepted partition it separately checks every quantified triple in the displayed original axiom. It then tests the inverse map, computed directly from the multiplication table.

The finite census is:

| Group | All dimensionalities | Inverse-incompatible |
|---|---:|---:|
| \(C_1,C_2,C_3,C_4,C_5\) | \(1,1,2,3,3\) | \(0\) throughout |
| \(C_6,C_7,C_8,C_9,C_{10},C_{11}\) | \(7,4,12,10,11,19\) | \(0\) throughout |
| \(C_2\times C_2\) | \(5\) | \(0\) |
| \(C_4\times C_2\) | \(28\) | \(0\) |
| \(C_2^3\) | \(100\) | \(0\) |
| \(C_3\times C_3\) | \(40\) | \(0\) |
| \(S_3\) | \(22\) | \(12\) |
| \(C_{12}\) | \(44\) | \(4\) |

Every group of order below six is cyclic or \(C_2\times C_2\). Every abelian group of order below twelve is cyclic or isomorphic to one of the four explicitly listed noncyclic groups, by the standard finite abelian-group classification. Hence the exhaustive counts and witnesses prove both claimed minimal orders. The checker additionally transforms the four exceptional \(C_{12}\) partitions under the four unit multipliers \(1,5,7,11\), confirming that they form one automorphism orbit.

## Verification

Execute the standalone file `dimensionality_boundary_check.py` with Python 3. It generates all candidates from the restricted-growth construction, constructs the group multiplication tables independently of external packages, and tests both block-product saturation and the original quantified decomposition axiom. The output ends in `DIMENSIONALITY_BOUNDARY_OK`, after verifying the witness multiplication tables, both minimality counts, and the \(C_{12}\) orbit statement. The finite enumeration is **exhaustive** for the stated orders; it is not an extrapolation to larger groups. Its algorithm is an executable certificate, not a formal proof-assistant verification.

## Relationship to prior work

Jenča, *Dimensionalities on monoids*, arXiv:2611.18000v1 (first public 13 November 2026), introduces dimensionalities, proves their relational-monoid quotient theorem, and proves the polygroupoid quotient theorem **under an inverse-compatibility hypothesis**. That paper does not state the two sharp finite-group boundaries or these inverse-incompatible witnesses. The present examples show this hypothesis is genuinely necessary in general, rather than merely a convenient proof assumption.

Haviv and Levy, *Dioid Partitions of Groups*, arXiv:1708.02974v2, study the more restrictive notion that **includes inverse compatibility as an axiom**. Their results for inverse-stable group partitions, including three-part partitions over prime cyclic groups, do not imply this inverse-unstable composite-order census. In particular, the witnesses above are not dioid partitions in their sense.

## Limitations

The minimum orders and boundary counts are about finite groups and finite abelian groups respectively, not arbitrary infinite groups. Only the first abelian boundary \(C_{12}\), not all abelian groups of order twelve, is completely counted. The two exhibited quotient monoids are non-hypergroups because they demonstrably have multiple inverse candidates, rather than merely because the partition fails inversion compatibility. The historical novelty comparison cannot rule out an unindexed equivalent result. Independent mathematical validation has not been conducted.

## References

1. G. Jenča, *Dimensionalities on monoids*, arXiv:2611.18000v1 (2026), https://arxiv.org/abs/2611.18000.
2. I. Haviv and D. Levy, *Dioid Partitions of Groups*, arXiv:1708.02974v2 (2018), https://arxiv.org/abs/1708.02974.
3. MSC2020, 20N20, hypergroups, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=20N.
