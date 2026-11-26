# Sharp bounded-variation norm of the cubic Legendre projector

## Finding

Let \(\mathcal P_3\) be the unweighted \(L^2([-1,1])\)-orthogonal projector onto real polynomials of degree at most three, restricted to real \(BV(-1,1)\) functions. If \(\operatorname{Var}(f)=|Df|((-1,1))\), then its **exact sharp variation operator norm on functions modulo constants** is

\[
\boxed{\sup_{\operatorname{Var}(f)>0}\frac{\operatorname{Var}(\mathcal P_3 f)}{\operatorname{Var}(f)}=\frac{15\sqrt{21}}{28}-\frac58=1.829951265\ldots.}
\]

The central jump \(f(t)=\mathbf 1_{(0,1)}(t)\) attains equality. Because the projector is linear, the same sharp constant governs the variation of differences of two inputs. This is a statement about the completed degree-three projection, not about convergence rates as polynomial degree grows.

## Assumptions and scope

All functions are real and defined up to almost-everywhere equivalence on \((-1,1)\). Their distributional derivatives are finite signed Radon measures. The normalizations of the Legendre polynomials are \(P_k(1)=1\), \(\int_{-1}^1P_kP_j=2\delta_{jk}/(2k+1)\), and

\[
(\mathcal P_3 f)(x)=\sum_{k=0}^{3}\frac{2k+1}{2}P_k(x)\int_{-1}^1f(t)P_k(t)\,dt.
\]

The variation seminorm is unweighted and refers only to the open interval, excluding spurious effects from endpoint representatives. Since constants are preserved, passage to the quotient by constants is well-defined.

## Proof

