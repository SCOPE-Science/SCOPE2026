# Critical logarithmic spreading and exact diffusion amplitudes for reinforced run–rest transport

## Finding

For a persistent finite-speed walk with self-reinforcing directional choices after exponential rests, the **diffusive–superdiffusive phase boundary is logarithmically superdiffusive**. In the notation below, the exact limiting laws are

\[
\lim_{t\to\infty}\frac{\mathbb E X_t^2}{t}=\frac{C}{1-\theta}\quad(0<\theta<1),
\qquad
\lim_{t\to\infty}\frac{\mathbb E X_t^2}{t\log(\lambda t)}=C\quad(\theta=1),
\]

where \(C=\frac{2v^2}{\lambda}(1-\lambda/\gamma)>0\). The critical equality is feasible for strictly positive rates precisely when \(\lambda/\eta<2/3\), at the choice \(\alpha_0=\frac13+\frac{\lambda}{2\eta}\). For fixed \(\lambda,\eta,v\), the subcritical effective diffusion coefficient \(D_{\mathrm{eff}}=C/[2(1-\theta)]\) diverges as the critical reinforcement approaches from below. At criticality the diffusivity is not a finite constant: the mean-square displacement grows as \(t\log t\), strictly between linear and any fixed power larger than one.

## Assumptions and scope

Take \(v,\lambda,\eta>0\), \(0<\alpha_0<2/3\), and time \(t>0\). A particle at position \(X_t\) moves at velocity \(+v\) or \(-v\) until a Poisson event of rate \(\lambda\) puts it at rest. While at rest, rate-\(\eta\) events choose a new state with probabilities

\[
r_\pm(x,t)=\frac13\pm\frac{\alpha_0 x}{2vt},\qquad r_0=\frac13.
\]

All choices are well-defined because \(|X_t|\le vt\). A rest-to-rest event does not change the state. Initially \(X_0=0\), there is no resting mass, and each initial moving orientation has probability \(1/2\). Define

\[
\gamma=\lambda+\frac{2\eta}{3},\quad
\theta=\frac{2\alpha_0\eta}{\gamma},\quad
M(t)=\mathbb E(X_t^2).
\]

The statement concerns the exact physical-time, infinite-observation-time limit at **fixed** rates and \(\theta\le1\). There is no assertion about a functional limit theorem, finite-time estimation, or jointly changing parameters. The moving-state symmetry gives \(\mathbb EX_t=0\), so \(M(t)\) is also the displacement variance.

## Proof

**1. Exact moment dynamics.** Let \(A(t)=\mathbb E[X_tV_t]\), where \(V_t\in\{-v,0,v\}\), and \(B(t)=\mathbb E[X_t^2\mathbf1_{\{V_t=0\}}]\). Integrating the three-state forward equations against \(x\) and \(x^2\), with zero boundary flux because \(|x|\le vt\), gives

\[
\begin{aligned}
M'&=2A,\\
A'&=v^2\left[1-\frac{\lambda}{\gamma}(1-e^{-\gamma t})\right]-\lambda A+\frac{\alpha_0\eta}{t}B,\\
B'&=\lambda M-\gamma B.
\end{aligned}
\]

All three variables begin at zero. In particular, the bracket in the equation for \(A'\) is the strictly positive active-state probability; \(B(t)\ge0\) from its probabilistic definition. Therefore \(A(t)>0\) and \(M'(t)>0\) for every positive time. The same system yields

\[
M''+\lambda M'-\frac{2\lambda\alpha_0\eta}{t}
\int_0^t e^{-\gamma(t-u)}M(u)\,du
=2v^2\left(1-\frac\lambda\gamma+\frac\lambda\gamma e^{-\gamma t}\right).
\]

**2. Resolvent equation.** The bound \(0\le M(t)\le v^2t^2\) guarantees a finite Laplace transform \(F(s)=\int_0^\infty e^{-st}M(t)\,dt\) for all \(s>0\). Because \(\mathcal L[M(t)/t]\) is inconvenient, transform the identity after multiplication by \(t\); equivalently differentiate the transformed equation in \(s\). Exact algebra gives

\[
F'(s)+P(s)F(s)=Q(s),
\]

\[
P(s)=\frac{2s+\lambda+2\lambda\alpha_0\eta/(s+\gamma)}{s(s+\lambda)},
\qquad
Q(s)=-\frac{2v^2}{s(s+\lambda)}
\left[\frac{1-\lambda/\gamma}{s^2}+\frac{\lambda/\gamma}{(s+\gamma)^2}\right].
\]

Here the \(\lambda\alpha_0\eta\) contribution follows from \(\mathcal L[B]=\lambda F/(s+\gamma)\) and the multiplication by time. At \(s\downarrow0\), with \(C=\frac{2v^2}{\lambda}(1-\lambda/\gamma)\),

