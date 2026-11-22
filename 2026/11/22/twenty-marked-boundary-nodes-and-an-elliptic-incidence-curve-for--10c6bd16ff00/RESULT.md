# Twenty marked boundary nodes and an elliptic incidence curve for general line–conic Hadamard quartics

## Finding
Let \(L,C\subset\mathbb P^3_{\mathbb C}\) be a general projective line and a general smooth plane conic. Their coordinatewise Hadamard product \(W=L\star C\) is a quartic surface. Its normalization is \(\nu:\mathbb P^1\times\mathbb P^1\to W\). The singular curve is a twisted cubic \(B\), with four ordinary pinch points. Each of the four distinguished coordinate planes meets \(B\) transversely in three ordinary double-curve points, and avoids the four pinch points.

More precisely, the plane section \(W\cap H_i\) consists of one smooth conic and two distinct lines, with exactly five ordinary nodes and no other singularities as a reduced plane curve. Exactly **two** nodes of this plane curve lie on the smooth locus of \(W\); these are ordinary tangencies of \(H_i\) to \(W\). The other **three** nodes lie on \(B\). The twenty nodes across the four coordinate sections are distinct, including **eight smooth-surface tangencies and twelve crossings on the singular curve**.

The ordered pairs of intersecting ruling lines form a smooth elliptic curve \(D\) of bidegree \((2,2)\) in \(\mathbb P^1\times\mathbb P^1\), equipped with its exchange involution. Its quotient is the normalization of \(B\), and the quotient map is a double cover branched at four simple fixed points. There is an explicit determinant equation for \(D\) below.

## Assumptions and scope
Everything is over \(\mathbb C\). "General" means a nonempty Zariski-open subset of the irreducible parameter space of pairs consisting of a line and a smooth plane conic; it is not a claim about special degenerations. Parametrize \(L\) and \(C\) by
\[
  L([s:t])=[a_0s+b_0t:\cdots:a_3s+b_3t],\qquad
  C([u:v])=[q_0(u,v):\cdots:q_3(u,v)],
\]
where the \(q_i\) are binary quadratics spanning a three-dimensional vector space. Require distinct simple zero divisors of the \(q_i\), distinct zeroes of the \(a_is+b_it\), and the generic smoothness/incidence conditions verified below. The map is
\[
  \nu([s:t],[u:v])=[(a_is+b_it)q_i(u,v)]_{i=0}^3,
  \qquad \nu^*\mathcal O_W(1)=\mathcal O(1,2).
\]
In particular \(\nu\) is a morphism with no contracted curves. The term "node" for \(W\cap H_i\) refers to its reduced plane-curve germ, not to the three-dimensional ambient surface germ.

## Proof
**Degree and normalization.** The pulled-back linear series has self-intersection \((1,2)^2=4\). The four sections are linearly independent and have no nonzero quadratic relation for a nonempty open family (the example in Verification has ranks four and ten). Hence the image is neither a plane nor a quadric; the finite map must be birational onto an irreducible degree-four surface. Since the source is normal and \(\nu\) is finite, it is the normalization.

**The elliptic line-incidence correspondence.** Put \(\ell_z=\operatorname{span}(a_iq_i(z),b_iq_i(z))\), the ruling line associated to \(z\in\mathbb P^1\). Two such lines meet precisely when the following four-column determinant vanishes:
\[
 T(z,w)=\det\begin{pmatrix}
 a_0q_0(z)&b_0q_0(z)&a_0q_0(w)&b_0q_0(w)\\
 \vdots&\vdots&\vdots&\vdots\\
 a_3q_3(z)&b_3q_3(z)&a_3q_3(w)&b_3q_3(w)
 \end{pmatrix}.
\]
It is symmetric in \(z,w\), has bidegree \((4,4)\), and vanishes to order at least two on the diagonal. After dividing by the squared diagonal equation, the residual \(\Psi(z,w)=0\) has bidegree \((2,2)\) and is symmetric. The explicit example below has a smooth residual curve, with four distinct transverse intersections with the diagonal. Consequently the same holds for general data, by openness, and \(D=(\Psi=0)\) is a smooth connected genus-one curve by adjunction. The involution \((z,w)\leftrightarrow(w,z)\) has four fixed points; Riemann–Hurwitz gives genus zero for the quotient.

For general data, two different rulings meet transversely at a unique point, with neither generic triple concurrency nor an extra one-dimensional nonimmersion locus. The double-point conductor on the normalization identifies with the ordered incidence curve \(D\): the second ruling parameter is uniquely determined at a generic nonnormal point, and the residual incidence parametrization extends across the four simple diagonal limits. The quotient maps birationally to the reduced double curve \(B\). Since \(W\) is a quartic hypersurface, \(\omega_W\cong\mathcal O_W\), and the conductor adjunction formula gives \(\omega_{\mathbb P^1\times\mathbb P^1}=\nu^*\omega_W(-D)\). Thus its divisor class is \((2,2)\). Since \(D\to B\) has degree two and \(\nu^*H\) has class \((1,2)\),
\[
 \deg B=\tfrac12 D\cdot(1,2)=\tfrac12(2\cdot2+2\cdot1)=3.
\]
A nonplanarity witness is given below; therefore a general irreducible rational cubic \(B\subset\mathbb P^3\) is a twisted cubic. At the four simple diagonal incidence points, the stable local normalization has the ordinary Whitney-pinch model; elsewhere on \(B\) its generic germ has two transverse branches. The classical ruled-quartic classification supplies the same generic local models independently; we use it as background, not a novelty claim.

