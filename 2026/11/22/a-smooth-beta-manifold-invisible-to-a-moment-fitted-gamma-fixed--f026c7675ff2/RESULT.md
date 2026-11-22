# A smooth Beta manifold invisible to a moment-fitted Gamma fixed-point test

## Finding

Consider the scalar, uncensored Gamma fixed-point U-statistic proposed by Vaisakh, Sreedevi and Kattumannil (2021), with both Gamma parameters fitted by the population/sample method of moments. Its population discrepancy is **not identifying**: the entire uniform scale family has discrepancy zero, and a real-analytic curve of non-Gamma Beta distributions passes through the uniform law and has the same zero discrepancy. For the power-law Beta subfamily, the departure has the exact sign formula
\[
\Delta(\operatorname{Beta}(a,1))=\frac{a(a-1)}{2(a+1)(2a+1)},\qquad a>0.
\]

Under the non-Gamma alternative \(F=\operatorname{Uniform}(0,1)\), the moment-fitted statistic obeys
\[
\sqrt n\,\widehat\Delta_n\ \Rightarrow\ N(0,7/540).
\]
Its moment-matched Gamma null is \(\Gamma(3,1/6)\) (shape, scale), under which the *same moment-fitted statistic* satisfies
\[
\sqrt n\,\widehat\Delta_n\ \Rightarrow\ N(0,37/2592).
\]
Consequently an asymptotically valid, two-sided, parametric-Gamma calibration that refits the two moment parameters in each replicate has limiting rejection probability under this fixed uniform alternative
\[
\boxed{\ 2\Phi\left(-z_{1-\alpha/2}\sqrt{185/168}\right)\ },
\]
which is \(0.039711278797\ldots\) at nominal level \(\alpha=0.05\), rather than tending to one. Here \(\Phi\) is the standard-normal CDF. This statement is about the specified scalar statistic and the specified method-of-moments calibration; it does not concern the integrated-squared fixed-point tests or censored-data versions.

## Assumptions and scope

Let \(X_1,\ldots,X_n\) be independent copies of an almost surely positive, continuously distributed random variable with finite second moment, positive variance, and \(n\ge2\). Define \(m=EX\), \(v=\operatorname{Var}(X)\), \(s_2=EX^2\), and fitted Gamma shape and scale \(k=m^2/v\) and \(\lambda=v/m\). For independent \(X,Y\) with the same distribution put
\[
A=E\min(X,Y),\qquad B=E\left[\frac{X}{Y}\mathbf1_{\{X<Y\}}\right]=\tfrac12 E\left[\frac{\min(X,Y)}{\max(X,Y)}\right].
\]
The scalar departure of the source paper (its uncensored Eq. (4)) is
\[
\Delta(F)=\frac A\lambda+(1-k)B-\frac k2
=\frac{mA+(v-m^2)B-m^2/2}{v}.
\]
For data, let \(\widehat m=n^{-1}\sum_iX_i\), \(\widehat v=n^{-1}\sum_i(X_i-\widehat m)^2\), \(\widehat k=\widehat m^2/\widehat v\), and \(\widehat\lambda=\widehat v/\widehat m\), and define
\[
U_{1,n}=\frac{2}{n(n-1)}\sum_{i<j}\min(X_i,X_j),\quad
U_{2,n}=\frac{1}{n(n-1)}\sum_{i<j}\frac{\min(X_i,X_j)}{\max(X_i,X_j)},
\]
\[
\widehat\Delta_n=\frac{U_{1,n}}{\widehat\lambda}+(1-\widehat k)U_{2,n}-\frac{\widehat k}{2}.
\]
The scale parameterization is \(E\Gamma(k,\lambda)=k\lambda\) and \(\operatorname{Var}\Gamma(k,\lambda)=k\lambda^2\). The Beta-distribution claims concern support \((0,1)\). The explicit rejection-probability conclusion assumes the usual central two-sided Gaussian limiting critical values, or a consistent parametric-Gamma bootstrap which **re-estimates moment parameters in every replicate**. The source paper also discusses a one-sided critical region; it should not be conflated with this two-sided calibration.

## Proof

