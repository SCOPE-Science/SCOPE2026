# A positive logarithmic Douglas jump family beyond superharmonic disk weights

## Finding
Let \(dm(\theta)=d\theta/(2\pi)\) be Haar probability on the circle, \(P_t(\theta)=(1-t^2)/(1-2t\cos\theta+t^2)\), and
\[
w_c(z)=(1-|z|^2)\left[1+c\log\frac1{1-|z|^2}\right],\qquad c\ge0.
\]
For a trigonometric polynomial \(f\) and its harmonic Poisson extension \(u=P[f]\), set
\[
\mathcal E_c(f)=\frac1\pi\int_{\mathbb D}\left(|\partial_z u|^2+|\partial_{\bar z}u|^2\right)w_c(z)\,dx\,dy.
\]
Then its exact Fourier symbol is \(\psi_c(0)=0\) and
\[
\psi_c(n)=\frac{|n|}{|n|+1}\left[1+c(H_{|n|+1}-1)\right],\quad n\in\mathbb Z\setminus\{0\},
\]
where \(H_m=\sum_{k=1}^m1/k\). For every \(c\ge0\), the following density is **strictly positive** and strictly decreasing on \((0,\pi)\):
\[
j_c(\theta)=\int_0^1P_t(\theta)\left[1+c\left(\frac{t}{1-t}-\log(1-t)-1\right)\right]dt,
\quad0<|\theta|\le\pi.
\]
It gives the positive Douglas formula
\[
\boxed{\ \mathcal E_c(f)=\frac12\int_{\mathbb T}\!\int_{\mathbb T}|f(e^{ix})-f(e^{iy})|^2j_c(x-y)\,dm(x)\,dm(y).\ }
\]
The same identity holds with values in \([0,\infty]\) for every \(f\in L^2(\mathbb T)\), interpreting both sides by their closed Fourier forms. The total jump intensity is exactly one at \(c=0\) and infinite for every \(c>0\). For \(c>0\),
\[
j_c(\theta)=\frac{c\pi}{|\theta|}+O_c\!\left(1+\log^2\frac1{|\theta|}\right),\quad\theta\to0,
\]
so \(\int_{\varepsilon<|\theta|\le\pi}j_c(\theta)dm(\theta)=c\log(1/\varepsilon)+O_c(1)\). Furthermore, \(\Delta w_c(0)=4(c-1)>0\) for \(c>1\): **the whole positive jump family continues beyond superharmonic weights**.

## Assumptions and scope
All logarithms are natural; \(\mathbb D=\{|z|<1\}\), and \(\mathbb T=\mathbb R/2\pi\mathbb Z\). Parameter \(c\) ranges over all finite nonnegative real numbers. Fourier coefficients use normalized Haar measure, and the spatial energy uses \(dx\,dy/\pi\) rather than an unnormalized area or gradient norm. The jump density is a function of the angular difference; its value at \(\theta=0\) is irrelevant. For \(c>0\), the measure is infinite near the diagonal, but its integral against squared trigonometric increments is finite. The intensity is the mass of \(j_c\,dm\) in the difference coordinate, **not** the mass of the symmetrized pair measure, which has an extra factor \(1/2\).

## Proof
**1. Spectral computation.** The harmonic modes \(e^{in\theta}\) extend to \(z^n\) for \(n>0\) and \(\bar z^{|n|}\) for \(n<0\). Orthogonality in polar coordinates gives, for \(n\ge1\),
\[
\psi_c(n)=n^2\int_0^1t^{n-1}(1-t)[1-c\log(1-t)]dt
=\frac{n}{n+1}[1+c(H_{n+1}-1)].
\]
The second equality is the beta integral and its derivative with respect to the second parameter. This also verifies the precise area/complex-derivative normalization.

**2. A signed Poisson mixture with a positive result.** Put
\[
v(t)=\frac{t}{1-t}-\log(1-t)-1.
\]
Elementary integration, using \((1-t^n)t/(1-t)=\sum_{k=1}^{n}t^k\) and \(\int_0^1t^n[-\log(1-t)]dt=H_{n+1}/(n+1)\), yields
\[
\int_0^1(1-t^n)v(t)dt=\frac{n}{n+1}(H_{n+1}-1).
\]
Also \(\int_0^1(1-t^n)dt=n/(n+1)\). The circle Poisson kernel has \(n\)-th Fourier coefficient \(t^{|n|}\), whence
\[
\int_{\mathbb T}(1-\cos n\theta)j_c(\theta)dm(\theta)=\psi_c(n).
\]
The integrals are legitimate: \((1-t^n)v(t)\) is integrable, while the fixed nonzero-angle Poisson integral defining \(j_c\) is absolutely convergent. The positive representation follows from step 3 and Parseval, first for polynomials and then by monotone Fourier-series convergence for the closed form domain.

