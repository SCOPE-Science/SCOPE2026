# Maximum uniform spacing and Greenwood concentration have exact positive covariance

## Finding
Let \(m\ge2\) and let
\[
(D_1,\ldots,D_m)\sim\operatorname{Dirichlet}(1,\ldots,1),
\]
so the vector is uniform on the simplex
\[
D_i\ge0,\qquad \sum_{i=1}^mD_i=1.
\]
Equivalently, these are the \(m\) complete spacings cut out by \(m-1\) independent \(\operatorname{Unif}(0,1)\) points. Define
\[
L_m=\max_{1\le i\le m}D_i,
\qquad
G_m=\sum_{i=1}^mD_i^2.
\]
Here \(G_m\) is the normalized Greenwood square-sum statistic. Write
\[
H_m=\sum_{j=1}^m\frac1j,
\qquad
H_m^{(2)}=\sum_{j=1}^m\frac1{j^2}.
\]
Then
\[
\boxed{\operatorname{Cov}(L_m,G_m)=\frac{H_m^2+H_m^{(2)}-2H_m}{m(m+1)(m+2)}>0.}
\]
The exact correlation is
\[
\boxed{\operatorname{Corr}(L_m,G_m)=\frac{\bigl(H_m^2+H_m^{(2)}-2H_m\bigr)\sqrt{(m+1)(m+3)}}{2\sqrt{(m+2)(mH_m^{(2)}-H_m^2)(m-1)}}.}
\]
Consequently,
\[
\operatorname{Corr}(L_m,G_m)\sim\frac{\sqrt6}{2\pi}\frac{(\log m)^2}{\sqrt m}.
\]
Thus the largest complete spacing and the Greenwood concentration are positively correlated for every finite \(m\), but the correlation tends to zero.

## Assumptions and scope
The theorem is exact for the uniform simplex law \(\operatorname{Dirichlet}(1,\ldots,1)\), hence for complete spacings from iid uniform points. It concerns the maximum spacing and the sum of squared spacings computed from the same spacing vector. No claim is made for nonuniform Dirichlet parameters or for spacings from a nonuniform parent distribution without probability-integral transformation.

The number \(m\) counts spacings, not sampled interior points. A sample of \(n\) iid uniform points produces \(m=n+1\) complete spacings.

## Proof
For \(x\ge0\), let
\[
A_i(x)=\{D_i>x\}.
\]
Since \(L_mG_m=\int_0^{L_m}G_m\,dx\), Tonelli's theorem and inclusion-exclusion give
\[
\mathbb E[L_mG_m]
=
\sum_{k=1}^m(-1)^{k+1}\binom mk
\int_0^{1/k}
\mathbb E\!\left[G_m\mathbf1_{A_1(x)\cap\cdots\cap A_k(x)}\right]dx.
\]
Fix \(k\) and put \(T=1-kx\). On the intersection of the first \(k\) events, subtracting \(x\) from those \(k\) coordinates leaves a simplex of total mass \(T\). Its volume ratio is \(T^{m-1}\), and after division by \(T\) the residual vector is again \(\operatorname{Dirichlet}(1,\ldots,1)\). Therefore
\[
\mathbb P(A_1(x)\cap\cdots\cap A_k(x))=T^{m-1},
\]
and, conditionally on that event,
\[
\mathbb E[G_m]
=
kx^2+\frac{2kxT}{m}+\frac{2T^2}{m+1}.
\]
Hence the \(k\)-fold intersection contribution is
\[
J_{m,k}
=
\int_0^{1/k}T^{m-1}
\left(kx^2+\frac{2kxT}{m}+\frac{2T^2}{m+1}\right)dx
=
\frac{2}{km(m+2)}+
\frac{2}{k^2m(m+1)(m+2)}.
\]
Using the classical alternating binomial identities
\[
\sum_{k=1}^m(-1)^{k+1}\binom mk\frac1k=H_m,
\]
and
\[
\sum_{k=1}^m(-1)^{k+1}\binom mk\frac1{k^2}
=
\frac{H_m^2+H_m^{(2)}}2,
\]
we obtain
\[
\mathbb E[L_mG_m]
=
\frac{2H_m}{m(m+2)}+
\frac{H_m^2+H_m^{(2)}}{m(m+1)(m+2)}.
\]
The standard simplex moments give
\[
\mathbb E[L_m]=\frac{H_m}{m},
\qquad
\mathbb E[G_m]=\frac2{m+1}.
\]
Subtracting their product proves the covariance formula.

