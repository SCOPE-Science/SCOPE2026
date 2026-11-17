# A universal supercriticality law for the first oscillatory instability of cyclic Euler–Lotka–Volterra competition

## Finding
For an explicitly characterized two-parameter region of nonnegative cyclic competition, the positive homogeneous equilibrium of the three-species Euler–Lotka–Volterra map loses stability **first** through a supercritical Neimark–Sacker bifurcation. Its cubic radial coefficient has the exact, strictly negative expression
\[
\boxed{\ell_1=-2R_*a^2(1+R_*)<0},
\]
with the Fourier coordinate and parameters defined below. No low-order resonance exclusion is needed: the inequality specifying the first oscillatory instability itself precludes all resonances of orders one through four. The theorem gives an attracting small invariant closed curve and its sharp leading amplitude for every admissible competition pair, not just a numerical example.

## Assumptions and scope
Fix \(\alpha,\beta\geq0\) such that
\[
1<\alpha+\beta<2,\qquad \alpha^2+\beta^2>\alpha+\beta.
\]
(The first strict lower bound follows from the second inequality and \(\alpha+\beta<2\), but is written to clarify the region.) On a neighborhood of the positive equilibrium, consider the polynomial map
\[
\begin{aligned}
x'&=x+Rx(1-x-\alpha y-\beta z),\\
y'&=y+Ry(1-\beta x-y-\alpha z),\\
z'&=z+Rz(1-\alpha x-\beta y-z),
\end{aligned}\qquad R>0.
\]
Write
\[
S=1+\alpha+\beta,\qquad a=1-\frac{\alpha+\beta}{2},\qquad
b=\frac{\sqrt3}{2}(\alpha-\beta),\qquad C=a^2+b^2,
\]
and define
\[
\boxed{R_*=\frac{2Sa}{C}}.
\]
These assumptions imply \(0<a<1/2\), \(b\neq0\), and \(0<R_*<2\). For the invariant-curve assertion the parameter \(R\) varies near \(R_*\), with \(\alpha,\beta\) fixed. The map is used locally as an analytic map of \(\mathbb R^3\); no global positive-octant invariance outside this neighborhood is asserted.

Let \(\omega=e^{2\pi i/3}\). The *Fourier amplitude* \(w\) and spatial-mean displacement \(r\) are defined uniquely near the equilibrium by
\[
(x_j)_{j=0}^{2}=S^{-1}+r+w\omega^j+\bar w\omega^{-j},\quad
(x_0,x_1,x_2)=(x,y,z).
\]
The cubic coefficient uses a near-identity complex normal-form coordinate \(z=w+O(|w|^2)\) with unit complex derivative at the fixed point; its numerical value depends on this normalization while its sign does not.

## Proof
**1. Sharp location of the first stability loss.** The homogeneous equilibrium is \(E=(S^{-1},S^{-1},S^{-1})\). Fourier diagonalization of its circulant Jacobian yields
\[
\lambda_0=1-R,\qquad \lambda_\pm=1-\frac{R}{S}(a\pm ib),\qquad
|\lambda_\pm|^2=1-\frac{2Ra}{S}+\frac{R^2 C}{S^2}.
\]
The complex pair first meets the unit circle at \(R=R_*\), with
\[
\left.\frac{d}{dR}|\lambda_\pm|\right|_{R_*}=\frac aS>0.
\]
The radial multiplier meets \(-1\) at \(R=2\). Direct expansion gives
\[
C-Sa=\frac32(\alpha^2+\beta^2-\alpha-\beta)>0,
\]
so \(R_*<2\). Thus \(E\) is locally asymptotically stable for every \(0<R<R_*\), and the pair crosses outward while the third multiplier lies strictly inside the unit disk.

