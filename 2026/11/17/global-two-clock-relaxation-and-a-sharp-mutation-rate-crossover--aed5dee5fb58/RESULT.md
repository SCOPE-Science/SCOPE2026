# Global two-clock relaxation and a sharp mutation-rate crossover on the balanced May–Leonard surface

## Finding

Consider the three-species May–Leonard system with all-to-all linear mutation
\[
\dot x_i=x_i(1-x_i-\alpha x_{i+1}-\beta x_{i+2})+\mu(x_{i+1}+x_{i+2}-2x_i),
\qquad i\in\mathbb Z/3\mathbb Z,
\]
under the **balanced competitive condition** \(\alpha+\beta=2\), with \(\alpha,\beta,\mu>0\). Every nonzero nonnegative initial condition converges to the equal coexistence state \(e=(1/3,1/3,1/3)\). Beyond convergence, every nonsymmetric trajectory admits a **nonvanishing rotating exponential profile**.

Write \(S_0=\sum_i x_i(0)>0\), \(C=S_0^{-1}-1\), \(p_i=x_i/S\), \(u=p-e\), \(a=\alpha-1\), and introduce the skew-symmetric operator
\[
(Bu)_i=-\frac{u_{i+1}-u_{i+2}}{3},\qquad
\tau(t)=\log\!\left(\frac{e^t+C}{1+C}\right),\qquad
R(t)=\exp(aB\tau(t)).
\]
If \(p(0)\ne e\), there exists a uniquely determined vector \(v\in\{z\in\mathbb R^3:\sum_i z_i=0\}\setminus\{0\}\), depending on the trajectory, such that
\[
\boxed{p(t)-e=e^{-3\mu t}R(t)v+O(e^{-6\mu t}).}
\]
The operator \(R(t)\) is a Euclidean rotation in the zero-sum plane, through signed angle \(a\tau(t)/\sqrt3\) with the sign fixed by the chosen orientation. Thus for \(\alpha\ne\beta\) the composition approaches coexistence by a rotating spiral of exact nonzero leading amplitude \(\lVert v\rVert e^{-3\mu t}\).

For the full population displacement, the conserved orthogonality of the mass and composition directions yields the exact identity
\[
\lVert x(t)-e\rVert^2
=\frac{(S(t)-1)^2}{3}+S(t)^2\lVert p(t)-e\rVert^2.
\]
For every initial condition satisfying both \(S_0\ne1\) and \(p(0)\ne e\), letting \(L=\lVert v\rVert>0\), there is a **sharp mutation-rate crossover**:
\[
\boxed{
\begin{array}{ll}
\displaystyle\lim_{t\to\infty}e^{3\mu t}\lVert x(t)-e\rVert=L,&0<\mu<1/3,\\[5pt]
\displaystyle\lim_{t\to\infty}e^t\lVert x(t)-e\rVert=\sqrt{C^2/3+L^2},&\mu=1/3,\\[5pt]
\displaystyle\lim_{t\to\infty}e^t\lVert x(t)-e\rVert=|C|/\sqrt3,&\mu>1/3.
\end{array}}
\]
If \(S_0=1\), only the composition clock remains; if \(p(0)=e\), only the mass clock remains. When both equalities hold the state is already at equilibrium.

## Assumptions and scope

Indices are cyclic modulo three. Parameters obey \(0<\alpha<2\), \(\beta=2-\alpha\), and \(\mu>0\). The initial vector is in \([0,\infty)^3\setminus\{0\}\); for such data the all-to-all mutation term makes all components strictly positive for every \(t>0\). The norm is the ordinary Euclidean norm. All assertions concern solutions of the displayed continuous-time differential equation, not Euler discretizations or stochastic population models. The critical crossover is asserted for the two-channel generic initial data only; the exceptional initial manifolds are stated separately.

## Proof

**1. Exact mass separation.** Summing the equations and using \(\alpha+\beta=2\) gives
\[
S'=S-S^2,\qquad S(t)=\frac1{1+C e^{-t}}.
\]
The expression is positive for every \(t\ge0\). The nonnegative octant is forward invariant: on any coordinate face with \(S>0\), its derivative is \(\mu S>0\). Consequently each nonzero nonnegative initial state becomes strictly interior immediately.

