# Sharp SSPRK(3,3) CFL for piecewise-constant sparse-grid DG

## Result

Consider the periodic constant-coefficient transport problem discretized in space by the standard piecewise-constant total-level sparse-grid upwind discontinuous Galerkin method of Huang (2026). Let
\[
B_{\boldsymbol c}=\sum_{\ell=1}^d c_\ell P_{\mathcal S_N}A_\ell,
\qquad
m=\max_\ell |c_\ell|>0,
\qquad
\nu=\frac{\Delta t}{h},
\]
with the directional upwind convention used for the signs of the velocities. Huang proves for forward Euler that, after setting
\[
H=I-\frac1m B_{\boldsymbol c},
\]
one has \(\|H\|_2\le 1\), while both \(+1\) and \(-1\) are eigenvalues of \(H\). The \(+1\) mode is constant and the \(-1\) mode is a finest-level alternating mode in a direction attaining the speed \(m\). Huang's Remark 3.11 extends the forward-Euler estimate to SSP Runge--Kutta methods through the SSP coefficient but leaves the sharpness of that higher-order condition open.

For any Runge--Kutta stability polynomial \(R\), define \(\mu=m\nu=m\Delta t/h\). The fully discrete amplification operator satisfies the general two-sided estimate
\[
\boxed{
\max\{1,|R(-2\mu)|\}
\;\le\;
\|R(-\nu B_{\boldsymbol c})\|_2
\;\le\;
\max_{|z+\mu|\le\mu}|R(z)|.
}
\]
Indeed,
\[
R(-\nu B_{\boldsymbol c})=R\bigl(\mu(H-I)\bigr).
\]
The upper bound is von Neumann's inequality applied to the contraction \(H\) and the polynomial \(p(w)=R(\mu(w-1))\). The two lower bounds come from the eigenvalues \(+1\) and \(-1\) of \(H\), which map to the scalar arguments \(0\) and \(-2\mu\), respectively.

For the standard three-stage third-order SSP method SSPRK(3,3),
\[
R_3(z)=1+z+\frac{z^2}{2}+\frac{z^3}{6}.
\]
Let \(\mu_*\) be the unique positive root of
\[
\boxed{2\mu^3-3\mu^2+3\mu-3=0.}
\]
Numerically,
\[
\boxed{\mu_*=1.256372663309164\ldots.}
\]
Then the sparse-grid DG + SSPRK(3,3) scheme is \(L^2\)-stable at every step if and only if
\[
\boxed{
\Delta t\le \mu_*\frac{h}{\max_\ell |c_\ell|}.
}
\]
Thus the exact SSPRK(3,3) CFL ceiling is about \(25.6373\%\) larger than the SSP-coefficient bound \(\Delta t\le h/m\), since SSPRK(3,3) has SSP coefficient one.

## Proof of the SSPRK(3,3) disk bound

It remains only to show that the entire origin-tangent disk
\[
D_\mu=\{z\in\mathbb C:|z+\mu|\le\mu\}
\]
lies in the scalar stability region of \(R_3\) exactly for \(0\le\mu\le\mu_*\). By the maximum-modulus principle it is enough to take
\[
z=\mu(w-1),\qquad |w|=1.
\]
Set
\[
x=1-\operatorname{Re}w\in[0,2],\qquad y=x/2\in[0,1].
\]
Direct expansion gives
\[
1-|R_3(\mu(w-1))|^2
=\frac{\mu x}{9}F_\mu(x),
\]
where
\[
F_\mu(x)
=18+3\mu(\mu^2-6)x
+2\mu^2(6-6\mu+3\mu^2-\mu^3)x^2.
\]
In the degree-two Bernstein basis on \(y\in[0,1]\),
\[
F_\mu(2y)
=b_0(1-y)^2+2b_1y(1-y)+b_2y^2,
\]
with
\[
b_0=18,
\]
\[
b_1=3(6-6\mu+\mu^3),
\]
\[
b_2=2(2\mu^2-3\mu+3)(3-3\mu+3\mu^2-2\mu^3).
\]
The cubic
\[
P(\mu)=3-3\mu+3\mu^2-2\mu^3
\]
is strictly decreasing on \([0,\infty)\), because
\[
P'(\mu)=-3(2\mu^2-2\mu+1)<0.
\]
Its unique positive zero is \(\mu_*\), and \(1<\mu_*<4/3\). Therefore \(P(\mu)\ge0\) for \(0\le\mu\le\mu_*\), while \(2\mu^2-3\mu+3>0\) for all real \(\mu\). Also, \(6-6\mu+\mu^3\) is decreasing on \([0,4/3]\) and equals \(10/27>0\) at \(4/3\). Hence all three Bernstein coefficients are nonnegative on \([0,\mu_*]\). It follows that \(F_\mu(x)\ge0\) for every \(x\in[0,2]\), and consequently
\[
\max_{z\in D_\mu}|R_3(z)|\le1
\qquad(0\le\mu\le\mu_*).
\]
Von Neumann's inequality now yields \(\|R_3(-\nu B_{\boldsymbol c})\|_2\le1\). The constant mode gives equality of the norm with one.

