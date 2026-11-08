# Two-boundary surface thresholds and numerical-range rigidity for dimerized weighted shifts

## Finding
Let \(a,b,c,d>0\) with \(a\ne b\). On complex \(\ell^2(\mathbb N_0)\), let \(T\) be the unilateral forward weighted shift whose consecutive weights are
\[
(c,d,a,b,a,b,\ldots).
\]
Write \(L=a+b\), \(S=c^2+d^2\), and \(R=c^2+(L/b)d^2\). Then the following statements hold.

**Sharp surface-state and numerical-radius criterion.** If \(R\le L^2\), then
\[
w(T)=L/2,\qquad W(T)=\{z\in\mathbb C:|z|<L/2\}.
\]
If \(R>L^2\), there is a unique \(\lambda>L\) satisfying
\[
\lambda-\frac{c^2}{\lambda}=d^2\,g_{a,b}(\lambda),
\qquad
g_{a,b}(\lambda)=
\frac{\lambda^2+b^2-a^2-
\sqrt{[\lambda^2-L^2][\lambda^2-(a-b)^2]}}{2b^2\lambda}.
\]
In that regime
\[
w(T)=\lambda/2,\qquad W(T)=\{z\in\mathbb C:|z|\le\lambda/2\}.
\]
The square root is the positive real branch for \(\lambda>L\). Thus a two-parameter boundary modification creates a sharp transition from an unattained to an attained numerical radius.

**Exact allocation phase diagram.** Fix \(S=c^2+d^2>0\) while varying the allocation with \(c,d>0\). If \(S\le bL\), no allocation produces a surface state or closed numerical range. If \(bL<S<L^2\), a surface state occurs exactly when
\[
d^2>\frac ba(L^2-S).
\]
If \(S\ge L^2\), every positive allocation produces one. Throughout the fixed-budget family, \(w(T)\) is nondecreasing as \(d^2\) increases, and is strictly increasing whenever the smaller allocation already has a surface state. The threshold \(bL\) is sharp, and so is the automatic-binding threshold \(L^2\).

**Quadratic emergence.** Fix \(a,b,d>0\) with \(a\ne b\) and \(d^2<bL\). Let \(c_*^2=L^2-(L/b)d^2>0\), and set \(\varepsilon=c^2-c_*^2\downarrow0\) from above. Then the surface eigenvalue and numerical radius satisfy
\[
\lambda-L=\frac{b^3}{2aL d^4}\,\varepsilon^2+O(\varepsilon^3),
\qquad
w(T)-L/2=\frac{b^3}{4aL d^4}\,\varepsilon^2+O(\varepsilon^3).
\]
This is a genuine quadratic threshold onset, despite the linear dependence of the binding criterion on squared boundary weights.

## Assumptions and scope
The Hilbert space is complex, with orthonormal basis \((e_n)_{n\ge0}\). Precisely, \(Te_0=ce_1\), \(Te_1=de_2\), and for every integer \(k\ge0\), \(Te_{2k+2}=ae_{2k+3}\) and \(Te_{2k+3}=be_{2k+4}\). The numerical range is \(W(T)=\{\langle Tx,x\rangle:\|x\|=1\}\) and \(w(T)=\sup\{|z|:z\in W(T)\}\). All four weights are strictly positive; no assertion of the same phase diagram is made for a different periodic tail or for negative or complex edge weights without taking absolute values.

## Proof
**1. Periodic-tail resolvent.** Set \(J=T+T^*\). Discard the first two sites and consider the Jacobi operator \(B\) on the span of \((e_n)_{n\ge2}\), with first edge weight \(a\), second \(b\), and so on. Its spectral upper edge is \(L=a+b\): the two-periodic Floquet matrix gives bands with endpoints \(\pm(a+b)\) and \(\pm|a-b|\), and the half-line restriction has norm at most \(L\) by the maximum weighted row-sum bound. Approximate periodic vectors supported far from the boundary show \(L\) is in its essential spectrum. Thus \(\|B\|=L\).

