# Identical mean-squared displacements but strictly different fourth cumulants in active Brownian dimers

## Finding

Consider two stationary nonreciprocal-force mechanisms for the same overdamped bound pair: a continuous Ornstein–Uhlenbeck stiffness asymmetry (G) and a symmetric telegraph stiffness asymmetry (T). Match their two-time covariances exactly. The resulting center-of-mass displacements have the **same mean and mean-squared displacement at every time**, but for every observation duration \(T>0\) their fourth cumulants obey a strict ordering, with exact integral formulas, a universal long-time ratio, and inequivalent finite-time exponential-moment domains.

For \(a,b,A,B>0\), let \(c=a+b\) and define
\[
F_{c,d}(T)=\int_{\substack{x,y,z\geq0\\x+y+z<T}}(T-x-y-z)e^{-c(x+z)-dy}\,dx\,dy\,dz,\qquad d>0.
\]
Then
\[
\begin{aligned}
\kappa_4^{\mathrm G}(T)&=48A^2B^2\bigl(F_{c,2a}(T)+F_{c,2b}(T)+F_{c,2c}(T)\bigr),\\
\kappa_4^{\mathrm T}(T)&=48A^2B^2\bigl(F_{c,2a}(T)-F_{c,2c}(T)\bigr).
\end{aligned}
\]
In particular, \(0<\kappa_4^{\mathrm T}(T)<\kappa_4^{\mathrm G}(T)\) for **every** \(T>0\). Moreover,
\[
\begin{aligned}
\lim_{T\to\infty}\frac{\kappa_4^{\mathrm G}(T)}{T}
&=\frac{24A^2B^2}{c^2}\left(\frac1a+\frac1b+\frac1c\right),\\
\lim_{T\to\infty}\frac{\kappa_4^{\mathrm T}(T)}{T}
&=\frac{24A^2B^2}{c^2}\left(\frac1a-\frac1c\right),
\end{aligned}
\]
so the ratio of these strictly positive growth coefficients equals
\[
1+3\frac ab+\left(\frac ab\right)^2.
\]
At equal relaxation rates \(a=b\), it is exactly \(5\). For every finite \(T>0\), the telegraph displacement has exponential moments of all real orders, whereas the Gaussian-stiffness displacement has a finite nonzero exponential-moment radius, specified exactly in the proof.

## Assumptions and scope

Fix \(a,b,A,B>0\) and \(D_x\geq0\). Let \(Y\) be a centered stationary real Ornstein–Uhlenbeck process with \(\mathbb E[Y_sY_t]=Ae^{-a|t-s|}\). Independently, define two centered stationary processes: \(U^{\mathrm G}\), a real Ornstein–Uhlenbeck process with covariance \(Be^{-b|t-s|}\); and \(U^{\mathrm T}_t=\sqrt B S_t\), where \(S\) is a stationary symmetric sign process switching at rate \(b/2\). Both are independent of a standard Brownian motion \(W\). Each mechanism uses an independent copy of the appropriate process and the same laws for \(Y\) and \(W\). Define, for every deterministic \(T\geq0\),
\[
X^{j}_T=\sqrt{D_x}\,W_T-\int_0^T U^{j}_tY_t\,dt,\qquad j\in\{\mathrm G,\mathrm T\}.
\]
The cumulant convention is \(\kappa_4(X)=\mathbb E[(X-\mathbb EX)^4]-3\operatorname{Var}(X)^2\). Time is physical and the stationary force processes are initialized at time zero. No repulsive interparticle potential is present.

These laws are precisely the maximally anticorrelated continuous and synchronized discrete stiffness limits of the unrepelled dimer in Cocconi–Alston–Bertrand, equations (2), (11), and (17), under
\[
a=2\bar k,\qquad b=\mu=2\lambda,\qquad
A=D_x/\bar k,\qquad B=D_\kappa/\mu=\kappa_0^2,
\]
with \(D_x>0\), \(\bar k>0\), \(D_\kappa>0\), and \(\lambda>0\). Their force-asymmetry variable is \(\psi=2U\); the center-of-mass drift is \(-UY\).

## Proof

