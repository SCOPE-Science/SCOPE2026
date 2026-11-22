# Exact generic singular-curve census and phase-dependent normalization of three-variable Lissajous hypersurfaces

## Finding

Fix positive pairwise coprime integers \(p_1,p_2,p_3\). For \(\lambda\in\mathbb C^\times\), define the smooth two-dimensional torus coset
\[
T_\lambda=\left\{(u_1,u_2,u_3)\in(\mathbb C^\times)^3:\prod_{i=1}^{3}u_i^{p_i}=\lambda\right\}
\]
and the reduced image \(X_\lambda\subset\mathbb A^3\) of
\[
\nu:T_\lambda\longrightarrow\mathbb A^3,\qquad x_i=(u_i+u_i^{-1})/2.
\]
It is an irreducible two-dimensional Lissajous hypersurface associated to a rank-two integer matrix with primitive kernel vector \((p_1,p_2,p_3)\).

**Generic phase.** If \(\lambda^2\ne1\), the finite map \(\nu:T_\lambda\to X_\lambda\) is the normalization. For each index \(j\), introduce two kinds of irreducible curves:

* \(C_{j,[\zeta]}=\nu(T_\lambda\cap\{u_j=\zeta\})\), indexed by the \(p_j-1\) unordered reciprocal pairs \([\zeta]=\{\zeta,\zeta^{-1}\}\) with \(\zeta^{2p_j}=1\) and \(\zeta\ne\pm1\);
* \(D_{j,\eta}=\nu(T_\lambda\cap\{u_j=\eta\})\), indexed by the \(2p_j\) distinct nonzero solutions \(\eta^{p_j}\in\{\lambda,-\lambda\}\).

