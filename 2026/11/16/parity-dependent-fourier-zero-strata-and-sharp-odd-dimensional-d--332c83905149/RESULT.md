# Parity-dependent Fourier zero strata and sharp odd-dimensional demicube zero radii

## Finding

Let \(d\ge3\) be an integer, \(a>0\), and let the *demicube vertex measure* be
\[
\mu_{d,a}=2^{1-d}\sum_{\substack{\varepsilon\in\{-1,1\}^{d}\\\prod_{j=1}^{d}\varepsilon_j=1}}\delta_{a\varepsilon}.
\]
Use the Euclidean Fourier convention \(\widehat\mu(\xi)=\int e^{-2\pi i\xi\cdot x}\,d\mu(x)\), and write \(Z_{d,a}=\{\xi\in\mathbb R^d:\widehat\mu_{d,a}(\xi)=0\}\).

**Odd dimensions.** If \(d\ge3\) is odd, the complete real zero set is
\[
\boxed{Z_{d,a}=\bigcup_{j\ne k}\ \bigcup_{m,n\in\mathbb Z}
\left\{\xi:\xi_j=\frac{m+1/2}{2a},\quad \xi_k=\frac{n}{2a}\right\}.}
\]
Consequently \(Z_{d,a}\) is a locally finite union of affine codimension-two flats, of Hausdorff dimension exactly \(d-2\). Its sharp distance from the origin is
\[
\boxed{\operatorname{dist}(0,Z_{d,a})=\frac{1}{4a},\qquad
Z_{d,a}\cap\left\{|\xi|=\frac{1}{4a}\right\}
=\left\{\frac{\pm e_j}{4a}:1\le j\le d\right\}.}
\]
The support diameter is \(D=2a\sqrt{d-1}\), and hence the scale-invariant zero-free radius satisfies
\[
\boxed{D\operatorname{dist}(0,Z_{d,a})=\frac{\sqrt{d-1}}2.}
\]
For \(d=3\) this describes the six closest zeros of the equally weighted regular-tetrahedron vertex transform, and the entire zero set is a union of three families of orthogonal line lattices.

**Even dimensions.** If \(d\ge4\) is even, \(Z_{d,a}\) contains a smooth real-analytic hypersurface patch consisting of zeros with **no** coordinate satisfying either a sine or cosine zero condition. In particular, its real zero-set dimension is \(d-1\), rather than \(d-2\). This is a genuine parity change in the geometry of Fourier cancellation for the same natural vertex family.

## Assumptions and scope

Each atom has mass \(2^{1-d}\), so the total mass is one. The support is the parity-selected half of the \(d\)-dimensional sign cube (also called a demihypercube). The parameter \(a\) scales physical positions, while \(\xi\) is measured in cycles per unit length. The two parts refer to different dimensions and use the same definition of \(\mu_{d,a}\). Statements about zeros always refer to *real* frequency vectors. The even-dimensional assertion establishes a hypersurface stratum but does not assert that every even-dimensional zero lies on it.

## Proof

**Character-parity factorization.** Put \(\theta_j=2\pi a\xi_j\). The parity indicator on the sign cube is
\[
\mathbf1_{\{\prod\varepsilon_j=1\}}=\frac{1+\prod_j\varepsilon_j}{2}.
\]
Expanding the two products gives the exact identity, for all integers \(d\ge3\),
\[
\widehat\mu_{d,a}(\xi)
=\prod_{j=1}^{d}\cos\theta_j+(-i)^d\prod_{j=1}^{d}\sin\theta_j.\tag{1}
\]
Indeed \(\frac12\sum_{\varepsilon=\pm1}e^{-i\varepsilon\theta}=\cos\theta\) and \(\frac12\sum_{\varepsilon=\pm1}\varepsilon e^{-i\varepsilon\theta}=-i\sin\theta\). The normalization in the definition of \(\mu_{d,a}\) cancels the half-cube cardinality exactly; at \(\xi=0\) both sides of (1) equal one.

**Odd dimensions: all zeros.** When \(d\) is odd, \((-i)^d\) is purely imaginary. The two products in (1) are real; the complex sum therefore vanishes precisely when *both* products vanish. A cosine factor vanishes exactly when \(\theta_j\in\pi(\mathbb Z+1/2)\); a sine factor vanishes exactly when \(\theta_k\in\pi\mathbb Z\). They cannot vanish in the same coordinate, so \(j\ne k\). Solving for the frequencies gives the displayed complete union of codimension-two flats. This union is locally finite because only finitely many relevant integers fit in any bounded frequency box; it contains a full affine flat and no open hypersurface, proving its Hausdorff dimension is \(d-2\).

