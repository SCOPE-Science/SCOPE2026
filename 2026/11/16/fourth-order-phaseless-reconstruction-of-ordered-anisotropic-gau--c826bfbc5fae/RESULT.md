# Fourth-order phaseless reconstruction of ordered anisotropic Gaussian pairs, with a sharp planar obstruction

## Finding

Let \(d\ge3\). A sum of two unit-mass multivariate Gaussian densities with arbitrary centers and **strictly Loewner-ordered covariance matrices** is determined, up to translation, reflection, and interchange of components, by the value and the complete derivatives of orders two and four at the origin of its Fourier intensity. The result is global, includes coincident centers, and requires no upper bound on center separation. Order four is necessary. The dimension bound is sharp for this data: in \(d=2\) there are noncongruent strictly covariance-ordered pairs with identical complete intensity jets through degree four.

Here the strict-order hypothesis means that the two real symmetric positive definite covariance matrices \(A,B\) can be labeled so that \(A-B\) is positive definite. The Fourier convention is \(\widehat f(\xi)=\int_{\mathbb R^d} f(x)e^{-i\xi\cdot x}\,dx\). We make no claim about unrestricted covariance pairs, arbitrary unequal mixture weights, stability under measurement noise, or sufficiency of sixth-order data in dimension two.

## Assumptions and scope

For a symmetric positive definite \(d\times d\) matrix \(C\), write
\[
g_C(x)=(2\pi)^{-d/2}(\det C)^{-1/2}\exp\!\left(-\tfrac12 x^T C^{-1}x\right).
\]
Take \(c_1,c_2\in\mathbb R^d\) and \(A,B\succ0\) such that, after possibly exchanging labels, \(A-B\succ0\). Set
\[
f(x)=g_A(x-c_1)+g_B(x-c_2),\qquad I(\xi)=|\widehat f(\xi)|^2.
\]
The data comprise \(I(0)\), the entire symmetric Hessian \(D^2 I(0)\), and the entire symmetric fourth derivative tensor \(D^4 I(0)\); odd derivatives vanish. The known unit component masses give \(I(0)=4\). Unavoidable invariances are common translation of both centers, simultaneous reflection of both centers, and interchange of the component labels. A linear orthogonal rotation of physical coordinates is **not** an allowed ambiguity because the intensity is measured in fixed coordinates.

Introduce homogeneous quadratic forms and a linear form, all in the frequency variable:
\[
S(\xi)=\tfrac12\xi^T(A+B)\xi,\qquad
Q(\xi)=\tfrac12\xi^T(A-B)\xi,\qquad
H(\xi)=(c_1-c_2)\cdot\xi.
\]
We use the ordering \(Q\succ0\). The polynomial \(H^2\) determines the center-difference vector up to its sign.

## Proof

**1. Exact intensity and fourth cumulant.** The Gaussian Fourier formula gives
\[
I(\xi)=2e^{-S(\xi)}\bigl(\cosh Q(\xi)+\cos H(\xi)\bigr).
\]
As \(I(0)=4\), the real logarithm \(\log(I/4)\) is analytic near the origin. Define its homogeneous Taylor terms of degrees two and four by
\[
\log(I(\xi)/4)=L_2(\xi)+L_4(\xi)+O(|\xi|^6).
\]
Direct expansion, respecting that \(S,Q\) have degree two while \(H\) has degree one, gives the exact identities
\[
L_2=-S-\tfrac14 H^2,\qquad
L_4=\tfrac14 Q^2-\tfrac1{96}H^4.
\]
Consequently the measured derivatives determine
\[
M:=-L_2=S+\tfrac14H^2,\qquad
T:=4L_4=Q^2-R^2,
\quad R:=\frac{H^2}{\sqrt{24}}.
\]
In particular, \(R\) is either zero or a positive semidefinite rank-one quadratic form, and the measured quartic is a product
\[
T=(Q+R)(Q-R).
\]

