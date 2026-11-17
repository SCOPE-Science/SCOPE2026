# Sharp lower Gabor frame bounds for the Poisson kernel on two interlaced translation grids

## Finding

Fix \(w>0\), and let \(g_w(t)=1/(t^2+w^2)\). For a real offset \(\theta\), consider the indexed Gabor family
\[
\mathcal G_{w,\theta}=\bigl\{e^{2\pi i m t}g_w(t-k),\ e^{2\pi i m t}g_w(t-k-\theta):m,k\in\mathbb Z\bigr\}
\]
in \(L^2(\mathbb R)\). Write \(d=\operatorname{dist}(\theta,\mathbb Z)\in[0,1/2]\). Its *optimal lower frame bound*, with the displayed unnormalized window, is exactly
\[
\boxed{A_w(\theta)=\frac{8\pi^2\sinh^2(\pi w)}{w^2}\,
\frac{\sin^2(\pi d/2)}{[\cosh(2\pi w)+\cos(\pi d)]^2}.}
\]
The family is a frame if and only if \(\theta\notin\mathbb Z\). For every \(w>0\), the sharp lower bound is strictly increasing in \(d\in[0,1/2]\), hence is maximized exactly at \(\theta\equiv1/2\pmod1\). The maximizing bound is
\[
\boxed{A_w(1/2)=\frac{4\pi^2\sinh^2(\pi w)}{w^2\cosh^2(2\pi w)}.}
\]
As \(\theta\to0\) through noninteger offsets, the collapse is quadratic, with sharp coefficient
\[
\boxed{\lim_{\theta\to0}\frac{A_w(\theta)}{\theta^2}=
\frac{\pi^4}{2w^2}\tanh^2(\pi w)\operatorname{sech}^2(\pi w).}
\]
The same expansion applies near any integer offset. These statements concern the *lower* bound; no formula for the optimal upper bound or condition-number minimization is asserted.

## Assumptions and scope

The Fourier convention is \(\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-2\pi i t\xi}\,dt\). Translations are \(T_a f(t)=f(t-a)\); modulations are \(M_mf(t)=e^{2\pi i m t}f(t)\). The family has two translation cosets \(\mathbb Z\cup(\mathbb Z+\theta)\) and the *integer* modulation grid; it is not the semi-regular frequency-coset family. Duplicate vectors at integral offsets are harmless to the non-frame assertion, whether retained as indexed terms or deduplicated. No normalizing factor is applied to \(g_w\). Parameters \(w>0\) and \(\theta\in\mathbb R\) are arbitrary, and all bounds are in the standard squared Hilbert norm convention.

## Proof

**1. Zak diagonalization.** Define \(Zf(x,\nu)=\sum_{k\in\mathbb Z}f(x+k)e^{-2\pi i k\nu}\), with \(x,\nu\in[0,1)\). This is unitary from \(L^2(\mathbb R)\) to \(L^2([0,1)^2)\). For integer time and frequency shifts, the Zak images are the product of \(Zg\) and the standard two-dimensional Fourier characters (up to unimodular constants). Parseval therefore gives, for every \(f\in L^2(\mathbb R)\),
\[
\sum_{m,k\in\mathbb Z}\Bigl(|\langle f,M_mT_k g_w\rangle|^2+|\langle f,M_mT_{k+\theta}g_w\rangle|^2\Bigr)
=\int_{[0,1)^2}|Zf(x,\nu)|^2F_{w,\theta}(x,\nu)\,dx\,d\nu,
\]
where \(F_{w,\theta}(x,\nu)=|Zg_w(x,\nu)|^2+|Zg_w(x-\theta,\nu)|^2\). Thus the sharp lower frame bound is the essential infimum of \(F_{w,\theta}\), and the upper bound is finite because the Zak series converges uniformly for fixed \(w\).

**2. Exact frequency minimization.** The Fourier transform of \(g_w\) equals \((\pi/w)e^{-2\pi w|\xi|}\). Put \(r=e^{-2\pi w}\), \(z=e^{2\pi ix}\), and \(D=1+r^2-2r\cos(2\pi x)>0\). Poisson summation and two geometric series give, for \(0<\nu<1\),
\[
Zg_w(x,\nu)=\frac\pi w e^{2\pi i\nu x}\left[\frac{r^\nu}{1-rz}+\frac{r^{1-\nu}}{z-r}\right].
\]
Set \(a=r^\nu\), \(b=r^{1-\nu}\), \(P=a-rb\), \(Q=b-ra\); then \(ab=r\). Taking absolute squares gives
\[
|Zg_w(x,\nu)|^2=\left(\frac\pi w\right)^2\frac{D(a^2+b^2)-4r^2+2r(1+r^2)\cos(2\pi x)}{D^2}.
\]
The only \(\nu\)-dependent term has *strictly positive* coefficient \(1/D\), and \(r^{2\nu}+r^{2(1-\nu)}\) has its unique minimum on the frequency circle at \(\nu=1/2\). Hence, simultaneously for every \(x\), both summands in \(F_{w,\theta}\) attain their frequency minimum at \(\nu=1/2\). Consequently the infimum over \(x,\nu\) equals the minimum over \(x\) at \(\nu=1/2\).

