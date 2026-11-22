# Covariance-invisible coupling and two distinct non-Gaussian switching resonances

## Finding

Consider two overdamped thermal oscillators coupled with a randomly reversing sign. At stationarity their entire **cross-coordinate covariance function** vanishes, although each individual coordinate is strictly non-Gaussian whenever the coupling and switching are both nonzero. The stationary coordinate fourth cumulant is explicitly positive and possesses a unique maximum as the switching rate varies. Normalizing it by the squared stationary variance produces a **different**, strictly larger maximizing switching rate. The two rates separate on different asymptotic scales as the mechanical stability boundary is approached.

With parameters and notation specified below, set \(b=a^2-g^2>0\) and \(\varphi=(1+\sqrt5)/2\). The raw fourth cumulant and the excess kurtosis are, respectively,

\[
\kappa_4(X)=\frac{3D^2g^4q}{a(b+aq)^2(2b+aq)}>0,
\qquad
\mathcal K(X)=\frac{3g^4q}{a(2b+aq)(a+q)^2}>0.
\]

Their respective **unique** maximizers over every \(q>0\) are

\[
q_{\mathrm{raw}}=\frac{b}{a\varphi},\qquad
q_{\mathrm{excess}}=\frac{a}{2}\bigl(\sqrt{r^2+4r}-r\bigr),
\qquad r=\frac{b}{a^2}\in(0,1),
\]

and satisfy \(0<q_{\mathrm{raw}}<q_{\mathrm{excess}}\). The maximal raw cumulant is \(3D^2g^4/(a^2b^2\varphi^5)\). In the near-instability regime \(r\downarrow0\),

\[
q_{\mathrm{raw}}/a=r/\varphi,\quad
q_{\mathrm{excess}}/a\sim\sqrt r,\quad
q_{\mathrm{excess}}/q_{\mathrm{raw}}\sim\varphi/\sqrt r.
\]

These are statements about the stationary *position marginal* and two-time *cross-position* correlations, not a claim that all auto-correlations or all fourth-order joint observations vanish.

## Assumptions and scope

Let \(a,D,q,g\) be real with \(a>g>0\), \(D>0\), \(q>0\). On a two-sided stationary probability space let \(\sigma_t\in\{-1,1\}\) be the symmetric continuous-time Markov chain which flips \(+1\leftrightarrow-1\) with intensity \(q\) in each direction. It is independent of two independent standard Brownian motions. Define the Itô dynamics

\[
\begin{aligned}
dX_t&=(-aX_t+g\sigma_tY_t)\,dt+\sqrt{2D}\,dW^x_t,\\
dY_t&=(-aY_t+g\sigma_tX_t)\,dt+\sqrt{2D}\,dW^y_t.
\end{aligned}
\]

The drift matrix has eigenvalues \(-a\pm g\) at both switch signs, so its symmetric part is uniformly negative definite. The process therefore has a unique stationary joint law (including the telegraph sign) with finite moments of every order. All expectations below refer to this law. Define \(m_2=\mathbb E[X_t^2]\), \(\kappa_4(X)=\mathbb E[X_t^4]-3m_2^2\), and \(\mathcal K(X)=\kappa_4(X)/m_2^2\). Exchange symmetry gives identical statements for \(Y\).

## Proof

**Zero cross-correlations.** The joint stationary dynamics is invariant in law under the involution \((X,Y,\sigma)\mapsto(X,-Y,-\sigma)\), accompanied by changing the sign of the second Brownian motion. Since the stationary law is unique, for all real times \(t,s\), the joint law of \((X_t,Y_s)\) is invariant under \((x,y)\mapsto(x,-y)\). Hence \(\mathbb E[X_tY_s]=0\), and \(\mathbb E[X_t]=\mathbb E[Y_s]=0\). This proves zero cross-coordinate covariance at every lag, not just zero equal-time covariance.

**Second moments.** Set \(m=\mathbb E[X^2]=\mathbb E[Y^2]\) and \(p=\mathbb E[\sigma XY]\). The stationary Markov generator applied to \(X^2\) and \(\sigma XY\) gives

\[
0=-2am+2gp+2D,\qquad
0=-2(a+q)p+2gm.
\]

Consequently \(m=D(a+q)/(a^2+aq-g^2)\) and \(p=gm/(a+q)\), with \(m>0\).

**Fourth moments.** Denote \(A=\mathbb E[X^4]\), \(B=\mathbb E[\sigma X^3Y]\), and \(C=\mathbb E[X^2Y^2]\). Symmetry under exchange of the two coordinates makes the polynomial stationary moment equations close:

\[
\begin{aligned}
0&=-4aA+4gB+12Dm,\\
0&=-(4a+2q)B+g(A+3C)+6Dp,\\
0&=-4aC+4gB+4Dm.
\end{aligned}
\]

