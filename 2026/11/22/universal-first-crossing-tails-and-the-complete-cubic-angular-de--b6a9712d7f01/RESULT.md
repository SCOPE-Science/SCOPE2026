# Physical-time first-crossing tails from finite-order angular zeros

## Finding

Let \(\dot z=\lambda z+Q(z)\) in the plane, where \(\lambda>0\), \(p\ge1\) is integral, and \(Q\) is a homogeneous polynomial vector field of degree \(2p+1\). Write \(u_\theta=(\cos\theta,\sin\theta)\), let \(J(x,y)=(-y,x)\), and set
\[
a(\theta)=-\langle u_\theta,Q(u_\theta)\rangle,\qquad
g(\theta)=\langle Ju_\theta,Q(u_\theta)\rangle.
\]
Assume \(a>0\) on the circle. Let the lifted angles \(\theta_a<\theta_c<\theta_a+2\pi\) satisfy \(g(\theta_a)=0\) and \(g>0\) on \((\theta_a,\theta_c]\), with \(g(\theta_a+\delta)=c\delta^k+O(\delta^{k+1})\) for an integer \(k\ge1\) and \(c>0\). Fix \(I=[r_-,r_+]\) with \(0<r_-<r_+<\infty\). Start at \((r,\theta_a+\delta)\), where \(r\in I\) and \(0<\delta\le h\le\theta_c-\theta_a\). Let \(T(r,\delta)\) be the first original physical time at which the lifted angle reaches \(\theta_c\), with \(T=0\) if the trajectory starts on that ray. Put \(v_*=a(\theta_a)/\lambda\). Uniformly on \(I\),
\[
\frac{T(r,\delta)}{\log(1/\delta)}\longrightarrow\frac{v_*}{c}\quad(k=1),\qquad
T(r,\delta)\delta^{k-1}\longrightarrow C_k:=\frac{v_*}{(k-1)c}\quad(k\ge2).
\]
Suppose the starting law is supported on the indicated annular sector and its angular offset has a density \(q(\delta)\) with \(q(\delta)\to q_0>0\) as \(\delta\downarrow0\). In particular this holds for a continuous probability density \(w(r,\theta)\) relative to \(dr\,d\theta\) with \(q_0=\int_I w(r,\theta_a)\,dr>0\); for a density relative to Euclidean area, absorb the polar Jacobian into \(w\). Then
\[
\lim_{t\to\infty}\frac{\log\Pr(T>t)}{t}=-\frac{c}{v_*}\quad(k=1),\qquad
\Pr(T>t)\sim q_0\left(\frac{C_k}{t}\right)^{1/(k-1)}\quad(k\ge2).
\]
For \(k=1\) every positive moment of \(T\) is finite. For \(k\ge2\), the \(s\)-th moment for \(s>0\) is finite exactly when \(s<1/(k-1)\).

## Proof

For \(v=r^{-2p}\) the polar equations are \(\dot v=-2p\lambda v+2pa(\theta)\) and \(\dot\theta=g(\theta)/v\). Variation of constants bounds \(v\) between
\[
L=\min(r_+^{-2p},\min a/\lambda)>0,\qquad U=\max(r_-^{-2p},\max a/\lambda)<\infty.
\]
These bounds keep nonzero trajectories in a bounded positive annulus, so they exist at least through the first crossing. The angle increases up to the target and has speed at least \(g/U\); for each \(\delta>0\), the integral of \(U/g\) from the starting angle to the target is finite. This bound is uniform for offsets bounded away from zero.

Integrate the log-radius derivative used in the periodic-orbit period computation of [2], now between the initial and crossing rays rather than around a closed orbit. In physical time \(1=a(\theta)/(\lambda v)-\dot v/(2p\lambda v)\), so
\[
T(r,\delta)=\frac1\lambda\int_{\theta_a+\delta}^{\theta_c}\frac{a(\theta)}{g(\theta)}\,d\theta
-\frac{1}{2p\lambda}\log\frac{v(T)}{v(0)}.
\]
The endpoint term is bounded in absolute value by \(\log(U/L)/(2p\lambda)\), uniformly in \(r,\delta\). At distance \(x\downarrow0\) from the source, \(a(\theta_a+x)/g(\theta_a+x)\sim a(\theta_a)/(cx^k)\). Bounding this integrand between \(1\pm\varepsilon\) times that power in a fixed small interval gives the two divergent clocks; the integral beyond that interval is fixed and finite. This proves the stated uniformity. The formula includes the trivial crossing at \(\theta_c\) when the closed endpoint is allowed.

