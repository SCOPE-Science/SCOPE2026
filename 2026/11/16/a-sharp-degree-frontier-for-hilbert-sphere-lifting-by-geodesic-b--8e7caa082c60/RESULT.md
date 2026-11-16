# A sharp degree frontier for Hilbert-sphere lifting by geodesic Bernstein sampling

## Finding

Let \(\Psi_d\) be the cone of continuous real zonal positive-semidefinite kernels on the unit sphere \(S^d\), expressed as functions of geodesic distance \(\theta\in[0,\pi]\), and let \(\Psi_\infty\) denote the corresponding Hilbert-sphere cone. For each integer \(n\ge1\), define the **geodesic-angle Bernstein operator**

\[
(\mathcal B_n f)(\theta)=\sum_{j=0}^n\binom nj(\theta/\pi)^j(1-\theta/\pi)^{n-j}f(j\pi/n).
\]

**Theorem (sharp universal lifting frontier).** For every \(d\ge2\), including arbitrary finite dimensions and the Hilbert sphere, the inclusion
\[
\mathcal B_n(\Psi_d)\subseteq\Psi_\infty
\]
holds for \(n=1,2,3\). This degree range is sharp *uniformly over dimensions*: for every \(n\ge4\), an input from \(\Psi_2\) has a Bernstein image not belonging to \(\Psi_\infty\). By contrast, on the circle,
\[
\mathcal B_n(\Psi_1)\subseteq\Psi_\infty\quad\Longleftrightarrow\quad n\le2.
\]

In the positive direction the output has an absolutely convergent series with nonnegative coefficients in \(u=\cos\theta\); thus its positive definiteness is valid simultaneously in every spherical dimension. The failures in this theorem are failures of the *dimension-lifting property*, not claims that the indicated outputs are non-positive-definite on their original spheres.

## Assumptions and scope

Here positive definite means that every finite kernel matrix is positive semidefinite; strict positive definiteness is not assumed. \(S^d\) is the unit sphere of \(\mathbb R^{d+1}\), and \(S^\infty\) is the unit sphere of a real infinite-dimensional Hilbert space. The same scalar function \(f(\theta)\) is transported between spheres; there is no rescaling of geodesic distance. The normalization \(f(0)=1\) is used for basis computations, while the theorem is homogeneous and also covers zero kernels.

A normalized Gegenbauer basis element \(R_m^{(d)}(u)\), with \(R_m^{(d)}(1)=1\), defines an element of \(\Psi_d\). On \(S^2\) it is the Legendre polynomial \(P_m(u)\), and on \(S^1\) it is \(\cos(m\theta)\). The Schoenberg expansions of arbitrary continuous positive-definite kernels use nonnegative summable weights on these basis elements. The Hilbert-sphere characterization is a nonnegative summable power series in \(u=\cos\theta\).

The operator is Bernstein interpolation **in the angular variable \(\theta/\pi\)**. It is not affine Bernstein interpolation in the dot-product variable \((u+1)/2\); the two use different sampling nodes and have different outputs.

## Proof

### 1. A universal bound for the Gegenbauer samples

Fix \(d\ge2\) and a normalized Gegenbauer basis element \(R_m^{(d)}\). Put \(p=R_m^{(d)}(1/2)\). The key bounds are
\[
-\frac13\le p\le1\quad(m\text{ even}),\qquad -1\le p\le\frac12\quad(m\text{ odd}). \tag{1}
\]

To prove them without a dimension-dependent estimate, restrict the positive-definite zonal kernel \(R_m^{(d)}(x\cdot y)\) to an embedded \(S^2\). Its unique Legendre expansion has nonnegative coefficients by Schoenberg's theorem. As the polynomial has degree at most \(m\), parity \(m\), and value one at \(u=1\), it is a **convex combination** of Legendre polynomials \(P_\ell(u)\) with \(0\le\ell\le m\) and \(\ell\equiv m\pmod 2\). It is therefore enough to bound their values at \(u=1/2\).

The first eight such values, in order \(\ell=0,\ldots,7\), are exactly
\[
1,\quad\frac12,\quad-\frac18,\quad-\frac7{16},\quad-\frac{37}{128},\quad\frac{23}{256},\quad\frac{331}{1024},\quad\frac{457}{2048}.
\]
For all \(\ell\ge8\), the classical Laplace integral, evaluated at \(u=1/2\), gives
\[
P_\ell(1/2)=\frac1\pi\int_0^\pi\left(\frac12+i\frac{\sqrt3}{2}\cos t\right)^\ell\,dt,
\]
so that
\[
|P_\ell(1/2)|\le\frac1\pi\int_0^\pi\left(\frac14+\frac34\cos^2t\right)^{\ell/2}dt
\le\frac1\pi\int_0^\pi\left(\frac14+\frac34\cos^2t\right)^4dt
=\frac{10643}{32768}<\frac13.\tag{2}
\]
The final equality is an exact binomial expansion using \(\pi^{-1}\int_0^\pi\cos^{2j}t\,dt=\binom{2j}{j}/4^j\). The low-degree values and (2) prove (1). The trivial bound \(|p|\le1\) also follows from the positive-definite two-point matrix.

