# Direction-dependent contact intensities of zeros for Gaussian–first-Hermite spectrograms

## Finding

Let \(\mathcal N\) be centered circular complex white noise on \(\mathbb R\). For \(0\le s\le1\), define the real normalized analysis window
\[
h_0(t)=2^{1/4}e^{-\pi t^2},\qquad h_1(t)=2\sqrt\pi\,t h_0(t),\qquad g_s=\sqrt{1-s}\,h_0+\sqrt{s}\,h_1.
\]
Let \(F_s(x,y)=V_{g_s}\mathcal N(x,y)\), with \(V_g f(x,y)=\langle f,e^{2\pi i y(\cdot)}g(\cdot-x)\rangle\); only its zeros matter, so a smooth nonvanishing gauge factor is immaterial. Write \(\rho_{2,s}(u)\) for the *ordered, unsigned, off-diagonal* second factorial intensity of its simple zeros at separation \(u\in\mathbb R^2\), with respect to Lebesgue area in \((x,y)\). The process is stationary under time-frequency translations. The limiting contact intensities along the two physical coordinate axes exist and are exactly
\[
\boxed{\lim_{r\downarrow0}\rho_{2,s}((r,0))=\frac{2s^3(4+7s-8s^2)}{(1+2s)^2}},
\qquad
\boxed{\lim_{r\downarrow0}\rho_{2,s}((0,r))=\frac{6s^4}{(1-2s+4s^2)^2}}.
\]
These assertions hold at both endpoints, with common value \(0\) at \(s=0\) and common value \(2/3\) at \(s=1\). For every fixed \(s>0\), the limiting pair contribution comes exclusively from *oppositely charged* zeros (a charge being the sign of the nonzero real Jacobian); both like-charge pair contact limits vanish. In the small-admixture limit the two distinct orders are
\[
\lim_{r\downarrow0}\rho_{2,s}((r,0))\sim8s^3,\qquad
\lim_{r\downarrow0}\rho_{2,s}((0,r))\sim6s^4
\quad(s\downarrow0).
\]
Consequently their ratio diverges as \(4/(3s)\). The order of limits is specified: take spatial separation to zero first and *then* send the Hermite power fraction \(s\) to zero. No angularly uniform limit is asserted.

## Assumptions and scope

The white noise is a circular complex isonormal Gaussian generalized function on \(L^2(\mathbb R)\), with covariance \(\mathbb E[\langle\mathcal N,\phi\rangle\overline{\langle\mathcal N,\psi\rangle}]=\langle\phi,\psi\rangle\). The Hermite functions shown above have norm one and are orthogonal. All intensities are population factorial moment densities, not discretely sampled frequencies or empirical zero counts. A point with Jacobian zero is non-simple; the expected zero measures under consideration almost surely have simple, isolated zeros. Derivatives are taken in the physical \((x,y)\) coordinates, with the \(2\pi\) Fourier convention above. The coefficients of \(g_s\) are real nonnegative; a general complex relative phase is not included in the directional claims.

## Proof

**A contact Kac–Rice lemma.** Let \(F\) be a smooth circular complex Gaussian field, with nondegenerate \((F(0),D_uF(0))\) for a unit direction \(u\), and with two-point Kac–Rice valid off the diagonal. Let \(v\) be the \(+90^\circ\) rotation of \(u\). Write \(J(z)=\operatorname{Im}(\overline{F_u(z)}F_v(z))\), the oriented real Jacobian. The conditions \(F(0)=F(ru)=0\) give, in the conditional Gaussian distribution,
\[
F_u(0)=-\tfrac r2F_{uu}(0)+o_{L^2}(r),\qquad
F_u(ru)=\tfrac r2F_{uu}(0)+o_{L^2}(r),\qquad
F_v(ru)=F_v(0)+o_{L^2}(1).
\]
The joint zero-value density is \(r^{-2}p_{F(0),F_u(0)}(0,0)(1+o(1))\). Gaussian moment bounds and regression, followed by dominated convergence in the two-point Kac–Rice expression, therefore imply
\[
\boxed{\lim_{r\downarrow0}\rho_2(ru)=\tfrac14p_{F,F_u}(0,0)\,\mathbb E\!\left[\{\operatorname{Im}(\overline{F_{uu}}F_v)\}^2\mid F=F_u=0\right].}
\tag{1}
\]
All quantities on the right are evaluated at the origin. The signs of \(J(0)\) and \(J(ru)\) are opposite to leading order; whenever the right-hand variable is nonzero almost surely, the like-charge contact limits are zero. The regularity/nondegeneracy hypotheses follow here from smoothness and nonproportionality of distinct time-frequency shifts of the nonzero Schwartz window; if a Gaussian conditional covariance becomes singular at the analytic endpoint \(s=0\), the same formula follows by a limiting regression or the standard Gaussian analytic zero repulsion.

**Gaussian coordinates.** Put \(a=\sqrt{1-s}\), \(b=\sqrt{s}\), and let \(Z_0,Z_1,Z_2,Z_3\) be independent standard circular complex Gaussians in the orthonormal Hermite basis. The Hermite recurrence gives at the origin, in distribution,
\[
\begin{aligned}
F&=aZ_0+bZ_1,\\
F_x&=\sqrt\pi(-bZ_0+aZ_1+\sqrt2bZ_2),\\
F_y&=-i\sqrt\pi(bZ_0+aZ_1+\sqrt2bZ_2),\\
F_{xx}&=\pi(-aZ_0-3bZ_1+\sqrt2aZ_2+\sqrt6bZ_3),\\
F_{yy}&=-\pi(aZ_0+3bZ_1+\sqrt2aZ_2+\sqrt6bZ_3).
\end{aligned}
\tag{2}
\]
Signs in the first derivatives can be simultaneously reversed by a convention for the noise pairing; the squared contact expressions remain unchanged. Set \(U=-bZ_0+aZ_1\), independent of \(F\), so \(F_x=\sqrt\pi(U+\sqrt2bZ_2)\), \(F_y=-i\sqrt\pi(2abF+(1-2s)U+\sqrt2bZ_2)\).

