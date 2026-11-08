# A sharp dimension barrier for reachable transient centers on periodic orbits

## Finding

Let \(M\) be a smooth two-dimensional manifold without boundary, let \(f\) be a complete \(C^1\) vector field on \(M\), and let \(v\in C^1(M,\mathbb R)\). **No point on a nonstationary periodic orbit of \(f\) is a reachable \(v\)-transient center.** This is true for attracting, repelling, neutral, and nonisolated periodic orbits and does not assume hyperbolicity.

The dimension threshold is sharp: the complete smooth autonomous flow on \(\mathbb R^3\)
\[
\begin{aligned}
\dot x&=-y+x\frac{x^2+y^2-1}{x^2+y^2+1},\\
\dot y&= x+y\frac{x^2+y^2-1}{x^2+y^2+1},\\
\dot z&=-z,
\end{aligned}
\]
with observable \(v(x,y,z)=x^2+y^2-1+z\), has a hyperbolic saddle periodic orbit \(\Gamma=\{(\cos\theta,\sin\theta,0):\theta\in\mathbb R\}\). **Every point of \(\Gamma\) is a reachable \(v\)-transient center.** For starting points \((\sqrt{1+\varepsilon},0,\varepsilon)\), the first forward and backward exits from each fixed sufficiently small observable-speed threshold \(s>0\) both take \(\log(1/\varepsilon)+O_s(1)\) time. In fact, the two additive constants are explicit below.

## Assumptions and scope

For a complete flow \(\phi_t\), put \(g=Dv=f\cdot\nabla v\) in Euclidean coordinates (or the Lie derivative on \(M\)). For a threshold \(s>0\), define
\[
T_s^+(p)=\inf\{t\ge0:|g(\phi_t p)|>s\},\qquad
T_s^-(p)=\inf\{t\ge0:|g(\phi_{-t}p)|>s\},
\]
with the infimum of the empty set taken as infinity. A point \(p_*\) is a **reachable \(v\)-transient center** if some \(S>0\) has the property that for every \(0<s<S\), every \(T>0\), and every neighborhood \(U\) of \(p_*\), there exists \(p\in U\) for which
\[
T<T_s^+(p)<\infty\quad\text{and}\quad T<T_s^-(p)<\infty.
\]
This is the two-direction observable-speed definition of Liu--Magpantay and Pasion--Magpantay; it is not merely a criterion involving one escaping orbit in either direction separately.

The two-dimensional assertion is local near any regular closed orbit; completeness is imposed to keep both exit-time definitions globally meaningful. The three-dimensional example is globally complete because its vector field has at most linear growth, with globally bounded first derivatives. No conclusion is asserted for equilibria or for periodic points of discrete-time maps.

## Proof

### 1. Necessary vanishing on a periodic orbit

Suppose \(p_*\) is reachable and belongs to a periodic orbit \(\Gamma\). If \(g(\phi_{t_0}p_*)\ne0\) at some orbit phase, choose \(s>0\) smaller than both the magnitude there and the reachability constant \(S\). By periodicity choose \(t_0\ge0\). Continuity of \(p\mapsto g(\phi_{t_0}p)\) makes the forward speed exceed \(s\) by time \(t_0\) for every sufficiently nearby initial state, contradicting the requirement \(T_s^+(p)>T\) with \(T>t_0\). Consequently \(g=0\) everywhere on \(\Gamma\).

### 2. One-sided confinement in dimension two

For a tubular neighborhood \(W\) of a nonstationary periodic orbit \(\Gamma\), take a sufficiently small transverse segment \(I\) with coordinate \(u=0\) at \(\Gamma\). Its first-return map \(P\), defined close to zero, is a \(C^1\) local diffeomorphism fixing zero. If \(M\) is nonorientable, \(P\) may reverse transverse orientation; in either case \(Q=P^2\) is strictly increasing near zero and fixes zero.

Shrinking \(I\), continuity of the flow and compactness of the closed orbit ensure that every orbit segment joining a point of \(I\) to its second forward or second backward return stays in \(W\). For a small positive transverse coordinate \(u\), if \(Q(u)\le u\), monotonicity gives \(0<Q(u)\le u\), so all forward \(Q\)-iterates remain in \((0,u]\). If \(Q(u)\ge u\), all backward iterates \(Q^{-1}\) remain in \((0,u]\). Equality confines in both directions. Reversing the sign of the coordinate gives the same dichotomy for \(u<0\). Every intermediate first return and every connecting orbit segment also stays in \(W\) by the preceding uniform small-section choice. Flowbox coordinates around the compact orbit transfer this one-sided confinement to all points of a sufficiently small neighborhood \(V\) of \(\Gamma\). Thus **for each \(p\in V\), at least one of its two time semiorbits remains entirely in \(W\)**.

If \(g=0\) on \(\Gamma\), then for any \(s>0\) there exists such a tubular \(W\) where \(|g|<s\). The neighborhood \(V\) just constructed therefore satisfies
\[
\forall p\in V:\quad T_s^+(p)=\infty\ \text{or}\ T_s^-(p)=\infty.
\]
This contradicts reachable transience. If \(g\) fails to vanish on \(\Gamma\), the first step already excludes reachability. Hence no point on any periodic orbit in dimension two is reachable.

### 3. Sharpness in dimension three

