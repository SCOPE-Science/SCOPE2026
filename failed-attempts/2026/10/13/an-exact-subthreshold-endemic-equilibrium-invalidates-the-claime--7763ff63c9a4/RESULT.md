# An exact subthreshold endemic equilibrium invalidates the claimed global disease-free stability

## Finding

Consider the vector-host system
\[
\begin{aligned}
S_h'&=\Lambda_h-\frac{\beta_1S_hI_v}{1+\alpha_1I_v}-\mu_hS_h,\\
I_h'&=\frac{\beta_1S_hI_v}{1+\alpha_1I_v}-(\mu_h+\delta_h)I_h-\frac{\gamma uI_h}{1+buI_h},\\
R_h'&=\frac{\gamma uI_h}{1+buI_h}-\mu_hR_h,\\
S_v'&=\Lambda_v-\frac{\beta_2S_vI_h}{1+\alpha_2I_h}-\mu_vS_v,\\
I_v'&=\frac{\beta_2S_vI_h}{1+\alpha_2I_h}-\mu_vI_v.
\end{aligned}
\]

The published Theorem 3.3 claims global asymptotic stability of the disease-free equilibrium whenever
\[
R_0<1.
\]
An exact positive endemic equilibrium exists below that threshold.

Set
\[
\Lambda_h=\frac{871}{5000},\qquad
\Lambda_v=\frac{121}{400},\qquad
\mu_h=\frac1{10},\qquad
\mu_v=\frac12,
\]
\[
\beta_1=\beta_2=1,\qquad
\alpha_1=\alpha_2=\frac1{10},\qquad
\delta_h=\frac1{10},\qquad
\gamma=2,\qquad
u=1,\qquad
b=20.
\]
Then
\[
R_0^2=\frac{9581}{10000}<1,
\]
while
\[
E_*=
\left(
\frac{1313}{1500},
\frac1{10},
\frac23,
\frac{101}{200},
\frac1{10}
\right)
\]
is an exact endemic equilibrium.

Moreover,
\[
S_h+I_h+R_h
=
\frac{821}{500}
<
\frac{\Lambda_h}{\mu_h}
=
\frac{871}{500},
\]
and
\[
S_v+I_v
=
\frac{121}{200}
=
\frac{\Lambda_v}{\mu_v},
\]
so the equilibrium lies in the biological region used for the model.

A trajectory initialized at \(E_*\) is constant and cannot approach the disease-free equilibrium. Hence the claimed global attractivity, and therefore the claimed global asymptotic stability, is false.

The same witness exposes the failure of the published Lyapunov calculation. Substituting \(E_*\) into the right-hand side printed as equation (3.8) gives
\[
-\frac{264869}{3030000},
\]
but the actual orbital derivative at an equilibrium must be zero.

## Assumptions and scope

All parameters are positive, and \(u=1\) is within the treatment-intensity range used in the model family.

The reproduction number is the source's
\[
R_0
=
\sqrt{
\frac{\beta_1\beta_2\Lambda_h\Lambda_v}
{\mu_v^2\mu_h(\mu_h+\delta_h+\gamma u)}
}.
\]

The finding concerns Theorem 3.3, which states global disease-free stability from \(R_0<1\). It does not challenge the source's local disease-free stability theorem and does not classify the stability of the endemic equilibria.

No sharp replacement global threshold is claimed.

## Proof

At any positive endemic equilibrium, the vector equations give
\[
S_v
=
\frac{\Lambda_v(1+\alpha_2I_h)}
{\beta_2I_h+\mu_v(1+\alpha_2I_h)},
\]
\[
I_v
=
\frac{\beta_2S_vI_h}
{\mu_v(1+\alpha_2I_h)},
\]
\[
S_h
=
\frac{\Lambda_h}
{\mu_h+\beta_1I_v/(1+\alpha_1I_v)},
\]
and
\[
R_h
=
\frac{\gamma uI_h}
{\mu_h(1+buI_h)}.
\]

