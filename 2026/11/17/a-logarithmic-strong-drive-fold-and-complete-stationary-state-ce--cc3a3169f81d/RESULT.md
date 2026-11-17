# A logarithmic strong-drive fold and complete stationary-state census for the active three-state Potts flow

## Finding

Consider the spatially homogeneous continuous-time three-state active Potts mean-field equations with ferromagnetic coupling \(k=\beta zJ>0\), cyclic bias \(b=\beta h>0\), and Glauber transition rates as defined below. Put
\[
c_*=1+\log(3/2).
\]
There exist \(b_0>0\) and a unique smooth cyclically triple saddle-node threshold \(k_{\mathrm{SN}}(b)\) in a fixed-width neighborhood of \(b+\log b+c_*\), for \(b>b_0\), satisfying
\[
\boxed{k_{\mathrm{SN}}(b)=b+\log b+c_*+\frac{\log b+c_*-1}{b}+O\!\left(\frac{(\log b)^2}{b^2}\right)}.
\]
More globally in the strong-drive scaling, fix any real \(c\ne c_*\), and choose for each sufficiently large \(b\) the unique \(k>b\) satisfying \(k-b-\log k=c\). If \(c<c_*\), the mean-field system has **exactly one** stationary state on its closed probability simplex, namely \((1/3,1/3,1/3)\). If \(c>c_*\), it has **exactly seven** stationary states: the uniform state, three asymptotically stable ordered nodes and three saddles, all in the interior. Their cyclic permutations are distinguished by the majority state. With state \(0\) the majority, the corresponding two ordered branches obey
\[
(\rho_0,\rho_1,\rho_2)=\left(1-\frac{2u_\pm(c)}{k}+o(k^{-1}),\frac{u_\pm(c)}{k}+o(k^{-1}),\frac{u_\pm(c)}{k}+o(k^{-1})\right),
\]
where \(0<u_-(c)<1/3<u_+(c)\) are the two positive roots of
\[
2u=e^{-c+3u},\qquad u_\pm(c)=-\frac13W_{0,-1}\!\left(-\frac32e^{-c}\right).
\]
The lower root is the stable-node branch and the upper is the saddle branch. The uniform state is also linearly asymptotically stable in both strong-drive regimes. The classification is of equilibria, not of all periodic or recurrent trajectories.

## Assumptions and scope

Let \(\rho_i\ge0\), \(\sum_{i=0}^2\rho_i=1\), with indices read modulo three. Define \(\sigma(s)=(1+e^{-s})^{-1}\), \(w_i=\sigma\!\bigl(b+k(\rho_{i+1}-\rho_i)\bigr)\), and cyclic edge currents
\[
J_i=(\rho_i+\rho_{i+1})w_i-\rho_{i+1}.
\]
The evolution, after dividing time by the positive Glauber time constant, is
\[
\dot\rho_i=J_{i-1}-J_i.
\]
These equations are precisely the zero-gradient, spatially homogeneous specialization of equations (5)–(7) in Tateyama et al., arXiv:2611.09180v1. The three forward and backward rates along any edge sum to one. All rates are strictly positive for finite parameters, so the closed simplex is forward invariant and all its equilibria lie in its interior. The theorem is an asymptotic statement as \(b\to\infty\) with \(k-b-\log k\) bounded; no claim is made about the complete finite-b global bifurcation diagram.

The saddle-node assertion means a locally unique simultaneous fold near each of the three simplex vertices. The full equilibrium counts hold for every fixed \(c\ne c_*\), once \(b\) is sufficiently large depending on \(c\); the precisely critical scaling at \(c=c_*\) is resolved instead by the displayed finite-b fold expansion.

## Proof

**1. Reduction near a majority-state vertex.** Write \(\rho_0=1-x-y\), \(\rho_1=x\), \(\rho_2=y\). The exact currents are
\[
J_0=(1-y)w_0-x,\quad J_1=(x+y)w_1-y,\quad J_2=(1-x)w_2-(1-x-y),
\]
with \(\dot x=J_0-J_1\), \(\dot y=J_1-J_2\). Set \(\varepsilon=1/k\), \(u=kx\), \(v=ky\), \(c=k-b-\log k\). For bounded \(u,v,c\) and \(\varepsilon\downarrow0\), the first rate has the **exact** representation
\[
w_0=\frac{\varepsilon A}{1+\varepsilon A},\qquad A=e^{-c+2u+v}.
\]
The other two rates differ from one by exponentially small quantities, with the same control on every fixed finite number of derivatives. Thus the rescaled vector field \((\dot u,\dot v)=(k\dot x,k\dot y)\), which is conjugate to the original field under this coordinate change, satisfies on every compact set the \(C^2\) expansion
\[
\dot u=A-2u-\varepsilon A(A+v)+O(\varepsilon^2),\qquad
\dot v=u-v+O(e^{-\eta/\varepsilon})
\]
for some local \(\eta>0\). This follows by expanding \((1-\varepsilon v)A/(1+\varepsilon A)\) while retaining the exact exponentially suppressed reverse rates.

