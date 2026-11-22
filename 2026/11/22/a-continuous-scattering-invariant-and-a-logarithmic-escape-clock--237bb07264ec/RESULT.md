# A continuous scattering invariant and a logarithmic escape clock in a quadratic flow

## Finding
Consider the polynomial system
\[
\dot x=yz,\qquad \dot y=x^2-y,\qquad \dot z=-4x.
\]
Set \(q=-z\), \(p=y/x^2\), and \(\varepsilon=qx\). On the open region
\[
\Omega=\left\{x>0,\ q>3,\ \tfrac12<p<2,\ 0<\varepsilon<\tfrac1{10}\right\},
\]
for **every** initial state, the solution exists for all positive time, remains in \(\Omega\), and has \(q(t)\to\infty\), \(x(t),y(t)\to0\). The limit
\[
\mathcal L(x_0,y_0,z_0)=\lim_{t\to\infty}x(t)\exp\bigl(q(t)^2/8\bigr)
\]
exists in \((0,\infty)\), is continuous and nonconstant on \(\Omega\), and is invariant under forward time translation. Every such solution has the **two-term, initial-state-resolved escape clock**
\[
q(t)^2=8\log t+4\log\log t+4\log8+8\log\mathcal L+o(1).
\]
Moreover, in original physical time,
\[
\lim_{t\to\infty}tq(t)x(t)=1,\qquad
\lim_{t\to\infty}t\bigl(p(t)-1\bigr)=2,\qquad
\log\bigl(x(t)e^{q(t)^2/8}\bigr)=\log\mathcal L+\frac2t+o(t^{-1}).
\]
The invariant is defined on this escaping region only; its existence does **not** assert a global polynomial, rational, or Darboux first integral.

## Assumptions and scope
The independent variable \(t\) is real continuous physical time and all initial coordinates are real. The zero-forcing parameter choice in the two-parameter quadratic family is fixed throughout. The region \(\Omega\) is open and nonempty. We make no assertion for initial data outside \(\Omega\) or for other forcing parameters. \(\mathcal L\) depends on the entire starting state, and the unspecified \(o(1)\) is pointwise in that state.

## Proof
**1. Exact coordinates and trapping.** In \(\Omega\), the equations become
\[
\dot x=-qpx^2,\quad \dot q=4x,\quad
\dot p=1-p+2\varepsilon p^2,\quad
\dot\varepsilon=x^2(4-q^2p).
\tag{1}
\]
At \(p=\tfrac12\) the \(p\)-derivative is positive; at \(p=2\) it is at most \(-1+8/10<0\). Since \(q\ge3\) and \(p\ge1/2\), \(4-q^2p\le-1/2<0\), so \(\varepsilon\) strictly decreases; \(q\) increases. These strict inward signs show forward invariance. The estimate \(\dot x\le-(3/2)x^2\) gives
\[
0<x(t)\le\frac{x_0}{1+(3/2)x_0t},
\quad q(t)\le q_0+\frac83\log\bigl(1+(3/2)x_0t\bigr).
\tag{2}
\]
Thus no finite positive-time blow-up occurs and
\(\varepsilon(t)=O(\log(2+t)/(1+t))\in L^2(0,\infty)\).
Also, using \(q\) as a time coordinate,
\[
\frac{dx}{dq}=-\frac14qpx,
\]
so if \(q\) had a finite upper limit, \(x\) would stay bounded below by a positive constant, contradicting \(\dot q=4x\). Consequently \(q\to\infty\) and \(x\to0\), while \(y=px^2\to0\).

**2. A positive scattering limit.** Put \(r=p-1\). The exact equation
\[
\dot r+r=2\varepsilon p^2
\tag{3}
\]
and \(1/2<p<2\) imply \(r\in L^2(0,\infty)\): its variation-of-constants formula is a decaying exponential plus an exponential convolution of an \(L^2\) function. By Cauchy--Schwarz, \(\varepsilon r\in L^1(0,\infty)\). The logarithmic derivative of \(J=xe^{q^2/8}\) is the exact identity
\[
\frac{d}{dt}\log J=-qpx+\frac14q\dot q=\varepsilon(1-p)=-\varepsilon r.
\tag{4}
\]
Therefore \(\log J\) converges to a **finite real** limit, establishing \(0<\mathcal L<\infty\). Explicitly,
\[
\mathcal L=x_0e^{q_0^2/8}\exp\left[-\int_0^\infty\varepsilon(t)r(t)\,dt\right].
\tag{5}
\]
Forward time translation changes neither limit, so \(\mathcal L\) is an invariant.

