# Sharp two-anchor Gaussian–Fock interpolation and three-node collision law

## Finding

Fix \(L>0\). In the classical Gaussian Bargmann–Fock Hilbert space with kernel \(K(z,w)=\exp(z\overline w)\), let \(k_x(z)=\exp(zx-x^2/2)\) be the unit evaluation vector for real \(x\). Given evaluations at \(0\) and \(L\), the **exact worst-case unit-norm interpolation error** at any \(x\in[0,L]\) is
\[
P_L(x)=\operatorname{dist}\bigl(k_x,\operatorname{span}\{k_0,k_L\}\bigr).
\]
It has one and only one maximizer, \(x=L/2\), for every \(L>0\), and
\[
\boxed{\max_{0\le x\le L}P_L(x)=\frac{1-e^{-L^2/4}}{\sqrt{1+e^{-L^2/2}}}.}
\]
Equivalently, the determinant of the **untruncated**, unit-diagonal three-point sampling Gram matrix \(G(0,x,L)\) is uniquely maximized at the midpoint, with exact value
\[
\boxed{\max_{0\le x\le L}\det G(0,x,L)
=(1-e^{-L^2/4})^3(1+e^{-L^2/4}).}
\]
At the midpoint, put \(q=e^{-L^2/4}\). The complete three eigenvalues are
\[
\lambda_- =\frac{2+q^2-\sqrt{q^4+8q}}2,
\qquad \lambda_0=1-q^2,
\qquad \lambda_+=\frac{2+q^2+\sqrt{q^4+8q}}2;
\]
they are strictly ordered \(0<\lambda_-<\lambda_0<\lambda_+\) for finite \(L>0\).

For fixed \(0<a<1\), as \(L\downarrow0\), the three eigenvalues of \(G(0,aL,L)\), in increasing order, obey
\[
\lambda_1=\frac{a^2(1-a)^2}{4(a^2-a+1)}L^4+O_a(L^6),\qquad
\lambda_2=\frac23(a^2-a+1)L^2+O_a(L^4),\qquad
\lambda_3=3+O_a(L^2).
\]
The leading small eigenvalue coefficient is uniquely maximized over fixed \(a\in(0,1)\) at \(a=1/2\), where it equals \(1/48\). At that midpoint the squared spectral condition number of the Gram matrix satisfies
\[
\kappa_2\bigl(G(0,L/2,L)\bigr)=144L^{-4}(1+O(L^2)).
\]

## Assumptions and scope

The Fock space uses unit Gaussian scale: entire \(f\) with \(\sum_{j\ge0}|f_j|^2j!<\infty\), so \(K(z,w)=e^{z\bar w}\). The three samples are **values**, not derivative values. Their locations lie on the real axis at \(0\), \(x\), and \(L\), with \(0\le x\le L\). Endpoint equality allows repeated nodes and zero determinant. The interpolation error is the sharp supremum of \(|f(x)-\langle f,\Pi k_x\rangle|\) over \(\|f\|\le1\), where \(\Pi\) projects onto the two anchor kernels. For the collision expansion \(a\) is held fixed in \((0,1)\); its remainder is not asserted uniform up to \(a=0,1\). The condition number is the ratio of the largest and smallest **Gram** eigenvalues, not the ratio of their square roots.

## Proof

### Exact Schur complement

For real nodes \(u,v\), normalized evaluation kernels satisfy \(\langle k_u,k_v\rangle=e^{-(u-v)^2/2}\). Writing \(y=L-x\), the determinant is
\[
D_L(x)=1-e^{-x^2}-e^{-y^2}-e^{-L^2}
+2e^{-L^2+xy}.
\]
The anchor Gram determinant is \(1-e^{-L^2}\). Schur complementation therefore gives
\(P_L(x)^2=D_L(x)/(1-e^{-L^2})\).

### Strict midpoint rigidity for every separation

Write \(x=L/2+h\), \(a=L^2/2>0\), \(u=L|h|\in[0,a]\), and
\[
H(h)=e^{-h^2}\bigl(\cosh(Lh)-e^{-a}\bigr).
\]
A direct rearrangement gives
\[
D_L(L/2+h)=1-e^{-L^2}-2e^{-L^2/4}H(h).
\]
It suffices to show that \(H(h)\) strictly increases with \(|h|\) on \([0,L/2]\).
For \(h>0\), differentiating gives
\[
H'(h)=2he^{-h^2}\bigl[e^{-a}-F_a(u)\bigr],\qquad
F_a(u)=\cosh u-\frac a u\sinh u.
\]
We now prove \(F_a(u)<e^{-a}\) for every \(0\le u<a\), with the removable value \(F_a(0)=1-a\).

For \(u>0\), the derivative of \(F_a\) has the sign of \(A(u)-a\), where
\[
A(u)=\frac{u^2\sinh u}{u\cosh u-\sinh u}
=\left(\int_0^1 s\frac{\sinh(su)}{\sinh u}\,ds\right)^{-1}.
\]
The denominator is strictly positive because \(u\cosh u-\sinh u=\int_0^u t\sinh t\,dt>0\). For every \(0<s<1\), the function \(\sinh(su)/\sinh u\) is strictly decreasing in \(u>0\), since the logarithmic derivative is \(s\coth(su)-\coth u<0\); this follows from strict increase of \(v\coth v\), whose derivative is \((\sinh v\cosh v-v)/\sinh^2 v>0\). Consequently \(A(u)\) strictly increases, with \(A(0+)=3\). Moreover \(A(u)>u\), because \(\sinh u>ue^{-u}\), equivalent to \(e^{2u}>1+2u\).

