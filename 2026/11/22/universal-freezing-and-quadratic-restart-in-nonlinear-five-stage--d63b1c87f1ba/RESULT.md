# Universal freezing and quadratic restart in nonlinear five-stage commutator splitting

## Finding

For the energy-associated, symmetric five-stage commutator scheme (5C) applied to the nonlinear damped Hamiltonian family below, one positive step size annihilates the modified Hamiltonian subflow **for every potential in the stated class**. Precisely, if \(h_*=6\sqrt{2}/\gamma\), the numerical one-step map is
\[
\Phi_{h_*}(x,y)=(e^{-\gamma h_*}x,y).
\]
Every point \((0,y)\) is therefore a numerical equilibrium and the iteration from any \((x_0,y_0)\) converges to \((0,y_0)\), whereas the continuous system converges globally to \((0,0)\).

This is not merely a single exactly resonant step. For each fixed real \(y_0\), as \(h\to h_*\),
\[
\pi_y\Phi_h(0,y_0)-y_0
= -\bigl(1+e^{-4\sqrt2}\bigr)\omega^2 V'(y_0)(h-h_*)^2
+O\bigl(|h-h_*|^3\bigr).
\]
If \(\kappa=V''(0)>0\), the spectral radius of the linearized map at the origin satisfies the sharp two-sided relation
\[
1-\rho(D\Phi_h(0,0))
=\kappa\omega^2\,
\frac{(1+e^{-2\sqrt2})(1+e^{-4\sqrt2})}{1-e^{-6\sqrt2}}
(h-h_*)^2+O\bigl(|h-h_*|^3\bigr).
\]
Thus local linear relaxation becomes arbitrarily slow as the step approaches the universal freezing step, even while the method remains non-increasing in energy.

## Assumptions and scope

Let \(\gamma>0\), \(\omega\in\mathbb R\setminus\{0\}\), and let \(V\in C^4(\mathbb R)\) be coercive and strictly convex, with unique minimizer at \(y=0\), \(V(0)=0\) and \(V''(0)=\kappa>0\). Set
\[
H(x,y)=\tfrac12x^2+V(y),\quad
J=\omega\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
R=\begin{pmatrix}\gamma&0\\0&0\end{pmatrix}.
\]
The exact ODE is
\[
\dot x=-\gamma x-\omega V'(y),\qquad \dot y=\omega x.
\]
Use exact subflows in the source's 5C splitting, with its specified \(1/6,1/2,2/3,1/2,1/6\) coefficients and conservative correction \(\widehat{J}=J-h^2C/72\). Both conservative subflows are evaluated at the fixed step-dependent corrected field, not at a separately reset correction. The claim concerns this exact-subflow method; no assertion is made for approximate subflow solvers or general coupled systems.

## Proof

