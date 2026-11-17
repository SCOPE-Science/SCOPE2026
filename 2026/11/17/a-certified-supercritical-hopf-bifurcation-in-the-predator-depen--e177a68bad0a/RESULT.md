# A certified supercritical Hopf bifurcation in the predator-dependent replicator flow

## Finding

For the positive-payoff two-prey/one-predator replicator flow specified below, there is exactly one interior coexistence equilibrium at which a conjugate pair of Jacobian eigenvalues is purely imaginary as the carrying capacity varies. This point is a **nondegenerate supercritical Hopf bifurcation**. Its carrying-capacity threshold lies in
\[
1.6617073473533870<K_*<1.6617073473536950.
\]
For all sufficiently small \(K-K_*>0\), there exists a locally orbitally asymptotically stable nonconstant periodic solution with both prey types and predator strictly positive. For \(K<K_*\) sufficiently close, the coexistence equilibrium is locally exponentially stable; on crossing \(K_*\), it loses stability in a complex-conjugate pair. The first Lyapunov coefficient for the explicitly defined normalization in the proof has a validated interval enclosure
\[
-5.877089159<\ell_1<-5.877089130<0.
\]
This verifies an attracting periodic-orbit onset for the positive-parameter case where earlier computations had indicated a bifurcation near carrying capacity \(1.66\).

## Assumptions and scope

Let the prey frequency satisfy \(0<x<1\), total prey abundance \(p>0\), and predator density \(y>0\). Let the positive carrying-capacity parameter be \(K\), and set predator conversion coefficient \(\beta=2\). Use the birth-payoff matrix with rows \((16/5,3/4)\) and \((3,4/5)\), and the predation-payoff matrix with rows \((1/2,3/5)\) and \((7/20,3/10)\). Writing
\[
\begin{aligned}
 u(x)&=(5x-1)/20, &v(x)&=3(2-x)/20,\\
 r(x)&=(5x^2+43x+16)/20, &\delta(x)&=(3-x)(3x+2)/20,
\end{aligned}
\]
consider the smooth polynomial differential equation
\[
\begin{aligned}
 \dot x&=x(1-x)[u(x)-v(x)y],\\
 \dot p&=p[r(x)-p/K-\delta(x)y],\\
 \dot y&=2y[-1+\delta(x)p].
\end{aligned}
\]
The claim is local to the strictly positive coexistence branch and a neighborhood of its Hopf point. In particular it does not assert that the periodic orbit is unique globally, that all positive trajectories converge to it, or that no other periodic orbits exist for other capacities.

## Proof

**1. Exact coexistence branch.** A positive equilibrium must have \(u(x)=v(x)y\) and \(\delta(x)p=1\). Hence
\[
 y=m(x)=\frac{5x-1}{3(2-x)},\qquad p=\frac1{\delta(x)}.
\]
The physical domain is \(1/5<x<1\). The remaining equilibrium equation gives \(K=\kappa(x)=[\delta(x)F(x)]^{-1}\), where
\[
 F(x)=r(x)-\delta(x)m(x)=\frac{137x^2-187x-102}{60(x-2)},
\]
and consequently
\[
 \kappa(x)=\frac{-1200(x-2)}{(x-3)(3x+2)(137x^2-187x-102)}.
\]
On the physical interval, \(m,F,\delta,\kappa\) are positive.

**2. A unique imaginary-pair candidate.** Differentiate the three displayed differential equations with respect to \((x,p,y)\), and only then substitute \((p,y,K)=(1/\delta(x),m(x),\kappa(x))\). For the resulting Jacobian \(J(x)\), write its characteristic polynomial as \(\lambda^3+a_1(x)\lambda^2+a_2(x)\lambda+a_3(x)\), with \(a_1=-\operatorname{tr}J\), \(a_2\) the sum of its three principal minors of order two, and \(a_3=-\det J\). Direct exact rational elimination yields
\[
 a_1a_2-a_3=\frac{Q(x)}{36000(x-3)(x-2)^3(3x+2)},
\]
where
\[
\begin{aligned}
 Q(x)={}&67455x^8-1105515x^7+5246054x^6-9041754x^5\\
 &+3370659x^4+3356225x^3-826776x^2\\
 &+296532x-146880.
\end{aligned}
\]
A rational Sturm-sequence computation shows that \(Q\) has exactly one root in \((1/5,1)\), and that this root \(x_*\) satisfies
\[
\frac{3381326771974}{10^{13}}<x_*<\frac{3381326771975}{10^{13}}.
\]
On this rational bracket, outward-rounded rational-function interval arithmetic proves \(a_1,a_2,a_3>0\), \((a_1a_2-a_3)'>0\), and \(\kappa'<0\). Consequently the characteristic polynomial factors at \(x_*\) as \((\lambda+a_1)(\lambda^2+a_2)\); the eigenvalues are \(-a_1<0\) and \(\pm i\sqrt{a_2}\). The carrying capacity \(K_*=\kappa(x_*)\) belongs to the stated enclosure. If \(\Lambda(K)\) is the eigenvalue with positive imaginary part, implicit differentiation of the cubic gives
\[
 \left.\frac{d\operatorname{Re}\Lambda}{dK}\right|_{K_*}
 =-\frac{(a_1a_2-a_3)'(x_*)}{2[a_1(x_*)^2+a_2(x_*)]\kappa'(x_*)}>0.
\]
Thus the crossing is transversal and has the stated direction. There is no other imaginary-pair Hopf candidate along this positive branch.

