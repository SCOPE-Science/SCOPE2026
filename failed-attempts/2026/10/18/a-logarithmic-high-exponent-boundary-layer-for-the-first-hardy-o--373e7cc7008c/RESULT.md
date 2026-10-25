# A logarithmic high-exponent boundary layer for the first Hardy optimal polynomial inverse of \(1-z\)

## Finding
Let \(1<p<\infty\), and equip \(H^p(\mathbb D)\) with normalized boundary norm
\[
\|h\|_{H^p}^p=\frac1{2\pi}\int_0^{2\pi}|h(e^{i\theta})|^p\,d\theta.
\]
The unique polynomial \(Q_p\) of degree at most one minimizing \(\|1-(1-z)Q\|_{H^p}\) has the form
\[
 Q_p(z)=\frac{1+t_p+z}{2+t_p},
 \qquad t_p>0.
\]
Here \(t_p\) is the unique positive solution of
\[
 \int_{-1}^1\frac{(1-x)|t+2x|^{p-2}(t+2x)}{\pi\sqrt{1-x^2}}\,dx=0.
\]
In particular its only zero lies strictly outside the closed unit disk, at \(-1-t_p\), **for every finite real exponent** \(p>1\). The principal new conclusion is the sharp high-exponent law
\[
 (p-1)t_p-\log(4(p-1))\longrightarrow0
 \qquad (p\to\infty).
\]
Thus the root tends to the boundary point \(-1\) from the exterior, with the exact logarithmic separation
\[
 |-1-t_p|-1=\frac{\log(4(p-1))+o(1)}{p-1}.
\]
For even exponents \(p=2m\), this is equivalently \(t_{2m}=[\log(8m)+o(1)]/(2m)\).

## Assumptions and scope
The approximated function is exactly \(f(z)=1-z\), the approximating polynomials have complex coefficients and degree at most one, and \(p\) ranges through **all real** numbers greater than one. The limit varies the boundary integrability exponent \(p\), not the polynomial degree. All norms are normalized with arc measure \(d\theta/(2\pi)\). No assertion is made for arbitrary \(f\), arbitrary approximating degree, or \(p=\infty\) uniqueness.

## Proof
**1. Reduction by the unique metric projection.** Write the error polynomial \(q(z)=1-(1-z)Q(z)\). The map \(Q\mapsto q\) bijects complex polynomials of degree at most one with quadratic polynomials satisfying \(q(1)=1\). For \(p>1\), strict convexity of \(L^p(\mathbb T)\) gives a unique minimizing \(q\). Both conjugation of coefficients \(q(z)\mapsto\overline{q(\bar z)}\) and conjugate reciprocal reflection \(q(z)\mapsto z^2\overline{q(1/\bar z)}\) preserve \(q(1)=1\) and its boundary norm. Uniqueness forces \(q(z)=u+(1-2u)z+uz^2\) with \(u\in\mathbb R\). On the unit circle, \(q(e^{i\theta})=e^{i\theta}[1+2u(\cos\theta-1)]\).

For \(G_p(u)=\int_0^{2\pi}|1+2u(\cos\theta-1)|^p\,d\theta/(2\pi)\), differentiation gives \(G_p'(0)=-2p<0\) and \(G_p'(1/2)=2p\int|\cos\theta|^p\,d\theta/(2\pi)>0\). Strict convexity gives the unique minimizer \(0<u_p<1/2\). Put \(t_p=u_p^{-1}-2>0\). Then \(q(z)=(1+t_p z+z^2)/(2+t_p)\), so polynomial division yields the claimed \(Q_p\).

**2. Exact scalar characterization.** Let \(X\) have arcsine distribution \(dx/(\pi\sqrt{1-x^2})\) on \((-1,1)\). The reduced objective is
\[
 \Phi_p(t)=\mathbb E\left|\frac{t+2X}{t+2}\right|^p,
 \quad t>0.
\]
Differentiation shows its derivative has the sign of \(D_p(t)=\mathbb E[(1-X)|t+2X|^{p-2}(t+2X)]\). The real function \(s\mapsto |s|^{p-2}s\) is strictly increasing for \(p>1\); hence \(D_p\) is strictly increasing. Symmetry yields \(D_p(0)=-2^{p-1}\mathbb E|X|^p<0\), and \(D_p(t)\sim t^{p-1}\mathbb E(1-X)>0\) as \(t\to\infty\). Thus the displayed scalar equation has exactly one positive root and describes the global minimizer, not merely a stationary point.

