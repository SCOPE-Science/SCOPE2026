# A sharp saturation threshold for bounded-diffusivity first-passage design

## Finding

Consider a one-dimensional, zero-drift Itô diffusion that starts at its reflecting left endpoint and is absorbed at its right endpoint. Suppose the diffusivity has a fixed spatial mean and two strict physical bounds. Its **unique** mean-first-passage-minimizing profile has a square-root interior, a lower-saturation layer adjacent to the absorbing endpoint, and an upper-saturation layer at the reflecting endpoint if and only if the mean exceeds a sharp threshold. The optimal first-passage value is twice continuously differentiable but not three times differentiable at that threshold.

In dimensionless coordinates, fix \(0<\ell<m<u<\infty\), impose \(\ell\le D(x)\le u\) almost everywhere and \(\int_0^1D(x)\,dx=m\), and let \(\tau\) be the first arrival at \(1\) starting from reflecting \(0\). Set
\[
m_c=\frac{2u}{3}+\frac{\ell^3}{3u^2}.
\]
There is a unique \(c>\ell\) satisfying \(\int_0^1\min\{u,\max\{\ell,c\sqrt{1-x}\}\}\,dx=m\), and the unique optimal profile up to equality almost everywhere is
\[
D_*(x)=\min\{u,\max\{\ell,c\sqrt{1-x}\}\}.
\]
For \(\ell<m\le m_c\), \(c\in(\ell,u]\) is the unique solution of
\[
3m=2c+\frac{\ell^3}{c^2},\qquad
\mathbb E\tau_{\min}=\frac{2}{3c}-\frac{\ell^3}{6c^4}.
\]
For \(m_c<m<u\),
\[
c^2=\frac{u^3-\ell^3}{3(u-m)},\qquad
\mathbb E\tau_{\min}=\frac{1}{2u}+\frac{3(u-m)^2}{2(u^3-\ell^3)}.
\]
The lower saturated layer always has length \(\ell^2/c^2\); the upper saturated layer has length \(\max\{0,1-u^2/c^2\}\). Consequently a genuinely **three-region** optimum occurs precisely for \(m>m_c\), with the two saturated regions separated by an unsaturated square-root region. At \(m=m_c\), the upper layer first appears with zero length.

As a function of \(m\), the minimum \(F(m)=\mathbb E\tau_{\min}\) belongs to \(C^2((\ell,u))\) and has a nonzero jump in its third derivative at \(m=m_c\):
\[
F'''(m_c^-)= -\frac{27u^5}{2(u^3-\ell^3)^3},\qquad
F'''(m_c^+)=0.
\]
The term *transition* here describes a change of an optimization active set, not a thermodynamic singularity.

## Assumptions and scope

A spatial interval \([0,1]\), a reflecting boundary at \(0\), and an absorbing boundary at \(1\) are fixed. The particle starts at \(0\), and its generator is \((\mathcal L f)(x)=D(x)f''(x)\), the Itô prescription with zero drift. The diffusivity is Borel measurable, essentially bounded, and uniformly positive, with the prescribed \(\ell,m,u\). For smooth \(D\), the process solves \(dX_t=\sqrt{2D(X_t)}\,dW_t\) with reflection at \(0\); for general measurable \(D\) it is the regular natural-scale diffusion with speed density \(1/D\). The classical mean-time equation remains valid in its absolutely continuous weak sense. Admissible profiles are identified up to Lebesgue-almost-everywhere equality. There is no other drift, resetting, diffusivity-gradient force, kinetic interpretation, or reactive boundary.

For an interval \([0,L]\), the formulas above give \(\mathbb E\tau_{\min}/L^2\) when \(m,\ell,u\) retain physical diffusivity units and \(D(Lx)\) is used in the normalized profile.

## Proof

**1. First-passage functional.** Let \(T_D(z)=\mathbb E_z\tau\). The reflecting-absorbing backward equation is \(D(z)T_D''(z)=-1\) almost everywhere with \(T_D'(0)=0\) and \(T_D(1)=0\). Thus \(T_D'(z)=-\int_0^z D(y)^{-1}\,dy\), and Fubini gives
\[
T_D(0)=\int_0^1\frac{1-x}{D(x)}\,dx.
\]
Uniform ellipticity ensures finiteness and justifies this derivation by approximation for measurable coefficients.

**2. A global pointwise certificate.** For every \(c>0\), consider the strictly convex function \(g_x(d)=(1-x)/d+d/c^2\) on \([\ell,u]\) for \(0\le x<1\). Its unique minimizer is \(d_c(x)=\min\{u,\max\{\ell,c\sqrt{1-x}\}\}\). Therefore, for every admissible \(D\),
\[
\int_0^1\frac{1-x}{D(x)}\,dx+\frac{m}{c^2}
\ge\int_0^1\frac{1-x}{d_c(x)}\,dx+\frac{1}{c^2}\int_0^1d_c(x)\,dx.
\]
If \(c\) makes \(\int d_c=m\), the budget terms cancel. The strict convexity for almost every \(x\) proves uniqueness almost everywhere. The map \(c\mapsto\int d_c\) is continuous, strictly increasing on the region with mean in \((\ell,u)\), from \(\ell\) to \(u\), so such \(c\) exists uniquely.

