# Directional Kullback–Leibler projection has a sharp two-versus-many Poisson phase transition

## Finding
Let \(m\ge2\) be an integer and \(0<r<1\). The normalized circle Poisson density is
\[
P_{r,\phi}(\theta)=\frac{1-r^2}{1-2r\cos(\theta-\phi)+r^2},\qquad
\int_0^{2\pi}P_{r,\phi}(\theta)\,\frac{d\theta}{2\pi}=1.
\]
Define an equal-weight, equally spaced source mixture
\[
Q_{m,r}(\theta)=\frac1m\sum_{j=0}^{m-1}P_{r,2\pi j/m}(\theta).
\]
For a candidate \(P_{t,\phi}\), \(0\le t<1\), and \(\phi\in\mathbb R/(2\pi\mathbb Z)\), define \(D(U\Vert V)=\int U\log(U/V)\,d\theta/(2\pi)\). The **two orientations of projection have different exact minimizer sets**:

1. For every \(m\ge2\) and \(0<r<1\), the unique density minimizing \(D(Q_{m,r}\Vert P_{t,\phi})\) is the uniform density \(P_{0,\phi}=1\). The parameter \(\phi\) is immaterial when \(t=0\).
2. For \(m=2\), the unique optimal density minimizing \(D(P_{t,\phi}\Vert Q_{2,r})\) is uniform when \(r\le1/\sqrt2\). For \(r>1/\sqrt2\), exactly two distinct optimizers occur, at \(\phi\in\{0,\pi\}\) and radius
\[
t_*(r)=\sqrt{2-r^{-2}}.
\]
The optimal radius emerges continuously at the threshold.
3. For each \(m\ge3\), let
\[
q_c(m)=\frac{(m-1)^{m-1}}{m^{m/2}(m-2)^{(m-2)/2}},\quad
r_c(m)=q_c(m)^{1/m},\quad
t_c(m)=\frac{\sqrt{m(m-2)}}{m-1}.
\]
Then \(0<r_c(m)<1\). The reverse projection is uniquely uniform for \(r<r_c(m)\); exactly \(m+1\) densities (the uniform one and the \(m\) mode-aligned ones with radius \(t_c(m)\)) minimize it at \(r=r_c(m)\); and for \(r>r_c(m)\), exactly \(m\) optimizers occur, at phases \(2\pi j/m\), \(j=0,\ldots,m-1\), and at the unique radius \(t_*(r)\in(t_c(m),1)\) satisfying
\[
r^m t_*^{m-2}\big[m-(m-1)t_*^2\big]=1.
\]
Thus \(m=2\) has a continuous onset, whereas every \(m\ge3\) has a discontinuous jump. The many-component threshold satisfies
\[
r_c(m)=1-\frac1{2m^2}+O(m^{-3}),\qquad
 t_c(m)=1-\frac1{2(m-1)^2}+O(m^{-4}).
\]
The critical radii include \(r_c(3)=(4/(3\sqrt3))^{1/3}\) and \(r_c(4)=(27/32)^{1/4}\).

## Assumptions and scope
All densities are strictly positive and normalized relative to \(d\theta/(2\pi)\). The candidate family includes the uniform density at radius zero and all Poisson radii strictly below one; only equal-weight regular \(m\)-gons of a common source radius are considered. Both directions use the same fixed source mixture \(Q_{m,r}\), and their arguments in \(D(U\Vert V)\) are specified explicitly. Angles are understood modulo \(2\pi\), and distinct optimal densities, not redundant parameterizations at \(t=0\), are counted.

