# Sharp high-order half-density Gabor conditioning for unscaled cardinal B-splines

## Finding
Let \(B_n=\mathbf 1_{[0,1]}^{*n}\) be the nonnegative cardinal B-spline of order \(n\ge2\), normalized by \(\int_{\mathbb R}B_n(t)\,dt=1\). Let \(A_n,B_n^{\mathrm{up}}\) be the optimal lower and upper bounds of the Gabor frame \(\{e^{\pi ijt}B_n(t-k):j,k\in\mathbb Z\}\) in \(L^2(\mathbb R)\). Put \(c=2\sqrt2/\pi\). Then, as the **order** \(n\to\infty\), with lattice spacings unchanged,
\[
 A_n=2c^{2n}(1+O((3/5)^n)),\qquad
 1\le B_n^{\mathrm{up}}\le1+O(c^{2n}),
\]
where the big-O constants are absolute. In particular,
\[
 \lim_{n\to\infty}\frac{A_n}{2(8/\pi^2)^n}=1,\quad
 \lim_{n\to\infty} B_n^{\mathrm{up}}=1,\quad
 \lim_{n\to\infty}\frac{(8/\pi^2)^n B_n^{\mathrm{up}}}{A_n}=\frac12.
\]
Equivalently, the optimal condition number grows as \(\frac12(\pi^2/8)^n\). If \((x_n,\nu_n)\) minimizes the Zak frame symbol, its frequency satisfies \(\operatorname{dist}(\nu_n,\frac14+\frac12\mathbb Z)\to0\). The leading exponential lower bound does not depend on the time coordinate.

## Assumptions and scope
We use \(\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-2\pi it\xi}\,dt\), translations \(T_k f(t)=f(t-k)\), modulations \(M_{j/2}f(t)=e^{\pi ijt}f(t)\), and the unnormalized Zak transform
\[
 Zf(x,\nu)=\sum_{k\in\mathbb Z}f(x+k)e^{-2\pi ik\nu},\qquad (x,\nu)\in[0,1]^2.
\]
Changing to centered B-splines only translates the window and does not change the frame bounds. Frame bounds refer to the infinite Gabor family, not finite truncations, and the asymptotics vary the spline order rather than the sampling density. The known integer-oversampling frame theorem guarantees positive lower bounds for each \(n\ge2\) at this lattice.

## Proof
**1. Exact frame symbol and normalizations.** The period-one Zak transform diagonalizes the Gabor frame operator at translation step one and modulation step one half. In the stated normalization, its scalar multiplier is
\[
 Q_n(x,\nu)=|ZB_n(x,\nu)|^2+|ZB_n(x,\nu+\tfrac12)|^2.
\]
Therefore \(A_n=\min_{[0,1]^2}Q_n\) and \(B_n^{\mathrm{up}}=\max_{[0,1]^2}Q_n\). One can reconstruct the normalization directly from the Walnut representation: its coefficients are \(2\sum_jB_n(x+j)B_n(x+j-2\ell)\), which are precisely the even Fourier coefficients of the displayed sum of Zak-modulus squares. For \(n=2\), \(ZB_2(x,\nu)=(1-x)+xe^{-2\pi i\nu}\) for \(0\le x\le1\), and \(Q_2=2((1-x)^2+x^2)\); thus \(A_2=1\), \(B_2^{\mathrm{up}}=2\). This checks the scaling.

**2. Uniform Poisson alias bounds.** Since
\[
 \widehat B_n(\xi)=e^{-\pi in\xi}\left(\frac{\sin\pi\xi}{\pi\xi}\right)^n,
\]
Poisson summation (also obtained by applying Fourier series to the continuous periodization) gives
\[
 ZB_n(x,\nu)=\sum_{\ell\in\mathbb Z}\widehat B_n(\nu+\ell)e^{2\pi i(\nu+\ell)x}.
\]
Put \(s(t)=\sin(\pi t)/(\pi t)\) for \(0\le t<1\), with \(s(0)=1\). It is positive and strictly decreasing on \((0,1)\). By periodicity and conjugation of the real-window Zak transform, it suffices to consider \(0\le\nu\le1/2\).

On \(\nu\in I=[1/8,3/8]\), the nearest Fourier alias of \(ZB_n(x,\nu)\) is \(\ell=0\), while the nearest alias of \(ZB_n(x,\nu+1/2)\) is \(\ell=-1\). Both are unique. The ratio of the modulus of the next alias to the leading alias is at most \(3/5\) on \(I\), and the remaining alias ratios sum to at most \(C(3/5)^n\) for an absolute \(C\) and all \(n\ge2\). Therefore, uniformly in \(x\) and \(\nu\in I\),
\[
 Q_n(x,\nu)=\{s(\nu)^{2n}+s(1/2-\nu)^{2n}\}(1+O((3/5)^n)). \tag{1}
\]
If \(0\le\nu\le1/8\), the unique nearest alias of the first Zak term lies at distance at most \(1/8\) from zero and all others have at least distance \(7/8\), giving
\[
 Q_n(x,\nu)\ge(1-O(7^{-n}))s(1/8)^{2n}.
\]
The symmetrical inequality holds for \(3/8\le\nu\le1/2\), using the second Zak term. Since \(s(1/8)>s(1/4)\), neither outer interval can contain a global minimizer for sufficiently large \(n\).

