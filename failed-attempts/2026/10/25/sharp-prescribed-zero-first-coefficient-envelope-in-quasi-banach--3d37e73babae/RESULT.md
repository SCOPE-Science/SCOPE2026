# Sharp prescribed-zero first-coefficient envelope in quasi-Banach Hardy spaces

## Finding
Fix \(0<p<1\) and put \(q=2/p>2\). For \(0\le\rho\le1\), define \(t_q(0)=0\) and, for \(0<\rho\le1\), let \(t_q(\rho)\) be the unique nonnegative solution of
\[
(q-1)\rho t^2+(1-\rho^2)t-\rho=0.
\]
Define
\[
\mathcal C_q(\rho)=\frac{1-\rho^2+q\rho t_q(\rho)}{(1+t_q(\rho)^2)^{q/2}}.
\]
For every \(f\in H^p(\mathbb D)\) with \(\|f\|_{H^p}=1\) and canonical inner–outer factorization \(f=IF\), where \(\rho=|I(0)|\), the sharp conditional inequality is
\[
|f'(0)|\le\mathcal C_q(\rho).
\]
For \(0\le\rho<1\), equality holds if and only if, for unimodular \(\lambda,\eta\),
\[
f(z)=\lambda\,\frac{\rho+\eta z}{1+\rho\eta z}
\left(\frac{1+t_q(\rho)\eta z}{\sqrt{1+t_q(\rho)^2}}\right)^q.
\]
For \(\rho=1\), the inner factor is constant and equality holds exactly for \(f(z)=\lambda[(1+(q-1)^{-1/2}\eta z)/\sqrt{1+(q-1)^{-1}}]^q\). The fractional powers are defined by their analytic logarithms, normalized to be positive at zero.

The profile \(\mathcal C_q\) is strictly increasing on \([0,1]\), with \(\mathcal C_q(0)=1\) and
\[
\mathcal C_q(1)=\sqrt q\left(\frac{q-1}{q}\right)^{(q-1)/2}.
\]
It has sharp endpoint expansions
\[
\mathcal C_q(\rho)=1+\left(\frac q2-1\right)\rho^2+O_q(\rho^4)\quad(\rho\downarrow0),
\]
\[
\mathcal C_q(1)-\mathcal C_q(\rho)=\left(\frac q{\sqrt{q-1}}-2\right)
\left(\frac{q-1}{q}\right)^{q/2}(1-\rho)+O_q((1-\rho)^2)
\quad(\rho\uparrow1).
\]

In particular, for every fixed \(a\in\mathbb D\), the **exact prescribed-zero coefficient bound** is
\[
\sup_{\substack{f\in H^p,\ \|f\|_{H^p}=1\\f(a)=0}}|f'(0)|=\mathcal C_q(|a|).
\]
For \(a\ne0\), equality requires the single Blaschke factor with zero \(a\), and the outer factor indicated above with \(\eta=-|a|/a\). For \(a=0\), the equality family is \(f(z)=\lambda z\). No other equality cases occur.

