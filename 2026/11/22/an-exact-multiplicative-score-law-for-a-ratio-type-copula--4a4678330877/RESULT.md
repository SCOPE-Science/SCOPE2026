# An exact multiplicative-score law for a ratio-type copula

## Finding

Let \((U,V)\) have standard-uniform marginals and the ratio-type copula
\[
C(u,v)=\frac{uv(u+v)}{1+uv},\qquad 0\le u,v\le1.
\]
For the scalar product \(Z=UV\), the entire distribution is
\[
\boxed{\Pr(Z\le z)=\frac{4z}{(1+z)^2}},\qquad 0\le z\le1,
\]
and its density on \((0,1)\) is \(4(1-z)/(1+z)^3\).

The aggregate negative-log score \(W=-\log U-\log V=-\log Z\) consequently satisfies
\[
\boxed{\Pr(W\le w)=\tanh^2(w/2)},\qquad w\ge0.
\]
Equivalently, if \(L_1,L_2\) are independent standard logistic random variables, then
\[
W\ \stackrel{d}{=}\ \max\{|L_1|,|L_2|\}.
\]
In particular,
\[
\mathbb E W=2,\qquad \operatorname{Var}(W)=8\log2-4.
\]
There is also a **unique crossing of the multiplicative-score CDF with independence**. If \(Z_0\) is the product of two independent uniform random variables, then \(\Pr(Z_0\le z)=z(1-\log z)\). There exists exactly one \(z_*\in(0,1)\), numerically \(z_*=0.0992045541719469983\ldots\), with
\[
\Pr(Z\le z)<\Pr(Z_0\le z)\quad(0<z<z_*),\qquad
\Pr(Z\le z)>\Pr(Z_0\le z)\quad(z_*<z<1).
\]
The crossing is the unique positive root \(t_*=-\log z_*\) of \(4/(1+e^{-t})^2=1+t\). Thus the dependence does not stochastically order the product uniformly against independence: its impact reverses exactly once with the tail threshold.

The exact \(p\)-quantile of \(Z\), for \(0<p<1\), is
\[
Q_Z(p)=\frac{p}{2-p+2\sqrt{1-p}}.
\]

## Assumptions and scope

The joint distribution is specified exactly by the displayed copula, with no extra parameters, conditional independence, or restrictions beyond \(u,v\in[0,1]\). The probability statements cover all real \(z\in[0,1]\) and \(w\ge0\), and the density statement applies to \(0<z<1\). A standard logistic random variable here has distribution function \(x\mapsto(1+e^{-x})^{-1}\). The result concerns the **ordinary random-variable product** \(UV\), not the Markov or star product of copulas.

The copula is absolutely continuous: it has uniform boundary margins and nonnegative joint density
\[
c(u,v)=\frac{2(u+v)}{(1+uv)^3}\ge0.
\]
This also verifies directly that the stipulated law is valid.

## Proof

For \(0<z<1\), decompose the event \(UV\le z\) into \(U\le z\) and \(z<U<1\). The first event has probability \(z\). Conditional on \(U=u\), the conditional distribution function of \(V\) equals \(\partial_u C(u,v)\), because \(U\) is continuously uniform. Direct differentiation gives
\[
\partial_u C(u,v)=\frac{2uv+v^2+u^2v^2}{(1+uv)^2}.
\]
Consequently, whenever \(z<u<1\),
\[
\Pr(V\le z/u\mid U=u)=\frac{2z+z^2+z^2/u^2}{(1+z)^2}.
\]
Integrating the exact conditional probability over the remaining values of \(u\),
\[
\begin{aligned}
\Pr(UV\le z)
&=z+\int_z^1\frac{2z+z^2+z^2/u^2}{(1+z)^2}\,du\\
&=z+\frac{(2z+z^2)(1-z)+(z-z^2)}{(1+z)^2}\\
&=\frac{4z}{(1+z)^2}.
\end{aligned}
\]
The formula extends to \(z=0,1\) by continuity; differentiating it yields the asserted density.

