# Exact local advection regression and activity decomposition in Lorenz–96
## Finding
Consider the standard Lorenz–96 system
\[
\dot x_i
=
(x_{i+1}-x_{i-2})x_{i-1}
-
x_i
+
F,
\qquad
i=1,\ldots,N,
\]
with cyclic indices,
\[
N\ge4,
\qquad
F>0.
\]
Define the nonlinear advective transfer into site \(i\) by
\[
A_i
=
(x_{i+1}-x_{i-2})x_{i-1}.
\]

Let \(\mu\) be any compactly supported invariant Borel probability measure. Then every site obeys the exact conditional closure
\[
\boxed{
\mathbb E_\mu[A_i\mid x_i]
=
x_i-F
}.
\]
Equivalently, for every bounded Borel one-site observable \(f\),
\[
\boxed{
\mathbb E_\mu
\left[
f(x_i)
\left(
A_i-x_i+F
\right)
\right]
=
0
}.
\]

Thus the conditional mean of a quadratic three-site interaction is exactly affine in the local state, for every compact stationary regime and without an ergodicity or spatial-homogeneity assumption.

The residual is the instantaneous coordinate acceleration:
\[
A_i-(x_i-F)=\dot x_i.
\]
Consequently,
\[
\boxed{
\operatorname{Var}_\mu(A_i\mid x_i)
=
\mathbb E_\mu[\dot x_i^2\mid x_i]
}
\]
almost surely.

The conditional mean also fixes the sign of the mean nonlinear transfer at a given local amplitude:
\[
\mathbb E[A_i\mid x_i]<0
\quad\text{when}\quad
x_i<F,
\]
\[
\mathbb E[A_i\mid x_i]=0
\quad\text{when}\quad
x_i=F,
\]
and
\[
\mathbb E[A_i\mid x_i]>0
\quad\text{when}\quad
x_i>F,
\]
where these statements are understood on the corresponding portions of the conditional support.

There is a global site-time form that separates static spread from dynamical activity. Choose a site
\[
I
\]
uniformly from
\[
\{1,\ldots,N\}
\]
independently of a state sampled from \(\mu\), and write
\[
X=x_I,
\qquad
A=A_I.
\]
Set
\[
D
=
\frac1N
\sum_{i=1}^N
\mathbb E_\mu[\dot x_i^2].
\]
Then
\[
\boxed{
\operatorname{Cov}(X,A)
=
\operatorname{Var}(X)
}
\]
and
\[
\boxed{
\operatorname{Var}(A)
=
\operatorname{Var}(X)+D
}.
\]

Lorenz and Emanuel already derived the classical site-time balance
\[
\operatorname{Var}(X)
=
m(F-m),
\qquad
m
=
\frac1N
\sum_{i=1}^N
\mathbb E_\mu[x_i].
\]
Combining that prior balance with the new activity decomposition gives
\[
\boxed{
\operatorname{Var}(A)
=
m(F-m)+D
}.
\]

The defect
\[
D
\]
vanishes exactly when \(\mu\) is supported on Lorenz–96 equilibria. Therefore every compact stationary state not supported on equilibria satisfies
\[
D>0,
\]
\[
0<m<F,
\]
and
\[
\boxed{
0<
\operatorname{Corr}(X,A)
<
1
}.
\]
More precisely,
\[
\boxed{
\operatorname{Corr}(X,A)
=
\left(
1+
\frac{D}{m(F-m)}
\right)^{-1/2}
}.
\]

For the standard strongly chaotic forcing
\[
F=8,
\]
the exact formulas specialize to
\[
\operatorname{Var}(X)
=
m(8-m)
\]
and
\[
\operatorname{Var}(A)
=
m(8-m)+D.
\]
Thus the excess nonlinear-transfer variance over state variance is not a fitted closure error: it is exactly the mean-square coordinate activity.

## Assumptions and scope
The result concerns the one-scale Lorenz–96 system with the standard quadratic cyclic advection, linear damping, and constant forcing.

Compact support ensures that the generator tests and second moments are legitimate. No ergodicity, cyclic symmetry of the measure, or uniqueness of a physical measure is assumed.

The site-time variable \(X\) means that a state is sampled from \(\mu\) and then a site is selected uniformly. This is the same spatial-and-temporal averaging convention used in the classical Lorenz–Emanuel energy calculation.

The classical identity
\[
\operatorname{Var}(X)=m(F-m)
\]
and the resulting bounds
\[
0\le m\le F,
\qquad
\sqrt{\operatorname{Var}(X)}
\le
\frac F2
\]
are prior results and are not claimed as new.

