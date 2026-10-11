# Bounded-volume, quadratic-crossing asymmetric L-space knots
## Finding
Let \(K_{m,n}\) be the Himeno--Teragaito knot defined as the closure of the positive \((m+2)\)-braid
\[
[(1,2,\ldots,m+1)^{(m+2)n+2},(m+1,m,\ldots,1),1,2,1,1].
\]
For every \(m\ge3\) and \(n\ge1\),
\[
c(K_{m,n})=(m+1)(m+2)n+3m+7.
\]
Moreover, if
\[
V_0=\operatorname{Vol}(S^3\setminus L14n61770),
\]
then
\[
\operatorname{Vol}(S^3\setminus K_{m,n})<V_0.
\]

Writing \(b=m+2\), the same family consists of asymmetric hyperbolic L-space knots with braid index and bridge index \(b\), exact crossing number
\[
c(K_{b-2,n})=b(b-1)n+3b+1,
\]
and
\[
rac{\operatorname{Vol}(S^3\setminus K_{b-2,n})}{c(K_{b-2,n})}
<
rac{V_0}{b(b-1)n+3b+1}.
\]
In particular, for every \(b\ge5\),
\[
c(K_{b-2,1})=(b+1)^2,
\]
while the hyperbolic volumes remain below the same constant \(V_0\). Thus this sequence has volume density tending to \(0\) while braid index, bridge index and crossing number all diverge.

## Assumptions and scope
Crossing number means the minimum number of crossings among all planar diagrams of the knot. Braid index is the minimum number of strands in a closed-braid presentation.

The statement uses the family and parameter range \(m\ge3\), \(n\ge1\) in which Himeno and Teragaito prove asymmetry, hyperbolicity and the L-space property. Their paper also proves that the braid index is \(m+2\), that the bridge index agrees with it, and that
\[
g(K_{m,n})=rac{(m^2+3m+2)n}{2}+m+3.
\]

The volume bound uses the fixed cusped hyperbolic manifold \(M\) appearing in their proof, identified there with the complement of the census link `L14n61770`.

## Proof
Count the crossings in the displayed positive braid. The repeated block has length
\[
(m+1)((m+2)n+2),
\]
the descending block has length \(m+1\), and the final block has length \(4\). Hence the displayed diagram has
\[
c_D=(m+1)(m+2)n+3m+7
\]
crossings.

For every knot \(K\), the standard crossing--genus--braid-index inequality is
\[
c(K)\ge2g(K)+b(K)-1.
\]
One way to reconstruct it is to take any oriented diagram with \(c_D\) crossings and \(s_D\) Seifert circles. Its canonical Seifert surface has genus
\[
g_D=rac{c_D-s_D+1}{2},
\]
so \(g(K)\le g_D\) gives \(c_D\ge2g(K)+s_D-1\). Yamada's theorem says the minimum possible number of Seifert circles is the braid index, hence \(s_D\ge b(K)\).

For \(K_{m,n}\), the source gives \(b(K_{m,n})=m+2\) and
\[
2g(K_{m,n})=(m^2+3m+2)n+2m+6.
\]
Therefore
\[
2g(K_{m,n})+b(K_{m,n})-1
=(m+1)(m+2)n+3m+7=c_D.
\]
The displayed positive braid attains the universal lower bound, so it is crossing-minimal and the claimed exact crossing number follows.

For the volume statement, the source constructs a fixed hyperbolic manifold \(M\), homeomorphic to \(S^3\setminus L14n61770\), and identifies \(S^3\setminus K_{m,n}\) as a Dehn filling of \(M\) along the parameter-dependent slopes used in its asymmetry proof. For \(m\ge3\), \(n\ge1\), the resulting knot complement is hyperbolic. Hyperbolic volume strictly decreases under any nontrivial hyperbolic Dehn filling, so
\[
\operatorname{Vol}(S^3\setminus K_{m,n})
<
\operatorname{Vol}(M)=V_0.
\]

Finally set \(b=m+2\). Then
\[
(m+1)(m+2)n+3m+7=b(b-1)n+3b+1.
\]
For \(n=1\), this simplifies to
\[
b(b-1)+3b+1=(b+1)^2.
\]
Dividing the uniform volume bound by the exact crossing number proves the density estimate and its limit.

## Verification
The primary preprint was inspected at the defining braid, Theorem 1.1, Corollary 1.2 and the hyperbolic-filling construction. It states primary MSC \(57K10\), first posting date 2026-09-24, braid index \(m+2\), bridge index \(m+2\), the genus formula above, and identifies the common parent \(M\) with the complement of `L14n61770`.

The crossing lower bound was independently reconstructed from the Seifert-surface genus formula and Yamada's theorem. The strict volume inequality is the standard hyperbolic Dehn-filling volume theorem.

The bundled arithmetic regression checks all parameter pairs with \(3\le m\le102\) and \(1\le n\le100\). It prints:

`VERIFY_OK pairs=10000 crossing_identity=true n1_square_identity=true`

That finite check only guards the algebraic identities; the theorem is proved symbolically for all stated parameters.

## Relationship to prior work
Himeno and Teragaito prove that their family realizes every braid index above \(4\) by infinitely many asymmetric hyperbolic L-space knots, and they record the bridge index and genus. Their asymmetry proof also realizes every complement as a filling of one fixed hyperbolic manifold. The paper does not state a crossing-number formula, a uniform-volume consequence, or a volume-density comparison.

Yamada's theorem supplies the general crossing lower bound through the minimum-Seifert-circle characterization of braid index, while Thurston's hyperbolic Dehn-filling theory supplies strict volume decrease. Neither general result identifies the Himeno--Teragaito family or the simultaneous quadratic-crossing/uniform-volume behavior.

Searches for the family name together with crossing number, bounded volume, volume density, bridge index and the census parent `L14n61770` did not locate an equivalent statement. The closest indexed topology findings concerned a single asymmetric L-space census knot, Jones-span data, and unrelated exact knot-complexity invariants.

## Limitations
The exact crossing formula itself also holds for the source family in the broader range \(m\ge1\), \(n\ge1\) once its stated braid-index and genus facts are used, but the present theorem is intentionally restricted to \(m\ge3\) because that is the range where the source proves asymmetry and hyperbolicity.

No numerical value of \(V_0\) is needed or claimed. The result gives a uniform upper bound on volume, not monotonicity or an exact volume formula.

The proof combines recent family-specific information with classical general theorems; an unindexed note could have observed the same synthesis.

## References
1. K. Himeno and M. Teragaito, *Asymmetric L-space knots with arbitrary braid index*, arXiv:2609.28917v1, first posted 2026-09-24.
2. S. Yamada, *The minimal number of Seifert circles equals the braid index of a link*, Inventiones Mathematicae 89 (1987), 347--356, DOI `10.1007/BF01389082`.
3. W. P. Thurston, *The Geometry and Topology of Three-Manifolds*, Princeton lecture notes, 1978--1981.
4. J. S. Purcell, *Hyperbolic Knot Theory*, Graduate Studies in Mathematics 209, American Mathematical Society, 2020; Theorem 6.30 records strict volume decrease under hyperbolic Dehn filling.
