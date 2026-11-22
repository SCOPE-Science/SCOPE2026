# Global two-observable recovery of unequal switching rates in a shared harmonic trap

## Finding

For every calibrated diffusion strength \(D>0\) and two distinct, positive harmonic relaxation rates \(a>b>0\), consider \(N\ge 2\) independent Brownian particles subjected to a *common* two-state stiffness environment. The transition rate from the stronger trap \(a\) to the weaker trap \(b\) is \(r_1>0\); the reverse transition rate is \(r_2>0\). At stationarity define
\[
S=\mathbb E[X_1^2],\qquad
K=\operatorname{Cov}(X_1^2,X_2^2).
\]
Write \(v_-=D/a\) and \(v_+=D/b\). **The complete feasible region** for \((S,K)\) as \((r_1,r_2)\) ranges over all strictly positive pairs is exactly
\[
\boxed{v_-<S<v_+,\qquad 0<K<(S-v_-)(v_+-S).}
\]
For **each** point in this open region there is **exactly one ordered pair** \((r_1,r_2)\) producing it. No positive finite pair attains either covariance boundary. The inversion is constructive, requiring only nested one-dimensional monotone root searches.

An equivalent single-particle statement uses its stationary fourth cumulant: \(\kappa_4(X_1)=\mathbb E[X_1^4]-3\mathbb E[X_1^2]^2=3K\). Therefore the second and fourth marginal moments alone uniquely recover both transition rates. A single scalar variance does not.

## Assumptions and scope

The common environment \(J_t\in\{1,2\}\) is a stationary irreducible continuous-time Markov chain with jumps \(1\to2\) at \(r_1\) and \(2\to1\) at \(r_2\), independent of all standard Brownian motions \(W_i\). Particle positions obey
\[
\mathrm dX_i(t)=-\mu_{J_t}X_i(t)\,\mathrm dt+\sqrt{2D}\,\mathrm dW_i(t),
\quad\mu_1=a,\quad\mu_2=b,\quad 1\le i\le N.
\]
All parameters \(D,a,b,r_1,r_2\) are finite and strictly positive, and \(a>b\). The first three are known independently. Observables refer to ensemble expectations under the unique stationary joint law, not empirical finite-sample estimates. No direct particle coupling, hydrodynamic interaction, phase-dependent diffusivity, or resetting jump is included. For the single-particle cumulant formulation, \(N=1\) suffices.

## Proof

**1. A common conditional Gaussian variance.** Conditional on the complete past of the environment, the stationary positions are independent centered Gaussians with the same random variance \(V\), which evolves according to \(\dot V=2D-2\mu_JV\). Since \(a>b\), it lies strictly between \(v_-=D/a\) and \(v_+=D/b\) almost surely. Put \(\Delta=v_+-v_->0\) and \(U=(V-v_-)/\Delta\). In state 1 the deterministic velocity of \(U\) is \(-2aU\); in state 2 it is \(2b(1-U)\).

**2. Exact stationary mixing density.** Set
\[
A=\frac{r_1}{2a},\quad B=\frac{r_2}{2b},\quad
 t=A+B,\quad z=\frac A{A+B},\quad d=a-b.
\]
The two stationary state-resolved densities for \(0<u<1\) are proportional to
\[
f_1(u)=c\,b\,u^{A-1}(1-u)^B,\qquad
f_2(u)=c\,a\,u^A(1-u)^{B-1}.
\]
Indeed their total probability flux \(-2au f_1+2b(1-u)f_2\) vanishes, and the switching balance equations follow by differentiation using \(r_1=2aA\), \(r_2=2bB\). Normalization gives
\[
h_{A,B}(u)=f_1(u)+f_2(u)=
\frac{(b+du)u^{A-1}(1-u)^{B-1}}
{\mathrm B(A,B)(b+dz)},\qquad 0<u<1,
\]
where \(\mathrm B\) is Euler's beta function. Positive switching precludes stationary endpoint atoms. This independently reconstructs the known conditional-Gaussian representation of the switching-trap model.

**3. Observable-to-moment reduction.** Conditional Gaussian independence yields
\[
S=v_-+\Delta m,\qquad K=\Delta^2(q-m^2),
\quad m=\mathbb E[U],\quad q=\mathbb E[U^2].
\]
Using beta integrals and the linear tilt \(b+du\),
\[
m=z+\frac{d z(1-z)}{(t+1)(b+dz)},
\]
\[
q=\frac{z(tz+1)\bigl(b(t+2)+d(tz+2)\bigr)}
{(b+dz)(t+1)(t+2)}.
\]
All denominators are positive for the stated parameters.

**4. Strict one-to-one moment map.** Fix any \(0<m<1\). For each \(t>0\), the family indexed by \(z\in(0,1)\) has a strictly increasing likelihood ratio in \(u\) as \(z\) increases: the ratio of two densities is proportional to \((u/(1-u))^{t(z_2-z_1)}\). Thus exactly one \(z=z_m(t)\in(0,1)\) gives the specified mean, and this choice is continuous in \(t\).

Consider two such distributions at \(t_2>t_1\) with the same mean, with shapes \((A_j,B_j)\). Both shapes must strictly increase. For if one increased and the other decreased (or stayed equal), the density ratio would be strictly monotone, causing a strict change of mean; both shapes cannot decrease since their sum increases. Consequently
\[
\frac{h_{A_2,B_2}(u)}{h_{A_1,B_1}(u)}
=C_0u^{A_2-A_1}(1-u)^{B_2-B_1}
\]
for a positive constant \(C_0\), with both exponents positive. This ratio tends to zero at both endpoints and has a unique interior maximum. Since the densities normalize to one, it crosses one at exactly two points \(0<c_1<c_2<1\): the second density is smaller in both tails and larger in the middle. The signed integral against \((u-c_1)(u-c_2)\) is therefore strictly negative. The densities have the same mass and mean, so the signed integral equals \(\mathbb E_2[U^2]-\mathbb E_1[U^2]<0\). Hence \(q-m^2\) decreases **strictly** as \(t\) increases along a fixed mean.

