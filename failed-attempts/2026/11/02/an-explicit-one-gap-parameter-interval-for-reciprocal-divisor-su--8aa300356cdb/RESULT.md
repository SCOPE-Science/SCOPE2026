# An explicit one-gap parameter interval for reciprocal divisor-sum ranges

## Finding
For every real parameter \(19/10\le r\le191/100\), define \(\sigma_{-r}(n)=\sum_{d\mid n}d^{-r}\), \(u=2^{-r}\), \(v=3^{-r}\), and \(W=\zeta(r)(1-u)(1-v)\). Then the topological closure of the positive-integer range is **exactly**
\[
\overline{\{\sigma_{-r}(n):n\ge1\}}=[1,W]\;\cup\;[1+v,\zeta(r)].
\]
The two displayed intervals are disjoint; thus the range has exactly one bounded gap, \((W,1+v)\). The set of positive integers whose values lie in the first interval is precisely \(\{n:\gcd(n,6)=1\}\), of natural density \(1/3\). The complementary set, of natural density \(2/3\), takes values in the second interval.

## Assumptions and scope
The parameter \(r\) is an arbitrary **real**, not necessarily rational, number in the **closed** interval \([19/10,191/100]\). All closures are in the usual real topology. The Riemann zeta series \(\zeta(r)=\sum_{n\ge1}n^{-r}\) converges because \(r>1\). A finite prime-power Euler factor is \(S_a(z)=\sum_{j=0}^{a}z^j\) for integers \(a\ge0\); put \(S_\infty(z)=(1-z)^{-1}\) for \(0<z<1\). These infinite factors and infinite prime products are closure limits, not finite inputs.

## Proof
**1. A prime-tail interval.** Let \(p_j\) be the \(j\)-th prime and \(T_j=\prod_{i>j}(1-p_i^{-r})^{-1}\). If \(1+p_j^{-r}\le T_j\) for every \(j\ge3\), the closure of the values supported only on primes at least five is \([1,T_2]=[1,W]\). To see the mechanism, write \(z=p_j^{-r}\). The intervals \(S_a(z)[1,T_j]\), for \(a=0,1,\ldots\), overlap consecutively because \(S_{a+1}(z)/S_a(z)\le1+z\le T_j\). Their union together with the limit interval is \([1,T_j/(1-z)]\). Iterating this choice over the primes yields every target in \([1,W]\) as a limit of finite Euler products: the unselected tail-product upper bounds tend to one. This is also the prime-tail greedy lemma of Sanna (2015, Lemma 2.3).

For \(1<r\le2\), Defant's consecutive-prime lemma and its proof of Theorem 2.2 give \(F_j=(1+p_j^{-r})\prod_{i\le j}(1-p_i^{-r})^{-1}<\zeta(r)\) for every \(j\ge5\), while \(F_3<F_4\). Thus one need only verify the prime-seven inequality \(1+7^{-r}<T_4\), for it implies the prime-five inequality as well. The exact rational interval certificate below verifies this strictly and also separately checks the prime-eleven inequality. Hence the required interval for the primes at least five holds **uniformly** in \(r\).

**2. Add the prime three.** Since \(S_{a+1}(v)/S_a(v)\) decreases with \(a\), the single condition \(S_2(v)/S_1(v)<W\) makes all scaled copies \(S_b(v)[1,W]\) for \(b\ge1\) overlap. Their union has lower endpoint \(1+v\) and upper endpoint \(W/(1-v)\). The \(b=0\) interval is \([1,W]\). The strict inequality \(W<1+v\) separates them, giving
\[
\overline{\{\sigma_{-r}(n):2\nmid n\}}=[1,W]\cup[1+v,W/(1-v)].
\]

**3. Add the prime two.** The copies with exponent \(a\ge1\) of the first band are
\(S_a(u)[1,W]\). They overlap when \(S_2(u)/S_1(u)<W\) and their union is \([1+u,W/(1-u)]\). The copies with exponent \(a\ge1\) of the second band are \(S_a(u)[1+v,W/(1-v)]\). They overlap if \(S_2(u)/S_1(u)<W/(1-v^2)\) and their union is \([(1+u)(1+v),W/((1-u)(1-v))]\). Since \(W/((1-u)(1-v))=\zeta(r)\), it remains to join these two positive-exponent bands to the \(a=0\) upper band. The two strict inequalities
\[
1+u<\frac{W}{1-v},\qquad (1+u)(1+v)<\frac{W}{1-u}
\]
accomplish exactly this. The \(a=0\) lower band \([1,W]\) remains isolated, since every integer divisible by two or three has divisor sum at least \(1+v>W\). Thus the stated two-interval formula follows.

