# Poissonization restores thinning self-decomposability in adjacent-gamma mixtures

## Finding
Let \(r,\theta>0\), \(0\le s\le1\), and let \(\Lambda\) have distribution
\[
s\,\Gamma(r,\text{rate }\theta)+(1-s)\,\Gamma(r+1,\text{rate }\theta),
\qquad X\mid\Lambda\sim\operatorname{Pois}(\Lambda).
\]
Put \(g(z)=\theta/(\theta+1-z)\). The count PGF is
\[
G(z)=s g(z)^r+(1-s)g(z)^{r+1}
=\frac{\theta^r[\theta+s(1-z)]}{(\theta+1-z)^{r+1}}.
\]
The law of \(X\) is always compound Poisson. It is Bernoulli-thinning self-decomposable if and only if
\[
(r+1)(\theta+s)^2\ge s(\theta+1)^2. \tag{1}
\]
For \(s=0\) or \(s\ge1/(r+1)\) this holds at every \(\theta>0\). For \(0<s<1/(r+1)\) it holds exactly when
\[
\theta\ge\theta_*(r,s)=\frac{\sqrt{s}-s\sqrt{r+1}}{\sqrt{r+1}-\sqrt{s}}.
\tag{2}
\]
The continuous mixing law is self-decomposable precisely for \(s=0\) or \(s\ge1/(r+1)\). Thus (2) gives a region of count self-decomposability despite a non-self-decomposable mixing law.

For the Poisson new X-Lindley (PNXL) law, \(r=1,s=1/2\), the factorial-Palm residual \(Y_m\) has the law
\[
\Pr(Y_m=n)=\frac{(n+m)_{\underline m}\Pr(X=n+m)}{\mathbb E[(X)_{\underline m}]},
\qquad n=0,1,\ldots,\quad m=0,1,\ldots.
\]
Here the underline denotes a falling factorial. It has PGF
\[
\mathbb E[z^{Y_m}]=\frac1{m+2}g(z)^{m+1}+\frac{m+1}{m+2}g(z)^{m+2},
\tag{3}
\]
so the lower-shape weight is exactly the critical all-rate weight \(1/((m+1)+1)\). Each residual is thinning self-decomposable for every \(\theta>0\).

## Assumptions and scope
The gamma Laplace transform for shape \(r\) and rate \(\theta\) is \((\theta/(\theta+t))^r\). Continuous self-decomposability means \(\Lambda\stackrel d=c\Lambda'+R_c\) for every \(0<c<1\), with \(\Lambda'\stackrel d=\Lambda\) independent of a nonnegative \(R_c\). Thinning self-decomposability means \(X\stackrel d=c\circ X'+Z_c\) for all such \(c\), where \(X'\stackrel d=X\), \(c\circ X'\) independently retains each counted unit with probability \(c\), and the innovation \(Z_c\) is independent of the thinned count. One can construct the innovation independently of \(X'\) and the thinning. These are different definitions.

## Proof

