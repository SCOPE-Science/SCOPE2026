# Exact slow-escape area and sampling-dependent lifetime tails in a harmonic cubic gradient flow

## Finding

Consider the three-dimensional symmetric-Jacobian quadratic ODE
\[
\dot x=x^2-y^2,\qquad \dot y=-2xy,\qquad \dot z=-z,
\]
with potential \(V(x,y,z)=\tfrac13(x^3-3xy^2)-\tfrac12z^2\). Let \(T(x,y,z)\in(0,\infty]\) be the maximal forward existence time. Put
\[
B_*=\operatorname{B}(\tfrac12,\tfrac16)
 =\int_{-\infty}^{\infty}(1+s^2)^{-2/3}\,ds,
\qquad K_*=\frac{B_*^3}{27\pi}.
\]
For every \(t>0\), the planar slow-escape set
\[
D_t=\{(x,y)\in\mathbb R^2:T(x,y,z)>t\}
\]
(independent of \(z\)) has **exact** two-dimensional Lebesgue area
\[
\boxed{|D_t|=\frac{B_*^3}{27t^2}.}
\]
Except for three stable rays and the origin (a planar null set), every initial condition blows up in finite forward physical time. If the planar initial point is uniform in \(D_s\) for a fixed \(s>0\), its conditional survival law is **exactly Pareto**:
\[
\Pr(T>t\mid (X,Y)\text{ uniform in }D_s)=(s/t)^2,
\qquad t\ge s.
\]
If \((X,Y)\) instead has any bounded continuous probability density \(f\) on \(\mathbb R^2\) with \(f(0,0)>0\), then
\[
\boxed{\lim_{t\to\infty}t^2\Pr(T>t)=\frac{B_*^3}{27}f(0,0).}
\]
Its positive lifetime moments are finite precisely for orders \(0<p<2\); at order two the truncated second moment grows like \(2B_*^3f(0,0)\log L/27\). For an isotropic Gaussian with independent coordinate variance \(\sigma^2\), the tail constant becomes \(B_*^3/(54\pi\sigma^2)\). In contrast, if the planar start is **uniform in angle on a fixed circle** of radius \(R>0\), then
\[
\boxed{\lim_{t\to\infty}t^3\Pr(T>t)=\frac{B_*^3}{27\pi R^3}=K_*R^{-3},}
\]
and its positive lifetime moments are finite precisely for \(0<p<3\). The planar density and fixed-radius ensembles therefore have different sharp tail and moment exponents, even though the deterministic flow is identical.

## Assumptions and scope

All solutions use original, unrescaled physical time. The variables \(x,y,z\) are real, with global polynomial right-hand side and unique maximal solutions. The auxiliary independent \(z\)-coordinate may have **any** finite initial distribution, including deterministic, because \(z(t)=z(0)e^{-t}\) and does not affect the lifespan. The initial planar probability law in the density assertion is assumed to have a bounded density continuous at the origin and strictly positive there; fixed-radius sampling means uniform angular measure on one specified circle. The sets \(D_t\) are unbounded but finite-area, so normalized area on \(D_s\) is a genuine probability law.

## Proof

**Step 1: Exact scalarization and completeness boundary.** Write \(w=x+iy\) and \(w^3=u+iv\). Since \(\dot w=\overline w^{\,2}\), direct differentiation gives
\[
\frac{d}{dt}w^3=3w^2\overline w^{\,2}=3|w|^4,
\quad \dot v=0,
\quad \dot u=3(u^2+v^2)^{2/3}.
\]
For \(v\ne0\), \(u\) increases strictly and the remaining original-time lifespan from any finite \(u\) is
\[
T(u,v)=\frac13\int_u^{\infty}(q^2+v^2)^{-2/3}\,dq<\infty.
\]
The magnitude \(|w|=(u^2+v^2)^{1/6}\) tends to infinity as \(u\to\infty\), so this is the actual maximal lifespan. The cubic map has three local inverse branches, followed continuously by each nonzero trajectory; it does not create a branch-changing ambiguity. For \(v=0,u>0\), the lifespan is \(u^{-1/3}\); for \(v=0,u<0\), \(u(t)\uparrow0\) only as \(t\to\infty\). At \(w=0\), the planar component is stationary. Thus the global initial points are precisely the origin and the three half-rays \(w^3<0\), with any \(z\).

**Step 2: Exact area-coordinate Jacobian.** The map \(w\mapsto w^3\) is three-to-one away from the origin with absolute real Jacobian \(9|w|^4=9(u^2+v^2)^{2/3}\). Summing the three inverse branches gives, as a planar area element,
\[
 dx\,dy=\frac{du\,dv}{3(u^2+v^2)^{2/3}}=|dT|\,dv.
\]
For each fixed \(v\ne0\), as \(u\) increases from \(-\infty\) to \(+\infty\), remaining lifespan \(T\) decreases from
\[
M(v)=\frac13\int_{-\infty}^{\infty}(q^2+v^2)^{-2/3}\,dq
 =\frac{B_*}{3|v|^{1/3}}
\]
to zero. Therefore the joint area in coordinates \((T,v)\) is exactly ordinary Lebesgue area on
\[
\{(\tau,v): v\ne0,\;0<\tau<M(v)\}.
\]
The sets \(v=0\) and \(w=0\) have zero planar area and do not alter this identity. With \(c=B_*/3\) and \(v_*=(c/t)^3\), Tonelli's theorem gives
\[
|D_t|=\int_{\mathbb R}(c|v|^{-1/3}-t)_+\,dv
=2\int_0^{v_*}(cv^{-1/3}-t)\,dv
=2\left(\frac{3c}{2}v_*^{2/3}-tv_*\right)
=\frac{c^3}{t^2}=\frac{B_*^3}{27t^2}.
\]
For a uniform initial point in \(D_s\), the inclusion \(D_t\subset D_s\) for \(t\ge s\) yields the exact Pareto ratio \(|D_t|/|D_s|=(s/t)^2\).

