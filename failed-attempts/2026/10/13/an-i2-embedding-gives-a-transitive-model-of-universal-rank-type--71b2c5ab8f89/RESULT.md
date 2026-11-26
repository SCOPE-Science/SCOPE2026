# An \(I2\) embedding gives a transitive model of universal rank-type compactness
## Finding

Assume that there exists an \(I2\)-embedding. Then there is a transitive set-sized model
\[
M\models\mathrm{ZFC}
\]
such that, internally in \(M\), the following scheme holds:

For every logic \(\mathcal L\), there is a cardinal
\[
\lambda=\beth_\lambda
\]
such that for every ordinals
\[
\alpha<\lambda<\zeta
\]
there is a cardinal
\[
\alpha<\mu<\lambda
\]
for which \(\mathcal L\) is \((\mu,\lambda)\)-chain compact for rank type \((\zeta,\lambda)\).

Thus an \(I2\)-embedding gives a transitive-model upper consistency bound for a Makowsky-style universal compactness principle ranging over every logic.

## Assumptions and scope

The statement is a relative consistency statement with a transitive set-sized model as conclusion. It does not assert that the ambient universe itself satisfies the compactness scheme.

Following Osinski, a vocabulary carries a designated unary predicate \(P\). A structure \(A\) has rank type \((\zeta,\lambda)\) when
\[
\operatorname{rk}(A)=\zeta
\quad\text{and}\quad
\operatorname{rk}(P^A)=\lambda.
\]

For cardinals \(\mu,\lambda\), the logic \(\mathcal L\) is \((\mu,\lambda)\)-chain compact for rank type \((\zeta,\lambda)\) if every \(\mathcal L\)-theory \(T\) with
\[
|T|=\lambda
\]
that can be written as an increasing union
\[
T=\bigcup_{\xi<\mu}T_\xi
\]
has a model of rank type \((\zeta,\lambda)\) whenever every \(T_\xi\) has such a model.

All quantification over logics and all cardinal, rank, and compactness assertions in the conclusion are internal to \(M\).

## Proof

Lücke and Poveda prove in Theorem 1.3 of *The effects of forcing on exacting and ultraexacting cardinals* that the existence of an \(I2\)-embedding yields a transitive set-sized model
\[
M\models\mathrm{ZFC}+\text{“there is a proper class of exacting cardinals.”}
\]

Because \(M\) is a set-sized model, the displayed proper-class assertion is interpreted internally: the exacting cardinals of \(M\) are unbounded in \(\operatorname{Ord}^M\).

Osinski proves in Corollary 5.9 of *Compactness beyond choice and HOD* that, over ZFC, the following are equivalent:

1. there are unboundedly many exacting cardinals;
2. for every logic \(\mathcal L\), there is a cardinal \(\lambda=\beth_\lambda\) such that for every \(\alpha<\lambda<\zeta\) there is \(\alpha<\mu<\lambda\) for which \(\mathcal L\) is \((\mu,\lambda)\)-chain compact for rank type \((\zeta,\lambda)\).

Since \(M\models\mathrm{ZFC}\), Osinski's theorem applies inside \(M\). The first side of the equivalence holds there by Lücke--Poveda's construction, so the second side holds there as well.

No upward absoluteness of exactingness or compactness from \(M\) to the ambient universe is used or claimed.

## Verification

Osinski's arXiv record gives first public submission on 21 September 2026 and explicitly lists primary MSC \(03E55\). Definition 3.2 defines rank type, Definition 5.3 defines \((\mu,\lambda)\)-chain compactness with the theory-size restriction, and Corollary 5.9 gives the exact equivalence between unboundedly many exacting cardinals and the universal compactness scheme used here.

Lücke--Poveda's Theorem 1.3 states that an \(I2\)-embedding yields a transitive set-sized model of ZFC with a proper class of exacting cardinals. Their proof constructs a model with unboundedly many exacting cardinals and then obtains a transitive set-sized model; the paper contains no occurrence of “compactness” and does not cite Osinski's compactness preprint.

The deduction therefore consists only of applying a theorem of ZFC internally to the transitive ZFC model supplied by the later forcing theorem.

## Relationship to prior work

Osinski identifies unbounded exacting cardinals with a universal compactness scheme ranging over every logic, but his paper contains no \(I2\) statement and does not supply the later transitive-model consistency upper bound.

Lücke and Poveda establish the \(I2\)-to-proper-class-exacting transitive-model theorem, but their paper does not formulate a logical compactness consequence.

The present synthesis transfers the later consistency construction across Osinski's exact equivalence. Published-finding database searches for the combined \(I2\), proper-class-exacting, and universal rank-type compactness statement did not return an equivalent result.

## Limitations

The conclusion is internal to a transitive set-sized model of ZFC. It is not a claim that the ambient universe satisfies the universal compactness scheme.

No lower bound or equiconsistency with \(I2\) is asserted. In particular, the result only supplies an upper consistency bound.

The argument depends on Osinski's specific rank-type compactness notion and its theory-size restriction; it does not imply unrestricted ordinary compactness for every logic.

The result is a synthesis of two recent theorems rather than a new forcing construction.

## References

[1] Jonathan Osinski, “Compactness beyond choice and HOD,” arXiv:2609.25291, first submitted 21 September 2026; Corollary 5.9, Definition 3.2, Definition 5.3.

[2] Philipp Lücke and Alejandro Poveda, “The effects of forcing on exacting and ultraexacting cardinals,” arXiv:2609.32338, first submitted 26 September 2026; Theorem 1.3 and its proof in Section 3.
