# Convex ridge weights restore inclusion monotonicity on nested circles

## Finding
For a closed Euclidean disk \(D(c,r)\subset\mathbb R^2\) with \(r>0\), a unit vector \(v\in S^1\), and any finite nonnegative convex function \(g:\mathbb R\to[0,\infty)\), set
\[
  W_{g,v}(D(c,r))=\int_{\partial D(c,r)}g(\langle v,x\rangle)\,d\mathcal H^1(x).
\]
For **every** pair of nested positive-radius disks \(D(c,r)\subseteq D(C,R)\), without a restriction on their positions relative to the origin,
\[
  W_{g,v}(D(c,r))\le W_{g,v}(D(C,R)). \tag{1}
\]
Consequently, for **every real exponent** \(p\ge1\),
\[
  \int_{\partial D(c,r)}\|x\|_2^p\,d\mathcal H^1(x)
  \le \int_{\partial D(C,R)}\|x\|_2^p\,d\mathcal H^1(x), \tag{2}
\]
with strict inequality for proper disk containment. The conclusion extends by positive superposition to all weights of the form \(\phi(\rho)=\int_{[1,\infty)}\rho^p\,d\mu(p)\) whenever the resulting boundary integrals are finite (\(\mu\) is nonnegative).

The convex-ridge restriction is meaningful: there are smooth, strictly increasing, bounded, nonnegative radial weights \(\phi\) and nested disks \(A\subset B\) such that \(\int_{\partial A}\phi(\|x\|_2)>\int_{\partial B}\phi(\|x\|_2)\). More precisely, for \(a>r>0\), \(t=a-r\), \(A=D((a,0),r)\), and \(B_\varepsilon=D((a-\varepsilon,0),r+\varepsilon)\), the step-weight boundary-length difference is
\[
 \mathcal H^1(\partial B_\varepsilon\cap\{\|x\|_2\ge t\})-
 \mathcal H^1(\partial A\cap\{\|x\|_2\ge t\})
 =-4\sqrt{\frac{rt}{a}}\,\sqrt{\varepsilon}+O_{a,r}(\varepsilon),\quad \varepsilon\downarrow0. \tag{3}
\]
Thus nonnegative increasing radial weights do **not** have the universal disk-monotonicity property without additional structure.

## Assumptions and scope
All disks have positive radius, and containment is ordinary Euclidean set inclusion. The argument does not require that either disk contain the origin. The scalar \(g\) is finite everywhere, convex, and nonnegative. When \(g\) is only considered on the compact projection interval swept out by the disks, it suffices to be convex and nonnegative there. The power result uses \(p\ge1\); no statement is made about \(0<p<1\). The counterexample uses sufficiently small \(0<\varepsilon<\min\{a-r,r\}\), and the smooth approximants are chosen after the strict step-weight difference has been established. The relevant classification is planar convex geometry, MSC2020 52A20.

## Proof
**1. The one-sided hinge.** Fix \(s\in\mathbb R\) and write \(g_s(u)=(u-s)_+\). For the scalar projection of the center \(a=\langle v,c\rangle\) and radius \(r>0\), define
\[
 F_s(a,r)=\int_{\partial D(c,r)}(\langle v,x\rangle-s)_+\,d\mathcal H^1(x).
\]
Taking \(v\) as the horizontal axis gives \(F_s(a,r)=r\int_0^{2\pi}(a+r\cos\theta-s)_+\,d\theta\). Put \(q=(s-a)/r\). Direct integration yields
\[
 F_s(a,r)=\begin{cases}
 0,&q\ge1,\\
 2r^2\bigl(\sqrt{1-q^2}-q\arccos q\bigr),&-1<q<1,\\
 2\pi r(a-s),&q\le-1.
 \end{cases} \tag{4}
\]
The formulas agree continuously at \(q=\pm1\).

**2. Disk containment implies a monotone path.** Given \(D(c,r)\subseteq D(C,R)\), we have \(R\ge r\) and \(\|C-c\|_2\le R-r\). Interpolate linearly, \(r_u=r+u(R-r)\), \(c_u=c+u(C-c)\) for \(u\in[0,1]\). If \(R>r\), use radius as the parameter. The projected center \(a(r_u)=\langle v,c_u\rangle\) then has slope \(|da/dr|\le1\).

