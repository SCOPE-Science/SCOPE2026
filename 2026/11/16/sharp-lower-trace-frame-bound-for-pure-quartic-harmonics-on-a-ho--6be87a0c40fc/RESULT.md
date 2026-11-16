# Sharp lower trace frame bound for pure quartic harmonics on a Hopf torus

## Finding
Let \(\mathcal H_4\) be the 25-dimensional complex eigenspace of degree-four scalar spherical harmonics on the unit three-sphere \(S^3\subset\mathbb C^2\), with probability-normalized round measure. For \(0<t<1\), put
\[
T_t=\{(\sqrt t e^{i\alpha},\sqrt{1-t}e^{i\beta}):\alpha,\beta\in\mathbb R/2\pi\mathbb Z\},
\]
with probability-normalized angular measure, and let \(R_t f=f|_{T_t}\). Denote by \(A(t)=\lambda_{\min}(R_t^*R_t)\) the **least** squared singular value, allowing zero when the restriction is singular.

**Theorem.** There exists a unique \(\tau\in(21/50,43/100)\) satisfying
\[
25\tau^3-48\tau^2+30\tau-6=0.
\]
The sharp globally optimal least frame eigenvalue is
\[
\boxed{\sup_{0<t<1} A(t)=5\tau^4=0.163608701688480\ldots.}
\]
Equality holds precisely at \(t=\tau\) and \(t=1-\tau\). At either optimum the 25-dimensional restriction map is injective, and the smallest eigenvalue has complex multiplicity exactly six. At \(t=\tau\) its eigenspace is spanned by the two Fourier modes \((m,n)=(\pm4,0)\) and the four modes \((m,n)=(\pm1,\pm1)\), with independently chosen signs.

The exact full singular spectrum, at any radius, is as follows. For integers \(a,b\ge0\) with \(a+b\in\{0,2,4\}\) and \(j=(4-a-b)/2\), define
\[
\lambda_{a,b}(t)=5\frac{j!(j+a+b)!}{(j+a)!(j+b)!}\,t^a(1-t)^b\bigl[P_j^{(b,a)}(2t-1)\bigr]^2.
\]
This value occurs for every Fourier weight \((m,n)\) with \((|m|,|n|)=(a,b)\), so its multiplicity is \((2-\mathbf1_{a=0})(2-\mathbf1_{b=0})\) before accidental eigenvalue collisions. In particular all 25 eigenvalues are accounted for. The nine distinct weight sectors are the five \(5\binom4a t^a(1-t)^{4-a}\) for \(a+b=4\); the three
\[
5t^2(4t-3)^2,\qquad30t(1-t)(2t-1)^2,\qquad5(1-t)^2(4t-1)^2
\]
for \((a,b)=(2,0),(1,1),(0,2)\); and \(\frac54(3(2t-1)^2-1)^2\) for \((a,b)=(0,0)\).

## Assumptions and scope
All spaces are complex Hilbert spaces. Ambient and torus surface measures both have mass one; the torus is endowed with the **normalized parameter measure** \(d\alpha\,d\beta/(2\pi)^2\), which equals its normalized induced Riemannian measure since its area element is constant. Only pure degree four, not the band of all degrees at most four, is included. The sharp optimization ranges over the one-parameter Hopf-torus family \(0<t<1\), with no assertion for other embedded observation surfaces. The positive eigenvalues are squared singular values with respect to the two probability norms. The dimension of \(\mathcal H_4\) is \(25\).