Every zero contains at least one cosine-zero coordinate, so \(|\theta|\ge\pi/2\), equivalent to \(|\xi|\ge1/(4a)\). Equality forces exactly one nonzero coordinate, equal to \(\pm\pi/2\); any other coordinate has sine zero because \(d\ge3\). Thus the \(2d\) stated points are precisely all closest zeros. Two allowed sign vertices differ in an even number of coordinates; since \(d\) is odd, their maximum possible Hamming distance is \(d-1\), attained by choosing the second sign vector to reverse all but one coordinate. Their Euclidean diameter is therefore \(2a\sqrt{d-1}\), yielding the scale-free formula.

**Even dimensions: genuine hypersurface cancellation.** When \(d\) is even, equation (1) is the real-valued analytic function
\[
F(\theta)=\prod_j\cos\theta_j+(-1)^{d/2}\prod_j\sin\theta_j.
\]
Choose signs \(s_j\in\{-1,1\}\) satisfying \(\prod_j s_j=(-1)^{d/2+1}\), and let \(\theta_j=s_j\pi/4\). Every sine and cosine factor is nonzero and the two terms cancel. At that point,
\[
\frac{\partial F}{\partial\theta_j}=-2s_j\,2^{-d/2}\ne0.
\]
The implicit-function theorem supplies a smooth real-analytic \((d-1)\)-dimensional zero hypersurface around each of these points, with no coordinate sine/cosine zero in a sufficiently small neighborhood. Since \(F\) is nonzero at the origin, its entire zero set has empty interior; analyticity bounds its real dimension by \(d-1\). This proves the stated parity change and completes the theorem.

## Verification

The algebraic expansion in (1), the exact sine/cosine zero conditions, the diameter computation, and the nonvanishing derivative are the complete analytical verification; no finite sample is used as an infinite-dimensional proof. Independent arithmetic sanity checks of the product formula compared the direct \(2^{d-1}\)-term exponential sum with the factored expression at 30 deterministic random phase vectors in each dimension \(3\le d\le9\), and tested the constructed zeros. Every check passed at numerical tolerance \(10^{-12}\). The exact identities, not these numerical tests, establish all quantified statements.

## Relationship to prior work

Gómez-Serrano, Levitin, Platt and Polterovich (2026) study the nearest Fourier zeros of *Lebesgue indicator functions of convex bodies*, with a sharp distinction between planar and higher-dimensional geometric behavior. That work motivates asking for a natural zero-radius invariant, but it does not treat atomic vertex measures or parity-selected demicube zero strata. Its primary objects, normalization and quantifiers are different.

The exact parity projector on Boolean sign cubes is classical. Related published work on affine Walsh projection norms on even-parity sign cubes addresses endpoint operator norms, rather than Euclidean Fourier transforms of the corresponding atomic vertex measures. Related classifications of sparse Fourier zeros on finite cyclic product groups concern finite character grids, not continuous-frequency real zero varieties. In particular their conclusions cannot supply the codimension jump and the sharp Euclidean first-zero directions above without an additional argument. The new claim is the combined all-dimensional zero-set geometry and scale-free odd-dimensional extremal formula, not the parity-indicator identity alone.

## Limitations

The even-dimensional theorem shows a smooth hypersurface stratum but does not provide a complete even-dimensional zero-set classification or its smallest zero radius. Only equal positive masses at the half-cube vertices are covered; perturbing masses or vertex locations is outside scope. The proof is elementary once the parity factorization is identified, and an equivalent identity or zero-set description may occur in older coding-theory, probability or polytope Fourier literature under different terminology. No independent audit is claimed.

## References

1. J. Gómez-Serrano, M. Levitin, D. Platt, I. Polterovich, *An isoperimetric problem for Fourier zeros of centrally symmetric convex bodies*, arXiv:2609.10517v1, first made public 9 September 2026, especially §§1–3, https://arxiv.org/abs/2609.10517.
2. *A four-phase parity defect in sharp affine Fourier projection norms*, public mathematical record, 26 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-four-phase-parity-defect-in-sharp-affine-fourier-projection-no--c1a2f4dd20fe.
3. *Phase-only Fourier-zero spectrum of a four-point rectangle on cyclic product groups*, public mathematical record, 4 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-phase-only-fourier-zero-spectrum-of-a-four-point-rectangle-on-cy--b51ecb1779fe.
4. R. de Wolf, *A Brief Introduction to Fourier Analysis on the Boolean Cube*, Theory of Computing Library, Graduate Surveys 1 (2008), https://theoryofcomputing.org/articles/gs001/.