**2. Limiting roots and their stability.** At \(\varepsilon=0\), the stationary equations give \(v=u>0\) and \(2u=e^{-c+3u}\). Equivalently, \(c=3u-\log(2u)\). This function has its unique minimum \(c_*=1+\log(3/2)\) at \(u=1/3\). It has zero positive roots for \(c<c_*\), one double root for \(c=c_*\), and two simple roots for \(c>c_*\). At a simple root the linearization is
\[
D F_0(u,u)=\begin{pmatrix}4u-2&2u\\1&-1\end{pmatrix},\quad
\operatorname{tr}DF_0=4u-3,\quad\det DF_0=2-6u.
\]
Its discriminant is \(16u^2+1>0\). Thus \(u_-<1/3\) is a stable node and \(u_+>1/3\) is a saddle. The implicit-function theorem transfers these two nondegenerate roots and their types to the finite-parameter dynamics, and cyclic relabeling produces three copies of each.

**3. No overlooked equilibria.** Suppose \(b_j\to\infty\), \(k_j-b_j-\log k_j\) bounded, and take an arbitrary sequence of equilibria. Pass to a subsequence converging in the compact closed simplex. If this limit is not a simplex vertex, every cyclic density difference is strictly less than one, so every forward rate tends uniformly to one along the subsequence. The limiting stationary equations are those of the directed three-cycle, \(\dot\rho_i=\rho_{i-1}-\rho_i\); their sole solution is the uniform state. The Jacobian there converges to the Hurwitz directed-cycle Jacobian, so the uniform equilibrium is locally unique for large parameters.

Otherwise, by symmetry suppose \(\rho_0\to1\), \(x=\rho_1\to0\), \(y=\rho_2\to0\). In this region \(1-w_1\) and \(1-w_2\) are \(O(e^{-(1-o(1))b})\), so equality of stationary currents implies
\[
y-x=O(e^{-(1-o(1))b}),\qquad (1-y)w_0=2x+O(e^{-(1-o(1))b}).
\]
Since \(w_0\ge\sigma(-\log k-c)\), it follows that \(x\ge C/k\) for some \(C>0\), so \(y/x\to1\). Put \(u=kx\), \(v=ky\); then \(u\) is bounded away from zero and \(v/u\to1\). The exact logistic odds identity and current balance give
\[
\log(2u)+o(1)=-c+2u+v.
\]
If \(u\to\infty\), its right-hand side grows at least linearly, contradicting the logarithmic left-hand side. Hence \((u,v)\) stays in a compact subset of the positive quadrant and every limit point obeys \(v=u\), \(2u=e^{-c+3u}\). For fixed \(c\ne c_*\), step 2 and local uniqueness around each simple root therefore exhaust **all** stationary states. The boundary has no stationary states because rates are strictly positive.

**4. Quantitative location of the fold.** Near \(u=v=1/3\), the second stationary equation determines \(v=u+O(e^{-\eta/\varepsilon})\) smoothly. Substitution into the first gives the scalar equation
\[
H(u,c,\varepsilon)=e^{-c+3u}-2u-\varepsilon e^{-c+3u}\bigl(u+e^{-c+3u}\bigr)+O(\varepsilon^2)=0
\]
in \(C^2\) on a neighborhood of the fold. At \((u,c,\varepsilon)=(1/3,c_*,0)\), \(H=H_u=0\), \(H_{uu}=6\), \(H_c=-2/3\). Therefore the equations \(H=H_u=0\) have a unique smooth solution \((u_{\rm SN}(\varepsilon),c_{\rm SN}(\varepsilon))\) for small positive \(\varepsilon\), with a genuine quadratic saddle-node because the relevant derivatives do not vanish. Since the coefficient of \(\varepsilon\) in \(H\) at that point is \(-2/3\), differentiation along the fold gives
\[
c_{\rm SN}(\varepsilon)=c_*-\varepsilon+O(\varepsilon^2).
\]
Because \(c=k-b-\log k\) and \(\varepsilon=1/k\), inversion yields
\[
k_{\rm SN}(b)=b+\log b+c_*+\frac{\log b+c_*-1}{b}+O\!\left(\frac{(\log b)^2}{b^2}\right).
\]
Local uniqueness together with the compactness argument in step 3 excludes any other strong-drive saddle-node in this bounded-offset window.

