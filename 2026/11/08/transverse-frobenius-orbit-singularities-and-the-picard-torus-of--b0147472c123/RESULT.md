# Transverse Frobenius-orbit singularities and the Picard torus of higher Ballico–Hefez curves

## Finding

Let \(q\ge2\) be any prime power and \(n\ge3\) an integer. Let \(B_n\subset\mathbb P^n_{\mathbb F_q}\) be the reduced image of the symmetric-Frobenius map \(\Phi_n:\mathbb P^1\to\mathbb P^n\) defined below. For each divisor \(d>1\) of \(n\), put
\[
N_d=\frac1d\sum_{e\mid d}\mu(e)q^{d/e}.
\]
Then the singular locus of \(B_n\) consists of precisely \(N_d\) **distinct \(\mathbb F_q\)-rational points of geometric multiplicity \(d\)** for each \(d\mid n\), \(d>1\). All \(d\) branches at such a point are smooth, have **linearly independent tangent directions**, and form a seminormal ordinary \(d\)-fold *space-curve* crossing. In particular the geometric completed local ring at such a point is
\[
\overline{\mathbb F}_q[[u_1,\ldots,u_d]]/(u_i u_j\mid 1\le i<j\le d),
\]
its local normalization defect has dimension \(d-1\), and
\[
p_a(B_n)=\sum_{\substack{d\mid n\\d>1}}(d-1)N_d.
\]
The connected generalized Jacobian is a split product over the distinct singular points of individually nonsplit norm-quotient tori:
\[
\operatorname{Pic}^{0}_{B_n/\mathbb F_q}\ \cong\
\prod_{\substack{d\mid n\\d>1}}
\left(\operatorname{Res}_{\mathbb F_{q^d}/\mathbb F_q}\mathbb G_m/\mathbb G_m\right)^{N_d},
\]
where \(\mathbb G_m\) in each denominator is embedded diagonally. Hence the group is a smooth connected torus of dimension \(p_a(B_n)\), and
\[
\#\operatorname{Pic}^{0}_{B_n}(\mathbb F_q)
=\prod_{\substack{d\mid n\\d>1}}
\left(\frac{q^d-1}{q-1}\right)^{N_d}.
\]
Its closed-point arithmetic also yields, for every integer \(r\ge1\),
\[
\#B_n(\mathbb F_{q^r})=q^r+1+
\sum_{\substack{d\mid n\\d>1}}N_d\bigl(1-d\mathbf1_{d\mid r}\bigr),
\qquad
Z(B_n,T)=\frac{\prod_{\substack{d\mid n\\d>1}}(1-T^d)^{N_d}}
{(1-qT)(1-T)^{1+\sum_{d\mid n,\ d>1}N_d}}.
\]
The extension-point and zeta formulas are explicitly recorded consequences of the already-known normalization-fiber classification; they are **not asserted as independent new discoveries**. The new geometric step is independence of the tangent directions, which establishes the exact local structure needed for the Picard-torus description.

## Assumptions and scope

Work over the finite field \(k=\mathbb F_q\), with \(\operatorname{char}k=p\) arbitrary. The integers \(q\) and \(n\) range over every prime power \(q\ge2\) and every integer \(n\ge3\), including \(p\mid n\). Let \((s:t)\) be coordinates on \(\mathbb P^1\) and set \(D=\sum_{i=0}^{n-1}q^i\). Define the \(n+1\) homogeneous forms of degree \(D\) by the coefficient vector of
\[
\prod_{i=0}^{n-1}(s^{q^i}X+t^{q^i}Y).
\]
Their projective vector is \(\Phi_n([s:t])\). The leading coordinate is \(s^D\), so on \(s=1\), with affine parameter \(a=t/s\), the image is equivalently represented by the coefficients of the monic polynomial
\[
F_a(Z)=\prod_{i=0}^{n-1}(Z-a^{q^i}).
\]
The image is the reduced integral projective curve \(B_n\); its normalization \(\nu=\Phi_n:\mathbb P^1\to B_n\) and its fiber classification are in Fukasawa–Homma–Kim, Theorem 6.4. An ordinary \(d\)-fold *space-curve* crossing here means the union of \(d\) smooth embedded curve germs with independent tangent lines; it is **not** a planar ordinary multiple point when \(d>2\). The inverse image of each singular point is one Frobenius orbit of degree \(d\) on \(\mathbb P^1\), so the singular point itself is \(k\)-rational.

