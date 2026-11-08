# Discriminant, maximal tangencies, and wreath-product monodromy of even Fermat-surface projections

## Finding

For every even integer \(d=2m\ge4\), project the complex Fermat surface \(F_d=\{X^d+Y^d+Z^d+W^d=0\}\subset\mathbb P^3\) from the exterior point \(P=[1:1:0:0]\). The resulting finite degree-\(d\) map \(p:F_d\to\mathbb P^2\) has exactly \(m\) reduced branch-curve components, all smooth plane Fermat curves of degree \(d\), with exactly \(d\) common points at which *each pair* has contact order \(d\). The discriminant has multiplicity one on one distinguished component and multiplicity two on every other component. Its full geometric monodromy/Galois-closure group, not just its group of deck transformations, is \((\mathbb Z/2\mathbb Z)^m\rtimes S_m\), while the deck group is \(\mathbb Z/2\mathbb Z\).

More explicitly, put \(r=d-1\), \(u=(X+Y)/2\), \(v=(X-Y)/2\), and \(S=Z^d+W^d\). For each orbit \([\lambda]=\{\lambda,\lambda^{-1}\}\) of the roots of \(\lambda^r=-1\), define
\[
 c_{[\lambda]}=-\frac{2^d}{(\lambda-1)^r}.
\]
These are exactly \(m\) distinct nonzero complex constants, including \(c_{[-1]}=2\). For \(B_c=\{S+c v^d=0\}\subset\mathbb P^2_{[v:Z:W]}\), the scheme-theoretic discriminant divisor is
\[
\boxed{\operatorname{Disc}(p)=B_2+2\sum_{c\ne2}B_c.}
\]
The ramification divisor on \(F_d\) has \(d-1\) smooth degree-\(d\) plane-curve components, all passing through exactly \(d\) points and meeting pairwise transversely there. The reduced branch curve has exactly those \(d\) singular points; at each point its local equation is analytically \(\prod_c(s+c v^d)=0\), with \(s\) an analytic local parameter transverse to \(v\). Thus the local delta invariant is \(d\binom m2\) and the Milnor number is \(d m(m-1)-m+1\). In the first case \(d=4\), the branch curve consists of two smooth quartics tangent to order four at four points, giving four \(A_7\) singularities; the monodromy is the order-eight dihedral group.

## Assumptions and scope

Work over \(\mathbb C\), in characteristic zero, with even \(d\ge4\). The Fermat surface is smooth. The center \(P=[1:1:0:0]\) is exterior to it because \(1^d+1^d\ne0\), so linear projection is a finite morphism. The target coordinates are \([v:Z:W]\); in these coordinates the inverse-image equation is
\[
 f(u;v,Z,W)=(u+v)^d+(u-v)^d+Z^d+W^d=0.
\]
The term *discriminant* refers to the homogeneous polynomial discriminant of this degree-\(d\) polynomial in \(u\), or equivalently the branch discriminant with its natural vanishing multiplicities. The reduced support and the ramification scheme are stated separately. The monodromy group is the permutation group on a geometric generic fiber; the deck group denotes automorphisms of the original cover over the target. No statement is made about odd degrees, other centers, or fields of positive characteristic.

## Proof

**Critical roots and branch factors.** Differentiation gives
\[
 \frac{\partial f}{\partial u}=d\big((u+v)^r+(u-v)^r\big).
\]
For generic \(v\ne0\), a critical root has \(u=\alpha_\lambda v\), where \(\lambda^r=-1\) and \(\alpha_\lambda=(\lambda+1)/(\lambda-1)\). The Möbius transformation is injective on these \(d-1\) roots; hence the critical roots are simple. Substitution yields \(f(\alpha_\lambda v)=S+c_{[\lambda]}v^d\). Replacing \(\lambda\) by \(\lambda^{-1}\) negates \(\alpha_\lambda\) and preserves \(c_{[\lambda]}\); only \(\lambda=-1\) is its own inverse, and there \(u=0\), \(c=2\). To see that different orbits have distinct constants, write \(\lambda=e^{i\theta}\) for \(\theta=(2k+1)\pi/r\), \(0\le k<r\). Then \(|c|=2/|\sin(\theta/2)|^r\), which is strictly distinct apart from the inverse-paired angles. The discriminant is the resultant with the derivative, up to a nonzero scalar; each nonzero paired critical root contributes two equal factors and the zero critical root contributes one. Its homogeneous degree is \(d(d-1)\), exactly the combined degree of the proposed factors, so no additional discriminant factor occurs at \(v=0\). This proves the discriminant divisor formula.

