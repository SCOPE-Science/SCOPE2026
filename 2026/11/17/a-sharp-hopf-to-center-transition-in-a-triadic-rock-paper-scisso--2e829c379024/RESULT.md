# A sharp Hopf-to-center transition in a triadic rock–paper–scissors replicator

## Finding
For the three-strategy, cyclic pairwise-plus-triadic replicator defined below, fix
\(1<\alpha\le 2\), \(0<\beta\le 1\), and
\(b>(2\alpha-\beta-1)/4\). Define
\[
D=3+2\alpha-\beta,\qquad C=1+b,\qquad
 a_*=\frac{1+4b+\beta-2\alpha}{D}.
\]
Then \(a_*>0\), and as \(a\) crosses \(a_*\), the symmetric interior equilibrium
\(u_*=(1/3,1/3,1/3)\) has a transverse imaginary-eigenvalue crossing.
In an oriented orthonormal simplex chart, its Hopf **radial cubic coefficient**
(normalized in the original time and with a near-identity change of state coordinates)
is exactly
\[
\boxed{\ell=\frac{(1+b)(1-\beta)}{2(3+2\alpha-\beta)}.}
\]
For every \(0<\beta<1\), \(\ell>0\), so the crossing is a nondegenerate **subcritical Hopf bifurcation**: for \(a>a_*\) sufficiently close to \(a_*\), a locally unique small **repelling** periodic orbit encloses the attracting equilibrium. The normal-form amplitude \(\rho\) obeys
\[
\rho^2=\frac{(3+2\alpha-\beta)^2}{9(1+b)(1-\beta)}(a-a_*)+O((a-a_*)^2).
\]
At the sharp admissible endpoint \(\beta=1\), the cubic coefficient vanishes and, more strongly, the *full nonlinear vector field at* \(a=a_*\) is reversible under exchange of the first two strategies. The symmetric equilibrium is a **nonlinear center**: every sufficiently close, nonstationary trajectory is a periodic orbit. Thus the endpoint is not a nondegenerate Hopf point, nor is this result merely a formal vanishing of one coefficient.

## Assumptions and scope
The state is \(u=(u_1,u_2,u_3)\) in the probability simplex \(u_i\ge0\), \(\sum_i u_i=1\). The exact Griffin–Wu payoff matrices are
\[
A=\begin{pmatrix}0&-C&a+1\\a+1&0&-C\\-C&a+1&0\end{pmatrix},
\qquad
B_1=\begin{pmatrix}
0&-C/2&(a+1)\beta/2\\
-C/2&-C&0\\
(a+1)\beta/2&0&(a+1)\alpha
\end{pmatrix}.
\]
Here \(B_2\) and \(B_3\) result by simultaneously rotating the rows and columns of \(B_1\) cyclically, sending strategy \(1\) to \(2\) and \(2\) to \(3\). In particular, the explicit three matrices in the accompanying checker fix this convention completely. Define the individual fitnesses and their population mean by
\[
f_i(u)=(Au)_i+u^{\mathsf T}B_i u,\qquad
\bar f(u)=\sum_{j=1}^3u_jf_j(u),
\qquad \dot u_i=u_i(f_i(u)-\bar f(u)).
\]
The simplex is invariant and \(u_*\) is an equilibrium. Parameters are held fixed except when varying \(a\) across the Hopf surface. The positive-\(a\) condition above keeps the crossing in the original source's \(a,b\ge0\) parameter sector. All attraction, periodicity and uniqueness statements are **local** near \(u_*\). No global orbit census, global bifurcation surface or stability beyond the local branch is claimed.

## Proof
**1. Orthonormal reduction.** Put
\[
X=\frac{u_1-u_2}{\sqrt2},\qquad
Y=\frac{u_1+u_2-2u_3}{\sqrt6},\qquad z=X+iY.
\]
The inverse coordinate formulas are \(u_1=1/3+X/\sqrt2+Y/\sqrt6\),
\(u_2=1/3-X/\sqrt2+Y/\sqrt6\), and \(u_3=1/3-2Y/\sqrt6\). Direct substitution in the **exact quartic** replicator field gives its linearization
\[
\begin{pmatrix}\dot X\\\dot Y\end{pmatrix}
=\begin{pmatrix}\mu&-\Omega\\\Omega&\mu\end{pmatrix}
\begin{pmatrix}X\\Y\end{pmatrix}+O(X^2+Y^2),
\quad \mu=-\frac{D(a-a_*)}{18},
\]
where
\[
\Omega=\frac{\sqrt3\,[2a\alpha+a\beta+3a+2\alpha+6b+\beta+9]}{18}.
\]
At \(a=a_*\), \(\mu=0\), the angular frequency is
\[
\omega=\frac{\sqrt3 C(10\alpha-\beta+15)}{9D}>0,
\]
and \(\partial_a\mu=-D/18<0\). Hence the crossing is transverse.