**Distinguished coordinate sections.** The divisor \(\nu^{-1}(H_i)\) decomposes as
\[
  E_i+F_i^++F_i^-,\qquad
  E_i=\{a_is+b_it=0\}\cong\mathbb P^1,
\]
where \(F_i^\pm\) are the two fibers over the simple zeros of \(q_i\). The restriction of \(\nu\) embeds \(E_i\) as a smooth conic and each \(F_i^\pm\) as a line in \(H_i\cong\mathbb P^2\). On a nonempty open set the conic and lines are distinct, the lines cross away from the conic, and all conic-line intersections are transverse (the explicit rational example verifies these open conditions). Thus the plane quartic has precisely \(2+2+1=5\) nodes.

Two of those nodes are the images of the **same source points** \(E_i\cap F_i^\pm\): locally \(x_i\circ\nu\) is a product of two transverse parameters, and the immersion and single-fiber conditions make \(W\) smooth there and \(H_i\) an ordinary tangent plane. At each of the other two conic-line crossings, and at the crossing of the two lines, the two branches have **distinct source points**. Those three nodes therefore belong to the double curve \(B\). Since \(\deg B=3\), these are the full transverse intersections \(B\cap H_i\), excluding pinch points. The same source-coordinate root-separation conditions keep all five nodes of a given section off the other coordinate planes. Therefore the four sections contribute twenty distinct nodes with the asserted \(8+12\) split.

**Nonemptiness of the open conditions.** Use the explicit line \(L(r)=[r:r+1:r+2:r+4]\) and plane conic
\[
 C(z)=[z^2+z+2:z^2+3z+3:2z^2+3z+1:3z^2+z+4].
\]
The second displayed curve is a nonsingular plane conic (the four quadratics span dimension three, and the parametrization is Veronese after a linear embedding). The diagonal-cancelled determinant, up to a scalar, is
\[
 \Psi(z,w)=17z^2w^2+5z^2w+5zw^2-40zw+5z+5w+27.
\]
Exact Gröbner bases on all four affine charts of \(\mathbb P^1\times\mathbb P^1\) establish that this \((2,2)\) curve is smooth. Its diagonal polynomial is \(17z^4+10z^3-40z^2+10z+27\), with nonzero discriminant. Exact resultant and conic-rank tests certify five transverse nodes for each coordinate-plane section; four explicitly computed pairwise-ruling intersection points span \(\mathbb P^3\), establishing nonplanarity. These tests establish nonempty openness; the geometric arguments, not a finite sample, prove the generic assertions.

## Verification
The standalone `check_example.py` runs in Python 3 with SymPy, performing exact rational polynomial computations. It checks the absence of a plane or quadric relation, separate coordinate roots, the explicit determinant factorization, the Jacobian smoothness criterion in all four incidence charts, four simple diagonal roots, smooth conics and transverse line/conic contacts on every coordinate section, nonplanarity, and the four simple nonimmersion parameters. A successful run prints `PASS`. Mathematical genericity follows because all tested nonvanishing and smoothness conditions are Zariski open in the irreducible family of pairs; testing finitely many points alone would not establish the full theorem.

## Relationship to prior work
Antolini–Ballico–Oneto (arXiv:2502.18813, Section 4, Proposition 4.4 and Corollary 4.5) show that higher-degree line–curve Hadamard surfaces are nonnormal and their coordinate-plane intersections are nontransversal. Their example in Section 4 is a **special cubic** arising from prescribed coordinate incidence; it does not calculate the general line–conic quartic's marked five-node boundary sections or distinguish smooth tangencies from double-curve crossings. Polo-Blanco–van der Put–Top (arXiv:0904.2374, Sections 1 and 3) classify ruled quartics, including twisted-cubic double curves, elliptic conductor correspondences, and pinch points. The general ruled-quartic structure and four-pinch count are classical, not newly claimed in isolation. The additional assertion here is the **Hadamard-coordinate-marked incidence and the exact 20-node/8-versus-12 boundary stratification**, together with the factorization-specific determinant realization of the conductor.

## Limitations
The theorem concerns a general line and a general smooth plane conic, not all quartic Hadamard products, nor the special cubic examples. It does not classify degenerations in which roots coincide, conic-line contacts become tangent, or the ruled surface develops additional singularities. The originality comparison is based on the inspected texts and targeted mathematical-record searches; independently unindexed derivations cannot be excluded. Independent mathematical validation has not been performed.

## References
1. D. Antolini, E. Ballico, A. Oneto, *Algebraic surfaces as Hadamard products of curves*, arXiv:2502.18813, first submitted 26 February 2025; https://arxiv.org/abs/2502.18813 (especially Section 4).
2. I. Polo-Blanco, M. van der Put, J. Top, *Ruled quartic surfaces, models and classification*, arXiv:0904.2374, 2009; *Geometriae Dedicata* 150 (2011), 151–180; https://doi.org/10.1007/s10711-010-9500-0.
