# A complete spherical angle spectrum and a skew-normal exposure law for isocanted cubes

## Finding

The Euclidean isocanted cube has a complete, parameter-independent spherical vertex-normal-cone angle spectrum and a non-symmetric Gaussian-exposure limit. Fix an integer \(d\ge2\) and real numbers \(0<a<\ell\), and put
\[
\mathcal I_d(\ell,a)=\left\{x\in\mathbb R^d:\ |x_i|\le\frac\ell2,\quad |x_i-x_j|\le\ell-a\quad(1\le i<j\le d)\right\}.
\]
Write \(U_1,\ldots,U_d\) for independent half-normal variables, \(U_i\overset{\mathrm d}=|G_i|\), with independent standard Gaussian \(G_i\). Let
\[
q_{d,j}=\Pr\left\{\sum_{i=1}^{j}U_i>\sum_{i=j+1}^{d}U_i\right\},\qquad 0\le j\le d.
\]
Empty sums are zero. Then the normalized spherical vertex-normal-cone solid angles are exactly the \(d\) **distinct** values
\[
\omega_{d,j}=2^{-d}q_{d,j},\qquad 1\le j\le d,
\]
with respective multiplicities \(2\binom dj\). In particular \(q_{d,0}=0\), \(q_{d,d}=1\), \(q_{d,j}+q_{d,d-j}=1\), and
\[
0<q_{d,1}<q_{d,2}<\cdots<q_{d,d}=1.
\]
Every angle and multiplicity is independent of \(a\) and \(\ell\) throughout the stated open parameter domain.

Let \(\Phi\) and \(\phi\) denote the standard Gaussian CDF and density and put \(c=\sqrt{2/(\pi-2)}\). A dimension-uniform Berry--Esseen bound gives
\[
\sup_{0\le j\le d}\left|q_{d,j}-\Phi\left(c\frac{2j-d}{\sqrt d}\right)\right|\le\frac{C}{\sqrt d}
\]
for an absolute finite constant \(C\). In particular, if \((2j_d-d)/\sqrt d\to z\), then \(2^d\omega_{d,j_d}\to\Phi(cz)\).

Choose an independent uniform direction on the sphere and let \(J_d\) be the label \(j\) of the almost surely unique exposed vertex's angle level. Then
\[
\Pr\{J_d=j\}=2^{1-d}\binom dj q_{d,j},\qquad 1\le j\le d,
\]
and the **area-weighted** angle-rank law is skew-normal:
\[
\frac{2J_d-d}{\sqrt d}\ \xrightarrow{\mathrm d}\ Z,\qquad f_Z(z)=2\phi(z)\Phi\left(\sqrt{\frac2{\pi-2}}\,z\right),\quad z\in\mathbb R.
\]
The rank moments are exactly
\[
\mathbb EJ_d=\frac d2+\frac d\pi\arcsin\frac1{\sqrt d},\qquad
\operatorname{Var}(J_d)=\frac d4-\frac{d^2}{\pi^2}\arcsin^2\frac1{\sqrt d}.
\]
Consequently, \(\mathbb EJ_d=d/2+\sqrt d/\pi+O(d^{-1/2})\), and \(\operatorname{Var}(J_d)=d(1/4-1/\pi^2)+O(1)\).

## Assumptions and scope

All geometry is intrinsic to the ordinary Euclidean coordinates \(\mathbb R^d\), not to a lattice-normalized or affine-changed model. A vertex-normal-cone angle is the \((d-1)\)-dimensional spherical measure of the outer normal cone intersected with the unit sphere, divided by the surface measure of that sphere. Equivalently it is the probability that a standard Gaussian direction uniquely exposes that vertex. The theorem covers every integer \(d\ge2\) and every pair of real parameters \(0<a<\ell\). At the excluded degeneracies \(a=0\) or \(a=\ell\), the vertex and normal-cone descriptions change, and the stated multiplicities are not asserted.

## Proof

