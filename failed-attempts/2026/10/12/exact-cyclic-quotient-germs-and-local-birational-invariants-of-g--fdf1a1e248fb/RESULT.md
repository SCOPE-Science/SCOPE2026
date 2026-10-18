# Exact cyclic-quotient germs and local birational invariants of generic reciprocal planes

## Finding
Let \(n\ge 4\), and let \(H_1,\ldots,H_n\) be distinct projective lines in \(\mathbb P^2_{\mathbb C}\) with no three concurrent. Choose defining nonzero linear forms \(\ell_i\), and let \(X\subset\mathbb P^{n-1}\) be the projective reciprocal plane, the closure of
\[
 [x]\longmapsto [1/\ell_1(x):\cdots:1/\ell_n(x)]
 =\left[\prod_{j\ne1}\ell_j(x):\cdots:\prod_{j\ne n}\ell_j(x)\right].
\]
Put \(r=n-2\) and let \(p_i\) denote the \(i\)-th coordinate vertex of \(\mathbb P^{n-1}\). Then:

1. The complete local germ of \(X\) at every \(p_i\) is the full degree-\(r\) Veronese surface cone, not merely a cone with the same tangent cone:
\[
 \widehat{\mathcal O}_{X,p_i}\;\cong\;\mathbb C[[s,t]]^{\mu_r},
 \qquad \zeta\cdot(s,t)=(\zeta s,\zeta t).
\]
In particular \(p_i\) has cyclic quotient type \(\frac1r(1,1)\). There are no other singular points.

2. At every singular point,
\[
 \operatorname{Cl}(\mathcal O_{X,p_i})\cong \mathbb Z/r\mathbb Z,\qquad
 e(\mathcal O_{X,p_i})=r,\qquad
 \operatorname{edim}(\mathcal O_{X,p_i})=r+1.
\]
The local Gorenstein index equals \(r/\gcd(r,2)\), and the minimal log discrepancy equals \(2/r\). Thus all singularities are klt; they are canonical and Gorenstein exactly when \(n=4\). For \(n\ge5\) they are noncanonical and non-Gorenstein, although \(\mathbb Q\)-Gorenstein.

The published singular-support and tangent-cone theorem already gives the singular points and Veronese tangent cones. The blowup of the arrangement double points, together with contraction of the strict arrangement lines, is also a published geometric model (Schenck, Theorem 3.4). The assertion assessed here is the **full local analytic normal form**—an explicit nonlinear coordinate automorphism identifying each completed local ring with its Veronese tangent cone—and the resulting local divisor, Gorenstein-index and log-discrepancy classification.

## Assumptions and scope
All varieties and completions are over \(\mathbb C\). The condition that no three arrangement lines meet is equivalent to a realization of the uniform rank-three matroid on \(n\) elements. It is essential: coincident lines or triple concurrencies can change the singular strata and invalidate the local normal form. Quotient type refers to the completed analytic germ of an isolated normal surface singularity. The singular-locus assertion refers to its reduced support, not to a proposed primary decomposition of a Jacobian singular scheme.

## Proof
**Previously established global blowup model (rederived for context).** Schenck, Theorem 3.4, already identifies the image of the blowup of the arrangement intersection points and proves contraction of the arrangement lines. The following calculations recall that model but are not proposed as new. Set \(F_i=\prod_{j\ne i}\ell_j\). Away from the pairwise line intersections, at least one \(F_i\) is nonzero. At the intersection \(q_{ij}=H_i\cap H_j\), the remaining forms are units in the local ring, so \(F_i\) and \(F_j\) generate the maximal ideal \((\ell_j,\ell_i)\), and all other \(F_k\) lie in its square. Thus the base scheme is exactly the reduced set of \(\binom n2\) pairwise intersection points. Blowing up these points resolves the map; on the exceptional curve \(E_{ij}\), the two leading coordinates \(F_i,F_j\) vary as independent linear forms, and all others vanish to higher order. Hence \(E_{ij}\) maps isomorphically to \(\overline{p_ip_j}\).