These curves are all distinct, and
\[
\left(\operatorname{Sing}X_\lambda\right)_{\mathrm{red}}=
\bigcup_{j,[\zeta]} C_{j,[\zeta]}\ \cup\ \bigcup_{j,\eta}D_{j,\eta},\qquad
\boxed{\#\operatorname{Irr}(\operatorname{Sing}X_\lambda)=3(p_1+p_2+p_3)-3}.
\]
Along a general point of every component, the completed analytic germ is a transverse ordinary double surface \(\{st=0\}\times\mathbb A^1\). No assertion is made here about exceptional points where two or more components meet.

**Symmetric phase.** If \(\lambda\in\{1,-1\}\), the inversion \(\iota(u_1,u_2,u_3)=(u_1^{-1},u_2^{-1},u_3^{-1})\) preserves \(T_\lambda\), and the normalization of \(X_\lambda\) is \(T_\lambda/\langle\iota\rangle\). This normal surface has exactly four singularities, all of type \(A_1\). This statement concerns the normalization, not the number or types of all singularities on \(X_\lambda\).

## Assumptions and scope

All schemes are over \(\mathbb C\), with their reduced induced structure. The exponents are positive and pairwise coprime; in particular their greatest common divisor is one. This ensures \(T_\lambda\) is a connected two-torus coset and every slice obtained by holding one \(u_j\) constant is connected. The generic phase condition is exactly \(\lambda\ne\pm1\), not an unspecified Zariski-open restriction. All claims concern affine hypersurfaces, without projective compactification.

## Proof

**1. Finite morphism and normalization.** Let \(B=\mathbb C[u_1^{\pm1},u_2^{\pm1},u_3^{\pm1}]/(\prod u_i^{p_i}-\lambda)\). Pairwise coprimality implies the exponent vector is primitive, so \(B\) is the coordinate ring of a smooth irreducible two-torus. Every \(u_i\) satisfies the monic equation \(u_i^2-2x_iu_i+1=0\), and \(u_i^{-1}=2x_i-u_i\). Hence \(B\) is integral, and finite, over the image coordinate ring \(R=\mathbb C[(u_i+u_i^{-1})/2:1\le i\le3]\subset B\). A point in the fiber over \(x\) differs from a chosen \(u\) only by coordinatewise inversions \(u_i\mapsto u_i^{-1}\).

For a nonempty subset \(S\subseteq\{1,2,3\}\), inversion of exactly the coordinates in \(S\) preserves the torus equation precisely where \(\prod_{i\in S}u_i^{2p_i}=1\). If \(S\) is all three indices, this requires \(\lambda^2=1\). For a proper nonempty subset, the displayed equation cuts out a proper closed subset of \(T_\lambda\) because the corresponding character is nonconstant on \(T_\lambda\). Thus for \(\lambda^2\ne1\), the map is generically one-to-one. As its source is normal and the map is finite and birational, it is the normalization.

If \(\lambda^2=1\), inversion of all coordinates preserves \(T_\lambda\) and is generically free. Every other partial sign inversion is constrained to a proper closed subset, so the generic fiber is exactly a two-point inversion orbit. The finite map factors through the normal affine quotient \(T_\lambda/\langle\iota\rangle\), birationally onto \(X_\lambda\), proving the second normalization statement. Since the exponent vector is primitive, the equation \(\prod u_i^{p_i}=\lambda\) has exactly four solutions with \(u_i=\pm1\); these are precisely the fixed points of inversion. Its differential on the two-dimensional torus at each fixed point is \(-\mathrm{id}\), giving the local invariant ring \(\mathbb C[[s^2,st,t^2]]\cong\mathbb C[[A,B,C]]/(AC-B^2)\). Away from the fixed points, the quotient is smooth. Thus its four singularities are exactly \(A_1\) points.

**2. Generic noninjective fibers.** Assume \(\lambda^2\ne1\). Suppose two distinct preimages have equal \(x\)-coordinates. Their coordinatewise inversion set is a proper nonempty subset \(S\). If \(S=\{j\}\), then \(u_j^{2p_j}=1\) and \(u_j\ne\pm1\). Writing \(u_j=\zeta\), the two source slices \(u_j=\zeta\) and \(u_j=\zeta^{-1}\) project to the same curve: their remaining two coordinates are unchanged, and \(\zeta^{p_j}=\zeta^{-p_j}\). There are \(p_j-1\) reciprocal pairs. If \(S\) consists of the two indices other than \(j\), the product of those two powers is \(\pm1\), equivalently \(u_j^{p_j}=\pm\lambda\). Thus the noninjectivity locus on the image is contained in, and generically equals, the union of the proposed \(C\)- and \(D\)-curves.

**3. Connectedness and distinctness.** A slice \(u_j=\xi\) is a translate of the kernel of the character \((u_k,u_l)\mapsto u_k^{p_k}u_l^{p_l}\) on \((\mathbb C^\times)^2\). Since \(\gcd(p_k,p_l)=1\), each slice is an irreducible one-dimensional torus, so each image is an irreducible curve. Two slices yield the same image only if their fixed coordinate values have the same \(x_j\), hence the parameters are identical or reciprocal. Reciprocal \(C\)-parameters yield the same curve, as above. Reciprocal \(D\)-parameters cannot both solve \(\eta^{p_j}=\pm\lambda\) unless \(\lambda^2=1\). A \(C\)-parameter and a \(D\)-parameter cannot be reciprocal or equal for the same reason. Curves with distinct fixed indices are distinct, because on each slice both other \(x\)-coordinates vary nontrivially. Thus there are exactly \(\sum_j((p_j-1)+2p_j)=3\sum_jp_j-3\) distinct candidate curves.

**4. No omitted singular components or isolated singular points.** In logarithmic tangent coordinates, \(T_\lambda\) has tangent equation \(\sum p_i\,d\log u_i=0\), while \(dx_i=(u_i-u_i^{-1})d\log u_i/2\). Consequently \(d\nu\) has full rank unless at least two coordinates satisfy \(u_i=\pm1\). At any such rank-drop point, if \(j\) denotes the remaining index, then \(u_j^{p_j}=\pm\lambda\), putting its image on a \(D_{j,\eta}\)-curve. If a fiber is a singleton and \(d\nu\) has full rank, the finite analytic map is locally an embedded smooth surface, because all preimages of sufficiently nearby points lie in a neighborhood of the unique preimage; the image is therefore smooth there. Conversely every proposed curve is generically traced by two distinct preimages and hence lies in the singular locus of the image (a smooth variety has a unique point over it under normalization). Taking closures proves the equality of reduced singular loci and excludes further isolated points.

**5. Ordinary transverse double type.** Along a general point of each proposed curve, precisely two preimages occur and none of their coordinates equals \(\pm1\). The two tangent planes have normal covectors proportional to \((p_i/(u_i-u_i^{-1}))_{i=1}^3\). The relevant partial inversion changes the signs of one or two, but not all three, entries. Because all three entries are nonzero, these normals are not proportional. Hence the two smooth local branches meet transversely along a curve; their completed analytic local equation is a unit multiple of \(st=0\).

## Verification

The accompanying `check_example.py` provides an exact symbolic test of the first unequal-exponent case, \((p_1,p_2,p_3)=(1,1,2)\) and \(\lambda=2\). It eliminates one auxiliary Laurent trace to compute a squarefree irreducible defining polynomial of degree eight with coordinate degrees \((4,4,8)\). The common factors of its defining polynomial and all three partial derivatives on the predicted constant-coordinate slices detect exactly the expected \(2+2+5=9\) curves. This finite example checks the formulas but does not establish the general theorem; the proof above establishes arbitrary pairwise coprime positive exponents.

To replay: install Python 3 with SymPy and execute `python check_example.py` from a directory containing the extracted script. The checker performs exact rational/algebraic-number arithmetic, not numerical sampling.

## Relationship to prior work

Mascarin and Telen (2025), Theorems 1.4 and 2.3, establish irreducibility, degree formulas and the Laurent toric parametrization, including the special Cayley and generic sextic examples. Mascarin (2026), Theorem 5.3 and its Section 5, provides general singular-locus inclusions and explicitly analyzes a special-phase surface for exponent vector \((1,3,5)\); its exact hypersurface characterization is stated for at least four ambient coordinates, rather than an arbitrary three-coordinate weighted circuit with generic phase. These sources motivate the present complete, componentwise classification but do not state the sharp \(3\sum p_i-3\) census, the transverse type on all its components, or the phase-dependent normalization theorem. The unweighted \((1,1,1)\) generic-phase surface is a known special case and is not claimed separately. Searches of mathematical result records and the accessible literature did not identify a statement implying the all-exponent classification; this is not a proof that no unindexed equivalent work exists.

## Limitations

The theorem assumes positive pairwise coprime exponents and is not asserted for arbitrary primitive exponent vectors whose pairs share a gcd. The component census concerns only \(\lambda^2\ne1\); the complete singular-locus decomposition of the special-phase image is not determined. Local analytic types at multiple-curve intersections or at the finite ramification points on the double curves are not classified. Neither conductor ideals nor projective-closure singularities are calculated. Independent validation has not been performed.

## References

1. F. M. Mascarin, *Intersections, Equations, and Singularities of Lissajous Varieties*, arXiv:2611.15725v1, first public 2026-11-11, especially Theorems 4.3, 5.3 and Corollary 5.10. https://arxiv.org/abs/2611.15725
2. F. M. Mascarin and S. Telen, *Lissajous Varieties*, arXiv:2509.06844v1, first public 2025-09-08, especially Theorems 1.4, 2.3 and Section 3. https://arxiv.org/html/2509.06844v1