For real \(\lambda>L\), put \(g(\lambda)=\langle e_2,(\lambda I-B)^{-1}e_2\rangle\). The tail starts with edge \(a\), while the stripped next tail starts with \(b\). Two applications of Schur complementation yield
\[
g(\lambda)=\frac1{\lambda-a^2 h(\lambda)},\qquad
h(\lambda)=\frac1{\lambda-b^2g(\lambda)}.
\]
Consequently
\[
b^2\lambda g^2-(\lambda^2+b^2-a^2)g+\lambda=0.
\]
The resolvent condition \(g(\lambda)\sim\lambda^{-1}\) at infinity selects the stated minus-square-root solution. In particular, \(g(L+)=1/b\). The spectral theorem gives \(g(\lambda)>0\), \(g'(\lambda)=-\|(\lambda I-B)^{-1}e_2\|^2<0\), and \(g(\lambda)\to0\) as \(\lambda\to\infty\). Moreover, \(g(\lambda)>1/\lambda\) for \(\lambda>L\): expand the resolvent in powers of \(B/\lambda\), note that all odd diagonal moments vanish by bipartiteness, and the second even moment equals \(a^2>0\).

**2. Binding threshold and uniqueness.** On the first two sites, \(J\) is the symmetric matrix with off-diagonal \(c\); the second site couples to \(B\) with strength \(d\). Schur complementation for \(\lambda>L\) reduces its eigenvalue condition to
\[
F(\lambda):=\lambda-\frac{c^2}{\lambda}-d^2g(\lambda)=0.
\]
This is equivalent to the existence of a nonzero square-summable eigenvector: the tail component is \(d u_1(\lambda-B)^{-1}e_2\), and the boundary equations determine nonzero \(u_0,u_1\). We have
\[
F'(\lambda)=1+\frac{c^2}{\lambda^2}-d^2g'(\lambda)>0,
\qquad
F(L+)=L-\frac{c^2}{L}-\frac{d^2}{b}=\frac{L^2-R}{L}.
\]
Also \(F(\lambda)\to+\infty\). Thus a unique eigenvalue above \(L\) exists precisely when \(R>L^2\). Equality does not produce an eigenvalue at \(L\), because a two-periodic tail at the band edge has no nonzero decaying \(\ell^2\) solution. As \(J\) is a finite-rank perturbation of the periodic half-line Jacobi operator, \(L\) is always an essential spectral point; no other eigenvalue can lie above it. Chiral conjugation by \(e_n\mapsto(-1)^n e_n\) gives spectral symmetry, so \(\|J\|\) is the top spectral point, equal either to \(L\) or to the unique \(\lambda\).

**3. Numerical range and attainment.** For each \(\theta\in\mathbb R\), conjugation by \(e_n\mapsto e^{in\theta}e_n\) turns \(T\) into \(e^{i\theta}T\). Hence every rotated real part has largest spectral value \(\|J\|/2\), and \(w(T)=\|J\|/2\). Unitary rotational invariance and Toeplitz--Hausdorff convexity force \(W(T)\) to be an open or closed centered disk. Equality in the real-part Rayleigh bound occurs exactly when \(\|J\|\) is an eigenvalue of \(J\). By step 2, this happens precisely for \(R>L^2\), giving the stated open/closed classification.

**4. Fixed-budget allocation.** With \(S=c^2+d^2\), the binding inequality is
\[
R=S+(a/b)d^2>L^2.
\]
Because \(0<d^2<S\), the possible ranges immediately give the three sharp regimes in the finding. To compare radii, write
\[
F(\lambda)=\lambda-\frac S\lambda-d^2\left(g(\lambda)-\frac1\lambda\right).
\]
The parenthesized quantity is strictly positive for every \(\lambda>L\), so increasing \(d^2\) strictly lowers \(F\) at each spectral parameter. Its unique root, when present, strictly increases; if no root occurs, both radii equal \(L/2\). This proves the monotonicity and its precise strictness qualification.

**5. Sharp edge scaling.** Near \(\lambda=L\), set \(\eta=\lambda-L\downarrow0\). The square-root formula gives
\[
g(L+\eta)=\frac1b-\kappa\sqrt\eta+O(\eta),
\qquad \kappa=\sqrt{\frac{2a}{b^3L}}>0.
\]
At fixed \(d\) and critical \(c_*\), the boundary equation therefore becomes
\[
0=-\frac\varepsilon L+d^2\kappa\sqrt\eta+O(\eta)+O(\varepsilon\eta).
\]
The nonzero coefficient of \(\sqrt\eta\) permits solving analytically in \(\sqrt\eta\) near \(\varepsilon=0\). Thus \(\sqrt\eta=\varepsilon/(Ld^2\kappa)+O(\varepsilon^2)\), giving the asserted coefficient \(b^3/(2aLd^4)\) and the halved numerical-radius coefficient.

## Verification
The formulas can be reproduced without finite-dimensional approximations: insert any positive \(a,b,c,d\) with \(a\ne b\) into the stated scalar \(g_{a,b}\), test the sign of \(R-L^2\), and, in the bound-state regime, solve the strictly increasing scalar equation \(F(\lambda)=0\) on \((L,\infty)\). The accompanying `CHECK.py` verifies the Schur quadratic, its boundary value, spectral inequalities, the threshold classification, and finite-section eigenvalue comparisons for several cases, using only the Python standard library. Finite sections are diagnostic and do not substitute for the spectral-theorem and Schur-complement arguments.

## Relationship to prior work
Ghosh--Birbonshi--Ojha (2026) analyze numerical radii of compact geometrically damped weighted shifts with a repeating four-term modulation. This result instead concerns a noncompact dimerized periodic tail with two tunable boundary bonds. Undrakh--Nakazato--Vandanjav--Chien (2015) calculate numerical radii for finitely many exceptional bonds followed by a *constant* tail, which covers the degenerate case \(a=b\), excluded from the stated scope. Garmon--Ordonez--Noba (2025) treat a quantum emitter attached by *one* exceptional hopping bond to an otherwise exactly period-two SSH tail, and derive its strong- and weak-coupling bound-state thresholds. Their single-bond model is a specialization of the present two-boundary-bond setup when the second boundary bond equals the appropriate bulk bond; no new discovery is claimed for that subfamily. The new comparison is the entire two-parameter threshold surface for genuine alternating tails, the fixed-squared-budget allocation phase diagram, and the quantitative edge onset. Wang--Wu (2011) study general openness of weighted-shift numerical ranges; their general openness criteria are not represented as new here.

## Limitations
The theorem determines the *upper* surface eigenvalue and hence the numerical radius; it does not classify eigenvalues in the central spectral gap or resonances on other sheets. General half-line Jacobi Weyl functions and SSH surface-state methods are established techniques, and a broader transfer-matrix treatment could imply the formula; a complete publication-priority determination would require comparison beyond the inspected texts, especially the full 2011 Wang--Wu article, which was not accessible. The quadratic coefficient is for fixed strictly positive second bond \(d\); it is not uniform as \(d\downarrow0\). The constant-tail limit \(a=b\) is previously studied and specifically excluded from the claimed new regime.

## References
1. A. Ghosh, R. Birbonshi, and S. Ojha, *On the numerical radius of a class of weighted shift operators*, arXiv:2608.17486v1 (first public 2026-08-18), https://arxiv.org/abs/2608.17486.
2. B. Undrakh, H. Nakazato, A. Vandanjav, and M.-T. Chien, *The numerical radius of a weighted shift operator*, Electronic Journal of Linear Algebra **30** (2015), https://doi.org/10.13001/1081-3810.2821.
3. S. Garmon, G. Ordonez, and K. Noba, *Weak-coupling bound states in semi-infinite topological waveguide QED*, arXiv:2503.07211v1 (2025), https://arxiv.org/abs/2503.07211.
4. K.-Z. Wang and P. Y. Wu, *Numerical ranges of weighted shifts*, Journal of Mathematical Analysis and Applications **381** (2011), 897--909, https://doi.org/10.1016/j.jmaa.2011.04.010.
5. C. W. Duncan, P. Öhberg, and M. Valiente, *Exact edge, bulk, and bound states of finite topological systems*, arXiv:1801.08942 (2018), https://arxiv.org/abs/1801.08942.