Along \(H_i\) away from its intersection points, only \(F_i\) is nonzero, so its entire strict transform \(\widetilde H_i\) maps to \(p_i\). Distinct strict transforms are disjoint because all their intersections were blown up. Each is isomorphic to \(\mathbb P^1\), with
\[
 \widetilde H_i^2=1-(n-1)=-(n-2)=-r.
\]
The map is birational because reciprocating coordinates on the dense torus recovers the original linear subspace. Its fibers outside the coordinate vertices have degree one: on the dense torus the inverse is explicit, on each coordinate line it is furnished by the corresponding exceptional \(E_{ij}\), and there are no other support strata for a uniform rank-three matroid. The published flat-stratification and singular-support results cited below also show that \(X\) is smooth off its coordinate vertices. Local normality at those vertices follows from the calculation below, so the morphism is a resolution. Since each contracted irreducible curve has self-intersection \(-r\le-2\), there is no exceptional \((-1)\)-curve, hence the resolution is minimal.

**Exact local coordinate change.** Fix \(i\). Choose linear coordinates \((u,v,w)\) on the original three-space so that \(u=\ell_i\). For every \(j\ne i\), write
\[
 \ell_j=\alpha_j u+L_j(v,w),
\]
where the binary linear forms \(L_j\) are pairwise nonproportional: otherwise two lines would meet \(H_i\) at the same point, contradicting the absence of triple intersections. On the target affine chart \(Y_i\ne0\), write \(y_j=Y_j/Y_i\). On a dense subset we have
\[
 y_j=\frac{u}{\alpha_j u+L_j(v,w)}.
\]
The functions \(1-\alpha_jy_j\) are units at the origin \(p_i\). Consequently
\[
 z_j=\frac{y_j}{1-\alpha_jy_j},\qquad
 y_j=\frac{z_j}{1+\alpha_jz_j}
\]
are mutually inverse regular changes of local coordinates, with
\[
 z_j=\frac{u}{L_j(v,w)}.
\]
Let \(T(v,w)=\prod_{k\ne i}L_k(v,w)\) and \(Q_j(v,w)=T(v,w)/L_j(v,w)\), for \(j\ne i\). Each \(Q_j\) is a homogeneous binary form of degree \(r=n-2\). The transformed image has dense parametrization
\[
 (z_j)_{j\ne i}=\lambda\,(Q_j(v,w))_{j\ne i},
 \qquad \lambda=\frac{u}{T(v,w)}.
\]
There are exactly \(r+1=n-1\) such forms. They constitute a basis of the vector space \(H^0(\mathbb P^1,\mathcal O(r))\): evaluating a linear relation at the zero of any \(L_j\) annihilates every \(Q_k\) except \(Q_j\), which remains nonzero. Their projective image is therefore the complete rational normal curve of degree \(r\), and the affine closure of the displayed parametrization is precisely its homogeneous cone. Since the coordinate changes are regular isomorphisms on neighborhoods of their origins and the two images have a common dense parametrization, their reduced irreducible scheme closures agree there. Taking completed local rings gives the asserted exact germ, rather than merely an isomorphism of associated graded rings.

**Divisors, canonical index and discrepancy.** The degree-\(r\) Veronese cone has homogeneous coordinate ring \(\bigoplus_{k\ge0}\mathbb C[s,t]_{kr}=\mathbb C[s,t]^{\mu_r}\). In its two-dimensional toric lattice \(N=\mathbb Z^2+\frac1r(1,1)\mathbb Z\), the two primitive rays are the standard coordinate rays. Thus the toric divisor exact sequence has cokernel \(N/\mathbb Z^2\cong\mathbb Z/r\mathbb Z\), which is its local divisor-class group. The projectivized tangent cone is the degree-\(r\) rational normal curve, giving Hilbert–Samuel multiplicity \(r\), while the degree-\(r\) monomials form a minimal set of \(r+1\) tangent-space generators.

The generator of \(\mu_r\) acts on the volume form \(ds\wedge dt\) by \(\zeta^2\), so the local canonical/Gorenstein index is \(r/\gcd(r,2)\). Adjunction along a contracted \((-r)\)-curve \(C\) gives \(K_{\widetilde X}\cdot C=r-2\), and writing \(K_{\widetilde X}=f^*K_X+aC\) yields \(a=2/r-1\). The unique exceptional curve on the minimal toric resolution realizes the minimal log discrepancy \(1+a=2/r\); the standard two-dimensional quotient/toric discrepancy criterion shows no further divisorial valuation lowers it. For \(r=2\), the discrepancy is zero and the germ is of type \(A_1\); for \(r>2\), the discrepancy is negative but greater than \(-1\). This proves the asserted klt, canonical, and Gorenstein thresholds.

