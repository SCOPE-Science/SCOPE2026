# A unique warming-mismatch threshold for the value of thermal refugia under symmetric dispersal

## Finding

**Theorem (complete comparison with homogenization).** Consider two equally sized habitat patches whose temperatures differ by a fixed, symmetric offset, and a continuous-time, low-density population with symmetric per-capita movement. Assume a Gaussian thermal performance curve. Write \(a>0\) for the temperature half-contrast divided by thermal niche width, \(x\geq0\) for the absolute mismatch of the mean temperature from the niche optimum divided by that width, \(R>0\) for peak gross growth, \(\mu\geq0\) for common loss, and \(m>0\) for the migration rate in either direction. Let \(\Lambda_{\rm het}(a,x,R,\mu,m)\) be the dominant exponential growth exponent of the heterogeneous two-patch system and \(\Lambda_{\rm hom}(x,R,\mu)\) that of two homogeneous patches at the common mean temperature.

Define
\[
 x_1=\frac a2,\qquad
 x_2=\frac1a\operatorname{arcosh}\!\left(e^{a^2/2}\right).
\]
Then \(0<x_1<x_2\). For **every** fixed \(a,R,\mu,m\) satisfying the stated conditions, there is exactly one \(x_*(a,R,m)\in(x_1,x_2)\) such that
\[
\Lambda_{\rm het}<\Lambda_{\rm hom}\quad(0\le x<x_*),\qquad
\Lambda_{\rm het}=\Lambda_{\rm hom}\quad(x=x_*),\qquad
\Lambda_{\rm het}>\Lambda_{\rm hom}\quad(x>x_*).
\]
The equality is transversal, the threshold \(x_*\) is strictly increasing in \(m/R\), and it is independent of the common loss \(\mu\). Its limits and first-order laws are
\[
\lim_{m\downarrow0}x_*=x_1,\qquad
 x_*=\frac a2+\frac{e^{a^2/8}}{Ra}m+O(m^2),
\]
\[
\lim_{m\to\infty}x_*=x_2,\qquad
 x_2-x_*\sim\frac{R e^{-x_2^2/2}\sqrt{1-e^{-a^2}}}{2am}.
\]
In the intermediate mismatch range \(x_1<x<x_2\), there is equivalently exactly one critical movement rate \(M_a(x)>0\): heterogeneous habitat is better for \(0<m<M_a(x)\), equal at \(m=M_a(x)\), and worse for \(m>M_a(x)\). The explicit rate is
\[
M_a(x)=\frac{R e^{-x^2/2}\left(2e^{-a^2/2}\cosh(ax)-1-e^{-a^2}\right)}{2\left(1-e^{-a^2/2}\cosh(ax)\right)}.
\]
It increases strictly from zero to infinity as \(x\) traverses \((x_1,x_2)\). Thus the equation \(M_a(x_*)=m\) characterizes the unique threshold without any numerical search over population trajectories.

## Assumptions and scope

Fix thermal niche optimum \(\theta\in\mathbb R\), thermal scale \(\sigma>0\), and actual habitat temperatures \(\bar T\pm h\) with \(h>0\). Put \(a=h/\sigma\) and \(x=|\bar T-\theta|/\sigma\). The local gross growth response is precisely \(R\exp[-(T-\theta)^2/(2\sigma^2)]\), with a common constant loss \(\mu\). Assuming nonnegative patch abundances \(n_+,n_-\), the linear population dynamics are
\[
\frac{d}{dt}\begin{pmatrix}n_+\\ n_-\end{pmatrix}=
\begin{pmatrix}
R e^{-(x-a)^2/2}-\mu-m&m\\
m&R e^{-(x+a)^2/2}-\mu-m
\end{pmatrix}\begin{pmatrix}n_+\\ n_-\end{pmatrix}.
\]
The comparison replaces the two local temperatures by their common mean, without changing \(R,\mu,m\), patch sizes or population accounting. For every strictly positive initial total abundance, the long-run total abundance exponent is the Perron eigenvalue (the matrix is irreducible and Metzler). This is a comparison of **low-density long-run growth exponents**, not of nonlinear carrying capacity, finite-time abundance, ecological persistence under environmental randomness, or a measured field response.