Here \(-2qB\) is precisely the telegraph-flip generator term. Solving this nonsingular linear system, inserting the second-moment formula, and simplifying yields

\[
A-3m^2=\frac{3D^2g^4q}{a(a^2+aq-g^2)^2(2a^2+aq-2g^2)}.
\]

Every denominator factor is positive under the hypotheses, establishing strict non-Gaussianity. Division by \(m^2\) gives the displayed excess-kurtosis identity. In particular both cumulant measures tend to zero as \(q\downarrow0\) and as \(q\to\infty\).

**The two unique resonances.** Let \(b=a^2-g^2\) and \(x=aq/b>0\). Apart from a strictly positive factor independent of \(q\), the raw fourth cumulant has the profile \(f(x)=x/[(1+x)^2(2+x)]\), whose derivative equals

\[
f'(x)=\frac{2(1-x-x^2)}{(1+x)^3(2+x)^2}.
\]

The sole positive root is \(x=1/\varphi\), with the derivative strictly positive before and strictly negative afterward. Direct substitution yields \(q_{\mathrm{raw}}\) and its maximum.

For excess kurtosis, write \(r=b/a^2\in(0,1)\) and \(t=q/a\). Its rate profile is \(h(t)=t/[(2r+t)(1+t)^2]\). The sign of \(h'(t)\) is that of \(r-rt-t^2\), which has exactly one positive root \(t_{\mathrm{excess}}=(\sqrt{r^2+4r}-r)/2\). The defining quadratic \(t^2+rt-r\) evaluated at \(t_{\mathrm{raw}}=r/\varphi\) equals \(r(r-1)<0\), proving the strict ordering of the two positive peaks. Their respective near-instability expansions follow directly from these exact formulas.

## Verification

The reproducible file `check.py` independently solves the untransformed stationary moment generator equations by exact fractional Gaussian elimination for a grid of rational parameters, and checks the algebraic cumulant formulas and stationarity residuals. It additionally verifies the derivative identities, unique-root defining equations, peak order at deterministic parameter samples, and limiting behaviors. The executed checker reported **2,668 successful exact-rational, symbolic, and deterministic numerical assertions**. This finite exercise is not the proof of an all-parameter result; the proof is the stationary generator algebra and one-variable sign analyses above.

## Relationship to prior work

Kryuchkov, Mantsevich, and Yurchenko (2022) study spectra of harmonic oscillators with randomly fluctuating coupling and establish mode mixing without cross-correlations. This motivates the present question, but the already known disappearance of cross-correlations is not claimed as new. The new assessed statements concern the explicit positive stationary *coordinate fourth cumulant*, its unique switching-rate maximum, the distinct normalized-kurtosis maximum, and their singular separation near the stability edge in the explicitly defined overdamped symmetric telegraph model.

Cerasoli and collaborators (2022) analyze spectral fingerprints of a two-dimensional **constant-coupling**, two-temperature Brownian gyrator, rather than multiplicatively sign-switched coupling. Sarkar, Santra, and Basu (2022) analyze harmonic chains with **additive** colored active forcing, including telegraph boundary driving, rather than the present sign-switched intercoordinate drift. Both provide relevant contrasts between stationary second- and higher-order observations.

A complete version of the closest fluctuating-coupling article could not be examined; its publisher abstract and bibliographic metadata were examined, so implicit prior coverage of the fourth-order formulas remains an explicit publication-priority uncertainty. No uniqueness-of-discovery claim is made.

## Limitations

All statements require identical local damping and thermal diffusivity, independent Brownian driving, symmetric Markov sign flips, and strict mechanical stability \(a>g>0\). They do not cover unequal damping, non-Markov switching, inertial response, or nonthermal noise. There is no claim that the diagonal auto-covariances are independent of switching. The switching-rate maxima optimize two particular stationary fourth-order statistics, not entropy production, mode-mixing spectra, or all non-Gaussianity metrics. Scientific originality is assessed against available material; independent validation and a complete inspection of the inaccessible closest paper are outstanding.

## References

1. N. P. Kryuchkov, V. N. Mantsevich, S. O. Yurchenko, “Interacting Oscillators with Fluctuating Coupling: Mode Mixing without Cross-Correlations,” *Physical Review Letters* **129**, 034102 (2022), https://doi.org/10.1103/PhysRevLett.129.034102 (publisher public date 2022-07-11; abstract available).
2. S. Cerasoli et al., “Spectral fingerprints of nonequilibrium dynamics: The case of a Brownian gyrator,” *Physical Review E* **106**, 014137 (2022), https://doi.org/10.1103/PhysRevE.106.014137; full lawful author PDF: https://www.peliti.org/Publications/Phys_Rev_E_Gyrator_Spectra.pdf.
3. R. Sarkar, I. Santra, U. Basu, “Stationary states of activity-driven harmonic chains,” arXiv:2210.09035 (2022), https://arxiv.org/abs/2210.09035 (full preprint inspected).
