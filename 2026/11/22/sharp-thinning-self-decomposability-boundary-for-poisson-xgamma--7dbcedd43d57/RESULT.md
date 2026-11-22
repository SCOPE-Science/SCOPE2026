# Sharp thinning self-decomposability boundary for Poisson–xgamma counts

## Finding
Let \(X_\theta\) have the Poisson–xgamma count distribution defined below, with \(\theta>0\). Every such law is compound Poisson (and hence ordinarily infinitely divisible). However, under **binomial thinning** it is self-decomposable if and only if
\[
\theta\ge\theta_*=0.4253264084492916059\ldots,
\]
where \(\theta_*\) is the unique positive root of
\[
\theta^4+8\theta^3+13\theta^2-3=0.
\]
At the boundary, exactly the first two consecutive canonical coefficients are equal and all later consecutive coefficients are strictly decreasing. Below it, the first two canonical coefficients are in the opposite order. Moreover, for \(\theta=2/5\), the probability mass function is strictly decreasing at every count while the law is **not** thinning self-decomposable. Thus an ordinary compound-Poisson representation, and even a strictly decreasing mass function, do not force binomial-thinning self-decomposability.

## Assumptions and scope
For \(\theta>0\), let \(\Lambda\) have density
\[
f_\theta(t)=\frac{\theta^2}{1+\theta}\left(1+\frac{\theta t^2}{2}\right)e^{-\theta t},\qquad t>0,
\]
and, conditionally on \(\Lambda\), let \(X_\theta\) be Poisson with mean \(\Lambda\). Thus \(X_\theta\) takes values in \(\{0,1,\ldots\}\). Set \(q=(1+\theta)^{-1}\in(0,1)\), \(d=q(1-q)\), and \(u=(1+i\sqrt d)^{-1}\).

A nonnegative integer-valued law with probability-generating function \(G\) is called *binomial-thinning self-decomposable* if, for every \(c\in(0,1)\), there is a probability-generating function \(G_c\) such that
\[
G(z)=G(1-c+cz)G_c(z),\qquad 0\le z\le1.
\]
In this definition, the independent remainder need not belong to the Poisson–xgamma family. This is distinct from the ordinary infinite divisibility of \(X_\theta\) under addition.

## Proof
**1. The exact generating function.** The mixing density is a mixture of a shape-one Gamma distribution with weight \(1-q\) and a shape-three Gamma distribution with weight \(q\), both of rate \(\theta\). Direct conditioning gives
\[
G(z)=(1-q)\frac{1-q}{1-qz}+q\left(\frac{1-q}{1-qz}\right)^3
=\frac{(1-q)^2((1-qz)^2+d)}{(1-qz)^3}.
\]
In particular, its masses are
\[
p_n=q^n\left((1-q)^2+q(1-q)^3\binom{n+2}{2}\right),\qquad n\ge0.
\]
Since \((1-qz)^2+d=(1+d)(1-quz)(1-q\overline{u}z)\), power-series factorization at zero yields
\[
\log G(z)=\sum_{n=1}^\infty \lambda_n(z^n-1),\qquad
\lambda_n=\frac{q^n}{n}\left(3-2\operatorname{Re}(u^n)\right).
\]
The expression for the constant coefficient follows from \(G(1)=1\). Because \(|u|=(1+d)^{-1/2}<1\), each \(\lambda_n>0\) and their sum is finite. Consequently \(G\) is the generating function of a genuine compound-Poisson law for *every* \(\theta>0\).

