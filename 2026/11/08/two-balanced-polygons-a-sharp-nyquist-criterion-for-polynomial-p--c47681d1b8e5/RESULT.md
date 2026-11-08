# Two balanced polygons: a sharp Nyquist criterion for polynomial phase retrieval

## Finding

For every integer \(d\ge3\), two concentric regular \(2d\)-gons at distinct positive radii recover every complex polynomial of degree at most \(d\), up to a single unimodular scalar, **exactly** when their relative angle \(\alpha\) satisfies \(\sin(d\alpha)\ne0\). The number of squared-modulus samples is \(4d\), divided equally between the polygons. The criterion is sharp in the angle and in the necessity of distinct nonzero radii.

In fact the \(4d\) measurements uniquely reconstruct the *entire* trigonometric intensity profiles on both circles by an explicit Fourier inversion. Their injectivity is not merely a generic-coefficient assertion.

## Assumptions and scope

Fix \(d\in\mathbb Z\), \(d\ge3\), real \(\alpha\), and \(0<r<R\). Define
\[
S_{d,r,R,\alpha}=\{r e^{\pi i k/d}:0\le k<2d\}\,\cup\,\{R e^{i(\alpha+\pi k/d)}:0\le k<2d\}.
\]
For any \(p(z)=\sum_{j=0}^d a_jz^j\), the measured data are \(|p(s)|^2\) for every \(s\in S_{d,r,R,\alpha}\). Two polynomials are equivalent only when they differ by multiplication by a constant of modulus one. We allow lower-degree and zero polynomials without extra genericity hypotheses.

The theorem is the equivalence
\[
\forall p,q\in\mathbb C[z]_{\le d}:\quad
\bigl(\forall s\in S_{d,r,R,\alpha},\ |p(s)|^2=|q(s)|^2\bigr)
\Longrightarrow\exists\zeta\in\mathbb C,\ |\zeta|=1,\ q=\zeta p
\quad\Longleftrightarrow\quad \sin(d\alpha)\ne0.
\]
The double implication above means the displayed universally quantified identification property holds exactly for the stated angular condition.

## Proof

**Step 1: only the top Fourier mode aliases.** For \(\rho>0\) write
\[
H_{p,\rho}(\theta)=|p(\rho e^{i\theta})|^2
=\sum_{m=-d}^d c_m(\rho)e^{im\theta},\qquad
c_m(\rho)=\rho^m\sum_{j=0}^{d-m}a_{j+m}\overline{a_j}\rho^{2j}\quad(0\le m\le d).
\]
Here \(c_{-m}(\rho)=\overline{c_m(\rho)}\). In particular, \(c_d(\rho)=\rho^d C_p\), where \(C_p=a_d\overline{a_0}\) is independent of radius. At nodes \(\theta_k=\phi+\pi k/d\), define
\[
D_m(\rho,\phi)=\frac{1}{2d}\sum_{k=0}^{2d-1}
H_{p,\rho}(\theta_k)e^{-im\theta_k}.
\]
Root-of-unity orthogonality gives \(D_m(\rho,\phi)=c_m(\rho)\) for \(0\le m<d\). The alternating sum is
\[
B(\rho,\phi)=\frac{1}{2d}\sum_{k=0}^{2d-1}(-1)^kH_{p,\rho}(\theta_k)
=2\rho^d\operatorname{Re}(e^{id\phi}C_p).
\]
Thus only the real Nyquist datum aliases; every lower Fourier coefficient is determined separately on each orbit.

**Step 2: two angles resolve the alias.** Take \((\rho,\phi)=(r,0)\) and \((R,\alpha)\). Put
\[
u=\frac{B(r,0)}{2r^d},\qquad v=\frac{B(R,\alpha)}{2R^d}.
\]
Then \(u=\operatorname{Re}C_p\) and \(v=\cos(d\alpha)\operatorname{Re}C_p-\sin(d\alpha)\operatorname{Im}C_p\). When \(\sin(d\alpha)\ne0\),
\[
C_p=u+i\frac{\cos(d\alpha)u-v}{\sin(d\alpha)}.
\]
This reconstructs the top Fourier coefficients on both radii and hence both full intensity profiles. More structurally, the space of *pairs* of real degree-\(d\) trigonometric polynomials whose respective top coefficients are \(r^d C\) and \(R^d C\) for a common \(C\in\mathbb C\) has real dimension \(2(2d-1)+2=4d\). The foregoing formulas invert its \(4d\)-sample map precisely when \(\sin(d\alpha)\ne0\). They also display the exact \(1/|\sin(d\alpha)|\) angular sensitivity of the top-frequency inversion, without claiming a full noisy phase-retrieval estimate.

