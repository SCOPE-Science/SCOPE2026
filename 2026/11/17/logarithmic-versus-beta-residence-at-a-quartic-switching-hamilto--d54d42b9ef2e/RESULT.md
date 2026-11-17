# Logarithmic versus beta residence at a quartic switching Hamiltonian center

## Finding

A nondegenerate global center can have two quartic Hamiltonian halves with radically different high-energy dynamics. Fix real \(a,b>0\), set
\[
H(x,y)=\begin{cases}
\tfrac12(x^2+y^2)+a x^2y^2,&y\geq0,\\
\tfrac12(x^2+y^2)+b y^4,&y<0,
\end{cases}
\qquad (\dot x,\dot y)=(-\partial_yH,\partial_xH).
\]
For every \(E>0\), its level \(\Gamma_E=\{H=E\}\) is a periodic orbit. Write \(T_\pm(E)\) for the **original-time** residence in the upper and lower half-planes, and \(A_\pm(E)\) for the Euclidean areas of the corresponding portions of \(\{H\leq E\}\). Define
\[
B_1=B(\tfrac14,\tfrac12),\qquad B_2=B(\tfrac14,\tfrac32),
\]
where \(B\) denotes Euler's beta function. As \(E\to\infty\),
\[
\begin{aligned}
T_+(E)&\sim\frac{\log E}{2\sqrt{aE}},&
A_+(E)&\sim\sqrt{\frac Ea}\log E,\\
T_-(E)&\sim\frac{\sqrt2 B_1}{4b^{1/4}}E^{-1/4},&
A_-(E)&\sim\frac{\sqrt2 B_2}{2b^{1/4}}E^{3/4}.
\end{aligned}
\]
Consequently the upper half has a vanishing, but logarithmically enhanced, fraction of the full period and area:
\[
\begin{aligned}
\frac{T_+}{T_++T_-}&\sim
\frac{\sqrt2\,b^{1/4}}{\sqrt a\,B_1}\,E^{-1/4}\log E,\\
\frac{A_+}{A_++A_-}&\sim
\frac{\sqrt2\,b^{1/4}}{\sqrt a\,B_2}\,E^{-1/4}\log E.
\end{aligned}
\]
Their **relative sampling bias** has the universal parameter-independent limit
\[
\boxed{\lim_{E\to\infty}
\frac{T_+/(T_++T_-)}{A_+/(A_++A_-)}=\frac23.}
\]
The associated conditional spatial laws are also sharp. Let \(Y=|y|\) be sampled either from uniform physical time on \(\Gamma_E\), conditioned on the indicated half-plane, or from uniform area in \(\{H\le E\}\), similarly conditioned. For upper-half sampling, both laws of
\[
W_E=\min\!\left\{1,\max\!\left\{0,\frac{2\log Y}{\log E}\right\}\right\}
\]
converge weakly to \(\operatorname{Uniform}[0,1]\). For lower-half sampling, if \(u(E)>0\) is the solution of \(u^2+2bu^4=2E\), then \((Y/u(E))^4\) converges respectively to \(\operatorname{Beta}(1/4,1/2)\) under physical time and to \(\operatorname{Beta}(1/4,3/2)\) under area.

## Assumptions and scope

All statements hold for every fixed pair \(a,b>0\); no smallness or analyticity across the switching line is assumed. The vector field is continuous and locally Lipschitz, with the two polynomial expressions joined on \(y=0\). The orbit energy \(E\) is the common first integral, and the large-energy limit is taken with \(a,b\) held fixed. \(T_\pm\) are times, not reparameterized angular lengths. The two area measures refer to interiors, not arclength on the orbit. Both conditional laws are defined only after conditioning on the named half-plane. The exponentiation by \(4\) in the lower variables is part of the distribution statement. The upper logarithmic statistic \(W_E\) is defined for \(E>1\), and its value at \(Y=0\) is set to \(0\); this event has zero mass under both relevant sampling measures.

## Proof

**Global periodic levels and their clocks.** Both Hamiltonians coincide on \(y=0\), where \(H(x,0)=x^2/2\) and the vector field is \((0,x)\) from either side. The global \(H\) is continuously differentiable, coercive, and increases strictly along every ray from the origin: its quadratic part is positive and each quartic part is nonnegative. Its gradient is zero only at the origin. Thus each \(E>0\) is a single compact regular oval meeting the switching line at \((\pm\sqrt{2E},0)\). Uniqueness and nonzero tangential speed imply a single periodic orbit covering this oval in finite time. Since the flow is Hamiltonian with the same positive energy coordinate on both sides, differentiating the enclosed-area integrals gives the exact identities \(A_+'(E)=T_+(E)\) and \(A_-'(E)=T_-(E)\).

