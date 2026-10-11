# No finite inhomogeneity cutoff for thermal entanglement in the XXZ dimer

## Finding

Consider the two-qubit XXZ Hamiltonian
\[
H=\frac12\left[
J(\sigma_x\otimes\sigma_x+\sigma_y\otimes\sigma_y)
+J_z\sigma_z\otimes\sigma_z
+(B+b)\sigma_z\otimes I
+(B-b)I\otimes\sigma_z
\right],
\]
with
\[
J>0,\qquad J_z\ge0,\qquad T>0.
\]
Write
\[
\eta=\sqrt{J^2+b^2}.
\]
The Gibbs-state concurrence is
\[
\boxed{
C(T,b)=
\frac{2}{Z}
\left[
e^{J_z/(2T)}
\frac{J}{\eta}\sinh(\eta/T)
-e^{-J_z/(2T)}
\right]_+
}
\]
with
\[
Z=
2e^{-J_z/(2T)}\cosh(B/T)
+
2e^{J_z/(2T)}\cosh(\eta/T).
\]

Hence
\[
\boxed{
C(T,b)>0
\iff
\frac{J}{\eta}\sinh(\eta/T)>e^{-J_z/T}.
}
\]
The uniform field \(B\) affects the magnitude through \(Z\), but not the zero-versus-positive concurrence condition.

Because
\[
x\longmapsto\frac{\sinh x}{x}
\]
is strictly increasing for \(x>0\), the left-hand side is strictly increasing with \(|b|\). Therefore increasing field inhomogeneity can never destroy concurrence once it is present.

There are exactly three possibilities.

If
\[
\sinh(J/T)>e^{-J_z/T},
\]
then
\[
C(T,b)>0
\]
for every finite \(b\).

If
\[
\sinh(J/T)=e^{-J_z/T},
\]
then
\[
C(T,0)=0
\]
and
\[
C(T,b)>0
\]
for every \(b\ne0\).

If
\[
\sinh(J/T)<e^{-J_z/T},
\]
there is one and only one number \(b_*>0\) satisfying
\[
\frac{J}{\sqrt{J^2+b_*^2}}
\sinh\!\left(
\frac{\sqrt{J^2+b_*^2}}{T}
\right)
=
e^{-J_z/T}.
\]
In this case
\[
\boxed{
C(T,b)=0\quad\text{for}\quad |b|\le b_*,
}
\]
and
\[
\boxed{
C(T,b)>0\quad\text{for}\quad |b|>b_*.
}
\]
Whenever this activation threshold exists, it strictly decreases as \(J_z\) increases.

Finally, at fixed \(J,J_z,B,T\),
\[
\boxed{
\lim_{|b|\to\infty}\frac{|b|}{J}C(T,b)=1.
}
\]
Thus
\[
C(T,b)\sim\frac{J}{|b|}.
\]
The inhomogeneous field produces an algebraically small but strictly positive concurrence tail rather than a finite upper cutoff.

For the parameters used in the source's discussion of an alleged common critical inhomogeneity,
\[
J=1,\qquad B=0.8,\qquad T=0.6,
\]
the exact formula gives, at \(b=5\),
\[
C\approx0.1955468,\ 0.1958237,\ 0.1959890
\]
for
\[
J_z=0,\ 0.4,\ 0.9,
\]
respectively. All remain positive.

## Assumptions and scope

The Hamiltonian convention is the one used in the source. The result assumes the antiferromagnetic transverse coupling
\[
J>0
\]
and
\[
J_z\ge0.
\]
Boltzmann's constant is set to one.

The theorem concerns Wootters concurrence of the two-qubit Gibbs state. It classifies only zero versus positive concurrence and gives its large-inhomogeneity leading term.

The statement does not assert monotonicity of the concurrence magnitude in \(b\) at every parameter value. It asserts the stronger topological fact relevant to a “critical field”: once concurrence is positive, no larger finite \(|b|\) can make it vanish.

## Proof

The source diagonalizes the Hamiltonian with energy scale
\[
\eta=\sqrt{J^2+b^2}.
\]
Its Gibbs state has \(X\)-form. The two outer diagonal entries have geometric mean
\[
\frac{e^{-J_z/(2T)}}{Z},
\]
while the magnitude of the only potentially entangling off-diagonal entry is
\[
\frac{e^{J_z/(2T)}}{Z}
\frac{J}{\eta}\sinh(\eta/T).
\]
Wootters' formula for this \(X\)-state therefore gives
\[
C(T,b)=
\frac{2}{Z}
\left[
e^{J_z/(2T)}
\frac{J}{\eta}\sinh(\eta/T)
-e^{-J_z/(2T)}
\right]_+.
\]
This proves the exact positivity criterion.

Set
\[
g(\eta)=J\frac{\sinh(\eta/T)}{\eta}.
\]
For \(\eta>0\),
\[
g'(\eta)
=
\frac{J}{\eta^2}
\left[
\frac{\eta}{T}\cosh(\eta/T)-\sinh(\eta/T)
\right].
\]
The bracket is strictly positive because
\[
x\cosh x-\sinh x
\]
has derivative
\[
x\sinh x>0
\]
and vanishes at \(x=0\). Hence \(g\) is strictly increasing.

