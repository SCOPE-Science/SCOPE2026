# A sharp hard-edge sine-integral law for Chebyshev projection of bounded-variation data

## Finding
Let \(d\mu(x)=dx/(\pi\sqrt{1-x^2})\) on \((-1,1)\), and let \(Q_n\) be the \(L^2(\mu)\)-orthogonal projection onto real polynomials of degree at most \(n\). For every integer \(n\ge0\), define
\[
E_n=\sup_{\substack{f\in BV(-1,1)\\\operatorname{TV}(f)>0}}
\frac{\|f-Q_nf\|_{L^2(\mu)}}{\operatorname{TV}(f)}.
\]
Then the **exact finite-degree constant** is
\[
E_n^2=\frac1{\pi^2}\max_{0\le\theta\le\pi}
\left[\pi\theta-\theta^2-
\sum_{k=1}^{n}\frac{1-\cos(2k\theta)}{k^2}\right]. \tag{1}
\]
For every degree the supremum is attained by at least one interior unit step \(f=\mathbf1_{[\cos\theta,1]}\), up to addition of a constant and multiplication by a scalar. In particular \(E_0=1/2\).

Define \(\operatorname{Si}(c)=\int_0^c(\sin t)/t\,dt\), and let \(c_*\in(0,\pi)\) be the unique solution of \(\operatorname{Si}(c_*)=\pi/2\). Then
\[
\boxed{\lim_{n\to\infty}\sqrt n\,E_n
=\frac{\sqrt{1-\cos c_*}}{\pi}=0.369596161139\ldots.} \tag{2}
\]
If \(\theta_n\in[0,\pi]\) is **any** maximizing argument in (1) and \(\delta_n=\min\{\theta_n,\pi-\theta_n\}\), then
\[
2n\delta_n\longrightarrow c_*,\qquad
1-|\cos\theta_n|\sim\frac{c_*^2}{8n^2}. \tag{3}
\]
Numerically \(c_*=1.926447660317\ldots\). The strict amplification relative to fixed interior jumps is the universal factor \(\sqrt{1-\cos c_*}>1\) at the level of the \(\sqrt n\)-scaled error.

## Assumptions and scope
Functions are real \(L^1\) equivalence classes of bounded distributional variation on the open interval; \(\operatorname{TV}(f)=|Df|((-1,1))\). Pointwise endpoint modifications have no effect on either side. The arcsine measure is a probability measure; this normalization is essential to (1) and (2). The polynomial projector is the continuous weighted \(L^2\) orthogonal projector, **not** interpolation at Chebyshev nodes or a discrete least-squares rule. The limit concerns all integer degrees \(n\to\infty\). Equation (3) concerns maximizing **single-jump locations**, not a classification of arbitrary multi-jump extremizers.

## Proof
**1. Reduction to one jump.** A representative of each real BV class has a finite signed distributional derivative \(\nu=Df\) and, modulo constants and null sets, can be written
\[
f(x)=\mathrm{constant}+\int_{(-1,1)}\mathbf1_{[t,1]}(x)\,d\nu(t).
\]
The constant lies in the range of \(Q_n\). Applying the bounded linear map \(I-Q_n\), Bochner integration in \(L^2(\mu)\), and the triangle inequality gives
\[
\|(I-Q_n)f\|_2\le |\nu|((-1,1))\,
\sup_{-1<t<1}\|(I-Q_n)\mathbf1_{[t,1]}\|_2.
\]
An interior unit step has variation one, proving equality of the two operator suprema. Its residual norm depends continuously on its angular location, is zero at the endpoints, and has a positive interior maximum; hence the finite-degree norm is attained by a step.

**2. Exact Parseval formula.** Let \(t=\cos\theta\), \(0\le\theta\le\pi\). The orthonormal polynomials for \(\mu\) are \(1\) and \(\sqrt2\,T_k(x)\) for \(k\ge1\), where \(T_k(\cos u)=\cos(ku)\). The unit step has coefficients \(\sqrt2\sin(k\theta)/(\pi k)\) for \(k\ge1\). Thus Parseval gives
\[
\|(I-Q_n)\mathbf1_{[\cos\theta,1]}\|_2^2
=\frac{1}{\pi^2}\sum_{k=n+1}^{\infty}\frac{1-\cos(2k\theta)}{k^2}.
\tag{4}
\]
The classical cosine-square sum \(\sum_{k\ge1}(1-\cos(2k\theta))/k^2=\pi\theta-\theta^2\) on \([0,\pi]\) converts (4) into (1). For \(n=0\), maximizing \(\theta(\pi-\theta)\) gives \(E_0^2=1/4\).

**3. Boundary scaling.** Put \(H_n(\theta)=n\pi^2\|(I-Q_n)\mathbf1_{[\cos\theta,1]}\|_2^2\) and \(c=2n\theta\). If \(c_n\to c\ge0\), the absolutely dominated Riemann-sum limit of (4) gives
\[
H_n(c_n/(2n))\longrightarrow
G(c):=\int_1^{\infty}\frac{1-\cos(ct)}{t^2}\,dt.
\tag{5}
\]
The integrable bound \(2/t^2\) handles the infinite tail, and the statement holds for variable \(c_n\), not only fixed arguments. Integration by parts yields
\[
G(c)=1-\cos c+c\bigl(\pi/2-\operatorname{Si}(c)\bigr),
\qquad G'(c)=\pi/2-\operatorname{Si}(c) \quad(c>0).
\tag{6}
\]
We use \(G(0)=0\) by continuity.