## Proof

Put \(p=e^{-a^2/2}\in(0,1)\), \(q=e^{-x^2/2}\), \(v=ax\), and \(G=Rq\). Local gross growth rates are \(Gpe^v\) and \(Gpe^{-v}\). Direct diagonalization gives
\[
\Lambda_{\rm hom}=G-\mu,\qquad
\Lambda_{\rm het}=Gp\cosh v-\mu-m+\sqrt{m^2+G^2p^2\sinh^2v}.
\tag{1}
\]
The common loss cancels from the difference. Since \(G>0\), it suffices to compare the displayed growth terms.

If \(0\leq x\leq a/2\), the better heterogeneous patch has gross growth \(Gpe^{ax}\leq G\), and the other has strictly less. For \(m>0\), strict Perron comparison with the homogeneous irreducible movement matrix gives \(\Lambda_{\rm het}<\Lambda_{\rm hom}\). Alternatively, apply the Rayleigh variational principle to (1). The strict inequality includes both endpoints \(x=0\) and \(x=a/2\).

The heterogeneous *mean* gross growth equals \(Gp\cosh(ax)\). It is at least the homogeneous value exactly when \(x\geq x_2\), with \(x_2\) as above. At such \(x>0\) the habitat contrast is nonzero and the square root in (1) strictly exceeds \(m\). Therefore \(\Lambda_{\rm het}>\Lambda_{\rm hom}\) for every finite \(m>0\) and \(x\ge x_2\). Also \(x_2>a/2\) because \(p\cosh(a^2/2)=(1+p^2)/2<1\).

For \(a/2<x<x_2\), one patch has gross growth above \(G\), the other below \(G\), and the arithmetic mean is below \(G\). With \(x\) fixed, the eigenvalue in (1) is strictly decreasing in \(m\) because its derivative is \(-1+m/\sqrt{m^2+G^2p^2\sinh^2v}<0\). As \(m\downarrow0\) it tends to the better patch's rate, which exceeds \(G-\mu\); as \(m\to\infty\) it tends to the arithmetic-mean rate, which is below \(G-\mu\). Hence there is one and only one critical \(m\). Solving equality in (1) after a valid squaring (both sides \(m+G(1-p\cosh v)>0\)) gives precisely \(M_a(x)\) above. Its numerator and denominator are positive throughout this interval.

