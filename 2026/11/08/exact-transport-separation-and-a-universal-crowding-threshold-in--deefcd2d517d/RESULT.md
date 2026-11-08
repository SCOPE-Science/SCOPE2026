# Exact transport separation and a universal crowding threshold in resetting active-matter coexistence

## Finding

In the one-dimensional locally reset run-and-tumble active-gas model of Grange [1], a dense-droplet stationary solution and a supersaturated pure-gas stationary solution coexist at the same physical parameters. Normalizing either symmetric stationary density to a probability law and then taking its absolute position gives radial laws \(\mathsf D\) (droplet) and \(\mathsf G\) (gas). The following **coexistence transport theorem** holds.

Put \(m=\rho_m>4\), \(\chi=\sqrt{r(r+\alpha)}/v_0\), and \(h=M\chi/2\). Assume
\[
1<h<\frac m4.
\]
Define the positive gas-branch inverse flux
\[
u_m(F)=\frac m2\left(1-\sqrt{1-\frac{4F}{m}}\right),\qquad 0<F\leq \frac m4,
\]
and abbreviate \(u_*=u_m(1)\), \(u_h=u_m(h)\).

For any radial upper-tail level \(0<q<1\), let \(L_{\mathsf G}(q)\) and \(L_{\mathsf D}(q)\) be the positions where the corresponding survival probabilities equal \(q\). They satisfy
\[
0<L_{\mathsf G}(q)-L_{\mathsf D}(q)\leq\Delta_m(h),
\]
where
\[
\boxed{\Delta_m(h)=\frac{1}{\chi}\left[\log\frac{u_h}{u_*}-\frac2m(u_h-u_*)-\frac{\log h}{m}\right].}
\]
**The upper bound is attained for every \(0<q\leq 1/h\)**: the outer gas tails in inverse-survival coordinates are exact horizontal translates. In particular, the dense-droplet radial distribution strictly first-order stochastically dominates in concentration, and its exact infinite-order Wasserstein distance from the gas radial distribution is
\[
\boxed{W_\infty(\mathsf D,\mathsf G)=\Delta_m(h).}
\]
The same ordered quantile coupling has a finite exact mean transport cost:
\[
\boxed{W_1(\mathsf D,\mathsf G)=\frac{B(u_h)-B(u_*)-(h-1)/m}{h\chi},\qquad B(u)=u-\frac{3u^2}{2m}+\frac{2u^3}{3m^2}.}
\]

At fixed mass \(M\) and motility threshold \(m\), the contrast \(\Delta_m(h)\), as a function of reset rate (equivalently \(h\)), has a **sharp universal optimization transition**. Let \(q_*\in(0,1)\) be the unique zero of
\[
G(q)=\frac{1+q^2}{4}+q+\log(1-q)-\frac{1-q^2}{4}\log(1-q^2),
\]
and let \(m_*=4/(1-q_*^2)=7.3222270683788\ldots\). For \(4<m\leq m_*\), \(\Delta_m(h)\) increases strictly throughout \(1<h<m/4\), so its supremum is at the upper coexistence boundary. For \(m>m_*\), it has a **unique interior global maximum** at \(h=h_*(m)\). As \(m\to\infty\),
\[
\boxed{h_*(m)\longrightarrow e,\qquad\max_{1<h<m/4}\Delta_m(h)\longrightarrow\frac{M}{2e}.}
\]

## Assumptions and scope

The kinetic continuum model [1] has positive total mass \(M\), free run speed \(v_0>0\), tumbling intensity \(\alpha>0\), and local independent Poisson resetting intensity \(r>0\) to the origin. Runs have velocity \(\pm v(\rho)\), where the gas branch is \(v_0(1-\rho/m)\) below the density threshold \(m>4\), and the liquid branch is the constant \(v_0/m\). Density and run-orientation fields are taken as the stationary, symmetric, finite-mass continuum solutions of [1], without finite-speed returners or additional spatial diffusion.

There are two distinct stationary solutions at the **same** parameters when \(1<h<m/4\). Their normalized position distributions are \(\rho(x)\,dx/M\), with \(\int_{\mathbb R}\rho=M\). The radial law is the push-forward under \(x\mapsto|x|\), with density \(2\rho(x)/M\) on positive radii. The pure-gas solution is described as metastable in [1]; the result is a comparison of its stationary profile with the two-phase profile, **not** a claim that both are dynamically stable.

In the \(W_\infty\) statement, the transport cost is the essential supremum of radial distance \(|R_{\mathsf G}-R_{\mathsf D}|\), minimized over couplings of the radial laws. No distributional approximation or numerical truncation is part of the theorem. The upper coexistence boundary \(h=m/4\) can be included by continuous extension of the profiles; the supremum phrasing also covers exclusion of this limiting gas state.

## Proof

