# Rank-one covariance and finite-energy contrasts of divisor counts in proportional windows

## Finding

For fixed real constants \(0<a_j<b_j<\infty\) and real coefficients \(c_j\), \(1\le j\le m\), let \(y\) tend to infinity through positive integers, and let \(n\) be uniformly distributed over a complete common divisibility period (defined below). Put
\[
D_j(n;y)=\#\{d\mid n:a_jy<d\le b_jy\},\qquad
S_y(n)=\sum_{j=1}^m c_jD_j(n;y),
\]
\[
v=\sum_{j=1}^m c_j\log(b_j/a_j),\quad
G(t)=\sum_{j=1}^m c_j\bigl(H_{\lfloor b_j/t\rfloor}-H_{\lfloor a_j/t\rfloor}\bigr),
\]
where \(H_0=0\) and \(H_k=\sum_{r=1}^k1/r\) for positive integers \(k\). Write \(\kappa=6/\pi^2\) and \(B=\max_j b_j\).

**Theorem (complete bounded-variance criterion).** If \(v\ne0\), then
\[
\operatorname{Var}(S_y)=\kappa v^2\log y+O_{\mathbf a,\mathbf b,\mathbf c}(1).
\]
If \(v=0\), then
\[
\boxed{\displaystyle\lim_{y\to\infty}\operatorname{Var}(S_y)
=\kappa\int_0^B G(t)^2\,\frac{dt}{t}<\infty.}
\]
Consequently the variance remains bounded as \(y\to\infty\) **if and only if** \(\sum_jc_j\log(b_j/a_j)=0\), and the leading covariance matrix of any fixed family of windows is rank one:
\[
\operatorname{Cov}(D_i,D_j)=\kappa\log(b_i/a_i)\log(b_j/a_j)\log y+O_{\mathbf a,\mathbf b}(1).
\]

In particular, take two **disjoint** consecutive dyadic windows
\[
D_0=\#\{d\mid n:y<d\le2y\},\qquad
D_1=\#\{d\mid n:2y<d\le4y\}.
\]
They have \(\operatorname{Corr}(D_0,D_1)\to1\), although their difference has the strictly positive finite limiting variance
\[
\begin{aligned}
C_{\rm dyad}&=\lim_{y\to\infty}\operatorname{Var}(D_0-D_1)\\
&=\frac6{\pi^2}\int_0^4\left(2H_{\lfloor2/t\rfloor}-H_{\lfloor1/t\rfloor}-H_{\lfloor4/t\rfloor}\right)^2\frac{dt}{t}\\
&=0.5082185\ldots>0.
\end{aligned}
\]
This displays almost-perfect linear correlation together with a persistent, explicitly determined second-order contrast. Moreover, the cited divisor-presence estimates imply that both dyadic counts (and hence their difference) converge to zero in probability, although the difference has strictly positive limiting variance. This is a failure of uniform integrability of the squared difference, not a contradiction.

## Assumptions and scope

All window endpoints and coefficients are **fixed** as \(y\to\infty\). Their endpoints need not be rational. Choose \(L_y=\operatorname{lcm}(1,2,\ldots,\lfloor By\rfloor)\), with \(L_y=1\) if \(\lfloor By\rfloor<1\); probabilities and expectations are uniform on \(n\in\{1,\ldots,L_y\}\). Thus each divisor indicator \(1_{d\mid n}\) is exactly periodic and has mean \(1/d\), while paired indicators have mean \(1/\operatorname{lcm}(d,e)\). The covariance formula and limits also hold if \(n\) is uniform in \(1\le n\le X=X(y)\) with \(y^2/X(y)\to0\): the direct pair-counting discrepancy is \(O_{\mathbf a,\mathbf b,\mathbf c}(y^2/X)\). All logarithms are natural. No statement about central limit laws is asserted.

## Proof

**1. Exact second-moment decomposition.** Define the finitely supported weights \(w_y(d)=\sum_j c_j\mathbf1_{a_jy<d\le b_jy}\), for positive integers \(d\le\lfloor By\rfloor\). Then \(S_y=\sum_d w_y(d)\mathbf1_{d\mid n}\). Therefore
\[
\mathbb ES_y=\sum_{d\ge1}\frac{w_y(d)}d
=\sum_jc_j\bigl(H_{\lfloor b_jy\rfloor}-H_{\lfloor a_jy\rfloor}\bigr)
=v+O(y^{-1}).
\]
The identity \(\gcd(d,e)=\sum_{r\mid\gcd(d,e)}\varphi(r)\) gives the **exact** finite-period formula
\[
\begin{aligned}
\mathbb ES_y^2
&=\sum_{d,e}\frac{w_y(d)w_y(e)}{\operatorname{lcm}(d,e)}
=\sum_{d,e}\frac{w_y(d)w_y(e)\gcd(d,e)}{de}\\
&=\sum_{r\le By}\frac{\varphi(r)}{r^2}
\left(\sum_{k\ge1}\frac{w_y(rk)}k\right)^2
=\sum_{r\le By}\frac{\varphi(r)}{r^2}G(r/y)^2.
\end{aligned}
\]
Here the harmonic-floor expression is exact even for irrational endpoints, because \(rk\le by\) is equivalent to \(k\le\lfloor by/r\rfloor\).

**2. The totient measure.** The classical summatory totient estimate
\[
\sum_{r\le x}\varphi(r)=\frac{3}{\pi^2}x^2+O(x\log(2x))
\]
implies, by partial summation,
\[
\sum_{r\le x}\frac{\varphi(r)}{r^2}=\kappa\log x+O(1).
\]
It also implies that, for every fixed \(0<u<v\),
\[
\lim_{y\to\infty}\sum_{uy<r\le vy}\frac{\varphi(r)}{r^2}=\kappa\log(v/u).
\]
In particular, these discrete measures converge against any bounded piecewise-continuous function on compact intervals inside \((0,\infty)\), provided it has only finitely many jump discontinuities there.