**2. Automatic absence of the strong resonances.** Since \(\alpha,\beta\ge0\),
\[
b^2\le3(1-a)^2,\qquad
C>Sa\iff b^2>3a(1-a).
\]
Combining gives \(a<1/2\), and then \(b^2>3a^2\). At the crossing,
\[
\lambda=1-\frac{R_*}{S}(a+ib)=\frac{b^2-a^2-2iab}{a^2+b^2}.
\]
Therefore \(|\arg\lambda|=2\arctan(a/|b|)<\pi/3\). As \(\lambda\ne1\), it is not a root of unity of any order from one through four. In particular the quadratic and cubic normal-form transformations used below are nonresonant, with no additional assumptions.

**3. Exact Fourier dynamics.** Denote \(c=a+ib\). Substituting the Fourier coordinates into the polynomial map gives exactly, with no remainder,
\[
\begin{aligned}
r'&=(1-R)r-R(Sr^2+2a|w|^2),\\
w'&=\left(1-\frac{Rc}{S}\right)w
-R\bigl[(S+c)rw+\bar c\,\bar w^2\bigr].
\end{aligned}
\]
At \(R=R_*\), a smooth local two-dimensional center manifold has a quadratic graph \(r=h|w|^2+O(|w|^3)\). The first exact equation and \(|\lambda|=1\) yield
\[
h=(1-R_*)h-2R_*a,\qquad h=-2a.
\]
On this manifold the complex coordinate obeys
\[
w'=\lambda w+q\bar w^2+d\,w|w|^2+O(|w|^4),\qquad
q=-R_*\bar c,\quad d=2R_*a(S+c).
\]

**4. The universal cubic sign.** Eliminate the quadratic term with \(w=z+H\bar z^2+O(|z|^3)\), where
\[
H=\frac{q}{\bar\lambda^{\,2}-\lambda}.
\]
The resonant cubic coefficient in the complex normal form is
\[
L=d+2q\bar H,
\]
up to removable nonresonant cubic terms. Its radial component is
\[
\begin{aligned}
\ell_1&=\operatorname{Re}(\bar\lambda L)
=\operatorname{Re}(\bar\lambda d)
+2|q|^2\operatorname{Re}\!\left(\frac{1}{\lambda^3-1}\right)\\
&=2R_*a(S-a-R_*a)-R_*^2(a^2+b^2)\\
&=-2R_*a^2(1+R_*)<0.
\end{aligned}
\]
Here \(|\lambda|=1\), \(\lambda^3\ne1\), and the elementary identity \(\operatorname{Re}[(\zeta-1)^{-1}]=-1/2\) for \(|\zeta|=1\), \(\zeta\ne1\), were used. In the last step use \(R_*C=2Sa\). This establishes the signed cubic coefficient without numerical approximation.

**5. Bifurcating circle and its amplitude.** The standard local nonresonant Neimark–Sacker theorem applies: the transverse multiplier is contracting, the complex pair crosses transversely, no resonances of orders one through four occur, and \(\ell_1<0\). Thus for every fixed admissible \((\alpha,\beta)\), and every sufficiently small positive \(\delta=R-R_*\), there exists a locally attracting invariant Jordan curve in the positive octant. The radial normal form gives uniformly along that curve
\[
\boxed{|w|^2=\frac{\delta}{2R_*aS(1+R_*)}+o(\delta)}.
\]
The center-manifold spatial mean satisfies \(r=-2a|w|^2+o(\delta)\); in particular the mean population shifts below \(S^{-1}\) by \(\delta/[R_*S(1+R_*)]+o(\delta)\). Local attracting means the circle attracts all sufficiently nearby trajectories transverse to and along the circle as a set, not that every trajectory converges to a single periodic point on it. The region remains positive because \(E\) is interior and the curve shrinks to \(E\) at onset.

## Verification
The standalone `check_normal_form.py` is executable with Python 3 and SymPy. It uses symbolic simplification over freely varying positive real parameters to prove the universal coefficient identity, verifies the exact coordinate recurrence by symbolic expansion at a nontrivial algebraic parameter choice, tests resonance and transversality, and confirms a nearby numerical amplitude. Run `python check_normal_form.py` in the extracted directory. The numerical orbit is merely an illustration; the universal assertion follows from the analytic algebra and the standard bifurcation theorem.

