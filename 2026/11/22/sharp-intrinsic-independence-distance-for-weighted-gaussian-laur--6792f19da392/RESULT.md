# Sharp intrinsic independence distance for weighted Gaussian Laurent fields on an annulus

## Finding

Fix \(0<q<1\), \(r>0\), and the circular complex Gaussian analytic field
\[
X_{q,r}(z)=\sum_{n\in\mathbb Z}\frac{\xi_n z^n}{\sqrt{1+r q^{2n}}},\qquad q<|z|<1,
\]
where the \(\xi_n\) are independent standard circular complex Gaussians. Let \(d_q\) be the intrinsic Poincaré distance of curvature \(-1\) on the annulus, and define its *independence distance*
\[
D_q(r)=\inf\{d_q(z,w):q<|z|,|w|<1,\;X_{q,r}(z)\text{ and }X_{q,r}(w)\text{ independent}\},
\]
with \(\inf\varnothing=+\infty\). Put \(L=\log(1/q)\) and \(\xi=\log r/(2\log q)\).

**Theorem.** If \(\xi\in\mathbb Z\), there are no independent evaluation pairs in the annulus. Otherwise, writing \(\{\xi\}=\xi-\lfloor\xi\rfloor\in(0,1)\),
\[
\boxed{D_q(r)=2\operatorname{arsinh}\!\left(\frac{\sinh(\pi^2/(2L))}{\sin(\pi\{\xi\})}\right).}
\]
Let \(k=\lceil\xi\rceil\) and \(s=q^{2k}/r\in(q^2,1)\). All independent evaluation pairs have \(z\overline w=-s\). The infimum is attained precisely by the antipodal pairs
\[
(z,w)=(\sqrt{s}\,e^{i\phi},-\sqrt{s}\,e^{i\phi}),\qquad\phi\in\mathbb R/(2\pi\mathbb Z).
\]
Consequently \(D_q(r)\) is periodic in \(\log r\) with period \(2L\) in absolute value, it obeys the sharp uniform lower bound
\[
\boxed{D_q(r)\ge\frac{\pi^2}{L},}
\]
with equality exactly at \(r=q^{2m+1}\), \(m\in\mathbb Z\). This lower bound equals one half of the length of the annulus's unique core closed hyperbolic geodesic.

For \(r\to q^{2m}\), let \(h=\operatorname{dist}(\log r,2L\mathbb Z)\to0\). The divergence is sharp:
\[
\boxed{D_q(r)=2\log\!\left(\frac{4L\sinh(\pi^2/(2L))}{\pi h}\right)+o(1).}
\]
Thus exact independence is geometrically excluded altogether at discrete positive weights and requires points arbitrarily far apart as one approaches such a weight.

## Assumptions and scope

All distances are intrinsic to the complete curvature-\(-1\) Poincaré metric of \(\mathbb A_q=\{z:q<|z|<1\}\); using curvature \(-4\) would divide the reported lengths by two. The parameters satisfy \(q\in(0,1)\) and \(r>0\) without further restrictions. The field is proper/circular Gaussian, not a real Gaussian field. The Laurent series converges locally normally almost surely: the positive modes converge for \(|z|<1\), and negative modes converge for \(|z|>q\). Independence refers to two complex random variables at distinct positions, not to independence of their zero processes.

The exact **zeros of the covariance kernel** are an input from the established Jacobi-theta formula for weighted annular Szegő kernels; the new geometric conclusion is the minimization of intrinsic distance, its unique minimizing orbit, and its complete weight phase law.

## Proof

