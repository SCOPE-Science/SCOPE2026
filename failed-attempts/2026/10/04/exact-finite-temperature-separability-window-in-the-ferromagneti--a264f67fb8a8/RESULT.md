# Exact finite-temperature separability window in the ferromagnetic XYZ dimer with DM coupling

## Finding

Consider the two-qubit XYZ Hamiltonian with a \(z\)-directed Dzyaloshinskii--Moriya interaction and no magnetic fields,
\[
H=\frac12\left[
J_x\,\sigma_x\otimes\sigma_x+
J_y\,\sigma_y\otimes\sigma_y+
J_z\,\sigma_z\otimes\sigma_z+
D\left(\sigma_x\otimes\sigma_y-\sigma_y\otimes\sigma_x\right)
\right],
\]
in the ferromagnetic ordering
\[
J_z<J_y<J_x<0.
\]
Write
\[
J_\pm=\frac{J_x\pm J_y}{2},\qquad
a=|J_-|,\qquad
g=|J_+|,\qquad
z=|J_z|,
\]
and let
\[
\tau=kT>0,\qquad
\nu(D)=\sqrt{g^2+D^2}.
\]
Then the thermal concurrence vanishes for exactly one closed interval
\[
\boxed{D_-(\tau)\le D\le D_+(\tau)}.
\]

The right endpoint is always
\[
\boxed{
D_+(\tau)=
\sqrt{
\left[
\tau\,\operatorname{arsinh}\!\left(e^{z/\tau}\cosh(a/\tau)\right)
\right]^2-g^2
}.
}
\]

For the left endpoint define
\[
u(\tau)=e^{z/\tau}\sinh(a/\tau).
\]
If
\[
u(\tau)\le\cosh(g/\tau),
\]
then the thermal state at \(D=0\) is already separable and
\[
\boxed{D_-(\tau)=0}.
\]
If instead
\[
u(\tau)>\cosh(g/\tau),
\]
then
\[
\boxed{
D_-(\tau)=
\sqrt{
\left[
\tau\,\operatorname{arcosh}u(\tau)
\right]^2-g^2
}.
}
\]

The zero-temperature level-crossing coupling reported by the source is
\[
D_c=\sqrt{(z+a)^2-g^2}.
\]
Whenever \(D_->0\),
\[
D_-<D_c<D_+.
\]
When \(D_-=0\), the right inequality remains strict. Moreover,
\[
\lim_{\tau\downarrow0}D_-(\tau)
=
\lim_{\tau\downarrow0}D_+(\tau)
=
D_c.
\]
Thus the single zero-concurrence point at zero temperature broadens into an exactly computable finite-temperature separability window.

## Assumptions and scope

The result uses the two-qubit Hamiltonian and concurrence convention of Gürkan and Pashaev, with no homogeneous or inhomogeneous magnetic field, \(D\ge0\), and
\[
J_z<J_y<J_x<0.
\]
The temperature variable is the thermal energy \(\tau=kT\), so no unit convention for Boltzmann's constant is needed.

The claim classifies only the zero-concurrence set as a function of \(D\) at fixed positive temperature. It does not address many-spin chains, external fields, other DM-vector orientations, other entanglement measures, or dynamical entanglement.

## Proof

In the computational basis the Hamiltonian splits into two \(2\times2\) blocks. The \(\{|00\rangle,|11\rangle\}\) block has center energy \(-z/2\) and off-diagonal magnitude \(a\). The \(\{|01\rangle,|10\rangle\}\) block has center energy \(z/2\) and off-diagonal magnitude
\[
\nu(D)=\sqrt{g^2+D^2}.
\]
Exponentiating the two blocks gives an \(X\)-state Gibbs density matrix. Up to the common partition function \(Z\),
\[
|\rho_{14}|=e^{z/(2\tau)}\sinh(a/\tau),
\qquad
\rho_{22}=\rho_{33}=e^{-z/(2\tau)}\cosh(\nu/\tau),
\]
and
\[
|\rho_{23}|=e^{-z/(2\tau)}\sinh(\nu/\tau),
\qquad
\rho_{11}=\rho_{44}=e^{z/(2\tau)}\cosh(a/\tau).
\]
The concurrence of an \(X\)-state is
\[
C=2\max\!\left\{
0,\,
|\rho_{14}|-\sqrt{\rho_{22}\rho_{33}},\,
|\rho_{23}|-\sqrt{\rho_{11}\rho_{44}}
\right\}.
\]
Consequently entanglement occurs on the low-\(D\) branch exactly when
\[
\cosh(\nu/\tau)
<
e^{z/\tau}\sinh(a/\tau),
\]
and on the high-\(D\) branch exactly when
\[
\sinh(\nu/\tau)
>
e^{z/\tau}\cosh(a/\tau).
\]