**Intersections and local singularities.** Each \(B_c\) is a smooth plane Fermat curve: since \(c\ne0\), its three projective partial derivatives vanish simultaneously only at the excluded all-zero coordinates. For distinct \(c,c'\), their equations imply \(v=0\) and \(Z^d+W^d=0\), giving exactly \(d\) distinct points. At any one of these, \(s=Z^d+W^d\) and \(v\) are analytic coordinates on the target, and the branch germs are \(s+c v^d=0\). Thus every two branches have intersection multiplicity \(d\); all are smooth, so the total delta invariant is the sum of the \(\binom m2\) pairwise intersection multiplicities and the reduced curve has no other singularities. For a reduced plane curve with \(m\) branches, \(\mu=2\delta-m+1\), yielding the stated Milnor number. At \(d=4\), a two-branch order-four tangency is analytically \(y^2=x^8\), the singularity \(A_7\).

**The ramification divisor.** The derivative has the distinct linear factors \(u-\alpha_\lambda v\). Intersecting each of these planes with \(F_d\) gives \(S+c_{[\lambda]}v^d=0\), a smooth Fermat plane curve. Two different planes meet on \(F_d\) only where \(u=v=0\), which requires \(S=0\) and consists of the same \(d\) points. Near such a point, \(u,v\) are analytic coordinates on \(F_d\), since a partial derivative of \(S\) is nonzero; the component germs are distinct straight lines \(u=\alpha_\lambda v\). Hence these are precisely \(d\) ordinary \((d-1)\)-fold points of the reduced ramification divisor. Each component maps isomorphically onto \(B_{c_{[\lambda]}}\); the two inverse-paired components of the ramification divisor have the same image.

**Full geometric monodromy.** On the affine chart \(v=1\), put \(t=u^2\), \(s=Z^d+W^d\), and
\[
 H_m(t)=2\sum_{j=0}^{m}\binom{2m}{2j}t^j.
\]
Then \(f=H_m(u^2)+s\). The \(m-1\) nonzero critical pairs \(u=\pm\alpha_\lambda\) correspond to \(m-1\) simple, distinct critical points of the degree-\(m\) polynomial \(H_m(t)\), with pairwise distinct critical values. Consequently the degree-\(m\) cover \(s=-H_m(t)\) has local transpositions around each finite branch value; these transpositions generate a transitive subgroup because \(H_m(t)+s\) is irreducible over \(\mathbb C(s)\), and therefore generate \(S_m\). On lifting through \(u^2=t\), the full monodromy lies in \((\mathbb Z/2\mathbb Z)^m\rtimes S_m\). The additional, distinct branch value \(s=-2\) has \(t=0\) as a simple root because \(H_m(0)=2\) and \(H'_m(0)=d(d-1)\ne0\); its local inertia flips the two square roots of this one \(t\)-sheet and fixes the other sheets. Conjugating that single-pair flip by the surjective \(S_m\)-action supplies all \(m\) independent flips. Thus the full geometric monodromy over \(\mathbb C(s)\) is exactly the stated wreath product.

Finally, the substitution \(s=z^d+w^d\) does not shrink this geometric group: \(\mathbb C(z,w)/\mathbb C(s)\) is a regular function-field extension, since the generic plane curve \(z^d+w^d=s\) is geometrically integral over \(\overline{\mathbb C(s)}\). It is therefore linearly disjoint from the finite Galois splitting field of \(H_m(u^2)+s\), so the group remains unchanged over the generic base function field \(\mathbb C(z,w)\). The deck automorphisms centralize its action on the \(d\) sheets. The centralizer of the full wreath product in \(S_d\), for \(m\ge2\), is the diagonal simultaneous swap of every pair, a group of order two; it is realized by \(u\mapsto-u\). This determines the deck group.

## Verification

The accompanying standalone `verify.py` uses symbolic integer arithmetic to check, for \(d\in\{4,6,8,10\}\), that
\[
 \operatorname{disc}_u\big((u+1)^d+(u-1)^d+s\big)=(-1)^m2^{d-1}(s+2)\operatorname{Res}_t\big(H_m(t)+s,H'_m(t)\big)^2,
\]
that the nonzero critical-value factor is squarefree and does not vanish at \(s=-2\), and that its degree is \(m-1\). The program also checks the formula for \(c_{[-1]}\). Its `VERIFY_OK` output records exact finite-case algebraic consistency, not a proof for every \(d\). The preceding arguments establish the uniform theorem without relying on finite enumeration.

## Relationship to prior work

Miura and Taki, *Quasi-Galois points for quartic surfaces* (arXiv:2608.25445, first publicly posted 2026-08-26), study quasi-Galois centers of smooth quartic surfaces and enumerate the 28 such centers for the Fermat quartic. Their normal form motivates the particular special projection considered here, but the inspected paper does not establish the all-even-degree discriminant factorization, order-\(d\) tangency singularities, or full wreath-product geometric monodromy. Miura and Takahashi, *Projective Lifting Theorem, Complex Reflection Groups, and Quasi-Galois Points for Fermat Varieties* (arXiv:2610.09331, first posted 2026-10-07), also treats the classification of quasi-Galois points for Fermat varieties. Only its abstract and metadata were accessible for this comparison; it is an explicit historical-priority uncertainty, particularly for general even \(d\). Ciliberto and Flamini, *On the branch curve of a general projection of a surface to a plane* (arXiv:0811.0467), prove results for general projection centers, which do not cover the special reducible branch divisor here. General polynomial-cover monodromy theory supplies the wreath-product upper bound in decomposable cases, but the exact group and geometric ramification stratification here require the explicit critical-value analysis.

## Limitations

Historical priority is qualified by the inaccessible full text of arXiv:2610.09331 and potentially implicit general polynomial-cover statements. The result is for even-degree Fermat surfaces over \(\mathbb C\) and this one distinguished family of projection centers. No assertion is made about other centers, deformations, odd degrees, or characteristic-positive fibers. Independent mathematical audit has not been performed.

## References

1. Kei Miura and Shingo Taki, *Quasi-Galois points for quartic surfaces*, arXiv:2608.25445 (v1, 2026-08-26), https://arxiv.org/abs/2608.25445.
2. Kei Miura and Takeshi Takahashi, *Projective Lifting Theorem, Complex Reflection Groups, and Quasi-Galois Points for Fermat Varieties*, arXiv:2610.09331 (2026-10-07), https://arxiv.org/abs/2610.09331.
3. Ciro Ciliberto and Flaminio Flamini, *On the branch curve of a general projection of a surface to a plane*, arXiv:0811.0467, https://arxiv.org/abs/0811.0467.
4. Joachim König and Danny Neftin, *Reducible Fibers of Polynomial Maps*, arXiv:2001.03630, https://arxiv.org/abs/2001.03630.