Substituting the stated rational parameters reduces the remaining infected-host equilibrium equation to
\[
-\frac{
I_h(10I_h-1)(286420I_h-4609)
}{
50(20I_h+1)(14321I_h+1000)
}
=0.
\]
Thus
\[
I_h=\frac1{10}
\]
is an exact positive root. Substituting it into the equilibrium formulas gives
\[
S_h=\frac{1313}{1500},\qquad
R_h=\frac23,\qquad
S_v=\frac{101}{200},\qquad
I_v=\frac1{10}.
\]
Direct substitution into all five differential equations gives zero.

The reproduction number obeys
\[
R_0^2
=
\frac{
\beta_1\beta_2\Lambda_h\Lambda_v
}{
\mu_v^2\mu_h(\mu_h+\delta_h+\gamma u)
}
=
\frac{9581}{10000}.
\]
Therefore
\[
R_0<1.
\]

The disease-free equilibrium is
\[
P_0=
\left(
\frac{871}{500},0,0,\frac{121}{200},0
\right),
\]
which is distinct from \(E_*\). Since the solution with initial condition \(E_*\) is identically \(E_*\), \(P_0\) cannot attract every initial state in the biological region.

For the Lyapunov check, evaluate the five terms printed on the right-hand side of equation (3.8) at \(E_*\). Exact simplification gives
\[
-\frac{264869}{3030000}.
\]
Yet along the constant equilibrium trajectory,
\[
\frac{d}{dt}L(E_*)=0.
\]
Consequently the printed equation (3.8) is not an identity for the orbital derivative of the proposed \(L\).

## Verification

The bundled `verify.py` uses exact rational and symbolic arithmetic.

It verifies all five equilibrium residuals, the exact value
\[
R_0^2=\frac{9581}{10000},
\]
the biological-region inequalities, and the exact factorization of the infected-host equilibrium equation.

It then evaluates the source's printed equation-(3.8) expression at the witness and obtains
\[
-\frac{264869}{3030000}.
\]

No floating-point computation is used to establish the counterexample.

## Relationship to prior work

The motivating source derives a local disease-free threshold, studies endemic equilibria and backward-bifurcation calculations, and then states in Theorem 3.3 that \(R_0<1\) is sufficient for global asymptotic stability of the disease-free equilibrium.

The broader phenomenon is well known for saturated treatment: a reproduction number below one need not exclude endemic equilibria. Pérez gives a different epidemic model in which a backward-bifurcation interval below one contains two endemic equilibria and the disease-free equilibrium is globally stable only below a stricter threshold. Later network-SIS work with saturated treatment likewise makes global disease-free stability below one conditional on uniqueness of the disease-free equilibrium.

Those broader results do not imply the exact source-specific counterexample above. The new content is the exact admissible parameter vector for this vector-host model, the exact subthreshold endemic equilibrium, and the direct diagnosis that the published Lyapunov derivative is nonzero at that equilibrium.

Searches by DOI, exact title, theorem topic, saturated-treatment aliases, subthreshold endemic-equilibrium language, and correction terminology did not locate a published correction of Theorem 3.3.

## Limitations

The result disproves the global theorem but does not determine whether either endemic equilibrium is stable.

It does not provide the sharp global eradication threshold for the full vector-host model.

An unindexed author correction could exist outside the checked records.

## References

1. M. A. Khan, N. Iqbal, Y. Khan, E. Alzahrani, “A biological mathematical model of vector-host disease with saturated treatment function and optimal control strategies,” Mathematical Biosciences and Engineering 17 (2020), 3972–3997. DOI: 10.3934/mbe.2020220.
2. Á. G. C. Pérez, “Bifurcation Analysis of an SIR Model with Logistic Growth, Nonlinear Incidence, and Saturated Treatment,” Complexity (2019), Article 9876013. DOI: 10.1155/2019/9876013.
3. X. Wei, X. Zhao, Y. Zhou, “Global stability of a network-based SIS epidemic model with a saturated treatment function,” Physica A 597 (2022), 127295. DOI: 10.1016/j.physa.2022.127295.