**1. Matched mean-squared displacements.** Each drift \(V_t=U_tY_t\) has zero mean and covariance \(\mathbb E[V_sV_t]=ABe^{-c|t-s|}\), independent of the mechanism. The Brownian increment is independent and centered. Twice integrating the triangular covariance yields, for every \(T\geq0\),
\[
\mathbb EX^{j}_T=0,\qquad
\operatorname{Var}(X^{j}_T)=D_xT+2AB\left(\frac{T}{c}-\frac{1-e^{-cT}}{c^2}\right).
\]
In particular the entire MSD curve is identical, not merely its diffusive limit.

**2. Ordered four-point cumulant.** Take four ordered observation times \(t_1\leq t_2\leq t_3\leq t_4\), with successive gaps \(x=t_2-t_1\), \(y=t_3-t_2\), \(z=t_4-t_3\). Wick's formula gives
\[
\mathbb E[Y_{t_1}Y_{t_2}Y_{t_3}Y_{t_4}]
=A^2e^{-a(x+z)}(1+2e^{-2ay}).
\]
The Gaussian asymmetry satisfies the same formula with \((A,a)\) replaced by \((B,b)\), whereas independent Poisson switching increments give
\[
\mathbb E[U^{\mathrm T}_{t_1}U^{\mathrm T}_{t_2}U^{\mathrm T}_{t_3}U^{\mathrm T}_{t_4}]
=B^2e^{-b(x+z)}.
\]
Subtracting all three covariance pairings of \(V_t=U_tY_t\), whose pair covariance is \(ABe^{-c|t-s|}\), yields the ordered connected four-point functions
\[
\begin{aligned}
\operatorname{cum}_4(V^{\mathrm G}_{t_1},\ldots,V^{\mathrm G}_{t_4})
&=2A^2B^2e^{-c(x+z)}\bigl(e^{-2ay}+e^{-2by}+e^{-2cy}\bigr),\\
\operatorname{cum}_4(V^{\mathrm T}_{t_1},\ldots,V^{\mathrm T}_{t_4})
&=2A^2B^2e^{-c(x+z)}\bigl(e^{-2ay}-e^{-2cy}\bigr).
\end{aligned}
\]
These formulas also hold by continuity when gaps vanish. Since \(b>0\), \(a<c\), and \(y>0\), the telegraph integrand is positive except on a null boundary; the difference between Gaussian and telegraph integrands is everywhere strictly positive in the interior.

**3. Integration and asymptotics.** All fourth moments exist on finite intervals. Multilinearity of cumulants and Fubini's theorem integrate the connected four-point function over \([0,T]^4\); adding the independent Gaussian Brownian increment changes no cumulant of order four. The \(4!\) ordering chambers contribute equally, and integrating the first observation time produces the factor \(T-x-y-z\). Thus the preceding connected formulas give exactly the stated two \(F\)-combinations. Their difference is
\[
\kappa_4^{\mathrm G}(T)-\kappa_4^{\mathrm T}(T)
=48A^2B^2\bigl(F_{c,2b}(T)+2F_{c,2c}(T)\bigr)>0.
\]
Similarly \(F_{c,2a}-F_{c,2c}>0\), proving the other strict inequality. To obtain the long-time limits, divide each nonnegative defining integral by \(T\), extend to the positive octant, and use dominated convergence: for every \(d>0\),
\[
\lim_{T\to\infty}\frac{F_{c,d}(T)}T
=\left(\int_0^\infty e^{-cx}\,dx\right)^2
\left(\int_0^\infty e^{-dy}\,dy\right)=\frac{1}{c^2d}.
\]
Substitution gives the coefficients and ratio as stated. As \(T\downarrow0\), an additional direct expansion gives
\[
\kappa_4^{\mathrm G}(T)\sim6A^2B^2T^4,\qquad
\kappa_4^{\mathrm T}(T)\sim\frac45 A^2B^2bT^5.
\]