The model was introduced earlier in 1996, but the checked 1996 source was not available with a day-resolved public date. The structured source date is therefore 1 February 1998, the earliest checked day-resolved full public source containing the exact equations and energy balance.

A later mathematical study lists \(34C23\) first among its primary Mathematics Subject Classification codes; that classification is used here.

## Proof
Let
\[
L
\]
be the flow generator.

Fix a site \(i\). For every continuous function \(\phi\) on the compact projection of the support onto the \(x_i\)-axis, choose an antiderivative \(H\) satisfying
\[
H'(x_i)=\phi(x_i).
\]
Then
\[
LH
=
\phi(x_i)\dot x_i
=
\phi(x_i)
\left(
A_i-x_i+F
\right).
\]
Invariance gives
\[
0
=
\int LH\,d\mu
=
\mathbb E_\mu
\left[
\phi(x_i)
\left(
A_i-x_i+F
\right)
\right].
\]
By the defining characterization of conditional expectation,
\[
\mathbb E_\mu[A_i-x_i+F\mid x_i]=0.
\]
Hence
\[
\mathbb E_\mu[A_i\mid x_i]
=
x_i-F.
\]

Because
\[
\dot x_i
=
A_i-(x_i-F),
\]
the same identity is
\[
\mathbb E_\mu[\dot x_i\mid x_i]=0.
\]
Conditioning the squared residual therefore gives
\[
\operatorname{Var}_\mu(A_i\mid x_i)
=
\mathbb E_\mu[\dot x_i^2\mid x_i].
\]

Now sample a site \(I\) uniformly and independently and set
\[
X=x_I,
\qquad
A=A_I,
\qquad
V=\dot x_I.
\]
Then
\[
A=X-F+V
\]
and
\[
\mathbb E[V\mid I,X]=0.
\]
Therefore
\[
\mathbb E[V]=0
\]
and
\[
\operatorname{Cov}(X,V)=0.
\]
It follows that
\[
\operatorname{Cov}(X,A)
=
\operatorname{Cov}(X,X-F+V)
=
\operatorname{Var}(X)
\]
and
\[
\operatorname{Var}(A)
=
\operatorname{Var}(X)
+
\mathbb E[V^2].
\]
Since
\[
\mathbb E[V^2]
=
\frac1N
\sum_i
\mathbb E_\mu[\dot x_i^2]
=
D,
\]
the activity decomposition follows.

For completeness, the classical global balance can be reconstructed directly. The nonlinear advection conserves quadratic energy:
\[
\sum_i x_iA_i
=
\sum_i
x_ix_{i-1}x_{i+1}
-
\sum_i
x_ix_{i-1}x_{i-2}
=
0
\]
by cyclic reindexing. Hence
\[
\frac{d}{dt}
\frac12
\sum_i x_i^2
=
-
\sum_i x_i^2
+
F\sum_i x_i.
\]
Stationarity gives
\[
\frac1N
\sum_i
\mathbb E[x_i^2]
=
Fm.
\]
For the uniformly sampled site,
\[
\mathbb E[X]=m,
\qquad
\mathbb E[X^2]=Fm,
\]
and therefore
\[
\operatorname{Var}(X)=m(F-m).
\]

Finally,
\[
D=0
\]
if and only if
\[
\dot x_i=0
\]
for every site almost surely, which is exactly support on equilibria. If the measure is not equilibrium-supported, then
\[
D>0.
\]
Also,
\[
\operatorname{Var}(X)>0.
\]
Indeed, if
\[
\operatorname{Var}(X)=0,
\]
then all coordinates equal the same constant almost surely. The only invariant constant vector is
\[
x_i=F
\]
for every \(i\), which is an equilibrium.

Thus
\[
m(F-m)>0,
\]
so
\[
0<m<F.
\]
The covariance formula gives
\[
\operatorname{Corr}(X,A)
=
\frac{\operatorname{Var}(X)}
{\sqrt{
\operatorname{Var}(X)
\left(
\operatorname{Var}(X)+D
\right)
}}
=
\left(
1+
\frac{D}{\operatorname{Var}(X)}
\right)^{-1/2},
\]
and substitution of
\[
\operatorname{Var}(X)=m(F-m)
\]
gives the stated strict formula.

## Verification
The packaged checker uses only the Python standard library and exact rational arithmetic.