Since
\[
\eta=\sqrt{J^2+b^2}
\]
is strictly increasing with \(|b|\), the concurrence positivity condition is likewise monotone in \(|b|\). At \(b=0\), \(\eta=J\), so the sign of
\[
\sinh(J/T)-e^{-J_z/T}
\]
determines which of the three cases occurs. In the subthreshold case, continuity, strict monotonicity, and
\[
g(\eta)\to\infty
\]
as \(\eta\to\infty\) give one unique activation threshold.

For its \(J_z\)-dependence, the threshold equation is
\[
g(\eta_*)=e^{-J_z/T}.
\]
The right side strictly decreases in \(J_z\), while \(g\) strictly increases in \(\eta_*\). Therefore \(\eta_*\), and hence \(b_*\), strictly decreases with \(J_z\).

For the large-\(|b|\) asymptotic, the positive-part operation is eventually inactive. Since
\[
\eta\sim|b|,
\]
and
\[
\sinh(\eta/T)\sim\frac12e^{\eta/T},
\qquad
\cosh(\eta/T)\sim\frac12e^{\eta/T},
\]
the dominant terms in numerator and partition function give
\[
C(T,b)
\sim
\frac{J}{\eta}
\sim
\frac{J}{|b|}.
\]
This proves the reciprocal tail.

## Verification

`verify_xxz_inhomogeneity.py` reconstructs the \(4\times4\) Hamiltonian directly from Pauli matrices, forms the Gibbs state by spectral decomposition, and computes concurrence from the eigenvalues of the Wootters spin-flip product.

Across a deterministic parameter grid, it compares this direct matrix concurrence with the closed formula. It separately checks the unique lower activation threshold in a high-temperature example and verifies positivity at large inhomogeneity for the parameter values used in the source's plotted comparison.

The script also checks convergence of
\[
\frac{|b|}{J}C(T,b)
\]
to \(1\) at increasing \(|b|\).

The finite replay is supplementary. The all-parameter topology and asymptotic tail are proved analytically above.

## Relationship to prior work

Zhang and Li derive the same Gibbs \(X\)-state and concurrence formula. In their discussion of the inhomogeneous field, they state that concurrence decreases with \(b\) and reaches zero at a common critical value independent of \(J_z\) for the plotted choices
\[
J=1,\qquad B=0.8,\qquad T=0.6.
\]
The exact positivity condition above, derived directly from their thermal state, shows that this interpretation is not correct: no finite upper critical \(b\) exists.

Asoudeh and Karimipour earlier analyzed the isotropic two-spin Heisenberg model in an inhomogeneous field. They found that sufficiently strong inhomogeneity can create entanglement in parameter regimes where the homogeneous system is unentangled. Their exact isotropic formula is consistent with the activation mechanism derived here. The present claim is narrower in provenance but broader in the anisotropy parameter: it gives the complete zero-versus-positive topology for the XXZ Gibbs family of Zhang and Li, proves the \(J_z\)-dependence of the activation threshold, and supplies the universal reciprocal tail.

Wu and Zhou subsequently studied the anisotropic XXZ model under an inhomogeneous field. Accessible bibliographic material confirms that this is a closely related follow-up and therefore an important residual comparison risk. The full mathematical content of that article was not available for complete comparison here, so the originality claim is restricted to the exact statements above and records that access limitation.

Targeted searches using the source title, its “critical inhomogeneous magnetic field” statement, the threshold equation, and the reciprocal tail did not locate a published correction matching all of these conclusions.

## Limitations

The result assumes
\[
J>0,\qquad J_z\ge0.
\]
Other sign regimes can have different threshold structure and are not claimed.

The theorem classifies concurrence positivity, not monotonicity of the concurrence magnitude. The magnitude can vary nonmonotonically even though its positive set has the one-threshold form proved here.

A very closely related 2006 XXZ paper by Wu and Zhou could not be fully inspected. Its accessible abstract and bibliographic record do not establish coverage of the exact correction, activation topology, or reciprocal asymptotic, but this remains the principal originality risk.

The direct 2005 physics source does not carry an accessible MSC label. Subject ownership is supported by the mathematically indexed close XXZ inhomogeneous-field treatment, whose primary classification is \(81P68\).

## References

1. G.-F. Zhang and S.-S. Li, “Thermal entanglement in a two-qubit Heisenberg XXZ spin chain under an inhomogeneous magnetic field,” arXiv:quant-ph/0509009, first public 1 September 2005; *Physical Review A* 72 (2005), 034302, DOI: 10.1103/PhysRevA.72.034302.
2. M. Asoudeh and V. Karimipour, “Thermal entanglement of spins in an inhomogeneous magnetic field,” arXiv:quant-ph/0407073; *Physical Review A* 71 (2005), 022308, DOI: 10.1103/PhysRevA.71.022308.
3. K.-D. Wu and B. Zhou, “Thermal entanglement in the anisotropic XXZ model under an inhomogeneous magnetic field,” *International Journal of Modern Physics B* 20 (2006), DOI: 10.1142/S0217979206034583.