**Step 1: the support function and a complete vertex labelling.** The Minkowski segment presentation of the isocanted cube is
\[
\mathcal I_d(\ell,a)=\frac{\ell-a}{2}[-1,1]^d+\frac a2[-1,1]\mathbf1,
\]
where \(\mathbf1=(1,\ldots,1)\). This follows directly by solving the coordinate range constraints, and appears in the 2024 volume paper cited below. The support function at \(g\in\mathbb R^d\) is therefore
\[
h(g)=\frac{\ell-a}{2}\sum_i|g_i|+\frac a2\left|\sum_i g_i\right|.
\]
For every \(g\) having no zero coordinate and nonzero sum, its unique exposed point is
\[
v(s,\eta)=\frac{\ell-a}{2}s+\frac a2\eta\mathbf1,
\qquad s_i=\operatorname{sgn}g_i,\quad \eta=\operatorname{sgn}\sum_i g_i.
\]
The only impossible pairs are all-positive \(s\) with \(\eta=-1\) and all-negative \(s\) with \(\eta=+1\). All other pairs occur on nonempty open direction cones: whenever the signs include one with the sign \(\eta\), make that coordinate large in absolute value and the others small. The resulting points are distinct: for different \(\eta\), equality would force every coordinate sign to flip in the same direction, requiring precisely one of the two excluded pairs; for equal \(\eta\), equality forces equal \(s\). Hence the list is precisely the \(2^{d+1}-2\) vertices, and there are no hidden zero-angle vertices.

**Step 2: exact angular levels.** Suppose the sign vector has \(j\) positive coordinates and the sum of coordinates is positive. The Gaussian probability of this full sign event and of positive total is \(2^{-d}q_{d,j}\), since Gaussian signs are independent fair signs and independent of their half-normal magnitudes. For negative total, a sign vector with \(d-j\) positive coordinates has the same angle after central reflection. Thus the number of vertices at level \(q_{d,j}/2^d\) is \(2\binom dj\). There are \(d\) levels since \(q_{d,0}=0\) and \(q_{d,d}=1\). By coupling all half-normal variables on one probability space, increasing \(j\) to \(j+1\) adds \(2U_{j+1}\) to the signed sum. It strictly raises the positivity probability because the joint density is positive on the open configurations that cross zero. Thus all levels are distinct. The complement symmetry gives \(q_{d,j}=1-q_{d,d-j}\), and the angles sum to one.

**Step 3: uniform asymptotic profile.** Let \(\mu=\mathbb EU_1=\sqrt{2/\pi}\) and \(\sigma^2=\operatorname{Var}(U_1)=1-2/\pi\). The signed sum defining \(q_{d,j}\) has mean \(\mu(2j-d)\) and variance \(d\sigma^2\). Its centered summands are independent, have uniformly bounded absolute third moments, and share variance \(\sigma^2\). Berry--Esseen therefore applies uniformly over every choice of signs and \(j\), giving the stated absolute \(O(d^{-1/2})\) approximation with \(\mu/\sigma=\sqrt{2/(\pi-2)}\).