**1. Exact Beta departure.** If \(X\sim\operatorname{Beta}(a,1)\), its density is \(a x^{a-1}\) on \((0,1)\). Elementary integration gives
\[
m=\frac a{a+1},\quad v=\frac a{(a+1)^2(a+2)},\quad
k=a(a+2),\quad \lambda=\frac1{(a+1)(a+2)},
\]
\[
A=\int_0^1(1-t^a)^2dt=\frac{2a^2}{(a+1)(2a+1)},\quad
B=\int_0^1\frac{a y^{a-1}}y\int_0^y a x^a\,dx\,dy=\frac a{2(a+1)}.
\]
Substitution and rational factorization yield exactly the boxed departure above. In particular it vanishes at \(a=1\), is negative on \(0<a<1\), and is positive on \(a>1\). The uniform law is not Gamma, since it has bounded support. For every scale \(c>0\), uniform \((0,c)\) has the same zero departure by scale invariance. Moreover, the moment-matched Gamma for uniform \((0,1)\) is \(\Gamma(3,1/6)\): both have mean \(1/2\) and variance \(1/12\).

**2. An analytic continuum of blind Beta alternatives.** Let \(D(a,b)=\Delta(\operatorname{Beta}(a,b))\) for \(a,b>0\). All its moment and pairwise integrals are real analytic in a neighborhood of \((1,1)\): the bounded kernels \(\min(x,y)\) and \(\min(x,y)/\max(x,y)\), together with Beta densities and their logarithmic parameter derivatives, have integrable local dominators. For a density perturbation \(1+\varepsilon h(x)\) with \(\int_0^1h=0\), differentiating the displayed functional at uniform \((0,1)\) yields
\[
D'_{\mathrm{unif}}[h]=12\int_0^1h(x)g(x)\,dx,\qquad
g(x)=\frac{x}{4}-\frac{x^2}{4}+\frac{x\log x}{6}.
\]
The Beta score functions at \((a,b)=(1,1)\) are \(h_a(x)=1+\log x\) and \(h_b(x)=1+\log(1-x)\). Using
\[
\int_0^1x\log(1-x)\,dx=-\frac34,\quad
\int_0^1x^2\log(1-x)\,dx=-\frac{11}{18},
\]
\[
\int_0^1x\log x\log(1-x)\,dx=1-\frac{\pi^2}{12},
\]
one obtains
\[
D(1,1)=0,\qquad
\partial_aD(1,1)=\frac1{12},\qquad
\partial_bD(1,1)=\frac{19-2\pi^2}{12}\ne0.
\]
The analytic implicit-function theorem supplies a unique local analytic function \(a=a(b)\) with \(a(1)=1\), \(D(a(b),b)=0\), and
\[
a'(1)=2\pi^2-19=0.739208802\ldots\ .
\]
For sufficiently small nonzero \(|b-1|\), this curve consists of nonuniform continuous Beta laws, all distinct from every Gamma law because their support is bounded. It is not an isolated accidental cancellation.

**3. Influence functions and limiting distributions.** Standard two-sample U-statistic projection and the multivariate delta method apply to the two pairwise bounded-ratio kernels and the sample moments. At any law with positive \(v\), put \(a_F(x)=E\min(x,Y)\), \(b_F(x)=E[\min(x,Y)/\max(x,Y)]\). At \(\Delta(F)=0\) the influence function is
\[
\operatorname{IF}_F(x)=\frac1v\left[(A-4mB-m)(x-m)+B(x^2-s_2)
+2m(a_F(x)-A)+(v-m^2)(b_F(x)-2B)\right].
\]
For \(F=\operatorname{Uniform}(0,1)\), substitution of \(m=1/2\), \(v=1/12\), \(A=1/3\), and \(B=1/4\) gives
\[
\operatorname{IF}_{\mathrm{unif}}(x)=3x-3x^2+2x\log x.
\]
Its expectation is zero and direct integration gives
\[
\int_0^1\operatorname{IF}_{\mathrm{unif}}(x)^2dx=\frac7{540}>0.
\]
Thus the asymptotic normal limit under this alternative is nondegenerate.