For strict positivity, define
\[
F_m=H_m^2+H_m^{(2)}-2H_m.
\]
Then \(F_1=0\), and direct subtraction gives
\[
F_m-F_{m-1}=\frac{2(H_m-1)}m>0
\]
for every \(m\ge2\). Thus \(F_m>0\).

For the correlation, the same inclusion-exclusion calculation with \(L_m^2=2\int_0^{L_m}x\,dx\) gives
\[
\operatorname{Var}(L_m)=\frac{mH_m^{(2)}-H_m^2}{m^2(m+1)}.
\]
Dirichlet fourth moments give
\[
\operatorname{Var}(G_m)=\frac{4(m-1)}{(m+1)^2(m+2)(m+3)}.
\]
Substitution yields the displayed exact correlation. Finally, \(H_m\sim\log m\) and \(H_m^{(2)}\to\pi^2/6\), which yields the stated asymptotic.

## Verification
The accompanying standard-library checker evaluates the intersection integrals by exact beta integrals, reconstructs the inclusion-exclusion mixed moment, independently reconstructs both marginal variances from exact Dirichlet moments, and checks the covariance identity with rational arithmetic for \(2\le m\le100\). It also checks the positive-increment identity for \(F_m\) through \(m=1000\).

The replay output is:

`VERIFY_OK intersection_checks=5049 mixed_checks=99 covariance_checks=99 variance_checks=198 positivity_checks=999 increment_checks=998`

These finite checks supplement rather than replace the all-\(m\) proof above.

## Relationship to prior work
Pyke's classical review develops the exact simplex law of uniform spacings and surveys both Greenwood's square-sum statistic and largest-spacing statistics as standard but separate goodness-of-fit constructions. In the directly relevant survey section, the square-sum and maximum-spacing tests are listed separately; the inspected material does not state a joint mixed moment or covariance between them.

Mirakhmedov studies Greenwood's statistic as the sum of squared disjoint spacings and develops its asymptotic efficiency theory. The full text inspected for this comparison contains no maximum-spacing coupling; occurrences of “largest” concern an integer indexing convention rather than the largest spacing.

Royen gives exact marginal distribution representations for the square sum of Dirichlet variables and hence Greenwood's statistic. The accessible full record and text searches do not contain a maximum-spacing or covariance result.

The present theorem therefore concerns a different question from the known marginal distributions: the exact same-vector dependence between a canonical extreme spacing and the canonical quadratic concentration statistic.

## Limitations
The proof uses the uniform density on the simplex in an essential way. A general \(\operatorname{Dirichlet}(\alpha_1,\ldots,\alpha_m)\) law does not preserve its shape after subtracting a common threshold from selected coordinates, so the same inclusion-exclusion calculation does not transfer unchanged.

The originality comparison is strongest against the classical spacing survey and the directly relevant Greenwood-distribution papers inspected here. Older random-division or ordered-spacing literature may encode an equivalent mixed moment under different notation; no such statement was located in the searches performed, so this remains the principal residual originality risk.

## References
1. S. M. Mirakhmedov, “On Greenwood goodness-of-fit test,” *Journal of Statistical Planning and Inference* 140 (2010), 3017–3025, DOI 10.1016/j.jspi.2010.04.002. Available online 2010-04-13; primary MSC 62G10.
2. T. Royen, “The distribution of the square sum of Dirichlet random variables and a table with quantiles of Greenwood's statistic,” arXiv:1008.4059, first submitted 2010-08-24.
3. R. Pyke, “Spacings,” *Journal of the Royal Statistical Society: Series B* 27 (1965), 395–449, DOI 10.1111/j.2517-6161.1965.tb00602.x.
