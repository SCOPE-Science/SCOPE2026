# A sharp rectification-direction switch in a three-site disordered exclusion channel

## Finding
For a three-site open symmetric exclusion chain with departure-rate vector \((t,1,2t)\), \(t>0\), and unit-strength reservoir couplings specified below, let \(J_t(\delta)\) denote stationary left-to-right current under boundary reservoir parameters \(\rho_L=(1+\delta)/2\), \(\rho_R=(1-\delta)/2\). The leading even current is
\[
J_t(\delta)+J_t(-\delta)=2A(t)\delta^2+O_t(\delta^4),
\]
where
\[
A(t)=\frac{4tP(t)}{(t+1)^2(2t+1)^2[324t^3+987t^2+700t+108]^2}
\]
and
\[
\begin{aligned}
P(t)={}&5148t^8-61284t^7-275777t^6-414618t^5\\
&-292561t^4-103752t^3-19176t^2-2304t-144.
\end{aligned}
\]
There is exactly one positive zero \(t_*\) of \(P\), with \(15<t_*<16\) and \(t_*=15.6669537561014\ldots\). Thus the leading rectification is negative for \(0<t<t_*\), zero at \(t=t_*\), and positive for \(t>t_*\). The equilibrium profile is reflection-asymmetric for every \(t>0\), since the first and last departure rates remain unequal. A change of *absolute* outer-rate scale therefore reverses the local rectification direction while preserving their fixed ratio \(1:2\) and the left-right ordering.

This is a minimal-length effect in the unit-hopping-multiplier family: for the analogous two-site chain with any departure rates \(a,c>0\), its quadratic coefficient is
\[
A_2(a,c)=\frac{8ac(a-c)(a^2+6ac+4a+c^2+4c)}{(a+1)^2(c+1)^2(5a+5c+2)^2}.
\]
Consequently a two-site unit-multiplier channel with fixed unequal rate ratio cannot reverse the quadratic rectification sign under common positive rate scaling. No claim is made about arbitrary models with enhanced hopping multipliers, or about full-bias antisymmetry at \(t=t_*\).

## Assumptions and scope
The state space is \(\{0,1\}^n\) with \(n=3\) for the main theorem or \(n=2\) for the comparator. Occupation variables are \(\eta_i\). If adjacent sites have occupations \((1,0)\), the particle jumps right at rate \(a_i\); if they have \((0,1)\), the particle jumps left at rate \(a_{i+1}\). The jumps obey hard-core exclusion. At site \(1\), a particle is inserted if empty at rate \(\rho_L\), or removed if occupied at rate \(a_1(1-\rho_L)\). At site \(n\), the analogous rates are \(\rho_R\) and \(a_n(1-\rho_R)\). For the main claim \((a_1,a_2,a_3)=(t,1,2t)\). The reservoir bias \(\delta\) lies in \((-1,1)\). Current is the expectation of the signed jump rate across the first interior bond:
\[
J_t(\delta)=a_1\mathbb E_{\pi_\delta}[\eta_1(1-\eta_2)]-a_2\mathbb E_{\pi_\delta}[\eta_2(1-\eta_1)].
\]
All rates connecting allowed configurations are positive, so the finite chain has a unique stationary distribution and its current is analytic in a neighborhood of \(\delta=0\). The asymptotic \(O_t\) is for fixed positive \(t\) as \(\delta\to0\), not uniform in \(t\).

