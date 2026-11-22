# Sharp dimension-free extendibility of the two-parameter half-logistic copula

## Finding

Fix \(\alpha>0\) and \(\theta>0\), and let \(\Psi_{\alpha,\theta}\) be the multiplicative Archimedean generator
\[
\Psi_{\alpha,\theta}(u)
=\frac{(e^\theta+\alpha)(e^{\theta u}-1)}
{(e^\theta-1)(e^{\theta u}+\alpha)},\qquad 0\le u\le1.
\]
For every integer \(d\ge2\), form its *canonical Archimedean extension*
\[
C_d(u_1,\ldots,u_d)=\Psi_{\alpha,\theta}^{-1}
\!\left(\prod_{j=1}^d\Psi_{\alpha,\theta}(u_j)\right).
\]
Then \(C_d\) is a copula for **every** finite dimension \(d\) if and only if
\[
\boxed{0<\alpha\le1,\quad \theta>0.}
\]
The boundary is independent of \(\theta\). More precisely, set
\[
q=\frac{e^\theta-1}{e^\theta+\alpha},\qquad
w_k=\frac{q^k\big[1+(-1)^{k+1}\alpha^k\big]}{k\theta},\quad k=1,2,\ldots .
\]
For \(0<\alpha\le1\), \((w_k)_{k\ge1}\) is a probability distribution and all of the copulas have the explicit finite-dimensional mixture representation
\[
\boxed{C_d(u_1,\ldots,u_d)=\sum_{k=1}^{\infty}w_k
\prod_{j=1}^d\Psi_{\alpha,\theta}(u_j)^k.}
\]
Every weight is strictly positive for \(0<\alpha<1\); for \(\alpha=1\), the frailty is supported *exactly* on odd positive integers. For \(\alpha>1\), the canonical construction fails in at least one finite dimension, although it remains a valid bivariate copula. For example, \((\alpha,\theta)=(100,\log 3)\) already fails in dimension three.

## Assumptions and scope

The original two-parameter half-logistic family is considered with finite \(\alpha>0\) and \(\theta>0\). The multiplicative generator is continuous, strictly increasing from \(0\) to \(1\), and log-concave, hence its bivariate copula is valid for every such pair. The result concerns the canonical *associative Archimedean formula* in every dimension, not arbitrary exchangeable multivariate extensions with the same bivariate margins. The separate degenerate limit \(\theta\downarrow0\) is independence and is valid in all dimensions for every \(\alpha>0\).

Write \(H(t)=\Psi_{\alpha,\theta}^{-1}(e^{-t})\), \(t\ge0\). The multivariate Archimedean criterion says that the canonical formula yields copulas of every finite dimension exactly when \(H\) is completely monotone; it yields a copula of a specific dimension \(d\) when \(H\) is \(d\)-monotone. This classical equivalence is used here rather than claimed as a new theorem.

## Proof

**1. Exact generator inversion.** Put \(r=e^\theta>1\) and \(q=(r-1)/(r+\alpha)\), so \(0<q<1\). Solving \(z=\Psi_{\alpha,\theta}(u)\) for \(e^{\theta u}\) gives
\[
e^{\theta u}=\frac{1+\alpha qz}{1-qz},\quad
\Psi_{\alpha,\theta}^{-1}(z)=\frac{1}{\theta}
\log\frac{1+\alpha qz}{1-qz}.
\]
Consequently,
\[
H(t)=\frac1\theta\left[\log(1+\alpha qe^{-t})-
\log(1-qe^{-t})\right],\qquad H(0)=1,\quad H(\infty)=0.
\]

**2. Sufficiency and the exact frailty distribution.** When \(0<\alpha\le1\), both \(q\) and \(\alpha q\) are below one, so both logarithms admit absolutely convergent series even at \(t=0\). Expanding gives
\[
H(t)=\sum_{k\ge1}\frac{q^k}{k\theta}
\left[1+(-1)^{k+1}\alpha^k\right]e^{-kt}
=\sum_{k\ge1}w_k e^{-kt}.
\]
For odd \(k\), the square bracket is \(1+\alpha^k>0\); for even \(k\), it is \(1-\alpha^k\ge0\). Moreover,
\[
\sum_{k\ge1}w_k=H(0)=\frac1\theta
\log\frac{1+\alpha q}{1-q}=\frac{\log r}{\theta}=1.
\]
Thus \(H\) is the Laplace transform of an integer-valued random variable \(K\ge1\), proving complete monotonicity. For \(u_j\in[0,1]\),
\[
C_d(u_1,\ldots,u_d)=H\!\left(-\sum_j\log\Psi_{\alpha,\theta}(u_j)\right)
=\mathbb E\left[\prod_j\Psi_{\alpha,\theta}(u_j)^K\right],
\]
with continuous extension at zero. Conditional on \(K=k\), take \(d\) independent variables with CDF \(u\mapsto\Psi_{\alpha,\theta}(u)^k\). Their mixture has a uniform one-coordinate marginal since \(\mathbb E[\Psi_{\alpha,\theta}(u)^K]=u\). This directly proves that each \(C_d\) is a copula, without relying solely on the general complete-monotonicity theorem. At \(\alpha=1\), the even weights vanish and all odd weights remain strictly positive.

