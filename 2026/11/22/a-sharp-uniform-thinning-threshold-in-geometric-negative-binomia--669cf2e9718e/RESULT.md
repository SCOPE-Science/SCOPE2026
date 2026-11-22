# A sharp uniform thinning threshold in geometric–negative-binomial mixtures

## Finding

For \(0\le p\le1\) and \(0<q<1\), define the probability generating function
\[
G_{p,q}(z)=p\frac{1-q}{1-qz}+(1-p)\left(\frac{1-q}{1-qz}\right)^3.
\]
Every distribution in this family is infinitely divisible under ordinary addition on the nonnegative integers. The stronger property of **discrete self-decomposability under Bernoulli thinning for every retention probability** holds for every \(q\in(0,1)\) if and only if
\[
\boxed{p=0\quad\text{or}\quad 4/9\le p\le1.}
\]
More sharply, when \(0<p<4/9\), there is an \(\varepsilon_p>0\) such that self-decomposability fails for **every** \(q\in(1-\varepsilon_p,1)\). Thus the endpoint \(p=0\) is isolated from the positive mixture weights in this uniform-in-rate classification.

In the shape-three Poisson-modified quasi-Lindley model of Tharshan and Wijekoon, \(p=\alpha^3/(1+\alpha^3)\) and \(q=(1+\theta)^{-1}\). Restricting to its genuine convex-mixture parameters \(\alpha\ge0\), \(\theta>0\), the uniform-in-\(\theta\) self-decomposable region is precisely
\[
\boxed{\alpha=0\quad\text{or}\quad\alpha\ge(4/5)^{1/3}.}
\]
The assertion concerns **uniform validity over all rates**; it does not classify every fixed pair of model parameters.

## Assumptions and scope