## Proof
**Fourier and Poisson reduction.** The normalized Poisson density has Fourier series
\[
P_{r,\phi}(\theta)=\sum_{k\in\mathbb Z}r^{|k|}e^{ik(\theta-\phi)}.
\]
Averaging over the regular \(m\)-gon kills every nonmultiple-of-\(m\) frequency, giving the exact identity
\[
Q_{m,r}(\theta)=P_{r^m,0}(m\theta).
\]
For \(0\le t<1\), the absolutely convergent Fourier series of \(\log|1-te^{i\theta}|\), or its harmonic mean-value property, yields
\[
\int P_{t,\phi}(\theta)\log Q_{m,r}(\theta)\,\frac{d\theta}{2\pi}
=\log(1-q^2)-2\log|1-qt^m e^{im\phi}|,
\quad q=r^m.
\]
Also \(\int P_{t,\phi}\log P_{t,\phi}\,d\theta/(2\pi)=-\log(1-t^2)\). Hence
\[
D(P_{t,\phi}\Vert Q_{m,r})=-\log(1-t^2)-\log(1-q^2)+2\log|1-qt^m e^{im\phi}|. \tag{1}
\]
For positive \(t\), the last modulus is uniquely minimized at phases \(\phi=2\pi j/m\). After subtracting the radius-independent constant \(-\log(1-q^2)\), minimizing (1) reduces to minimizing
\[
F_{m,q}(t)=2\log(1-qt^m)-\log(1-t^2),\quad 0\le t<1. \tag{2}
\]
Here \(F_{m,q}(0)=0\), and \(F_{m,q}(t)\to+\infty\) as \(t\uparrow1\), since \(q<1\). A direct differentiation gives
\[
F'_{m,q}(t)=\frac{2t[1-qh_m(t)]}{(1-t^2)(1-qt^m)},\quad
h_m(t)=t^{m-2}[m-(m-1)t^2]. \tag{3}
\]

**The two-source case.** For \(m=2\), \(h_2(t)=2-t^2\). If \(q\le1/2\), (3) is strictly positive for positive \(t\). Otherwise its sign switches once, from negative to positive, at \(t=\sqrt{2-1/q}\). This proves the exact continuous transition, since \(q=r^2\).

**All larger polygons.** For \(m\ge3\), differentiation shows that \(h_m\) increases strictly from zero to its unique maximum at \(t_0=\sqrt{(m-2)/(m-1)}\), then decreases strictly to \(h_m(1)=1\). Its maximum is
\[
H_m=2\left(\frac{m-2}{m-1}\right)^{(m-2)/2}>1.
\]
When \(q\le1/H_m\), (3) is nonnegative everywhere and positive except possibly at one radius; the uniform density uniquely minimizes (2). For \(1/H_m<q<1\), equation \(qh_m(t)=1\) has exactly two roots. The smaller is a local maximum of \(F_{m,q}\), and the larger is its unique positive-radius local minimum. Consequently the global minimum is either at zero or at the larger root.