**1. Covariance zeros and Gaussian independence.** Orthogonality of the coefficients gives the analytic covariance kernel
\[
K_{q,r}(z,w)=\mathbb E[X_{q,r}(z)\overline{X_{q,r}(w)}]
=\sum_{n\in\mathbb Z}\frac{(z\overline w)^n}{1+r q^{2n}}.
\]
For a proper centered complex Gaussian vector, its two entries are independent exactly when their cross-covariance vanishes. Set \(u=z\overline w\); its modulus satisfies \(q^2<|u|<1\). The theta identity (Katori--Shirai, equation (2.30) in arXiv:2008.04177v3) in the product convention below reads
\[
K_{q,r}(z,w)=c_{q,r}\frac{\theta(-ru;q^2)}{\theta(u;q^2)},\qquad c_{q,r}=\frac{\prod_{j=1}^\infty(1-q^{2j})^3}{\theta(-r;q^2)}>0,
\]
where \(\theta(v;p)=\prod_{j=0}^{\infty}(1-vp^j)(1-p^{j+1}/v)\prod_{j=1}^{\infty}(1-p^j)\). This convention multiplies Katori--Shirai's theta by \(\prod_{j=1}^{\infty}(1-p^j)\), accounting for the cube in the prefactor. The numerator has simple zeros exactly at \(-ru=q^{2k}\), \(k\in\mathbb Z\), and the denominator has no zeros in \(q^2<|u|<1\). Thus the only candidate product is \(u=-q^{2k}/r\), with at most one possible index \(k\) in this open annulus. Write \(\xi=\log r/(2\log q)\). If \(\xi\notin\mathbb Z\), the unique choice is \(k=\lceil\xi\rceil\) and \(s=q^{2k}/r\in(q^2,1)\); otherwise no product zero exists. Conversely any \(z,w\in\mathbb A_q\) with \(z\overline w=-s\) gives independent values, and such pairs exist because \(q^2<s<1\). More explicitly, \(w=-s/\overline z\) with
\[
\max(q,s)<|z|<\min(1,s/q).
\]

**2. Intrinsic distance of two antipodal-angle points.** Let \(L=-\log q>0\), and lift the annulus by \(z=e^{x+iy}\) to the strip \(-L<x<0\), with deck translations \(y\mapsto y+2\pi j\). A conformal map to the upper half-plane is \(U=\exp(i\pi(x+L+iy)/L)\). It pulls back the curvature-\(-1\) metric to
\[
\mathrm ds=\frac{\pi\,|\mathrm d(x+iy)|}{L\sin(\pi(x+L)/L)}.
\]
If \(z\overline w=-s\), the angular displacement is \(\pi\) modulo \(2\pi\). Among all deck lifts, the smallest angular displacement in absolute value is \(\pi\), so the minimizing half-plane lift has multiplicative radial ratio \(e^{\pm\delta}\), where \(\delta=\pi^2/L\). The upper-half-plane distance identity \(\cosh d(U,V)=1+|U-V|^2/(2\operatorname{Im}U\operatorname{Im}V)\) consequently gives
\[
\cosh d_q(z,w)=\frac{\cosh\delta-\cos\theta_1\cos\theta_2}{\sin\theta_1\sin\theta_2},
\qquad
\theta_1=\frac\pi L\log\frac{|z|}{q},\quad
\theta_2=\frac\pi L\log\frac{|w|}{q}.
\]
This formula is the minimum over lifts; all more distant lifts increase \(\cosh\delta\).

**3. Strict minimization.** Because \(|z||w|=s\), the angle sum \(\theta_1+\theta_2=2\theta_0\) is fixed, with \(\theta_0=\pi\log(s/q^2)/(2L)\in(0,\pi)\). Put \(\theta_1=\theta_0+t\), \(\theta_2=\theta_0-t\), with both angles in \((0,\pi)\). A direct trigonometric reduction yields
\[
\cosh d_q(z,w)=\frac{\cosh\delta-\cos^2\theta_0+\sin^2 t}{\sin^2\theta_0-\sin^2 t}
=1+\frac{\cosh\delta-1+2\sin^2 t}{\sin^2\theta_0-\sin^2 t}.
\]
The admissibility conditions impose \(|t|<\min(\theta_0,\pi-\theta_0)\le\pi/2\). Hence \(\sin^2 t\) strictly increases with \(|t|\), and the right-hand side strictly increases with it; the denominator is positive throughout. The unique minimizing configuration therefore has \(t=0\), or \(|z|=|w|=\sqrt{s}\). Its distance satisfies
\[
\cosh D_q(r)=1+\frac{\cosh\delta-1}{\sin^2\theta_0},
\qquad
D_q(r)=2\operatorname{arsinh}\!\left(\frac{\sinh(\delta/2)}{\sin\theta_0}\right).
\]
Since \(k=\lfloor\xi\rfloor+1\), \(s=q^{2(k-\xi)}\); hence \(\theta_0=\pi\{\xi\}\) and the asserted exact distance follows.