**2. The criterion for thinning self-decomposability.** Put
\[
b_n=n\lambda_n=q^n\left(3-2\operatorname{Re}(u^n)\right),\qquad n\ge1.
\]
The canonical-coefficient criterion of Steutel and van Harn (1979, Theorem 2.2) says that an infinitely divisible law on the nonnegative integers with positive mass at zero is binomial-thinning self-decomposable if and only if the sequence \((b_n)_{n\ge1}\) is nonincreasing. The cited theorem uses the coefficients of \(G'(z)/G(z)\), which here are exactly \(b_{n+1}\).

An exact calculation gives
\[
b_1-b_2=\frac{q(1-q)}{(1+d)^2}P(q),\qquad
P(q)=3q^4-6q^3-5q^2+4q+1.
\]
On \([0,1]\), \(P''(q)=36q^2-36q-10<0\). Moreover \(P(0)=1\), \(P(1)=-3\), so \(P\) has a unique zero \(q_*\) in \((0,1)\), and \(P(q)\ge0\) precisely when \(q\le q_*\). Direct rational evaluations give
\[
P(7/10)=123/10000>0,\qquad
P(71/100)=-6561557/100000000<0,
\]
so \(7/10<q_*<71/100\). The substitution \(q=(1+\theta)^{-1}\) transforms \((1+\theta)^4P(q)\) into \(\theta^4+8\theta^3+13\theta^2-3\). Its derivative is strictly positive on \((0,\infty)\); hence its unique positive root is \(\theta_*=q_*^{-1}-1\). The first monotonicity inequality fails exactly when \(\theta<\theta_*\).

**3. All higher inequalities hold throughout the surviving range.** For each integer \(n\ge2\),
\[
\begin{aligned}
\frac{b_n-b_{n+1}}{q^n}
&=3(1-q)-2\operatorname{Re}\bigl(u^n(1-qu)\bigr)\\
&\ge 3(1-q)-\frac{2\sqrt{1-q}}{(1+d)^{3/2}}.
\end{aligned}
\]
Here \(|1-qu|^2=(1-q)/(1+d)\) and \(|u|^{n}\le (1+d)^{-1}\) for \(n\ge2\). Thus the right side is strictly positive whenever
\[
H(q):=9(1-q)(1+q(1-q))^3>4.
\]
Differentiation gives \(H'(q)=9(1+d)^2(7q^2-10q+2)\). On \([0,71/100]\) its only interior critical point is a maximum, so the minimum occurs at an endpoint. Both endpoints satisfy
\[
H(0)=9>4,\qquad
H(71/100)-4=\frac{57693129079919}{100000000000000}>0.
\]
Therefore \(b_n>b_{n+1}\) for all \(n\ge2\) whenever \(q\le q_*<71/100\). Together with the first difference and the canonical criterion, this proves the stated necessary-and-sufficient threshold, including equality.

**4. Strictly decreasing masses can lie outside the thinning class.** At \(\theta=2/5\) one has \(q=5/7>q_*\) and, exactly,
\[
b_1-b_2=-\frac{2390}{170569}<0.
\]
However, using the displayed mass formula, for every integer \(n\ge0\),
\[
p_{n+1}-p_n
=-q^n(1-q)^2\frac{2\bigl(5(n-1)^2+4\bigr)}{343}<0.
\]
This proves the contrasting monotone-mass example on the whole infinite support.

## Verification
The standalone \(\texttt{checker.py}\) uses exact rational arithmetic (Python standard library). Run \(\texttt{python3 checker.py}\) alongside this file. It checks the mixing and mass formulas, polynomial signs, the first canonical difference, the strict decreasing-mass witness and finite sets of further canonical differences for rational parameters. These finite diagnostics confirm the critical algebra but **do not** establish either infinitely many inequalities or global originality; both mathematical quantifiers are handled in the analytic proof above. The theorem uses no numerical rounding for acceptance; the displayed decimal is illustrative.

## Relationship to prior work
Para, Jan and Bakouch (first public online publication 1 May 2020) introduced the Poisson–xgamma count law and derived its basic distributional characteristics. Altun, Cordeiro and Ristić (first online 9 February 2021) independently analyzed a Poisson–xgamma mixture, including its use as *innovations* in an INAR(1) model; specifying an innovation distribution is not the same as identifying when that distribution can be an INAR(1) *stationary marginal* under every thinning rate. The 1979 Steutel–van Harn theorem supplies the general canonical criterion, but does not evaluate the Poisson–xgamma coefficients, derive the quartic boundary, or establish the family-specific all-degree reduction in this finding. The new contribution assessed here is the exact family-specific phase boundary, not the general criterion or the original distribution.

## Limitations
The claim concerns ordinary compound-Poisson infinite divisibility and binomial-thinning self-decomposability for the specified one-parameter Poisson–xgamma law only; it does not claim closure of its parametric family under thinning, nor an estimator or a uniform large-sample result. The mathematical argument has not undergone independent external validation. The accessible earlier papers do not identify this threshold, but exhaustiveness of all prior literature cannot be guaranteed. Some later two-parameter generalizations have not been examined in their complete publisher text; any unnoticed earlier broader theorem could affect historical priority.

## References
1. B. A. Para, T. R. Jan and H. S. Bakouch (2020), *Poisson Xgamma distribution: A discrete model for count data analysis*, Model Assisted Statistics and Applications **15**, 139–151. First published online 1 May 2020. https://doi.org/10.3233/MAS-200484
2. E. Altun, G. M. Cordeiro and M. M. Ristić (2021 online; 2022 issue), *An one-parameter compounding discrete distribution*, Journal of Applied Statistics **49**, 1935–1956. https://doi.org/10.1080/02664763.2021.1884846 ; open full text https://pmc.ncbi.nlm.nih.gov/articles/PMC9225500/
3. F. W. Steutel and K. van Harn (1979), *Discrete analogues of self-decomposability and stability*, Annals of Probability **7**, 893–899, especially Theorem 2.2. https://doi.org/10.1214/aop/1176994950 ; https://pure.tue.nl/ws/files/1956807/Metis199408.pdf
