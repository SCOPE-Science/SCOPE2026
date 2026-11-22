# Sharp half-filling entropy barrier in active-exclusion hydrodynamics

## Finding
For the dimensionless one-dimensional density–polarization equations of the interacting active exclusion lattice gas, an explicit strictly convex local entropy exists throughout the open low-density region \(0\le\rho<1/2\). It yields an **exact, activity-independent nonlinear dissipation identity** and an exponential relaxation bound for every smooth periodic trajectory that remains uniformly below half filling. More decisively, **no nonconstant smooth periodic steady or traveling-wave profile can be confined to \(\rho\le1/2\) everywhere**, at any positive activity. The threshold is sharp for local convex symmetrization: at a homogeneous unpolarized state of density \(\rho\ge1/2\), no twice-differentiable entropy whose Hessian is positive definite can symmetrize the advective flux.

## Assumptions and scope
Let \(L>0\), \(\mathrm{Pe}>0\), and let \(\rho,m\in C^{1,2}([0,T]\times\mathbb T_L)\) be real-valued classical solutions (with any extra regularity needed to justify the displayed identities) of
\[
\partial_t\rho=\partial_{xx}\rho-\mathrm{Pe}\,\partial_x[m(1-\rho)],\qquad
\partial_t m=\partial_{xx}m-\mathrm{Pe}\,\partial_x[\rho(1-\rho)]-2m.
\]
Here \(\mathbb T_L=\mathbb R/L\mathbb Z\). The physical occupancy domain is \(0\le\rho<1\) and \(|m|\le\rho\); the algebraic identities hold whenever \(\rho<1\). Define the conserved spatial mean \(\bar\rho=L^{-1}\int_{\mathbb T_L}\rho\,dx\). The exponential estimate assumes a genuinely uniform, **trajectory-wide** bound \(0\le\rho(x,t)\le R<1/2\), not just a low initial mean or low initial maximum. No assertion is made that this bound is dynamically invariant for arbitrary data and activity.

Set
\[
f(s)=s^2-(1-s)\log(1-s)-s,\quad
h(\rho,m)=f(\rho)+\tfrac12m^2,\quad
q(\rho,m)=m(1-\rho)[2\rho+\log(1-\rho)].
\]
Then \(h_{\rho\rho}=(1-2\rho)/(1-\rho)\), \(h_{mm}=1\), and \(h_{\rho m}=0\).

## Proof
**1. Exact local entropy pair.** For the advective flux
\[
F(\rho,m)=\binom{m(1-\rho)}{\rho(1-\rho)},\quad
A=DF=\begin{pmatrix}-m&1-\rho\\1-2\rho&0\end{pmatrix},
\]
put \(H=D^2h=\operatorname{diag}((1-2\rho)/(1-\rho),1)\). Direct differentiation gives \(HA=A^\mathsf TH\) and \(\nabla q=A^\mathsf T\nabla h\). Therefore the chain rule and integration by parts give the pointwise balance
\[
\partial_t h+\mathrm{Pe}\,\partial_x q
=\partial_x\bigl(h_\rho\,\partial_x\rho+h_m\,\partial_x m\bigr)
-\frac{1-2\rho}{1-\rho}|\partial_x\rho|^2
-|\partial_xm|^2-2m^2.
\tag{1}
\]
Thus, on every periodic classical solution with \(\rho<1\), the entropy functional \(\mathcal H=\int_{\mathbb T_L}h\,dx\) satisfies the exact identity
\[
\frac{d\mathcal H}{dt}=-\int_{\mathbb T_L}
\left(\frac{1-2\rho}{1-\rho}|\partial_x\rho|^2+|\partial_xm|^2+2m^2\right)dx.
\tag{2}
\]
The disappearance of \(\mathrm{Pe}\) in (2) is exact, not a small-activity approximation. The right side need not be negative at high density.