For the Gamma null it suffices by scale invariance to take \(Y\sim\Gamma(3,1)\). Here \(m=3\), \(v=3\), \(s_2=12\), \(A=33/16\), \(B=9/32\). Direct integration of its Erlang density gives
\[
a_F(x)=3-e^{-x}(3+2x+x^2/2),\quad
b_F(x)=\frac{3(1-e^{-x})}{x}-e^{-x}(3+x).
\]
Writing \(H(x)=x\operatorname{IF}_F(x)\), substitution yields
\[
H(x)=P_0(x)+e^{-x}P_1(x),
\]
\[
P_0(x)=\frac{3x^3}{32}-\frac{23x^2}{16}+\frac{99x}{16}-6,\qquad
P_1(x)=-x^3-2x^2+6.
\]
Because the Gamma density is \(x^2e^{-x}/2\), the influence variance equals
\[
\frac12\int_0^\infty e^{-x}(P_0(x)+e^{-x}P_1(x))^2\,dx
=\frac{37}{2592}>0,
\]
using only \(\int_0^\infty x^r e^{-cx}dx=r!/c^{r+1}\) for nonnegative integer \(r\). Under both laws, the asymptotic linearization has an \(o_p(1)\) remainder after multiplication by \(\sqrt n\); hence the respective central limit theorems follow.

**4. Test calibration.** A two-sided, nominal-\(\alpha\), consistent parametric-Gamma null calibration recomputing moment estimates has limiting critical values \(\pm z_{1-\alpha/2}\sqrt{37/2592}/\sqrt n\) when the fitted parameters converge to \((3,1/6)\). They do so under uniform \((0,1)\). The alternative CLT therefore gives the stated probability, since \((37/2592)/(7/540)=185/168\). For each sufficiently near nonuniform Beta law on the analytic zero curve, an analogous nondegenerate \(\sqrt n\) limit and finite Gamma-reference critical values exclude consistency; the precise limiting power depends on the curve point. If only large **positive** values cause rejection, then for every \(\operatorname{Beta}(a,1)\) with \(0<a<1\) the rejection probability instead tends to zero because its departure is strictly negative.

## Verification

Run `python verify_gamma_blind.py` with SymPy installed. Its 19 analytic checks independently verify the Beta power-law identity, the uniform cancellation, both Beta directional derivatives and the analytic curve tangent, the exact uniform and Gamma influence variances, and the limiting two-sided rejection probability. The Gamma calculation is an exact finite sum of factorial integrals, not a numerical limit. No experimental enumeration is used to prove a continuous or asymptotic claim.

## Relationship to prior work

Vaisakh, Sreedevi and Kattumannil (2021), arXiv:2108.00503, introduce the scalar integrated fixed-point departure and its U-statistic form in equations (1)–(5); their Section 3 supplies the explicit moment-estimator parameterization, and Section 4 investigates finite-sample power. Their full preprint is the source of the exact statistic analyzed here. The 2023 published journal abstract confirms the general test but was not used as proof of an unchanged complete later text.

Betsch and Ebner (2018 preprint, 2019 journal) introduce the underlying pointwise Gamma fixed-point characterization and an **integrated squared discrepancy**; their Section 4 establishes consistency of that different nonnegative quadratic statistic. Pointwise identity characterizes Gamma, while cancellation of a **single signed scalar integral** does not. The present finding does not contradict the global-consistency theorem for the integrated-squared statistic. Related Stein identity surveys concern identities over classes of test functions, not the specific scalar cancellation and power formula here.

## Limitations

The result applies to the stated uncensored moment-fitted scalar statistic, and does not assert that the source's censoring-corrected version is blind, or that all possible Gamma parameter estimators behave identically. The numerical rejection probability assumes a two-sided asymptotically correct Gamma calibration with moment estimates re-fitted in every bootstrap replicate; it is not a claimed finite-sample rate or an evaluation of any particular software implementation. The implicit Beta curve is local; no global classification of all blind laws is claimed. Historical priority remains subject to earlier scalar-characterization literature not fully accessible in the searches described in the accompanying review. No independent mathematical validation has been performed.

## References

1. Vaisakh, K. M., Sreedevi, E. P., and Kattumannil, S. K. *A new goodness of fit test for gamma distribution with censored observations*. arXiv:2108.00503, first posted 2021-08-01. https://arxiv.org/abs/2108.00503 ; journal version DOI:10.1080/03610918.2023.2245180.
2. Betsch, S. and Ebner, B. *A new characterization of the Gamma distribution and associated goodness-of-fit tests*. arXiv:1806.06028, first posted 2018-06-15; *Metrika* 82 (2019), 779–806. https://arxiv.org/abs/1806.06028 .
3. *Stein's identities and the related topics: an instructive explanation on shrinkage, characterization, normal approximation and goodness-of-fit* (2024), overview of Gamma Stein characterization. https://link.springer.com/article/10.1007/s42081-023-00239-6 .
