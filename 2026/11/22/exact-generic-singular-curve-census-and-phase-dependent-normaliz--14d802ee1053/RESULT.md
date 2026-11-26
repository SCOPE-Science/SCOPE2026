# Exact generic singular-curve census and phase-dependent normalization of three-variable Lissajous hypersurfaces

## Finding

Fix positive pairwise coprime integers \(p_1,p_2,p_3\). For \(\lambda\in\mathbb C^\times\), let
\[
T_\lambda=\{u\in(\mathbb C^\times)^3:\prod_{i=1}^3u_i^{p_i}=\lambda\},
\qquad \nu(u)_i=(u_i+u_i^{-1})/2,
\]
and let \(X_\lambda\subset\mathbb A^3\) be the reduced image. It is an irreducible two-dimensional Lissajous hypersurface associated to a rank-two integer matrix with primitive kernel vector \((p_1,p_2,p_3)\).

If \(\lambda^2\ne1\), the finite map \(\nu:T_\lambda\to X_\lambda\) is the normalization. Its image has the following distinct irreducible singular curves:

* \(C_{j,[\zeta]}=\nu(T_\lambda\cap\{u_j=\zeta\})\), indexed for each \(j\) by the \(p_j-1\) unordered reciprocal pairs \([\zeta]=\{\zeta,\zeta^{-1}\}\) with \(\zeta^{2p_j}=1\) and \(\zeta\ne\pm1\);
* \(D_{j,\eta}=\nu(T_\lambda\cap\{u_j=\eta\})\), indexed for each \(j\) by the \(2p_j\) solutions \(\eta^{p_j}\in\{\lambda,-\lambda\}\).

Their union is the entire reduced singular locus. Its number of irreducible components is \(3(p_1+p_2+p_3)-3\). At a general point of each curve the completed local ring is \(\mathbb C[[s,t,w]]/(st)\).

If \(\lambda=\pm1\), the normalization is instead the quotient of \(T_\lambda\) by simultaneous inversion in all three coordinates. The quotient has exactly four singularities, all of type \(A_1\). This does not classify all singularities of \(X_\lambda\) at these phases.

## Assumptions and scope

All schemes are over \(\mathbb C\), and images and loci in the statement are reduced. Positivity and pairwise coprimality ensure that the torus coset and its constant-coordinate slices are connected. The condition \(\lambda^2\ne1\) applies as stated, including \(\lambda^2=-1\). Only affine hypersurfaces are considered.

## Proof

**1. Finite morphism and normalization.** The exponent vector is primitive, so \(T_\lambda\) is a smooth irreducible torus translate of dimension two. Each \(u_i\) satisfies the monic equation \(u_i^2-2x_iu_i+1=0\) with \(u_i^{-1}=2x_i-u_i\). Thus the torus coordinate ring is finite over the image ring, which is a domain of dimension two. A primitive exponent vector extends to an integral basis, yielding a Laurent parametrization by two torus coordinates with the stated kernel. Since a fiber of the trace map consists of coordinatewise inversions, inverting exactly the coordinates of a nonempty set \(S\) gives another point of \(T_\lambda\) if and only if \(\prod_{i\in S}u_i^{2p_i}=1\). For a proper \(S\) the corresponding character is nonconstant on \(T_\lambda\), so the condition is proper. For the full set it is precisely \(\lambda^2=1\). When \(\lambda^2\ne1\) the map is therefore generically one-to-one, hence birational in characteristic zero. The finite birational map from the smooth source is the normalization.

For \(\lambda=\pm1\) the generic fiber is exactly one simultaneous-inversion orbit of size two. The map therefore factors through the finite normal affine quotient, which is birational to the image. The inversion has four fixed points: these are the sign triples satisfying \(\prod_i u_i^{p_i}=\lambda\), and at least one exponent is odd. Local logarithmic coordinates at a fixed point turn the action into multiplication by \(-1\) on a two-dimensional plane. Its completed invariant ring is \(\mathbb C[[a,b,c]]/(ac-b^2)\). Away from the fixed points the action is free and the quotient is smooth.

**2. Noninjective fibers for \(\lambda^2\ne1\).** Any two distinct preimages differ by a proper nonempty inversion set. Inverting only \(j\) requires \(u_j^{2p_j}=1\), and gives a distinct point only if \(u_j\ne\pm1\). Reciprocal parameters give the same \(C\)-curve because this inversion identifies the two slices over the image. Inverting the two coordinates other than \(j\) requires that the product of their powers be \(\pm1\), or \(u_j^{p_j}=\pm\lambda\). This yields exactly the candidates \(D_{j,\eta}\). Generically on each candidate slice the indicated inversion gives a distinct point in the fiber.

