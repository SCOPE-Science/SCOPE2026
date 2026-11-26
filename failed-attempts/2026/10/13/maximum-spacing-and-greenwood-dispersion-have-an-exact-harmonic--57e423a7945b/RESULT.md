# Maximum spacing and Greenwood dispersion have an exact harmonic covariance

## Finding

Let
\[
(D_1,\ldots,D_m)\sim\operatorname{Dirichlet}(1,\ldots,1),
\qquad m\ge2,
\]
and define
\[
M_m=\max_{1\le i\le m}D_i,
\qquad
G_m=\sum_{i=1}^m D_i^2.
\]

The statistic \(G_m\) is Greenwood's sum-of-squared-spacings statistic, while \(M_m\) is the maximum spacing. Write
\[
H_m=\sum_{j=1}^m\frac1j,
\qquad
H_m^{(2)}=\sum_{j=1}^m\frac1{j^2}.
\]

Then the exact mixed moment is
\[
\boxed{
\mathbb E[M_mG_m]
=
\frac{2}{m(m+2)}
\left(
H_m+\frac{H_m^2+H_m^{(2)}}{2(m+1)}
\right).
}
\tag{1}
\]

Consequently,
\[
\boxed{
\operatorname{Cov}(M_m,G_m)
=
\frac{H_m^2+H_m^{(2)}-2H_m}
{m(m+1)(m+2)}
>0.
}
\tag{2}
\]

Using
\[
\operatorname{Var}(M_m)
=
\frac{mH_m^{(2)}-H_m^2}{m^2(m+1)}
\tag{3}
\]
and
\[
\operatorname{Var}(G_m)
=
\frac{4(m-1)}
{(m+1)^2(m+2)(m+3)},
\tag{4}
\]
the exact correlation is
\[
\boxed{
\operatorname{Corr}(M_m,G_m)
=
\frac{H_m^2+H_m^{(2)}-2H_m}{2}
\sqrt{
\frac{(m+1)(m+3)}
{(m+2)(m-1)(mH_m^{(2)}-H_m^2)}
}.
}
\tag{5}
\]

In particular,
\[
\boxed{
\operatorname{Corr}(M_m,G_m)
\sim
\frac{\sqrt6}{2\pi}
\frac{(\log m)^2}{\sqrt m}.
}
\tag{6}
\]

Thus the two canonical spacing diagnostics are positively dependent at every finite size, but their standardized dependence vanishes slowly.

## Assumptions and scope

The theorem is stated for the uniform Dirichlet simplex because this is the common null law of ordinary uniform spacings.

It has two standard interpretations.

For \(m-1\) iid uniform points on \((0,1)\), include the two boundary gaps; the resulting \(m\) linear spacings have the Dirichlet law above.

For \(m\) iid uniform points on the circle, divide the cyclic gaps by the circumference; the \(m\) circular spacings have the same Dirichlet law.

The result is exact for every integer \(m\ge2\). The asymptotic statement keeps no additional parameter fixed.

## Proof

For a nonempty subset \(K\subseteq\{1,\ldots,m\}\) of size \(k\), let
\[
A_K(t)=\{D_i>t\text{ for every }i\in K\}.
\]
For
\[
0\le t\le\frac1k,
\]
translate the coordinates indexed by \(K\):
\[
D_i=t+Y_i\quad(i\in K),
\qquad
D_i=Y_i\quad(i\notin K).
\]
The residual simplex has total mass
\[
s=1-kt.
\]

Because the Dirichlet density is constant on the simplex,
\[
\Pr(A_K(t))=s^{m-1}.
\tag{7}
\]
Conditional on \(A_K(t)\), the scaled vector \(Y/s\) again has the uniform Dirichlet law. Therefore
\[
\mathbb E\!\left[\sum_{i\in K}\frac{Y_i}{s}\right]
=
\frac{k}{m}
\]
and
\[
\mathbb E\!\left[\sum_{i=1}^m\left(\frac{Y_i}{s}\right)^2\right]
=
\frac{2}{m+1}.
\]
Hence
\[
\mathbb E[G_m\mathbf 1_{A_K(t)}]
=
s^{m-1}
\left(
kt^2+\frac{2kts}{m}+\frac{2s^2}{m+1}
\right).
\tag{8}
\]

Since
\[
\{M_m>t\}=\bigcup_{i=1}^m\{D_i>t\},
\]
inclusion-exclusion gives
\[
\mathbb E[G_m\mathbf 1_{\{M_m>t\}}]
=
\sum_{k=1}^{\lfloor1/t\rfloor}
(-1)^{k+1}\binom{m}{k}
(1-kt)^{m-1}
\left(
kt^2+\frac{2kt(1-kt)}m+\frac{2(1-kt)^2}{m+1}
\right).
\tag{9}
\]

For any nonnegative random variable \(M_m\),
\[
\mathbb E[M_mG_m]
=
\int_0^1
\mathbb E[G_m\mathbf 1_{\{M_m>t\}}]\,dt.
\tag{10}
\]
The contribution of the \(k\)-th inclusion-exclusion term is
\[
\int_0^{1/k}
(1-kt)^{m-1}
\left(
kt^2+\frac{2kt(1-kt)}m+\frac{2(1-kt)^2}{m+1}
\right)\,dt
\]
\[
=
\frac{2}{m(m+2)}
\left(
\frac1k+\frac1{(m+1)k^2}
\right).
\tag{11}
\]

