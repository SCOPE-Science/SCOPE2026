# A sharp \(120^\circ\) positivity barrier for lumped-mass triangular Crank–Nicolson heat steps

## Finding
For a single isosceles planar \(P_1\) finite-element triangle of vertices \((-1,0)\), \((1,0)\), and \((0,h)\), with \(0<h<1\), zero-flux Neumann conditions, unit diffusion, and nodal lumped mass, let \(B_\tau\), \(C_\tau\), and \(E_\tau\) denote respectively the backward-Euler, Crank–Nicolson, and exact semidiscrete heat updates of the same three nodal values at time \(\tau\ge0\). Put \(b=h^2\). Entrywise nonnegativity is classified exactly by
\[
B_\tau\ge0\ \Longleftrightarrow\ \tau=0\ \text{or}\ \tau\ge\frac{1-b}{3},
\]
\[
\boxed{\ C_\tau\ge0\ \Longleftrightarrow\ \tau=0\ \text{or}\ \left(b\ge\frac13\ \text{and}\ \frac{2(1-b)}3\le\tau\le\frac{4b}{3}\right).\ }
\]
For every \(b\in(0,1)\), the exact semigroup has one and only one positive recovery time \(\tau_*=2b z_b/3\), where \(z_b>0\) is the unique positive root of
\[
2+e^{-3z_b}=3e^{-bz_b}.
\]
Specifically, \(E_\tau\ge0\) exactly at \(\tau=0\) and at \(\tau\ge\tau_*\). The only entries that can be negative in backward Euler or in the exact semigroup are transfers between the two base vertices. For Crank–Nicolson the apex diagonal is additionally negative for \(\tau>4b/3\).

The triangle's apex angle is \(\Theta=2\arctan(1/h)\). Thus Crank–Nicolson has any nonzero positivity-preserving timestep precisely when \(\Theta\le120^\circ\); for \(\Theta=120^\circ\), the only positive timestep is \(\tau=4/9\), with update
\[
C_{4/9}=\begin{pmatrix}1/2&0&1/2\\0&1/2&1/2\\1/2&1/2&0\end{pmatrix}.
\]
The positivity intervals are exact, not merely sufficient timestep conditions.

## Assumptions and scope
The unknowns are the three nodal coefficients of continuous affine basis functions on exactly one nondegenerate isosceles triangle. Both the stiffness \(K\) and lumped mass \(M\) are assembled from that triangle; there are no other cells, forcing terms, reactions, or Dirichlet constraints. The standard row-sum lumping yields \(M=(h/3)I\). With \(\nabla\phi_1=(-1/2,-1/(2h))\), \(\nabla\phi_2=(1/2,-1/(2h))\), and \(\nabla\phi_3=(0,1/h)\), the stiffness is \(K_{ij}=h\nabla\phi_i\cdot\nabla\phi_j\). The three propagators are
\[
B_\tau=(M+\tau K)^{-1}M,\quad C_\tau=(M+\tau K/2)^{-1}(M-\tau K/2),\quad E_\tau=e^{-\tau M^{-1}K}.
\]
The symbols \(\ge0\) for matrices denote **entrywise** nonnegativity. No assertion of pointwise positivity at nonnodal positions or for multiple elements is made. Time and spatial coordinates are normalized exactly as above, so the numerical thresholds have units fixed by this geometry and diffusivity.

## Proof
**Exact diagonalization.** Set \(\alpha=3/(2b)\) and \(H=M^{-1}K\). Direct stiffness assembly gives \(H=\alpha(bP_A+3P_S)\), where the three mutually orthogonal idempotent projectors summing to the identity are
\[
P_0=\frac13\begin{pmatrix}1&1&1\\1&1&1\\1&1&1\end{pmatrix},\quad
P_A=\frac12\begin{pmatrix}1&-1&0\\-1&1&0\\0&0&0\end{pmatrix},\quad
P_S=\frac16\begin{pmatrix}1&1&-2\\1&1&-2\\-2&-2&4\end{pmatrix}.
\]
The eigenvalues of \(H\) are \(0,\alpha b,3\alpha\); they are all nonnegative. Every update is a linear combination of the above projectors and is symmetric with unit row sums. In particular all its entries are determined by two nontrivial scalar damping factors.

**Backward Euler.** Write \(x=\alpha\tau\) and \(a_x=(1+bx)^{-1}\), \(s_x=(1+3x)^{-1}\). Then \(B_\tau=P_0+a_xP_A+s_xP_S\), so
\[
(B_\tau)_{12}=\frac13-\frac{a_x}{2}+\frac{s_x}{6}
=\frac{x(2bx+b-1)}{2(1+bx)(1+3x)}.
\]
The apex-to-base entries are \((1-s_x)/3>0\) for positive steps. Every diagonal entry is positive because the matrix is positive definite. For positive \(x\), the base-to-base entry is nonnegative exactly if \(x\ge(1-b)/(2b)\), equivalently \(\tau\ge(1-b)/3\). At zero the update is the identity. This proves the first phase diagram.

