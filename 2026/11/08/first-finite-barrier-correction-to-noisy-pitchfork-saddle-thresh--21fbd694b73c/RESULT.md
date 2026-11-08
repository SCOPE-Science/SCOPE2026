# First finite-barrier correction to noisy pitchfork saddle-threshold escape

## Finding
For the one-dimensional noisy subcritical pitchfork, the familiar Gaussian mean-first-passage crossover at the two unstable equilibria has a computable, nonconstant first finite-barrier correction. Specifically, for every fixed \(B>0\), uniformly for \(|\beta|\le B\) as \(r\to\infty\),
\[
\boxed{\frac{\mathbb E_0\tau_{r,\beta}}{\pi e^{r^2/2}/(\sqrt2 r)}=\Phi(2\beta)+\frac{(2\beta^2+1)e^{-2\beta^2}}{2\sqrt{2\pi}\,r}+O_B(r^{-2}).}
\]
The leading error-function profile was known in general Kramers first-passage theory. The claim here concerns the **next term**, its uniformity across the saddle-scale detection window, and the resulting finite-barrier threshold calibration. In particular, the first correction is positive at every fixed \(\beta\), and at the exact deterministic saddle it is \(1/(2\sqrt{2\pi}\,r)\) in Kramers-normalized units.

## Assumptions and scope
Let \(r>0\) and \(W_t\) be standard Brownian motion. Starting at \(X_0=0\), consider the unique solution, stopped upon exit from a bounded interval, of
\[
 dX_t=(-r X_t+X_t^3)\,dt+dW_t.
\]
For real \(\beta\), define \(b_{r,\beta}=\sqrt r+\beta/\sqrt r\) and \(\tau_{r,\beta}=\inf\{t\ge0:|X_t|=b_{r,\beta}\}\), whenever \(b_{r,\beta}>0\). Local existence and uniqueness suffice up to this stopping time; no assertion of global nonexplosion is needed for the unstopped cubic diffusion. Let \(\Phi(s)=\frac1{\sqrt{2\pi}}\int_{-\infty}^{s}e^{-v^2/2}dv\). The error symbol \(O_B(r^{-2})\) means that for each fixed \(B\) its absolute magnitude is bounded by \(C_Br^{-2}\) for all sufficiently large \(r\), uniformly in \(|\beta|\le B\).

The detector lies at signed distance \(\beta/\sqrt r\) from either unstable equilibrium. This is exactly the Gaussian fluctuation scale around the saddle: changing the detector by that amount affects the leading normalized exit time by a nontrivial amount. A detector placed at the deterministic saddle corresponds to \(\beta=0\).

## Proof
Write \(V_r(x)=rx^2/2-x^4/4\). The generator before stopping is \(L_r=(1/2)\partial_x^2-V'_r(x)\partial_x\). If \(u(x)=\mathbb E_x\tau_{r,\beta}\), its Dirichlet boundary problem is \(L_ru=-1\), \(u(\pm b_{r,\beta})=0\). Reflection symmetry forces \(u'(0)=0\). Multiplying the derivative equation by \(e^{-2V_r(x)}\) and integrating twice yields the exact formula
\[
 u(0)=2\int_0^{b_{r,\beta}} e^{2V_r(z)}\left(\int_0^z e^{-2V_r(y)}\,dy\right)dz.\tag{1}
\]
This representation is classical, not an originality claim. It also proves finiteness of the mean exit time for each bounded positive detection interval.

The well is at \(y=0\). For \(z\) in the growing saddle window \(|z-\sqrt r|\le r^{-3/10}\), and hence in every fixed \(K/\sqrt r\) saddle window, the inner integral in (1) is uniformly
\[
 \int_0^z e^{-ry^2+y^4/2}\,dy =\frac{\sqrt\pi}{2\sqrt r}\bigl(1+O_K(r^{-2})\bigr).\tag{2}
\]
To see this, rescale \(y=s/\sqrt r\), use \(e^{-s^2+s^4/(2r^2)}=e^{-s^2}(1+O(s^4/r^2))\) on \(s\le r^{1/4}\), and bound the remainder beyond this region by exponentially small Gaussian tails. Uniformly for the present growing saddle window, the upper limit in the rescaled inner integral is \(s=r+O(r^{1/5})\). Throughout \(0\le s\le r+B\), the exponent is bounded above by \(-c s^2\) for sufficiently large \(r\), so the tail argument remains uniform. The detection boundary is within a bounded saddle window. Contributions to (1) with outer saddle coordinate \(|t|>r^{1/5}\) are exponentially small relative to the saddle contribution. One may use the exact identity \(2V_r(z)=r^2/2-(r-z^2)^2/2\) to control the tails uniformly.