**4. Sharp global geometry and singular weights.** The denominator \(\sin(\pi\{\xi\})\) lies in \((0,1]\). Equality with one occurs precisely for \(\{\xi\}=1/2\), equivalently \(r=q^{2m+1}\). At the core circle \(|z|=\sqrt q\), the metric density is \(\pi/L\) in the angular coordinate; its full length is \(2\pi^2/L\), proving the geometric interpretation of \(\delta\). For \(r\to q^{2m}\) set \(h=\operatorname{dist}(\log r,2L\mathbb Z)\). Then \(\sin(\pi\{\xi\})=\sin(\pi h/(2L))\sim\pi h/(2L)\). Substituting into the exact formula and using \(\operatorname{arsinh}v=\log(2v)+o(1)\) at infinity gives the stated logarithmic blow-up. These computations also establish the periodicity under \(r\mapsto q^2r\).

## Verification

The standalone \(\texttt{verify_independence.py}\) script performs 180 finite arbitrary-precision diagnostics at 75 decimal digits. These check theta-zero series cancellations for selected nonexceptional parameters, exact logarithmic periodicity, the strip distance identity, strict increase away from the minimizing equal-radius orbit, the sharp core lower bound, exceptional weights, and the near-exception asymptotic. The checker must not be interpreted as an infinite proof: the four-step derivation above establishes the global statements. Run with \(\texttt{python verify_independence.py}\) after installing \(\texttt{mpmath}\).

## Relationship to prior work

Katori--Shirai (arXiv:2008.04177, 2020), particularly equation (2.30), Lemma 2.3 and Proposition 2.4, established the theta-quotient covariance kernel, its zero products and independence for the conformally invariant weight. Gafai--Murid--Wahid (arXiv:2202.09114, 2022) also give a weighted annular Szegő product representation, with the same zero factors in equation (38). The covariance identities, and hence which weights admit independent evaluation pairs, are not claimed as new. The quantity classified here is instead the **smallest intrinsic hyperbolic separation of independent evaluations over all pairs**, including its weight-dependent minimizing orbit, uniform geometric bound, exact log-periodic profile and divergence law. A 2023 study by Gafai and coauthors focuses on computing Szegő-kernel zeros via conformal mapping, rather than this optimal intrinsic-distance question. Relevant published indexed work on powers, critical points and nonradial perturbations of annular Szegő kernels also addresses different claims.

## Limitations

The theorem concerns the explicitly defined annular Gaussian Laurent field and its weighted Szegő covariance, not arbitrary annular Gaussian analytic functions or their zero-point processes. It computes an exact zero-correlation distance, not a uniform bound on small nonzero correlations or a general probabilistic mixing scale. The source identities and simple-strip geometry make this a focused exact structural result, not a new formula for the theta quotient. Historical priority beyond the checked literature may require further expert comparison. No independent mathematical audit has been performed.

## References

1. M. Katori and T. Shirai, *Zeros of the i.i.d. Gaussian Laurent series on an annulus: weighted Szegő kernels and permanental-determinantal point processes*, first posted 10 August 2020, arXiv:2008.04177, https://arxiv.org/abs/2008.04177. See equation (2.30) in v3, Lemma 2.3 and Proposition 2.4.
2. N. S. Gafai, A. H. M. Murid and N. H. A. A. Wahid, *Infinite Product Representation for the Szegö Kernel for an Annulus*, first posted 18 February 2022, arXiv:2202.09114, https://arxiv.org/abs/2202.09114. See the weighted product formula (38).
3. N. S. Gafai and collaborators, *Computing the zeros of the Szegö kernel for doubly connected regions using conformal mapping*, 2023, https://doi.org/10.3934/math.2023607.