**3. Sharp spatial minimization.** Substitution at \(\nu=1/2\) yields
\[
|Zg_w(x,1/2)|^2=\frac{4\pi^2\sinh^2(\pi w)}{w^2}\,
\frac{\cos^2(\pi x)}{[\cosh(2\pi w)-\cos(2\pi x)]^2}.
\]
Write \(y=x-1/2\), \(\beta=\cosh(2\pi w)>1\), \(K=4\pi^2\sinh^2(\pi w)/w^2\), and
\[
\varphi(t)=\frac{t}{(\beta+1-2t)^2},\qquad 0\le t\le1.
\]
Then \(|Zg_w(x,1/2)|^2=K\varphi(\sin^2(\pi y))\). The derivatives
\[
\varphi'(t)=\frac{\beta+1+2t}{(\beta+1-2t)^3}>0,\qquad
\varphi''(t)=\frac{8(\beta+1+t)}{(\beta+1-2t)^4}>0
\]
show strict increase and strict convexity on the whole interval. Quasiperiodicity of the Zak modulus and the symmetry between the two cosets reduce to \(\theta=d\in[0,1/2]\). Put \(u=\sin^2(\pi y)\) and \(v=\sin^2(\pi(y-d))\). The identity
\[
u+v=1-\cos(\pi d)\cos(2\pi y-\pi d)\ge1-\cos(\pi d)=2\sin^2(\pi d/2)
\]
and Jensen's inequality imply
\[
\varphi(u)+\varphi(v)\ge2\varphi\left(\frac{u+v}{2}\right)
\ge2\varphi\bigl(\sin^2(\pi d/2)\bigr).
\]
Equality occurs at \(y=d/2\) (modulo one); at \(d=1/2\), also at \(y=d/2+1/2\) (modulo one). Substituting \(\beta+1-2\sin^2(\pi d/2)=\beta+\cos(\pi d)\) proves the exact displayed formula for \(A_w(\theta)\), including attainability rather than a mere lower estimate.

**4. Frame criterion, optimum, and limit.** The formula vanishes precisely for integral \(\theta\); otherwise it is strictly positive, while the upper bound is finite by Step 1. On \(d\in[0,1/2]\), the numerator \(\sin^2(\pi d/2)\) increases strictly and the positive denominator \(\beta+\cos(\pi d)\) decreases strictly. This proves the unique modulo-one optimizer \(d=1/2\). Taylor expansion at \(d=0\) and \(\beta+1=2\cosh^2(\pi w)\) give the sharp quadratic coefficient. No limiting interchange or numerical extrapolation is needed.

## Verification

The standalone `CHECK.py` checks the rational Zak identity and convexity derivatives symbolically; compares the closed Zak transform with 4,001-point-side partial Fourier/Zak sums; checks the sharp inequality and equality over multiple window widths and offsets; performs independent global numerical minimizations; and compares the small-offset quotient with its analytic limit. Run `python CHECK.py` with `numpy`, `scipy`, and `sympy` installed. These computations are finite consistency checks. Every universal statement follows from the preceding exact Poisson summation, elementary inequalities and Fourier/Zak Parseval identities, not from grid enumeration.

## Relationship to prior work

Belov and Semenov, *Irregular Gabor Frames for the Poisson Kernel* (arXiv:2610.30037, first posted 2026-10-21), establish a qualitative criterion for frequency-irregular systems \(M\times\alpha\mathbb Z\) and explicitly distinguish the unresolved *opposite orientation* \(\alpha\mathbb Z\times M\). The present theorem handles that opposite orientation for the two-coset translation set \(M=\mathbb Z\cup(\mathbb Z+\theta)\) at integer modulation frequencies; moreover it computes the exact *sharp* lower bound and optimizes the coset offset. The result is not asserted to solve the general orientation problem.

Kloos and Stöckler (arXiv:1311.7359) treat totally positive generators, Zak zeros, and lower bounds for **regular rectangular lattices** (including two-sided exponentials, Fourier-related to the present Poisson window). Those statements do not imply the entire nonlattice offset profile or the unique minimax offset. Janssen (2003) discusses critical-density Zak zeros and tight-window constructions, not this two-coset sharp lower bound. Standard Zak diagonalization is background rather than claimed novelty. Fourier duality with two-sided exponentials is an important equivalence to check; it does not alone transfer regular-lattice frame-bound formulas to arbitrary noninteger two-coset offsets.

## Limitations

Only the two-translation-coset / integer-modulation geometry is treated. The optimal upper frame bound is finite but not evaluated, and nothing is claimed about optimal condition numbers or general irregular sets. The quantitative result is new relative to the cited and inspected material, not independently certified as a publication-priority fact; a differently normalized equivalent computation could exist in older filter-bank literature. All calculations use the unnormalized Poisson window and squared-norm frame conventions.

## References

1. Y. Belov and A. V. Semenov, *Irregular Gabor Frames for the Poisson Kernel*, arXiv:2610.30037v1 (2026-10-21), https://arxiv.org/abs/2610.30037 .
2. T. Kloos and J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359 (2013-11-28), https://arxiv.org/abs/1311.7359 .
3. A. J. E. M. Janssen, *On generating tight Gabor frames at critical density*, Journal of Fourier Analysis and Applications 9 (2003), 175–214, DOI:10.1007/s00041-003-0011-3.
4. Standard Zak-transform Parseval representation for integer Gabor shifts, as discussed in the references above.
