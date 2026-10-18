# Passive bone mass creates a neutral direction and an exact cycle-closure law
## Finding
Consider the alcohol-modified bone-remodeling model
\[
\dot C=f(C,B),\qquad
\dot B=g(C,B),\qquad
\dot z=H(C,B),
\]
with
\[
H(C,B)=-k_1(C-\bar C)_+ + k_2(B-\bar B)_+,
\qquad
(u)_+=\max(u,0).
\]
The first two equations describe osteoclast and osteoblast populations, while \(z\) is bone mass.

The full system has an exact translation symmetry in the bone-mass coordinate:
\[
(C,B,z)\mapsto(C,B,z+c).
\]
Consequently, any cell equilibrium \((C_*,B_*)\) that also satisfies
\[
H(C_*,B_*)=0
\]
lifts to an entire line of full equilibria,
\[
\mathcal E_*=
\{(C_*,B_*,z):z\in\mathbb R\},
\]
or to the intersection of this line with a physically imposed bone-mass domain. No single point of \(\mathcal E_*\) can be locally asymptotically stable as a three-dimensional equilibrium. If the source's thresholds \(\bar C,\bar B\) are the equilibrium cell counts, then
\[
H(\bar C,\bar B)=0
\]
automatically.

There is also an exact closure law for periodic cell dynamics. If
\[
(C(t+T),B(t+T))=(C(t),B(t))
\]
for all \(t\), then
\[
z(t+T)-z(t)=\Delta,
\]
where
\[
\Delta=
\int_0^T
\left[
-k_1(C(s)-\bar C)_+
+k_2(B(s)-\bar B)_+
\right]\,ds.
\]
Therefore the full state is \(T\)-periodic if and only if
\[
\Delta=0.
\]
When \(\Delta\ne0\),
\[
z(t+nT)=z(t)+n\Delta
\]
for every integer \(n\ge0\). A periodic or neutral-center orbit in the cell subsystem is thus insufficient by itself to guarantee periodic bone mass.

## Assumptions and scope
The model is exactly the three-equation system printed by Chaiya et al. The cell equations have the form
\[
\dot C=f(C,B),\qquad \dot B=g(C,B)
\]
and contain no \(z\)-dependence. The bone-mass equation contains \(C\) and \(B\) but no \(z\)-dependence.

All parameters \(k_1,k_2,\bar C,\bar B\) are treated as fixed during a trajectory. The positive-part function is
\[
(u)_+=\max(u,0).
\]

The equilibrium-line statement applies to every cell equilibrium satisfying
\[
H(C_*,B_*)=0.
\]
The paper defines \(\bar C,\bar B\) as equilibrium osteoclast and osteoblast counts. When those thresholds coincide with the cell equilibrium being considered, the flux condition is automatic.

The cycle-closure law applies to every \(T\)-periodic solution of the two-dimensional cell subsystem. It does not assume linearization, a particular amplitude, or a particular alcohol-consumption regime.

## Proof
Because \(z\) does not occur in \(f\), \(g\), or \(H\), if
\[
(C(t),B(t),z(t))
\]
solves the full system, then for every constant \(c\),
\[
(C(t),B(t),z(t)+c)
\]
has the same derivatives and is also a solution. This proves vertical translation symmetry.

Now let \((C_*,B_*)\) satisfy
\[
f(C_*,B_*)=g(C_*,B_*)=H(C_*,B_*)=0.
\]
Then for every constant \(z_*\),
\[
(C(t),B(t),z(t))=(C_*,B_*,z_*)
\]
is an equilibrium. Hence the full equilibrium is not isolated.

Choose any point
\[
E=(C_*,B_*,z_*).
\]
For every sufficiently small nonzero \(\varepsilon\), the nearby point
\[
E_\varepsilon=(C_*,B_*,z_*+\varepsilon)
\]
is also an equilibrium. Its trajectory stays a fixed distance \(|\varepsilon|\) from \(E\), so it cannot converge to \(E\). Thus \(E\) is not locally asymptotically stable as a point equilibrium. This argument does not require differentiability of the positive-part function.

For the periodic statement, integrate the bone-mass equation over one cell period:
\[
z(t+T)-z(t)
=
\int_t^{t+T}H(C(s),B(s))\,ds.
\]
Since \(H(C(s),B(s))\) is \(T\)-periodic, a change of variables gives
\[
\int_t^{t+T}H(C(s),B(s))\,ds
=
\int_0^T H(C(s),B(s))\,ds
=
\Delta,
\]
independent of \(t\). Iteration yields
\[
z(t+nT)=z(t)+n\Delta.
\]
If \(\Delta=0\), then \(z(t+T)=z(t)\), so the full state is \(T\)-periodic. If \(\Delta\ne0\), the stroboscopic values of \(z\) drift linearly and the full state cannot be \(T\)-periodic. This proves necessity and sufficiency.