**Step 3: equality on two entire circles implies a global phase.** Suppose \(p,q\) have equal samples, and \(\sin(d\alpha)\ne0\). Steps 1–2 imply \(|p(z)|=|q(z)|\) for every \(|z|=r\) and every \(|z|=R\). If either polynomial is identically zero, the other is zero too, because either orbit has \(2d>d\) distinct nodes. We may therefore assume both are nonzero and define the rational function \(F=p/q\). Equality on the circle \(|z|=\rho\) implies the rational identity
\[
F(z)\,\overline{F(\rho^2/\overline z)}=1
\]
for every point where both sides make sense, because it holds on the entire circle and hence identically as a rational identity. Comparing the identities for \(r\) and \(R\) yields
\[
F(w)=F\bigl((R/r)^2w\bigr)
\]
for all admissible \(w\). A rational function invariant under a real dilation by a factor strictly greater than one is constant: for example, its nonzero poles and zeros would otherwise have infinite dilation orbits, while a remaining monomial \(cw^j\) has invariance only if \(j=0\). The constant has modulus one by either circle. Therefore \(p=\zeta q\), as required.

**Step 4: sharp obstructions.** If \(\sin(d\alpha)=0\), every node \(z\) on both polygons has real \(z^d\). The two polynomials \(p(z)=1+i z^d\) and \(q(z)=1-i z^d\) have the same squared moduli at every node but are not constant unimodular multiples. If the two positive radii coincide, \(p(z)=1\) and \(q(z)=(z/r)^d\) agree in modulus on both polygons, irrespective of rotation. If one radius is zero, the nonzero orbit alone and the origin are likewise ambiguous: with \(\phi\) the angle of that orbit, take \(1+i e^{-id\phi}z^d\) and \(1-i e^{-id\phi}z^d\). This exhausts the claimed boundary failures.

## Verification

The attached standalone `check_sampling.py` numerically reconstructs all Fourier coefficients at both radii for degrees \(1\) through \(13\), tests off-grid intensity values, and verifies explicit resonance counterexamples. It prints `BALANCED_POLYGON_PHASE_CHECKS_PASS 5148`. It uses a fixed pseudorandom seed and only the Python standard library. These finite calculations test formulas, not universal injectivity; the proof above is the general certificate. In particular, the displayed top-mode inversion is a direct algebraic check of the essential determinant \(\sin(d\alpha)\).

## Relationship to prior work

Pohl, Li and Boche established a general \(4d\)-evaluation polynomial phase-retrieval construction using \(2d+1\) sites on one circle and \(2d-1\) on another [2, Theorem 7]. This proves existence at the same sample count but **does not imply** the result for two equally sized regular \(2d\)-gons, or classify their angular resonance. Chalendar and Partington established uniqueness from *entire* distinct circles of modulus data [1]; that full-circle theorem does not establish finite sampling. Bodmann and Hammen use two **intersecting** circles [3]; Przybyłek and Siedlecki study a larger polynomial-time sampling construction [4]. The present balanced two-orbit invertibility and sharp angular failure condition are the additional statements.

The degree-two case of a balanced two-square configuration has a direct separate treatment; this theorem isolates the uniform all-degree statement for \(d\ge3\). No claim is made of a new universal minimal measurement count.

## Limitations

The theorem applies to ordinary complex one-variable polynomials, concentric circular orbits, equal angular mesh sizes, distinct positive radii and squared point magnitudes. It does not supply a closed-form coefficient reconstruction algorithm from noisy data, a full Lipschitz recovery constant, or any optimality claim against arbitrary sampling designs. Prior constructions already attain the same number of measurements with different geometries. The absence of an identified equivalent balanced-circle theorem in the inspected literature does not establish exhaustive historical priority.

## References

[1] I. Chalendar and J. R. Partington, *Phase retrieval on circles and lines*, arXiv:2403.16255 (initial public submission 2024-03-24), especially §2 and the full-circle uniqueness results. https://arxiv.org/abs/2403.16255

[2] V. Pohl, N. Li and H. Boche, *Phase retrieval in spaces of analytic functions on the unit disk*, SampTA (2017), DOI:10.1109/SAMPTA.2017.8024411, Theorem 7 and Lemmas 4–6. https://doi.org/10.1109/SAMPTA.2017.8024411

[3] B. G. Bodmann and N. Hammen, *Stable phase retrieval with low-redundancy frames*, arXiv:1302.5487 (2013), polynomial sampling on intersecting circles. https://arxiv.org/abs/1302.5487

[4] M. R. Przybyłek and P. Siedlecki, *A note on the complexity of a phaseless polynomial interpolation*, arXiv:1907.09371 (2019), §4. https://arxiv.org/abs/1907.09371