**4. Exponential-moment separation.** On \(L^2([0,T])\), let \(C_U\) and \(C_Y\) be the covariance integral operators with kernels \(Be^{-b|s-t|}\) and \(Ae^{-a|s-t|}\). Both are positive trace-class operators. The positive operator
\[
K_T=C_U^{1/2}C_YC_U^{1/2}
\]
is nonzero, because \(\operatorname{tr}K_T=\int_0^T\int_0^T ABe^{-c|s-t|}\,ds\,dt>0\). Put \(\rho_T=\|K_T\|>0\). Conditioning on the Gaussian path \(U^{\mathrm G}\) and using the Gaussian quadratic-form identity gives
\[
\mathbb E[e^{\theta X^{\mathrm G}_T}]
=e^{D_x\theta^2T/2}\det(I-\theta^2K_T)^{-1/2},\qquad
|\theta|<\rho_T^{-1/2}.
\]
At \(|\theta|\geq\rho_T^{-1/2}\), the expectation diverges: in a top eigenfunction direction the Gaussian squared exponential is nonintegrable, including at equality. By contrast, for every telegraph path \(\|U^{\mathrm T}\|_2^2=BT\). The Schur bound \(\|C_Y\|\leq2A/a\) gives a conditional Gaussian variance at most \(2ABT/a\). Consequently, for every real \(\theta\),
\[
\mathbb E[e^{\theta X^{\mathrm T}_T}]
\leq\exp\left[\frac{\theta^2T}{2}\left(D_x+\frac{2AB}{a}\right)\right]<\infty.
\]
This proves the finite-time domain distinction and completes the theorem.

## Verification

A standalone Python checker, `check.py`, evaluates the defining positive integrals, separately reconstructs all four-point cumulants from Wick pairings and telegraph increments, tests the strict differences, verifies short- and long-time limits, and compares the Gaussian fourth cumulant against a discretized covariance-operator trace. It passed 193 numerical and algebraic diagnostics, including three independent Nyström trace comparisons; numerical tests are consistency checks, not substitutes for the proof.

For reproducibility, a useful one-dimensional representation of the integral is
\[
F_{c,d}(T)=\int_0^T se^{-cs}\left[\frac{T-s}{d}-\frac{1-e^{-d(T-s)}}{d^2}\right]ds.
\]
The embedded files `check.py` and `requirements.txt` give the exact numerical procedure and dependencies.

## Relationship to prior work

Cocconi, Alston, and Bertrand (2023), equations (2), (11), and (17) and supplementary derivations, establish the underlying two-particle dynamics, stationary product drift and the two MSD laws for continuous and discrete interaction fluctuations. Those dynamics and second moments are **not** claimed here as new. The assessed additional result is the all-time fourth-cumulant inequality and explicit formulas, long-time ratio, and finite-time moment-domain split after **matching** the two force covariances.

Shee and Chaudhuri (2021) derive fourth displacement moments in an active Brownian particle with OU speed and orientation diffusion, but its orientation process and driving geometry differ from the telegraph/OU stiffness product here. Sarkar, Santra, and Basu (2022/2023) compare active driving noise classes in a harmonic chain, using different harmonic-reservoir observables, not the present dimer theorem. Patel, Shee, and Chaudhuri (2024) derive fourth position moments in a trapped active model with speed and angular orientation fluctuations rather than two matched dimer stiffness mechanisms. General Gaussian quadratic-form identities supply a proof tool for the moment-domain statement but do not by themselves state the full paired dynamical comparison.

## Limitations

The theorem uses stationary forcing, exact independence of the stiffness asymmetry and harmonic relative coordinate, no steric repulsion, zero mean asymmetry, and fixed positive relaxation rates. It does not classify general asymmetry correlations, repulsive interactions, or finite-sample statistical estimation error. Its originality is assessed against the inspected sources and accessible research records; priority against unindexed equivalent derivations remains subject to independent literature review. No full large-deviation rate function is claimed.

## References

1. L. Cocconi, H. Alston, and T. Bertrand, *Active Bound States Arise From Transiently Nonreciprocal Pair Interactions*, arXiv:2304.07738v1, first posted 2023-04-16; Phys. Rev. Research **5**, 043032 (2023). https://arxiv.org/abs/2304.07738
2. D. Shee and D. Chaudhuri, *Active Brownian motion with speed fluctuations in arbitrary dimensions: exact calculation of moments and dynamical crossovers*, arXiv:2108.12228 (2021). https://arxiv.org/abs/2108.12228
3. R. Sarkar, I. Santra, and U. Basu, *Stationary states of activity-driven harmonic chains*, arXiv:2210.09035 (2022); Phys. Rev. E **107**, 014123 (2023). https://arxiv.org/abs/2210.09035
4. P. Patel, D. Shee, and D. Chaudhuri, *Dynamical metastability and re-entrant localization of trapped active elements with speed and orientation fluctuations*, arXiv:2410.22004 (2024). https://arxiv.org/abs/2410.22004