**3. Exact branches.** Under \(c\le u\), the unsaturated interval ends at \(x=1-\ell^2/c^2\). Direct integration gives
\[
m=\frac{2c}{3}+\frac{\ell^3}{3c^2},\quad F=\frac{2}{3c}-\frac{\ell^3}{6c^4}.
\]
The first expression is strictly increasing for \(c>\ell\), since its derivative is \(\frac23(1-\ell^3/c^3)>0\). At \(c=u\) it attains \(m_c\). Under \(c>u\), splitting at \(x=1-u^2/c^2\) and \(x=1-\ell^2/c^2\) yields
\[
m=u-\frac{u^3-\ell^3}{3c^2},\quad F=\frac1{2u}+\frac{u^3-\ell^3}{6c^4}.
\]
Eliminating \(c\) gives the stated second branch. Both expressions agree at \(c=u\); the two-layer structure is exhaustive because \(d_c\) is monotone decreasing.

**4. Differentiability classification.** Differentiating either parametric branch gives \(F'(m)=-c^{-2}\). The second derivatives are
\[
F''(m)=\begin{cases}
\dfrac{3}{c^3-\ell^3},&\ell<m<m_c,\\
\dfrac{3}{u^3-\ell^3},&m_c<m<u.
\end{cases}
\]
The values of \(F,F',F''\) match at \(c=u\). On the lower branch, \(dc/dm=\frac{3c^3}{2(c^3-\ell^3)}\), and so \(F'''=-\frac{27c^5}{2(c^3-\ell^3)^3}\). On the upper branch \(F''\) is constant, giving \(F'''=0\). Since \(\ell<u\), the one-sided third derivatives differ, proving exactly \(C^2\) and not \(C^3\) across the threshold.

## Verification

The accompanying `checker.py` independently checks algebraic branch identities and derivative transitions with exact symbolic computation, evaluates the first-passage and budget integrals with break-point-aware numerical quadrature, and compares the analytic profile with independently optimized discretizations under both hard bounds. The mathematical proof does not rely on finite numerical sampling.

For \(\ell=0.5\), \(u=1.5\), \(m=1.2\), the threshold is \(m_c=1.0185185185\ldots\); the optimal mean time is \(0.37487179487\ldots\), compared with \(0.41666666667\ldots\) for homogeneous diffusivity. The upper, intermediate, and lower regions occupy respectively \(0.3769230769\ldots\), \(0.5538461538\ldots\), and \(0.0692307692\ldots\) of the interval.

## Relationship to prior work

Menon (2026), arXiv:2611.17470v1, proves the unconstrained fixed-spatial-average optimization for an arbitrary stochastic prescription and derives the one-dimensional unbounded Itô square-root optimum \(D(x)=\frac{3m}{2}\sqrt{1-x}\). It also uses a numerical positivity floor in discretized optimization. The present result **credits** that variational structure and asks a different practical question: simultaneous prescribed nonzero pointwise floor and finite ceiling. The exact cap-activation threshold, three-region solution, piecewise exact optimal value, and \(C^2\)-but-not-\(C^3\) active-set transition are not established by the unconstrained result or its numerical floor.

Menon, dos Santos and Anteneodo (2023), arXiv:2311.00818v1, derive first-passage and efficiency formulas for general diffusivity, including the Itô-weighted integral. They compare heterogeneous examples rather than classify two-sided constrained global optimal designs. Tung and Lawley (2025), arXiv:2512.19646v1, treat escape in general heterogeneous domains with small targets; their principal problem is not the finite-contrast allocation of diffusivity in this reflecting-absorbing interval. These comparisons do not establish bibliographic uniqueness.

## Limitations

The result optimizes mean absorption time, not higher moments, extreme-arrival statistics, or a full stochastic trajectory order. The claimed \(C^2\) regularity concerns variation in the *mean-diffusivity budget* at fixed floor and ceiling, not a physical phase transition. The optimizer is not claimed for higher dimensions, interior start positions, or non-Itô prescriptions. Possible equivalent constrained-design treatments outside indexed searches remain a publication-priority risk. No independent scientific audit is asserted.

## References

1. L. Menon, *Optimal heterogeneous diffusivity profiles for mean first-passage minimization*, arXiv:2611.17470v1 (first public 12 November 2026). https://arxiv.org/html/2611.17470v1
2. L. Menon Jr., M. A. F. dos Santos and C. Anteneodo, *Random-search efficiency in a bounded interval with spatially heterogeneous diffusion coefficient*, arXiv:2311.00818v1 (1 November 2023). https://arxiv.org/pdf/2311.00818
3. H.-R. Tung and S. D. Lawley, *Escape from heterogeneous diffusion*, arXiv:2512.19646v1 (22 December 2025). https://arxiv.org/abs/2512.19646
