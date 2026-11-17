# Sharp third-harmonic susceptibility and optimal speed ratio in weakly elliptical pure pursuit

## Finding

Let the evader traverse \(E_\varepsilon(t)=\cos t+i(1-\varepsilon)\sin t\) in the complex plane and let a pursuer travel in its instantaneous direction with fixed speed ratio \(n\in(0,1)\). For the unique attracting periodic pursuer \(P_{n,\varepsilon}\), define its third *phase-resolved* Fourier coefficient by
\[
\widehat P_3(n,\varepsilon):=\frac1{2\pi}\int_0^{2\pi}P_{n,\varepsilon}(t)e^{-3it}\,dt.
\]
For every fixed \(0<n<1\), with \(r=\sqrt{1-n^2}\),
\[
\boxed{\widehat P_3(n,\varepsilon)=\varepsilon\frac{in(r+in)}{2(3-2in/r)}+O_n(\varepsilon^2).}
\]
Consequently the (strictly positive) third-harmonic susceptibility is
\[
\boxed{S(n):=\lim_{\varepsilon\downarrow0}\frac{|\widehat P_3(n,\varepsilon)|}{\varepsilon}
=\frac{n\sqrt{1-n^2}}{2\sqrt{9-5n^2}}.}
\]
It has a unique global maximizer on \((0,1)\):
\[
\boxed{S(n)\le\frac1{10},\quad S(n)=\frac1{10}\ \Longleftrightarrow\ n=\sqrt{\frac35}.}
\]
Thus weak ellipticity creates a nonzero third phase harmonic at every subunit chase-speed ratio, but its leading amplitude is *nonmonotonic* in that ratio and peaks at the stated algebraic value.

## Assumptions and scope

Positions are identified with complex numbers. The evader starts at \(E_\varepsilon(0)=1\), turns counterclockwise, and has eccentricity *parameter* \(\varepsilon=1-b\) (not the geometric eccentricity). Its major semiaxis is one and minor semiaxis is \(1-\varepsilon\), with \(0\le\varepsilon\ll1\). The pursuer obeys the classical pure-pursuit ODE
\[
P'(t)=n|E_\varepsilon'(t)|\frac{E_\varepsilon(t)-P(t)}{|E_\varepsilon(t)-P(t)|},\qquad P(t)\ne E_\varepsilon(t).
\]
The theorem concerns the unique attracting \(2\pi\)-periodic pursuer trajectory for each fixed \(0<n<1\), guaranteed for elliptical orbits by the established global periodic-orbit theorem in [1]. All asymptotic errors are for \(\varepsilon\to0^+\) at *fixed* \(n\), without uniformity near \(n=0\) or \(n=1\). Fourier modes refer to this canonical evader-anomaly parameter \(t\). They are not invariant under arbitrary nonlinear time reparameterization.

## Proof