**2. Exact cyclic polynomial and the cubic coefficient.** The rotation by one strategy acts on \(z\) as multiplication by a primitive cube root of unity. Its equivariance restricts all degree-at-most-four terms at the crossing to precisely
\[
\dot z=i\omega z+Q\bar z^2+Rz^2\bar z+Sz^4+Tz\bar z^3,
\]
with the *exact* coefficients
\[
Q=\frac C{6D}\bigl[\sqrt2(8\alpha+\beta+15)+i\sqrt6(1-\beta)\bigr],
\]
\[
R=\frac C D\left[\frac{1-\beta}{2}-\frac{i\sqrt3(\alpha-\beta)}3\right],
\quad S=\frac C{4D}\bigl[2\sqrt2(\alpha-\beta)+i\sqrt6(1-\beta)\bigr],
\quad T=\bar S.
\]
Each identity is verified by exact expansion from the displayed payoff matrices in `check_hopf.py`.
To remove the nonresonant quadratic term, use
\(z=w+iQ\bar w^2/(3\omega)+O(|w|^3)\). The resulting resonant cubic coefficient is
\[
R-\frac{2i|Q|^2}{3\omega},
\]
so its **real part** is \(\ell=\Re R=C(1-\beta)/(2D)\).
Equivalently, the standard planar derivative formula in orthonormal coordinates has vanishing quadratic-correction numerator and yields
\[
\ell=\frac{F_{XXX}+F_{XYY}+G_{XXY}+G_{YYY}}{16}
\quad (F=\dot X,\ G=\dot Y)
\]
at the critical equilibrium. Thus no unknown normal-form correction changes the sign. For \(\beta<1\), the Hopf theorem and \(\mu<0\) when \(a>a_*\) give the repelling small cycle. Its radial balance \(\rho^2=-\mu/\ell+O(\mu^2)\) gives the displayed amplitude.

**3. Reversibility and a genuine center at the endpoint.** If \(\beta=1\), the formulas above show \(Q,S,T\in\mathbb R\), \(R\in i\mathbb R\), and \(\omega\in\mathbb R\). Consequently the *entire* quartic field obeys
\[
V(-\bar z)=\overline{V(z)}.
\]
This is exactly reversibility under \(\mathcal S(z)=-\bar z\), i.e. \((X,Y)\mapsto(-X,Y)\), which interchanges \(u_1\) and \(u_2\) and reverses time. It is not just a cubic-truncation symmetry.
The fixed line \(X=0\) is transverse to the flow near every sufficiently small point \((0,Y)\) with \(Y\ne0\): \(\dot X=-\omega Y+O(Y^2)\). For any small \(Y_0>0\), a solution starting at \((0,Y_0)\) remains close to the linear rotation for one half turn and intersects the same line transversely again at some \((0,Y_1)\), \(Y_1<0\). The bounded positive angular speed and \(\dot r=O(r^2)\) guarantee this uniformly for sufficiently small initial radii. Because the flow is reversible and *both intersection points are fixed by* \(\mathcal S\), reflecting the first flight in time yields the return flight and an exact periodic orbit. Every sufficiently small nonzero orbit meets such a transversal, establishing a full local period annulus. This proves the center statement without assuming an analytic first integral.

## Verification
Run `python check_hopf.py` with Python 3 and SymPy from the embedded files. It checks the four real Jacobian entries, five complete complex normal-form coefficients, the vanishing of the real quadratic Hopf correction, and **both** exact reversibility identities at the endpoint. It also checks positivity/degeneracy on 18 exact-rational parameter triples in the permitted region. Its successful output is:

```
TRIADIC_RPS_HOPF_EXACT_OK jacobian=4 complex_coefficients=5
TRIADIC_RPS_HOPF_EXACT_OK quadratic_correction=0 reversal=2
TRIADIC_RPS_HOPF_EXACT_OK endpoint_and_parameter_samples=18
```

The symbolic identities are asserted for arbitrary symbolic parameters; the 18 samples are ancillary. The inference from reversibility to a local period annulus is analytic and is not inferred from finite integration or numerical trajectories.

## Relationship to prior work
Griffin and Wu (2023, arXiv:2301.02518, first public version January 6, 2023) introduce **exactly these** pairwise and triadic payoff tensors, derive the Hopf surface, and numerically report a subcritical cycle. Neither their displayed local analysis nor their numerical construction gives the above analytic radial coefficient or identifies the reversible-center endpoint \(\beta=1\). The new content is the exact all-parameter cubic criticality sign and the center, not discovery of the Hopf surface or numerical evidence for unstable oscillations.

Griffin, Feng and Wu (2024, arXiv:2312.16722 / DOI 10.1088/1751-8121/ad3bf6) compute a first Lyapunov coefficient for a **four-dimensional travelling-wave reduction of a spatial model**, using a *different* pairwise payoff matrix and different triadic tensor slices. Their coefficient and attracting travelling waves do not imply the present two-dimensional coefficient or the endpoint reversibility. Classical symmetric/reversible-center and Hopf normal-form theory supplies the methods, not the model-specific identities.

## Limitations
The sharp change at \(\beta=1\) is established only on the positive-parameter Hopf surface and locally around the coexistence equilibrium. The theorem neither proves global coexistence nor classifies cycles far from that equilibrium. The formula uses a specifically normalized orthonormal chart and original physical time; other first-Lyapunov conventions rescale the coefficient but preserve its sign and zero set. The source comparison is limited to the identified primary treatments and accessible indexed literature; unindexed prior calculations are a residual publication-priority risk. No independent mathematical validation has been performed.

## References
- C. Griffin and R. Wu, *Higher Order Dynamics in the Replicator Equation Produce a Limit Cycle in Rock-Paper-Scissors*, arXiv:2301.02518 (first public version 2023-01-06), https://arxiv.org/abs/2301.02518; EPL 142 (2023), 33001, DOI 10.1209/0295-5075/accd93.
- C. Griffin, L. Feng and R. Wu, *Spatial Dynamics of Higher Order Rock-Paper-Scissors and Generalisations*, arXiv:2312.16722 (2023), J. Phys. A 57 (2024), 185701, https://doi.org/10.1088/1751-8121/ad3bf6.
- E. C. Zeeman, *Population dynamics from game theory*, in *Global Theory of Dynamical Systems*, Lecture Notes in Mathematics 819 (1980), 471–497 (classical planar matrix-replicator comparison).