### 2. Cubic Bernstein images and arcsine coordinates

Write \(u=\cos\theta\), \(A(u)=\arcsin u\), \(y=A(u)/\pi\), and \(x=\theta/\pi=1/2-y\). By parity, the four samples of \(R_m^{(d)}(\cos\theta)\) at \(0,\pi/3,2\pi/3,\pi\) are \((1,p,p,1)\) if \(m\) is even and \((1,p,-p,-1)\) if \(m\) is odd. Direct Bernstein expansion yields
\[
\mathcal B_3[R_m^{(d)}](u)=
\begin{cases}
(1+3p)/4+3(1-p)(A(u)/\pi)^2,&m\text{ even},\\
\tfrac32(1+p)A(u)/\pi+(2-6p)(A(u)/\pi)^3,&m\text{ odd}.
\end{cases}\tag{3}
\]

For even \(m\), (1) shows both scalar coefficients in (3) are nonnegative. Since \(A(u)\) has a nonnegative power series in odd powers of \(u\), the entire even expression has nonnegative ordinary power coefficients.

### 3. The cubic arcsine coefficient lemma

Write \(A(u)=\sum_{k\ge0}a_k u^{2k+1}\), with \(a_k=\binom{2k}{k}/(4^k(2k+1))>0\), and \(A(u)^3=\sum_{k\ge0}c_k u^{2k+1}\). Then \(c_0=0\) and
\[
\frac{c_k}{a_k}=r_k:=6\sum_{j=1}^k\frac1{(2j-1)^2},\qquad 0\le r_k<\frac{3\pi^2}{4}.\tag{4}
\]
Indeed, \((1-u^2)A''-uA'=0\) and \((1-u^2)(A^3)''-u(A^3)'=6A\). Comparing coefficients gives
\[
(2k+3)(2k+2)a_{k+1}=(2k+1)^2a_k,
\]
\[
(2k+3)(2k+2)c_{k+1}=(2k+1)^2c_k+6a_k,
\]
so \(r_{k+1}-r_k=6/(2k+1)^2\). The strict upper bound follows from \(\sum_{j\ge1}(2j-1)^{-2}=\pi^2/8\).

In the odd case of (3), the coefficient of \(u^{2k+1}\) is
\[
\frac{a_k}{\pi}\left[\frac32(1+p)+\frac{2-6p}{\pi^2}r_k\right].\tag{5}
\]
If \(-1\le p\le1/3\), both summands in brackets are nonnegative. If \(1/3<p\le1/2\), (4) and the negative coefficient \(2-6p\) yield the lower bound
\[
\frac32(1+p)+\frac{2-6p}{\pi^2}r_k\ge\frac32(1+p)+\frac34(2-6p)=3(1-p)>0.
\]
Thus every cubic Bernstein image of a Gegenbauer basis kernel has an ordinary nonnegative power expansion.

Schoenberg's Hilbert-sphere theorem makes each basis image positive definite on \(S^\infty\). For a general \(f\in\Psi_d\), its nonnegative Gegenbauer series converges absolutely and uniformly, and the finite-node operator \(\mathcal B_3\) is bounded in the uniform norm. Passing to the limit and using closedness of the cone (or nonnegative coefficient summation) proves \(\mathcal B_3f\in\Psi_\infty\). No assumption on the differentiability or strict positivity of \(f\) is required.

### 4. Lower degrees

For \(n=1\), the even basis image is the constant one, while the odd image is \(2A(u)/\pi\). For \(n=2\), the even image with \(p=R_m^{(d)}(0)\) is
\[
(1+p)/2+2(1-p)(A(u)/\pi)^2,
\]
and the odd image is \(2A(u)/\pi\). Here \(|p|\le1\). These nonnegative power expansions establish lifting for \(n=1,2\) on every sphere, including \(S^1\).

### 5. Sharp failure at degree four and every higher degree

An output belonging to \(\Psi_\infty\) must be nonnegative at \(u=0\), because it is a nonnegative power series in \(u\). For \(n=4\), take the legitimate \(S^2\) basis kernel \(f(\theta)=P_6(\cos\theta)\). Its samples at \(j\pi/4\) are \((1,-19/128,-5/16,-19/128,1)\), and the midpoint Bernstein weights are \((1,4,6,4,1)/16\). Hence
\[
\boxed{\mathcal B_4 f(\pi/2)=-17/256<0.}\tag{6}
\]