**3. Sharp minimization.** Write \(L(t)=\log s(t)\). On \(I\), \(L'(t)<0\), bounded away from zero in magnitude, and \(L''(t)=-\pi^2\csc^2(\pi t)+t^{-2}\) is bounded. For all sufficiently large \(n\), the function \(h_n(t)=s(t)^{2n}\) is strictly convex on \(I\), since
\[
 h_n''(t)=2n h_n(t)\big(L''(t)+2nL'(t)^2\big)>0.
\]
By symmetry and convexity, \(h_n(\nu)+h_n(1/2-\nu)\ge2h_n(1/4)=2c^{2n}\), with equality only at \(\nu=1/4\). Applying (1) to the lower bound and evaluating (1) at \(\nu=1/4\) proves \(A_n=2c^{2n}(1+O((3/5)^n))\). For each fixed \(\varepsilon>0\), a central frequency with \(\lvert\nu-1/4\rvert\ge\varepsilon\) has at least one leading term at least \(s(1/4-\varepsilon)^{2n}\), exponentially larger than \(2c^{2n}\); this and the excluded outer intervals prove that every minimizing frequency converges to \(1/4\) modulo \(1/2\).

**4. Upper frame bound.** The cardinal partition of unity \(\sum_{k\in\mathbb Z}B_n(x+k)=1\) and positivity give \(|ZB_n(x,\nu)|\le1\) for every \(x,\nu\), while \(ZB_n(x,0)=1\). Of the two frequencies \(\nu,\nu+1/2\), at least one has distance at least \(1/4\) from the nearest integer. The Poisson alias formula bounds that Zak component uniformly by \(C s(1/4)^n=Cc^n\). Thus \(1\le B_n^{\mathrm{up}}\le1+C^2c^{2n}\). Combining with the lower-bound result yields the stated condition-number limit. \(\square\)

## Verification
The standalone `CHECK.py` reconstructs the cardinal splines from their B-spline basis, verifies the Poisson expansion independently of the direct finite sum, checks the exact order-two Zak frame symbol and the partition of unity, and numerically optimizes representative high-order frame symbols. Its finite tests supplement, rather than replace, the uniform alias and convexity proof. Reproduce with `python CHECK.py` (Python 3, NumPy, SciPy).

## Relationship to prior work
Hasannasab and Lemvig (arXiv:2609.13116, first posted September 11, 2026) prove frame-set and Zak-zero results for B-splines, including existence at the specified integer oversampling; their main results do not provide the order-dependent sharp lower-frame-bound asymptotic above. Stangl and Frederick (arXiv:2609.00481) treat the second-order spline's frame set and do not take spline order to infinity. Christensen, Kim, and Kim (arXiv:1708.04803) study **rescaled** high-order splines converging to Gaussian windows; that normalization and deformation of the window is not the fixed unscaled cardinal-spline regime here. Kloos and Stöckler (arXiv:1311.7359) develop Zak frame methods and bounds for exponential splines, notably order two and critical-density asymptotics, a different parameter limit. The Zak fiber identity and Fourier transform of splines are classical and are not claimed as new. The assertion here is the sharp fixed-lattice **order-growth** conditioning law.

## Limitations
The result only concerns the particular rectangular lattice \(a=1,b=1/2\), the nonnegative integral-one cardinal B-splines, and the limit of large spline order. Scaling the splines to unit height, unit norm, or Gaussian-like variance changes absolute bounds (though not their ratio for scalar rescalings); the constants above require the stated integral-one convention. No finite-order exact minimizer or optimal design among other lattices is asserted. The asymptotic error estimate is analytic, not an empirical extrapolation. Publication-priority assessment is provisional: equivalent calculations may be indexed under spline approximation or Weyl–Heisenberg frame terminology.

## References
- M. Hasannasab and J. Lemvig, *The zero set of the Zak transform of B-splines with applications to Gabor frames*, arXiv:2609.13116 (2026), https://arxiv.org/abs/2609.13116.
- A. Stangl and C. Frederick, *The frameset of the second-order B-Spline along \(ab=1/q\)*, arXiv:2609.00481 (2026), https://arxiv.org/abs/2609.00481.
- O. Christensen, H. O. Kim, and R. Y. Kim, *B-spline approximations of the Gaussian, their Gabor frame properties, and approximately dual frames*, arXiv:1708.04803 (2017), https://arxiv.org/abs/1708.04803.
- T. Kloos and J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359 (2013), https://arxiv.org/abs/1311.7359.