**3. The cubic normal-form sign.** Write \(\omega=\sqrt{a_2(x_*)}\), and let \(B\) and \(C\) be the symmetric bilinear and trilinear forms furnished by the second and third derivatives of the *original* vector field at equilibrium (without factorial denominators). Choose a right eigenvector \(q\) of \(J\) for \(i\omega\), normalized by \(q_1=1\). Let \(\Pi\) denote spectral projection onto that eigendirection:
\[
 \Pi=\frac{(J+a_1I)(J+i\omega I)}{(a_1+i\omega)(2i\omega)}.
\]
In this normalization, the conventional first Lyapunov coefficient is
\[
\ell_1=\frac1{2\omega}\operatorname{Re}
\left[\Pi\left(C(q,q,\bar q)-2B\big(q,J^{-1}B(q,\bar q)\big)
+B\big(\bar q,(2i\omega I-J)^{-1}B(q,q)\big)\right)\right]_1.
\]
This formula follows from the standard cubic Hopf normal form. The accompanying verifier forms every derivative symbolically from the displayed vector field, performs the rational Sturm tests, and evaluates the full expression with outward-rounded complex interval arithmetic over the *entire* isolating bracket for \(x_*\). It establishes
\[
 -5.877089159<\ell_1<-5.877089130.
\]
Both nondegeneracy inequalities are therefore strict: the crossing speed is positive and \(\ell_1<0\). The classical Hopf theorem gives the asserted small, attracting periodic orbits for \(K>K_*\) and the stable equilibrium for \(K<K_*\), locally. Since the equilibrium is strictly interior, the sufficiently small cycles remain strictly biologically positive.

## Verification

Run `python verify_hopf.py` with SymPy and mpmath installed (see `requirements.txt`). The program reconstructs \(J,B,C\), prints the exact rational eighth-degree polynomial \(Q\), certifies one root in the physical interval by Sturm counts, isolates it by rational opposite-sign endpoints, checks positivity of all required coefficients and derivatives by interval arithmetic, computes the two-sided carrying-capacity bracket, and encloses the normal-form coefficient using interval Cramer's-rule solves. Its final marker is `VERIFY_OK` and the certified Lyapunov interval is strictly negative. These checks are algorithmic certificates for the displayed rational model, not numerical simulation or an independent mathematical audit.

## Relationship to prior work

Cruz and Neves, *Predator-dependent replicator dynamics or a predator-prey model with two prey types and frequency dependence* (arXiv:2607.13281v1, 2026-07-14), supply the model, its positive payoffs, the coexistence-branch framework and numerical evidence of a Hopf transition at about \(K=1.66\). Their discussion explicitly leaves a rigorous periodic-orbit existence proof open. The present contribution supplies that proof for the specified Scenario 8, including an exact algebraic threshold, a verified transversal crossing, and a validated negative first Lyapunov coefficient. Braga and Wardil's original predator-dependent replicator formulation is acknowledged; neither its general framework nor classical Hopf theory is claimed as new. An earlier stability-exchange result for boundary coexistence collisions addresses a different phenomenon and does not imply the interior Hopf sign or existence of a stable cycle.

## Limitations

The theorem fixes the two payoff matrices and conversion parameter. It proves a local Hopf onset, not a global cycle classification; it does not determine basin size, the maximal parameter interval of cycle persistence, or a complete classification of all steady states. The first Lyapunov coefficient is reported for the explicitly stated eigenvector normalization. Independent review and exhaustive historical-priority verification have not occurred.

## References

1. C. Cruz and R. Neves, *Predator-dependent replicator dynamics or a predator-prey model with two prey types and frequency dependence*, arXiv:2607.13281v1 (2026), https://arxiv.org/abs/2607.13281.
2. G. Braga and M. Wardil, *The predator-dependent replicator dynamics*, Journal of Physics A: Mathematical and Theoretical (2022), DOI:10.1088/1751-8121/ac40e4.
3. Y. A. Kuznetsov, *Elements of Applied Bifurcation Theory*, Springer, for the standard Hopf normal-form coefficient and theorem.
