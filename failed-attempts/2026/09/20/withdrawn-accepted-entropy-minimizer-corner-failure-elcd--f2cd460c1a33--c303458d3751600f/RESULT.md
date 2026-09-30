# Exact entropy minimizer and normalization obstruction for ELCD interface states

## Statement

Consider the mathematical entropy used for the ideal-gas Euler equations in Chu--Herty--Kurganov, *Entropy-Based Local Characteristic Decomposition* (arXiv:2609.19838v1),
\[
\eta(\rho,p)=-\frac{\rho}{\gamma-1}\log\!\left(\frac{p}{\rho^\gamma}\right),\qquad \gamma>1,
\]
with positive density and pressure. The paper describes its entropy-based average state as the minimizer of \(\eta\) over the rectangle whose density and pressure coordinates are supplied by two neighboring states, and then reduces that minimization to the four corners using convexity.

That corner reduction is false in general. Let
\[
\rho_-:=\min(\rho_L,\rho_R),\quad \rho_+:=\max(\rho_L,\rho_R),\quad p_+:=\max(p_L,p_R).
\]
The exact minimizer over the full positive rectangle is
\[
\boxed{\widehat p=p_+,\qquad
\widehat\rho=\Pi_{[\rho_-,\rho_+]}\!\left(e^{-1}p_+^{1/\gamma}\right),}
\]
where \(\Pi\) denotes scalar projection. Hence the minimizer is strictly interior in density whenever
\[
\boxed{\rho_-<e^{-1}p_+^{1/\gamma}<\rho_+.}
\]
In this regime Algorithm 1 of arXiv:2609.19838v1 solves only the corner-restricted problem, not the stated continuous rectangle minimization.

There is also a separate invariance obstruction. For any constant \(c\),
\[
\eta_c(U)=\eta(U)+c\rho
\]
is an equally valid convex entropy for the Euler conservation law, because the added term is a linear conserved quantity and leaves the entropy Hessian unchanged. Yet the continuous rectangle minimizer becomes
\[
\boxed{\widehat\rho_c=
\Pi_{[\rho_-,\rho_+]}\!\left(e^{-1}p_+^{1/\gamma}e^{-(\gamma-1)c/\gamma}\right).}
\]
Thus the selected density can be moved arbitrarily across the interval by an entropy normalization that is immaterial to the conservation law and entropy inequality. The four-corner selector is likewise non-invariant: for two distinct candidate densities its ordering flips for a suitable \(c\).

## Proof of the rectangle minimizer

The Hessian in the \((\rho,p)\) variables is
\[
\nabla^2\eta=
\frac1{\gamma-1}
\begin{pmatrix}
\gamma/\rho & -1/p\\
-1/p & \rho/p^2
\end{pmatrix},
\]
whose determinant is \(1/((\gamma-1)p^2)>0\); hence \(\eta\) is strictly convex on the positive quadrant. Convexity, however, does not imply that a minimum over a polytope occurs at a vertex.

Since
\[
\frac{\partial\eta}{\partial p}=-\frac{\rho}{(\gamma-1)p}<0,
\]
any rectangle minimizer must satisfy \(p=p_+\). Along that edge,
\[
\frac{d}{d\rho}\eta(\rho,p_+)
=
\frac{\gamma\log\rho+\gamma-\log p_+}{\gamma-1},
\]
which vanishes uniquely at \(\rho_0=e^{-1}p_+^{1/\gamma}\). Strict convexity then gives the projected formula above.

When \(\rho_0\in(\rho_-,\rho_+)\), the entropy excess of any density \(\rho\) on the \(p_+\) edge is exactly
\[
\boxed{
\eta(\rho,p_+)-\eta(\rho_0,p_+)
=
\frac{\gamma}{\gamma-1}
\left[\rho\log\frac{\rho}{\rho_0}-\rho+\rho_0\right]>0
}
\]
for \(\rho\ne\rho_0\). Thus no corner can attain the continuous minimum in the interior regime.

## Affine-normalization dependence