For \(w\ge0\), monotone transformation of \(Z\) gives
\[
\Pr(W\le w)=\Pr(Z\ge e^{-w})
=1-\frac{4e^{-w}}{(1+e^{-w})^2}
=\left(\frac{1-e^{-w}}{1+e^{-w}}\right)^2
=\tanh^2(w/2).
\]
To establish uniqueness of the independence comparison, put \(t=-\log z\ge0\), \(x=e^{-t}\), and consider
\[
H(t)=\frac{4}{(1+e^{-t})^2}-(1+t).
\]
The CDF difference is \(zH(t)\). Its derivative has the exact factorization
\[
H'(t)=\frac{8x-(1+x)^3}{(1+x)^3}
=\frac{(1-x)(x^2+4x-1)}{(1+x)^3}.
\]
Since \(0<x<1\) when \(t>0\), the derivative is positive until \(t_0=\log(2+\sqrt5)\) and negative afterward. Also \(H(0)=0\), \(H(t)>0\) for sufficiently small positive \(t\), and \(H(t)\to-\infty\) as \(t\to\infty\). Hence exactly one positive root \(t_*\) exists, and converting back to \(z\) proves the stated two strict inequalities. The displayed decimal is for orientation only and plays no part in the global uniqueness proof.

The standard logistic distribution satisfies
\[
\Pr(|L|\le w)=\frac{1}{1+e^{-w}}-\frac{1}{1+e^w}=\tanh(w/2).
\]
Independence of \(L_1,L_2\) therefore gives exactly the same distribution for \(\max\{|L_1|,|L_2|\}\), proving the representation.

Since \(\Pr(W>w)=\operatorname{sech}^2(w/2)\), the survival-integral identities imply
\[
\mathbb EW=\int_0^\infty\operatorname{sech}^2(w/2)\,dw=2,
\]
and
\[
\mathbb EW^2=2\int_0^\infty w\operatorname{sech}^2(w/2)\,dw=8\log2.
\]
For the last integral, an antiderivative is \(2w\tanh(w/2)-4\log\cosh(w/2)\), with limit \(4\log2\) at infinity and value \(0\) at the origin. Subtracting the squared mean proves the variance formula. Solving \(p=4z/(1+z)^2\) for its solution \(z\in(0,1)\) and rationalizing gives the quantile formula.

## Verification

`CHECK.py` independently differentiates the copula, verifies its margins and nonnegative-density formula, symbolically reconstructs the conditional-integral product distribution, checks the logistic transformation and the exact antiderivatives used for moments, and checks representative interior values. Run with `python CHECK.py` and the `sympy` package. The checker reports 13 symbolic identities and 16 numerical/domain assertions passing. These finite numerical values are diagnostics, not proofs of the statements for all \(z\) or \(w\); those follow from the displayed exact algebra and integration.

## Relationship to prior work

Chesneau (2022) introduced and studied precisely this ratio-type copula, including its dependence, association and tail properties. That original construction and all copula-validity facts are prior work, not new claims. The present contribution instead identifies the **complete law of the scalar multiplicative score**, its logistic order-statistic representation, its exact moment/quantile calibration, and the unique reversal in its comparison with the independent product. Chesneau (2023) examined different parametric ratio copulas and their **copula star product**, which is a different operation from multiplication of the two uniform observations. The publicly accessible abstracts and examined 2023 full text did not disclose the result stated here; the entire 2022 publisher text was not accessible for a conclusive priority comparison.

The distinction is substantive for multiplicative-score calibration. Under independence the analogous product has distribution \(z(1-\log z)\) on \((0,1)\), and its negative logarithm has the \(\operatorname{Gamma}(2,1)\) law. For the ratio-type dependence above, \(\Pr(UV\le z)\sim4z\) as \(z\downarrow0\), whereas the independent product has probability asymptotic to \(z\log(1/z)\). The ratio of the two small-product probabilities therefore tends to \(0\); the exact unique crossover above shows that the direction reverses at intermediate thresholds. The expected aggregate negative-log score remains \(2\) by uniformity of the margins.

## Limitations

This result concerns only the specified two-dimensional fixed copula. It does not classify the scalar product distribution for the three parametric extensions, nor does it provide an independent historical-priority or publication certification. The original 2022 publisher full text could not be examined; it remains possible that a related product identity is contained in its inaccessible main text or appendices. The logistic representation is an equality **in distribution**, not a coupling in which the original uniform coordinates are independent logistic transforms.

## References

1. C. Chesneau, “Some new ratio-type copulas: theory and properties,” *Applicationes Mathematicae* **49** (2022), 79–101; first public online date 24 February 2022. DOI: https://doi.org/10.4064/am2436-12-2021.
2. C. Chesneau, “Theoretical Advancements on a Few New Dependence Models Based on Copulas with an Original Ratio Form,” *Modelling* **4** (2023), 102–132. DOI: https://doi.org/10.3390/modelling4020008.