**Time direction.** Write \(D_+=1+2s\). Conditional on \(F=F_x=0\), orthogonal Gaussian projection yields independent standard circular \(R,Z_3\) and
\[
U=-\frac{\sqrt2b}{\sqrt{D_+}}R,\quad Z_2=\frac{R}{\sqrt{D_+}},\quad
F_y=-i\frac{2\sqrt{2\pi}\,sb}{\sqrt{D_+}}R,\quad
F_{xx}=\pi(\sqrt{2D_+}\,aR+\sqrt6bZ_3).
\tag{3}
\]
The complex Gaussian density is \(p_{F,F_x}(0,0)=1/(\pi^3D_+)\). Since \(\mathbb E|R|^4=2\) and \(\mathbb E[\operatorname{Re}(\overline{Z_3}R)^2]=1/2\),
\[
\mathbb E\left[\{\operatorname{Im}(\overline{F_{xx}}F_y)\}^2\mid F=F_x=0\right]
=\frac{8\pi^3s^3(4+7s-8s^2)}{D_+}.
\tag{4}
\]
Insert into (1), with \(u=e_x\), to obtain the first boxed formula.

**Frequency direction.** Put \(q=1-2s\), \(D_-=q^2+2s=1-2s+4s^2\). Choose \(u=e_y\), \(v=-e_x\). Conditional on \(F=F_y=0\), use independent standard circular \(R,Z_3\) and
\[
U=\frac{\sqrt2b}{\sqrt{D_-}}R,\quad Z_2=-\frac q{\sqrt{D_-}}R,\quad
-F_x=-\frac{2\sqrt{2\pi}\,sb}{\sqrt{D_-}}R,\quad
F_{yy}=-\pi\left(\frac{\sqrt2a(4s-1)}{\sqrt{D_-}}R+\sqrt6bZ_3\right).
\tag{5}
\]
Now \(p_{F,F_y}(0,0)=1/(\pi^3D_-)\). Unlike (3), the common \(R\)-parts of \(F_{yy}\) and \(-F_x\) have *real* relative phase and contribute no imaginary product. Therefore
\[
\mathbb E\left[\{\operatorname{Im}(\overline{F_{yy}}(-F_x))\}^2\mid F=F_y=0\right]
=\frac{24\pi^3s^4}{D_-}.
\tag{6}
\]
Equation (1) gives the second boxed formula. For every \(s>0\), the quantities in (4) and (6) are positive, with no atoms at zero for the limiting random variable, proving the charge-pair assertion. Elementary expansion at \(s=0\) and substitution at \(s=1\) give the stated boundary behavior.

## Verification

`CHECK.py` independently reconstructs the five random derivatives in (2) as Hermite-coordinate vectors, performs complex-Gaussian conditioning via a Gram-matrix Schur complement, and uses the circular-Gaussian fourth-moment identity to calculate the right side of (1). It checks both rational contact expressions at nine mixing strengths, including both endpoints, and verifies the cubic/quartic limiting coefficients. It returns `MIXED_HERMITE_DIRECTIONAL_CONTACT_CHECKS_PASSED`. Independent numerical Kac–Rice checks were also performed at small positive separations in the two coordinate directions; they approach the proved contact limits. These finite checks are corroboration, not proof of the limit.

## Relationship to prior work

The general first zero intensity and signed one-point intensity for Schwartz STFT windows were established by Haimi, Koliander, and Romero (2022), especially Theorems 1.9 and 1.12. They do not give the present *unsigned, anisotropic, short-distance two-point* formulas; their explicit charge-pair expressions in Section 5 use radial covariance. Feldheim, Haimi, Koliander, and Romero (first preprint 2024) derive large-region zero/charge variance results for possibly nonradial Gaussian Weyl–Heisenberg fields, rather than this local contact evaluation. Bellourak, Meignen, Polisano, and Nahon (first posted October 9, 2026) calculate zero intensities and pair correlations for *pure* Hermite windows, whose rotation-invariant behavior contrasts with the unequal directional exponents here. Its full text could not be inspected: this creates a remaining priority risk, though the available abstract specifies pure Hermite order \(n\) rather than superpositions.

## Limitations

The exact contact theorem concerns one real two-mode family and the two named axes, with ordered unsigned factorial intensities. It does not determine the entire angular contact profile, the pair correlation at finite separation, any finite-sample estimation error, or the full charge-resolved pair intensities. The zero-separation limit is taken at fixed \(s\); the asymptotic as \(s\downarrow0\) is taken afterward. Existing general Gaussian Kac–Rice theory is a foundation, not a claim of newly invented methodology. Publication priority is not independently certified.

## References

1. A. Haimi, G. Koliander, and J. L. Romero, *Zeros of Gaussian Weyl–Heisenberg Functions and Hyperuniformity of Charge*, Journal of Statistical Physics (2022), https://doi.org/10.1007/s10955-022-02917-3 .
2. N. Feldheim, A. Haimi, G. Koliander, and J. L. Romero, *Hyperuniformity and non-hyperuniformity of zeros of Gaussian Weyl-Heisenberg Functions*, arXiv:2406.20003 (first posted 2024-06-28), https://arxiv.org/abs/2406.20003 .
3. C. Bellourak, S. Meignen, K. Polisano, and M. Nahon, *Zeros of the Spectrogram of White Noise with Hermite Windows*, arXiv:2610.13531 (first posted 2026-10-09), https://arxiv.org/abs/2610.13531 .