**4. Uniform strict inequalities, with an exact certificate.** The accompanying standalone `verify_divisor_gap.py` establishes all eight strict tests in Steps 1–3 for **every real parameter in the interval**, not only finitely many sample parameters. It evaluates \(n^{-a/b}\) at the rational endpoints \(a/b=19/10,191/100\) by integer-power comparisons with rational brackets of mesh \(10^{-9}\), for each \(1\le n\le1024\). The zeta tail has rigorous integral bounds
\[
\frac{(1025)^{1-r}}{r-1}\le\sum_{n>1024}n^{-r}\le\frac{(1024)^{1-r}}{r-1}.
\]
All accumulated endpoints and comparisons use exact integers or rational fractions; floating-point output merely prints the already certified positive gaps. The factors \(u(r),v(r),W(r)\), and \(T_j(r)\) are decreasing in \(r\), while \(S_2(z)/S_1(z)=1+z^2/(1+z)\) is increasing in \(z\). Consequently, the endpoints give valid simultaneous worst-case bounds throughout the real parameter interval. The certificate verifies respectively (minimum slack, expressed conservatively to nine decimal places): positive separation \(W<1+v\), \(0.000595086\); prime-seven and prime-eleven tail tests, \(0.016694070\) and \(0.020301666\); higher three powers, \(0.105502860\); lower and upper two-power bands, \(0.062563304\) and \(0.079658833\); and the two band-joining tests, \(0.007712351\) and \(0.099782365\). Each printed decimal lower slack is backed by a strict rational inequality in the code.

**5. Component densities.** An integer coprime to six has no two- or three-factor and hence has \(\sigma_{-r}(n)\le W\). Conversely, if \(2\mid n\) or \(3\mid n\), then \(\sigma_{-r}(n)\ge\min(1+u,1+v)=1+v\). The standard elementary density of \(\gcd(n,6)=1\) is \(\varphi(6)/6=1/3\), giving component densities \(1/3\) and \(2/3\).

## Verification
Run `python3 verify_divisor_gap.py` with Python 3 and no third-party packages. Successful execution ends with `VERIFY_OK exact rational interval certificate for every real 1.9<=r<=1.91`. The code checks the endpoint zeta bounds and every inequality required by the proof with `fractions.Fraction`, and also independently checks 33,605 consecutive-prime ratios in the finite range used by Defant; this proves the inequalities for all real parameters by analytic monotonicity. The code is a finite rational certificate for the explicit estimates; the infinitely many primes are handled by Defant's proved prime-ratio lemma and the prime-tail argument, not enumerated.

## Relationship to prior work
Defant (2015, arXiv:1506.05432v1) proves the density threshold near \(1.8877909\), establishes the requisite consecutive-prime comparison for \(r\le2\), and asks which parameters yield precisely one gap. Sanna (2015, arXiv:1507.08091v1) proves all closures consist of finitely many intervals with rational component densities and provides a **general fixed-parameter algorithm**; its explicit worked example \(r=2\) gives three intervals, not the present two-interval parameter segment. The new contribution is an explicit, rigorously certified **whole real interval of parameters** with exact component endpoints and densities, derived using these earlier techniques. Zubrilina (2017, arXiv:1711.02871v1) and Achenjang–Berger (2018, arXiv:1808.07550v1) study component bounds and gaps but do not state this uniform formula in the inspected passages. Literature priority is not independently settled.

## Limitations
The result is asserted only for \(19/10\le r\le191/100\). It does not identify the maximal connected parameter interval on which one gap persists, nor does it determine the exact transition parameters. The proof depends on the published consecutive-prime lemma for \(1<r\le2\) and the listed exact-arithmetic inequalities. A general earlier interval-classification theorem not found in the inspected literature could supersede the priority claim. No independent mathematical audit was performed.

## References
1. Colin Defant, *On the Density of Ranges of Generalized Divisor Functions*, arXiv:1506.05432v1 (first public version 2015-06-17), https://arxiv.org/abs/1506.05432.
2. Carlo Sanna, *On the closure of the image of the generalized divisor function*, arXiv:1507.08091v1 (2015-07-29); *Uniform Distribution Theory* **12** (2017), 77–90, https://arxiv.org/abs/1507.08091.
3. Nina Zubrilina, *On the Number of Connected Components of Ranges of Divisor Functions*, arXiv:1711.02871v1 (2017-11-08), https://arxiv.org/abs/1711.02871.
4. Niven Achenjang and Aaron Berger, *On Gaps in the Closures of Images of Divisor Functions*, arXiv:1808.07550v1 (2018-08-22), https://arxiv.org/abs/1808.07550.
