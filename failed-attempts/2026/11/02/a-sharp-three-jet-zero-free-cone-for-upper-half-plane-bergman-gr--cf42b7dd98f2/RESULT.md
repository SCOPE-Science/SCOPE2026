# A sharp three-jet zero-free cone for upper-half-plane Bergman Gram kernels

## Finding
Let \(\mathbb H=\{z\in\mathbb C:\operatorname{Im}z>0\}\), and let \(A^2(\mathbb H)\) be its unweighted Bergman Hilbert space for planar Lebesgue measure. For any real \(a,b\), form the bounded evaluation functional
\[
L_{a,b,z}(f)=f(z)+a f'(z)+b f''(z)
\]
and its canonical Hermitian Gram kernel \(B_{a,b}(z,w)=L_{a,b,z}\overline{L_{a,b,w}}K_{\mathbb H}(z,w)\), with the bar indicating conjugate differentiation in the second argument. Define
\[
c_-=-\frac{3+\sqrt{30}}{14},\qquad c_+=\frac{\sqrt{30}-3}{14}.
\]
**Theorem.** For every \((a,b)\in\mathbb R^2\), \(B_{a,b}(z,w)\ne0\) for all \(z,w\in\mathbb H\) if and only if
\[
\boxed{\quad c_-a^2\le b\le c_+a^2.\quad}
\]
In the complementary parameter region, there are exactly two distinct scalar values \(u\) in the open upper half-plane for which \(B_{a,b}(z,w)=0\) whenever \(z-\overline w=u\). Each is a simple zero of the scalar kernel numerator, and every such value is attained by points \(z,w\in\mathbb H\). At either nontrivial boundary \(b=c_\pm a^2\), \(a\ne0\), the numerator instead has two distinct real roots, each double; these boundary roots are not attained. When \(a=0\), the zero-free region consists exactly of \(b=0\).

## Assumptions and scope
The coefficients \(a,b\) are **real**, the functional uses ordinary derivatives (not divided by factorials), and both evaluations occur in the upper half-plane. The associated finite sequence in the normalized differential-functional notation is \((1,a,2b,0,\ldots)\). The claim is not about the diagonal \(B_{a,b}(z,z)\), which is always positive, but about all off-diagonal pairs. Counting 'two zeros' means two values of \(u=z-\overline w\) in \(\operatorname{Im}u>0\), not just two ordered pairs of sampling points.

## Proof
The unweighted Bergman reproducing kernel is
\[
K_{\mathbb H}(z,w)=-\frac{1}{\pi(z-\overline w)^2}.
\]
Point evaluations and their first two derivatives are bounded at each interior point. Their Riesz representatives therefore exist, and their Gram kernel is exactly the mixed differential of \(K_{\mathbb H}\) stated above. In particular, it is positive definite. As an independent normalization check, the Laplace representation \(K_{\mathbb H}(z,w)=\pi^{-1}\int_0^\infty t e^{it(z-\overline w)}\,dt\) gives
\[
B_{a,b}(z,w)=\frac1\pi\int_0^\infty t\bigl((1-bt^2)^2+a^2t^2\bigr)e^{it(z-\overline w)}\,dt.
\]
The integral converges absolutely for \(z,w\in\mathbb H\), and its nonnegative spectral weight independently confirms the Gram structure.

Put \(u=z-\overline w\); then \(\operatorname{Im}u>0\). Because \(\partial_z=\partial_u\) and \(\partial_{\overline w}=-\partial_u\), the real-coefficient product of the two differential operators is
\[
(1+a\partial_u+b\partial_u^2)(1-a\partial_u+b\partial_u^2)
=1+(2b-a^2)\partial_u^2+b^2\partial_u^4.
\]
Applying this to the kernel gives the exact rational identity
\[
B_{a,b}(z,w)=-\frac{P_{a,b}(u)}{\pi u^6},\qquad
P_{a,b}(u)=u^4+(12b-6a^2)u^2+120b^2.
\]
No pole is attained because \(\operatorname{Im}u>0\). Conversely **every** \(u\) with positive imaginary part is attainable: take \(z=u/2\) and \(w=-\overline u/2\), both in \(\mathbb H\). Thus the full two-variable zero problem is precisely the upper-half-plane root problem for this even, real polynomial.

