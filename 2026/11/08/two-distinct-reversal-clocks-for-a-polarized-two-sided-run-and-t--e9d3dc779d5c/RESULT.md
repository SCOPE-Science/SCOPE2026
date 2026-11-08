# Two distinct reversal clocks for a polarized two-sided run-and-tumble gas

## Finding

Consider independent one-dimensional telegraph particles at speed \(v>0\), with sign reversals occurring at Poisson rate \(\gamma>0\). At initial time, each half-line carries an independent homogeneous Poisson cloud: density \(\rho_L>\rho_R>0\) to the left and right of the origin. Initial velocity signs are independent, with means \(m_L,m_R\in[-1,1]\) on the respective half-lines. All signs subsequently flip at rate \(\gamma\).

Write \(\Delta=\rho_L-\rho_R>0\), \(P=\rho_Lm_L+\rho_Rm_R\), and \(x=\gamma t\). Let \(Q(t)\) be the number of particles initially on the left and located on the right at time \(t\), minus the number initially on the right and located on the left. This is integrated transfer, not the total count of repeated pathwise crossings. Define \(\mathcal J(t)=\frac{d}{dt}\mathbb E Q(t)\), and let \(I_0,I_1\) denote the modified Bessel functions of orders zero and one.

For each \(t>0\), \(Q(t)\) has the Skellam law (the difference of independent Poisson variables) with parameters
\[
\mu_+(t)=\frac{\rho_L}{2}\bigl(V(t)+m_LM(t)\bigr),\qquad
\mu_-(t)=\frac{\rho_R}{2}\bigl(V(t)-m_RM(t)\bigr),
\]
where
\[
V(t)=vt e^{-x}[I_0(x)+I_1(x)],\qquad
M(t)=\frac v{2\gamma}(1-e^{-2x}).
\]
Consequently
\[
\mathbb E Q(t)=\tfrac12[\Delta V(t)+P M(t)],\qquad
\mathcal J(t)=\frac v2[\Delta e^{-x}I_0(x)+P e^{-2x}].
\]

There is a sharp dichotomy. If \(P\ge-\Delta\), then \(\mathcal J(t)>0\) and \(\mathbb E Q(t)>0\) for all \(t>0\). If \(P<-\Delta\), then \(\mathcal J\) reverses from negative to positive exactly once at \(t_J=x_J/\gamma\), and \(\mathbb E Q\) reverses from negative to positive exactly once at a strictly later time \(t_Q=x_Q/\gamma\). Put \(c=\Delta/(-P)\in(0,1)\); the two crossing locations are the unique positive solutions of
\[
e^{x_J}I_0(x_J)=c^{-1},\qquad
\frac{\sinh x_Q}{x_Q[I_0(x_Q)+I_1(x_Q)]}=c,
\quad 0<x_J<x_Q.
\]
For weak density contrast relative to adverse initial polarization, \(c\downarrow0\),
\[
x_J=\frac12\log\frac1c+\frac14\log\log\frac1c+\frac14\log\pi+o(1),
\qquad x_Q\sim\frac{\pi}{8c^2}.
\]
At onset, \(c\uparrow1\), one instead has \(x_J\sim1-c\) and \(x_Q\sim2(1-c)\). In particular, the two reversal clocks separate by an unbounded factor as the opposing density gradient tends to zero.

## Assumptions and scope

All statements hold for every fixed \(v,\gamma>0\), every \(\rho_L>\rho_R>0\), and every \(m_L,m_R\in[-1,1]\). The Poisson clouds, initial orientations, and the independent sign-flip processes are mutually independent. Each half-line is spatially unbounded. There are no particle interactions, positional resets, external potentials, or particle losses. The current is *net endpoint transfer* between the two sides of the origin, not a count of all path crossings. At \(t=0\) the current sign statements are interpreted by their right limits.

## Proof