At a nonzero tie with the uniform candidate, equations \(F_{m,q}(t)=0\) and \(F'_{m,q}(t)=0\) must hold. Put \(v=\sqrt{1-t^2}\in(0,1)\). The first equation reads \(qt^m=1-v\); the second becomes
\[
1-v^2=(1-v)[1+(m-1)v^2],
\]
so \(v=1/(m-1)\). Therefore \(t=t_c(m)\) and \(q=q_c(m)\), with exactly the values stated in the finding. Moreover \(t_c(m)>t_0\), so the tie involves the positive-radius local minimum rather than the local maximum. Strict convexity of \(x\mapsto x\log x\) proves \(q_c(m)<1\), since
\[
\log q_c(m)=(m-1)\log(m-1)-\tfrac12[m\log m+(m-2)\log(m-2)]<0.
\]
Also \(q_c(m)>1/H_m\), because \(h_m(t_c)<H_m\).

At \(q=q_c\), the derivative analysis already proves that the only possible global minima are \(t=0\) and the larger stationary root \(t=t_c\); the tie identities give \(F_{m,q_c}(0)=F_{m,q_c}(t_c)=0\). Hence \(F_{m,q_c}(t)\ge0\) for every radius, with equality only at these two radii. For every fixed \(t>0\), \(F_{m,q}(t)\) decreases strictly with \(q\), so \(q<q_c\) forces \(F_{m,q}(t)>F_{m,q_c}(t)\ge0\), while \(q>q_c\) gives \(F_{m,q}(t_c)<0\). Thus the uniform and off-center branches exchange global optimality exactly once, at \(q_c\). Since the descending branch of \(h_m\) is strictly monotone, its positive-radius optimizer is unique for every \(q>q_c\). This proves all optimizer counts and the discontinuity.

**The opposite KL orientation.** Using the Fourier expansion of \(\log P_{t,\phi}\) and the fact that the Fourier coefficients of \(Q_{m,r}\) vanish outside multiples of \(m\), one obtains
\[
\int Q_{m,r}\log P_{t,\phi}\,\frac{d\theta}{2\pi}
=\log(1-t^2)-\frac{2}{m}\log|1-qt^m e^{im\phi}|.
\]
Maximizing over \(\phi\) for fixed positive radius aligns one of the \(m\) phases. The derivative of the resulting cross-entropy is
\[
-\frac{2t[1-qt^{m-2}]}{(1-t^2)(1-qt^m)}<0\qquad(t>0).
\]
The source entropy is independent of candidate parameters, so this strict decrease proves the uniform density is the unique minimizer of \(D(Q_{m,r}\Vert P_{t,\phi})\).

**Large-polygon law.** Write \(k=m-1\). Taylor's formula for the symmetric second difference of \(f(x)=x\log x\) gives
\[
\log q_c(m)=f(k)-\frac{f(k+1)+f(k-1)}2=-\frac1{2k}+O(k^{-3}).
\]
Dividing by \(m\) and exponentiating gives \(r_c(m)=1-1/(2m^2)+O(m^{-3})\); direct binomial expansion of \(t_c(m)=\sqrt{1-(m-1)^{-2}}\) gives the stated jump-radius asymptotic.

## Verification
The standalone `CHECK.py` replays exact critical-parameter identities over a range of polygon orders, checks the predicted global radial minimizers against dense finite grids, and independently compares the analytic KL expression (1) with high-resolution periodic numerical quadrature. Execute it using `python3 CHECK.py` with Python 3 standard library only. Finite numerical tests corroborate but do not replace the analytic proof, which establishes the complete infinitely parameterized statement. The critical expressions at \(m=3\) and \(m=4\) and the limits for large \(m\) can be checked directly.

## Relationship to prior work
Nielsen and Okamura (2021), Theorems 4 and 5, establish invariance and symmetry of divergences between **two individual** circular/wrapped Cauchy densities. The present target is a genuinely non-Poisson mixture, so pairwise symmetry does not imply equal directed projection optima. Nielsen (2020) studies Cauchy information geometry and Voronoi diagrams rather than optimization against equiangular mixtures. Kalantan and Einbeck (2019) address estimation of finite real-line Cauchy mixtures, not the sharp regular-circle KL projection. Related previous analyses of squared-error Poisson compression concern a different objective: their global minimizers cannot determine (1) or its directed-KL first-order transitions. These distinctions do not establish absolute priority; an unlocated equivalent earlier result remains possible.

## Limitations
The theorem is restricted to a regular polygon of equal positive Poisson components and a single candidate Poisson density. It does not classify unequal weights, irregular source positions, other divergences, general mixture-model estimation, or local behavior of arbitrary parameter perturbations. No independent mathematical audit has been performed. The proof does not claim a universal novelty certificate.

## References
- F. Nielsen and K. Okamura, *On \(f\)-divergences between Cauchy distributions*, arXiv:2101.12459, first posted 29 January 2021. https://arxiv.org/abs/2101.12459
- F. Nielsen, *On Voronoi Diagrams on the Information-Geometric Cauchy Manifolds*, Entropy 22 (2020), article 713, published 28 June 2020. https://doi.org/10.3390/e22070713
- Z. I. Kalantan and J. Einbeck, *Quantile-Based Estimation of the Finite Cauchy Mixture Model*, Symmetry 11 (2019), article 1186, published 19 September 2019. https://doi.org/10.3390/sym11091186
- J. T. Kent and D. E. Tyler, *Maximum likelihood estimation for the wrapped Cauchy distribution*, Journal of Applied Statistics 15 (1988), 247–254. https://doi.org/10.1080/02664768800000029