For a rational parameter witness, set \((\alpha,\beta)=(3/2,1/10)\). Then \(S=13/5\), \(a=1/5\), \(b=7\sqrt3/10\), \(R_*=104/151\), and \(\lambda=(143-28\sqrt3 i)/151\). The exact first Lyapunov coefficient is \(-10608/114005\), and the third eigenvalue is \(47/151\).

## Relationship to prior work
Muni (2024) studies precisely this cyclic polynomial map, reporting numerically observed supercritical Neimark–Sacker behavior for selected parameter paths, torus doubling, and hyperchaos. This result does not claim to discover the map or the existence of any Neimark–Sacker bifurcation. Its specific addition is the sharp all-admissible-competition first-crossing criterion and an exact always-negative cubic coefficient with a family-wide invariant-circle amplitude law.

Joshi, Savescu, Syed, and Blackmore (2021) study the general three-species polynomial Lotka–Volterra family in equivalent birth-rate coordinates. Their inspected full text develops several other bifurcation mechanisms, including higher-dimensional sphere-producing analogs, but does not derive this cyclic first-crossing normal form. Gardini and Sushko (2011) give a generic qualitative three-dimensional Neimark–Sacker setting and torus-doubling scenarios, not a cyclic all-parameter coefficient calculation.

Gardini, Lupini, Mammana, and Messia (1987) is a particularly pertinent predecessor on the same cyclic map and its fixed-point Hopf/Neimark–Sacker structure. Only the abstract could be inspected; a complete overlap comparison was not possible. It may contain specialized weak-resonance results. This unresolved source is an explicit priority risk rather than evidence of noncoverage.

A published circulating-logistic-triad result derives a universal negative cubic coefficient for a **different** map whose cyclic interactions are antisymmetric rather than simultaneously nonnegative competitive. It cannot imply the present coefficient by setting its coupling constant, since such a substitution would require \(\alpha+\beta=0\), contradicting the present first-crossing region. A published Euler–May–Leonard invariant-measure theorem treats the disjoint balance line \(\alpha+\beta=2\) and not the present \(\alpha+\beta<2\) first oscillatory instability.

## Limitations
All bifurcation and attraction statements are local to the positive homogeneous equilibrium and to \(R=R_*\), with the competition pair held fixed. Neither global nonnegative invariance nor global attraction nor all rotation numbers on the small curve are characterized. The amplitude and cubic coefficient are specified in Fourier coordinates. The uniqueness of this analytic formula in the global historical literature is not established; the inaccessible 1987 same-map article remains a substantial publication-priority risk. A self-review is not an independent mathematical audit.

## References
1. S. S. Muni, *Torus and hyperchaos in 3D Lotka–Volterra map*, arXiv:2408.15054 (first posted 2024-08-27), https://arxiv.org/abs/2408.15054.
2. Y. Joshi, M. Savescu, M. Syed, and D. Blackmore, *Interesting Features of Three-Dimensional Discrete Lotka–Volterra Dynamics*, Applied Mathematics 12 (2021), 694–722, https://doi.org/10.4236/am.2021.128049.
3. L. Gardini, R. Lupini, C. Mammana, and M. G. Messia, *Bifurcations and Transitions to Chaos in the Three-Dimensional Lotka–Volterra Map*, SIAM J. Appl. Math. 47 (1987), 455–482, https://doi.org/10.1137/0147031 (abstract inspected only).
4. L. Gardini and I. Sushko, *Doubling bifurcation of a closed invariant curve in 3D maps*, ESAIM Proceedings 36 (2012), 1–14, https://www.mdef.it/public/fileadmin/whoiswho/gardini/Publications/Journals/GS_ESAIM_2012.pdf.
5. Y. A. Kuznetsov, *Elements of Applied Bifurcation Theory*, 3rd edition, Springer (2004), classical Neimark–Sacker theorem.