**1. Independent one-particle displacements.** Starting with initial velocity \(+v\), let \(X_t\) be the signed displacement. Since the conditional expected velocity is \(ve^{-2\gamma s}\),
\[
\mathbb E X_t=M(t)=\frac v{2\gamma}(1-e^{-2\gamma t}).
\]
An initial negative sign negates the displacement law, so the absolute first moment \(V(t)=\mathbb E|X_t|\) is independent of the initial sign.

For completeness, condition on the number \(N\) of sign flips, Poisson with mean \(x=\gamma t\). Given \(N=n\ge1\), the \(n+1\) successive holding-time fractions are uniform on the simplex. The fraction of positive-running time is Beta-distributed with parameters \((\lceil(n+1)/2\rceil,\lfloor(n+1)/2\rfloor)\). Direct beta integration gives
\[
\mathbb E[|X_t|\mid N=0]=vt,\quad
\frac{\mathbb E[|X_t|\mid N=2k-1]}{vt}
=\frac{\mathbb E[|X_t|\mid N=2k]}{vt}
=\frac{\binom{2k}{k}}{4^k},\quad k\ge1.
\]
One can verify the integral for even counts from the symmetric Beta\((k,k)\) case: weighting its density by \(2u\) makes Beta\((k+1,k)\), but leaves expectations of the symmetric function \(|2u-1|\) unchanged. Summing the Poisson probabilities and using the defining positive series for \(I_0\) and \(I_1\) yields
\[
V(t)=vt e^{-x}\left[\sum_{k=0}^{\infty}\frac{x^{2k}}{4^k(k!)^2}+
\sum_{k=0}^{\infty}\frac{x^{2k+1}}{2^{2k+1}k!(k+1)!}\right]
=vt e^{-x}[I_0(x)+I_1(x)].
\]
The standard Bessel derivative identities give \(V'(t)=ve^{-x}I_0(x)\) and \(M'(t)=ve^{-2x}\).

**2. Poisson transfer.** A particle starting at \(-y<0\) finishes on the positive half-line exactly when its displacement exceeds \(y\). Campbell's formula and Tonelli's theorem give \(\rho_L\mathbb E[X_t^+]\) for the mean number transferred from left to right. Its displacement has expectation \(m_LM(t)\), so \(\mathbb E[X_t^+]=(V+m_LM)/2\). Similarly the right-to-left mean is \(\rho_R(V-m_RM)/2\). Independent Poisson marking/thinning implies that these two counts are independent Poisson variables; their difference is Skellam. Differentiating proves the two displayed mean formulas.

**3. Instantaneous reversal.** Multiplying \(\mathcal J(t)\) by the positive factor \(2e^{2x}/v\) shows that its sign is the sign of
\[
F(x)=\Delta e^xI_0(x)+P.
\]
Since \(I_0(x)>0\), \(I_1(x)>0\), and \(\frac{d}{dx}(e^xI_0(x))=e^x(I_0(x)+I_1(x))>0\), the function \(F\) is strictly increasing from \(F(0)=\Delta+P\) to infinity. Thus it has exactly one positive zero precisely when \(P<-\Delta\), and no zero otherwise. If \(P=-\Delta\), \(F(0)=0\) but \(F(x)>0\) for every \(x>0\).