For every \(n\ge5\), use \(f(\theta)=P_2(\cos\theta)=(3\cos^2\theta-1)/2\), also positive definite on \(S^2\). The binomial characteristic function at \(x=1/2\) gives
\[
\mathcal B_n f(\pi/2)=\frac{1-3\cos(\pi/n)^n}{4}.\tag{7}
\]
The function \(t\mapsto\cos(\pi/t)^t\) increases strictly for \(t>2\): its logarithmic derivative is \(\log\cos z+z\tan z>0\), where \(z=\pi/t\), since the latter expression vanishes at \(z=0\) and has derivative \(z\sec^2z>0\). At \(t=5\),
\[
\cos(\pi/5)^5=(11+5\sqrt5)/64>1/3
\]
(the final inequality is equivalent to \(15\sqrt5>31\)). Thus (7) is strictly negative for every \(n\ge5\). This proves the sharp failure of the uniform \(S^2\)-to-\(S^\infty\) lifting assertion for every \(n\ge4\).

### 6. The circle boundary

On \(S^1\), \(\cos(2\theta)\) is a valid positive-definite zonal basis kernel. For every \(n\ge3\), its Bernstein image at the orthogonal angle has value
\[
\mathcal B_n[\cos(2\theta)](\pi/2)=-\cos(\pi/n)^n<0.
\]
It cannot lie in \(\Psi_\infty\). The result for \(n\le2\) was proved above, completing the circle classification.

## Verification

Run `python3 check.py` from the directory containing this document. The executable checker uses only standard-library exact fractions. It confirms the first eight Legendre values, the exact integral bound \(10643/32768\), twenty-one independent arcsine-cube coefficient ratios, the complete rational cubic Bernstein identity on a fifty-case grid, and the explicit degree-four/five/circle obstructions. The **infinite** positivity and sharpness statements are proved by the analytical arguments in Steps 1–6, not by finite enumeration.

## Relationship to prior work

Otten, Nguyen and Watts (2026) establish positive-definiteness preservation by the geodesic-angle Bernstein operator on the circle at every degree, and identify a failure of the *different* affine dot-product Bernstein operator on \(S^2\); Section 4 frames the higher-dimensional question. The present result supplies a sharp universal **Hilbert-sphere lifting** threshold for the geodesic-angle operator, not merely preservation in the source dimension. Its separation between \(S^1\) and \(S^2\) at degree three is not implied by the circle theorem.

Two published results on *affine Bernstein interpolation in the dot-product variable* give sharp positivity-preservation and Hilbert-sphere lifting frontiers; their sampling nodes \(-1+2j/n\) and polynomial output in \(u\) differ from angular nodes \(j\pi/n\) and polynomial output in \(\theta\). A published result on adjustable cubic nodes on the circle establishes circle preservation, not the all-dimensional lifting conclusion or the sharp obstruction above. These distinctions concern actual mappings and hypotheses, not merely different titles. Classical Schoenberg theory and Legendre integral identities are used as tools, not claimed as new.

## Limitations

The negative witnesses for \(n\ge4\) establish failure of lifting into \(\Psi_\infty\); they do **not** establish failure of preserving positivity on \(S^2\) or in each fixed higher dimension. No claim is made about nonuniform nodes, noise stability, other positive-definite spaces, or the optimality of a broader class of Bernstein-type methods. Older approximation or covariance literature could contain an equivalent result despite the targeted comparisons.

## References

- M. Otten, N. Nguyen, T. Watts, *Preservation of Positive-Definiteness by Bernstein Operators on the Circle*, arXiv:2608.04836, first posted 2026-08-05, https://arxiv.org/abs/2608.04836 .
- I. J. Schoenberg, *Positive definite functions on spheres*, Duke Math. J. **9** (1942), 96–108.
- N. H. Bingham, *Positive definite functions on spheres*, Math. Proc. Cambridge Philos. Soc. **73** (1973), 145–156.
- T. Gneiting, *Strictly and non-strictly positive definite functions on spheres*, Bernoulli **19** (2013), 1327–1349, https://arxiv.org/abs/1111.7077 .
- *Sharp dimension–degree frontier and infinite-sphere lift for affine Bernstein kernels*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-dimension-degree-frontier-and-infinite-sphere-lift-for-aff--3785c4062726 .
- *A sharp degree frontier for affine Bernstein approximation of spherical positive-definite kernels*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-degree-frontier-for-affine-bernstein-approximation-of-sp--a8520e405e97 .
- *Quadratic rigidity and cubic node freedom for positive-definite Bernstein interpolation on the circle*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-quadratic-rigidity-and-cubic-node-freedom-for-positive-definite--b87f6c90a4aa .