For \(k\ge2\) the uniform clock bounds trap \(\{T>t\}\), for all sufficiently large \(t\), between the starting events
\[
\delta<((1-\varepsilon)C_k/t)^{1/(k-1)}
\quad\hbox{and}\quad
\delta<((1+\varepsilon)C_k/t)^{1/(k-1)}.
\]
Offsets bounded away from zero cannot contribute to either tail for large \(t\). Since \(\Pr(\delta<x)\sim q_0x\), these bounds give the claimed constant as \(\varepsilon\downarrow0\). For \(k=1\) the same comparison with \((1\pm\varepsilon)(v_*/c)\log(1/\delta)\) gives the stated logarithmic rate. The tail integration formula \(\mathbb E T^s=s\int_0^\infty t^{s-1}\Pr(T>t)\,dt\) yields the moment criteria, with divergence at the power-law endpoint. No monotonicity in the starting radius or joint density of the two coordinates is required.

## Cubic realization

For \(p=1\), \(g\) is the restriction of the homogeneous quartic \(\langle J(x,y),Q(x,y)\rangle\). In a local slope coordinate based on a nonvanishing coordinate its finite-root orders are at most four, as a nonzero polynomial of degree at most four times a nonvanishing smooth factor. The resulting qualitative spectrum is known [1]. The following explicit examples realize each order for the physical-time law. Set
\[
Q_k(x,y)=\left(-x(x^2+y^2),-y(x^2+y^2)+P_k(x,y)\right),
\quad (P_1,P_2,P_3,P_4)=(x^2y,xy^2,-x^2y,x^3).
\]
The angular factor is \(xP_k\) on the circle, and \(a=1-yP_k\). In the four cases \(|yP_k|\) is bounded by \(1/4\) or \(3\sqrt3/16\) by maximizing \(x^2y^2\), \(|xy^3|\), or \(|x^3y|\) on \(x^2+y^2=1\); hence \(a>2/3\). Take \(\theta_a=0\) for \(k=1,2\) and \(\theta_a=\pi/2\) for \(k=3,4\). Then on \(0<\delta\le\pi/4\),
\[
g(\theta_a+\delta)=\frac{\tan^k\delta}{(1+\tan^2\delta)^2},\qquad a(\theta_a)=1.
\]
Choose the target \(\theta_c=\theta_a+\pi/4\). Sample the starting angle uniformly on the **open wedge \((\theta_a,\theta_a+\pi/4)\)**, independently of any radial probability law supported on \(I\). Thus \(q_0=4/\pi\), \(c=1\), and \(v_*=1/\lambda\). For \(k=1\) the logarithmic survival rate is \(-\lambda\). For \(k=2,3,4\) the survival laws are
\[
\Pr(T>t)\sim\frac4\pi\left(\frac1{(k-1)\lambda}\right)^{1/(k-1)} t^{-1/(k-1)}.
\]
The sampling wedge is not a full quadrant. Initial states past the target are excluded.

## Verification, relationship to prior work, and limitations

The accompanying standard-library `check.py` checks the cubic identities on a finite grid and integrates four individual under-target trajectories in physical time. It does not sample the starting ensemble or establish a uniform or infinite-time limit. The analytic clock bound and the angular-marginal comparison supply those steps.

The phase portraits and cubic multiplicity taxonomy are established [1], and the underlying polar equations and logarithmic-radius period computation for cycles are known [2]. Parameter-dependent saddle-node delays are also known [3]. This result concerns tails of deterministic first-crossing times from an actual angular zero, with explicit constants and moment cutoffs for distributions of initial states, rather than perturbed periodic-orbit occupation, time-rescaled clocks, or stochastic forcing. At a simple zero only the logarithmic rate is asserted. If the starting angular density vanishes at the source, the stated ensemble exponents need not apply. Historical priority for possible general waiting-time results is not established.

## References

1. B. Alarcón, S. B. S. D. Castro and I. S. Labouriau, *Global planar dynamics with a star node and contracting nonlinearity*, [arXiv:2307.16020v2](https://arxiv.org/html/2307.16020v2), Theorem 7.2 and Tables 2–4.
2. [Exact angular return and physical-time Floquet rigidity for contracting homogeneous star-node cycles](https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-exact-angular-return-and-physical-time-floquet-rigidity-for-cont--7c00337eaa41/RESULT.md), proof of the physical-time period.
3. C. Kuehn, *Scaling of Saddle-Node Bifurcations: Degeneracies and Rapid Quantitative Changes*, [arXiv:0807.1546](https://arxiv.org/abs/0807.1546), §2.1.
