# Torsion-lift criterion and Henselian classification for commutative generalized quasi t-fine rings

## Statement

Let \(R\) be a commutative ring with Jacobson radical \(J=J(R)\), and let
\[
\mathcal T(R)=\{u\in R^\times:u^n=1\text{ for some }n\ge1\}.
\]
Write \(\pi:R\to R/J\) for reduction. Following Bien--Danchev--Ramezan-Nassab, \(R\) is **generalized quasi \(t\)-fine** when every element of \(R\setminus J\) is a sum of a torsion unit and a quasinilpotent. Their Section 3 also records that, for commutative rings, the quasinilpotents are exactly \(J(R)\).

### Theorem 1 (exact commutative criterion)

A commutative ring \(R\) is generalized quasi \(t\)-fine if and only if

1. \(R\) is local, and
2. the reduction map
   \[
   \pi:\mathcal T(R)\longrightarrow (R/J)^\times
   \]
   is surjective.

Equivalently, generalized quasi \(t\)-fineness in the commutative case is exactly the assertion that every nonzero residue class has a torsion-unit representative.

### Theorem 2 (Henselian classification)

Let \((R,\mathfrak m,k)\) be a commutative Henselian local ring. Then
\[
\boxed{R\text{ is generalized quasi }t\text{-fine}\iff k\text{ is a locally finite field}.}
\]
Here “locally finite” means algebraic over a finite prime field, equivalently every finitely generated subfield is finite.

Consequently:

- every commutative complete local ring is generalized quasi \(t\)-fine exactly when its residue field is locally finite;
- for any commutative local ring \((A,\mathfrak m,k)\), its Henselization \(A^h\) is generalized quasi \(t\)-fine exactly when \(k\) is locally finite;
- \(\mathbb Z_p\) is generalized quasi \(t\)-fine for every prime \(p\);
- for a locally finite field \(F\), every formal power-series ring \(F[[x_1,\ldots,x_d]]\) is generalized quasi \(t\)-fine.

### Theorem 3 (a sharp localization/completion boundary)

For the localization \(\mathbb Z_{(p)}\),
\[
\boxed{\mathbb Z_{(p)}\text{ is generalized quasi }t\text{-fine}\iff p\in\{2,3\}.}
\]
Thus, for every prime \(p\ge5\), \(\mathbb Z_{(p)}\) is not generalized quasi \(t\)-fine, whereas its \(p\)-adic completion \(\mathbb Z_p\) is. This isolates torsion lifting, rather than merely the residue field, as the missing condition in the non-Henselian setting.

## Proof

For a commutative ring, \(\mathcal Q(R)=J(R)\). Suppose first that \(R\) is generalized quasi \(t\)-fine. If \(a\notin J\), write
\[
a=u+q,\qquad u\in\mathcal T(R),\ q\in J.
\]
Then
\[
a=u(1+u^{-1}q)
\]
is a unit because \(1+u^{-1}q\in1+J\subseteq R^\times\). Hence every element outside \(J\) is a unit, so \(R\) is local with maximal ideal \(J\). If \(\bar a\in(R/J)^\times\), choose a lift \(a\notin J\); the same decomposition gives \(\bar a=\bar u\), proving surjectivity of \(\mathcal T(R)\to(R/J)^\times\).

Conversely, suppose \(R\) is local and that reduction on torsion units is surjective. For any \(a\notin J\), choose \(u\in\mathcal T(R)\) with \(\pi(u)=\pi(a)\). Then \(a-u\in J=\mathcal Q(R)\), so \(a\) has the required generalized quasi \(t\)-fine decomposition. This proves Theorem 1.

Theorem 1 also shows that the residue field of any commutative generalized quasi \(t\)-fine ring has torsion multiplicative group. Such a field must have positive characteristic: in characteristic zero the element \(2\) in the prime subfield has infinite multiplicative order. If the characteristic is \(p\), every nonzero element \(a\) satisfies \(a^n=1\) for some \(n\), hence is algebraic over \(\mathbb F_p\). Thus the residue field is locally finite.

