# A symmetric logarithmic noise factor distinguishes reversed stable and inverse-stable clocks

## Finding

Fix indices \(0<\alpha<1\), \(0<\beta<1\), and an observation time \(t>0\). Let \(D_\alpha\) be a standard positive \(\alpha\)-stable subordinator, and let \(E_\beta\) be an independent inverse standard positive \(\beta\)-stable subordinator. Consider the two orders of composition
\[
 A_t=D_\alpha(E_\beta(t)),\qquad B_t=E_\beta(D_\alpha(t)).
\]
There exists a **nondegenerate, symmetric, infinitely divisible** real random variable \(W_{\alpha,\beta}\), independent of a variable with the law of \(B_t\), such that
\[
 \boxed{\log A_t\ \stackrel{\mathrm d}=\ \log B_t+W_{\alpha,\beta}.}
\]
The noise law depends on \(\alpha,\beta\) but not on \(t\), and its characteristic function is
\[
 \mathbb E e^{i\theta W_{\alpha,\beta}}
 =\frac{\sinh(\pi\theta)\,\sinh(\pi\beta\theta/\alpha)}
 {\sinh(\pi\theta/\alpha)\,\sinh(\pi\beta\theta)},\qquad\theta\in\mathbb R,
\]
with value \(1\) at \(\theta=0\). In particular, whenever the convex expectations are defined,
\[
 \boxed{\mathbb E\,\Phi(\log B_t)\le\mathbb E\,\Phi(\log A_t)}
\]
for every convex \(\Phi:\mathbb R\to\mathbb R\); the inequality is strict for every strictly convex \(\Phi\) with finite expectations. Both logarithms have the same finite mean,
\[
 \mathbb E\log A_t=\mathbb E\log B_t
 =\frac\beta\alpha\log t+\gamma\left(\frac\beta\alpha-1\right),
\]
where \(\gamma\) is Euler's constant, while their variances differ by the positive amount
\[
 \boxed{\operatorname{Var}(\log A_t)-\operatorname{Var}(\log B_t)
 =\frac{\pi^2}{3}\left(\alpha^{-2}-1\right)(1-\beta^2).}
\]
Thus reversing the same two random clocks produces an exact, time-independent mean-preserving spread **on the logarithmic clock scale**. This is a one-time-marginal statement; it does not assert an independent process-level perturbation.

## Assumptions and scope