**Step 4: exposure sampling and skew-normal limit.** Given independent standard Gaussians \(G_1,\ldots,G_d\), write \(K=\#\{i:G_i>0\}\) and \(S=\sum_iG_i\). From Step 1 the angle-level index of the exposed vertex is \(J_d=K\) when \(S>0\), and \(J_d=d-K\) when \(S<0\). Central reflection shows that \(J_d\) is identically distributed with \(K\) conditional on \(S>0\). Its finite distribution is \(2^{1-d}\binom dj q_{d,j}\).

Consider the independent identically distributed pairs \((\operatorname{sgn}G_i,G_i)\). Their covariance matrix has diagonal entries \(1\) and off-diagonal entry \(\rho=\mathbb E|G_i|=\sqrt{2/\pi}\). The bivariate central limit theorem yields
\[
\left(\frac{2K-d}{\sqrt d},\frac S{\sqrt d}\right)\xrightarrow{\mathrm d}(X,Y),
\quad (X,Y)\text{ centered bivariate normal with correlation }\rho.
\]
Since \(\Pr(Y=0)=0\) and \(\Pr(S>0)=1/2\), conditioning on a positive second coordinate is continuous at the limit. The conditional density of \(X\) given \(Y>0\) is
\[
2\phi(z)\Pr(Y>0\mid X=z)=2\phi(z)\Phi\left(\frac{\rho z}{\sqrt{1-\rho^2}}\right),
\]
which proves the stated limit.

**Step 5: exact moments.** Put \(\theta_d=\arcsin(d^{-1/2})\). The standard bivariate centered-normal orthant identity gives
\[
\Pr(G_1>0,S>0)=\frac14+\frac{\theta_d}{2\pi}.
\]
For two distinct coordinates, the trivariate centered-normal orthant identity, using \(\operatorname{Corr}(G_1,G_2)=0\) and the two correlations \(d^{-1/2}\), gives
\[
\Pr(G_1>0,G_2>0,S>0)=\frac18+\frac{\theta_d}{2\pi}.
\]
Conditioning on \(S>0\) and using exchangeability therefore yields
\[
\mathbb EJ_d=2d\Pr(G_1>0,S>0)
\]
and
\[
\mathbb E[J_d(J_d-1)]=2d(d-1)\Pr(G_1>0,G_2>0,S>0).
\]
Substituting and simplifying gives exactly the stated expectation and variance. Expanding \(\arcsin(d^{-1/2})\) gives their large-\(d\) orders.

## Verification

The standalone `check_normal.py` recreates the vertices directly in Euclidean coordinates, compares 16,000 Gaussian support directions per dimension against the predicted sign map for dimensions 2 through 8, checks exact finite moment identities by simulation, and tests half-normal angular levels and the central Gaussian profile. It also checks strict level ordering and angle normalization. These finite checks corroborate the theorem but are not the proof of its unbounded-dimensional assertions. Run with `python check_normal.py` using Python 3, NumPy and SciPy. Tested with NumPy 2.3.5 and SciPy 1.17.0.

## Relationship to prior work

The 2020 paper of de la Puente and Clavería established the isocanted alcoved family, its fixed combinatorial type and vertex count. Their 2024 paper supplies its zonotope segment representation and volume determinant. The 2025 paper computes lower-dimensional face measures, incidence numbers, and symmetries. These results establish the geometric starting point; none of the inspected treatments states the Gaussian-normal-cone angle spectrum, the uniform half-normal sigmoid, the skew-normal directional-exposure rank law, or the exact arcsine moment formulas as such. The new statements use the ordinary Euclidean normal fan rather than uniform vertex counting, volume covariance, or enclosing ellipsoids.

## Limitations

Historical novelty is supported by comparison with the cited primary texts and relevant indexed research records but is not a proof that no equivalent unpublished or unindexed result exists. The theory assumes the unmodified, isotropically normalized Euclidean realization and strictly positive segment lengths; it does not address boundary degeneration of parameters, other zonotopes with several noncoordinate circuits, or affine-invariant quantities. The numerical checker verifies finite examples only. No independent mathematical audit has been carried out.

## References

1. María Jesús de la Puente and Pedro Luis Clavería, *Isocanted alcoved polytopes*, arXiv:2009.13858, first submitted 2020-09-29, https://arxiv.org/abs/2009.13858; *Applications of Mathematics* 65 (2020), 703–726, https://doi.org/10.21136/AM.2020.0373-19.
2. M. J. de la Puente and P. L. Clavería, *The volume of an isocanted cube is a determinant*, arXiv:2406.01565, first submitted 2024-06-03, https://arxiv.org/abs/2406.01565.
3. M. J. de la Puente, *Isocanted cube: the lower Lebesgue volumes, incidence numbers and symmetries of this d-dimensional tile*, *Extracta Mathematicae* 40 (2025), 1–26, https://doi.org/10.17398/2605-5686.40.1.1.