The derivative \(\partial_a F_s\ge0\), so the least derivative along a permitted radius-increasing path occurs at \(da/dr=-1\). In the middle regime \(-1<q<1\), the chain rule gives
\[
 \frac{d}{dr}F_s(a(r),r)\bigg|_{a'=-1}
 =2r\left[2\sqrt{1-q^2}-(1+q)\arccos q\right]. \tag{5}
\]
Write \(q=\cos\alpha\), \(0<\alpha<\pi\). Then the bracket equals \((1+\cos\alpha)(2\tan(\alpha/2)-\alpha)\), which is nonnegative by \(\tan z\ge z\) for \(0\le z<\pi/2\). For \(q\ge1\), the derivative is zero in the open regime, and for \(q\le-1\) the least derivative is \(2\pi((a-s)-r)\ge0\). Continuity through the thresholds proves \(F_s(a,r)\) nondecreasing along the entire path. Replacing \(a\) and \(s\) by their negatives proves the same for \((s-u)_+\).

**3. Arbitrary nonnegative convex ridges.** Fix a compact interval containing all projections of all intermediate disks. A finite nonnegative convex \(g\) restricted to this interval is a nonnegative constant plus a positive superposition of right and left hinges, using the distributional second derivative and a supporting slope at a minimizer on the interval. Each summand has nondecreasing weighted perimeter by Step 2. Positive approximation handles nonsmooth or infinite second-derivative measures at endpoints. This proves (1).

**4. Radial powers and strictness.** Rotational averaging gives the exact identity
\[
 \|x\|_2^p=\frac{1}{\int_0^{2\pi}|\cos\theta|^p\,d\theta}
   \int_0^{2\pi}|\langle x,(\cos\theta,\sin\theta)\rangle|^p\,d\theta. \tag{6}
\]
The ridge function \(u\mapsto|u|^p\) is nonnegative and convex for every \(p\ge1\). Apply (1) in each direction, and integrate (Tonelli) to get (2). If containment is proper, then \(R>r\). Along the interpolating path, for directions perpendicular to the instantaneous center, the ridge perimeter has strictly positive radius derivative (the scalar center is zero, so the center derivative vanishes by symmetry). This persists for an open set of nearby directions. Its angular average therefore has positive derivative, yielding strictness in (2). Positive superposition gives the stated extension.

**5. Sharp boundary of the weight hypothesis.** For \(A\) and \(B_\varepsilon\) in the Finding, disk containment follows from equality \(\|(a,0)-(a-\varepsilon,0)\|=\varepsilon=(r+\varepsilon)-r\). Almost every point on \(\partial A\) has radial distance \(>t=a-r\), so its radial-step weighted perimeter is \(2\pi r\). With \(b=a-\varepsilon\) and \(R=r+\varepsilon\), the outer circle portion satisfying \(\|x\|_2\ge t\) has length \(2R\arccos q_\varepsilon\), where
\[
 q_\varepsilon=\frac{t^2-b^2-R^2}{2bR}.
\]
Since \(1+q_\varepsilon=2t\varepsilon/(ar)+O_{a,r}(\varepsilon^2)\) and \(\arccos(-1+h)=\pi-\sqrt{2h}+O(h^{3/2})\), expansion proves (3). This is negative for all sufficiently small positive \(\varepsilon\). Replacing the radial step by the smooth increasing logistic weights \(\phi_k(\rho)=1/(1+e^{-k(\rho-t)})\) and using dominated convergence on the two boundary circles yields the claimed smooth counterexamples for sufficiently large finite \(k\).

## Verification
The standalone `verify.py` (Python 3, standard library only) evaluates the closed hinge formula against independent trapezoidal quadrature, randomly checks nested-circle monotonicity for both hinges and radial powers, evaluates a strict smoothable step-weight example, and checks the square-root asymptotic coefficient. Command: `python verify.py`. One run passed 2,703 diagnostic assertions. The proof of universal statements is the analytic argument above; finite checks are not an infinite verification or a historical novelty certificate.

## Relationship to prior work
Csató and Giovagnoli (arXiv:2610.11677v1, October 8, 2026) prove inclusion monotonicity of nonnegative increasing radial weighted perimeters for convex bodies when the smaller contains the weight origin, and demonstrate failure without that condition using a triangle inside a square for the quadratic weight. Our result changes the shape class to *pairs of Euclidean disks*, removes any origin-containment requirement for all convex ridge integrands, and yields the full real range of radial powers \(p\ge1\). It also exhibits a sharp radial-step counterexample showing why their broad class of increasing weights cannot be treated identically on translated disks. Saracco and Stefani (arXiv:2306.07770) show that unrestricted convex-body inclusion monotonicity forces an isotropic weight to be constant, which does not imply or exclude the disk-restricted assertion here. We make no claim that a general convex-body theorem holds for the nonconstant powers in (2).

## Limitations
Historical priority remains conditional on further specialized comparison with results about convex-ordering of circular surface measures, arc-sine measures, or weighted spherical means. The result is planar. The proof does not extend all radial increasing convex weights automatically, nor does it cover \(0<p<1\). The auxiliary step-weight comparison concerns discontinuous weights first; smoothing yields existence, but no optimal smoothness scale is claimed. No external independent audit was performed.

## References
1. G. Csató and D. Giovagnoli, *Continuity and monotonicity of weighted perimeters of convex bodies*, arXiv:2610.11677v1 (first public October 8, 2026), https://arxiv.org/abs/2610.11677 .
2. G. Saracco and G. Stefani, *On the monotonicity of weighted perimeters of convex bodies*, arXiv:2306.07770 (first public June 13, 2023), Math. Nachr. 297 (2024), 1444–1450, https://doi.org/10.1002/mana.202300280 .