**1. Circle and hyperbolicity.** Write \(Z=e^{-it}P\), \(W_\varepsilon=e^{-it}E_\varepsilon\), and \(s_\varepsilon=|E_\varepsilon'|\). Then exactly
\[
Z'=-iZ+ns_\varepsilon\frac{W_\varepsilon-Z}{|W_\varepsilon-Z|},\qquad
W_\varepsilon=1+\frac\varepsilon2(e^{-2it}-1),\quad
s_\varepsilon=\sqrt{\sin^2t+(1-\varepsilon)^2\cos^2t}.
\]
Fix \(0<n<1\), put \(r=\sqrt{1-n^2}\), \(v=r+in\) (so \(|v|=1\)), and \(c=n/r\). At \(\varepsilon=0\), the equilibrium is \(Z_0=n(n-ir)\), whose displacement vector is \(1-Z_0=rv\) with length \(r>0\). The real variational matrix in the moving orthonormal frame \((v,iv)\) is
\[
M=\begin{pmatrix}0&1\\-1&-c\end{pmatrix}.
\]
Its trace is \(-c<0\), determinant is \(1\), and both eigenvalues have strictly negative real part. The monodromy therefore has no eigenvalue equal to one. Since the vector field is smooth where the separation is positive, the implicit-function theorem for the \(2\pi\)-time map provides a unique smoothly parameter-dependent \(2\pi\)-periodic solution near \(Z_0\), remaining uniformly away from capture. The global uniqueness theorem [1] identifies it with the attracting pursuer, and supplies the appropriate global interpretation. For fixed \(n\), smooth dependence gives a uniform \(O_n(\varepsilon^2)\) remainder in the first-order expansion below.

**2. Forced first variation.** As \(\varepsilon\to0\),
\[
W_\varepsilon=1+\varepsilon\frac{e^{-2it}-1}{2},\qquad
s_\varepsilon=1-\frac\varepsilon2(1+\cos2t)+O(\varepsilon^2).
\]
Writing
\[
Z=Z_0+\varepsilon v(\alpha+i\beta)+O_n(\varepsilon^2),
\]
where \(\alpha,\beta\) are real \(2\pi\)-periodic functions, differentiation of \(D\mapsto D/|D|\) at \(D=rv\) yields precisely
\[
\begin{aligned}
\alpha'&=\beta-\frac n2(1+\cos2t),\\
\beta'&=-\alpha-c\beta+\frac{nc}{2}(1-\cos2t)-\frac n2\sin2t.
\end{aligned}
\]
The constant solution part is \((\alpha_0,\beta_0)=(0,n/2)\). For the second harmonic let
\[
\alpha(t)=\Re(Ae^{2it}),\quad\beta(t)=\frac n2+\Re(Be^{2it}).
\]
Matching coefficients gives
\[
2iA=B-\frac n2,\qquad 2iB=-A-cB-\frac{nc}{2}+\frac{in}{2},
\]
and hence
\[
A=\frac{nc+in/2}{3-2ic},\qquad B=2iA+\frac n2.
\]
The denominators do not vanish for real positive \(c\), consistent with uniqueness of the periodic first variation.

**3. Spatial third harmonic.** Restoring \(P=e^{it}Z\), the product of \(e^{it}\) with the positive-frequency component \(\frac12v(A+iB)e^{2it}\) is exactly its third Fourier mode at first order. Therefore
\[
\widehat P_3(n,\varepsilon)=\frac\varepsilon2v(A+iB)+O_n(\varepsilon^2)
=\varepsilon\frac{inv}{2(3-2ic)}+O_n(\varepsilon^2).
\]
Taking the modulus and using \(|v|=1\) proves the displayed \(S(n)\). Positivity follows since \(0<n<1\).

**4. Sharp maximum.** Set \(x=n^2\in(0,1)\). Then
\[
S(n)^2=\frac{x(1-x)}{4(9-5x)},\qquad
\frac{d}{dx}S(\sqrt x)^2=\frac{5x^2-18x+9}{4(9-5x)^2}
=\frac{(5x-3)(x-3)}{4(9-5x)^2}.
\]
The derivative is strictly positive on \((0,3/5)\) and strictly negative on \((3/5,1)\). Since the endpoint limits vanish, the unique global maximum is at \(x=3/5\); substitution gives \(S=1/10\).

## Verification

The standalone `verify.py` reconstructs the \(2\pi\)-periodic solution using a Poincaré shooting equation and high-accuracy ODE integration, extracts the third Fourier coefficient by periodic quadrature, checks the asymptotic coefficient at four distinct speed ratios and two small deformations each, and symbolically verifies the sharp maximizer. It prints `VERIFY_OK` when all checks pass. These finite numerical and symbolic checks corroborate, but are not used in place of, the full proof for all \(n\).

## Relationship to prior work

Yoshihara [1] proves global existence, uniqueness and hyperbolic attraction of the slowly pursuing periodic orbit for arbitrary ellipses, and derives the circular equilibrium; its analysis of global dynamics and Floquet multipliers does not give the Fourier response to weak ellipticity or an optimal speed ratio. Yoshihara's earlier extended paper [2] presents numerical closed curves and a local circular stability calculation, with no such harmonic coefficient. The open-access conference chapter [3] proves that changing the speed parametrization changes no *geometric trajectory*, but does not quantify this canonically phase-parametrized third harmonic. Those facts are used as mathematical context, not republished as new. The new object is the explicit weak-deformation response and its sharp global maximum across speed ratios.

## Limitations

The third Fourier coefficient is measured in the natural anomaly clock \(t\); nonlinear reparameterizations can change it. A nonzero phase third harmonic alone does *not* prove that the unparametrized geometric image is not an ellipse. The leading coefficient is a local small-\(\varepsilon\) result at fixed \(n\); it says nothing about uniform double limits near capture threshold \(n=1\), nor about large ellipse eccentricity. No experimental validation is claimed. Closely related calculations in unindexed historical pursuit literature remain possible.

## References

[1] Sota Yoshihara, *Dynamical Systems in Elliptical Pursuit and Evasion*, arXiv:2605.07217, first posted 2026-05-08. https://arxiv.org/abs/2605.07217

[2] Sota Yoshihara, *Elliptical Pursuit and Evasion — Extended Version*, arXiv:2401.06338, preprint first circulated in 2024. https://arxiv.org/abs/2401.06338

[3] Sota Yoshihara, *Elliptical Pursuit and Evasion*, Proceedings of the 34th IUPAP Conference on Computational Physics, first online 2026-09-28. https://doi.org/10.1007/978-981-92-0844-9_11