For the displayed three-dimensional system put \(q=x^2+y^2\). Direct differentiation gives
\[
\dot q=\frac{2q(q-1)}{q+1},\qquad \dot z=-z,\qquad
 g=\frac{2q(q-1)}{q+1}-z.
\]
On \(\Gamma\), \(q=1\), \(z=0\), and the angular velocity is exactly \(1\); the two transverse linear exponents are \(+1\) and \(-1\). Thus \(\Gamma\) is a genuine saddle periodic orbit. Since the vector field is smooth and has at most linear growth, its flow exists for all real time.

Start with \(q(0)=1+\varepsilon\) and \(z(0)=\varepsilon>0\). For every finite time, \(q(t)>1\) and \(z(t)=\varepsilon e^{-t}>0\). The function \(q\mapsto 2q(q-1)/(q+1)\) is strictly increasing for \(q>1\). Because \(q(t)\) increases and \(z(t)\) decreases, \(g(\phi_t p)\) increases strictly from \(-\infty\) as \(t\to-\infty\) to \(+\infty\) as \(t\to+\infty\). The latter limits follow from \(q(t)\to1\) backward, \(q(t)\to\infty\) forward, and the explicit exponential formula for \(z\). For fixed \(s>0\) both threshold exits are therefore finite. As \(\varepsilon\downarrow0\), the initial state approaches \(\Gamma\) and \(g\) tends uniformly to zero on every bounded time interval, so both exit times exceed any prescribed \(T\). Rotational equivariance gives this construction near every point of \(\Gamma\), proving reachability with, for example, \(S=1\).

### 4. Explicit two-sided exit-time laws

The radial equation has the exact first integral
\[
\frac{(q(t)-1)^2}{q(t)}
=\frac{\varepsilon^2}{1+\varepsilon}e^{2t}.
\]
For a fixed \(s>0\), let
\[
q_s=\frac{s+2+\sqrt{(s+2)^2+8s}}4>1,
\]
which uniquely solves \(2q_s(q_s-1)/(q_s+1)=s\). By strict monotonicity of \(g\), its first forward crossing of \(+s\) and first backward crossing of \(-s\) are unique. Rescaling the exact first integral at times \(t=\log(1/\varepsilon)+c\), and the explicit \(z(t)\) at times \(t=-\log(1/\varepsilon)-c\), yields
\[
\boxed{T_s^+(\varepsilon)=\log\frac1\varepsilon+
\log\frac{q_s-1}{\sqrt{q_s}}+o(1)},\qquad
\boxed{T_s^-(\varepsilon)=\log\frac1\varepsilon+\log s+o(1)}.
\]
The error terms are for \(\varepsilon\downarrow0\) at each fixed \(s>0\). This proves long but finite slow residence in both time directions, with explicit constants, on the smallest possible state-space dimension permitting a saddle periodic orbit.

## Verification

The included `verify.py` checks the exact radial first-integral identity, derivative and transverse-exponent identities, and finite-precision estimates for both logarithmic exit-time constants at nine pairs of thresholds and initial offsets. The exclusion in dimension two is a qualitative Poincaré-return proof, not a finite computation; its compactness and monotone-iteration steps are stated explicitly above. The analytic limits in dimension three follow from the first integral and do not depend on the numerical tests.

## Relationship to prior work

Pasion and Magpantay, *Nonequilibrium Transient Centers in Continuous-Time Systems* (first public version 30 October 2026, arXiv:2610.41930v1), define observable-speed transient centers and reachable transient centers, and give general sufficient escape criteria. Liu, Magpantay and Abdella, *A framework for long-lasting, slowly varying transient dynamics* (2023), provide the two-sided escape criterion, recalled as Theorem 2.8 in the 2026 work. The present theorem identifies a dimension-specific **impossibility** for periodic trajectories, and a globally complete three-dimensional realization with exact escape-time constants. It does not claim novelty for the definitions, the ordinary one-dimensional Poincaré return-map monotonicity, or stable/unstable Floquet theory separately. The proof combines these existing ingredients for the newer observable-based reachability property.

## Limitations

The no-go statement applies to smooth autonomous flows on two-dimensional manifolds near nonstationary periodic orbits, not to equilibria, nonperiodic recurrent sets, delayed systems, or discrete-time dynamics. The three-dimensional example is a deliberately constructed smooth model demonstrating sharpness; no claim is made about prevalence among applications. Historical priority remains provisional, particularly because the complete 2022 original article defining transient centers was not available for direct full-text comparison. Independent scientific review has not been performed.

## References

1. A. Pasion and F. Magpantay, *Nonequilibrium Transient Centers in Continuous-Time Systems*, arXiv:2610.41930v1, posted 2026-10-30. https://arxiv.org/abs/2610.41930
2. A. Liu, F. M. G. Magpantay and K. Abdella, *A framework for long-lasting, slowly varying transient dynamics*, Mathematical Biosciences and Engineering **20** (2023), 12130–12153. DOI: 10.3934/mbe.2023540. https://www.aimspress.com/aimspress-data/mbe/2023/7/PDF/mbe-20-07-540.pdf
3. A. Liu and F. M. G. Magpantay, *A Quantification of Long Transient Dynamics*, SIAM Journal on Applied Mathematics **82** (2022), 381–407. DOI: 10.1137/20M1367131.
4. G. Teschl, *Ordinary Differential Equations and Dynamical Systems*, American Mathematical Society (2012), local Poincaré map and planar flow theory. https://www.mat.univie.ac.at/gerald/ftp/book-ode/ode.pdf