It follows that, on \([0,a]\), \(F_a\) is either strictly increasing throughout or first strictly decreasing and then strictly increasing: its derivative can change sign at most once, and only from negative to positive. Its maximum is thus at an endpoint. The endpoint values are \(F_a(0)=1-a<e^{-a}\) and \(F_a(a)=e^{-a}\). Hence \(F_a(u)<e^{-a}\) for all \(u<a\). Thus \(H'(h)>0\) for \(0<h<L/2\), establishing strict midpoint maximality without a small-separation assumption.

At \(x=L/2\), the three off-diagonal Gram entries are \(e^{-L^2/8}\), \(e^{-L^2/8}\), and \(e^{-L^2/2}\). Set \(q=e^{-L^2/4}\); direct determinant evaluation gives \(D_L(L/2)=(1-q)^3(1+q)\). Since \(1-e^{-L^2}=1-q^4\), the displayed exact formula for \(P_L\) follows.

### Eigenvalues and collision scales

At the midpoint, exchange of the two endpoint vectors yields an antisymmetric eigenvector with eigenvalue \(1-q^2\). The symmetric two-dimensional block has characteristic roots \((2+q^2\pm\sqrt{q^4+8q})/2\). The inequalities \(\lambda_-<1-q^2<\lambda_+\) follow from \(\sqrt{q^4+8q}>3q^2\), equivalent to \(q>q^4\), true for \(0<q<1\).

For the general collapsing triple \((0,aL,L)\), expand the Gram entries in powers of \(L^2\). The compression of the first nonconstant term to the orthogonal complement of \((1,1,1)\) is the rank-one matrix \((P t)(Pt)^T\), where \(t=(0,a,1)^T\) and \(P=I-\mathbf1\mathbf1^T/3\). Its nonzero eigenvalue is \(\|Pt\|^2=2(a^2-a+1)/3\), proving the middle-eigenvalue expansion. A Taylor expansion of the **exact** three-by-three determinant gives
\[
\det G(0,aL,L)=\tfrac12a^2(1-a)^2L^6+O_a(L^8).
\]
Since the largest eigenvalue tends to \(3\), multiplication of eigenvalues gives the small-eigenvalue expansion stated above. Finally with \(b=a(1-a)\in(0,1/4]\), its coefficient equals \(b^2/[4(1-b)]\), strictly increasing in \(b\), which is uniquely maximized at \(a=1/2\). There the eigenvalue asymptotics are \(\lambda_1=L^4/48+O(L^6)\), \(\lambda_2=L^2/2+O(L^4)\), \(\lambda_3=3+O(L^2)\), yielding the sharp condition-number constant \(144\).

## Verification

Run `python verify.py` with `mpmath` installed. The standalone high-precision checker compares the determinant formula with the direct three-by-three kernel matrix, checks strict midpoint optimality over separated grid nodes and seven positive interval lengths, compares the exact Schur-complement expression, verifies all three midpoint eigenvalues, and checks both collapsing eigenvalue scales at fifteen parameter combinations. It records \(431\) successful checks. These finite tests are reproducibility aids: strict global monotonicity and all asymptotic statements are proved algebraically above.

## Relationship to prior work

Karvonen, Särkkä, and Tanaka, *Kernel-based interpolation at approximate Fekete points*, arXiv:1912.07316 (initial public version December 16, 2019), introduce full-kernel determinant-optimal (Fekete) interpolation nodes but their Gaussian convexity and explicit optimization, in §4.1, concern a **truncated** orthonormal expansion, rather than the exact Gaussian Gram determinant. Their §2.1 gives the power-function/Schur-complement interpretation used here; neither statement supplies the full-kernel, all-separation three-point optimality or the collision spectrum.

Escudero, Haimi, and Romero, *Multiple sampling and interpolation in weighted Fock spaces of entire functions*, arXiv:2004.12922 (initial version April 27, 2020), treat Fock sampling and interpolation via density criteria and derivative samples, not fixed three-point determinant and local spectral optimization. Narayan, Yan, and Zhou, *Optimal design for kernel interpolation: applications to uncertainty quantification*, arXiv:2104.06291 (initial version April 13, 2021), discuss greedy/discretized determinant designs and conditioning but do not give this all-parameter midpoint theorem or its sharp collision coefficients. The general kernel power-function identity, Gaussian kernel formula, and Schur complement are existing tools and are not claimed as novel.

## Limitations

The new statement is for **exactly two prescribed real anchor nodes and one real additional node** in the unit-scale Gaussian Fock kernel. It is not a theorem for arbitrary complex placement, more anchors, non-Gaussian kernels, or finite-sample noise. Optimality concerns determinant and worst-case two-anchor interpolation error; the coefficient of the smallest eigenvalue is optimized only in the fixed-fraction collision limit, and no global finite-separation condition-number optimality is claimed. The literature comparison supports originality only to the checked materials; mathematically equivalent older Gaussian-process bridge inequalities or exact one-dimensional RBF design formulas could predate this statement.

## References

1. T. Karvonen, S. Särkkä, and K. Tanaka, *Kernel-based interpolation at approximate Fekete points*, arXiv:1912.07316 (first posted 2019-12-16), especially §§2.1 and 4.1.
2. L. A. Escudero, A. Haimi, and J. L. Romero, *Multiple sampling and interpolation in weighted Fock spaces of entire functions*, arXiv:2004.12922 (first posted 2020-04-27), especially §§1–2.
3. A. Narayan, L. Yan, and T. Zhou, *Optimal design for kernel interpolation: applications to uncertainty quantification*, arXiv:2104.06291 (first posted 2021-04-13), especially §§2–4.
