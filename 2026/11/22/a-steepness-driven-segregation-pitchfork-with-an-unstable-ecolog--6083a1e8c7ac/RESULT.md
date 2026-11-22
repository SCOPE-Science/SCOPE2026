# A steepness-driven segregation pitchfork with an unstable ecological onset

## Finding

In the two-patch, two-species competition model with competitor-induced sigmoidal emigration, imposing equal strong competition and centering the response at the symmetric coexistence density produces an **exact symmetry-breaking threshold**. When response steepness \(\xi\) crosses
\[
\xi_c=\frac{2(a+1)(\mu_0+\mu_S)-(a-1)}{a\mu_S},
\]
a pair of spatially segregated, positive coexistence *equilibria* emerges in a supercritical pitchfork. However, both new states are unstable in the unrestricted four-dimensional population system: they each have one positive eigenvalue. In particular, the birth of nonuniform stationary coexistence is not the onset of a stable ecological refuge.

Writing the spatial segregation contrast as \(d=u-v\), its near-threshold magnitude obeys
\[
d^2=\frac{\mu_S a/(a+1)}{(a-1)/2+\mu_Sa^3\xi_c^3/[48(a+1)]}(\xi-\xi_c)
+O((\xi-\xi_c)^2).
\]
The branch consists of one equilibrium with \(d>0\) and its species-and-patch reflected partner \(d<0\).

## Assumptions and scope

Consider two identical patches, species \(1,2\), and dimensionless population abundances \(x_i^j\geq0\), for species \(i\) in patch \(j\). For each patch \(j\), with \(k\ne j\) and the other species \(h\ne i\), define the four-dimensional smooth ODE
\[
\dot x_i^j=x_i^j(1-x_i^j-a x_h^j)
+ m(x_h^k)x_i^k-m(x_h^j)x_i^j,
\qquad
m(z)=\mu_0+\frac{2\mu_S}{1+\exp[\xi(\Delta-a z)]}.
\]
Assume \(a>1\), \(\mu_0>0\), \(\mu_S>0\), \(\xi>0\), and \(\Delta=a/(a+1)\). Let \(\xi_c>0\), equivalently \(2(a+1)(\mu_0+\mu_S)>a-1\). Conclusions are local for \(\xi\) in a sufficiently small interval about \(\xi_c\). The model is finite-dimensional, deterministic, and includes no evolution of intrinsic species traits. The positive equilibria near the symmetric state have all four coordinates positive; the theorem concerns equilibrium existence and local stability, not global persistence.

## Proof

**1. Invariant segregated plane and exact total-biomass equation.** The species-and-patch interchange symmetry leaves the two-dimensional subspace \((x_1^1,x_2^1,x_1^2,x_2^2)=(u,v,v,u)\) invariant. For \(s=u+v\), \(d=u-v\), and \(m\) as above, its equations are
\[
\dot s=s-\frac{a+1}{2}s^2+\frac{a-1}{2}d^2,
\qquad
\dot d=d(1-s)+s[m(u)-m(v)]-d[m(u)+m(v)].
\]
The spatially uniform coexistence equilibrium is \(s_0=2/(a+1)\), \(d=0\). The nearby positive stationary solution of the \(s\)-equation is uniquely
\[
s(d)=\frac{1+\sqrt{1+(a^2-1)d^2}}{a+1}
=\frac2{a+1}+\frac{a-1}{2}d^2+O(d^4).
\]
For small \(d\), the root has positive \(u=[s(d)+d]/2\) and \(v=[s(d)-d]/2\).