An exact sampling representation follows: draw \(K\) with probabilities \(w_k\), draw independent \(V_j\sim\mathrm{Uniform}(0,1)\), and put
\[
U_j=\frac1\theta\log\frac{1+\alpha q V_j^{1/K}}{1-q V_j^{1/K}}.
\]
The resulting \(d\)-vector has copula \(C_d\).

**3. Necessity, including logarithmic-series radius issues.** Suppose \(\alpha>1\). For any \(T>\max\{0,\log(\alpha q)\}\), expansion of the same logarithms is absolutely convergent at \(t\ge T\), yielding
\[
H(t)=\sum_{k\ge1} w_k e^{-kt},\quad t\ge T,
\qquad w_2=\frac{q^2(1-\alpha^2)}{2\theta}<0.
\]
Assume for contradiction that \(H\) is completely monotone. By the Bernstein--Widder theorem and \(H(0)=1\), it is the Laplace transform of a positive probability measure \(\mu\) on \([0,\infty)\). Then \(H(T+s)\) is the Laplace transform both of the finite positive measure \(e^{-Tx}\mu(dx)\) and of the finite signed measure \(\sum_{k\ge1}w_ke^{-Tk}\delta_k\). Uniqueness of Laplace transforms of finite signed measures forces equality of these two measures. This is impossible since the latter assigns negative mass \(w_2e^{-2T}<0\) to \(\{2\}\). Thus \(H\) is not completely monotone, and the canonical copula formula cannot be valid in every dimension. The shift by \(T\) is essential when \(\alpha q\ge1\), where the raw series at \(t=0\) need not converge.

**4. Explicit three-dimensional obstruction.** A smooth three-monotone Archimedean generator must satisfy \(-H'''(t)\ge0\) on \((0,\infty)\). For \(x=e^{-t}\), \(a=\alpha q\), and \(b=q\), direct differentiation gives
\[
-\theta H'''(t)=\frac{bx(1+bx)}{(1-bx)^3}+
\frac{ax(1-ax)}{(1+ax)^3}.
\]
At \(\alpha=100\), \(\theta=\log3\), one has \(b=2/103\), \(a=200/103\), and
\[
-\theta H'''(0)=\frac{21630}{101^3}-\frac{1998200}{303^3}
=-\frac{1414190}{27818127}<0.
\]
Continuity makes the strict violation persist for sufficiently small positive \(t\); hence the canonical three-dimensional expression is not a copula at this parameter pair. This example is not a classification of the full three-dimensional parameter region.

## Verification

The accompanying `checker.py` is a standalone standard-library Python script. Run `python3 checker.py`. It checks inverse-generator algebra numerically for representative parameters, the positivity and normalization of the mixing probabilities for \(0<\alpha\le1\), convergence to \(H\), the negative second signed coefficient for \(\alpha>1\), and the exact rational three-dimensional obstruction. It passed on the supplied contents. The infinitely many-dimensional equivalence is proved analytically above; numerical truncation is not used as an infinite proof.

## Relationship to prior work

Alzaid and Alhadlaq (published online 27 December 2023) define the one- and two-parameter half-logistic *bivariate* Archimedean copulas, establish bivariate generator validity, investigate their dependence, and observe the Frank limiting case. The formula for \(\Psi_{\alpha,\theta}\) is taken directly from their Section 4. The general criterion connecting complete monotonicity to every-dimensional Archimedean validity is due to Kimberling and is stated and developed in McNeil--Nešlehová (2009), Section 2. The 2020 generator paper by Alhadlaq--Alzaid concerns generator construction and bivariate copulas. The present family-specific threshold, positive discrete frailty weights, parity boundary and explicit trivariate failure calculation are not asserted in those inspected sources. This does not establish absolute historical priority.

## Limitations

Only the original positive-parameter family and its canonical Archimedean multivariate construction are addressed. For \(\alpha>1\) the proof shows failure in *some* finite dimension; it does not determine the maximum valid dimension at every \((\alpha,\theta)\), nor exclude all non-Archimedean multivariate extensions sharing its bivariate margins. The result uses a standard general theorem and standard uniqueness of Laplace transforms; its specific contribution is the exact family classification and constructive distributional representation. Literature coverage is finite, so independent priority and external mathematical validation remain open.

## References

1. A. A. Alzaid and W. M. Alhadlaq, *A New Family of Archimedean Copulas: The Half-Logistic Family of Copulas*, Mathematics **12** (2024), 101, published online 27 December 2023. https://doi.org/10.3390/math12010101
2. A. J. McNeil and J. Nešlehová, *Multivariate Archimedean copulas, d-monotone functions and \(\ell_1\)-norm symmetric distributions*, Annals of Statistics **37** (2009), 3059--3097. https://arxiv.org/abs/0908.3750; https://doi.org/10.1214/07-AOS556
3. W. Alhadlaq and A. Alzaid, *Distribution Function, Probability Generating Function and Archimedean Generator*, Symmetry **12** (2020), 2108. https://doi.org/10.3390/sym12122108