**5. Sharp range and inversion.** As \(t\downarrow0\) at fixed mean, \(z_m(t)\to bm/(a-dm)\) and the tilted beta law converges weakly to the Bernoulli law on \(\{0,1\}\) of mean \(m\). Thus \(q-m^2\to m(1-m)\). As \(t\to\infty\), \(z_m(t)\to m\), and the law concentrates at \(m\), giving \(q-m^2\to0\). The strict continuity and monotonicity prove that every and only \(0<q-m^2<m(1-m)\) is attained once. Converting back to \((S,K)\) establishes exactly the boxed region and uniqueness.

For reconstruction from feasible data, compute \(m=(S-v_-)/\Delta\) and \(k=K/\Delta^2\). At each trial \(t>0\), solve the strictly increasing mean equation for \(z_m(t)\), then solve the strictly decreasing equation \(q(t,z_m(t))-m^2=k\) for \(t\). Finally return \(r_1=2at z_m(t)\), \(r_2=2bt(1-z_m(t))\). No second solution is possible. Since \(\mathbb E[X_1^4]=3\mathbb E[V^2]\), \(\kappa_4(X_1)=3K\) follows.

## Verification

An independent generator-moment calculation checks the beta integrations. With \(p_1=r_2/(r_1+r_2)\), \(p_2=r_1/(r_1+r_2)\), put \(s_j=\mathbb E[V\mathbf1_{J=j}]\) and \(w_j=\mathbb E[V^2\mathbf1_{J=j}]\). They solve the distinct linear systems
\[
\begin{pmatrix}2a+r_1&-r_2\\-r_1&2b+r_2\end{pmatrix}
\binom{s_1}{s_2}=2D\binom{p_1}{p_2},\qquad
\begin{pmatrix}4a+r_1&-r_2\\-r_1&4b+r_2\end{pmatrix}
\binom{w_1}{w_2}=4D\binom{s_1}{s_2}.
\]
The supplied standard-library checker evaluates these equations exactly using rational arithmetic, compares all derived second and fourth moments, checks positivity and the feasible region, and tests monotonic inversion across multiple parameters. It passed **2,458** explicit assertions when executed from its delivered path; computation is a consistency check, not proof of the universal statements.

For a non-symmetric example, \(a=2,b=1,D=1,r_1=4,r_2=6\) give \(A=1,B=3\), \(m=7/25\), \(q=3/25\), and exactly \(S=16/25\), \(K=13/1250\). Inverting these observables reproduces both rates.

## Relationship to prior work

Biroli, Kulkarni, Majumdar and Schehr derive the full stationary conditional-Gaussian mixture and forward particle correlations of this exact switching-trap model. The present result **does not claim that forward distribution or its correlations as new**; its assessed addition is an exhaustive and globally injective *inverse* map from exactly two low-order stationary observables, including a sharp parameter-independent feasible moment region and nonattainment of both boundaries. Forward formulas alone do not state or establish the required global injectivity and two-crossing comparison.

Later experiments by Biroli and collaborators independently use variance and cross-particle square correlations to test the model, while restricting their experiments to equal switching rates. They do not give the all-positive-unequal-rate inverse theorem. General Markov-modulated Ornstein–Uhlenbeck moment results derive forward moments under broader process assumptions, not the claimed two-observable feasible region or uniqueness. An earlier two-state switching-OU stationary-density paper is a relevant antecedent; the accessible abstract does not resolve its relationship to this inverse theorem, so unexamined detailed coverage remains a residual literature risk.

## Limitations

The result concerns ensemble moments of an exactly specified, calibrated, noninteracting Gaussian diffusion under a common two-state *Poisson* environment. It does not establish statistical conditioning or finite-sample error bounds, identification when \(a,b,D\) are unknown, identification under direct interparticle coupling, or identifiability of non-Poisson residence-time laws. The limiting covariance boundaries correspond respectively to vanishing and diverging total switching speeds and are not attained for finite positive rates.

## References

1. M. Biroli, M. Kulkarni, S. N. Majumdar, and G. Schehr, *Dynamically emergent correlations between particles in a switching harmonic trap*, arXiv:2312.02570, first public 2023-12-05. https://arxiv.org/abs/2312.02570
2. M. Biroli, S. Ciliberto, M. Kulkarni, S. N. Majumdar, A. Petrosyan, and G. Schehr, *Experimental evidence for strong emergent correlations between particles in a switching trap*, arXiv:2508.07199, first public 2025-08-10. https://arxiv.org/html/2508.07199v2
3. A. Behme, P. Di Tella, and A. Sideris, *On moments of integrals with respect to Markov additive processes and of Markov modulated generalized Ornstein-Uhlenbeck processes*, arXiv:2207.11093, first public 2022-07-22. https://arxiv.org/abs/2207.11093
4. Z. Zhang and W. Wang, *The stationary distribution of Ornstein-Uhlenbeck process with a two-state Markov switching*, Communications in Statistics — Simulation and Computation **46** (2017), 4783–4794, https://doi.org/10.1080/03610918.2015.1132321