Finally, suppose a cell trajectory converges to a threshold equilibrium and its deviation is sufficiently integrable that
\[
\int_0^\infty |H(C(t),B(t))|\,dt<\infty.
\]
Then
\[
z(t)=z(0)+\int_0^t H(C(s),B(s))\,ds
\]
converges to a finite limit. Translation symmetry still implies that changing only \(z(0)\) changes this limiting value by the same constant, so the limit is not a unique asymptotically stable point of the full system.

## Verification
The result is analytic and requires no finite enumeration or numerical certificate.

The model equations were checked against the full text of the motivating article. Equation (2.3) has no \(z\)-dependence, and Section 3 explicitly removes that equation before computing steady states and the two-dimensional Jacobian for \(C\) and \(B\). Thus the neutral direction is not an artifact of rewriting the model.

The periodic closure law follows by direct integration over one period. It is exact for the nonsmooth positive-part flux because only continuity and periodicity of the integrand are needed.

The conclusion is deliberately limited. A displayed numerical trajectory in which \(z(t)\) approaches a constant is compatible with the theorem. What fails is pointwise three-dimensional asymptotic stability: a vertical perturbation in the initial bone mass persists additively. Likewise, a periodic cell orbit can produce periodic bone mass, but only when the exact net cycle flux \(\Delta\) vanishes.

## Relationship to prior work
The motivating article extends the Komarova bone-remodeling model with alcohol-dependent terms in the cell equations. It states that the stability analysis is performed on equations (2.1) and (2.2) after isolating equation (2.3), and it classifies the resulting cell equilibria using a two-dimensional Jacobian. Its simulations then interpret periodic, increasing, decreasing, or convergent bone-mass traces.

The original Komarova model already used a passive bone-mass equation driven by the excess numbers of osteoclasts and osteoblasts. Komarova et al. numerically displayed repeated remodeling cycles and analyzed stability of the cell equations. The accessible full text does not state the translation-symmetry consequence, the non-isolation of full equilibria, or the exact necessary-and-sufficient cycle balance \(\Delta=0\).

Ramtani et al. later retained the same passive bone-mass construction in a tumor-coupled extension and again reported periodic bone mass alongside periodic cell dynamics. Their open full text presents the bone equation and performs stability analysis on the active cell/tumor subsystem. It does not provide the exact full-state closure law used here.

The present finding therefore does not claim that passive bone-mass integration is new. The contribution is the source-specific structural completion: it identifies exactly what the two-dimensional stability calculation can and cannot establish for the three-dimensional alcohol model and supplies the missing scalar balance condition for genuine periodic bone mass.

## Limitations
The theorem does not challenge the numerical integration shown in the motivating article. It distinguishes full-state stability from transverse cell stability and gives a condition that any periodic bone-mass simulation must satisfy.

The result does not determine whether every plotted periodic trace in the paper satisfies \(\Delta=0\) to numerical precision. It also does not quantify the transient integral in each stable-spiral simulation.

No claim is made that a passive bone-mass coordinate is biologically optimal. Models with feedback from bone density to the cell equations, such as later porosity-coupled systems, do not have the same translation symmetry.

## References
1. I. Chaiya, T. Kaewkrathok, A. Ploykanha, D. Prathumwan, K. Trachoo, “Mathematical modeling of alcohol-induced effects on bone remodeling dynamics,” AIMS Mathematics 10 (2025), 27696–27717. DOI: 10.3934/math.20251218.
2. S. V. Komarova, R. J. Smith, S. J. Dixon, S. M. Sims, L. M. Wahl, “Mathematical model predicts a critical role for osteoclast autocrine regulation in the control of bone remodeling,” Bone 33 (2003), 206–215. DOI: 10.1016/S8756-3282(03)00157-1.
3. S. Ramtani, J. F. Sánchez, A. Boucetta, R. Kraft, J. J. Vaca-González, “A coupled mathematical model between bone remodeling and tumors: a study of different scenarios using Komarova’s model,” Biomechanics and Modeling in Mechanobiology 22 (2023), 1095–1113. DOI: 10.1007/s10237-023-01689-3.
