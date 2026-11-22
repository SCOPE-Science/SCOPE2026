# Sharp negative-set volume and radial rigidity in the first positive Fourier–Hermite shell

## Finding

Normalize the Euclidean Fourier transform on \(\mathbb R^d\) by
\[
\widehat f(\xi)=\int_{\mathbb R^d} f(x)e^{-2\pi i x\cdot\xi}\,dx.
\]
For each integer \(d\ge2\), let \(\mathcal H_d\) consist of real, even, nonzero functions \(f(x)=P(x)e^{-\pi |x|^2}\), where \(P\) is a real polynomial of total degree at most four, \(\widehat f=f\), and \(f(0)=0\). Write \(v_d=\pi^{d/2}/\Gamma(1+d/2)\).

**Theorem.** Every \(f\in\mathcal H_d\) satisfies
\[
\left|\{x\in\mathbb R^d:f(x)\le0\}\right|
\ge v_d\left(\frac{d+2}{2\pi}\right)^{d/2}.
\]
The bound is attained. Equality holds exactly for the positive multiples of
\[
 f_*(x)=|x|^2\left(|x|^2-\frac{d+2}{2\pi}\right)e^{-\pi|x|^2}.
\]
Hence the unique minimizing ray is radial, although radiality is not imposed on the competitors. Every nonradial competitor has strictly greater negative-set volume, possibly infinite.

The theorem has a quantitative counterpart. Each \(f\in\mathcal H_d\) has a unique homogeneous quartic \(Q\) such that
\[
 f(x)=\left(Q(x)-\frac{\Delta Q(x)}{8\pi}\right)e^{-\pi|x|^2}.
\]
If \(A(\omega)=Q(\omega)>0\) everywhere on \(S^{d-1}\), then
\[
\boxed{\quad
|\{f\le0\}|\ge v_d\left(\frac{d+2}{2\pi}
+\frac1{8\pi}\fint_{S^{d-1}} |\nabla_S\log A|^2\,d\sigma
\right)^{d/2}.\quad}
\]
The right side strictly exceeds the optimal radial volume whenever \(A\) is nonconstant. The area-average \(\fint\) uses ordinary surface measure divided by \(|S^{d-1}|\).

In dimension two, for \(-1<\varepsilon<1\), choose the positive quartic \(Q(r,\theta)=r^4(1+\varepsilon\cos(4\theta))\). Its negative-set area is exactly
\[
|\{f\le0\}|=\frac{2}{\sqrt{1-\varepsilon^2}},
\]
exhibiting a continuous nonradial family with strict volume excess for nonzero \(\varepsilon\).

## Assumptions and scope

The volume is Lebesgue measure of the closed nonpositive set; the same measure is obtained using \(f<0\), because a nonzero polynomial times a Gaussian has a zero set of Lebesgue measure zero. Fourier self-duality \(\widehat f=f\) is pointwise (equivalently in \(L^2\)) under the displayed normalization. No radiality, positivity, or nonnegative leading quartic is assumed. Finite negative-set volume forces the leading quartic to be nonnegative on the unit sphere. The theorem optimizes **only within** this finite-degree Fourier-invariant shell, not among all Fourier eigenfunctions.

## Proof

**1. The Fourier–Hermite shell.** For a homogeneous real quartic \(Q\) and a homogeneous real quadratic \(R\), the Gaussian differentiation identity gives
\[
\begin{aligned}
\mathcal F(Qe^{-\pi|x|^2})&=
\left(Q-\frac{\Delta Q}{4\pi}+\frac{\Delta^2Q}{32\pi^2}\right)e^{-\pi|\xi|^2},\\
\mathcal F(Re^{-\pi|x|^2})&=
\left(-R+\frac{\Delta R}{4\pi}\right)e^{-\pi|\xi|^2}.
\end{aligned}
\]
Decompose the even polynomial as \(P=Q+R+c\). The requirement \(f(0)=0\) gives \(c=0\). Comparing homogeneous quadratic coefficients in \(\widehat f=f\) gives \(2R=-\Delta Q/(4\pi)\), hence \(R=-\Delta Q/(8\pi)\). The constant coefficients then agree automatically. The quartic \(Q\) is uniquely determined, and it is nonzero: otherwise the quadratic comparison forces \(R=0\), contradicting \(f\ne0\).

**2. Finite volume and polar geometry.** Put \(A(\omega)=Q(\omega)\). For \(x=r\omega\), the polar Laplacian identity for a homogeneous degree-four function yields
\[
Q(r\omega)=r^4A(\omega),\qquad
\Delta Q(r\omega)=r^2\bigl(4(d+2)A(\omega)+\Delta_S A(\omega)\bigr).
\]
If \(A<0\) at some sphere point, then by continuity \(A<0\) on a nonempty spherical open patch. The quartic term makes \(f(r\omega)<0\) at all sufficiently large radii in a subpatch, giving infinite negative-set volume. It therefore suffices to consider \(A\ge0\). First suppose \(A>0\). Let
\[
R_0^2=\frac{d+2}{2\pi},\qquad
u(\omega)=R_0^2+\frac{\Delta_S A(\omega)}{8\pi A(\omega)}.
\]
The nonpositive set along each ray (up to its zero-measure endpoints) is \(0<r^2\le \nu(\omega)_+\), where \(s_+=\max\{s,0\}\). Consequently the **exact polar formula** is
\[
|\{f\le0\}|=\frac1d\int_{S^{d-1}}\bigl(\nu(\omega)_+\bigr)^{d/2}\,d\sigma(\omega).
\]