**3. Boundary at zero.** The harmonic-number estimate \(H_{\lfloor s/t\rfloor}-H_{\lfloor a/t\rfloor}=\log(s/a)+O_{a,s}(t)\) as \(t\downarrow0\) gives \(G(t)=v+O(t)\), uniformly for sufficiently small positive \(t\). Since \(G(t)=0\) for \(t>B\), and the floor-harmonic function has finitely many discontinuities in every compact subinterval of \((0,B]\), step 2 applies away from zero.

If \(v\ne0\), write \(G(t)=v+R(t)\) for \(0<t\le B\). The error \(R(t)=O(t)\) near zero implies
\[
\sum_{r\le By}\frac{\varphi(r)}{r^2}\bigl(2vR(r/y)+R(r/y)^2\bigr)=O(1),
\]
because \(\varphi(r)/r^2\le1/r\), \(R(r/y)=O(r/y)\) for small \(r/y\), and the remainder is bounded elsewhere. Thus \(\mathbb ES_y^2=\kappa v^2\log y+O(1)\); subtracting \((\mathbb ES_y)^2=v^2+O(1/y)\) proves the first case.

If \(v=0\), then \(G(t)=O(t)\) near zero. For every sufficiently small \(\varepsilon>0\),
\[
\sum_{r\le\varepsilon y}\frac{\varphi(r)}{r^2}G(r/y)^2
\ll\frac1{y^2}\sum_{r\le\varepsilon y}r\ll\varepsilon^2.
\]
On \([\varepsilon,B]\), the exact sum converges to \(\kappa\int_\varepsilon^B G(t)^2dt/t\) by step 2. As \(\varepsilon\downarrow0\), the displayed uniform tail bound proves convergence of the full sum to the finite integral. Its squared mean tends to zero. This proves the second case, the bounded-variance iff criterion, and—by polarization—the rank-one covariance formula.

**4. Dyadic corollary.** Both dyadic intervals have logarithmic width \(\log2\), so their individual variances and covariance are each \(\kappa(\log2)^2\log y+O(1)\). Their correlation therefore tends to one. Ford's interval-presence estimate, as stated in the introduction of the cited 2026 preprint, gives \(\mathbb P(D_i>0)\to0\) for both windows under the stated complete-period sampling; thus the difference tends to zero in probability even as its limiting variance remains positive. Their difference is balanced, and \(G(t)=2H_{\lfloor2/t\rfloor}-H_{\lfloor1/t\rfloor}-H_{\lfloor4/t\rfloor}\). For \(2<t<4\), this is exactly \(-1\), so the constant satisfies \(C_{\rm dyad}\ge\kappa\log2>0\). The decimal displayed above is a numerical evaluation of the integral, not an asserted closed form.

## Verification

The standalone Python 3 script `verify.py` makes independent *finite* checks, not a substitute for the preceding infinite proof. It enumerates full common periods for \(y=1,2,3\), compares all two-window first and second moments with the exact totient/harmonic identity using rational arithmetic, and verifies numerical convergence of the dyadic contrast at \(y=100,1000,5000\). It separately integrates the piecewise-constant integrand on \([1/3000,4]\), giving approximately \(0.508218525\); the omitted portion tends to zero by the \(O(t)\) bound in the proof. Run `python3 verify.py` in the same directory. The exact period cases are exhaustive for those three finite examples only.

## Relationship to prior work

Ford, Gabdullin and Pratt's November 11, 2026 preprint studies the count of integers possessing at least a prescribed number of divisors in a single dyadic interval. Its theorem addresses frequency tails rather than the joint covariance and exact bounded-variance contrast classification proved here. Ford's 2008 work determines asymptotic frequencies for the presence of divisors in general intervals. The exact second-moment identity uses the classical totient expansion of a greatest common divisor; novelty is sought in the resulting **all-proportional-window rank-one covariance law, necessary-and-sufficient bounded-variance classification, and positive explicit dyadic contrast limit**, not in that classical identity. A conference synopsis by Kovaleva mentions ongoing work on the statistics of the same divisor-count variable; its unpublished conclusions cannot be compared, so implicit overlap remains a material risk.

## Limitations

Fixed window parameters are essential; no uniformity for endpoints varying with \(y\), distributional convergence, or higher moments is claimed. The general integral can vanish for identically cancelling combinations, and the theorem classifies boundedness of variance rather than nondegeneracy of every balanced contrast. The numerical constant is approximate; the exact defining expression is the convergent integral. The literature comparison is limited by the absence of an accessible full written treatment of Kovaleva's ongoing project. The finite checker does not certify the analytic asymptotics, which follow from the proof and a standard classical totient estimate. Independent mathematical validation has not been performed.

## References

1. K. Ford, M. R. Gabdullin, and K. Pratt, *Integers with many divisors in a dyadic interval*, arXiv:2611.15534v1, publicly dated November 11, 2026. https://arxiv.org/html/2611.15534v1
2. K. Ford, *The distribution of integers with a divisor in a given interval*, Annals of Mathematics **168** (2008), 367–433. https://arxiv.org/html/math/0401223v5
3. K. Ford and G. Tenenbaum, *The distribution of integers with at least two divisors in a short interval*, Quarterly Journal of Mathematics **58** (2007), 187–201. https://doi.org/10.1093/qmath/ham001
4. V. Kovaleva, *Statistics of the divisor function on intervals (y,2y]*, conference presentation synopsis, marked work in progress. https://www.math.mcgill.ca/darmon/qvnts/kovaleva.html