If \((\eta,q)\) is an entropy pair for a conservation law, then adding a linear conserved quantity produces another entropy pair with the same convexity: for Euler, \(\eta_c=\eta+c\rho\) has entropy flux augmented by the corresponding mass flux. Its stationary density at fixed pressure obeys
\[
\frac{\gamma\log\rho+\gamma-\log p}{\gamma-1}+c=0,
\]
which yields the formula for \(\widehat\rho_c\). Given any target \(r>0\), choosing
\[
c=-\frac{\gamma}{\gamma-1}\log\!\left(\frac{r}{e^{-1}p_+^{1/\gamma}}\right)
\]
places the unconstrained minimizer exactly at \(r\).

The same ambiguity arises from the reference constant inside the logarithm. Replacing \(p/\rho^\gamma\) by \(p/(K\rho^\gamma)\) adds \((\log K)\rho/(\gamma-1)\), so a change of entropy reference can alter the selected ELCD state even though it does not alter the Euler equations or the entropy Hessian.

More generally, minimizing the raw value of a convex entropy over a finite candidate set is not invariant under the standard transformation \(\eta(U)\mapsto\eta(U)+a^TU+b\). For two distinct candidates \(U,V\), the difference of their transformed entropy values is affine in \(a\) and can be made to have either sign. An affine-invariant alternative would need to use a quantity such as a relative-entropy/Bregman divergence, for which the affine terms cancel, or explicitly fix a normalization as part of the numerical method.

## Source-benchmark instance

The paper's two-dimensional Riemann Configuration 3 contains neighboring states with
\[
(\rho,p)=(0.5323,0.3),\qquad (0.138,0.029),\qquad \gamma=1.4.
\]
For their rectangle,
\[
p_+=0.3,\qquad e^{-1}p_+^{1/\gamma}=0.155675654413166\ldots,
\]
which lies strictly between the two densities. The four-corner rule chooses \((\rho,p)=(0.138,0.3)\), with entropy
\[
-0.541211652324994\ldots,
\]
whereas the exact rectangle minimizer has entropy
\[
-0.544864790446082\ldots.
\]
The entropy excess is \(0.0036531381210876\ldots\). The corresponding sound speed \(\sqrt{\gamma p/\rho}\) is \(1.74455675198\ldots\) at the selected corner and \(1.64253372421\ldots\) at the true rectangle minimizer, a difference of about 6.21%. This does not by itself imply that the published numerical experiments are inaccurate; it shows that the implemented corner selector and the stated continuous entropy-minimization interpretation are genuinely different on a benchmark used in the paper.

## Consequences

1. The statement that convexity permits minimization over only the four corners is reversed: such a vertex principle is associated with maximizing a convex function, not minimizing it.
2. The full rectangle minimization has a closed form and therefore does not require a nonlinear solver.
3. The corner-restricted ELCD remains a well-defined numerical rule for the specific formula printed in the paper, but it is not intrinsic to the affine equivalence class of convex Euler entropies.
4. Any generalization of raw-entropy candidate selection to other hyperbolic systems inherits the same affine-normalization issue unless a normalization is fixed or an affine-invariant criterion is used.

## Limitations

This result does not claim that the corner-restricted ELCD produces worse numerical solutions than arithmetic or Roe averaging; the reported experiments may remain valid exactly as computed. It does not provide a convergence theorem for a corrected ELCD, nor does it identify an optimal normalization-invariant selection criterion. The affine-invariance observation is a standard fact about entropy pairs; the source-specific contribution is its consequence for the new ELCD rule, together with the exact rectangle minimizer, the sharp interior condition, the entropy-gap formula, and the benchmark-level discrepancy.

## References

- S. Chu, M. Herty, A. Kurganov, *Entropy-Based Local Characteristic Decomposition*, arXiv:2609.19838v1 (2026), especially Section 3 and Algorithm 1. https://arxiv.org/abs/2609.19838
- N. Leger, A. Vasseur, *Relative entropy and the stability of shocks and contact discontinuities for systems of conservation laws with non-BV perturbations*, Archive for Rational Mechanics and Analysis 201 (2011), 271--302; arXiv:1008.3113. https://arxiv.org/abs/1008.3113