It remains to prove that critical migration strictly increases with mismatch; without this step, the single-crossing statement at fixed \(m\) would not follow. Write
\[
h(x)=1-p\cosh(ax)>0,\qquad
 g(x)=\frac{1-p^2}{2h(x)}-1,
\qquad M_a(x)=R e^{-x^2/2}g(x).
\]
Then
\[
\frac{M_a'(x)}{R e^{-x^2/2}}=
 x+\frac{1-p^2}{2h(x)^2}\left(ap\sinh(ax)-xh(x)\right).
\tag{2}
\]
For \(x\ge a/2\), the bracket is strictly positive. Indeed \(ap\sinh(ax)/x\) is strictly increasing for \(x>0\), whereas \(h(x)\) is strictly decreasing, and at \(x=a/2\) their values are respectively \(1-p^2\) and \((1-p^2)/2\). Thus (2) is strictly positive throughout the intermediate interval. Direct endpoint evaluation gives \(M_a(a/2+)=0\) and \(M_a(x_2-)=+\infty\). Consequently, for every \(m>0\), \(M_a(x)=m\) has exactly one solution, and the earlier three cases yield the asserted sign on either side. Since \(M_a'>0\) and the growth-rate difference is strictly decreasing in \(m\) at equality, the crossing in \(x\) is transversal. Strict dependence on \(m/R\) follows from the normalized expression for \(M_a/R\).

For the endpoint expansions, differentiating the explicit expression gives \(M_a'(a/2+)=Ra e^{-a^2/8}\). Local inverse-function expansion yields the stated small-migration law. At \(x_2\), the identity \(p\cosh(ax_2)=1\) implies \(p\sinh(ax_2)=\sqrt{1-p^2}\), so
\[
M_a(x)\sim \frac{R e^{-x_2^2/2}\sqrt{1-p^2}}{2a(x_2-x)}\quad(x\uparrow x_2).
\]
Inversion proves the large-migration law. Every argument is analytic and applies to the full claimed parameter domain.

## Verification

A standalone, standard-library-only Python script `checker.py` performs deterministic randomized parameter checks of both comparison signs, computes critical mismatch by bisection, tests strict increase of the critical movement curve and checks both asymptotic coefficients. It reports **23,712 supplementary assertions passed** with its fixed seed. The script uses direct spectral formulas rather than simulated population trajectories. These finite checks are diagnostic only; the proof above establishes the universal statements.

For a dimensionless illustration with \(a=R=1\), \(m=0.1\), and arbitrary common \(\mu\), the unique critical mismatch is approximately \(x_*=0.596489536\), between \(x_1=0.5\) and \(x_2\approx1.085038502\). The heterogeneous exponent is below the homogeneous one at \(x=0.55\), above it at \(x=0.7\), and equal only at the interior threshold.

## Relationship to prior work

Backus, Clements and Baskett (2024) study restoring spatial climate heterogeneity with stochastic, density-dependent metapopulation simulations. Their results motivate this deliberately simpler analytical benchmark, but the paper does not give a two-patch Gaussian low-density Perron comparison, its unique warming-mismatch threshold, or its two migration asymptotics. Amarasekare (2024) models temperature-dependent emigration, transit survival and settlement over a spatial habitat array, rather than symmetric temperature-independent movement with a paired homogenization control. Grumbach and colleagues (2023) give dispersal-response classifications for nonlinear equilibrium total population size, rather than the dominant growth exponent and warming comparison here. Analytic spectral and reduction-principle ideas are classical tools and are not claimed as new in isolation. Related range-shift analysis by Terry, O'Sullivan and Rossberg (2023) concerns moving environmental envelopes in reaction-diffusion systems and does not, on accessible material, assert this finite-patch comparison; incomplete full-text access is a priority risk.

## Limitations

This is an idealized two-patch, symmetric-Gaussian, constant-rate, density-free and time-independent calculation. Backus and colleagues use a skew-normal performance response and more complex dispersal and climate trajectories, so the numerical thresholds should not be transferred to their simulation or to field restoration without deriving new results. Both heterogeneous and homogeneous growth exponents may be negative, and a positive difference is **not** proof of absolute persistence. In the far-mismatch regime, both growth benefits above the shared loss can be small in absolute terms even though their comparison has a strict sign. No empirical calibration, finite-population extinction inference or asymmetric-migration extension follows from the theorem.

## References

1. Backus, G. A., Clements, C. F., and Baskett, M. L. (2024). *Restoring spatiotemporal variability to enhance the capacity for dispersal-limited species to track climate change*. Ecology 105, e4257. First published 2024-03-01. https://doi.org/10.1002/ecy.4257
2. Amarasekare, P. (2024). *Temperature-dependent dispersal and ectotherm species' distributions in a warming world*. Journal of Animal Ecology 93, 428–446. First published 2024-02-26. https://doi.org/10.1111/1365-2656.14054
3. Grumbach, C., Reurik, F. N., Segura, J., Franco, D., and Hilker, F. M. (2023). *The effect of dispersal on asymptotic total population size in discrete- and continuous-time two-patch models*. Journal of Mathematical Biology 87, 60. https://doi.org/10.1007/s00285-023-01984-8
4. Terry, J. C. D., O'Sullivan, J. D., and Rossberg, A. G. (2023). *Schrödinger's Range-Shifting Cat: How Skewed Temperature Dependence Impacts Persistence with Climate Change*. The American Naturalist 203, 161–173. https://doi.org/10.1086/728002