**3. Strict positivity despite a changing-sign mixture.** The function \(v\) is strictly increasing on \((0,1)\), with \(v(0)=-1\) and \(v(t)\to+\infty\); it has a unique root \(t_0\in(0,1)\). Write \(J_v(\theta)=\int_0^1P_t(\theta)v(t)dt\). Direct integration at the antipodal angle gives
\[
J_v(\pi)=1-3\log2+2\operatorname{Li}_2(1/2)>0.
\]
Here \(\operatorname{Li}_2(x)=\sum_{k\ge1}x^k/k^2\) for \(0\le x<1\). Positivity is elementary from \(\log2<7/10\) and \(\operatorname{Li}_2(1/2)>1/2+1/16+1/72\). For \(0<\theta_1<\theta_2\le\pi\), the ratio
\[
R(t)=\frac{P_t(\theta_1)}{P_t(\theta_2)}
=\frac{1-2t\cos\theta_2+t^2}{1-2t\cos\theta_1+t^2}
\]
is strictly increasing since
\[
R'(t)=\frac{2(\cos\theta_1-\cos\theta_2)(1-t^2)}{(1-2t\cos\theta_1+t^2)^2}>0.
\]
Because \(v\) changes sign once, \([R(t)-R(t_0)]v(t)\ge0\), strictly on sets of positive measure. Hence
\[
J_v(\theta_1)>R(t_0)J_v(\theta_2)>J_v(\theta_2)>0
\]
by comparison with \(\theta_2=\pi\). The component \(J_0(\theta)=\int_0^1P_t(\theta)dt\) is also strictly positive and strictly decreasing. Thus \(j_c=J_0+cJ_v\) is strictly positive and strictly decreasing for every \(c\ge0\), even though its Poisson mixing density may be negative.

**4. Sharp activity transition.** Since \(\int_{\mathbb T}P_t(\theta)dm(\theta)=1\), Tonelli gives \(\int j_0dm=\int_0^1dt=1\). As \(v(t)\sim1/(1-t)\) and \(j_c\ge0\), the difference quotient or the short-angle asymptotics below shows infinite mass for \(c>0\). Write \(s=1-t\) and \(\delta=|\theta|\). For \(s\ll1\),
\[
P_{1-s}(\theta)=\frac{2s-s^2}{s^2+2(1-s)(1-\cos\theta)},\qquad
v(1-s)=\frac1s-2-\log s.
\]
Consequently the leading singularity of \(J_v\) is the elementary integral \(\int_0^1 2/(s^2+\delta^2)\,ds=\pi/\delta+O(1)\). For \(0<s<1/2\) and small \(\delta\), the denominator is comparable to \(s^2+\delta^2\). More precisely, the difference between \(P_{1-s}(\delta)/s\) and \(2/(s^2+\delta^2)\) is bounded by a constant times \(s/(s^2+\delta^2)+(s\delta^2+\delta^4)/(s^2+\delta^2)^2\). Its integral is \(O(1+\log(1/\delta))\). The remaining factor \(-2-\log s\) has integral bounded by \(O(1+\log^2(1/\delta))\); the \(s\ge1/2\) tail is bounded. The \(J_0\) component has only logarithmic growth. Integration with \(dm=d\theta/(2\pi)\) proves the truncated-mass formula. Finally, \(w_c(z)=1+(c-1)|z|^2+O_c(|z|^4)\), so \(\Delta w_c(0)=4(c-1)\) and superharmonicity fails for \(c>1\).

## Verification
The standalone `CHECK.py` uses exact rational harmonic-number identities, independent high-precision beta/Poisson integrals, strict angular ordering checks for both mixture components, and a near-diagonal singularity consistency check. It is a finite diagnostic and is **not** a proof of universal positivity or the limiting asymptotic. All such claims are established by the preceding analytic steps. Reproduce using `python CHECK.py` with Python 3 and `mpmath` installed. The exact symbolic portion uses only Python's standard library.

## Relationship to prior work
Bourabiaa, Elmadani, Hanine, Jamal and Labghail (2026) develop the general class of Douglas weights, their jump Dirichlet forms and processes, and explicitly ask which weights admit positive boundary forms and how to compute their jump kernels (Section 5, Problems 1 and 4). Their general framework is **not** itself an explicit certification of the logarithmically enhanced weight above. Bahajji-El Idrissi, El-Fallah, Elmadani and Hanine (2026) study **superharmonic** weights; that theory does not cover \(c>1\). An existing radial-power example has a positive jump representation at the critical exponent \(1\), but it neither implies positivity of the signed logarithmic derivative nor establishes the finite-to-infinite jump transition when the derivative is added with arbitrarily large coefficient. The new substance is the single-crossing positivity argument for every \(c\ge0\), including the nonsuperharmonic range, and the sharp Lévy-activity law.

## Limitations
This is an explicit one-parameter radial family, not a characterization of arbitrary Douglas weights. The boundary form is established for harmonic Poisson extensions with normalized area and complex derivatives; other energy conventions require rescaling. No uniqueness of arbitrary non-translation-invariant jump representations is asserted. No closed formula for the full semigroup or for general boundary capacities is obtained. Potential equivalent results under Bernstein-function or Lévy-symbol terminology remain a literature risk.

## References
1. J. Bourabiaa, Y. Elmadani, A. Hanine, A. Jamal, I. Labghail, *Douglas Weighted Dirichlet Spaces: Analytic and Probabilistic Aspects*, arXiv:2607.26870, first public 2026-07-29; especially Definition 2.1 and Section 5 Problems 1 and 4. https://arxiv.org/abs/2607.26870
2. H. Bahajji-El Idrissi, O. El-Fallah, Y. Elmadani, A. Hanine, *Superharmonically Weighted Dirichlet Spaces*, arXiv:2605.13787, first public 2026-05-13. https://arxiv.org/abs/2605.13787
3. G. Bao, N. G. Göğüş, S. Pouliasis, *On Dirichlet Spaces With a Class of Superharmonic Weights*, Canadian Journal of Mathematics **70** (2018), 721–741. https://doi.org/10.4153/CJM-2017-005-1
