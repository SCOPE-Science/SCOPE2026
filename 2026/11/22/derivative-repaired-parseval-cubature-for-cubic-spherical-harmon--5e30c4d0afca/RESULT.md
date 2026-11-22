# Derivative-repaired Parseval cubature for cubic spherical harmonics

## Finding

Let \(X\subset S^2\) be a finite, nonempty set with positive real weights \(w_x\) satisfying \(\sum_{x\in X}w_x=1\). Let \(\mathcal H_3\) be the seven-dimensional complex space of spherical harmonics of **exact degree three**, and use probability surface area \(d\sigma\) to define its \(L^2\) inner product. Define the sampled Hermitian form

\[
B_X(f,g)=\sum_{x\in X}w_x\left[\frac37 f(x)\overline{g(x)}+\frac1{21}\nabla_S f(x)\cdot\overline{\nabla_Sg(x)}\right].
\]

**Exact characterization.** The identity \(B_X(f,g)=\int_{S^2}f\overline g\,d\sigma\) holds for **every** \(f,g\in\mathcal H_3\) if and only if \(X\) integrates exactly all degree-two and degree-four spherical harmonics:

\[
\sum_{x\in X}w_xY(x)=0\quad\text{for every }Y\in\mathcal H_2\oplus\mathcal H_4.
\]

Equivalently, the antipodally symmetrized weighted node measure \(\tfrac12\sum_xw_x(\delta_x+\delta_{-x})\) is a weighted spherical five-design. Thus the point-and-gradient analysis map, with the displayed weights, is a **Parseval frame** even when value sampling alone is singular.

**Canonical sharp realization.** For the twelve unit vertices \(X_{\mathrm{ico}}\) of a regular icosahedron with equal weights, let \(S_0\) be the value-sampling Gram operator and \(S_1\) the tangential-gradient Gram operator divided by the spherical Dirichlet eigenvalue twelve:

\[
\langle S_0f,g\rangle=\frac1{12}\sum_{x\in X_{\mathrm{ico}}}f(x)\overline{g(x)},\qquad
\langle S_1f,g\rangle=\frac1{144}\sum_{x\in X_{\mathrm{ico}}}\nabla_Sf(x)\cdot\overline{\nabla_Sg(x)}.
\]

Their full spectra, with multiplicities, are

\[
\operatorname{spec}(S_0)=\{(7/3)^{[3]},0^{[4]}\},\qquad
\operatorname{spec}(S_1)=\{(7/4)^{[4]},0^{[3]}\}.
\]

Their nonzero spaces are orthogonal complements and

\[
\boxed{\frac37S_0+\frac47S_1=I_{\mathcal H_3}.}
\]

Moreover, \(\alpha S_0+(1-\alpha)S_1=I\) for real \(\alpha\) holds **only** at \(\alpha=3/7\).

## Assumptions and scope

The sphere is the unit two-sphere in real three-space. The Laplace–Beltrami operator is nonpositive: \(\Delta_SY=-k(k+1)Y\) on \(\mathcal H_k\). The gradients are intrinsic tangential vector fields and their products are the complex-bilinear Euclidean metric with conjugation in the second factor. All cubature integrals use probability surface area. The weighted characterization requires normalized positive weights; its algebraic proof also works for normalized real signed weights, but no positive-frame interpretation is asserted for signed rules. The theorem is exclusively about a single exact harmonic degree, not all degrees through three.

## Proof

**1. A degree-lowering differential identity.** For \(f,g\in\mathcal H_3\), write \(h=f\overline g\). The pointwise product rule and \(\Delta_Sf=-12f\) give

\[
\Delta_Sh=2\nabla_Sf\cdot\overline{\nabla_Sg}-24h.
\]

Consequently the mixed observation integrand is

\[
\frac37h+\frac1{21}\nabla_Sf\cdot\overline{\nabla_Sg}
=h+\frac1{42}\Delta_Sh.
\]

Because both factors have odd antipodal parity, \(h\) has an orthogonal harmonic expansion in degrees \(0,2,4,6\) only. On degree six, \(I+\Delta_S/42\) vanishes. Hence \(q=h+\Delta_Sh/42\) belongs to \(\mathcal H_0\oplus\mathcal H_2\oplus\mathcal H_4\), and \(\int q\,d\sigma=\int h\,d\sigma\). If all second- and fourth-degree harmonics have vanishing weighted node averages, then the node average of \(q\), hence \(B_X(f,g)\), equals the integral of \(h\). This proves sufficiency without any numerical computation or positivity assumption.

**2. Necessity.** Fix any unit vector \(u\in S^2\) and take \(f(x)=g(x)=P_3(u\cdot x)\), with \(P_k\) the Legendre polynomial normalized by \(P_k(1)=1\). Direct Legendre multiplication and the spherical zonal Laplacian give the exact identity

\[
P_3(t)^2+\frac1{42}\left((1-t^2)\frac{d}{dt}P_3(t)^2\right)'
=\frac17+\frac8{49}P_2(t)+\frac6{49}P_4(t).
\]

If the proposed cubature is exact for every cubic pair, applying it to these zonal squares implies

\[
8\sum_{x\in X}w_xP_2(u\cdot x)+6\sum_{x\in X}w_xP_4(u\cdot x)=0
\quad\text{for every }u\in S^2.
\]

As functions of \(u\), the two sums lie respectively in the mutually orthogonal spaces \(\mathcal H_2\) and \(\mathcal H_4\); they must vanish separately. By the addition formula, the rotated zonal harmonics span each \(\mathcal H_k\), so all weighted harmonic moments of degrees two and four vanish. The antipodal symmetrization automatically kills all odd-degree moments, including degrees one, three, and five, establishing the claimed weighted five-design equivalence. This proves necessity.