**3. Two competing endpoint saddles.** Set \(q=p-1\) and, for \(t\ge0\), write the signed integral \(D_p(t)=I_+(q,t)-I_-(q,t)\) by separating the regions \(t+2X>0\) and \(t+2X<0\). In the range \(0\le t\le C\log q/q\) for any fixed \(C>0\), uniform endpoint Laplace expansion (substitute \(X=1-y\) and \(X=-1+y\), respectively) gives
\[
 \begin{aligned}
 I_+(q,t)&=\frac{(2+t)^q}{2\sqrt{2\pi}\,q^{3/2}}
 \bigl(1+O(t+q^{-1})\bigr),\\
 I_-(q,t)&=\frac{2(2-t)^q}{\sqrt{2\pi q}}
 \bigl(1+O(t+q^{-1})\bigr).
 \end{aligned}
\]
The first endpoint has an extra vanishing factor \(1-X\), producing the differing powers \(q^{-3/2}\) and \(q^{-1/2}\). For completeness, near \(X=1\) the arcsine density is \((\pi\sqrt{2y})^{-1}(1+O(y))\), so the leading integral is proportional to \(\int_0^\infty y^{1/2}e^{-qy}\,dy=\Gamma(3/2)q^{-3/2}\). Near \(X=-1\), the factor \(1-X=2+O(y)\) and the leading integral is proportional to \(\int_0^\infty y^{-1/2}e^{-qy}\,dy=\Gamma(1/2)q^{-1/2}\). The Taylor remainders are uniformly integrable under scaling \(y\mapsto q^{-1}y\); away from fixed endpoint neighborhoods the integrals are exponentially smaller, uniformly over this \(t\)-range. The stated coefficients follow from \(\Gamma(3/2)=\sqrt\pi/2\) and \(\Gamma(1/2)=\sqrt\pi\).

Their ratio satisfies
\[
 \frac{I_+(q,t)}{I_-(q,t)}
 =\frac1{4q}\left(\frac{2+t}{2-t}\right)^q
 \bigl(1+O(t+q^{-1})\bigr).
\]
At \(t=(\log q)/(2q)\) this ratio tends to zero; at \(t=2\log q/q\) it diverges. Monotonicity of \(D_p\) traps its unique zero inside these bounds for sufficiently large \(q\), establishing \(t_p=O(\log q/q)\). Setting the ratio equal to one at the zero gives
\[
 q\log\frac{2+t_p}{2-t_p}=\log(4q)+O(t_p+q^{-1}).
\]
Because \(\log((2+t)/(2-t))=t+O(t^3)\) and \(q t_p^3=o(1)\), one obtains
\[
 q t_p=\log(4q)+o(1).
\]
This proves the sharp constant and the full real-exponent limit.

## Verification
For \(p=2\), the scalar equation gives \(t_2=1\), and hence \(Q_2(z)=(2+z)/3\). For \(p=4\), it reduces to \(t^3-3t^2+6t-3=0\), whose unique positive root is approximately \(0.677814645373914\), giving \(Q_4(z)\approx0.6265611579+0.3734388421z\). These finite cases agree with the previously published examples and are not independently claimed as new. The accompanying standalone Python checker verifies the scalar critical equation and the zero and compares the high-exponent scaled displacement with \(\log(4(p-1))\) for a range of exponents, including non-even ones. These computations are supplementary; the asymptotic is proved by the endpoint Laplace argument above.

## Relationship to prior work
Centner's 2022 *Optimal Polynomial Approximants in Lp*, Theorem 6.3 and Example 6.4, already give a general polynomial stationarity method for even exponents and numerical coefficients for \(f=1-z\) at several individual even exponents. The discussion following Example 6.4 expressly raises convergence of these degree-one zeros as \(p\to\infty\). Those finite computations are prior work, not new finite-level discoveries. The present contribution proves convergence for **all real** \(p>1\) and identifies the previously unstated logarithmic approach rate and its sharp constant through a two-endpoint asymptotic balance. Centner–Cheng–Felder (2023; later published) give general Hardy-space degree-one estimates and zero-separation results, while Bénéteau et al. (first public 2025) study nonlinear Hardy metric projections and zero-free regions; neither inspected result supplies this high-exponent rate. The general arbitrary-generator convergence question remains open.

## Limitations
This is a specific canonical boundary-zero generator and degree-one approximation. The proof does not establish convergence of zeros for arbitrary polynomials or growth of polynomial degree. Its limiting \(p=\infty\) approximation problem may have multiple minimizers; uniqueness is asserted only for finite \(p>1\). Historical priority cannot be established solely from searchable sources and is subject to unindexed or uninspected equivalents.

## References
1. R. Centner, *Optimal Polynomial Approximants in Lp*, Concrete Operators 9 (2022), 96–113, Theorem 6.3 and Example 6.4; full text https://d-nb.info/1263046533/34.
2. R. Centner, R. Cheng, C. Felder, *Optimal Polynomial Approximants in H^p*, arXiv:2305.16068, initial public version 2023; https://arxiv.org/abs/2305.16068.
3. C. Bénéteau, R. Cheng, C. Felder, D. Khavinson, M. Manolaki, K. Maronikolakis, *Metric projections, zeros of optimal polynomial approximants, and some extremal problems in Hardy spaces*, arXiv:2511.08000, initial public version 2025-11-11; https://arxiv.org/abs/2511.08000.