Now let \((R,\mathfrak m,k)\) be Henselian and assume \(k\) is locally finite. For \(\bar a\in k^\times\), let \(n\) be its finite multiplicative order. Since \(k\) has characteristic \(p>0\), \(p\nmid n\). The residue polynomial
\[
\bar f(X)=X^n-1
\]
has \(\bar a\) as a simple root because
\[
\bar f'(\bar a)=n\bar a^{n-1}\ne0.
\]
Hensel's lemma therefore gives \(u\in R\) reducing to \(\bar a\) with \(u^n=1\). Hence every nonzero residue class has a torsion-unit lift, and Theorem 1 applies. The converse was proved in the preceding paragraph, establishing Theorem 2. Complete local rings are Henselian, and Henselization preserves the residue field, yielding the stated consequences.

For Theorem 3, \(\mathbb Z_{(p)}\) is local with residue field \(\mathbb F_p\). Its torsion units are exactly the torsion elements of \(\mathbb Q^\times\), namely \(\{\pm1\}\). Their reductions fill \(\mathbb F_p^\times\) precisely for \(p=2\) or \(p=3\). Theorem 1 gives the classification. On the other hand, \(\mathbb Z_p\) is complete local with residue field \(\mathbb F_p\), so Theorem 2 makes it generalized quasi \(t\)-fine for every \(p\).

## Further consequences

If a commutative local ring has finite residue field \(\mathbb F_q\), Theorem 1 can be checked with one residue generator: since \(\mathbb F_q^\times\) is cyclic, the ring is generalized quasi \(t\)-fine if and only if some torsion unit reduces to a generator of \(\mathbb F_q^\times\).

The Henselian hypothesis in Theorem 2 is a sufficient lifting mechanism, not part of the exact general criterion. For instance, whenever a local ring contains a locally finite coefficient field mapping isomorphically onto its residue field, Theorem 1 applies directly because all nonzero coefficient-field elements are torsion. Thus the exact obstruction is failure of torsion-unit lifting, not failure of Henselianity itself.

The characteristic-zero examples above also sharply separate generalized quasi \(t\)-fineness from generalized \(t\)-fineness: Bien--Danchev--Ramezan-Nassab prove that generalized \(t\)-fine rings have positive characteristic, while \(\mathbb Z_p\) is generalized quasi \(t\)-fine for every prime \(p\).

## Relation to prior work and limitations

Bien--Danchev--Ramezan-Nassab introduce generalized quasi \(t\)-fine rings, give \(F[[x]]\) for finite \(F\) and \(\mathbb Z_{(2)}\) as commutative examples, record \(\mathcal Q(R)=J(R)\) for commutative rings, and prove that the center of any generalized quasi \(t\)-fine ring is local. Their paper does not state the torsion-unit reduction criterion or the Henselian/complete-local classification above.

Hensel's simple-root lifting theorem and the fact that complete local rings are Henselian are standard prior art and are used here as the lifting mechanism; they are not claimed as new. Likewise, lifting roots of unity in Henselian local rings is a standard application of Hensel's lemma.

The result is confined to commutative rings. It does not settle the paper's Problem 3.12 about quasi \(t\)-fine rings versus fine rings, nor does it classify the noncommutative generalized quasi \(t\)-fine case. Originality is asserted only to the best of our knowledge; because the source notion is very recent and the commutative reduction is concise once \(\mathcal Q(R)=J(R)\) is observed, a later revision or concurrent note could independently contain an equivalent criterion.

## References

1. M. H. Bien, P. V. Danchev, M. Ramezan-Nassab, *Generalized t-Fine and Quasi t-Fine Rings*, arXiv:2609.19882 (2026). https://arxiv.org/abs/2609.19882
2. The Stacks Project, Section 10.153, *Henselian local rings*, Tag 04GE. https://stacks.math.columbia.edu/tag/04GE
3. The Stacks Project, Lemma 10.153.9, *Complete local rings are Henselian*, Tag 04GM. https://stacks.math.columbia.edu/tag/04GM
4. The Stacks Project, Section 10.155, *Henselization and strict henselization*, Tag 0BSK. https://stacks.math.columbia.edu/tag/0BSK
