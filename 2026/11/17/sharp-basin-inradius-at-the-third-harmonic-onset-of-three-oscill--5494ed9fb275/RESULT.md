# Sharp basin inradius at the third-harmonic onset of three-oscillator splay locking

## Finding
For three identical, all-to-all pairwise phase oscillators with coupling \(H_a(t)=\sin t+a\sin(3t)\), a triangular splay rhythm becomes attracting at the sharp parameter \(a=1/6\). If \(\delta=a-1/6>0\), its attraction basin has, in the natural Euclidean metric on phases modulo common rotation, maximal centered-ball radius
\[
\boxed{\rho(a)=4\sqrt6\,\delta+O(\delta^2)\quad(\delta\downarrow0).}
\]
Each splay state has precisely three nearby non-synchronous equilibria, all saddles, at this same leading distance. This determines a sharp deterministic phase-error tolerance for the newly attracting rhythm; it does not assert that the complete basin area is small.

## Assumptions and scope
The state space is the three-torus of labelled phases, modulo common rotations, with dynamics
\[
\dot\theta_i=\omega+\sum_{j\ne i}\bigl[\sin(\theta_j-\theta_i)+a\sin(3(\theta_j-\theta_i))\bigr],\qquad i=1,2,3.
\]
Here \(a\) is real, \(\omega\) is arbitrary, and all pair gains equal one. Two splay phase classes are represented by \((0,2\pi/3,4\pi/3)\) and \((0,4\pi/3,2\pi/3)\). The quotient metric is the distance induced by the Euclidean norm on the orthogonal complement of \((1,1,1)\), with each phase taken modulo \(2\pi\). For each attracting splay class let \(\mathcal B_a\) be its basin and define \(\rho(a)=\sup\{r>0:B_r(\mathrm{splay})\subset\mathcal B_a\}\). The same quantity applies to both classes by permutation symmetry. All estimates below are for sufficiently small \(\delta>0\), with constants independent of \(\delta\).

## Proof
Common frequency cancels from phase differences. Near the first splay class set
\[
\theta_1=0,\qquad \theta_2=2\pi/3+x,\qquad\theta_3=4\pi/3+y,
\]
where this is a rotating reference-frame representative, and let \(w=(x,y)\). Writing \(F=(\dot\theta_2-\dot\theta_1,\dot\theta_3-\dot\theta_1)\), exact trigonometric differentiation gives
\[
F(w,\delta)=-9\delta w+Q(w)+E(w,\delta),\qquad
Q(w)=\frac{\sqrt3}{4}\begin{pmatrix}x^2+2xy-2y^2\\2x^2-2xy-y^2\end{pmatrix},
\]
with \(\|E(w,\delta)\|=O(\|w\|^3+|\delta|\|w\|^2)\) uniformly near the origin. In fact \(D_wF(0,\delta)=-9\delta I\) exactly.

The quotient norm has the coordinate expression
\[
r^2=\|w\|_q^2=\frac23(x^2-xy+y^2).
\]
A direct polynomial identity (checked also by the standalone script) is
\[
\|Q(w)\|_q^2=\frac{27}{32}\|w\|_q^4,
\qquad \|Q(w)\|_q=c\,r^2,\quad c=\frac{3\sqrt6}{8}.
\]
Consequently, using its associated inner product,
\[
\tfrac12\frac{d}{dt}r^2
=\langle w,F(w,\delta)\rangle_q
\le\bigl(-9\delta+c r+C(r^2+\delta r)\bigr)r^2
\]
for some uniform constant \(C\). Put \(R=9/c=4\sqrt6\). Choosing a sufficiently large fixed \(K\), the parenthesized expression is negative for every \(0<r\le R\delta-K\delta^2\) and all sufficiently small positive \(\delta\). Thus every initial phase class in the quotient ball of radius \(R\delta-K\delta^2\) converges to the splay class, establishing
\[
\rho(a)\ge R\delta-K\delta^2.
\]
This argument does not require a global basin description.