For necessity, the alternating eigenmode gives amplification \(R_3(-2\mu)\), and
\[
R_3(-2\mu)+1=\frac23P(\mu).
\]
Thus for every \(\mu>\mu_*\), \(R_3(-2\mu)<-1\), so that mode is amplified in \(L^2\). This proves the sharp threshold.

A closed radical form is available if desired. With \(a=(4+\sqrt{17})^{1/3}\),
\[
\mu_*=\frac12+\frac a2-\frac1{2a}.
\]
The associated negative-real stability endpoint is
\[
-2\mu_*=-2.512745326618329\ldots.
\]

## Relation to prior work

Huang's arXiv:2609.17312v1 proves the sharp forward-Euler condition and the contraction structure used above. Remark 3.11 gives the SSP sufficient condition but explicitly states that its sharpness is not guaranteed. The present result resolves that issue for SSPRK(3,3), in every spatial dimension covered by the standard total-level sparse-grid construction.

The Runge--Kutta stability-disk constant itself is not claimed as new. Jeltsch--Nevanlinna (1978) and Dahlquist--Jeltsch (1979; reprinted 2008) studied largest origin-tangent disks contained in explicit Runge--Kutta stability regions; Dahlquist--Jeltsch explicitly note a radius about \(1.25\) for third-order formulas. The new point here is the exact reduction of Huang's nonnormal sparse-grid DG operator to such a disk through the contraction \(H\), together with the alternating mode that makes the disk endpoint a matching necessity. A literature search did not locate this SSPRK(3,3) sharp CFL statement for the sparse-grid DG discretization.

## Limitations

The result applies to the linear, constant-coefficient, periodic transport model; the standard piecewise-constant total-level sparse-grid upwind DG space; exact arithmetic; and the \(L^2\) norm. It does not establish the same threshold for higher polynomial degree, nonlinear conservation laws, variable coefficients, limiters, adaptive/downward-closed index sets in which Huang's contraction may have a different sharp constant, or perturbed/non-Haar discretizations. The argument uses only the stability polynomial, so it concerns the one-step solution norm and does not address internal-stage amplification or floating-point roundoff. The originality claim is to the best of our knowledge, and the source preprint is very recent, so simultaneous or subsequent work is a material residual risk.

## Reproducibility

`artifacts/verify.py` symbolically verifies the Bernstein identity and root characterization, scans the stability disk, and constructs a finite two-dimensional Haar sparse-grid matrix to check the contraction-to-SSPRK3 implication numerically. `artifacts/verification.txt` records the executed output.

## References

1. J. Huang, *The sharp CFL condition of the piecewise constant sparse grid discontinuous Galerkin method for high-dimensional transport equations*, arXiv:2609.17312v1 (2026). https://arxiv.org/abs/2609.17312
2. S. Gottlieb, C.-W. Shu, E. Tadmor, *Strong Stability-Preserving High-Order Time Discretization Methods*, SIAM Review 43 (2001), 89--112. https://doi.org/10.1137/S003614450036757X
3. R. Jeltsch, O. Nevanlinna, *Largest disk of stability of explicit Runge--Kutta methods*, BIT 18 (1978), 500--502. https://doi.org/10.1007/BF01932030
4. G. Dahlquist, R. Jeltsch, *Generalized disks of contractivity for explicit and implicit Runge--Kutta methods*, TRITA-NA-7906 (1979), reprint ETH Research Report 2008-20. https://www.sam.math.ethz.ch/sam_reports/reports_final/reports2008/2008-20.pdf