Because \(\nu(D)\) is strictly increasing for \(D>0\), the first inequality, when it holds at \(D=0\), has a unique terminal point
\[
\nu_-=
\tau\,\operatorname{arcosh}\!\left(e^{z/\tau}\sinh(a/\tau)\right),
\]
which gives \(D_-\). If it fails already at \(D=0\), there is no low-\(D\) entangled branch and \(D_-=0\).

The second inequality always has a unique onset
\[
\nu_+=
\tau\,\operatorname{arsinh}\!\left(e^{z/\tau}\cosh(a/\tau)\right),
\]
which gives \(D_+\).

The zero-temperature level crossing occurs at
\[
\nu_c=z+a.
\]
To locate the finite-temperature thresholds relative to it, note the exact identities
\[
\cosh\!\left(\frac{z+a}{\tau}\right)
-
e^{z/\tau}\sinh(a/\tau)
=
e^{-a/\tau}\cosh(z/\tau)>0
\]
and
\[
e^{z/\tau}\cosh(a/\tau)
-
\sinh\!\left(\frac{z+a}{\tau}\right)
=
e^{-a/\tau}\cosh(z/\tau)>0.
\]
Hence, whenever \(\nu_-\) exists above \(g\),
\[
\nu_-<z+a<\nu_+,
\]
and therefore
\[
D_-<D_c<D_+.
\]

Finally, as \(\tau\downarrow0\),
\[
\tau\,\operatorname{arcosh}\!\left(e^{z/\tau}\sinh(a/\tau)\right)\to z+a,
\]
and
\[
\tau\,\operatorname{arsinh}\!\left(e^{z/\tau}\cosh(a/\tau)\right)\to z+a,
\]
which proves collapse of the finite-temperature interval to \(D_c\).

## Verification

`verify_dm_window.py` independently evaluates the two concurrence candidates obtained from the exact Gibbs \(X\)-state and compares their zero set with the closed-form endpoints.

It tests the source benchmark
\[
(J_z,J_y,J_x)=(-3,-2,-1),
\]
together with a deterministic grid of additional ferromagnetic couplings and temperatures. It checks endpoint equations, strict placement around \(D_c\), concurrence signs immediately outside and inside the predicted interval, and the low-temperature convergence to \(D_c\).

The finite checks supplement the analytic proof; they are not used to infer the all-parameter theorem.

## Relationship to prior work

Gürkan and Pashaev define
\[
J_\pm=(J_x\pm J_y)/2
\]
and derive the thermal concurrence for the ferromagnetic XYZ dimer with DM coupling. Their refined treatment separates the undercritical and overcritical branches at the zero-temperature coupling
\[
\sqrt{D_c^2+J_+^2}=|J_z|+|J_-|.
\]
They state that at positive temperature the concurrence vanishes on an interval containing \(D_c\), that the interval grows with temperature, and illustrate it graphically. The inspected source does not give closed formulas for the two interval endpoints.

An earlier 2007 preprint by the same authors treats the ferromagnetic XYZ+DM case more coarsely and gives only the high-\(D\) concurrence condition. The later 2008/2010 treatment supplies the two branch formulas used here.

Targeted searches for the paper identifier, the ferromagnetic ordering, inverse-hyperbolic endpoint formulas, exact separability windows, and corrections did not locate the displayed all-temperature endpoint classification. Later DM-entanglement literature found in the searches concerns different spin models or many-spin systems rather than this exact two-qubit phase boundary.

## Limitations

The result is an exact consequence of the two-qubit thermal \(X\)-state and does not establish a thermodynamic phase transition for an infinite chain. The phrase “phase boundary” here refers only to the entangled-versus-separable regions of this finite thermal state.

The left endpoint has an unavoidable piecewise form because sufficiently high temperature already destroys entanglement at \(D=0\). The right endpoint remains finite for every positive temperature, while arbitrarily strong \(D\) eventually restores entanglement.

A residual literature risk remains because the endpoint equations are elementary inversions of published concurrence inequalities and may have appeared in unindexed notes or later work with different parameter notation.

## References

1. Z. N. Gürkan and O. K. Pashaev, “Two Qubit Entanglement in Magnetic Chains with DM Antisymmetric Anisotropic Exchange Interaction,” arXiv:0804.0710, first public 4 April 2008.
2. Z. N. Gürkan and O. K. Pashaev, “Entanglement in two qubit magnetic models with DM antisymmetric anisotropic exchange interaction,” *International Journal of Modern Physics B* 24 (2010), 943–965, DOI: 10.1142/S0217979210054579.
3. Z. N. Gürkan and O. K. Pashaev, “Two Qubit Entanglement in XYZ Magnetic Chain with DM Antisymmetric Anisotropic Exchange Interaction,” arXiv:0705.0679, first public 4 May 2007.