To obtain the opposite inequality, put \(w=\delta W\) in the equilibrium equation and divide by \(\delta^2\). The limit as \(\delta\downarrow0\) is
\[
G(W)=-9W+Q(W)=0.
\]
Its only real solutions are \(W=(0,0)\) and
\[
W_1=(8\sqrt3,4\sqrt3),\qquad
W_2=(-4\sqrt3,4\sqrt3),\qquad
W_3=(-4\sqrt3,-8\sqrt3).
\]
Each nonzero solution has quotient norm exactly \(R\), and its Jacobian \(D_WG\) has the two eigenvalues \(9\) and \(-27\). The implicit-function theorem therefore produces three saddle equilibrium branches
\[
w_j(\delta)=\delta W_j+O(\delta^2),\qquad
\operatorname{spec}D_wF(w_j(\delta),\delta)=\{9\delta+O(\delta^2),-27\delta+O(\delta^2)\}.
\]
They are the only other equilibria in a sufficiently small fixed neighborhood: if \(F(w,\delta)=0\) and \(w\ne0\), the identity \(\|Q(w)\|_q=cr^2\) and the remainder estimate force \(r=O(\delta)\), after which compactness and the four simple roots of \(G\) exclude additional branches. Each saddle lies outside the basin, so no basin-centered ball may contain it. Thus
\[
\rho(a)\le \min_j\|w_j(\delta)\|_q=R\delta+O(\delta^2).
\]
Combining bounds proves the claimed expansion. Permutation of oscillator labels gives the identical conclusion at the opposite-chirality splay class. Synchrony remains exponentially attracting here because its nontrivial Jacobian eigenvalues are \(-3(1+3a)<0\); hence the newly attracting splay rhythms coexist with stable synchrony.

## Verification
Run `python checker.py` with Python, SymPy, NumPy and SciPy. The script reconstructs the two-dimensional phase-difference field from the stated ODE, verifies the exact Jacobian, Taylor coefficients and quotient-norm identity, solves the polynomial blow-up equation, checks the saddle eigenvalues symbolically, and numerically tests all three branches at three small positive parameter values. The proof of the infinite-parameter asymptotic uses analytic estimates and the implicit-function theorem, not extrapolation of numerical samples.

## Relationship to prior work
Qie, Pedersen, Song, Liu and Shilnikov (arXiv:2611.06836v1, first public November 4, 2026) investigate phase reduction of three-cell inhibitory networks, including synchronous and traveling-wave rhythms, through numerical return maps and phase portraits. Ashwin, Bick and Burylko (2016) give general linear stability and bifurcation principles for identical phase oscillators and emphasize the special role of higher harmonics for three oscillators. Those earlier linear stability principles account for the splay threshold but do not determine this nonlinear **basin inradius** or its coefficient. Earlier related studies of other oscillator interactions address different parameter families. No claim is made that the general spectral stability criterion or the phenomenon of coexisting rhythms is new.

## Limitations
The theorem is local in the coupling parameter and applies to the specified odd first-plus-third-harmonic phase model with identical pair gains and no phase lag. It gives an inradius about each splay point, not the total basin measure, global separatrix geometry, noise-driven escape probability or a theorem about the original delay differential equations. The singular coefficient can change when additional harmonics alter the quadratic normal form. Priorities outside the inspected literature cannot be excluded; independent mathematical review has not occurred.

## References
1. X. Qie, M. G. Pedersen, J. Song, S. Liu and A. L. Shilnikov, *Delay-induced multirhythmicity in a 3-cell inhibitory network*, arXiv:2611.06836v1 (November 4, 2026), https://arxiv.org/html/2611.06836v1.
2. P. Ashwin, C. Bick and O. Burylko, *Identical Phase Oscillator Networks: Bifurcations, Symmetry and Reversibility for Generalized Coupling*, Frontiers in Applied Mathematics and Statistics **2** (2016), article 7, https://doi.org/10.3389/fams.2016.00007.