## Proof
**1. Hopf harmonic diagonalization.** Write \(z_1=\cos\theta\,e^{i\alpha}\), \(z_2=\sin\theta\,e^{i\beta}\) and \(t=\cos^2\theta\). The uniform measure on \(S^3\) becomes \(dt\,d\alpha\,d\beta/(2\pi)^2\), with \(0<t<1\) (orientation is irrelevant). Let \(m,n\in\mathbb Z\), \(a=|m|\), \(b=|n|\), \(s=a+b\). For \(s\le4\) and \(4-s\) even set \(j=(4-s)/2\). The classical separated scalar Hopf harmonic is
\[
\Phi_{m,n,j}=C_{a,b,j}\,t^{a/2}(1-t)^{b/2}P_j^{(b,a)}(2t-1)e^{i(m\alpha+n\beta)},
\quad C_{a,b,j}^2=\frac{5j!(j+a+b)!}{(j+a)!(j+b)!}.
\]
Jacobi orthogonality gives ambient norm one. Substitution into the Hopf-coordinate Laplacian yields eigenvalue \(-4(4+2)=-24\); the 25 permissible weights account for the entire dimension of the degree-four eigenspace. Distinct weights are orthogonal in both ambient space and torus image. Their restricted amplitudes have squared magnitudes \(\lambda_{a,b}(t)\), giving all nine sector formulas and their sign multiplicities. The normalizing constants can alternatively be checked by integrating the squared Jacobi polynomials against \(t^a(1-t)^b\) over \([0,1]\).

**2. Two competing bottlenecks.** By exchanging the two complex coordinates it suffices to optimize over \(0<t\le1/2\). The \((4,0)\) sector has eigenvalue
\[
U(t)=5t^4,
\]
while the \((1,1)\) sector has
\[
V(t)=30t(1-t)(2t-1)^2.
\]
Consequently \(A(t)\le\min\{U(t),V(t)\}\). The equality equation \(U=V\) for \(t>0\) simplifies to \(25t^3-48t^2+30t-6=0\). Its value is negative at \(21/50\) and positive at \(43/100\). On \((21/50,43/100)\) its derivative \(75t^2-96t+30\) is strictly positive; hence this interval contains exactly one crossing \(\tau\).

The function \(U\) increases strictly on \((0,1/2]\). The function \(V\) decreases strictly on \([\tau,1/2]\): with \(z=t-1/2\), its derivative is \(60z(1-8z^2)<0\) whenever \(\tau\le t<1/2\), since \(|z|<0.08<1/\sqrt8\). Thus for \(0<t<\tau\), \(A(t)\le U(t)<U(\tau)\), and for \(\tau<t\le1/2\), \(A(t)\le V(t)<V(\tau)=U(\tau)\). This is a **global** bound, not only a stationary-point calculation.

**3. Attainment and equality multiplicity.** At \(\tau\in(0.42,0.43)\), the five \(s=4\) sectors satisfy
\[
5\binom4a\tau^a(1-\tau)^{4-a}\ge5\tau^4,
\]
strictly unless \(a=4\), because \(1-\tau>\tau\). The \((1,1)\) sector equals \(5\tau^4\) by the defining cubic. The remaining sectors strictly exceed \(5\tau^4\): indeed \(5\tau^4<0.171\), while the \((2,0)\) sector exceeds \(5(0.42)^2(3-4(0.43))^2>1.4\), the \((0,2)\) sector exceeds \(5(0.57)^2(4(0.42)-1)^2>0.75\), and the \((0,0)\) sector exceeds \(\frac54(1-3(0.16)^2)^2>1\). These inequalities follow from rational interval bounds, not rounded numerical evidence. Therefore \(A(\tau)=5\tau^4>0\), attained exactly in the two axial \((\pm4,0)\) modes and four \((\pm1,\pm1)\) modes, multiplicity six. Coordinate exchange provides the second, and only other, maximizing torus at \(1-\tau\).

**4. Sharp recovery inequality.** In particular the theorem is equivalent to
\[
\sup_{0<t<1}\inf_{0\ne f\in\mathcal H_4}\frac{\|f|_{T_t}\|_{L^2(T_t)}^2}{\|f\|_{L^2(S^3)}^2}=5\tau^4.
\]
At either optimal torus every harmonic is determined by its trace, and the sharp minimal-norm inversion operator has norm \((5\tau^4)^{-1/2}\). This is a stability statement for continuous exact traces, not for arbitrary finite noisy point sets.