## Proof
List configurations lexicographically as \(000,001,010,011,100,101,110,111\), writing the generator in column form \(Q(\delta)=Q_0+\delta Q_1\). Its off-diagonal entries are exactly the transition rates above, and each column sums to zero. At zero bias, detailed balance gives the product equilibrium law
\[
\pi_0(\eta)=Z^{-1}\prod_{i=1}^3a_i^{-\eta_i},\qquad Z=\prod_{i=1}^3(1+a_i^{-1}).
\]
Write the analytic stationary vector as \(\pi_\delta=\pi_0+\delta\pi_1+\delta^2\pi_2+\cdots\), where \(\mathbf1^\top\pi_j=0\) for \(j\ge1\). Substitution into \(Q(\delta)\pi_\delta=0\) yields the uniquely solvable finite linear systems
\[
Q_0\pi_1=-Q_1\pi_0,\qquad Q_0\pi_2=-Q_1\pi_1,
\]
with the displayed normalization. Let \(\ell_\eta=a_1\mathbf1_{(\eta_1,\eta_2)=(1,0)}-a_2\mathbf1_{(\eta_1,\eta_2)=(0,1)}\); the quadratic coefficient is exactly \(\ell^\top\pi_2\). Performing the two rational linear solves with \((a_1,a_2,a_3)=(t,1,2t)\) gives \(\ell^\top\pi_2=A(t)\) as printed in the finding. The accompanying `verify.py` constructs the generator directly from the transition rules and independently reconstructs this rational identity symbolically without a pre-tabulated stationary distribution.

Every denominator factor in \(A(t)\) is positive for \(t>0\). The coefficient sequence of \(P\) in descending powers has one positive entry followed by eight negative entries. Descartes' rule therefore gives at most one positive root, counted with multiplicity; continuity, \(P(0)<0\), and the positive leading term show that one exists. Direct integer substitution gives \(P(15)<0<P(16)\). The sign classification follows. Repeating the same normalized coefficient calculation for \(n=2\) gives the formula for \(A_2(a,c)\); its factor other than \(a-c\) is strictly positive. This proves the fixed-ratio two-site obstruction and the minimality assertion within the specified unit-multiplier family.

## Verification
Run `python verify.py` with Python 3 and SymPy installed. The standalone checker builds the two- and three-site generators from the stated transition rules, solves successive stationary-perturbation equations in exact rational functions, and compares the resulting coefficients against the claimed identities. It verifies the sign pattern of the degree-eight polynomial and numerically locates its single positive root. This is a finite symbolic certificate for the displayed rational formulas, not a replacement for the analytic existence, uniqueness, and sign arguments.

## Relationship to prior work
Sakai and Akimoto (arXiv:2609.03560, first public 2026-09-03) study the boundary-driven site-disordered exclusion process and approximate nonlinear current response, motivating an exact finite-channel sign test. Their reflection-symmetry obstruction and general phenomenon of sample-dependent rectification are **prior work**, not claimed here. Their earlier arXiv:2512.03316 studies bias reversal under bulk field driving, a different driving protocol. Exact two-site nonlinear response with an independently adjustable hopping multiplier and exact four-site single-defect response are also known in accessible earlier research; those formulations are not the new three-site, unit-multiplier, fixed-outer-ratio threshold. The present claim is limited to the explicit algebraic switch and its unit-multiplier two-site comparison, not to a new universal theory of rectification or to the general sufficiency of reflection asymmetry.

## Limitations
The result classifies only the leading even coefficient near equal baths at mean parameter \(1/2\). At \(t_*\), quadratic cancellation says nothing about whether higher even terms vanish: it is **not** a proof of exact full-bias antisymmetry. No thermodynamic limit, generic disorder ensemble, time-dependent observable, or high-bias global sign classification is asserted. The finite-channel algebra depends on the explicit boundary coupling convention and should not be transferred to different reservoir normalizations without re-derivation. The motivating source's complete full text was unavailable for inspection; an unindexed exact finite-chain treatment remains a priority risk.

## References
1. I. Sakai and T. Akimoto, *Sample-specific rectification-like response in a boundary-driven exclusion process*, arXiv:2609.03560v1 (2026-09-03), https://arxiv.org/abs/2609.03560.
2. I. Sakai and T. Akimoto, *Symmetry Breaking of Current Response in Disordered Exclusion Processes*, arXiv:2512.03316v1 (2025-12-03), https://arxiv.org/abs/2512.03316; Phys. Rev. E 113, 044123 (2026).
3. B. Derrida, B. Douçot and P.-E. Roche, *Current fluctuations in the one-dimensional symmetric exclusion process with open boundaries*, Journal of Statistical Physics 115 (2004), 717–748.
4. T. Chou, *How fast do fluids squeeze through microscopic single-file pores?*, Physical Review Letters 80 (1998), 85–88.