**1. Reduction to jumps.** For \(-1<s<1\), put \(H_s=\mathbf 1_{(s,1)}\) and \(Q_s=(\mathcal P_3H_s)'\). By the Legendre antiderivative identity,

\[
Q_s(x)=\frac12\sum_{k=1}^3\bigl(P_{k-1}(s)-P_{k+1}(s)\bigr)P_k'(x)
=\frac{15}{32}(1-s^2)\bigl((35s^2-7)x^2+8sx+3-7s^2\bigr).
\]

For a general \(f\in BV(-1,1)\), its distributional derivative \(\mu=Df\) yields \(f=c+\int H_s\,d\mu(s)\) almost everywhere (with an appropriate constant). Fubini and the invariance of constants imply \((\mathcal P_3f)'(x)=\int Q_s(x)\,d\mu(s)\), hence

\[
\operatorname{Var}(\mathcal P_3f)\le \bigl(\sup_{-1<s<1}V(s)\bigr)|\mu|((-1,1)),\qquad V(s)=\int_{-1}^1|Q_s(x)|\,dx.
\]

Each \(H_s\) has unit variation, so equality of the operator norm with \(\sup_sV(s)\) follows. Reflection makes \(V(s)=V(-s)\); consider \(0\le s\le1\).

**2. Central jump.** At \(s=0\), \(Q_0(x)=15(3-7x^2)/32\), with roots \(\pm\sqrt{3/7}\). Direct integration gives

\[
V(0)=\frac{15\sqrt{21}}{28}-\frac58>\frac95.
\]

**3. Exact upper bound near the center.** Let \(u=s^2\), \(A(u)=35u-7\), \(d(u)=245u^2-138u+21\), and \(v(u)=6u-7u^2\). For \(0\le s\le1/4\), the quadratic in the expression for \(Q_s\) is positive at the origin and negative at both endpoints, with two zeros strictly inside the interval. Elementary integration between its zeros yields

\[
V(s)=\frac54\frac{(1-u)d(u)^{3/2}}{A(u)^2}-\frac58(1-u)(7u+1).
\]

To prove \(V(s)\le V(0)\), it is enough to establish

\[
2(1-u)d(u)^{3/2}\le A(u)^2\left(\frac67\sqrt{21}+v(u)\right).
\]

Both sides are nonnegative on \(0\le u\le1/16\). The difference of their squares is

\[
B(u)=A(u)^4\left(\frac{108}{7}+v(u)^2+\frac{12}{7}\sqrt{21}\,v(u)\right)-4(1-u)^2d(u)^3.
\]

As \(v(u)\ge0\) and \(\sqrt{21}>4\), this is at least \(P(u)=A(u)^4(108/7+v(u)^2+48v(u)/7)-4(1-u)^2d(u)^3\). Its constant coefficient vanishes. The polynomial \(P(u)/u\), expressed in the degree-seven Bernstein basis after \(u=t/16\), has precisely these eight coefficients, all positive:

\[
162288,\ \frac{504825}{4},\ \frac{43471129}{448},\ \frac{2112076241}{28672},\ \frac{31610427257}{573440},\ \frac{446693101541}{11010048},\ \frac{61396126549}{2097152},\ \frac{5533791782221}{268435456}.
\]

Because the Bernstein basis is nonnegative on \(0\le t\le1\) and sums to one, \(P(u)\ge0\) throughout the interval (strict for positive \(u\)). This proves \(V(s)\le V(0)\) for \(0\le s\le1/4\).

**4. Exact exhaustive interval bound away from the center.** Differentiate the explicit quadratic to obtain

\[
\partial_sQ_s(x)=\frac{15}{32}\left[(84s-140s^3)x^2+(8-24s^2)x-20s+28s^3\right].
\]

For \(0\le s\le1\) and \(|x|\le1\), the absolute values of the three coefficients inside brackets are at most \(56\), \(16\), and \(8\), respectively. Hence \(|\partial_sQ_s(x)|\le75/2\). Partition \([1/4,1]\) into 300 closed intervals of length \(1/400\), centered at \(s_j=1/4+(2j+1)/800\) for \(j=0,\ldots,299\). It follows that

\[
V(s)\le V(s_j)+\frac3{32}\quad\text{whenever }|s-s_j|\le\frac1{800}.
\]

The accompanying exact-rational checker establishes \(V(s_j)<17/10\) for all 300 centers. It does so without floating-point decisions: it isolates every real root of each rational quadratic using rigorously enclosing rational square roots, integrates its signed polynomial exactly off the root enclosures, and bounds any excluded root enclosure by its rational length times \(|a|+|b|+|c|\). Thus the finite certificate covers the entire continuum \(1/4\le s\le1\), giving

\[
V(s)<\frac{17}{10}+\frac3{32}=\frac{287}{160}<\frac95<V(0).
\]

Together with step 3 and reflection, this proves \(\sup_sV(s)=V(0)\). The central jump attains the norm, completing the theorem.

## Verification

Run \(\texttt{python3 check_legendre.py}\) with the standard Python library. The script verifies the exact Bernstein coefficient certificate and all 300 covering intervals using rational arithmetic, including precise square-root bracketing and polynomial integration. It reports a largest rational upper enclosure of approximately \(1.683715\) among the 300 centers. The executable's finite arithmetic is part of a complete continuum proof because the analytic derivative bound covers every point between the tested centers. No finite sampling of input signals is used to infer the operator norm.

## Relationship to prior work

Leonardo E. Figueroa, *Orthogonal polynomial projection error measured in Sobolev norms in the unit ball* (arXiv:1607.00930, first public posting July 4, 2016), establishes polynomial projection estimates in weighted \(L^2\)-Sobolev norms via differentiation–projection commutators. Its studied Banach/Hilbert norms and degree-uniform approximation questions differ from the present exact \(BV\) seminorm at fixed degree three. Classical Fourier–Legendre convergence and \(L^p\) results (including Chanillo's endpoint work) also do not directly provide this sharp variation constant. A related sharp *degree-two* Jacobi-weighted variation-projection result treats a different polynomial range and finds off-center step extremizers; it does not imply the degree-three constant or the central extremizer proved here.

## Limitations

Only the unweighted real degree-three Legendre \(L^2\) projector on \((-1,1)\) is classified. No claim is made for higher degree, Jacobi weights, complex inputs, or best-possible approximation errors. Historical priority is qualified: some older literature was accessible only by abstract or bibliographic record, and absence from searched sources is not proof of uniqueness. The root-isolation checker is an exact arithmetic certificate for a specified finite algebraic inequality, not independent external verification. No independent mathematical audit has been performed.

## References

1. L. E. Figueroa, *Orthogonal polynomial projection error measured in Sobolev norms in the unit ball*, arXiv:1607.00930 (2016-07-04), https://arxiv.org/abs/1607.00930.
2. S. Chanillo, *On the weak behaviour of partial sums of Legendre series*, Transactions of the American Mathematical Society 268 (1981); abstract and introductory text available at https://www.researchgate.net/publication/315223658_On_the_weak_behaviour_of_partial_sums_of_Legendre_series.
3. R. Bera and B. Ghodadra, *Rate of convergence of Fourier–Legendre series of functions of the class \((n^\alpha)BV^p[-1,1]\)*, Acta et Commentationes Universitatis Tartuensis de Mathematica 28 (2024), https://doi.org/10.12697/ACUTM.2024.28.12 (later related background, not the archival lead).