**Crank–Nicolson.** Put \(y=\alpha\tau/2\); its scalar factors are \(a_y=(1-by)/(1+by)\) and \(s_y=(1-3y)/(1+3y)\), yielding
\[
(C_\tau)_{12}=\frac13-\frac{a_y}{2}+\frac{s_y}{6}
=\frac{y(2by+b-1)}{(1+by)(1+3y)},
\quad (C_\tau)_{33}=\frac{1-y}{1+3y}.
\]
Also \((C_\tau)_{13}=(C_\tau)_{23}=2y/(1+3y)>0\), and \((C_\tau)_{11}=(C_\tau)_{22}\) are strictly positive for \(0\le y\le1\) because \(a_y\ge0\) for \(0<b<1\) and \(s_y\ge-1/2\) there (in fact \((C_\tau)_{11}=1/3+a_y/2+s_y/6\ge1/4\)). Thus the necessary and sufficient sign inequalities at a positive step are \(y\ge(1-b)/(2b)\) and \(y\le1\). The interval is nonempty iff \(b\ge1/3\), and conversion back to physical time gives the claimed bounds. At \(b=1/3\), \(y=1\), projectors give the explicitly displayed matrix. The angle identity yields \(h\ge1/\sqrt3\) iff \(\Theta\le120^\circ\).

**Exact semigroup.** With \(z=\alpha\tau\), the spectral factors are \(a=e^{-bz}\) and \(s=e^{-3z}\). All diagonals and apex-to-base entries are strictly positive for \(z>0\). The remaining entry is
\[
(E_\tau)_{12}=\frac{2+e^{-3z}-3e^{-bz}}6=:g_b(z).
\]
We have \(g_b(0)=0\), \(g_b'(0)=(b-1)/2<0\), and \(g_b(z)\to1/3>0\). Moreover
\[
g_b'(z)=\frac{b e^{-bz}-e^{-3z}}2
\]
vanishes at the unique positive point \(z_m=\log(1/b)/(3-b)\), is strictly negative before it, and strictly positive afterward. Hence \(g_b\) has exactly one positive zero, with the asserted sign before and after the zero. The heat operator is symmetric, so all other signs are as stated.

## Verification
The self-contained Python 3 program `verify_triangle.py` assembles \(M\) and \(K\) from actual triangle gradients and uses exact rational Gaussian elimination to compute backward-Euler and Crank–Nicolson propagators. It independently compares them with the projector formulas and checks the sign classifications over 304 rational tests, including endpoints and rational near-threshold choices. It also checks the critical \(b=1/3\) matrix exactly in rational spectral variables and numerically samples the derivative-sign structure of the exact semigroup. The saved output is in `verify_output.txt`. Finite checks corroborate, but do not establish, the continuum quantified theorem; the above algebra is its proof. Reproduce from the package directory using `python verify_triangle.py`.

## Relationship to prior work
Larsson and Thomée (2018) study finite-element nonnegativity with Neumann and Robin boundary conditions; their accessible abstract establishes a broad Delaunay-type context but does not disclose an exact three-vertex isosceles Crank–Nicolson angle/timestep phase diagram. Full chapter text was unavailable for a conclusive exclusion. Jin, Lazarov, Thomée and Zhou (2015), especially their positivity theorems for lumped and consistent masses, establish broad qualitative sign criteria for diffusion/subdiffusion; they do not supply this exact triangular Crank–Nicolson boundary. Li and Huang (2012) give general sufficient discrete maximum-principle timestep restrictions, not the stated exact if-and-only-if family. Distinct published interpolation and diffusion records analyze one-dimensional consistent-mass grid thresholds or triangular nodal clipping energy, not this one-element mass-lumped Neumann update. The methodological ingredients (projector decomposition, Stieltjes conditions) are standard; the narrowly claimed contribution is this complete simultaneous time-stepping classification and the critical \(120^\circ\) boundary, not a general positivity principle.

## Limitations
The theorem concerns one triangle with Neumann conditions and nodal mass lumping, not general unstructured triangulations, Dirichlet elimination, consistent masses, nonisotropic diffusivity, nonuniform reaction terms, or other integrators. The semidiscrete cutoff is an implicit uniquely defined transcendental root, not an elementary formula. Nothing here establishes rounding-error robustness or an accuracy guarantee at positivity-safe steps. Some historical literature, notably the relevant 2018 Neumann chapter, could not be inspected in full; originality remains subject to independent publication-priority review. The mathematical verification is same-model only; no independent audit has been performed.

## References
- S. Larsson and V. Thomée, *On Nonnegativity Preservation in Finite Element Methods for the Heat Equation with Non-Dirichlet Boundary Conditions*, first online 2018-05-23, https://doi.org/10.1007/978-3-319-72456-0_35 .
- B. Jin, R. Lazarov, V. Thomée and Z. Zhou, *On Nonnegativity Preservation in Finite Element Methods for Subdiffusion Equations*, arXiv:1510.02825 (first posted 2015-10-09), https://arxiv.org/abs/1510.02825 .
- X. Li and W. Huang, *Maximum principle for the finite element solution of time dependent anisotropic diffusion problems*, arXiv:1209.5657 (2012), https://arxiv.org/abs/1209.5657 .
- Related exact one-dimensional consistent-mass backward-Euler analysis, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-sharp-backward-euler-positivity-on-arbitrary-graded-dirichlet-in--3b75689e09e8/RESULT.md .
- Related triangular clipping-energy analysis, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-sharp-obtuse-angle-amplification-law-for-nodal-finite-element-cl--a7adca9df150/RESULT.md .
- Related periodic consistent-mass Crank–Nicolson positivity analysis, https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-exact-periodic-finite-element-crank-nicolson-positivity-and-a-de--6d19e168e18a/RESULT.md .