**1. A common mass-flux coordinate.** Let \(R(x)=v(\rho(x))\rho(x)\) denote the positive-speed flux amplitude on the positive half-line. In each continuous phase, the stationary kinetic equations of [1] imply
\[
R'(x)=-v_0\chi\rho(x),\qquad R(+\infty)=0.
\]
Mass conservation and parity therefore give
\[
\frac{R(x)}{v_0}=\chi\int_x^\infty\rho(y)\,dy
=h\,\Pr(|X|>x).
\]
The initial flux is \(R(0)/v_0=h\) for **both** stationary branches. Write \(F=R/v_0\). In gas, \(F=\rho(1-\rho/m)\); the physical small-density root is \(\rho=u_m(F)\). In liquid, \(F=\rho/m\), so \(\rho=mF\). At the liquid-gas interface, both sides have \(F=1\), although their densities jump from \(m\) to \(u_*=u_m(1)\). The liquid branch occupies exactly the flux interval \(1<F\leq h\).

**2. Exact inverse-survival coordinates.** Since \(R'=-v_0\chi\rho\),
\[
\frac{dx}{dF}=-\frac{1}{\chi\rho(F)}.
\]
The antiderivatives for the gas and liquid are respectively
\[
\int\frac{dF}{u_m(F)}=\log u_m(F)-\frac{2u_m(F)}{m}+C,
\qquad \int\frac{dF}{mF}=\frac{\log F}{m}+C.
\]
A survival level \(q\) is exactly the flux level \(F=hq\). Thus
\[
L_{\mathsf G}(q)=\frac{1}{\chi}\left[\log\frac{u_h}{u_m(hq)}-\frac2m\bigl(u_h-u_m(hq)\bigr)\right],
\]
and
\[
L_{\mathsf D}(q)=\begin{cases}
\displaystyle\frac{\log(1/q)}{m\chi},&q\geq 1/h,\\[4pt]
\displaystyle\frac{\log h}{m\chi}+\frac{1}{\chi}\left[\log\frac{u_*}{u_m(hq)}-\frac2m\bigl(u_*-u_m(hq)\bigr)\right],&q<1/h.
\end{cases}
\]
For \(F\in[1,h]\), \(u_m(F)\leq m/2<mF\), so
\[
J_m(F):=\frac1{u_m(F)}-\frac1{mF}>0.
\]
Subtracting the quantiles therefore yields
\[
L_{\mathsf G}(q)-L_{\mathsf D}(q)=\frac1\chi
\begin{cases}
\displaystyle\int_1^h J_m(F)\,dF,&0<q\leq1/h,\\[4pt]
\displaystyle\int_{hq}^h J_m(F)\,dF,&1/h<q<1.
\end{cases}
\]
This proves strict first-order radial stochastic ordering, the constant tail shift, and the displayed closed expression for \(\Delta_m(h)\). In one dimension, monotone quantile coupling minimizes every convex increasing function of transportation distance, and its essential-supremum displacement equals the supremum quantile gap [2]. Since the gap is exactly \(\Delta_m(h)\) on a positive-measure interval of quantile levels, \(W_\infty=\Delta_m(h)\) is attained, not merely bounded.

**3. Exact mean transport cost.** Strict quantile ordering gives \(W_1=\int_0^1(L_{\mathsf G}-L_{\mathsf D})\,dq\). Tonelli's theorem applied to the positive integrand in step 2 gives
\[
W_1=\frac{1}{h\chi}\int_1^h FJ_m(F)\,dF.
\]
Put \(u=u_m(F)\), so \(F=u(1-u/m)\) and \(dF=(1-2u/m)du\). Then \(F\,dF/u=(1-3u/m+2u^2/m^2)du\), producing the displayed \(B(u)\) expression.

**4. The sharp crowding transition.** Define
\[
f_m(h)=\int_1^h J_m(F)\,dF
=\log\frac{u_m(h)}{u_*}-\frac2m\bigl(u_m(h)-u_*\bigr)-\frac{\log h}{m}.
\]
Because \(\chi=2h/M\), \(\Delta_m(h)=(M/2)f_m(h)/h\). Differentiating in the open coexistence interval,
\[
f_m'(h)=\frac1{u_m(h)}-\frac1{mh},\qquad
f_m''(h)=-\frac{1}{u_m(h)^2(1-2u_m(h)/m)}+\frac{1}{mh^2}<0.
\]
For the final strict inequality put \(t=u_m(h)/m\in(0,1/2)\). It is equivalent to \(1-2t<m(1-t)^2\); the right side is at least \(m/4>1\), whereas the left side is at most one. Therefore
\[
H_m(h):=h f_m'(h)-f_m(h)
\]
is strictly decreasing, since \(H_m'(h)=h f_m''(h)<0\), and \(H_m(1)=f_m'(1)>0\). This proves at most one positive-reset optimum for the transport contrast, with interior attainment exactly when \(H_m(m/4)<0\).

Write \(q=\sqrt{1-4/m}\). Evaluating the last expression at the gas endpoint yields
\[
H_m(m/4)=G(q)
=\frac{1+q^2}{4}+q+\log(1-q)-\frac{1-q^2}{4}\log(1-q^2).
\]
Its derivative is
\[
G'(q)=-\frac{q^2}{1-q}+\frac q2\log(1-q^2)<0\quad(0<q<1).
\]
Also \(G(0)=1/4\) and \(G(q)\to-\infty\) as \(q\uparrow1\). Therefore exactly one threshold \(q_*\), and hence exactly one \(m_*\), exists, with the stated optimization cases. Bisection gives the reported numerical value, which is illustrative, not needed for the existence proof.

For fixed \(h>1\), \(u_m(h)\to h\), so \(f_m(h)\to\log h\) and \(H_m(h)\to1-\log h\) as \(m\to\infty\). For sufficiently large \(m\), an interior maximizer exists; strict monotonicity of \(H_m\) traps its unique root between any constants below and above \(e\). Thus \(h_*(m)\to e\), and its maximal contrast tends to \(M/(2e)\).

## Verification

The accompanying standalone Python program `verify_transport.py` uses the standard library only. Execute `python3 verify_transport.py` from the directory containing this document. It checks exact inverse-flux quantiles against independent numerical flux integration, independently reconstructs the published Lambert-type stationary density in spatial coordinates, checks the radial tail integrals and exact \(W_1\), tests the positive quantile gap at many parameters, and independently brackets the crowding threshold and the high-crowding limit.

A recorded execution gave 1,070 passing numerical consistency checks, \(m_*=7.32222706837892\ldots\), and at \(m=8\), \(h=1.5\), \(M=2\):
\[
W_\infty=0.18467338469300\ldots,\qquad
W_1=0.15105285647208\ldots.
\]
The complete infinite-parameter assertions follow from the analytic inequalities in the proof. No finite test grid establishes strict ordering for all parameters or uniqueness of a continuous optimum.

## Relationship to prior work

Grange [1], first publicly posted October 19, 2026, derives the steady gas and droplet profiles, interface flux condition, phase coexistence range, liquid mass and nonmonotonic droplet half-width. Those formulas and their kinetic interpretation are **inputs**, not claimed anew. The new comparison proves a strict order between the *two entire coexisting radial laws*, obtains their exact optimal \(W_\infty\) transport gap and \(W_1\), identifies an exact constant displacement of all extreme-tail quantiles, and proves an additional parameter-threshold at \(m_*=7.322227\ldots\) separating boundary from interior maximization of this transport gap. The droplet-radius optimum in [1] is a different observable and does not supply this crowding threshold.

The one-dimensional quantile transport principle is classical [2]; the novelty claim concerns the nontrivial model-specific quantile difference, transport optimization and critical motility parameter. Earlier reset run-and-tumble theory [3] treats a noninteracting process and not coexisting nonlinear gas/droplet stationary branches. General MIPS theory [4] treats the active-particle phase-separation mechanism but not this exact resetting transport geometry. This is a best-knowledge comparison, not proof of publication priority.

## Limitations

The theorem applies to the specific piecewise motility law and symmetric continuum stationary solutions, in the two-solution region \(1<h<m/4\). It does not establish that metastable gas remains physically persistent under fluctuations, quantify finite-particle nucleation, compare time-dependent relaxation, or generalize automatically to smooth motility functions or higher spatial dimension. The endpoint \(h=m/4\) is understood by continuity if one requires a regular positive central gas derivative. The high-crowding limit holds at fixed \(M\), while the model assumptions are otherwise kept unchanged. The finite-speed-reset model of [1] is not asserted here. Exact density formulas already exist in [1], so the new contribution is their global transport comparison and sharp optimization, not a new stationary solution. Unindexed or unpublished analyses could affect priority.

## References

[1] P. Grange, *Motility-Induced Phase Separation of Run-and-Tumble Particles under Local Stochastic Resetting*, arXiv:2610.26149v1 (first posted October 19, 2026), full revised text arXiv:2610.26149v2 (October 20, 2026), https://arxiv.org/html/2610.26149 .

[2] L. De Pascale and J. Louet, *A study of the dual problem of the one-dimensional L-infinity optimal transport problem with applications*, arXiv:1704.02730, https://arxiv.org/abs/1704.02730 . One-dimensional quantile optimal transport is used as standard background.

[3] M. R. Evans and S. N. Majumdar, *Run and tumble particle under resetting: a renewal approach*, arXiv:1808.06450, https://arxiv.org/abs/1808.06450 .

[4] M. E. Cates and J. Tailleur, *Motility-Induced Phase Separation*, arXiv:1406.3533, https://arxiv.org/abs/1406.3533 .