It verifies the cyclic cancellation
\[
\sum_i x_iA_i=0
\]
for exact rational test states and checks the resulting stationary energy algebra.

It verifies abstract conditional-residual consequences:
\[
A=X-F+V,
\qquad
\mathbb E[V]=0,
\qquad
\operatorname{Cov}(X,V)=0,
\]
which imply
\[
\operatorname{Cov}(X,A)=\operatorname{Var}(X)
\]
and
\[
\operatorname{Var}(A)=\operatorname{Var}(X)+\mathbb E[V^2].
\]

It also checks the specialization
\[
F=8
\]
and the exact correlation formula for a rational stationary test moment set.

The stored checker output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation quantifier and the equilibrium-support equality classification are analytic arguments; they are not inferred from numerical orbit sampling.

## Relationship to prior work
Lorenz and Emanuel give the exact standard equations, identify the quadratic term as energy-conserving advection, and derive by spatial-and-long-time averaging
\[
\mathbb E[X^2]=F\mathbb E[X]
\]
and therefore
\[
\operatorname{Var}(X)=m(F-m).
\]
That global variance parabola is prior work.

The accepted result strengthens a different part of the structure. Instead of one energy-weighted average over all sites, it gives, separately at every site,
\[
\mathbb E[A_i\mid x_i]=x_i-F.
\]
This is equivalent to infinitely many weighted identities
\[
\mathbb E[f(x_i)(A_i-x_i+F)]=0
\]
and determines the exact conditional mean of the nonlinear advective transfer.

Gallavotti and Lucarini emphasize the decomposition of Lorenz–96 into an energy-conserving reversible advection part and forcing/dissipation and study nonequilibrium statistical ensembles. Their checked material concerns ensemble equivalence, phase-space contraction, Lyapunov spectra, and energy-conserving reversible modifications rather than the sitewise advection regression.

Kerin and Engler analyze the algebraic structure of the advection, bifurcations of the constant equilibrium, rotation invariance, generalized forcings and dissipations, and advection-only systems. Searches of the open article record found no conditional, variance, or stationary-measure formulation matching the present sitewise law.

Recent Lorenz–96 conditional-mean work studies how Fourier fine modes can be predicted from retained coarse modes under invariant snapshot statistics. That is a distinct conditioning problem: the accepted theorem conditions the instantaneous nonlinear physical-space transfer at one site on the state of that same site and gives its conditional mean exactly.

A published stability result for Lorenz–96-like quadratic advection identifies a closed energy-stability boundary for the constant equilibrium. Stability of the equilibrium does not imply the accepted stationary conditional law, which applies across equilibrium, periodic, quasiperiodic, and chaotic compact invariant measures.

## Limitations
The theorem is stated for the standard one-scale Lorenz–96 equation, not for stochastic, two-scale, or site-dependent variants.

It gives the conditional mean and residual variance of the local nonlinear transfer but not its full conditional distribution.

The global variance parabola is classical and explicitly excluded from the originality claim; it is used only to express the new activity decomposition in familiar Lorenz–96 statistics.

The complete 1998 source was inspected in full. The 2014 nonequilibrium-ensemble source was compared through its public preprint abstract and repository-exposed material rather than a fully parsed local copy.

A very recent preprint studies other conditional means in Lorenz–96, so conditional-statistics literature is active; its stated Fourier coarse-to-fine result does not cover the exact local advective-transfer regression proved here.

Because the proof is short, an equivalent one-site generator identity could remain in unindexed literature.

## References
1. E. N. Lorenz and K. A. Emanuel, “Optimal Sites for Supplementary Weather Observations: Simulation with a Small Model,” Journal of the Atmospheric Sciences 55, 399–414 (1998), DOI 10.1175/1520-0469(1998)055<0399:OSFSWO>2.0.CO;2.
2. G. Gallavotti and V. Lucarini, “Equivalence of Non-Equilibrium Ensembles and Representation of Friction in Turbulent Flows: The Lorenz 96 Model,” Journal of Statistical Physics 156, 1027–1065 (2014), arXiv:1404.6638, DOI 10.1007/s10955-014-1051-6.
3. J. Kerin and H. Engler, “On the Lorenz '96 Model and Some Generalizations,” Discrete and Continuous Dynamical Systems - B 27, 769–797 (2022), DOI 10.3934/dcdsb.2021064; preprint arXiv:2005.07767.
4. Z. Xu and J. Chen, “Intrinsic Instantaneous Coarse-to-Fine Recoverability in the Lorenz-96 System,” arXiv:2607.08323 (2026).