\[
P(s)=\frac{1+\theta}{s}+O(1),\qquad
Q(s)=-\frac{C}{s^3}+O(s^{-2}).
\]

**3. Sharp singularity at the marginal exponent.** Choose the positive integrating factor \(I(s)=\exp(\int^sP(u)\,du)\), normalized so that \(I(s)=s^{1+\theta}(1+O(s))\). Then \((IF)'=IQ\). For \(0<\theta<1\), integration at the lower endpoint gives

\[
F(s)\sim\frac{C}{1-\theta}s^{-2}.
\]

Indeed the integral of \(-Cs^{\theta-2}\) diverges as \(C s^{\theta-1}/(1-\theta)\) and dominates the homogeneous integration constant. At \(\theta=1\), the same integration is resonant: \((IF)'=-C/s+O(1)\), so

\[
F(s)=Cs^{-2}\log(1/s)+O(s^{-2}).
\]

The additive scale inside the logarithm only changes the lower-order term. The positivity and strict monotonicity of \(M(t)\) proved in step 1 meet the monotone-density condition of the Laplace Tauberian theorem (Karamata): \(F(s)\sim K s^{-2}L(1/s)\) implies \(M(t)\sim Kt L(t)/\Gamma(2)\) for a slowly varying \(L\). This yields both asserted limits, including the exact coefficients.

**4. Physical parameter boundary.** Solving \(\theta=1\) gives \(\alpha_0=\gamma/(2\eta)=\frac13+\frac\lambda{2\eta}\). It lies in the stipulated open physical interval \((0,2/3)\) if and only if \(\lambda/\eta<2/3\). No critical point is claimed at the excluded endpoint \(\alpha_0=2/3\).

## Verification

The standalone file `verify.py` checks the exact low-frequency singular coefficients symbolically, including the critical relation, and independently integrates the three coupled moment equations for two strictly positive rate sets and subcritical/critical reinforcements. In both cases the normalized finite-time moments approach their analytic limits from below. These finite numerical trajectories are supporting sanity checks, **not** an infinite-time proof; the proof uses the exact transform and the Tauberian argument above. Run with `python verify.py` after installing `sympy` and `scipy`.

## Relationship to prior work

Fedotov, Han, Ivanov and da Silva formulated exactly this finite-speed rest model and its full second-moment Laplace equation, and identified the condition \(\theta>1\) for power-law superdiffusion. The present result does **not** claim the model, the phase line, or the transform equation as original. Its assessed addition is the exact diffusive amplitude for \(\theta<1\) together with the **previously unstated logarithmic law and coefficient at \(\theta=1\)**. The boundary is not treated by simply continuing the quoted power law \(t^\theta\) to exponent one; the inhomogeneous transform term becomes leading at that resonance.

Schütz and Trimper's elephant random walk already has a \(t\log t\) marginal law, but is a *discrete-time, unit-step* process without finite run and rest rates. The relation is a close universality analogy, not an exact finite-rate parameter identification. Han and collaborators' no-rest persistent walk and their separate heavy-tailed Mittag-Leffler rest model cover different residence-time laws; the latter is asymptotically subdiffusive. The general Tauberian mechanism is standard and is not claimed as new.

## Limitations

These asymptotics alone do not establish a position distribution limit, an experimental detection rate, or uniform estimates when the parameters themselves approach the critical surface with observation time. The necessary strict physical condition excludes the corner \(\lambda/\eta=2/3\), \(\alpha_0=2/3\). The coefficient and logarithm emerge from the pre-existing exact transform equation and may be implicit in broader reinforcement or perturbation results not identified by the source comparison. The self-review is not an independent priority certification.

## References

1. S. Fedotov, D. Han, A. O. Ivanov and M. A. A. da Silva, *Superdiffusion in self-reinforcing run-and-tumble model with rests*, arXiv:2110.04299 (first public 2021-10-08); *Physical Review E* **105**, 014126 (2022), https://arxiv.org/abs/2110.04299 .
2. D. Han, M. A. A. da Silva, N. Korabel and S. Fedotov, *Self-reinforcing directionality generates truncated Lévy walks without the power-law assumption*, arXiv:2005.00498 (2020), https://arxiv.org/abs/2005.00498 .
3. G. M. Schütz and S. Trimper, *Elephants can always remember: Exact long-range memory effects in a non-Markovian random walk*, arXiv:cond-mat/0406593 (2004), https://arxiv.org/abs/cond-mat/0406593 .
4. D. Han, D. V. Alexandrov, A. Gavrilova and S. Fedotov, *Anomalous stochastic transport of particles with self-reinforcement and Mittag-Leffler distributed rest times*, arXiv:2110.04851 (2021), https://arxiv.org/abs/2110.04851 .
5. Karamata's Tauberian theorem for Laplace transforms and the monotone-density theorem; standard classical results used for the passage from Laplace asymptotics to physical-time asymptotics.