Write \(\mathrm{NB}(r,q)\) for the nonnegative-integer law with generating function \(((1-q)/(1-qz))^r\). The above family is the convex mixture \(p\,\mathrm{NB}(1,q)+(1-p)\,\mathrm{NB}(3,q)\). Bernoulli thinning \(t\circ X\), for \(t\in(0,1)\), independently retains each of the \(X\) counted items with probability \(t\). Discrete self-decomposability means that for every such \(t\) there exists a nonnegative-integer random variable \(E_t\), independent of \(t\circ X'\) with \(X'\) distributed as \(X\), such that \(X\) and \(t\circ X'+E_t\) have the same law. This is distinct from ordinary additive infinite divisibility.

## Proof

**1. Explicit compound-Poisson coefficients.** The cases \(p=0\) and \(p=1\) are negative-binomial laws of shape three and one, respectively, with logarithmic jump intensities \(3q^n/n\) and \(q^n/n\), for integers \(n\ge1\). Assume \(0<p<1\), and put
\[
\varepsilon=1-q,\qquad s=\frac{1-p}{p}>0,\qquad
w=\frac{q}{1+i\sqrt{s}\,\varepsilon}.
\]
Exact factorization gives
\[
G_{p,q}(z)=\frac{p\varepsilon\big[(1-qz)^2+s\varepsilon^2\big]}{(1-qz)^3}.
\]
Since \(|w|<q<1\), the logarithm has an absolutely convergent expansion on the closed unit disk:
\[
\log G_{p,q}(z)=\sum_{n\ge1}\lambda_n(z^n-1),\qquad
\lambda_n=\frac{3q^n-2\operatorname{Re}(w^n)}n.
\]
The normalization follows from \(G_{p,q}(1)=1\). For every \(n\ge1\),
\[
n\lambda_n\ge3q^n-2|w|^n>q^n>0.
\]
Moreover \(\sum_n\lambda_n<\infty\). Hence all the laws, including every positive interior mixture, are compound Poisson.

**2. Thinning criterion and constructive innovations.** Set \(b_n=n\lambda_n\). The classical discrete self-decomposability criterion says that a compound-Poisson law is self-decomposable under all Bernoulli thinnings exactly when \(b_n\ge b_{n+1}\) for every \(n\ge1\). For completeness, let \(c_n=b_n-b_{n+1}\). When the inequalities hold, \(c_n\ge0\), \(\sum_{n\ge1}c_n=b_1\), and, with \(L(z)=\log G_{p,q}(z)\),
\[
(1-u)L'(u)=\sum_{n\ge1}c_n(1-u^n).
\]
Thus for each \(t\in(0,1)\),
\[
\log\frac{G_{p,q}(z)}{G_{p,q}(1-t+tz)}
=\sum_{n\ge1}c_n\int_t^1\frac{(1-v+vz)^n-1}{v}\,dv.
\]
Each integrand is a polynomial generating positive jump intensities and their negative normalizing constant. Consequently, the quotient is a compound-Poisson probability generating function and defines the independent innovation. Conversely, if the quotient is a probability generating function for every \(t\), the coefficient of \(z^n\), for \(n\ge1\), in its expansion about \(t=1\) is \((1-t)c_n+o(1-t)\); it cannot be negative. This proves the criterion independently for the analytic family at issue.

**3. Uniform sufficient range.** Direct subtraction yields
\[
b_n-b_{n+1}=3q^n\varepsilon-2\operatorname{Re}\big(w^n(1-w)\big).
\]
Because
\[
\frac{|w|}{q}=\frac1{\sqrt{1+s\varepsilon^2}},\qquad
\frac{|1-w|}{\varepsilon}=\frac{\sqrt{1+s}}{\sqrt{1+s\varepsilon^2}},
\]
we obtain simultaneously for every integer \(n\ge1\)
\[
\frac{b_n-b_{n+1}}{q^n\varepsilon}
\ge3-\frac{2\sqrt{1+s}}{(1+s\varepsilon^2)^{(n+1)/2}}.
\]
For \(0<s\le5/4\), the right side is strictly positive for every \(q\in(0,1)\). The inequality \(s\le5/4\) is equivalent to \(p\ge4/9\). The endpoint \(p=1\) follows from its geometric canonical coefficients; at \(p=0\) the shape-three negative-binomial coefficients are also strictly decreasing. This proves uniform sufficiency.

**4. Sharpness and the nonuniform obstruction.** If \(0<p<4/9\), then \(s>5/4\). Put
\[
x=\frac{\arctan\sqrt{s}}{\sqrt{s}}>0,\qquad
n(\varepsilon)=\left\lfloor\frac{x}{\varepsilon}\right\rfloor.
\]
As \(\varepsilon\downarrow0\), with \(q=1-\varepsilon\), elementary complex-power convergence gives
\[
\left(\frac{w}{q}\right)^{n(\varepsilon)}\longrightarrow
 e^{-i\sqrt{s}x},\qquad
\frac{1-w}{\varepsilon}\longrightarrow1+i\sqrt{s}.
\]
It follows that
\[
\lim_{\varepsilon\downarrow0}
\frac{b_{n(\varepsilon)}-b_{n(\varepsilon)+1}}
{q^{n(\varepsilon)}\varepsilon}
=3-2\big[\cos(\sqrt{s}x)+\sqrt{s}\sin(\sqrt{s}x)\big]
=3-2\sqrt{1+s}<0.
\]
Thus a canonical coefficient eventually increases for every sufficiently small positive \(\varepsilon\), excluding self-decomposability and proving necessity of the stated uniform threshold. The limit is for an index growing with inverse rate; checking any fixed number of coefficients cannot replace it.

**5. Exact finite witness.** At \(p=1/5\) and \(q=99/100\), the complex root reduces to the Gaussian rational \(w=(99/100)/(1+i/50)\). Exact rational arithmetic gives \(b_n-b_{n+1}>0\) for \(1\le n\le12\) but \(b_{13}-b_{14}<0\); the latter, divided by \(q^{13}\), is approximately \(-0.00018947412013574786\). The included checker computes the sign as a rational fraction and separately reconstructs the canonical coefficients by formal power-series division.

## Verification

Run `python3 checker.py` from the directory containing this document. It uses only Python's standard library and compares the explicit complex-root coefficients against exact differentiation/division of the original probability generating function through index 31, as well as verifying the stated rational obstruction. These **finite checks do not certify the infinite theorem**; the uniform inequality and the moving-index limit in the proof provide the infinite arguments. No independent audit is asserted.

## Relationship to prior work

Tharshan and Wijekoon (arXiv:2110.13004v1, 25 October 2021), Proposition 1 and remarks, introduce the mixed-Poisson family and explicitly identify its geometric and negative-binomial components. Their later 2022 zero-modification article reproduces the parent model and focuses on modification, moments and estimation. These model definitions are entirely prior work. Steutel and van Harn (1979), Theorem 2.2, establish the **general** decreasing-canonical-measure characterization of discrete self-decomposability; that criterion is also prior work. The present family-specific results are the exact **uniform-over-rate** boundary \(4/9\), the isolated pure shape-three endpoint, and their all-parameter compound-Poisson property, proved directly from the model's complex-root factorization. Nearby results for different mixture shapes or count constructions do not imply this uniform boundary without new analysis.

## Limitations

The theorem does not identify the full set of individually self-decomposable interior pairs \((p,q)\). The endpoint \(p=1\) is a distributional closure point, not attained by finite \(\alpha\) under \(p=\alpha^3/(1+\alpha^3)\). The convex mixture condition \(\alpha\ge0\) is imposed to avoid a signed mixture. The finite checker is corroboration, not an independent infinite proof. Priority claims remain subject to undiscovered equivalent formulations in the extensive literature on discrete infinite divisibility and count mixtures.

## References

1. R. Tharshan and P. Wijekoon, *Poisson-modification of the Quasi Lindley distribution and its zero modification for over-dispersed count data*, arXiv:2110.13004v1, posted 25 October 2021, especially pp. 3–4. https://arxiv.org/abs/2110.13004
2. R. Tharshan and P. Wijekoon, *Zero-modified Poisson-Modification of Quasi Lindley distribution and its application*, *Statistics in Transition*, 23(4) (2022), 113–128, DOI:10.2478/stattrans-2022-0045, especially pp. 114–116. https://doi.org/10.2478/stattrans-2022-0045
3. F. W. Steutel and K. van Harn, *Discrete analogues of self-decomposability and stability*, *The Annals of Probability*, 7(5) (1979), 893–899, Theorem 2.2. https://doi.org/10.1214/aop/1176994950