In the outer integral, set \(z=\sqrt r-t/\sqrt r\). Then \(t\in[-\beta,r]\) and, exactly,
\[
 2V_r(z)=\frac{r^2}{2}-2t^2+\frac{2t^3}{r}-\frac{t^4}{2r^2}.
\]
For \(t\in[0,r]\), the exponent relative to \(r^2/2\) is \(-\frac12(2t-t^2/r)^2\le-t^2/2\); for negative \(t\), its domain is bounded by \(B\). Thus Gaussian domination and Taylor expansion on \(|t|\le r^{1/5}\), with exponentially small remaining tails, imply uniformly for \(|\beta|\le B\),
\[
 \int_0^{b_{r,\beta}}e^{2V_r(z)}dz=\frac{e^{r^2/2}}{\sqrt r}\left[J_0(\beta)+\frac{2J_3(\beta)}r+O_B(r^{-2})\right],\tag{3}
\]
where \(J_0(\beta)=\int_{-\beta}^{\infty}e^{-2t^2}dt=\sqrt{\pi/2}\,\Phi(2\beta)\) and \(J_3(\beta)=\int_{-\beta}^{\infty}t^3e^{-2t^2}dt=e^{-2\beta^2}(\beta^2/4+1/8)\). The discarded part of (1) is negligible because the inner integral is nonnegative and bounded by a Gaussian-well contribution on the relevant interval.

Substituting (2) and (3) into (1), and dividing by \(\pi e^{r^2/2}/(\sqrt2 r)\), gives the displayed theorem. The well expansion starts only at order \(r^{-2}\), so the first correction comes entirely from cubic skewness of the potential in the saddle coordinate.

Finally \(\Phi'(2\beta)=e^{-2\beta^2}/\sqrt{2\pi}\). Taylor expansion shows that replacing \(\beta\) by \(\beta+(\beta^2/2+1/4)/r\) in \(\Phi(2\beta)\) reproduces exactly the new \(r^{-1}\) term, uniformly on any bounded \(\beta\)-interval. This is the finite-barrier shift interpretation.

## Verification
Run `python verify_exit.py` with Python 3, NumPy and SciPy. The script solves the backward boundary-value equation using a second-order finite-difference discretization and separately evaluates the exact double integral by numerical quadrature. It checks agreement for four barrier parameters and three detector offsets, then tests the first correction against additional high-barrier quadratures. The finite checks are corroboration, not a proof of uniform asymptotics.

## Relationship to prior work
Sanders, Kuehn, Hilder and Bastiaansen [1, Appendix A] studied **this same stochastic pitchfork equation and the first-passage time at the unshifted unstable equilibria**, using the same backward-equation integral, and compared the numerical mean with an Eyring–Kramers approximation multiplied by an empirically chosen factor \(0.6\). Their exact integral and their numerical comparison are prior results. The classical Gaussian error-function dependence of a mean first-passage time on a moving detection threshold near a barrier is also explicitly presented by Jungblut and Dellago [2, Sect. 4.3, Eq. (77)], whose source should be credited for that leading profile. Berglund [3] surveys the established Kramers asymptotic framework. None of these inspected materials gives the **specific uniform next-order, offset-dependent coefficient** in the boxed equation. The advance claimed here is deliberately limited to that coefficient and its calibration interpretation.

## Limitations
Only one-dimensional additive unit noise, a cubic subcritical pitchfork, symmetric absorbing thresholds, and fixed bounded detector offset \(\beta\) are treated. This does not establish estimates for offsets growing with \(r\), exit-time distributions or higher moments, general colored noise, or multidimensional dynamics. The full error-function crossover and the saddle factor of one-half are classical and **not** original findings. The source comparison is necessarily non-exhaustive, particularly for older asymptotic expansions of mean-first-passage profiles; historical priority remains provisional. Independent scientific validation has not been performed.

## References
[1] P. A. Sanders, C. Kuehn, B. Hilder and R. Bastiaansen, *Early warning of critical transitions: Distinguishing supercritical and subcritical bifurcations from noisy observations*, arXiv:2610.38866v1 (2026), Appendix A. https://arxiv.org/html/2610.38866v1

[2] S. Jungblut and C. Dellago, *Pathways to self-organization: Crystallization via nucleation and growth*, European Physical Journal E **39**, 77 (2016), Sect. 4.3, Eq. (77), DOI 10.1140/epje/i2016-16077-6. https://doi.org/10.1140/epje/i2016-16077-6

[3] N. Berglund, *Kramers' law: Validity, derivations and generalisations*, arXiv:1106.5799v2 (2013). https://arxiv.org/html/1106.5799v2