**3. Icosahedral exactness and the two complementary blind spaces.** Let \(\varphi=(1+\sqrt5)/2\) and normalize the twelve vectors

\[
(0,\pm1,\pm\varphi),\quad(\pm1,\pm\varphi,0),\quad(\pm\varphi,0,\pm1)
\]

by \(\sqrt{\varphi+2}\). They are six antipodal pairs. For any selected six unit representatives \(a_1,\ldots,a_6\), elementary dot products show \(a_i\cdot a_j\in\{\pm1/\sqrt5\}\) for distinct indices, and \(\sum_{i=1}^6a_ia_i^{\mathsf T}=2I_3\). Each vertex has one antipode and ten other vertices, all at inner products \(\pm1/\sqrt5\). The even Legendre polynomials satisfy \(P_2(1/\sqrt5)=P_4(1/\sqrt5)=-1/5\). Thus each double harmonic moment sum of degree two or four is \(2+10(-1/5)=0\); the addition formula makes all individual degree-two/four moments zero. Antipodality settles the odd degrees, so this set is a weighted five-design.

For the normalized \(L^2\) reproducing kernel \(K_3(a,b)=7P_3(a\cdot b)\), the six-axis value Gram matrix before the factor \(7/6\) is \(C=(P_3(a_i\cdot a_j))\). Since \(P_3(\pm1/\sqrt5)=\mp1/\sqrt5\), including diagonal entries gives

\[
C=2I_6-A^{\mathsf T}A,\qquad A=[a_1\ \cdots\ a_6],\qquad AA^{\mathsf T}=2I_3.
\]

The nonzero eigenvalues of \(A^{\mathsf T}A\) are all two (multiplicity three). Hence \(C\) has three eigenvalues two and three zero. The sample operator on \(\mathcal H_3\), dimension seven, has the nonzero eigenvalues of \((7/6)C\), namely \(7/3\) three times, and four zero eigenvalues. The already established mixed Parseval identity gives \(S_1=7I/4-3S_0/4\), which yields \(0\) three times and \(7/4\) four times. Orthogonality and uniqueness of \(\alpha=3/7\) follow immediately by equating the two eigenspace coefficients.

## Verification

The accompanying `verify.py` is a standalone SymPy checker. It constructs a seven-element explicit basis of homogeneous harmonic cubics, computes its exact normalized spherical \(L^2\) Gram matrix using factorial/Pochhammer moments, and evaluates both value and tangent-gradient sample matrices on all twelve algebraic icosahedral vertices. It checks all 49 entries of the mixed Parseval identity, the degree-two/four zonal polynomial identity, and exact projector equations and traces yielding every spectral multiplicity. Execute `python verify.py` with SymPy installed. Its successful output is reproduced in `VERIFICATION.md`. The analytic proof above, not the test program, establishes the universal statement.

## Relationship to prior work

Xiao and Zhuang's *Spherical framelets from spherical designs* (initial arXiv release March 9, 2023) develops numerical spherical designs and tight multiscale framelets through scalar harmonic transforms and value cubature. It motivates exact stable sampling on designs but does not state the present mixed **field-value plus intrinsic field-gradient** Parseval form or the equivalence with even moment exactness. In particular, its gradient and Hessian of a design objective refer to **node-position derivatives**, not samples of the gradients of the reconstructed harmonics.

Allasia, Cavoretto and De Rossi consider Hermite–Birkhoff interpolation on the sphere using derivative information and cardinal radial bases. That construction does not state the present exact cubic eigenspace Gram form, its if-and-only-if moment characterization, or the optimal icosahedral mixture. Hitchin's earlier *Spherical harmonics and the icosahedron*, Proposition 1, establishes the previously known **four-dimensional nullspace of cubic point evaluations** on icosahedral vertices. That fact is fully credited here. The new focus is the general mixed-gradient Parseval characterization and its complementary gradient interpretation. Earlier work evaluating an icosahedral **cap-mixture** concentration spectrum can imply parts of the isolated vertex-spectral example through limiting arguments; it does not cover the arbitrary weighted node-set equivalence. No global uniqueness or historical priority certification is claimed.

## Limitations

The converse is proved only for exact degree three on the two-sphere; this document does not claim a characterization of mixed cubature at arbitrary harmonic degree or higher dimension. The frame is exact only when the stated weighted even moments vanish. Derivative samples must be intrinsic tangent gradients with the explicit Dirichlet normalization; unnormalized ambient gradients have different matrices. The sharp coefficient is unique for the icosahedron, not asserted to be unique for every weighted node set. The full historical literature may contain an equivalent observation not indexed in the consulted records; mathematical novelty has not been independently validated.

## References

- Y. Xiao and X. Zhuang, *Spherical framelets from spherical designs*, arXiv:2303.05365 (first public March 9, 2023), subsequently SIAM J. Imaging Sciences 16 (2023), 2072–2104, DOI: 10.1137/22M1542362. https://arxiv.org/abs/2303.05365
- N. Hitchin, *Spherical harmonics and the icosahedron*, arXiv:0706.0088 (2007), especially Proposition 1. https://arxiv.org/abs/0706.0088
- G. Allasia, R. Cavoretto and A. De Rossi, *Hermite-Birkhoff interpolation on scattered data on the sphere and other manifolds*, arXiv:1705.01032 (2017). https://arxiv.org/abs/1705.01032
- Delsarte, Goethals and Seidel, *Spherical codes and designs*, Geom. Dedicata 6 (1977), 363–388. https://doi.org/10.1007/BF03187604