## Verification
The standalone `verify_exact.py` computes every Jacobi sector using rational-coefficient polynomials, checks the ambient normalization of all nine sectors by independently integrating their weighted squares as exact beta integrals, checks all 25 Fourier-weight multiplicities, verifies all five explicit formulas at four distinct rational radii, and checks the cubic equality and strict sector inequalities using rational interval bounds. A 90-step exact rational bisection localizes the optimizer, and the program prints `HOPF_QUARTIC_CHECK_OK`. Run with `python3 verify_exact.py`; only the Python standard library is required. The analytic proof above establishes the global continuous optimization; finite regression tests are not substitutes for its quantified inequalities.

## Relationship to prior work
The scalar Hopf-coordinate Jacobi basis is classical, including its presentation in Ben Achour et al. (2015); it is *not* claimed as new. Zandieh, Han and Avron (2022) study robust recovery of spherical-harmonic expansions from full-sphere random samples. Montaldo, Oniciuc and Ratto (2022) analyze variations and index of the Clifford torus in a distinct geometric variational problem. An accessible earlier result, *Exact Clifford-torus harmonic trace spectrum and sharp exponential inverse instability* (2026), determines the equal-radius **low-pass** trace spectrum and sharp inverse stability over all degrees below a cutoff. Another result, *Parity-sharp rectangular Hopf-grid interpolation of exact spherical harmonics* (2026), determines **rank and minimum grid size** for discrete root-of-unity samples on a fixed nonresonant torus but does not optimize its radius for trace stability. *Sharp quadrupole reconstruction from generalized Clifford hypersurfaces* (2026) optimizes degree **two**, not four. The present theorem instead isolates degree four, explicitly evaluates its nine radius-dependent sectors and establishes the exact **global maximin trace-frame radius** with a sixfold spectral bottleneck. The available published results do not state or force this minimax equality without an additional sector comparison and global proof.

## Limitations
The claim does not describe the largest singular value, optimize the condition-number ratio, include lower harmonic degrees, or apply to non-Hopf surfaces and arbitrary point samples. The radius is characterized algebraically, rather than in radicals. The comparison of literature cannot guarantee universal historical priority; an unindexed equivalent result in Hopf-torus sampling or isoparametric trace theory may exist. The high-level full-text comparison includes accessible published mathematical results and the inspected introduction of the 2022 geometrical source; the 2022 stochastic spherical-reconstruction source was accessible by abstract and metadata, not fully inspected. No independent mathematical audit has been performed.

## References
- A. Zandieh, I. Han and H. Avron, *Near Optimal Reconstruction of Spherical Harmonic Expansions*, arXiv:2202.12995v1, first publicly submitted 2022-02-25, https://arxiv.org/abs/2202.12995.
- S. Montaldo, C. Oniciuc and A. Ratto, *On the second variation of the biharmonic Clifford torus in \(S^4\)*, arXiv:2201.10415v1, first publicly submitted 2022-01-25, https://arxiv.org/html/2201.10415v1.
- J. Ben Achour, E. Huguet, J. Queva and J. Renaud, *Explicit vector spherical harmonics on the 3-sphere*, arXiv:1505.03426, first publicly submitted 2015-05-13, https://arxiv.org/abs/1505.03426.
- *Exact Clifford-torus harmonic trace spectrum and sharp exponential inverse instability*, publicly indexed 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-clifford-torus-harmonic-trace-spectrum-and-sharp-exponenti--2d81ee89510d.
- *Parity-sharp rectangular Hopf-grid interpolation of exact spherical harmonics*, publicly indexed 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-parity-sharp-rectangular-hopf-grid-interpolation-of-exact-spheri--78e042407020.
- *Sharp quadrupole reconstruction from generalized Clifford hypersurfaces*, publicly indexed 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-quadrupole-reconstruction-from-generalized-clifford-hypers--a088b6652f83.