## Proof

**1. Singular fibers.** Fukasawa, Homma and Kim, Theorem 6.4, proves that \(\Phi_n\) is everywhere immersive and is the normalization of \(B_n\). It is one-to-one except at points in \(\mathbb P^1(\mathbb F_{q^n})\setminus\mathbb P^1(\mathbb F_q)\), where its geometric fibers are precisely the complete Frobenius orbits \(\{a,a^q,\ldots,a^{q^{d-1}}\}\) for divisors \(d>1\) of \(n\). Their images are \(k\)-rational. Counting geometric orbits of exact degree \(d\), by finite-field Möbius inversion, gives \(N_d=(1/d)\sum_{e\mid d}\mu(e)q^{d/e}\). The point at infinity is unramified and has a singleton fiber. This settles the locations and counts but not the formal singularity types.

**2. Independence of the branches.** Fix a fiber associated with \(a\in\mathbb F_{q^d}\) of degree exactly \(d\mid n\), and enumerate its distinct elements \(a_j=a^{q^j}\), \(j=0,\ldots,d-1\). Write \(m=n/d\) and \(G(Z)=\prod_{j=0}^{d-1}(Z-a_j)\). Then the common image corresponds to \(G(Z)^m\). Since the derivative of \(a^{q^i}\) vanishes for \(i\ge1\), the tangent vector of the monic-coefficient map at \(a_j\) is the coefficient vector of
\[
\left.\frac{\partial F_t(Z)}{\partial t}\right|_{t=a_j}
=-\prod_{i=1}^{n-1}(Z-a_j^{q^i})
=-G(Z)^{m-1}\frac{G(Z)}{Z-a_j}.
\]
The \(d\) polynomials \(G(Z)/(Z-a_j)\) are linearly independent: evaluating any linear relation at \(Z=a_k\) kills every term but the \(k\)-th, whose value \(G'(a_k)\) is nonzero because \(G\) is separable. Multiplication by the nonzero polynomial \(G^{m-1}\) preserves independence. The monic leading coefficient supplies a common affine chart, so these are also independent projective tangent directions. This argument is characteristic-free, including \(p\mid m\), because the derivative arises from the sole unraised \(t\)-factor and never introduces a factor \(m\).

**3. Formal local form.** At a geometric singular point \(P\), the normalization has exactly \(d\) branches, each formally smooth by the immersion. The branch tangent lines are independent by Step 2, and \(d\le n\). A formal change of ambient regular parameters straightens the \(d\) embedded branches simultaneously to the first \(d\) coordinate axes: inductively choose the \(d\) coordinate restrictions, whose linear parts are independent; all higher corrections are solved in the ambient formal power-series ring. The completed reduced local ring is therefore the coordinate-axis algebra displayed above, not just an equisingular approximation. Its normalization is \(\prod_{j=1}^{d}\bar k[[u_j]]\), with conductor equal to the positive-order terms and quotient \(\bar k^d/\bar k\) of dimension \(d-1\). Consequently its \(\delta\)-invariant is \(d-1\), and, because the normalization is \(\mathbb P^1\) of genus zero, the standard normalization genus formula gives \(p_a(B_n)=\sum(d-1)N_d\). In particular there are no hidden cusp, tacnode, or unipotent singularity contributions.

**4. The arithmetic Picard torus.** The inverse image of each rational singular point of type \(d\) is one closed point of degree \(d\) on \(\mathbb P^1_k\), whose étale residue algebra is \(k_d=\mathbb F_{q^d}\). Step 3 shows that locally the descent of the completed coordinate-axis ring is obtained by gluing the \(d\) conjugate smooth branches only along their common residue constant. Thus the quotient of normalized units by units on the singular curve is the multiplicative quotient
\[
\mathcal Q_P=\operatorname{Res}_{k_d/k}\mathbb G_m/\mathbb G_m.
\]
The normalization exact sequence for units, together with \(\operatorname{Pic}^0(\mathbb P^1_k)=0\), identifies \(\operatorname{Pic}^0(B_n)\) with the product of these local unit-quotient tori. Each quotient is connected and smooth of dimension \(d-1\). Taking \(k\)-points in \(1\to\mathbb G_m\to\operatorname{Res}_{k_d/k}\mathbb G_m\to\mathcal Q_P\to1\), with \(H^1(k,\mathbb G_m)=0\), yields \((q^d-1)/(q-1)\) points. Multiplying over the \(N_d\) singularities proves the group-order formula. This reasoning identifies the algebraic group over \(k\), not only its dimension or its point counts.

**5. Extension counts and zeta.** At extension degree \(r\), a degree-\(d\) normalization fiber contributes \(d\) preimage points if \(d\mid r\) and none otherwise; its image is a single rational point for all \(r\). Relative to \(\#\mathbb P^1(\mathbb F_{q^r})=q^r+1\), its adjustment is \(1-d\mathbf1_{d\mid r}\). Summation gives the stated count. Exponentiating \(\sum_{r\ge1}\#B_n(\mathbb F_{q^r})T^r/r\), and using \(\sum_{r\ge1}d\mathbf1_{d\mid r}T^r/r=-\log(1-T^d)\), gives the zeta function. This last step is a direct deduction from the previously established fiber result and is not a separate basis for the originality assessment.

## Verification

The attached pure-Python script `checks/field_orbits.py` constructs explicit finite fields, enumerates all normalization parameters over \(\mathbb F_{q^n}\), verifies that each Frobenius orbit produces one image, and checks full row rank \(d\) of the \(d\) polynomial tangent vectors using exact finite-field elimination. It tests \((q,n)=(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(4,3),(5,3)\). The cases \(n=2\) are sanity controls and **are not part of the new scope**. A separately written mod-2 homogeneous-coordinate computation in `checks/hilbert_functions.py` verifies Hilbert functions of the projective images for \((q,n)=(2,2),(2,3),(2,4)\), agreeing with the predicted arithmetic genera after stabilization. Logs are in `checks/field_orbits.txt` and `checks/hilbert_functions.txt`. Both checkers use only the standard Python library and terminate with distinct successful verification markers. Finite computations support the formulas but cannot substitute for Steps 1–5, which prove the claims for all \(q,n\).

For examples, \((q,n)=(2,3)\) has two rational ordinary triple-crossings, arithmetic genus \(4\), and generalized Jacobian order \(49\); \((2,4)\) has one rational node and three ordinary quadruple-crossings, genus \(10\), and generalized Jacobian order \(10125\).

## Relationship to prior work

Fukasawa, Homma and Kim (arXiv:1108.4227v1, 22 August 2011), especially Section 6, introduce this \(B_n\), prove normalization, immersion and the Frobenius-orbit fiber classification in Theorem 6.4, and count \(\mathbb F_q\)-points in Theorem 6.6. They do not assert that the tangent lines of different branches are independent, nor identify a higher-\(n\) generalized Jacobian as an arithmetic torus. Their fiber theorem *does* imply the extension-point and zeta formula after routine counting, so those consequences are recorded without a novelty claim.

Hoang–Shimada (arXiv:1402.3372v1, 14 February 2014) analyze automorphisms, defining equations, and covers for the **plane** \(n=2\) Ballico–Hefez curve, not the higher-dimensional branch crossings. The classical plane-curve nodes and their Picard norm-one factors are prior work and are excluded by the hypothesis \(n\ge3\). General normalization and generalized-Jacobian theory supplies the unit-quotient formalism, but the higher-\(n\) transversality established in Step 2 is the geometric input not implied by immersion alone. Searches of closely related published work and mathematical research records did not find an equivalent all-\(n\) local/Picard classification; this absence is not a proof of priority.

## Limitations

The theorem is confined to the specific symmetric-Frobenius embedded rational curves \(B_n\) and does not describe Jacobians of arbitrary Frobenius-nonclassical curves. It does not compute the action of the full projective automorphism group on Picard characters, or the complete homogeneous ideals for all \(q,n\). The verification programs only test finitely many fields and degrees. Historical originality is provisional pending independent literature review, especially specialist theses and work on singular generalized-Jacobian descriptions. No independent mathematical audit or certification has been performed.

## References

1. S. Fukasawa, M. Homma and S. J. Kim, *Rational curves with many rational points over a finite field*, arXiv:1108.4227v1 (22 August 2011), Section 6, Theorems 6.4 and 6.6; https://arxiv.org/pdf/1108.4227.
2. H. T. Hoang and I. Shimada, *On Ballico-Hefez curves and associated supersingular surfaces*, arXiv:1402.3372v1 (14 February 2014), especially Section 1 and Section 2; https://arxiv.org/pdf/1402.3372.
3. Classical normalization exact sequence and Rosenlicht–Serre generalized Jacobian theory (used as standard background rather than claimed as new).