**3. Sharp Jensen and rigidity.** For \(d\ge2\) the function \(s\mapsto(s_+)^{d/2}\) is convex. Jensen's inequality and the sphere identity \(|S^{d-1}|=dv_d\) give
\[
|\{f\le0\}|\ge v_d\left(\max\left\{0,\fint_S\nu\,d\sigma\right\}\right)^{d/2}.
\]
Integration by parts on the closed sphere yields the nonnegative exact identity
\[
\fint_S\frac{\Delta_S A}{A}\,d\sigma
=\fint_S\frac{|\nabla_S A|^2}{A^2}\,d\sigma
=\fint_S|\nabla_S\log A|^2\,d\sigma\ge0.
\]
Therefore \(\fint_S\nu\ge R_0^2>0\). This proves the quantitative bound and shows strictness if \(A\) is nonconstant. If \(A=c>0\), then \(Q(x)=c|x|^4\), the nonpositive set is the ball of radius \(R_0\), and equality holds.

**4. Quartics with spherical zeros.** Suppose \(A\ge0\) but \(A\) vanishes somewhere. For each \(\varepsilon>0\), put \(Q_\varepsilon(x)=Q(x)+\varepsilon|x|^4\) and define its self-Fourier companion \(f_\varepsilon\) using step 1. Then \(A_\varepsilon=A+\varepsilon>0\) and
\[
f_\varepsilon(r\omega)-f(r\omega)
=\varepsilon e^{-\pi r^2}r^2(r^2-R_0^2).
\]
For \(0<r<R_0\), the negative-set indicators converge pointwise almost everywhere and are bounded on a finite-volume ball, so dominated convergence applies. For \(r>R_0\), as \(\varepsilon\downarrow0\) they increase to the indicator of \(f<0\) at all points with \(f\ne0\), so monotone convergence applies, even when the total volume is infinite. Thus \(|\{f_\varepsilon<0\}|\to|\{f<0\}|\). Since each \(f_\varepsilon\) has volume at least \(v_dR_0^d\), the same is true of \(f\).

Moreover, any nonconstant \(A\ge0\) is nonconstant on some open patch where \(A>0\). On a smaller compact patch \(|\nabla_S A|\) is bounded below and \(A\) is bounded above; hence \(\fint |\nabla_S\log(A+\varepsilon)|^2\) has a uniform strictly positive lower bound for small \(\varepsilon\). Applying step 3 to \(f_\varepsilon\) and passing to the limit proves strict excess also in the presence of spherical zeros. A constant nonnegative nonzero \(A\) must be positive, completing the equality classification.

**5. Explicit anisotropic example.** In \(d=2\), \(r^4\cos(4\theta)\) is harmonic and \(\Delta r^4=16r^2\), so the quartic \(Q=r^4(1+\varepsilon\cos4\theta)\) yields \(f=e^{-\pi r^2}r^2[r^2(1+\varepsilon\cos4\theta)-2/\pi]\). For \(|\varepsilon|<1\), polar integration gives
\[
\frac12\int_0^{2\pi}\frac{2/\pi}{1+\varepsilon\cos(4\theta)}\,d\theta
=\frac2{\sqrt{1-\varepsilon^2}}.
\]

## Verification

The standalone, standard-library script `artifacts/verify_quartic.py` checks the Fourier coefficient identities exactly over sample quartics and dimensions, the radial Laplacian identity, and numerical polar integration against the closed anisotropic formula. It reports 1,999 passed assertions. These finite checks are supplementary; steps 1–5 are the proof for every integer \(d\ge2\).

## Relationship to prior work

Edwin's 2026 *Fourier inequalities and sign uncertainty II* formulates a **definite-set** sign-uncertainty minimization for real even Fourier eigenfunctions vanishing at the origin, explicitly observing that radialization is not automatic. The present theorem solves the restricted first nontrivial positive-eigenvalue Gaussian–Hermite shell, including nonradial competitors, and proves quantitative radial rigidity there; it does **not** solve the unrestricted problem. Cohn, Dong and Gonçalves studied low-degree **radial polynomial Gaussian** sign-uncertainty radii, a different objective with the radial hypothesis built in. Earlier work on Gaussian–Hermite extremal rays in the cone of nonnegative positive-definite functions addresses positivity and extremality under product and convolution, not the Lebesgue volume of a negative set. No equivalence or stronger theorem directly implying the displayed sharp volume and rigidity has been identified in the inspected sources.

## Limitations

The claim is limited to real even self-Fourier polynomial Gaussians of total polynomial degree at most four and \(d\ge2\). It does not calculate the unrestricted definite-set uncertainty constant, establish uniqueness for non-Gaussian functions, or handle the negative Fourier eigenvalue. The quantitative formula requires strictly positive spherical leading quartic; the qualitative sharp lower bound and uniqueness do not. Earlier equivalent integral rearrangement arguments or unpublished low-degree results remain possible bibliographic risks. The work has not undergone independent mathematical audit.

## References

1. R. Edwin, *Fourier inequalities and sign uncertainty II*, arXiv:2611.08224 (first public version 2026-11-05), https://arxiv.org/abs/2611.08224 , especially Problem 1.6 and the discussion of radialization.
2. H. Cohn, D. Dong and F. Gonçalves, *Sign uncertainty principles and low-degree polynomials*, arXiv:2210.01684 (2022), https://arxiv.org/abs/2210.01684 ; Proceedings of the American Mathematical Society, Series B (2024), DOI https://doi.org/10.1090/bproc/219 .
3. F. Gonçalves, D. Oliveira e Silva and J. P. G. Ramos, *On regularity and mass concentration phenomena for the sign uncertainty principle*, arXiv:2003.10765 (2020), https://arxiv.org/abs/2003.10765 .