Set \(y=u^2\). Its roots obey
\[
y^2+(12b-6a^2)y+120b^2=0,
\]
whose discriminant is
\[
\Delta=12(3a^4-12a^2b-28b^2).
\]
As \(P_{a,b}\) has real coefficients, it has no root with positive imaginary part exactly when all of its roots are real: every nonreal root is accompanied by its conjugate. This happens exactly when both \(y\)-roots are real and nonnegative. For \(b\ne0\), their product is \(120b^2>0\), and the two roots are real and positive precisely when \(\Delta\ge0\) and their sum \(6a^2-12b>0\). Solving \(\Delta\ge0\) yields
\[
-\frac{3+\sqrt{30}}{14}a^2\le b\le\frac{\sqrt{30}-3}{14}a^2,
\]
and that interval automatically implies \(6a^2-12b>0\) when \(a\ne0\), because \(c_+<1/2\). If \(b=0\), \(P_{a,0}(u)=u^2(u^2-6a^2)\), with only real roots. If \(a=0\) and \(b\ne0\), \(\Delta=-336b^2<0\). This proves the zero-free equivalence including the origin.

For parameters outside the closed cone, \(\Delta<0\) and \(b\ne0\). The two \(y\)-roots are distinct nonreal conjugates. Their four square roots are distinct and nonreal, exactly two in the open upper half-plane, proving the exact zero count and simplicity. At either boundary with \(a\ne0\), \(\Delta=0\), \(b\ne0\), and the unique \(y\)-root \(3a^2-6b\) is positive. Therefore \(P\) is the square of \(u^2-(3a^2-6b)\), giving precisely two real double roots; these remain outside the domain. This completes the classification.

## Verification
For reproducibility, run `python3 check.py` with the standard-library Python interpreter. The checker reconstructs all coefficients of the mixed-derivative numerator using exact integers, verifies the discriminant factor and the algebraic threshold identities using `fractions.Fraction`, and tests representative inside, outside, and boundary parameters by direct complex polynomial substitution. The symbolic proof above establishes the theorem for **all** real coefficients; finite representative tests are not an exhaustive proof.

## Relationship to prior work
Gehlawat–Jain–Sarkar (2026) introduced the canonical positive-definite Gram kernel for differential evaluations, gave its general derivative representation, and studied special pure-jet and exponential sequences on \(\mathbb H\). The present result uses that setting but identifies a different, exact **three-term real coefficient region**. The publicly recorded two-term value/first-derivative Lu Qi-Keng classification concerns \(b=0\); the separated value/second-derivative result concerns \(a=0\). Neither one implies the nonempty two-dimensional cone for \(a b\ne0\). The first nontrivial interplay of all three levels leads to the asymmetric quadratic boundary \(c_-a^2\le b\le c_+a^2\), instead of the one-coefficient half-plane condition. The general extremal theory of Bao–Guan–Sun (2025) does not explicitly supply these three-jet zero locations.

## Limitations
Only the real two-parameter coefficient family, the unweighted upper half-plane, and ordinary derivatives of orders zero through two are classified. The polynomial method extends to complex coefficients or higher jets, but no classification in those settings is asserted. On the boundary the accessible kernel is still zero-free, although real repeated roots of the auxiliary polynomial occur at unattainable points. No claim of independent verification or exhaustive originality search is made.

## References
1. S. Gehlawat, A. Jain, A. D. Sarkar, *A Canonical Positive Definite Kernel Associated with the ξ-Bergman Kernel*, arXiv:2608.13193 (first posted 2026-08-13), especially Sections 2 and 4, https://arxiv.org/abs/2608.13193.
2. S. Bao, Q. Guan, X. Sun, *On the p-Bergman kernel with respect to a functional ξ*, arXiv:2510.13144 (first posted 2025-10-15), https://arxiv.org/abs/2510.13144.
3. *Exact two-jet Lu Qi-Keng phase for the canonical ξ-Bergman Gram kernel*, published mathematical record `364c00673845` (2026).
4. *Parity law for zeros of separated weighted Bergman jet Gram kernels*, published mathematical record `48a4d84c1cc7` (2026).