**Exact upper quadratures.** On the upper half of the energy curve,
\[
x^2=\frac{2E-y^2}{1+2ay^2},\qquad
|\dot y|=\sqrt{(2E-y^2)(1+2ay^2)},\qquad 0\le y\le\sqrt{2E}.
\]
Both the ascending and descending branches contribute, so
\[
T_+=2\int_0^{\sqrt{2E}}\frac{dy}{\sqrt{(2E-y^2)(1+2ay^2)}}
=2K(-4aE),
\]
where \(K(m)=\int_0^{\pi/2}(1-m\sin^2\phi)^{-1/2}\,d\phi\). Likewise, using both horizontal sides of each interior slice,
\[
A_+=2\int_0^{\sqrt{2E}}\sqrt{\frac{2E-y^2}{1+2ay^2}}\,dy
=4E\left[\left(1+\frac1{4aE}\right)K(-4aE)-\frac{\mathsf E(-4aE)}{4aE}\right],
\]
where \(\mathsf E(m)=\int_0^{\pi/2}\sqrt{1-m\sin^2\phi}\,d\phi\) is the complete elliptic integral of the second kind. For \(m\to\infty\), the classical complementary-parameter transformation and near-one expansion give
\[
K(-m)=m^{-1/2}\left[\log(4\sqrt m)+O\left(\frac{\log m}{m}\right)\right],
\quad
\mathsf E(-m)=\sqrt m\left[1+O\left(\frac{\log m}{m}\right)\right].
\]
It follows more precisely that
\[
\begin{aligned}
T_+(E)&=\frac1{\sqrt{aE}}\left[\log(8\sqrt{aE})+O\left(\frac{\log E}{E}\right)\right],\\
A_+(E)&=2\sqrt{\frac Ea}\left[\log(8\sqrt{aE})-1+O\left(\frac{\log E}{E}\right)\right].
\end{aligned}
\]
The leading logarithmic constants in the finding follow.

**Lower quadratures and beta constants.** Let \(u=u(E)\) be defined above. The lower half has \(x^2=2E-y^2-2by^4\), and hence
\[
T_-=2\int_0^u\frac{dy}{\sqrt{2E-y^2-2by^4}},\qquad
A_-=2\int_0^u\sqrt{2E-y^2-2by^4}\,dy.
\]
As \(E\to\infty\), \(u\sim(E/b)^{1/4}\) and \(u^2/(2E)\to0\). On setting \(y=uz\), the normalized radicand tends to \(1-z^4\). The time integrand is dominated by \((1-z^2)^{-1/2}\), while the area integrand is bounded by \(1\); dominated convergence applies on \([0,1]\). Using
\[
\int_0^1(1-z^4)^{-1/2}\,dz=\frac{B_1}{4},\qquad
\int_0^1(1-z^4)^{1/2}\,dz=\frac{B_2}{4},
\]
yields precisely the displayed lower asymptotics. The beta identity \(B_2/B_1=2/3\) then gives the relative sampling-bias constant.

**Conditional laws.** For \(0<v<1\), the upper time mass below \(Y=E^{v/2}\) is
\[
2\int_0^{E^{v/2}}\frac{dy}{\sqrt{(2E-y^2)(1+2ay^2)}}
\sim\frac{v\log E}{2\sqrt{aE}}.
\]
The upper area mass below the same cutoff is similarly
\[
2\int_0^{E^{v/2}}\sqrt{\frac{2E-y^2}{1+2ay^2}}\,dy
\sim v\sqrt{\frac Ea}\log E.
\]
After division by their respective totals the probabilities tend to \(v\), establishing the upper uniform log-coordinate limits, including endpoints by monotonicity. Under the lower change of variable \(z=y/u(E)\) the conditional time density tends to a normalized \((1-z^4)^{-1/2}\) density, and the conditional area density tends to a normalized \((1-z^4)^{1/2}\) density. The change \(s=z^4\) supplies the two asserted beta distributions.

## Verification

The standalone `check.py` reconstructs both original conserved Hamiltonians symbolically, tests continuity of energy at the switch, compares the upper elliptic representations with independent quadratures, checks \(A_\pm'(E)=T_\pm(E)\), compares the high-energy constants and sampling bias, and tests the limiting time- and area-sampling distribution functions. It has been executed successfully. These finite-precision checks support, but do not substitute for, the analytic proof above.

## Relationship to prior work

Chen and Dong (arXiv:2401.07332, first version January 14, 2024) prove that piecewise Hamiltonian systems with homogeneous nonlinear parts have no isochronous switching centers; their paper gives local half-period expansions. The present result uses an explicit two-parameter, positive-quartic member of that class but concerns global large-energy **side-specific** periods, enclosed areas, and their conditional distributions. Earlier work of Gasull, Guillamon, Mañosa and Mañosas studies period functions for smooth Hamiltonian systems with homogeneous nonlinearities, not the stated joined two-potential sampling law. The time/area identity and standard elliptic/beta asymptotics are established mathematical tools rather than claimed new theorems.

## Limitations

The claim is for this canonical pair of quartic angular nonlinearities, not every quartic switching Hamiltonian. It addresses a deterministic globally periodic family, not arbitrary Filippov sliding systems. Asymptotic statements do not give uniform estimates when the fixed positive coefficients vary with energy. Independent external validation and a comprehensive historical publication-priority assessment have not been performed; a 1997 relevant smooth-Hamiltonian paper could not be inspected in full.

## References

1. X. Chen and G. Dong, *Non-isochronicity on piecewise Hamiltonian differential systems with homogeneous nonlinearities*, arXiv:2401.07332v1 (2024), https://arxiv.org/abs/2401.07332 .
2. A. Gasull, A. Guillamon, V. Mañosa and F. Mañosas, *The period function for Hamiltonian systems with homogeneous nonlinearities*, Journal of Differential Equations **139** (1997), 237–260, https://doi.org/10.1006/jdeq.1997.3296 .
3. C. Liu and S. Wang, *On the isochronous center of planar piecewise polynomial potential systems*, Proceedings of the American Mathematical Society **150** (2022), 2499–2507, https://doi.org/10.1090/proc/15879 .
4. NIST Digital Library of Mathematical Functions, Chapter 19, especially §19.12, asymptotics of complete elliptic integrals, https://dlmf.nist.gov/19.12 .
