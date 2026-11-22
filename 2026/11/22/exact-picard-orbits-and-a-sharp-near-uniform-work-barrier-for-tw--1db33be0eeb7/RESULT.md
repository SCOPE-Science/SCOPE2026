# Exact Picard orbits and a sharp near-uniform work barrier for two-invariant discrete-gradient correction

## Finding

A two-invariant discrete-gradient correction has an exactly solvable inner iteration when it preserves a linear mass and a quadratic energy using mean-value discrete gradients. Its predictor-initialized Picard iteration selects the near-predictor positive radial branch, but its convergence is not uniform as the predictor approaches the uniform-mass state. The exact orbit gives a sharp inverse-distance iteration count and exhibits a singular finite-step predictor for an explicit conservative oscillator.

Let \(d\ge3\), let \(u\in\mathbb R^d\) have \(\|u\|_2=1\), and prescribe the invariants
\[
H_1(x)=u^\top x=m,\qquad H_2(x)=\frac12\|x\|_2^2=\frac12(m^2+\rho^2),\qquad \rho>0.
\]
For a mass-preserving predictor \(p=mu+w\) with \(w\perp u\), write \(r=\|w\|_2\). The predictor-initialized fixed-point iteration of the multi-invariant correction in Pu--Ran (2026), with the mean-value discrete gradients, is denoted \(v^{(0)}=p\) and \(v^{(j+1)}=G_p(v^{(j)})\).

**Exact orbit.** For every \(r>0\), all these iterates exist and
\[
v^{(j)}=mu+t_j\frac{w}{r},\quad
 t_j=\rho\,\frac{1+\kappa^{j+1}}{1-\kappa^{j+1}},\quad
 \kappa=\frac{r-\rho}{r+\rho},\quad j=0,1,2,\ldots.
\]
They converge to \(v^*=mu+\rho w/r\), the nearest mass-and-energy-feasible point to \(p\). When \(r\ne\rho\), the full implicit correction equation also has the *different* branch \(mu-\rho w/r\); the initialized fixed-point iteration selects only the positive branch. When \(r=\rho\), the correction is already exact and the sole nonsingular solution is \(p\). At \(r=0\) the prescribed initialization makes the Gram system singular, while the nonsingular implicit solutions form the sphere \(\{mu+z:u^\top z=0,\ \|z\|=\rho\}\).

**Sharp work barrier.** For fixed \(0<\varepsilon<1\), define the minimum number of inner updates required for relative distance error at most \(\varepsilon\),
\[
N_\varepsilon(r)=\min\big\{j\ge0:\|v^{(j)}-v^*\|_2\le\varepsilon\rho\big\}.
\]
Then
\[
\boxed{\displaystyle\lim_{r\downarrow0}\frac{2r}{\rho}N_\varepsilon(r)=\log\frac{2-\varepsilon}{\varepsilon}.}
\]
In particular, \(\|v^{(1)}-mu\|_2=(r^2+\rho^2)/(2r)\) diverges as \(r\downarrow0\), despite the bounded exact corrected state. Thus the raw inner computation has both unbounded transient excursion and unbounded iteration cost near a perfectly feasible invariant manifold.

**Concrete conservative-ODE realization.** In three coordinates take \(u=e_1\) and the skew-symmetric generator \(J e_1=0\), \(J e_2=e_3\), \(J e_3=-e_2\). The ODE \(\dot x=Jx\) preserves the displayed mass and energy. The legitimate (first-order) three-evaluation explicit Runge--Kutta predictor
\[
k_1=Jx,\quad k_2=J(x+hk_1),\quad k_3=J(x+hk_2),\quad p_h=x+hk_3
\]
obeys, on an initial state \(x=mu+w\) with \(\|w\|=\rho\),
\[
p_h=mu+(1-h^2)(I+hJ)w,\qquad
\frac{\|p_h-mu\|}{\rho}=|1-h^2|\sqrt{1+h^2}.
\]
At the finite step \(h=1\) the predictor is *exactly* \(mu\) and the inner Gram solve is singular. Approaching this step from either side,
\[
\boxed{\displaystyle\lim_{h\to1}|h-1|N_\varepsilon\big(\rho|1-h^2|\sqrt{1+h^2}\big)=\frac{1}{4\sqrt2}\log\frac{2-\varepsilon}{\varepsilon}.}
\]
This is an inner-solver complexity result at large steps, not a claim that the explicit predictor accurately resolves the oscillator near \(h=1\).