## Verification
The accompanying standard-library-only `check.py` uses exact rational arithmetic. For each \(4\le n\le11\), it tests all \(n\) coordinate points in the explicit general-position arrangement \(\ell_i=u+i v+i^2w\). It reconstructs each decomposition \(\ell_j=\alpha_j\ell_i+L_j\), checks nonproportionality of the binary forms, computes the product-polynomial coefficient matrix, verifies its nonzero exact determinant, and checks the local Möbius identity at rational sample points. It also checks the formulas for resolution basepoint counts, degree, and canonical index. The recorded output is in `check_output.txt`.

These checks cover \(60\) local charts across eight finite arrangement sizes; they do **not** prove a universal statement, scheme equality, minimality, or literature originality. Those conclusions use the symbolic arguments above. For an independent replay, execute `python3 check.py` from the extracted package directory; no nonstandard modules are required.

## Relationship to prior work
Proudfoot–Speyer's *A Broken Circuit Ring* (first posted October 5, 2004) defines the reciprocal-plane ring, proves the key Gröbner degeneration, and describes the matroid-flat boundary strata. Sanyal–Sturmfels–Vinzant, *The Entropic Discriminant*, Theorem 24 and Corollary 26, go substantially further: for any reciprocal plane they determine its **entire tangent cone** and **reduced singular support**. In particular, the support statement and the Veronese **tangent cone** in the uniform rank-three case are prior results, not claimed as new here. The result proved above shows that the **completed local ring itself**, after an explicit nonlinear Möbius coordinate change, is the Veronese cone; equality of tangent cones alone does not supply such an analytic isomorphism.

Denham–Garrousian–Tohaneanu study graded Orlik–Terao ideals for generic arrangements. Garrousian–Simis–Tohaneanu identify the reciprocal plane as the special fiber of the ideal generated by the omitted-factor products and establish the corresponding Rees/blowup algebra framework; the construction of the graph of the reciprocal rational map is therefore known. More directly, Schenck's *Resonance varieties via blowups of \(\mathbb P^2\) and scrolls*, Theorem 3.4, already shows that this very line-arrangement map is defined on the blowup, contracts each arrangement line to a coordinate point, and maps each point-blowup divisor to a rational normal curve of degree one in the general-position case. Accordingly, the resolution and contracted-curve configuration are used as **prior foundations**, not counted as original. What remains new in the assessed claim is the exact nonlinear coordinate identification of the completed vertex germs and their unified quotient/class-group/canonical-index/minimal-log-discrepancy classification. The known tangent-cone theorem alone does not imply complete local-ring equivalence; the explicit coordinate change proves it.

## Limitations
The arrangement is required to be uniform of rank three, and the theorem is not asserted for dependent triples, higher-dimensional reciprocal varieties, or nonreduced Jacobian schemes. The blowup construction and contraction of arrangement lines, as well as the singular locus and its tangent cones, are established prior work, not original components of this finding. The local analytic classification is independent of the specific general-position moduli only at singular vertices; no classification of global isomorphism classes is claimed. An equivalent specialization under the language of rational maps, star configurations, or surface contractions might exist outside the inspected literature, and the assertion of literature originality is subject to that residual risk. No independent audit or external certification has been performed.

## References
1. N. Proudfoot and D. Speyer, *A Broken Circuit Ring*, arXiv:math/0410069, first version October 5, 2004, sections 3–4, especially Proposition 5. https://arxiv.org/abs/math/0410069
2. R. Sanyal, B. Sturmfels and C. Vinzant, *The Entropic Discriminant*, arXiv:1108.2925, Theorem 24 and Corollary 26 (reciprocal-plane tangent cones and singular support). https://arxiv.org/abs/1108.2925
3. G. Denham, M. Garrousian and Ş. O. Tohaneanu, *Modular decomposition of the Orlik–Terao algebra*, arXiv:1211.4562, section 4.4 (generic arrangement ideals). https://arxiv.org/abs/1211.4562
4. H. Schenck, *Resonance varieties via blowups of \(\mathbb P^2\) and scrolls*, arXiv:1012.0931, Theorem 3.4 and its proof (known blowup model and curve contractions). https://arxiv.org/abs/1012.0931
5. M. Garrousian, A. Simis and Ş. O. Tohaneanu, *A blowup algebra of hyperplane arrangements*, arXiv:1701.03470, Theorem 2.4, Remark 2.5 and Proposition 4.1 (known graph/blowup and special-fiber structure). https://arxiv.org/abs/1701.03470
