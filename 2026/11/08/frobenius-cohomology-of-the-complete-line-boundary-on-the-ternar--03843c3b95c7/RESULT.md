# Frobenius cohomology of the complete line boundary on the ternary Fermat quartic

## Finding

Let \(k=\mathbb F_3\), let
\[
S=V(X_0^4+X_1^4+X_2^4+X_3^4)\subset\mathbb P^3_k,
\]
and let \(D\subset S\) be the **reduced** union of all geometric projective lines contained in \(S\). Write \(U=S\setminus D\), let \(\nu:\widetilde D\to D\) be the normalization, let \(\Sigma\) be the reduced singular locus of \(D\), and set \(\widetilde\Sigma=(\nu^{-1}\Sigma)_{\mathrm{red}}\). Then:

1. The geometrically connected divisor \(D\) consists of \(112\) lines and has exactly \(280\) singular points, each an ordinary transverse **four-branch** point. Its arithmetic genus is \(p_a(D)=1569\). As schemes over \(k\),
   \[
   \widetilde D\cong\coprod_8\mathbb P^1_k\;\sqcup\;\coprod_{52}\mathbb P^1_{\mathbb F_9},\qquad
   \Sigma\cong\coprod_{16}\operatorname{Spec}k\;\sqcup\;\coprod_{132}\operatorname{Spec}\mathbb F_9,
   \]
   and
   \[
   \widetilde\Sigma\cong\coprod_{32}\operatorname{Spec}k\;\sqcup\;\coprod_{544}\operatorname{Spec}\mathbb F_9.
   \]
2. In the Grothendieck ring \(K_0(\operatorname{Var}_k)\),
   \[
   [D]=8[\mathbb P^1_k]+52[\mathbb P^1_{\mathbb F_9}]-16[\operatorname{Spec}k]-412[\operatorname{Spec}\mathbb F_9].
   \]
3. For every prime \(\ell\ne3\), geometric Frobenius acts on \(H^1(D_{\bar k},\mathbb Q_\ell)\) with eigenvalues \(+1\) of multiplicity \(369\) and \(-1\) of multiplicity \(360\); its dimension is \(729\). Its action on \(H^2(D_{\bar k},\mathbb Q_\ell)\) has eigenvalues \(+3\) of multiplicity \(60\) and \(-3\) of multiplicity \(52\). Consequently,
   \[
   Z(D/k,T)=\frac{(1-T)^{368}(1+T)^{360}}{(1-3T)^{60}(1+3T)^{52}}.
   \]
4. For every integer \(m\ge1\), put \(Q=3^m\). Then
   \[
   \#U(\mathbb F_Q)=
   \begin{cases}(Q-3)^2,&m\text{ odd},\\ (Q-9)(Q-81),&m\text{ even}.
   \end{cases}
   \]
   In particular, \(U(\mathbb F_{3^m})\) is empty **if and only if** \(m\in\{1,2,4\}\). The complete zeta function is
   \[
   Z(U/k,T)=\frac{(1-3T)^{48}(1+3T)^{42}}{(1-T)^{369}(1+T)^{360}(1-9T)}.
   \]

## Assumptions and scope

The equations specify the coefficientwise ternary Fermat quartic, not merely an unspecified geometric isomorphism class. The divisor consists of all \(112\) geometric lines with its reduced subscheme structure. All Frobenius, zeta-function, and finite-field statements are over the displayed \(\mathbb F_3\)-model. The finite fields \(\mathbb F_9\) and \(\mathbb F_{3^m}\) are extensions of this fixed base field. The Grothendieck-ring statement is a scissors identity, not a claim that \(D\) is smooth or a normal-crossings divisor.

## Proof