**Step 3: Continuous-density sampling.** Quadratic homogeneity of the planar vector field gives \(T(rw)=T(w)/r\) for \(r>0\). Hence \(D_t=t^{-1}D_1\). For any bounded density \(f\) continuous at zero,
\[
t^2\Pr(T>t)=\int_{D_1} f(q/t)\,dq
\xrightarrow[t\to\infty]{}f(0,0)|D_1|,
\]
by bounded convergence on a finite-area, though unbounded, domain. The assumed strict positivity of \(f(0,0)\) makes the constant nonzero. Integrating the asymptotic survival probability gives \(\mathbb E T^p<\infty\) exactly for \(0<p<2\), and the standard survival-tail integration identity yields
\(\mathbb E[T^2\mathbf1_{\{T\le L\}}]\sim 2B_*^3f(0,0)\log L/27\). For independent centered Gaussian planar coordinates of variance \(\sigma^2\), substitute \(f(0,0)=1/(2\pi\sigma^2)\).

**Step 4: Separatrix-driven fixed-radius sampling.** Put \(w=Re^{i\theta}\). The scalar integral and scaling give \(T=A(\theta)/R\), where, for nonexceptional angles,
\[
A(\theta)=\frac13\int_{\cos(3\theta)}^{\infty}
(s^2+\sin^2(3\theta))^{-2/3}\,ds.
\]
There are precisely three stable angles \(\theta_j=(2j+1)\pi/3\), with \(j=0,1,2\). As \(\theta\to\theta_j\), the initial integral endpoint approaches \(-1\) and \(|\sin3\theta|\sim3|\theta-\theta_j|\), so splitting the scaled integral at infinity yields
\[
A(\theta)\sim\frac{B_*}{3^{4/3}}|\theta-\theta_j|^{-1/3}.
\]
Away from the three stable angles \(A\) is bounded. The two-sided angular lengths of the three neighborhoods where \(A>Rt\) are therefore asymptotic to \(6(B_*/3^{4/3}Rt)^3\). Dividing by \(2\pi\) yields
\[
\Pr(T>t)\sim\frac{B_*^3}{27\pi R^3}t^{-3}.
\]
The same local asymptotics give \(\int A(\theta)^p\,d\theta<\infty\) iff \(p<3\), proving the circle-sampling moment threshold. No finite sampling or differential-equation solver is used to infer these infinite assertions.

## Verification

The accompanying `check.py` uses Python with SciPy to verify the exact scalar polynomial identities on 140 deterministic test points, the angular-time differential relation, angular singular scaling, the exact area-to-angle identity \((2\pi)^{-1}\int A^2= B_*^3/(27\pi)\), and large-threshold circle-survival constants. It is a reproducible numerical diagnostic, not an independent proof. Run `python check.py` with SciPy installed. The authoritative argument is Steps 1–4.

## Relationship to prior work

Messias and Silva (arXiv:2608.21681, first public 2026-08-21) establish that every symmetric-Jacobian quadratic three-dimensional field is the gradient of a cubic potential and classify qualitative bounded recurrence and dynamics at infinity; their Sections 1, 3–7, and 9 motivate quantitative finite-time escape and reference Gaussian-initialization experiments. They do not give the exact slow-escape area, action-time Jacobian, conditional Pareto law, or contrasting fixed-radius and continuous-density survival exponents calculated here. Matsue's 2019 geometric blow-up study concerns rates near compactified invariant sets rather than this exact planar area/initialization law. Fiedler's 2025 rational complex vector-field study concerns orbit connections and finite-time blow-up for a different class of ODEs; the exact sampled-lifetime calculation is not supplied there. Classical beta-integral and regular-variation techniques are used, not claimed as novel.

## Limitations

The result is for one canonical cubic-gradient example, **not** for all symmetric-Jacobian quadratic systems or all homogeneous cubic potentials. The general-source theorem about absence of bounded chaos is not extended. The fixed-radius cubic tail requires uniform angular sampling; arbitrary nonuniform angular laws may have other exponents. The continuous-density tail requires boundedness, continuity at the origin, and positive density there; densities vanishing at the origin or singular distributions may have different scaling. The Gaussian stochastic statements concern random *initial conditions*, not stochastic forcing. Historical priority outside searched accessible literature remains to be independently checked.

## References

1. M. Messias and R. P. Silva, *An Elegant Analytical Resolution of the Sprott–Zeraoulia Conjecture for Three-Dimensional Quadratic Differential Systems with Symmetric Jacobian Matrices*, arXiv:2608.21681 (first public 2026-08-21), https://arxiv.org/abs/2608.21681.
2. K. Matsue, *Geometric treatments and a common mechanism in finite-time singularities for autonomous ODEs*, Journal of Differential Equations 267 (2019), 7313–7368, https://doi.org/10.1016/j.jde.2019.07.022.
3. B. Fiedler, *Real-time blow-up and connection graphs of rational vector fields on the Riemann sphere*, arXiv:2504.20503 (2025), https://arxiv.org/abs/2504.20503.