**2. Exact reduction and the cubic coefficient.** With \(w=1/(a+1)\) and \(k=\xi a/2\), the centered logistic mobility is precisely
\(m(z)=\mu_0+\mu_S[1+\tanh(k(z-w))]\).
Put \(z=k[s(d)-s_0]/2\) and \(y=kd/2\). Then
\[
\dot d=d[1-s(d)-2(\mu_0+\mu_S)]
+\mu_Ss(d)[\tanh(z+y)-\tanh(z-y)]
-\mu_Sd[\tanh(z+y)+\tanh(z-y)]
\]
when evaluated on the stationary total-biomass curve. Since \(z=O(d^2)\), \(y=O(d)\), the difference of hyperbolic tangents is \(kd-k^3d^3/12+O(d^5)\), and their sum is \(k[s(d)-s_0]+O(d^4)\). The two terms proportional to \(\mu_S k[s(d)-s_0]d\) cancel. Consequently the stationary contrast equation divided by \(d\ne0\) has analytic even expansion
\[
0=\lambda_{\rm seg}(\xi)-h(\xi)d^2+O(d^4),
\qquad
\lambda_{\rm seg}(\xi)=\frac{a-1}{a+1}-2(\mu_0+\mu_S)+\frac{\mu_Sa}{a+1}\xi,
\]
\[
h(\xi)=\frac{a-1}{2}+\frac{\mu_Sa^3\xi^3}{48(a+1)}>0.
\]
Thus \(\lambda_{\rm seg}(\xi_c)=0\), with strictly positive derivative \(\mu_Sa/(a+1)\). The implicit-function theorem applied to \(d^2\) gives exactly one small positive \(d^2\) solution for \(\xi>\xi_c\), no such solution for \(\xi<\xi_c\), and the displayed quadratic-amplitude expansion. Reflection symmetry produces precisely the two signed branches. This proves supercriticality **on the invariant segregation plane**; no other nearby equilibria are asserted to be excluded outside this plane.

**3. The bifurcating equilibria are full-system saddles.** At the uniform coexistence equilibrium, spatially uniform species-composition perturbations see the usual competition matrix
\[
-\frac1{a+1}\begin{pmatrix}1&a\\a&1\end{pmatrix},
\]
whose eigenvalues are \(-1\) and \((a-1)/(a+1)>0\). The two spatially antisymmetric eigenvalues are \(\lambda_{\rm seg}(\xi)\) and \(-1-2(\mu_0+\mu_S)-\mu_Sa\xi/(a+1)<0\). At \(\xi=\xi_c\) there is exactly one zero eigenvalue and exactly one positive eigenvalue. On the segregated branches the center eigenvalue becomes negative: the reduced stationary contrast derivative is \(-2\lambda_{\rm seg}+O((\xi-\xi_c)^2)<0\), while the total-biomass eigenvalue remains negative. By continuity of the other two eigenvalues, every sufficiently small bifurcating segregated equilibrium has exactly one positive and three negative real eigenvalues. Hence neither is locally attracting in the complete population system.

## Verification

The companion program `verify.py` reconstructs the stationary branch, independently evaluates the full four-variable Jacobian and its eigenvalues, and checks the exact threshold and cubic normalization. For the admissible rational parameters \(a=2\), \(\mu_0=1/3\), \(\mu_S=1/6\), one finds \(\xi_c=6\) and
\[
d^2=\frac2{45}(\xi-6)+O((\xi-6)^2).
\]
Root checks at \(\xi-6=1/10,1/100,1/1000\) verify the predicted square-root approach and one-positive-eigenvalue pattern. These finite checks support but do not replace the analytic proof for all stated parameters.

## Relationship to prior work

Mattei, Soriano-Paños and Arenas (arXiv:2601.13947, v1, 20 January 2026) introduce the exact competitor-induced sigmoid mobility above, analyze asymmetric competition and limiting activation thresholds, and illustrate coexistence numerically. Their inspected main results and appendix do not provide the symmetric local pitchfork formula, cubic coefficient, or the full-space saddle index near onset. Sun and Mai (2019) analyze two-patch competition with **constant delayed dispersal**; their model has no state-dependent sigmoid derivative controlling segregation onset. Existing general local bifurcation theory supplies the implicit-function and eigenvalue-continuity tools, not these model-specific coefficients.

## Limitations

This is a local result at equal interspecific competition and the centered activation threshold. It does not claim stable coexistence near the pitchfork, nor exclude distant attracting segregated states, other symmetry types, heteroclinic behavior, or higher-dimensional lattice patterns. It does not prove historical uniqueness, and an older two-patch dispersal study by Mai, Sun and Wang (2023, DOI 10.1002/mma.9137) was available only in abstract form during the comparison; its coverage risk remains for independent review. No independent audit has been performed.

## References

- M. Mattei, D. Soriano-Paños and A. Arenas, *Nonlinear competition avoidance favors coexistence in microbial populations*, arXiv:2601.13947v1 (2026), https://arxiv.org/pdf/2601.13947.
- G. Sun and A. Mai, *Stability Analysis of a Two-Patch Competition Model with Dispersal Delays*, Discrete Dynamics in Nature and Society 2019, 3159591, https://doi.org/10.1155/2019/3159591.
- A. Mai, G. Sun and L. Wang, *Effects of dispersal on competitive coexistence in a two-patch competition model*, Mathematical Methods in the Applied Sciences 46 (2023), 10527–10539, https://doi.org/10.1002/mma.9137.