### The continuous and discrete Lévy kernels
The mixing Laplace transform is \(\theta^r(\theta+st)/(\theta+t)^{r+1}\). For \(s>0\), its logarithm is
\[
\int_0^\infty(e^{-tx}-1)\frac{k(x)}{x}\,dx,
\qquad k(x)=(r+1)e^{-\theta x}-e^{-\theta x/s}.
\]
This follows from the logarithm integral for \(\log(a/(a+t))\); for \(s=0\) the second exponential is omitted. The kernel is positive since \(0<s\le1\), and the Lévy integrability condition holds by boundedness near zero and exponential decay at infinity. The standard continuous criterion [2] is that \(k\) be nonincreasing. For \(s>0\), the positive term of \(k'(x)\) divided by \(\theta e^{-\theta x}\) is \(s^{-1}e^{-\theta(1/s-1)x}\), whose supremum for \(x>0\) is \(1/s\). The negative term after the same division is \(-(r+1)\), so the continuous cutoff is \(s\ge1/(r+1)\). At \(s=0\), the kernel is strictly decreasing.

For the count set \(q=1/(\theta+1)\) and \(a=s/(\theta+s)\). Then \(0\le a\le q<1\), and expansion at zero gives
\[
\log G(z)=\sum_{n\ge1}\lambda_n(z^n-1),
\qquad \lambda_n=\frac{(r+1)q^n-a^n}{n}>0.
\tag{4}
\]
The series of intensities is summable by geometric decay, and the constant is fixed by \(G(1)=1\). This proves the compound-Poisson statement.

### The discrete boundary and the innovation
The discrete canonical-sequence criterion [2] states that for (4), thinning self-decomposability is equivalent to \(b_n=n\lambda_n\) nonincreasing for \(n\ge1\). Here
\[
b_n-b_{n+1}=(r+1)(1-q)q^n-(1-a)a^n.
\]
Since \(a/q\le1\), the strongest inequality is \(n=1\); the remaining ones follow, including \(a=0\). The inequality there is equivalent to (1), since \(q(1-q)=\theta/(\theta+1)^2\) and \(a(1-a)=s\theta/(\theta+s)^2\). Taking the positive square roots gives
\((\sqrt{r+1}-\sqrt{s})\theta\ge\sqrt{s}-s\sqrt{r+1}\), with strictly positive coefficient of \(\theta\). This proves (2) and both all-rate cases, including equality in (1).

For an explicit innovation, put \(q_u=u/(\theta+u)\), \(a_u=su/(\theta+su)\), and \(b_n(u)=(r+1)q_u^n-a_u^n\) for \(u\in[0,1]\). The logarithm of the required PGF ratio \(H_c(z)=G(z)/G(1-c+cz)\) has degree-\(n\) coefficient \(\nu_n(c)=(b_n(1)-b_n(c))/n\). For \(u>0\),
\[
b_n'(u)=n\theta u^{n-1}\left[\frac{r+1}{(\theta+u)^{n+1}}-\frac{s^n}{(\theta+su)^{n+1}}\right].
\]
The second term after multiplying the bracket by \((\theta+u)^{n+1}\) is bounded by
\[
\frac{s(\theta+u)^2}{(\theta+su)^2}
\left(\frac{s(\theta+u)}{\theta+su}\right)^{n-1}
\le\frac{s(\theta+1)^2}{(\theta+s)^2},
\]
since the parenthesis is at most one and \((\theta+u)/(\theta+su)\) is nondecreasing. The \(s=0\) term is simply zero. Under (1) this proves \(\nu_n(c)\ge0\), and \(\nu_n(c)\le\lambda_n\) gives summability. With normalization at one, \(H_c(z)=\exp(\sum_{n\ge1}\nu_n(c)(z^n-1))\). If (1) fails, \(b_1'(1)<0\), so for \(c<1\) sufficiently close to 1 the linear coefficient of \(H_c\) equals \(H_c(0)\nu_1(c)<0\), a direct witness that no such count-valued innovation exists.

### The factorial-Palm hierarchy
The PNXL mixing density in [1] is \(\theta(1+\theta x)e^{-\theta x}/2\), the equal mixture of gamma shapes one and two. Differentiation uses the **rising** product \(v^{\overline m}=v(v+1)\cdots(v+m-1)\), equal to 1 for \(m=0\):
\[
\frac{d^m}{dz^m}g(z)^v=v^{\overline m}\theta^{-m}g(z)^{v+m}.
\]
The PGF of the residual is \(G^{(m)}(z)/G^{(m)}(1)\). The derivative weights for the two components are proportional to \(m!\) and \((m+1)!\), respectively. Dividing by their sum proves (3), with shape \(m+1\) and weight \(1/(m+2)\). The thinning conclusion follows from (1).

## Verification
The accompanying `checks/checker.py` checks exact rational cases of the PGFs, intensity and innovation formulas, boundary signs and Palm weights. For instance when \(r=1,s=1/4\), \(b_1-b_2=-230/5929\) at \(\theta=1/10\) and \(7/100\) at \(\theta=1/4\). Continuous self-decomposability fails at both rates. The general classification is analytic, not a consequence of finite checks.

## Relationship to prior work and limitations
The compound-Poisson, continuous and discrete criteria applied here are standard; [2] gives the continuous Lévy and discrete canonical-sequence characterizations. The PNXL count and its use as an INAR innovation are already in [1]; that use is not the claim that PNXL is a thinning self-decomposable stationary marginal. The PGL distribution [3] is the constrained subfamily \(r=\alpha-1\), \(s=\theta/(\theta+1)\) for \(\alpha>1\). The separate classification [4] covers the exact discrete boundary on that curve, \(\alpha\ge(\theta+1)^3/[\theta(\theta+2)^2]\), with an innovation law; no priority ordering is asserted between the classifications. The scope here is the boundary with independently varying mixing weight, its continuous-versus-discrete separation, and the critical factorial-Palm residuals. NB mixtures with an integer shift, rather than adjacent shape parameters, are different families. No classification of arbitrary gamma mixtures or other thinning mechanisms is claimed. The historical comparison is bounded.

## References
1. M. R. Irshad, S. Aswathy, R. Maya and S. Nadarajah, *New One-Parameter Over-Dispersed Discrete Distribution and Its Application to the Nonnegative Integer-Valued Autoregressive Model of Order One*, Mathematics **12** (2024), 81. [DOI](https://doi.org/10.3390/math12010081).
2. A. G. Pakes, *Mutant Number Laws and Infinite Divisibility*, Axioms **11** (2022), 584, §2. [DOI](https://doi.org/10.3390/axioms11110584).
3. Atikankul, *A New Poisson Generalized Lindley Regression Model*, Austrian Journal of Statistics **52** (2023), 39–50. [DOI](https://doi.org/10.17713/ajs.v52i1.1344).
4. *Sharp thinning self-decomposability frontier of the two-parameter Poisson-generalized Lindley law*, [Resultary record](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-sharp-thinning-self-decomposability-frontier-of-the-two-paramete--d7a7540680dd).