**4. Unique global maximum of the scaling profile.** Since \(\operatorname{Si}'(c)=\sin(c)/c>0\) for \(0<c<\pi\), and \(\operatorname{Si}(2)>\pi/2\), there is a unique \(c_*\in(0,2)\) with the asserted equation. On \((0,\pi)\), (6) makes \(G\) increase before \(c_*\) and decrease after it. On \([\pi,2\pi]\), \(G''(c)=-\sin(c)/c\ge0\), so no larger maximum occurs except possibly at an endpoint. The \(\pi\) endpoint is below \(G(c_*)\) by monotonicity. For \(c\ge2\pi\), integrating the cosine tail by parts gives
\[
G(c)=1-\int_1^\infty\frac{\cos(ct)}{t^2}\,dt
\le1+\frac2c\le1+\frac1\pi<\frac43.
\]
Elementary alternating Taylor enclosures \(\cos2<-0.416\), \(\operatorname{Si}(2)<1.606\), and \(\pi>3.14159\) give \(G(2)>1.34559>4/3\). Therefore \(c_*\) is the **unique global maximizer** of \(G\) on \([0,\infty)\), and \(G(c_*)=1-\cos c_*\).

**5. Exclusion of fixed/intermediate angles.** By reflection symmetry in (4), take \(0\le\theta_n\le\pi/2\). If \(n\theta_n\to\infty\), summation by parts with \(|\sum_{j=a}^{b}e^{2ij\theta}|\le1/|\sin\theta|\) gives
\[
\left|\sum_{k=n+1}^{\infty}\frac{\cos(2k\theta_n)}{k^2}\right|
\le\frac{2}{(n+1)^2\sin\theta_n}.
\]
Since \(\sin\theta\ge2\theta/\pi\) on \([0,\pi/2]\), its product by \(n\) vanishes. Meanwhile \(n\sum_{k>n}k^{-2}\to1\), so \(H_n(\theta_n)\to1\), strictly below \(G(c_*)>4/3\). Taking \(\theta=c_*/(2n)\) in (5) supplies the larger lower bound. Thus all maximizing angles have bounded \(2n\theta_n\); every subsequential limit maximizes \(G\) by (5), hence equals \(c_*\). This proves (2) and the first part of (3); expanding \(1-\cos\delta_n\sim\delta_n^2/2\) proves the second.

## Verification
The standalone `check.py` uses only Python's standard library. It checks the finite Fourier/Parseval formula against truncated positive tails with a rigorous elementary remainder tolerance, exact symmetry, the degree-zero value, first critical points for selected degrees, and convergence of the scaled locations and constants. The saved run yielded **2,916 successful assertions**, \(c_*=1.92644766031737\), and \(\sqrt{1-\cos c_*}/\pi=0.36959616113943\). These finite checks do **not** establish the BV-to-step reduction or infinite-degree asymptotic: those are supplied by the proof above.

To reproduce: `python check.py` with Python 3. No numerical library or internet access is needed. `check.py` and this file are supplied together as independent file contents.

## Relationship to prior work
Zhou–Narayan–Xu (arXiv:1401.0894v1, January 5, 2014) study Chebyshev polynomial spaces and **discrete** least-squares stability, including smooth-data convergence estimates; their Theorem 3.4 is not a sharp discontinuous-data norm for the continuous projector. Wang (arXiv:2106.03456, originally 2021) analyzes **pointwise** Chebyshev error localization for algebraic singularities and spectral differentiation, not the supremal variation-normalized weighted \(L^2\) error nor a moving discontinuity location. Akansha (arXiv:2404.18723, 2024) proves coefficient-decay and **\(L^1\)** error bounds for truncated Chebyshev approximations with approximate quadrature coefficients, under derivative-variation hypotheses; this does not yield (1)–(3). Standard coefficient-wise BV bounds give nonsharp \(n^{-1/2}\) decay but do not identify the universal hard-edge constant or maximizing spatial scale.

An accessible historical comparison concerns unweighted Legendre projection on BV data, whose worst jumps behave differently. Neither change of polynomial weight nor a Fourier-cosine equivalence alone determines the sharp supremum in (1); both the exact angular optimization and unique global limiting optimizer are required. The Fourier cosine identity and sine integral are classical tools, **not** claimed as new. The precise combination in (1)–(3) was not located in the investigated literature and mathematical record searches; absence of a match is not proof of priority.

## Limitations
Only real one-dimensional BV inputs, the normalized first-kind Chebyshev weight, and continuous weighted orthogonal projection are treated. The work does not give a quantitative remainder in (2), exact closed-form maximizing angles at each finite degree, an extension to complex BV data, or results for interpolation/noisy discrete coefficients. The large-degree hard-edge assertion is about worst **one-jump locations**; arbitrary BV maximizers are not classified. Equivalent older Fourier-cosine results or obscure textbook treatments may exist. Independent validation has not been performed.

## References
- T. Zhou, A. Narayan, and Z. Xu, *Multivariate discrete least-squares approximations with a new type of collocation grid*, arXiv:1401.0894v1 (January 5, 2014), https://arxiv.org/abs/1401.0894.
- H. Wang, *Analysis of error localization of Chebyshev spectral approximations*, arXiv:2106.03456 (June 7, 2021; later revisions), https://arxiv.org/abs/2106.03456.
- S. Akansha, *Exploring Chebyshev Polynomial Approximations: Error Estimates for Functions of Bounded Variation*, arXiv:2404.18723v1 (April 29, 2024), https://arxiv.org/abs/2404.18723.