## Assumptions and scope
The Hardy quasi-norm is \(\|f\|_{H^p}=\sup_{0<r<1}(\int_0^{2\pi}|f(re^{i\theta})|^p\,d\theta/(2\pi))^{1/p}\); the standard inner–outer factorization is unique up to a unimodular scalar. The theorem covers every real \(p\) strictly between zero and one, every normalized nonzero \(f\), every \(\rho\in[0,1]\), and every \(a\in\mathbb D\). The first coefficient is \(f'(0)\). The conditional parameter is the modulus of the **entire inner factor at the origin**, not \(|f(0)|\). The endpoint \(\rho=1\) means the inner factor is unimodular constant.

## Proof
Let \(f=IF\), \(\rho=|I(0)|\), and \(G=F^{1/q}\). An outer function is zero-free, so this power is analytic. Since \(qp=2\), \(\|G\|_{H^2}=\|f\|_{H^p}^{1/q}=1\). Write \(x=|G(0)|>0\) and \(y=|G'(0)|\). Parseval gives \(x^2+y^2\le1\). Schwarz–Pick gives \(|I'(0)|\le1-\rho^2\). By the product and chain rules,
\[
|f'(0)|\le(1-\rho^2)x^q+q\rho x^{q-1}y
\le(1-\rho^2)x^q+q\rho x^{q-1}\sqrt{1-x^2}.
\]
Set \(t=\sqrt{x^{-2}-1}\ge0\). The last expression becomes
\[
\Phi_{q,\rho}(t)=\frac{1-\rho^2+q\rho t}{(1+t^2)^{q/2}}.
\]
For \(\rho>0\), differentiation shows that the sign of \(\Phi'_{q,\rho}(t)\) is the sign of
\[
P_{q,\rho}(t)=\rho-(1-\rho^2)t-(q-1)\rho t^2.
\]
This quadratic strictly decreases on the nonnegative half-line, starts positive, and tends to \(-\infty\). Consequently its unique positive zero is the unique global maximum of \(\Phi\). For \(\rho=0\), \(\Phi_{q,0}(t)=(1+t^2)^{-q/2}\) is uniquely maximized at \(t=0\). The positive root satisfies \(0<t_q(\rho)\le1/\sqrt{q-1}<1\), the latter inequality following by testing the quadratic at \(1/\sqrt{q-1}\).

For \(0<\rho<1\), equality in Schwarz–Pick forces \(I\) to be a degree-one disk automorphism; equality in Parseval forces \(G\) to have no coefficients of order two or higher. Equality in the triangle inequality aligns the phases of the two derivative contributions. These constraints give precisely
\[
I(z)=\lambda_0\frac{\rho+\eta z}{1+\rho\eta z},\qquad
G(z)=\lambda_1\frac{1+t_q(\rho)\eta z}{\sqrt{1+t_q(\rho)^2}}.
\]
Since \(t_q(\rho)<1\), this \(G\) is outer. Its normalized boundary modulus implies \(\|I G^q\|_{H^p}^p=\|G\|_{H^2}^2=1\); direct differentiation gives equality. At \(\rho=0\), equality forces \(I(z)=\lambda_0 z\) and \(G\) constant. At \(\rho=1\), the maximum-modulus principle forces \(I\) constant; equality reduces to the normalized degree-one \(G\) with \(t=1/\sqrt{q-1}\). This establishes the complete equality classification.

For strict monotonicity, the envelope derivative for \(0<\rho\le1\) is
\[
\mathcal C_q'(\rho)=\frac{qt_q(\rho)-2\rho}{(1+t_q(\rho)^2)^{q/2}}.
\]
Writing \(R_{q,\rho}(t)=(q-1)\rho t^2+(1-\rho^2)t-\rho\), an exact calculation gives
\[
R_{q,\rho}(2\rho/q)=-\frac{\rho(q-2)(q-2\rho^2)}{q^2}<0.
\]
Since \(R_{q,\rho}\) strictly increases at nonnegative \(t\), its zero satisfies \(t_q(\rho)>2\rho/q\). Thus the derivative is positive for \(\rho>0\), and continuity handles the left endpoint. At \(\rho=1\), the quadratic gives \(t_q(1)=(q-1)^{-1/2}\) and the displayed exact \(\mathcal C_q(1)\). Implicit-function expansion at \(\rho=0\) gives \(t_q(\rho)=\rho+O_q(\rho^3)\), yielding the first expansion. Analyticity around \(\rho=1\) and the envelope derivative yield the second expansion. Its coefficient is positive since \(q^2>4(q-1)\) for \(q>2\).

Finally, if \(f(a)=0\), factor \(I=B_a J\), where \(B_a\) is the degree-one Blaschke factor with zero \(a\) and \(J\) is inner. Then \(|I(0)|=|a||J(0)|\le|a|\). Strict monotonicity gives \(|f'(0)|\le\mathcal C_q(|I(0)|)\le\mathcal C_q(|a|)\). Equality, when \(a\ne0\), forces \(J\) to be constant by maximum modulus, and the established equality family applies with \(\eta=-|a|/a\). At \(a=0\), the first equality classification gives exactly \(\lambda z\). This proves the prescribed-zero statement.

## Verification
The separate reproducibility artifact `verify.py` uses only Python's standard library. Running `python verify.py` returns `CHECK_OK: 80 analytic-parameter grids, 25 exact rational monotonicity certificates, endpoint tests`. It tests the quadratic stationarity, its positive root, normalization and derivative of the exhibited optimizer, strict increase on representative grids, exact rational factorization of the monotonicity witness, and the two endpoint coefficients. These finite checks corroborate formula algebra only. The global theorem follows from the Hardy factorization, Schwarz–Pick equality, Parseval, and strictly monotone quadratic, independent of testing.

For example, at \(p=1/2\), \(q=4\), and \(\rho=1/2\), the optimizer parameter solves \(6t^2+3t-2=0\), namely \(t=(\sqrt{57}-3)/12\approx0.379152869606\). The sharp conditional coefficient is \(\mathcal C_4(1/2)\approx1.152980415771\).

## Relationship to prior work
Brevig and Søvik [1] prove the qualitative theorem that norm-attaining bounded linear functional extremizers on \(H^p\), \(0<p<1\), must be outer. The present sharp prescribed-zero and fixed-inner-modulus coefficient profile quantifies the loss when a nontrivial inner factor is forced, identifying all conditional extremizers.

Brevig, Grepstad, and Instanes [2, Section 4] solve a related but distinct coefficient problem conditioned on the **entire value** \(f(0)\), not on \(|I(0)|\) or a specified zero. For their zero-containing branch the outer linear parameter equals the Blaschke parameter; for the present fixed-inner-modulus optimum, it instead solves a different quadratic and generally differs from the inner parameter (already at \(p=1/2\), \(\rho=1/2\)). Their theorem therefore does not state this conditional optimum or its zero-location corollary. The unrestricted sharp coefficient \(\mathcal C_q(1)\) is previously known and is not claimed new [3]. No claim of absolute historical priority is made.

## Limitations
The result concerns the first Taylor coefficient in one complex variable, \(0<p<1\), and a fixed modulus of the inner factor at zero or a prescribed interior zero. It does not give a stability distance between a near-extremizer and the equality family, nor extend the exact formula to higher Taylor coefficients. Pre-2026 coefficient-interpolation literature and potentially unindexed results on conditioned inner divisors may contain equivalent special cases; absence of a database match is not a proof of historical uniqueness. The source paper [1] motivates the quantitative question, but the proof above is separate.

## References
[1] O. F. Brevig and Ø. Søvik, *Extremals for linear functionals on H^p are outer when 0<p<1*, arXiv:2610.21788v1 (first public 2026-10-15), https://arxiv.org/abs/2610.21788.

[2] O. F. Brevig, S. Grepstad, and S. M. Instanes, *F. Wiener's Trick and an Extremal Problem for H^p*, arXiv:2011.07790 (first public 2020-11-16), https://arxiv.org/abs/2011.07790; freely accessible full text https://link.springer.com/article/10.1007/s40315-022-00469-x.

[3] O. F. Brevig and E. Saksman, *Coefficient estimates for H^p spaces with 0<p<1*, arXiv:1905.09547 (first public 2019-05-23), https://arxiv.org/abs/1905.09547.