**Hermitian incidence and completeness of the line boundary.** In characteristic \(3\), the four partial derivatives of the defining quartic are \(X_i^3\), so \(S\) is smooth; it is a K3 surface. Over \(\mathbb F_9\) its equation is the nondegenerate Hermitian form \(h(x,x)=\sum_i x_i x_i^3=0\). The classical Hermitian-surface count gives \(\#S(\mathbb F_9)=(3^3+1)(3^2+1)=280\). The tangent-plane section at each Hermitian rational point is the union of exactly four distinct \(\mathbb F_9\)-rational generators. Every generator has ten \(\mathbb F_9\)-points, hence the number of generators is \(280\cdot4/10=112\). The completeness theorem for the Fermat quartic's lines in characteristic three [1,3] identifies these with **all** geometric lines of \(S\). Any two such lines that meet do so at an \(\mathbb F_9\)-point because the lines themselves are \(\mathbb F_9\)-defined. Every such point lies on exactly four generators. Therefore the entire reduced singular support of \(D\) consists of \(280\) \(\mathbb F_9\)-points. At each one, four distinct ambient projective lines determine four distinct tangent directions in the smooth surface \(S\); the singularity is an ordinary fourfold point. The generalized-quadrangle line incidence graph is connected [3], so \(D\) is geometrically connected.

**Descent of lines and crossings.** At an \(\mathbb F_3\)-rational point the quartic equation is the quadratic equation \(q(x)=\sum_i x_i^2=0\). The quadratic form is split: the linearly independent isotropic vectors \((1,1,1,0)\) and \((1,2,0,1)\) are orthogonal, and the nondegenerate four-dimensional form thus has Witt index two. Its projective quadric is \(Q^+(3,3)\), with \(16\) rational points and two rulings of four \(\mathbb F_3\)-lines each. Each totally isotropic \(\mathbb F_3\)-plane extends to a totally Hermitian-isotropic \(\mathbb F_9\)-plane, so those eight lines lie on \(S\). Conversely, an \(\mathbb F_3\)-defined generator of \(S\) restricts to a totally isotropic plane for \(q\), so these are all eight rational generators. Each of the \(16\) rational points has exactly two rational generators and two further conjugate nonrational generators. Frobenius therefore fixes \(8\) geometric lines and exchanges the other \(104\) in \(52\) pairs. It fixes \(16\) of the \(280\) singular points and exchanges the other \(264\) in \(132\) pairs. Above the \(16\) fixed crossings there are \(32\) fixed branches and \(16\) pairs of branches; above the \(264\) nonfixed crossings there are \(528\) pairs of branches. This proves the three displayed scheme decompositions.

**Arithmetic genus and scissors relation.** Every line on this K3 surface has self-intersection \(-2\) by adjunction. At the \(280\) ordinary fourfold points, each pair of local branches meets once. Hence \(D^2=112(-2)+2\cdot280\binom42=3136\), and adjunction gives \(p_a(D)=1+D^2/2=1569\). The normalization is an isomorphism off \(\Sigma\); cutting the normalization and \(D\) along the finite reduced crossing schemes gives \([D]=[\widetilde D]-[\widetilde\Sigma]+[\Sigma]\), which expands to the stated motivic identity.

**Cohomology of the singular boundary.** For \(\ell\ne3\), the normalization exact sequence for constant \(\mathbb Q_\ell\)-sheaves is
\[
0\to\mathbb Q_{\ell,D}\to\nu_*\mathbb Q_{\ell,\widetilde D}\to\mathcal E\to0,
\]
where \(\mathcal E\) is supported on \(\Sigma\), with stalk the quotient of the permutation representation on the four branches by the diagonal copy of \(\mathbb Q_\ell\). Because every normalized component is a projective line, \(H^1(\widetilde D_{\bar k},\mathbb Q_\ell)=0\). Geometric connectedness gives \(H^0(D_{\bar k})\cong\mathbb Q_\ell\), hence
\[
[H^1(D_{\bar k})]=[H^0(\widetilde\Sigma_{\bar k})]-[H^0(\Sigma_{\bar k})]-[H^0(\widetilde D_{\bar k})]+[\mathbb Q_\ell]
\]
in the Grothendieck group of Frobenius representations. The geometric dimension is \(1120-280-112+1=729\). The Frobenius trace is \(32-16-8+1=9\) in odd powers, and \(1120-280-112+1=729\) in even powers. All these point-and-branch permutations have order dividing two, so the \(H^1\) multiplicities are \((729+9)/2=369\) and \((729-9)/2=360\). Meanwhile \(H^2(D_{\bar k})\) is the direct sum of the Tate-twisted fundamental classes of the \(112\) geometric components, with the claimed \(60\) positive and \(52\) negative Frobenius signs. The cohomological expression for the zeta function yields the displayed \(Z(D/k,T)\).

**The complement.** The standard Hermitian point count gives \(\#S(\mathbb F_9)=280\), while the split-quadric calculation gives \(\#S(\mathbb F_3)=16\). For a smooth quartic K3 surface the second \(\ell\)-adic Betti number is \(22\), its first and third cohomology vanish, and each geometric Frobenius eigenvalue on degree-two cohomology has complex absolute value \(3\). The \(\mathbb F_9\) count implies that the sum of the squares of those \(22\) eigenvalues is \(280-1-9^2=198=22\cdot9\). Equality in the triangle inequality forces **each squared eigenvalue to be \(9\)**. The \(\mathbb F_3\) count then yields eigenvalue multiplicities \(12\) for \(+3\) and \(10\) for \(-3\). Thus, for \(Q=3^m\),
\[
\#S(\mathbb F_Q)=1+Q^2+(12+10(-1)^m)Q.
\]
The motivic identity gives \(\#D(\mathbb F_Q)=8Q-8\) for odd \(m\), and \(\#D(\mathbb F_Q)=112Q-728\) for even \(m\). Subtracting yields the two factorizations for \(U\). In even degree, \(Q\) ranges through \(9,81,729,\ldots\), so both roots \(9,81\) occur; in odd degree, only \(Q=3\) is a root. Finally, the series definition \(Z(U/k,T)=\exp(\sum_{m\ge1}\#U(\mathbb F_{3^m})T^m/m)\) gives the stated rational function.

## Verification

The accompanying `check.py` performs an independent exact exhaustive enumeration over \(\mathbb F_9=\mathbb F_3[\alpha]/(\alpha^2+1)\). It enumerates reduced row-echelon bases of the projective lines in \(\mathbb P^3(\mathbb F_9)\), retains precisely the totally isotropic ones, independently enumerates all projective surface points, and computes the incidences, field-of-definition partition, connectedness, and branch-orbit counts. The observed results are \(112\) generators, \(8\) rational generators, \(280\) Hermitian points, \(16\) rational points, four branches per crossing, and \(30\) line neighbors per generator. The script also checks the symbolic point-count formulas for eight extension degrees and exits with `CHECK_OK`. Its finite enumeration confirms the exact small-field geometry; the proof above, not the finite test, establishes all extension-degree and cohomological assertions.

## Relationship to prior work

The classification of the \(112\) geometric lines and the characteristic-three Fermat quartic is prior work [1,3,4]. The generalized-quadrangle intersection graph, including the geometric stars, is also prior work [3,4]. The Hermitian-surface rational-point count is classical and reviewed in [2]. The new statement concerns the **specified \(\mathbb F_3\)-descent** of its entire reduced line divisor: the normalization and branch Frobenius orbits, its motivic scissors identity, exact \(H^1\) Frobenius representation, and the point-free extension degrees of the open complement. The cited geometric graph and point-count results alone do not identify the Frobenius-fixed and exchanged branches of this arithmetic model; that descent is supplied and checked here. Priority against additional finite-geometry literature is not conclusively established.

## Limitations

The claim concerns this single fixed \(\mathbb F_3\)-model and its reduced complete line boundary; no assertion is made for arbitrary twists, other quartics, or different divisors. The cohomology statement is about \(\mathbb Q_\ell\)-coefficients and the indicated Frobenius action, not integral cohomology. The all-extension identities are mathematical consequences of the proofs, rather than results of exhaustive enumeration over infinitely many fields. The originality assessment is based on the inspected literature and available mathematical-record comparisons, not a proof of unique priority. No independent scientific audit has been performed.

## References

1. S. Rams and M. Schütt, *112 lines on smooth quartic surfaces (characteristic 3)*, arXiv:1409.7485 (first submitted 2014-09-26), especially Example 2.1 and Theorem 1.2. https://arxiv.org/abs/1409.7485
2. M. Homma and S. J. Kim, *The characterization of Hermitian surfaces by the number of points*, arXiv:1304.0302 (first submitted 2013-04-01), formula (3) and Theorem 1.2. https://arxiv.org/abs/1304.0302
3. A. Degtyarev, *Lines in supersingular quartics*, arXiv:1604.05836 (first submitted 2016-04-20), Theorem 1.2 and the generalized-quadrangle description. https://arxiv.org/abs/1604.05836
4. D. C. Veniani, *Lines on K3 quartic surfaces in characteristic 3*, arXiv:1608.04209 (first submitted 2016-08-15), Sections 1 and 4. https://arxiv.org/abs/1608.04209
5. M. Homma and S. J. Kim, *A bound for the number of lines lying on a nonsingular surface in 3-space over a finite field*, arXiv:1409.6421 (first submitted 2014-09-23), Hermitian-surface line count and tangent-section discussion. https://arxiv.org/abs/1409.6421