**1. Exact continuous dissipation and attraction.** Along the ODE, \(\dot H=-\gamma x^2\le0\). Coercivity of \(V\) makes each energy sublevel compact, giving complete forward solutions. The largest invariant subset of \(\{x=0\}\) has \(V'(y)=0\), hence \(y=0\) by strict convexity and \(\omega\ne0\). LaSalle's invariance argument implies every continuous trajectory tends to \((0,0)\). Local Lyapunov stability follows from the strict minimum of \(H\).

**2. The nonlinear commutator cancels globally.** Write the dissipative and conservative vector fields as \(f_1=(-\gamma x,0)\) and \(f_2=(-\omega V'(y),\omega x)\). For the Lie bracket \([f,g]=Dg\,f-Df\,g\), direct differentiation gives
\[
[f_1,f_2]=(-\gamma\omega V'(y),-\gamma\omega x),\qquad
[f_1,[f_1,f_2]]=\gamma^2 f_2.
\]
Consequently the source's corrected conservative field is exactly
\[
\widehat f_2=\Bigl(1-\frac{\gamma^2h^2}{72}\Bigr)f_2
\]
for **every** admissible nonlinear potential, not only after linearization. At the unique positive zero \(h_*=6\sqrt2/\gamma\), both corrected conservative half-flows equal the identity. The three dissipative stages then compose to the full flow of \(f_1\) over time \(h_*\), proving \(\Phi_{h_*}(x,y)=(e^{-\gamma h_*}x,y)\) and the fixed-line and convergence statements.

**3. One-step detuning.** Let \(C_s\) be the exact flow of \(F=(-V'(y),x)\) for signed duration \(s\). Write \(D_t(x,y)=(e^{-\gamma t}x,y)\), \(a(h)=1-\gamma^2h^2/72\), and \(s(h)=\omega h a(h)/2\). The 5C map is
\[
\Phi_h=D_{h/6}\circ C_{s(h)}\circ D_{2h/3}\circ C_{s(h)}\circ D_{h/6}.
\]
For fixed \(y_0\), Taylor expansion of the exact conservative flow gives \(C_s(0,y_0)=(-sV'(y_0)+O(s^3),\ y_0-s^2V'(y_0)/2+O(s^3))\). Applying the middle damping and the second conservative subflow yields
\[
\pi_y\Phi_h(0,y_0)-y_0
=-\bigl(1+e^{-2\gamma h/3}\bigr)s(h)^2V'(y_0)+O(|s(h)|^3).
\]
Since \(s(h_*)=0\) and \(s'(h_*)=-\omega\), and \(e^{-2\gamma h_*/3}=e^{-4\sqrt2}\), the asserted quadratic expansion follows. The constants in the remainder may depend on the fixed \(y_0,V,\gamma,\omega\).

**4. Sharp slow multiplier.** The Jacobian at the origin is the exact 5C map for the linearized conservative generator \(F_\kappa=\left(\begin{smallmatrix}0&-\kappa\\1&0\end{smallmatrix}\right)\). Put \(u=e^{-\gamma h/6}\) and \(\phi=\sqrt\kappa\,s(h)\). Its determinant is \(u^6=e^{-\gamma h}\), while direct multiplication of the two oscillatory half-flows and three damping stages gives
\[
\operatorname{tr}D\Phi_h(0,0)
=(1+u^6)\cos^2\phi-(u^2+u^4)\sin^2\phi.
\]
At \(h=h_*\), the simple eigenvalues are \(1\) and \(u_*^6=e^{-6\sqrt2}\), with \(u_*=e^{-\sqrt2}\). The trace changes by \(-(1+u_*^2)(1+u_*^4)\phi^2+O(\phi^4)\) relative to \(1+u^6\) at fixed \(h\). Implicit differentiation of the characteristic polynomial at its simple root \(1\) therefore gives
\[
\lambda_{\mathrm{slow}}(h)=1-
\frac{(1+u_*^2)(1+u_*^4)}{1-u_*^6}\,\kappa\omega^2(h-h_*)^2
+O(|h-h_*|^3).
\]
The other eigenvalue remains near \(e^{-6\sqrt2}<1\); hence for all sufficiently small nonzero detunings, the slow root is positive and dominates the spectral radius. This proves the final formula and its positive, sharp coefficient.

## Verification

The standalone `verify.py` reproduces the nested commutator symbolically with a formal arbitrary potential, verifies the correction zero and its detuning derivative, reconstructs the exact linearized trace identity and slow-root coefficient, and checks the predicted near-step behavior using high-accuracy numerical integration for the strictly convex quartic example \(V(y)=y^2/2+y^4/4\). Execute `python verify.py` after installing the packages listed in `requirements.txt`. Numerical comparisons are diagnostics, not substitutes for the exact proof above.

## Relationship to prior work

Mönch and Marheineke (2026) introduce the nonlinear extension of the 5C commutator method, including exactly the conservative correction and the damped-momentum separable-Hamiltonian class used here. Their full article analyzes dissipation inequalities and numerical convergence, not a nonzero-step continuum of spurious fixed points or the exact quadratic slow-mode multiplier. Mönch and Marheineke (2024) derive the linear force-gradient ancestor and its energy preservation; their linear result alone does not establish the potential-independent nonlinear fixed-line law and near-step relaxation coefficient. The derivation here uses both constructions as prior art, without claiming to introduce the numerical method, commutator identity, or Lyapunov principle.

## Limitations

The exceptional step is generally much larger than the small-step range in which fourth-order accuracy is useful. The local slow-eigenvalue estimate does not assert a global convergence rate for the nonlinear iteration away from the exact freezing step. Other isolated resonances may exist for special potentials or parameters; their classification is not claimed. No external independent audit or exhaustive historical-priority proof is claimed.

## References

1. M. Mönch and N. Marheineke, *Energy-Associated Splitting Schemes for Closed Nonlinear Port-Hamiltonian Systems*, Proceedings in Applied Mathematics and Mechanics 26 (2026), e70116; first published 2026-04-10. https://doi.org/10.1002/pamm.70116
2. M. Mönch and N. Marheineke, *Fourth-order force-gradient splitting for linear port-Hamiltonian systems*, Proceedings in Applied Mathematics and Mechanics 24 (2024), e202400132; first published 2024-10-07. https://doi.org/10.1002/pamm.202400132
3. E. Hairer, C. Lubich and G. Wanner, *Geometric Numerical Integration*, 2nd edition (2006), for standard splitting and geometric-integration background.