The standard subordinator is normalized by
\(\mathbb E[e^{-sD_\alpha(u)}]=e^{-us^\alpha}\) for every \(s,u\ge0\). The inverse \(E_\beta(t)=\inf\{u\ge0:D_\beta'(u)>t\}\) is defined from an independent standard \(\beta\)-stable subordinator \(D_\beta'\); all processes appearing in either composition are independent. The index restrictions are strict, and \(t>0\). Each composed clock is positive almost surely. The classical first moment of \(D_\alpha(1)\) is infinite; no finite-first-moment assumption is used here. The entire conclusion concerns their **one-dimensional distributions**, not equality of sample paths or process increments.

Write \(S_\alpha=D_\alpha(1)\), \(J_\beta=E_\beta(1)\), taking independent copies within each product representation. By self-similarity,
\[
 A_t\stackrel{\mathrm d}=t^{\beta/\alpha}S_\alpha J_\beta^{1/\alpha},
 \qquad
 B_t\stackrel{\mathrm d}=t^{\beta/\alpha}S_\alpha^\beta J_\beta.
\]
These products are distributional representations only; they need not use the same factors across the two displays.

## Proof

**1. Mellin transforms.** The standard positive-stable and inverse-stable moment identities, obtained from their Laplace transforms, are
\[
 \mathbb E S_\alpha^z=\frac{\Gamma(1-z/\alpha)}{\Gamma(1-z)}
 \quad (\Re z<\alpha),\qquad
 \mathbb E J_\beta^z=\frac{\Gamma(1+z)}{\Gamma(1+\beta z)}
 \quad (\Re z>-1).
\]
These identities hold for complex \(z\) in the indicated domains. Consequently, for \(-\alpha<\Re z<\alpha\), after removing the common factor \(t^{\beta z/\alpha}\),
\[
 M_A(z)=\frac{\Gamma(1-z/\alpha)\Gamma(1+z/\alpha)}
 {\Gamma(1-z)\Gamma(1+\beta z/\alpha)},\qquad
 M_B(z)=\frac{\Gamma(1-\beta z/\alpha)\Gamma(1+z)}
 {\Gamma(1-\beta z)\Gamma(1+\beta z)}.
\]
Here \(M_A\) and \(M_B\) are Mellin transforms of the dimensionless products. The reflection identity \(\Gamma(1+z)\Gamma(1-z)=\pi z/\sin(\pi z)\) yields
\[
 \frac{M_A(z)}{M_B(z)}=
 \frac{\sin(\pi z)\sin(\pi\beta z/\alpha)}
 {\sin(\pi z/\alpha)\sin(\pi\beta z)}.
\]
Putting \(z=i\theta\) gives the displayed candidate noise characteristic function, with its value at zero defined continuously.

**2. A positive Lévy measure.** Put \(a=\alpha^{-1}>1\) and \(b=\beta\in(0,1)\). For \(c>0\), define the centered logistic characteristic function
\[
 \phi_c(\theta)=\frac{\pi c\theta}{\sinh(\pi c\theta)}.
\]
The Weierstrass product for \(\sinh\), or equivalently the elementary integral identity for \(\log(1+u^2)\), gives
\[
 \log\phi_c(\theta)=2\int_0^\infty
 \frac{\cos(\theta x)-1}{x(e^{x/c}-1)}\,dx.
\]
The candidate ratio equals \(\phi_a\phi_b/(\phi_1\phi_{ab})\). Define, for every \(x>0\),
\[
 \Delta_{a,b}(x)=\frac1{e^{x/a}-1}+\frac1{e^{x/b}-1}
 -\frac1{e^x-1}-\frac1{e^{x/(ab)}-1}.
\]
We prove that **\(\Delta_{a,b}(x)>0\) for all \(x>0\)**. Let \(h(y)=(e^{xe^{-y}}-1)^{-1}\). With \(v=xe^{-y}>0\),
\[
 h'(y)=\frac{ve^v}{(e^v-1)^2}>0,
 \qquad
 \frac{d}{dv}\log\left(\frac{ve^v}{(e^v-1)^2}\right)
 =\frac1v-\coth(v/2)<0.
\]
Because \(dv/dy=-v<0\), it follows that \(h''(y)>0\). Write \(u=\log a>0\) and \(v=\log b<0\). Strict convexity implies
\[
 h(u)-h(u+v)>h(0)-h(v),
\]
which is exactly \(\Delta_{a,b}(x)>0\). Furthermore,
\[
 \Delta_{a,b}(x)=\frac{(a-1)(1-b)}x+O(x)
 \quad (x\downarrow0),
\]
while it decays exponentially as \(x\to\infty\). Thus the symmetric measure on \(\mathbb R\setminus\{0\}\) defined by
\[
 \boxed{\nu_{a,b}(dx)=\frac{\Delta_{a,b}(|x|)}{|x|}\,dx}
\]
is a legitimate Lévy measure, with \(\int(1\wedge x^2)\nu_{a,b}(dx)<\infty\). Its Lévy–Khintchine exponent, using symmetry, is
\[
 \int_{\mathbb R\setminus\{0\}}(\cos(\theta x)-1)\nu_{a,b}(dx)
 =2\int_0^\infty\frac{\cos(\theta x)-1}{x}\Delta_{a,b}(x)\,dx
 =\log\frac{\phi_a(\theta)\phi_b(\theta)}{\phi_1(\theta)\phi_{ab}(\theta)}.
\]
By the Lévy–Khintchine theorem this is the characteristic function of a symmetric infinitely divisible variable \(W_{\alpha,\beta}\). Positivity of the Lévy measure makes the variable nondegenerate. Exponential decay at infinity and the quadratic Lévy integrability at zero give finite logarithmic variance.

**3. Factorization and convex order.** Take an independent copy of \(\log B_t\) and add the variable \(W_{\alpha,\beta}\) just constructed. The characteristic function of their sum is, by Step 1 and Step 2, exactly the characteristic function of \(\log A_t\). Uniqueness of characteristic functions establishes the distributional factorization. Since \(W_{\alpha,\beta}\) is symmetric and integrable, it has mean zero. Conditional Jensen gives
\[
 \Phi(\log B_t)=\Phi\bigl(\mathbb E[\log B_t+W_{\alpha,\beta}\mid\log B_t]\bigr)
 \le\mathbb E[\Phi(\log B_t+W_{\alpha,\beta})\mid\log B_t].
\]
After integration this proves convex order. Strict convexity and the nondegenerate independent noise yield strictness when expectations are finite. Differentiating the Mellin transforms at zero gives the common mean above; the second derivative of the log characteristic-function ratio gives
\(\operatorname{Var}(W_{\alpha,\beta})=(\pi^2/3)(a^2-1)(1-b^2)\). Independence proves the stated variance gap. This completes the proof.

## Verification

The proof above is analytical and covers every strict parameter pair and every \(t>0\). The accompanying `checker.py` independently evaluates the two gamma-function Mellin products against the hyperbolic-sine formula at imaginary arguments; verifies the proposed Lévy-density sign over a multidimensional sample grid; compares the exact second log-moment difference against numerical differentiation; and quadratures the Lévy–Khintchine exponent. In one reproducible run it passed **750 finite diagnostic comparisons**. These finite checks are not used to infer positivity for all parameters; that universal step is established by strict convexity of \(h\) in Step 2.

To reproduce from this package, run `python checker.py` with Python 3 and `mpmath` installed. The script outputs the counted diagnostics and fails by assertion if a tested identity or inequality is violated.

## Relationship to prior work

Tathe and Ghosh [1], Definitions 3.1–3.2, explicitly distinguish the compositions of a subordinator and an inverse subordinator in both orders in a time-changed compound-Poisson setting, but subsequently focus on the first order. Their time-change formulae and asymptotic/counting results do not provide a logarithmic convex comparison of the two positive clock marginals. The strict stable-index model here is independently defined and does not use their finite-moment assumptions.

Kataria and Vellaisamy [2] provide Fox-\(H\) density and Mellin-transform identities for powers and products of independent subordinators, and Gupta and Kumar [3] provide density expansions for stable and inverse-stable products. Those transforms supply classical ingredients for Step 1. **The contribution asserted here is not a new product density or Mellin transform:** it is the explicit **positive four-term Lévy kernel**, the resulting symmetric independent factorization for reversed compositions, and the exact all-convex-test logarithmic ordering. The inspected primary sections do not state these comparisons. Simon [4] proves convex-order comparisons among normalized inverse-stable (Mittag–Leffler) variables as the stability index varies, and provides rational-index beta factorizations. That ordering changes the index of one clock, not the composition order of two different clocks; its conclusions do not provide the symmetric independent factor claimed here. General convex-order theory [5] explains the Jensen consequence once an independent centered factor is proved, but does not itself prove that this factor exists.

## Limitations

This is only a one-time marginal identity, not a pathwise equality or a process-level coupling. Convex ordering is asserted on the **logarithms**, not on raw clocks: \(\mathbb E A_t=\infty\) in this index regime, so an ordinary finite-mean convex order on the clocks is not claimed. The endpoints \(\alpha=1\) or \(\beta=1\) are excluded (the noise degenerates at these boundaries by continuity). The comparison is derived for standardized positive stable processes, not for arbitrary Bernstein functions, tempered clocks, dependent components, or general jump-size distributions. An independent literature assessment, particularly for historical multiplicative stochastic-order results, remains outstanding.

## References

[1] K. Tathe and S. Ghosh, *Time-changed Compound Poisson Process*, arXiv:2611.16676v1 (first posted 12 November 2026). https://arxiv.org/html/2611.16676v1

[2] K. K. Kataria and P. Vellaisamy, *On Densities of the Product, Quotient and Power of Independent Subordinators*, arXiv:1608.06564 (2016), J. Math. Anal. Appl. 462 (2018), 1627–1643. https://arxiv.org/abs/1608.06564

[3] N. Gupta and A. Kumar, *Densities of Inverse Tempered Stable Subordinators and Related Processes With Mellin Transforrm*, arXiv:2108.09170v1 (2021), particularly Section 3. https://arxiv.org/pdf/2108.09170

[4] T. Simon, *Comparing Fréchet and positive stable laws*, Electron. J. Probab. 19 (2014), article 16; arXiv:1310.1888v2, especially Theorems A–C. https://arxiv.org/pdf/1310.1888

[5] M. Shaked and J. G. Shanthikumar, *Stochastic Orders*, Springer, 2007, chapters on convex order. https://doi.org/10.1007/978-0-387-34675-5