**5. Stability of the remaining equilibrium.** The exact homogeneous linearization at \(\rho_i=1/3\) has the two physical eigenvalues
\[
\lambda_\pm=-\frac32\left(1-\frac{k(1-\zeta^2)}3\right)\pm i\frac{\sqrt3}2\zeta,
\qquad \zeta=\tanh(b/2).
\]
For \(k=b+O(\log b)\), \(k(1-\zeta^2)\to0\). Hence its real parts are negative for all sufficiently large \(b\). The separate Hopf threshold from the source is \(k_{\rm H}=3/(1-\zeta^2)=3\cosh^2(b/2)\sim3e^b/4\), far above the logarithmic fold scale.

## Verification

The standalone `verify.py` computes the exact original Glauber currents (not a limiting surrogate), computes complex-step Jacobians, numerically locates four finite-b folds, and checks two pairs of stable-node/saddle equilibria on the high-coupling side. It also checks uniform-state residuals. Its completed output was:

```text
FOLD b= 8.0 k= 11.778519537091 k_asymp= 11.795519981012 scaled_minorities= 0.36785852 0.36761191
FOLD b= 20.0 k= 24.564268064514 k_asymp= 24.571257250745 scaled_minorities= 0.34813508 0.34813508
FOLD b= 40.0 k= 45.193789303435 k_asymp= 45.196703176278 scaled_minorities= 0.34105463 0.34105463
FOLD b= 80.0 k= 85.846235719159 k_asymp= 85.847335389567 scaled_minorities= 0.33730943 0.33730943
ORDERED_BRANCHES b= 20.0 c= 1.9054651 root_types= ['node', 'saddle']
ORDERED_BRANCHES b= 40.0 c= 1.9054651 root_types= ['node', 'saddle']
BELOW_THRESHOLD b= 40.0 c= 0.9054651 center_residual= 1.1102230246251565e-16
VERIFY_OK fold_points=4 ordered_pairs=2 uniform_equilibria=3; FINITE_CHECK_ONLY
```

Run with `python verify.py` using NumPy and SciPy. This finite check is not a proof of global completeness or asymptotic universality; those follow from steps 1–5.

## Relationship to prior work

Tateyama et al. (2026), Section III C and Figure 2, introduce this homogeneous reduction and demonstrate three simultaneous symmetry-related saddle-nodes numerically at finite cyclic biases, while Section III A provides the disordered-state Hopf threshold. The present result gives the previously unstated **analytical high-drive saddle-node scale**, its second asymptotic correction, and a **complete global equilibrium count** on both sides for every fixed noncritical rescaled parameter. Earlier cyclic active-Potts work by Noguchi, van Wijland and Fournier (2024) uses a distinct non-equilibrium continuum approximation and stochastic lattice model to study traveling and spiral-wave modes; it does not supply this strong-bias equilibrium census for the later equations. These literature comparisons support provisional originality but cannot certify historical priority over all possible generic singular perturbation theorems.

## Limitations

All conclusions concern the deterministic spatially homogeneous mean-field ODE and the scaling \(b\to\infty\), \(k-b-\log k=O(1)\); they do not count spatially patterned steady states, periodic orbits, heteroclinic trajectories or equilibria outside the specified parameter scaling. At exactly \(c=c_*\), the lower-order fold shift must be retained, so the fixed-c one-versus-seven alternative is intentionally not asserted. The theorem does not imply the stationary-state census for finite stochastic lattice models. No independent mathematical audit has been performed.

## References

1. Y. Tateyama, S. Yin, H. Ito, H. Kitahata, and H. Noguchi, *Continuum mean-field theory of spatiotemporal pattern formation in a three-state active Potts model*, arXiv:2611.09180v1 (publicly posted 2026-11-06), especially equations (5)–(10), Section III C, Figure 2 and supplemental sections.
2. H. Noguchi, F. van Wijland, and J.-B. Fournier, *Cycling and spiral-wave modes in an active cyclic Potts model*, arXiv:2311.05257, J. Chem. Phys. 161, 025101 (2024), especially Sections II and IV.
3. H. Noguchi and J.-B. Fournier, *Spatiotemporal patterns in the active cyclic Potts model*, arXiv:2407.02985, New J. Phys. 26, 093043 (2024); title and abstract consulted for scope comparison.