**3. Continuity and nonconstancy.** On any compact subset of \(\Omega\), the constants in (2) are uniform. The exponential convolution formula for (3) then makes the tail integral in (5) uniformly small as its lower endpoint tends to infinity. Finite-time continuous dependence proves that \(\mathcal L\) is continuous. To show it is not constant, hold \(q_0>3\) and \(p_0=1\) fixed and take \(x_0\downarrow0\), subject to \(q_0x_0<1/10\). The sharper inequalities \(x(t)\le x_0/(1+(q_0/2)x_0t)\) and \(q(t)\le q_0+(8/q_0)\log(1+(q_0/2)x_0t)\) show \(\|\varepsilon\|_{L^2}^2=O_{q_0}(x_0)\). Since \(r(0)=0\), Young's convolution inequality gives \(\|r\|_{L^2}\le8\|\varepsilon\|_{L^2}\). Formula (5) hence yields
\[
\mathcal L=x_0e^{q_0^2/8}\bigl(1+O_{q_0}(x_0)\bigr)\longrightarrow0.
\]
Each individual \(\mathcal L\) is positive, so the invariant is nonconstant.

**4. Clock inversion.** Since \(J(t)\to\mathcal L\), the increasing variable \(q\) obeys
\[
\frac{dq}{dt}=4\mathcal L e^{-q^2/8}(1+o(1)).
\]
As \(\int^Qe^{s^2/8}ds\sim4e^{Q^2/8}/Q\), integration gives
\[
t\sim\frac{e^{q(t)^2/8}}{\mathcal L q(t)}.
\tag{6}
\]
It follows that \(q(t)^2\sim8\log t\) and \(tq(t)x(t)\to1\). Taking logarithms of (6) and substituting \(\log q(t)=\tfrac12\log\log t+\tfrac12\log8+o(1)\) gives the displayed second-order clock, including its initial-state constant.

**5. First asymptotic correction to the scattering coordinate.** By (6), \(\varepsilon(t)=q(t)x(t)\sim t^{-1}\). In (3), the forcing is \(2\varepsilon p^2\sim2t^{-1}\) since \(p\to1\) by the stable linear equation (3). Its exponential convolution thus gives \(r(t)\sim2t^{-1}\): split the convolution at \(t/2\); the earlier portion is exponentially small, and on bounded backward lags the forcing divided by \(2/t\) tends uniformly to one. Equation (4) now yields \((\log J)'=-2t^{-2}+o(t^{-2})\). Integrating from \(t\) to infinity proves \(\log J(t)-\log\mathcal L=2/t+o(t^{-1})\).

## Verification
The standalone `verify.py` checks (1) and (4) symbolically, exact inward-sign bounds by rational arithmetic, and the asymptotic predictions using an independently integrated sample trajectory. The numerical portion is only a diagnostic: the assertions for every initial state follow from the analytic argument above. Sample initial state: \((x_0,p_0,q_0)=(1/50,1,4)\).

## Relationship to prior work
Algaba, Domínguez-Moreno, Merino and Rodríguez-Luis introduced the quadratic family and studied homoclinic-flip bifurcations; Qu and Yang gave a detailed non-Darboux integrability and compactification analysis. An existing exact theorem for this **same zero-forcing system** already proves that a forward-invariant escaping cone exists and gives \(tqx\to1\), \(q^2/(8\log t)\to1\) and \(p\to1\). Those results are explicitly **not** presented here as new. They do not determine an initial-data-dependent positive limit for \(xe^{q^2/8}\), a nonconstant continuous scattering integral, the \(4\log\log t\) correction, or the universal \(2/t\) approach of the renormalized logarithm. These additional conclusions require the \(L^2\)-to-\(L^1\) argument and inversion (6).

## Limitations
The scattering coordinate is only constructed on \(\Omega\), not across all of phase space; the theorem does not give a closed elementary formula for it. Non-Darboux integrability and the existence of a continuous local-domain integral are logically compatible. No uniform-in-initial-state asymptotics are asserted at the boundary of \(\Omega\). Original publication-priority uncertainty remains because the 2019 source full text was not retrievable, although its abstract and the subsequent 2024 complete analysis were checked.

## References
1. A. Algaba, M. C. Domínguez-Moreno, M. Merino, A. J. Rodríguez-Luis, *Study of a simple 3D quadratic system with homoclinic flip bifurcations of inward twist case C*, Communications in Nonlinear Science and Numerical Simulation **77** (2019), 324–337. DOI: https://doi.org/10.1016/j.cnsns.2019.05.005. Author-uploaded publicly on 2019-05-16.
2. J. Qu and S. Yang, *New Insights on Non-integrability and Dynamics in a Simple Quadratic Differential System*, Journal of Nonlinear Mathematical Physics **31** (2024), article 10. DOI: https://doi.org/10.1007/s44198-024-00174-4; full open-access text.
3. A. Giraldo, B. Krauskopf, H. M. Osinga, *Computing connecting orbits to infinity associated with a homoclinic flip bifurcation*, Journal of Computational Dynamics **7** (2020), 489–510. DOI: https://doi.org/10.3934/jcd.2020020.
4. Earlier exact leading-order escape theorem for the same quadratic system, finding identifier `fcfe8e03-c010-46c6-89dc-471d7b2c2296` (recorded mathematical claim).