**2. Factorization rigidity in dimensions at least three.** Let \(Q\) be a positive definite real quadratic form on \(\mathbb R^d\), \(d\ge3\), and \(R\) a nonnegative rank-one quadratic form. If \(R\ne0\), then \(Q+R\) is positive definite. By the rank-one perturbation principle, \(Q-R\) has at least \(d-1\) strictly positive eigenvalues; it is positive definite, has exactly one negative eigenvalue, or is positive semidefinite of rank \(d-1\). Both \(Q+R\) and \(Q-R\) are irreducible quadratic polynomials over \(\mathbb R\): a product of real linear forms is either rank one or is indefinite on the span of its two nonproportional factors; neither alternative is compatible with the stated signatures and ranks (an indefinite rank-two possibility is excluded because there are at least two positive directions). They are not associates because \(R\ne0\) and \(\operatorname{rank}Q=d\).

Unique factorization of \(\mathbb R[\xi_1,\ldots,\xi_d]\) therefore determines these two factors from \(T\) up to nonzero scalar rescalings and interchange. Because they are distinct irreducible factors, \(T\) is not a polynomial square, so a competing decomposition with \(R'=0\) is impossible. Suppose a second decomposition \(T=(Q'+R')(Q'-R')\) has \(Q'\succ0\) and \(R'\succeq0\) of rank one. After assigning the two irreducible factors, it has
\[
Q'+R'=t(Q+R),\qquad Q'-R'=t^{-1}(Q-R)
\]
for some real \(t\ne0\), or the two right sides interchanged. Since \(Q'\) and \(Q\) are positive on the \((d-1)\)-dimensional kernel of \(R\), necessarily \(t>0\). Subtraction gives, in the first assignment,
\[
2R'=(t-t^{-1})Q+(t+t^{-1})R.
\]
Whenever \(t\ne1\), the right side is a nonzero scalar multiple of an invertible rank-\(d\) matrix plus a rank-one matrix, and therefore has rank at least \(d-1\ge2\). Since \(R'\) has rank one, \(t=1\), giving \(Q'=Q\), \(R'=R\). In the exchanged assignment the same argument forces \(t=1\) and yields \(R'=-R\), impossible for a nonzero \(R\succeq0\). Thus \(Q,R\) are unique.

If \(R=0\), the quartic \(T=Q^2\) is a square of one positive definite irreducible quadratic. A competing decomposition with nonzero rank-one \(R'\) would factor into two distinct irreducible quadratics and cannot equal the square. The unique positive definite square root of \(T\) is \(Q\). This also treats coincident centers.

**3. Reconstruction.** Factor the observed homogeneous quartic \(T\) over the reals and impose the positivity, rank-one difference and product normalizations from step 2. This uniquely recovers \(Q\) and \(R\). Then
\[
H^2=\sqrt{24}\,R,\qquad
S=M-\tfrac14H^2,\qquad
\xi^TA\xi=S(\xi)+Q(\xi),\quad
\xi^TB\xi=S(\xi)-Q(\xi).
\]
The nonnegative rank-one polynomial \(H^2\) identifies \(c_1-c_2\) up to sign. This recovers the unordered covariance pair and center separation modulo the claimed invariances. The reasoning applies even when the two centers coincide and does not require a separation hypothesis.

**4. Why order four is necessary.** For any \(d\ge3\), choose \(H=0\), \(S(\xi)=5|\xi|^2\) and either \(Q_1(\xi)=|\xi|^2\) or \(Q_2(\xi)=2|\xi|^2\). All four forms \(S\pm Q_j\) are positive definite, and both pairs are strictly ordered. They share \(I(0)\) and the complete second-order intensity jet because \(L_2=-S\), but their fourth-order terms differ because \(L_4=Q_j^2/4\). Thus order two is insufficient in the stated model class; odd jets are identically zero.

**5. Sharp planar obstruction.** In two variables \((u,v)\), put
\[
Q_1=u^2+v^2,\quad R_1=\tfrac35u^2,\qquad
Q_2=\tfrac45u^2+\tfrac54v^2,\quad R_2=\tfrac34v^2.
\]
The exact identity
\[
(Q_1+R_1)(Q_1-R_1)
=\bigl(\tfrac85u^2+v^2\bigr)\bigl(\tfrac25u^2+v^2\bigr)
=\bigl(\tfrac45u^2+\tfrac12v^2\bigr)\bigl(\tfrac45u^2+2v^2\bigr)
=(Q_2+R_2)(Q_2-R_2)
\]
shows identical fourth logarithmic jets. Choose real linear forms \(H_j\) satisfying \(H_j^2=\sqrt{24}\,R_j\), and set
\[
S_1=10(u^2+v^2),\qquad S_2=S_1+\tfrac14(H_1^2-H_2^2).
\]
Then \(S_1+H_1^2/4=S_2+H_2^2/4\), so the second logarithmic jets also agree. All \(S_j+Q_j\) and \(S_j-Q_j\) are positive definite: they are diagonal, with diagonal coefficients bounded below by \(8\) (for \(j=1\)) or by \(10-3\sqrt6/8-5/4>7\) (for \(j=2\)). Hence both examples correspond to genuine Gaussian pairs with strictly positive definite covariance differences. Their center separations are nonzero and lie on perpendicular axes and their covariance differences are distinct, so they are not related by translation, reflection or component exchange. Equality of both logarithmic jets implies equality of the full intensity jets through degree four. This proves the sharp dimension boundary for the stated finite data.

## Verification

The accompanying \(checker.py\) is standalone Python/SymPy code that verifies the degree-two and degree-four logarithmic expansions, the exact planar factor identity, all four planar positive-definiteness tests, one three-dimensional rank-one factor test, and the strict lower-order counterexample. Run `python checker.py` with SymPy installed. Its finite symbolic examples are supplemental evidence; the all-dimensions conclusion rests on the factorization and rank proof above.

## Relationship to prior work

The June 22, 2026 article *The kurtosis of normal variance-mean mixtures* by F. Javed analyzes fourth-cumulant tensors for a scalar mean–variance mixing model; its two-support Gaussian specialization has proportional covariance matrices and it develops forward kurtosis and projection-pursuit formulas, rather than phaseless recovery of arbitrary strictly ordered covariance matrices or a sharp planar obstruction [1]. The October 29, 2026 article *Phase Retrieval of Bandlimited Signals Using a Morlet Wavelet and an Admissible Companion* by Liu, Ning, Wu and Zhang proves uniqueness from two families of sampled wavelet magnitudes for one-dimensional bandlimited signals, not a finite Fourier-intensity jet of Gaussian pairs [2].

Blomenhofer, Casarotti, Michałek and Oneto analyze generic identification of centered Gaussian mixtures from sixth-order ordinary mixture moments, via sums of powers of quadratic forms [3]; the present data are the even derivatives of an autocorrelation characteristic function and permit nonzero unknown center separation. Agostini, Améndola and Ranestad analyze homoscedastic mixture moments and an ordinary-moment order-four recovery, with equal component covariance matrices [4]. Neither assumption set or observed statistic directly includes the theorem above. Classical identifiability of full Gaussian mixtures from their entire densities does not imply finite-jet phaseless identifiability.

## Limitations

The strict Loewner-order assumption is substantive; the result does not address incomparable covariance matrices or unequal masses. The reconstruction is algebraic and no quantitative stability constant is established near nearly coincident covariance matrices or small separation. In dimension two the explicit counterexample concerns complete order-four data only, not the full intensity function or higher jets. Related statistical cumulant decomposition and autocorrelation literature remains a plausible source of an equivalent formulation, so publication-priority claims require an additional independent literature assessment. No independent validation is claimed.

## References

1. F. Javed, *The kurtosis of normal variance-mean mixtures*, first posted 2026-06-22, arXiv:2606.22951, https://arxiv.org/abs/2606.22951 .
2. B. Liu, M. Ning, L. Wu, and Q. Zhang, *Phase Retrieval of Bandlimited Signals Using a Morlet Wavelet and an Admissible Companion*, first posted 2026-10-29, arXiv:2610.39145, https://arxiv.org/html/2610.39145v1 .
3. A. Taveira Blomenhofer, A. Casarotti, M. Michałek, and A. Oneto, *Identifiability for mixtures of centered Gaussians and sums of powers of quadratics*, Bull. Lond. Math. Soc. 55 (2023), https://doi.org/10.1112/blms.12871 .
4. D. Agostini, C. Améndola, and K. Ranestad, *Moment Identifiability of Homoscedastic Gaussian Mixtures*, Found. Comput. Math. 21 (2021), https://doi.org/10.1007/s10208-020-09469-6 .