**2. Exact frequency equation and entropy.** Set \(p_i=x_i/S\), so \(\sum_i p_i=1\). Direct substitution gives
\[
p_i'=-aS p_i(p_{i+1}-p_{i+2})+\mu(1-3p_i).
\]
For positive frequencies define \(H(p)=-\sum_i\log(3p_i)\). The cyclic cubic term contributes zero to \(H'\), and
\[
H'=-\mu\left(\sum_i\frac1{p_i}-9\right)\le0.
\]
Cauchy's inequality gives \(\sum_i1/p_i\ge9\), with equality exactly at \(p=e\). For any \(t_0>0\), the sublevel \(H\le H(p(t_0))\) is a compact subset of the open simplex; away from a given neighborhood of \(e\), the dissipation is uniformly negative. Monotonicity therefore forces \(p(t)\to e\). Together with \(S(t)\to1\), this proves global convergence for the full population state.

**3. Rotating nonzero profile.** On the plane \(E=\{u:\sum_i u_i=0\}\) define \(N_i(u)=-u_i(u_{i+1}-u_{i+2})\). The frequency equation is exactly
\[
u'=-3\mu u+aS Bu+aS N(u).
\]
The matrix \(B\) is skew-symmetric, preserves \(E\), and satisfies \(B^2|_E=-I_E/3\). The quadratic function \(N\) obeys \(\lVert N(u)\rVert\le K\lVert u\rVert^2\) for a fixed numerical constant \(K\). If \(u(0)\ne0\), uniqueness of solutions precludes \(u(t)=0\) at finite time. Writing \(r=\lVert u\rVert>0\) and taking an inner product with \(u/r^2\) gives
\[
\frac{d}{dt}\log r=-3\mu+O(r),
\]
where the bound is uniform because \(S\) stays bounded. Since \(r\to0\), for every sufficiently late time \(r'\le-(3\mu/2)r\), hence \(\int_0^\infty r(t)\,dt<\infty\). Integrating the logarithmic derivative now gives a finite, strictly positive limit
\[
\lim_{t\to\infty}e^{3\mu t}r(t)=L\in(0,\infty).
\]
Define \(R(t)=\exp(aB\tau(t))\) with \(\tau'(t)=S(t)\) and \(R(0)=I\). Since \(B\) commutes with \(R\) and is skew-symmetric, the interaction-picture variable \(w=e^{3\mu t}R^{-1}u\) has derivative
\[
w'=aS e^{3\mu t}R^{-1}N(u).
\]
The already established asymptotic bound \(r=O(e^{-3\mu t})\) gives \(\lVert w'\rVert=O(e^{-3\mu t})\). Therefore \(w\) converges to \(v\in E\), \(\lVert v\rVert=L>0\), with \(w(t)=v+O(e^{-3\mu t})\). Multiplying by \(e^{-3\mu t}R(t)\) gives the stated expansion with \(O(e^{-6\mu t})\) error. The rotation angle follows from \(B^2=-I/3\).

**4. Sharp two-clock crossover.** The displacement decomposes orthogonally as
\[
x-e=\frac{S-1}{3}(1,1,1)+S u.
\]
Thus the displayed squared-norm identity holds exactly. For \(C\ne0\), the logistic identity gives \(S-1=-C e^{-t}+O(e^{-2t})\). For \(u(0)\ne0\), the rotating profile gives \(\lVert u\rVert=L e^{-3\mu t}(1+o(1))\). Comparing the two positive orthogonal squared contributions yields the three nonzero limits and the crossover at \(3\mu=1\). If \(C=0\) the mass contribution is identically zero; if \(u(0)=0\), the frequency equation preserves \(u=0\). These cover all exceptional cases.

## Verification

The accompanying `check.py` uses the standard-library rational number type to verify five defining algebraic identities in each of 60 exact parameter/state examples: logistic mass reduction, normalized frequency equation, entropy dissipation, the rotation-generator square, and separation into skew-linear and quadratic terms. A fourth-order Runge–Kutta diagnostic additionally tests convergence of the nonzero phase-corrected amplitude for two nonsymmetric parameter choices; the normalized differences between late-time vectors are below \(6\times10^{-6}\) in those tests. These finite calculations check transcription and examples only. The claims for all positive parameters and all nonzero nonnegative initial data follow from the preceding analytical proof.

Reproduce with `python3 check.py` (Python standard library only).

## Relationship to prior work

Jaramillo, Mrad and Stepien (2022) introduced this precise linearly mutated May–Leonard system and studied its equilibrium stability, local Hopf bifurcations, fold curves and oscillatory regimes. Their balanced critical surface gives a locally stable coexistence equilibrium for positive mutation. The statements above concern **global** convergence for every initial population and a complete asymptotic phase and rate law; they are not an assertion of a new Hopf threshold.

Mobilia (2009) and Toupo–Strogatz (2015) investigated global-mutation rock–paper–scissors replicator dynamics on a normalized probability simplex. The zero-sum game with global mutation contains a time-rescaled analogue of the frequency subsystem **when** \(S\equiv1\), so global stable coexistence on that invariant slice is prior background. The present full-population result distinguishes an independently relaxing logistic mass from a rotating frequency mode, gives a nonvanishing asymptotic vector for arbitrary positive initial mass, and identifies the sharp \(\mu=1/3\) competition between the two rates. No exclusive novelty claim is made for the known normalized-slice convergence or local eigenvalues.

## Limitations

The constant vector \(v\) is defined by a convergent trajectory limit, rather than an elementary closed formula in initial data. The criterion concerns the exact balanced slice \(\alpha+\beta=2\) with strictly positive mutation and need not persist off this surface. The result is asymptotic and does not supply a uniform finite-time rate bound over initial states approaching the boundary. Existing evolutionary-game work already covers global stable coexistence in related zero-sum probability models; an unindexed equivalent full-population asymptotic statement remains a publication-priority risk. No independent mathematical audit has been performed.

## References

1. G. Jaramillo, L. Mrad, and T. L. Stepien, *Dynamics of a linearly-perturbed May–Leonard competition model*, arXiv:2210.04342, first posted 2022-10-09. https://arxiv.org/abs/2210.04342
2. D. F. P. Toupo and S. H. Strogatz, *Nonlinear Dynamics of the Rock-Paper-Scissors Game with Mutations*, arXiv:1502.03370, first posted 2015-02-11. https://arxiv.org/abs/1502.03370
3. M. Mobilia, *Oscillatory Dynamics in Rock-Paper-Scissors Games with Mutations*, arXiv:0912.5179, first posted 2009-12-28. https://arxiv.org/abs/0912.5179