Now use the standard binomial-harmonic identities
\[
\sum_{k=1}^m(-1)^{k+1}\binom{m}{k}\frac1k
=
H_m
\tag{12}
\]
and
\[
\sum_{k=1}^m(-1)^{k+1}\binom{m}{k}\frac1{k^2}
=
\frac{H_m^2+H_m^{(2)}}2.
\tag{13}
\]
Substituting (11)--(13) into (10) proves (1).

The classical maximum-spacing tail formula obtained from the same inclusion-exclusion argument is
\[
\Pr(M_m>t)
=
\sum_{k=1}^{\lfloor1/t\rfloor}
(-1)^{k+1}\binom{m}{k}(1-kt)^{m-1}.
\tag{14}
\]
Integrating it gives
\[
\mathbb E M_m=\frac{H_m}{m},
\qquad
\mathbb E M_m^2=
\frac{H_m^2+H_m^{(2)}}{m(m+1)}.
\tag{15}
\]
Also
\[
\mathbb E G_m=\frac{2}{m+1}.
\tag{16}
\]
Subtracting the product of (15) and (16) from (1) proves (2).

To see strict positivity, put
\[
A_m=H_m^2+H_m^{(2)}-2H_m.
\]
Then
\[
A_2=\frac12
\]
and
\[
A_{m+1}-A_m
=
\frac{2(H_m-1)}{m+1}
+
\frac{2}{(m+1)^2}
>0
\qquad(m\ge2).
\tag{17}
\]

Equation (3) follows from (15). For (4), the Dirichlet moments give
\[
\mathbb E D_i^4
=
\frac{24}{m(m+1)(m+2)(m+3)}
\]
and, for \(i\ne j\),
\[
\mathbb E D_i^2D_j^2
=
\frac{4}{m(m+1)(m+2)(m+3)}.
\]
Thus
\[
\mathbb E G_m^2
=
\frac{4(m+5)}{(m+1)(m+2)(m+3)},
\]
which yields (4). Combining (2)--(4) gives (5).

Finally,
\[
H_m=\log m+\gamma+o(1),
\qquad
H_m^{(2)}=\frac{\pi^2}{6}+o(1),
\]
so the numerator of (5) is asymptotic to \((\log m)^2\), whereas
\[
mH_m^{(2)}-H_m^2\sim\frac{\pi^2}{6}m.
\]
This proves (6).

## Verification

The accompanying exact checker verifies the algebra through \(m=80\).

For each \(m\), it independently expands every polynomial integrand in (11), integrates it term by term with rational arithmetic, performs the full inclusion-exclusion sum, and checks the closed mixed moment (1).

It separately checks the two binomial-harmonic identities, both marginal variances, the covariance reduction, strict positivity, and the exact correlation-square identity.

No floating-point simulation is used for the finite identities. Numerical asymptotic checks are supplementary to the proof.

## Relationship to prior work

Pyke's classical review develops the general distribution theory of sample spacings and discusses limiting distributions for functions of spacings. The accessible publisher summary does not expose a mixed maximum-spacing/Greenwood moment. A full publisher PDF could not be lawfully retrieved in the source inspection, so this remains the strongest residual originality risk.

Royen gives exact distributional representations and moments for the square sum of Dirichlet variables and identifies the uniform-spacing special case as Greenwood's statistic. His full public manuscript treats the distribution of the square sum itself; searches of the manuscript for maximum-spacing and covariance formulations did not reveal the mixed law (1)--(5).

Aaron, Cholaquidis, and Fraiman survey maximal-spacing theory and its statistical applications and extend the maximal-spacing framework in higher dimensions. Their full public manuscript contains no Greenwood statistic.

The accepted result is not a new marginal distribution. Its content is the closed-form finite dependence law between the largest component of a uniform Dirichlet vector and its quadratic concentration statistic.

## Limitations

The exact formula uses the uniform Dirichlet law. Symmetric Dirichlet laws with parameter different from \(1\) do not admit the same translated-simplex probability in (7), so the argument does not extend unchanged.

Positive covariance does not imply positive quadrant dependence or association of \(M_m\) and \(G_m\).

The classical joint density of all spacings determines every functional in principle. The value here is the explicit closed harmonic form obtained after a nontrivial inclusion-exclusion integration, not a claim that the underlying spacing law is new.

Older spacing literature is extensive. In particular, the inaccessible full text of Pyke's broad 1965 review remains a residual risk for an equivalent mixed-moment identity.

## References

1. T. Royen, “The distribution of the square sum of Dirichlet random variables and a table with quantiles of Greenwood's statistic,” arXiv:1008.4059v1, first submitted 2010-08-24. The manuscript lists MSC 2010 classes \(62E15,62H10\).
2. R. Pyke, “Spacings,” *Journal of the Royal Statistical Society, Series B* 27 (1965), 395–436, DOI 10.1111/j.2517-6161.1965.tb00602.x.
3. C. Aaron, A. Cholaquidis, and R. Fraiman, “A Generalization of the maximal-spacings in several dimensions and a convexity test,” arXiv:1411.2482, first submitted 2014-11-10.