## Assumptions and scope

All statements are in exact real arithmetic. The invariant target has \(\rho>0\), and the predictor is constrained to preserve \(H_1\) exactly. We use the **mean-value discrete gradient**, which for these invariants is
\[
\overline\nabla H_1(p,v)=u,\qquad \overline\nabla H_2(p,v)=\frac{p+v}{2}.
\]
The correction is exactly the source's Gram-multiplier fixed-point map: with \(B(p,v)\) having these two gradient columns, solve
\[
B(p,v)^\top B(p,v)\,\lambda
=\begin{pmatrix}m-H_1(p)\\ (m^2+\rho^2)/2-H_2(p)\end{pmatrix}
\]
and set \(G_p(v)=p+B(p,v)\lambda\), only where the Gram matrix is invertible. No other discrete gradient, nonlinear energy, inexact linear solve, or arbitrary predictor initial guess is covered. The theorem concerns one correction stage, not the global accuracy of the outer integration method.

## Proof

**1. Orthogonal reduction and Gram elimination.** Write \(v=mu+z\) with \(u^\top z=0\). Since \(p=mu+w\), \(H_1(p)=m\), and the second residual is \((\rho^2-r^2)/2\), eliminating the first multiplier from the \(2\times2\) Gram system yields
\[
G_p(mu+z)=mu+w+\frac{\rho^2-r^2}{\|w+z\|^2}(w+z),\qquad w+z\ne0.
\]
Indeed, the component of the second discrete gradient orthogonal to \(u\) is \((w+z)/2\), with squared norm \(\|w+z\|^2/4\). This establishes the formula as the exact two-invariant Gram solve, not as an independently substituted radial projection.

**2. Explicit inner orbit and branch count.** For \(r>0\), set \(e=w/r\). With \(v^{(0)}=mu+re\), every iterate is \(mu+t_je\) and
\[
t_{j+1}=r+\frac{\rho^2-r^2}{r+t_j}=\frac{rt_j+\rho^2}{r+t_j},\qquad t_0=r.
\]
All \(t_j\) are positive; the denominators and Gram determinants are therefore positive. The Cayley coordinate \(c(t)=(t-\rho)/(t+\rho)\) satisfies
\[
c(t_{j+1})=\frac{r-\rho}{r+\rho}\,c(t_j)=\kappa c(t_j),\qquad c(t_0)=\kappa.
\]
Since \(|\kappa|<1\), inversion gives the displayed exact orbit and its limit.

For any nonsingular fixed point \(v=mu+z\), mass and energy conservation imply \(z\perp u\) and \(\|z\|=\rho\). The correction equation projected to \(u^\perp\) makes \(z-w\) a scalar multiple of \(z+w\). Since \(w\ne0\), the coefficient cannot be one, and \(z\) must be collinear with \(w\). Thus only \(z=\pm\rho e\) are possible. The negative root is nonsingular exactly when \(r\ne\rho\); the positive root is always nonsingular. The positive root minimizes \(\|z-w\|\) among all points on the radius-\(\rho\) sphere by Cauchy--Schwarz. For \(r=0\), the starting Gram determinant is zero. At any \(v=mu+z\) with \(z\ne0\), the map is \(G_p(v)=mu+(\rho^2/\|z\|^2)z\), so the fixed points are exactly the stated sphere. In dimension at least three this is a continuum.

**3. Sharp stopping law and transient.** For \(0<r<\rho\), put \(a=(\rho-r)/(\rho+r)\in(0,1)\). The exact orbit gives, according to the parity of \(j\),
\[
\frac{|t_j-\rho|}{\rho}=\begin{cases}
2a^{j+1}/(1+a^{j+1}),&j\text{ even},\\
2a^{j+1}/(1-a^{j+1}),&j\text{ odd}.
\end{cases}
\]
Therefore an even index succeeds exactly when \(a^{j+1}\le\varepsilon/(2-\varepsilon)\), while an odd index succeeds exactly when \(a^{j+1}\le\varepsilon/(2+\varepsilon)\). The earliest successful index is bounded below by \(\log((2-\varepsilon)/\varepsilon)/(-\log a)-1\) and above by that expression plus at most two integer steps. Since
\[
-\log a=\log\frac{\rho+r}{\rho-r}=\frac{2r}{\rho}+O\big((r/\rho)^3\big),
\]
the exact limit for \(N_\varepsilon\) follows. Substituting \(j=1\) in the recurrence gives \(t_1=(r^2+\rho^2)/(2r)\).