**3. Connectedness and distinctness.** In a slice \(u_j=\xi\), the two remaining coordinates, denoted \(u_k,u_l\), satisfy \(u_k^{p_k}u_l^{p_l}=\lambda/\xi^{p_j}\). Coprimality makes this a one-dimensional torus translate on which each of \(u_k,u_l\), hence also each of \(x_k,x_l\), varies nontrivially. Its finite image is a closed irreducible curve. Different fixed indices give different curves. For a common index \(j\), a coincidence of images would require the fixed parameters to agree or be reciprocal, since their trace coordinates must agree. For \(C\)-curves reciprocal parameters were already identified, and \(C\)- and \(D\)-parameters cannot agree or be reciprocal because their \(p_j\)-th powers belong to disjoint sets \(\{1,-1\}\) and \(\{\lambda,-\lambda\}\). Two distinct reciprocal \(D\)-parameters can occur when \(\lambda^2=-1\); in this case their \(p_j\)-th powers have opposite signs. The two slices have opposite values of \(\varepsilon=\lambda/\xi^{p_j}\in\{1,-1\}\). Let \(T_a(x)\) be the Chebyshev polynomial defined by \(T_a((v+v^{-1})/2)=(v^a+v^{-a})/2\). Taking traces of \(u_k^{p_k}u_l^{p_l}=\varepsilon\) gives \(T_{p_k}(x_k)=\varepsilon T_{p_l}(x_l)\). These two opposite-sign identities cannot hold on the same curve because \(T_{p_l}(x_l)\) is nonconstant. Hence the reciprocal \(D\)-slices still have distinct images. The number of distinct curves is \(\sum_j((p_j-1)+2p_j)\).

**4. Exhaustiveness.** On the logarithmic tangent plane \(\sum_i p_i\,d\log u_i=0\), the differential is \(dx_i=(u_i-u_i^{-1})d\log u_i/2\). Its rank can drop only if at least two coordinates are \(\pm1\), because a tangent vector in its kernel must vanish off these coordinates. At such a point the remaining \(u_j\) satisfies \(u_j^{p_j}=\pm\lambda\), so the image is on a \(D\)-curve. If the fiber is a singleton and the rank is two, the local analytic map is an embedding, and finiteness ensures that no branch from outside a neighborhood of the single preimage approaches the point. The image is then smooth. Conversely, the general points of the candidate curves have at least two preimages and cannot be smooth, by the normalization property. The singular locus is closed, proving the equality with the union.

**5. Generic local type.** Away from the intersections of the distinct curves and from the finite subset of each slice where a varying coordinate equals \(\pm1\), every point on each curve has exactly the two preimages given by its defining inversion. Its fixed coordinate is not \(\pm1\) by the parameter conditions. Both branches are smooth immersions, with tangent normals proportional to \((p_i/(u_i-u_i^{-1}))_{i=1}^3\) at each preimage. The defining inversion changes the signs of one or two entries, so the normals are independent. Finiteness excludes other branches. Two smooth hypersurface branches with independent normals have local coordinates with equations \(s=0\) and \(t=0\); the reduced completed image therefore has equation \(st=0\).

## Verification

The companion `check_example.py` is an exact SymPy slice check for \((p_1,p_2,p_3)=(1,1,2)\) and \(\lambda=2\). It checks the expected \(2+2+5=9\) candidate curves using the defining polynomial and its partial derivatives; this example is not a proof of the general census. For a direct check at the phase where reciprocal \(D\)-parameters coincide in the fixed trace coordinate, take \((p_1,p_2,p_3)=(1,1,1)\), \(\lambda=i\). For any fixed \(j\), the slices \(u_j=i,-i\) both have \(x_j=0\) but impose \(u_l=u_k^{-1},-u_k^{-1}\), respectively. Their images are the distinct lines \(x_l=x_k\) and \(x_l=-x_k\) in that plane.

## Relationship to prior work

Mascarin and Telen establish irreducibility, degree formulas and the Laurent toric parametrization, including the special Cayley and generic sextic examples. Mascarin's Theorem 5.3 gives general singular-locus inclusions; its Corollary 5.10 gives an equality for coloop-free hypersurfaces with at least four ambient coordinates. Example 1.2 analyzes the special-phase surface for exponent vector \((1,3,5)\). Two related records treat the unweighted triangle: one gives six lines and classifies crossings and pinch points for \(c=(\lambda+\lambda^{-1})/2\notin\{0,\pm1\}\), and the other gives six lines, the conductor and local types for \(c=0\). These specialize the generic-phase census here and give local information not claimed here. The contribution considered here is the full three-coordinate weighted census with generic transverse type and the phase-dependent normalization. Historical priority outside the inspected literature is not established.

## Limitations

No census is given for pairs of exponents with a common divisor, or for the singular locus of the special-phase image. The local types at multiple-curve intersections and finite ramification points, conductor ideals and projective closures are not addressed.

## References

1. F. M. Mascarin, *Intersections, Equations, and Singularities of Lissajous Varieties*, arXiv:2611.15725v1, especially Theorems 4.3, 5.3 and Corollary 5.10. https://arxiv.org/abs/2611.15725
2. F. M. Mascarin and S. Telen, *Lissajous Varieties*, arXiv:2509.06844v1, especially Theorems 1.4, 2.3 and Section 3. https://arxiv.org/html/2509.06844v1
3. *Four triple crossings and twelve pinch points on generic triangle Lissajous sextics*, mathematical result record `c7d4b55603be` (2026-11-22).
4. *The conductor and twelve pinch points of the triangle Lissajous sextic*, mathematical result record `3c3fa534e9d7` (2026-11-22).
