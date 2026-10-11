# Uniform Klein-four quotient description for all magic octic--dodecic K3 maps
## Finding
Let \(S\subset \mathbf P^5\) be any magic octic K3 model in Auel--Singer, and let \(\widetilde S\) be its minimal resolution. For any partition \(P\) of the six homogeneous coordinates into three unordered pairs, write \(S'_P\) for the associated magic dodecic K3 surface and \(\widetilde S'_P\) for its minimal resolution. Then the pair-sign group
\[
G_P=(\mu_2)^3/\mu_2\cong (\mathbf Z/2\mathbf Z)^2
\]
acts symplectically on \(\widetilde S\), and \(\widetilde S'_P\) is isomorphic to the minimal resolution of \(\widetilde S/G_P\).

Consequently the Klein-four quotient description that Auel--Singer establish for Bremner's smooth magic octic holds uniformly for every magic octic model and for each of the 15 coordinate-pair partitions.

## Assumptions and scope
The ground field is \(\mathbf C\). The octic model \(S\) is one of the complete intersections of three diagonal quadrics considered in Auel--Singer; it may have rational double points, and \(\widetilde S\) denotes its crepant minimal resolution. A partition \(P\) consists of three disjoint unordered pairs whose union is the six coordinates. The associated dodecic is the closure of the image of the product-coordinate map to \( (\mathbf P^1)^3\) obtained from those three pairs.

The conclusion concerns the minimal resolutions and makes no assertion that the singular models themselves are isomorphic before resolution.

## Proof
For a chosen partition \(P\), independently multiply the two coordinates in each pair by a common sign. Modulo simultaneous global sign this gives a group \(G_P\) of order four. Because the three defining quadrics of \(S\) are diagonal, every such pair-sign change preserves \(S\). The action lifts uniquely to the minimal resolution of the rational double points.

The product-coordinate map is unchanged by pair-sign changes, so the dominant rational map \(p_P:S\dashrightarrow S'_P\) is \(G_P\)-invariant. Auel--Singer prove for these maps that the generic fiber has four points and is exactly an orbit of the pair-sign group. Hence
\[
\mathbf C(S'_P)\subseteq \mathbf C(S)^{G_P}\subseteq \mathbf C(S)
\]
and both the left and right field extensions have degree four. Therefore
\[
\mathbf C(S'_P)=\mathbf C(S)^{G_P}.
\]
Thus \(S'_P\) is birational to the quotient \(S/G_P\), and equivalently \(\widetilde S'_P\) is birational to the minimal resolution of \(\widetilde S/G_P\).

It remains to identify the quotient resolution as a K3 surface. A nontrivial class in \(G_P\) can be represented by changing the signs on one pair, or equivalently on the complementary two pairs. In either representation an even number of the six homogeneous coordinates changes sign, so the determinant on the ambient coordinate space is \(+1\). The defining diagonal quadrics themselves are fixed. The Poincare-residue generator of the holomorphic two-form of the complete intersection is therefore fixed on the smooth locus. Since the singularities are rational double points, this form extends across the crepant minimal resolution, and the lifted \(G_P\)-action on \(\widetilde S\) is symplectic.

For a finite symplectic group acting on a complex K3 surface, the quotient has only rational double points and its minimal resolution is again a K3 surface. Let \(Z_P\) denote that resolution. The function-field equality above gives a birational map \(Z_P\dashrightarrow \widetilde S'_P\). Both are smooth projective K3 surfaces, hence minimal surfaces of Kodaira dimension zero, so a birational map between them is an isomorphism. Therefore \(Z_P\cong \widetilde S'_P\).

## Verification
The bundled script `artifacts/verify_pair_sign_quotient.py` independently enumerates all 15 perfect matchings of six coordinates. For each matching it constructs the four projective pair-sign classes, checks that every representative has determinant \(+1\), checks invariance of arbitrary diagonal quadratic monomials, and checks invariance of all three product coordinates. Its recorded output ends in `VERIFY_OK`.

The infinite geometric steps are not inferred from this finite enumeration. They are the function-field argument above together with the standard theorem that a tame finite symplectic quotient of a K3 surface has rational double points and K3 minimal resolution.

## Relationship to prior work
Auel--Singer construct the associated dodecic projections, prove that the maps have degree four with generic fibers equal to pair-sign orbits, and explicitly identify the associated dodecics as resolutions of Klein-four symplectic quotients in the special case of Bremner's smooth magic octic. Their statement of the quotient interpretation is specialized to that smooth model.

The present argument shows that the same quotient interpretation survives for every magic octic model after resolving its rational double points. General work on symplectic automorphisms of K3 surfaces supplies the quotient theorem, but does not identify these particular magic dodecics as those quotients.

## Limitations
This result does not compute the Neron--Severi lattices of the quotient resolutions, fixed-point configurations for each singular octic model, or an integral Hodge isometry beyond what follows from the quotient correspondence. It also does not claim a new classification of finite symplectic groups on K3 surfaces. The originality is the uniform identification of Auel--Singer's explicit dodecic images with the Klein-four quotient resolutions outside the Bremner case.

## References
1. Asher Auel and Benjamin Singer, *The algebraic geometry of 3-by-3 magic squares of squares*, arXiv:2609.09351v1, first posted 2026-09-08.
2. Yuya Matsumoto, *On \(\mu_n\)-actions on K3 surfaces in positive characteristic*, Nagoya Mathematical Journal 249 (2023), 11--49, DOI 10.1017/nmj.2022.20; Theorem 5.1 includes the characteristic-zero tame symplectic quotient statement.
3. Benedetta Piroddi, *K3 surfaces with a symplectic automorphism of order 4*, Mathematische Nachrichten 297 (2024), 2302--2332, DOI 10.1002/mana.202300052.