**4. Realization by an explicit conservative predictor.** On \(u^\perp\), \(J^2=-I\) and \(J^3=-J\), so three nested explicit field evaluations produce
\[
I+hJ+h^2J^2+h^3J^3=(1-h^2)(I+hJ).
\]
Moreover, \(\|(I+hJ)w\|^2=(1+h^2)\|w\|^2\) by skew symmetry. Thus the predictor norm formula follows. Since \(|1-h^2|\sqrt{1+h^2}=2\sqrt2|h-1|+O((h-1)^2)\), substitution into the already established work limit proves the final coefficient. At \(h=1\), the starting point is uniform and the Gram matrix has rank one, which directly establishes the claimed singularity.

## Verification

Run `python3 checker.py`. The standard-library-only script performs more than one thousand exact rational Gram-solve and orbit checks with several masses, predictor radii, targets, and both implicit branches; it also checks the rank-collapse case, the parity-sensitive stopping count, and the explicit oscillator predictor. These finite checks support the proof but do not replace its algebraic and asymptotic arguments. The script's actual output is recorded in `CHECKS.txt`.

A convenient exact three-node instance is \(u=e_1\), \(m=0\), \(p=e_2\), and \(\rho=2\). The multipliers reduce to \(t_{j+1}=(t_j+4)/(1+t_j)\), and \(t_j=2(1+(-1/3)^{j+1})/(1-(-1/3)^{j+1})\), giving the alternating sequence \(1,5/2,13/7,\ldots\), converging to \(2\).

## Relationship to prior work

Pu and Ran, *A Multi-Invariant Preserving Discrete Gradient Methods* (2026, arXiv:2605.30827), define the Gram-based multi-invariant correction in their section 4 and prescribe predictor-initialized fixed-point iteration in Algorithm 1. They establish conservation, local accuracy, and existence under regularity assumptions; they do not state this exact mass--quadratic-energy Picard orbit, its two-branch classification, the sharp near-uniform iteration count, or the finite-step oscillator singularity. The present result analyzes their published method; it does not claim to invent the discrete gradient, Gram correction, or a new integration scheme.

Norton, McLaren, Quispel, Stern, and Zanna (arXiv:1302.2713) establish general equivalences between projection and discrete-gradient methods, including multiple first integrals, and give local well-posedness theory and numerical experiments. This broader framework does not directly specify the predictor-initialized Gram map here or imply its sharp inner-solver work asymptotic. Classical radial normalization immediately computes the nearest point when \(r>0\); the point is that the *prescribed iterative implementation* may require arbitrarily many updates even in this exactly solvable case.

## Limitations

The result is restricted to a linear invariant and an isotropic quadratic invariant, with a mass-preserving predictor and mean-value discrete gradients. It is an exact-arithmetic theorem, not a finite-precision complexity guarantee. The inner Picard iterates before convergence are not themselves necessarily energy-feasible; only their limit solves the implicit correction. The oscillator singularity occurs at a large step where the explicit predictor should not be expected to be accurate. No statement is made about other discrete gradients, generic nonlinear invariants, global outer convergence, or independently verified historical priority. Other published special-case analyses of the same rational fixed-point iteration could remain unindexed.

## References

1. H. Pu and M. Ran, *A Multi-Invariant Preserving Discrete Gradient Methods*, arXiv:2605.30827v1, publicly posted 2026-05-29, https://arxiv.org/html/2605.30827 . See Section 2 (mean-value gradient), Section 4 (Gram correction), Algorithm 1 (Picard initialization).
2. R. A. Norton, D. I. McLaren, G. R. W. Quispel, A. Stern, and A. Zanna, *Projection methods and discrete gradient methods for preserving first integrals of ODEs*, arXiv:1302.2713v1, 2013, https://arxiv.org/pdf/1302.2713 . See Sections 1, 4, and the multiple-integral example and discussion in Section 6.
3. R. A. Norton and G. R. W. Quispel, *Discrete gradient methods for preserving a first integral of an ordinary differential equation*, Discrete and Continuous Dynamical Systems 34 (2014), 1147--1170, https://doi.org/10.3934/dcds.2014.34.1147 . Background local solvability and linearly implicit quadratic cases.