**2. Convexity, nonlinear decay, and pattern barrier.** For \(0\le\rho\le R<1/2\), define \(\alpha_R=(1-2R)/(1-R)>0\). Then \(\alpha_R\le f''(\rho)\le1\). The nonnegative relative entropy
\[
\mathcal E(t)=\int_{\mathbb T_L}
\left[f(\rho)-f(\bar\rho)-f'(\bar\rho)(\rho-\bar\rho)+\frac{m^2}{2}\right]dx
\]
obeys \(\frac{d\mathcal E}{dt}=\frac{d\mathcal H}{dt}\), since \(\bar\rho\) is conserved. Uniform convexity implies
\[
\frac{\alpha_R}{2}\|\rho-\bar\rho\|_2^2+\frac12\|m\|_2^2
\le\mathcal E\le\frac12\|\rho-\bar\rho\|_2^2+\frac12\|m\|_2^2.
\]
Using the sharp periodic Poincaré inequality \(\|\partial_x\rho\|_2^2\ge(2\pi/L)^2\|\rho-\bar\rho\|_2^2\) in (2) yields
\[
\boxed{\mathcal E(t)\le\mathcal E(0)\exp[-\Lambda_Rt],\qquad
\Lambda_R=\min\{2\alpha_R(2\pi/L)^2,\ 4\}.}
\tag{3}
\]
This bound applies throughout any interval over which the stated uniform cap holds.

Now suppose a smooth periodic stationary or traveling-wave solution remains pointwise in \(0\le\rho\le1/2\), with \(m\) periodic in space and, for a traveling wave, translated at constant speed. Its spatial integral \(\mathcal H\) is constant. Identity (2) forces \(m=0\) and \(\partial_x\rho=0\) wherever \(\rho<1/2\). At points where \(\rho=1/2\), differentiability and the upper bound force \(\partial_x\rho=0\) as well. Hence \(\rho\) is constant. Therefore every genuinely spatially inhomogeneous smooth stationary or traveling-wave profile must satisfy \(\max_x\rho(x)>1/2\). The same reasoning excludes nonconstant time-periodic solutions whose entire trajectory stays at or below half filling.

**3. Sharp convex-symmetrization obstruction.** At a homogeneous unpolarized state \((\rho_*,m_*)=(\rho_*,0)\),
\[
A_* =\begin{pmatrix}0&1-\rho_*\\1-2\rho_*&0\end{pmatrix},
\qquad\lambda_{\pm}(A_*)=\pm\sqrt{(1-\rho_*)(1-2\rho_*)}.
\]
For \(1/2<\rho_*<1\), these eigenvalues are nonreal. At \(\rho_*=1/2\), the matrix is nonzero nilpotent, hence non-diagonalizable. A strictly convex \(C^2\) entropy–flux pair in a neighborhood of such a state would give a positive-definite Hessian \(H_*\) with \(H_*A_*=A_*^\mathsf TH_*\), making \(A_*\) similar to a real symmetric matrix. Neither spectral case permits this. Conversely the explicit Hessian above is positive definite for every \(\rho_*<1/2\). The half-filling frontier is therefore sharp for this form of local convex entropy symmetrization. Within the subclass \(h=f(\rho)+c m^2/2\) with constant \(c>0\), the symmetry equation uniquely forces \(f''(\rho)=c(1-2\rho)/(1-\rho)\), up to affine additions.

## Verification
Run `python CHECKER.py` with Python, SymPy and NumPy installed. The code verifies the entropy Hessian/flux identity symbolically, the half-filling nilpotent matrix, uniqueness within the stated quadratic-polarization subclass, and the dissipation and decay inequalities against an independently assembled Fourier-spectral PDE right-hand side at several admissible trigonometric profiles and activity strengths. The checker yields 83 passed symbolic and numerical assertion groups. All universal and infinite-dimensional conclusions are proved by the analytic identities and Poincaré inequality, not by the finite-grid tests.

## Relationship to prior work
Kourbane-Houssene, Erignoux, Bodineau and Tailleur (2018) derive the exact microscopic-to-hydrodynamic equations and the **linear** spinodal criterion \(\mathrm{Pe}^2(1-\rho_0)(2\rho_0-1)>2\). The same paper also computes binodals for a flat stationary phase interface using equations (8)–(11). The linear criterion already implies no linear instability around homogeneous means at or below half filling; the specific interface construction is not an exhaustive classification of arbitrary periodic stationary or traveling profiles. The statement here is different: it gives an explicit **nonlinear** entropy identity, uniform relaxation conditional on a pointwise low-density cap, a nonexistence theorem for **all** sub-half-filling stationary and traveling profiles, and a sharp no-positive-Hessian theorem at and above half filling. Agranov, Ro, Kafri and Lecomte (2021) construct only a Gaussian-order fluctuation quasi-potential, which is not an exact deterministic nonlinear entropy. Agranov, Cates and Jack (2022) analyze stochastic/informatic entropy production and its large deviations in the same active lattice gas; that quantity is not the deterministic Lyapunov entropy \(h\) used here. General symmetrizable-system entropy techniques are standard antecedents; only their explicit sharp application and resulting nonlinear pattern barrier are asserted as the addition.

## Limitations
The PDE and its hydrodynamic interpretation are prior work. The density cap in (3) is **not** proved invariant from arbitrary low-density initial data; no unconditional global-in-time relaxation statement is made. A low **mean** density does not rule out localized portions exceeding half filling. The obstruction concerns strictly convex \(C^2\) local entropy-flux pairs near homogeneous unpolarized states, not every possible nonlocal functional or weighted stability method. The result neither locates the actual binodal/spinodal at high density nor proves a large-system stochastic microscopic theorem. Publication priority could depend on implicit coverage in general entropy/symmetrizer theory or less-visible active-matter literature; no independent review has occurred.

## References
1. M. Kourbane-Houssene, C. Erignoux, T. Bodineau and J. Tailleur, *Exact Hydrodynamic Description of Active Lattice Gases* (first arXiv public date 2018-01-26), https://arxiv.org/abs/1801.08952.
2. T. Agranov, S. Ro, Y. Kafri and V. Lecomte, *Exact fluctuating hydrodynamics of active lattice gases – Typical fluctuations* (first arXiv public date 2021-04-29), https://arxiv.org/abs/2104.14650.
3. T. Agranov, M. E. Cates and R. L. Jack, *Entropy production and its large deviations in an active lattice gas* (first arXiv public date 2022-09-07), https://arxiv.org/abs/2209.03000; DOI: 10.1088/1742-5468/aca0eb.