**4. Cumulative reversal and uniqueness.** The ratio
\[
R(x)=\frac{M(t)}{V(t)}=\frac{\sinh x}{x[I_0(x)+I_1(x)]}
\]
is strictly decreasing on \((0,\infty)\), from \(R(0+)=1\) to \(R(\infty)=0\). Indeed, using \(I_0'=I_1\) and \(I_1'=I_0-I_1/x\),
\[
\frac{xR'(x)}{R(x)}=\frac{2x}{e^{2x}-1}-\frac{I_0(x)}{I_0(x)+I_1(x)}.
\]
The positive power series gives \(I_1(x)\le (x/2)I_0(x)\), whereas \(e^{2x}-1>2x+2x^2\) for every \(x>0\). Hence
\[
\frac{2x}{e^{2x}-1}<\frac1{1+x}<\frac1{1+x/2}\le\frac{I_0(x)}{I_0(x)+I_1(x)},
\]
so \(R'(x)<0\). For \(P<-\Delta\), the sign of \(\mathbb E Q\) is that of \(c-R(x)\), yielding exactly one crossing \(x_Q\). Because \(\mathbb E Q(0)=0\), \(\mathcal J\) is initially negative and becomes positive only after \(x_J\), while \(\mathbb E Q\) grows unboundedly positive at large \(t\); therefore its zero occurs strictly after the unique minimum at \(x_J\). When \(P\ge-\Delta\), positive \(\mathcal J\) implies positive cumulative transfer.

**5. Sharp edge scales.** The classical positive-axis modified-Bessel expansion gives \(I_0(x)=e^x(2\pi x)^{-1/2}(1+O(x^{-1}))\) and \(I_1(x)=e^x(2\pi x)^{-1/2}(1+O(x^{-1}))\). Taking logarithms in \(e^{x_J}I_0(x_J)=c^{-1}\) and solving once by substitution yields
\[
x_J=\tfrac12L+\tfrac14\log L+\tfrac14\log\pi+o(1),\quad L=\log(1/c).
\]
The same Bessel expansions yield \(R(x)=\sqrt{\pi/(8x)}(1+O(x^{-1}))\), hence \(x_Q\sim\pi/(8c^2)\). As \(x\downarrow0\), \(e^xI_0(x)=1+x+O(x^2)\) and \(R(x)=1-x/2+O(x^2)\), which give the onset asymptotics.

## Verification

The accompanying `check.py` computes \(\mathbb E|X_t|\) independently by conditioning on the Poisson flip count and integrating Beta holding-time fractions; it compares this against the Bessel expression at six dimensionless times. It then checks six pairs of independent numerical root solves, strict root order, mean-current signs at five times, and seven analytic inequality probes. Every check passed in a SciPy-equipped environment. These computations test formulas at finitely many points; the infinite-domain conclusions rely on the preceding proof.

## Relationship to prior work

Britton, Zhang, Han, and Bertrand (2026) develop orientation-dependent run-and-tumble dynamics and spatial/orientational observables. Jose, Rosso, and Ramola (2023) establish exact one-sided current statistics with initial magnetization and give Bessel expressions for the relevant telegraph first moments. The present theorem uses those established microscopic ingredients but asks a different, two-sided step-initial question: a left-to-right density gradient opposing unequal initial directional preferences. Its new assertion is the complete sign diagram for *both* instantaneous and integrated currents, exact uniqueness of two crossing times, and their parametrically distinct logarithmic versus inverse-square scales. A standard one-sided cloud cannot exhibit the adverse-polarization regime \(P<-\Delta\).

## Limitations

The result describes independent particles on the full line and net endpoint transfer, not interacting active matter, non-Poisson spatial ensembles, pathwise total crossing counts, or Brownian translational noise. The limiting formulas concern mean behavior and do not claim that individual Skellam realizations reverse at deterministic times. The source papers' publicly indexed abstracts and extracted passages were accessible, but complete texts of some highly relevant sources could not be inspected; potentially more general unindexed results remain a publication-priority risk. No independent external review has been performed.

## References

- C. Britton, Z. Zhang, S. Han, and T. Bertrand, *Run-and-tumble particles with preferred reorientation*, arXiv:2608.23519 (first posted 2026-08-24), https://arxiv.org/abs/2608.23519.
- S. Jose, A. Rosso, and K. Ramola, *Effect of initial conditions on current fluctuations in non-interacting active particles*, arXiv:2310.16811 (2023), https://arxiv.org/abs/2310.16811.
- S. Jose, A. Rosso, and K. Ramola, *Generalized disorder averages and current fluctuations in run and tumble particles*, Physical Review E 108 (2023), L052601, https://doi.org/10.1103/PhysRevE.108.L052601.
- E. Aghion and R. K. Singh, *Spatial density, first passage times, and entropy of run and tumble particles in a bistable potential*, arXiv:2610.08029 (2026), https://arxiv.org/abs/2610.08029 (related context only; different potential setup).
