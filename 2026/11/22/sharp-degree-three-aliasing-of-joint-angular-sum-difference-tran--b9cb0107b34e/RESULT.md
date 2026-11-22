# Sharp degree-three aliasing of joint angular sum–difference transforms

## Finding
Let \(U,V\) have an absolutely continuous copula density \(c\) on \([0,1]^2\). Observe the *paired* circular angular-probability-integral-transform summaries
\[
S=(U+V)\bmod 1,\qquad D=(U-V)\bmod 1.
\]
The joint law of \((S,D)\) is exactly the product-uniform law if and only if, almost everywhere on the two-torus,
\[
 c(u,v)+c((u+1/2)\bmod1,(v+1/2)\bmod1)=2.\tag{1}
\]
For copula densities that are trigonometric polynomials of total Fourier degree at most two, (1) forces \(c=1\) almost everywhere. Degree **three** is sharp: for each \(0<\varepsilon<1\),
\[
c_\varepsilon(u,v)=1+\varepsilon\sin(2\pi u)\sin(4\pi v)\tag{2}
\]
is a strictly positive real-analytic, nonexchangeable, positively quadrant-dependent copula density. Its entire **joint** pair \((S,D)\), not just either summary separately, has the same law as under independence, although
\[
\rho_S(c_\varepsilon)=\frac{3\varepsilon}{2\pi^2}>0,\quad
\tau_K(c_\varepsilon)=\frac{\varepsilon}{\pi^2}>0,\quad
\|P_{c_\varepsilon}-P_{\rm ind}\|_{\rm TV}=\frac{2\varepsilon}{\pi^2}>0.
\]
Consequently, for every integer \(n\ge1\), every test using *only* \(n\) independent observations of the **oracle** transformed pairs \((S_i,D_i)\) has power equal to its rejection probability under independent uniform \((U_i,V_i)\). This is an exact finite-sample nonidentifiability statement, not an asymptotic approximation.

## Assumptions and scope
All additions, subtractions, and half-period translations in the main theorem are modulo one. The copula density \(c\ge0\) is integrable, has total integral one, and satisfies both uniform-marginal identities \(\int_0^1c(u,v)\,dv=\int_0^1c(v,u)\,dv=1\) almost everywhere. The first equivalence permits any such integrable density, including nonsmooth ones. For Fourier minimality, *total degree* means \(\max\{|m|+|n|:\widehat c(m,n)\ne0\}\) over nonzero Fourier modes of a finite trigonometric polynomial. The example (2) has total degree three.

The testing consequence concerns the population-transform, or *oracle*, experiment: independent pairs \((U_i,V_i)\) are transformed by their true marginal distribution functions. Procedures using empirically estimated marginal distribution functions or the ranks of the original coordinates retain additional information not present in the oracle pairs; no exact-power or asymptotic-power assertion is made for those procedures. The claim is about what is identifiable from the full paired summaries \((S,D)\), and therefore also from either marginal summary.

## Proof
**Two-sheet pushforward.** The group homomorphism \(T:\mathbb T^2\to\mathbb T^2\), \(T(u,v)=(u+v,u-v)\), has determinant \(-2\) and precisely two preimages for each target, differing by \((1/2,1/2)\). Its Jacobian has absolute determinant two. Hence the density of \((S,D)\) at \((s,d)\) is
\[
p(s,d)=\frac12\left[c(u,v)+c(u+1/2,v+1/2)\right],
\]
where \((u,v)\) is either preimage and the arguments are reduced modulo one. Thus \(p\equiv1\) almost everywhere exactly when (1) holds. The same equivalence follows from Fourier characters because
\[
\mathbb E\exp\{2\pi i(kS+\ell D)\}=\widehat c(-k-\ell,-k+\ell),\qquad k,\ell\in\mathbb Z,
\]
and the observed lattice consists of integer pairs whose coordinates have the same parity. Fourier uniqueness for integrable functions gives the converse. The sign convention in the Fourier transform does not affect the vanishing condition.

**Minimality.** Uniform marginals eliminate all nonconstant Fourier modes on either coordinate axis. With total degree at most two, the only remaining possible nonzero modes are \((\pm1,\pm1)\), all of which belong to the observed same-parity lattice. Joint uniformity of \((S,D)\) therefore forces those coefficients to vanish too; the only surviving coefficient is the constant one, so \(c=1\). The density (2) is supported on modes \((\pm1,\pm2)\), all of opposite parity, proving sharpness at degree three.

**Copula construction and positive dependence.** Each sine in (2) integrates to zero over \([0,1]\), so both marginals equal one. For \(0<\varepsilon<1\), \(1-\varepsilon\le c_\varepsilon\le1+\varepsilon\), establishing positivity. The density is a finite trigonometric polynomial and hence real-analytic. Its copula distribution function is
\[
C_\varepsilon(u,v)=uv+\frac{\varepsilon}{8\pi^2}
  (1-\cos 2\pi u)(1-\cos4\pi v)\ge uv,
\]
with strict inequality on a nonempty open set. It is not exchangeable: \(c_\varepsilon(1/4,1/8)=1+\varepsilon\), but \(c_\varepsilon(1/8,1/4)=1\).

Under the simultaneous half-period shift, \(\sin(2\pi(u+1/2))=-\sin(2\pi u)\) and \(\sin(4\pi(v+1/2))=\sin(4\pi v)\), so the perturbation cancels between the two sheets. Applying (1), \((S,D)\) is jointly product-uniform.

**Exact dependence coefficients.** Since \(\int_0^1u\sin(2\pi u)\,du=-1/(2\pi)\) and \(\int_0^1v\sin(4\pi v)\,dv=-1/(4\pi)\), the uniform-marginal Spearman coefficient \(12\mathbb E[UV]-3\) is \(3\varepsilon/(2\pi^2)\). The copula identity \(\tau_K=4\mathbb E[C_\varepsilon(U,V)]-1\), together with \(\int F F'=0\) for the sine primitives vanishing at both endpoints, gives \(\tau_K=\varepsilon/\pi^2\). The total variation distance from independence is one half the integral of \(|c_\varepsilon-1|\); each absolute-sine integral equals \(2/\pi\), giving \(2\varepsilon/\pi^2\).

**Exact indistinguishability and retained information.** For each independent observation the image law is the same under the null and (2), so all product laws of the paired images agree, proving the test-power assertion for every sample size. Conversely, retaining \(U\) alongside \(S\) gives an invertible torus map, since \(V=(S-U)\bmod1\). In particular,
\[
\mathbb E_{c_\varepsilon}\cos(2\pi(-U+2S))=-\varepsilon/4,
\]
whereas the expectation is zero under independence. Thus the lost information is caused by the two-sheet observation map, rather than by a vanishing dependence signal in the original copula.

## Verification
Run `python verify.py` using Python 3 and SymPy. The script checks the exact one-dimensional sine integrals, copula primitives, half-period parity, minimal Fourier-degree enumeration, Spearman and Kendall formulas, the nonexchangeability witnesses, the distinguishing Fourier moment, and the total-variation formula. It reports a passing exact symbolic check. The all-degree equivalence and finite-sample equality are established by the preceding analytic proof; finite computation is not being substituted for these arguments.

## Relationship to prior work
Fernández-Durán and Gregorio-Domínguez's 2023 angular probability integral transform (APIT) independence procedure uses uniformity of the circular sum or difference of marginal transforms; its preprint, Section 3, explicitly describes that uniformity as equivalent to bivariate independence. Uniformity is necessary under independence, but (2) demonstrates it is not sufficient, even for **both transforms jointly** and even within a smooth, positively quadrant-dependent alternative. The original article's Johnson–Wehrly joining-density model has a special dependence form \(c(u,v)=g(u\pm v)\), under which a single projection can characterize the model parameter; (2) falls outside that restricted joining-density family. The earlier Pewsey–Kato work concerns parametric goodness-of-fit within the Wehrly–Johnson framework, not the joint two-sheet null fiber studied here. Generic subindependence examples show why sums need not identify independence, but do not by themselves imply the joint sum–difference aliasing, sharp trigonometric-degree threshold, and positive-quadrant dependence proved above.

## Limitations
The published APIT implementation uses empirical ranks rather than oracle marginal transforms; its finite-sample power under (2) is not determined by this theorem. The frequency-minimality statement is for trigonometric-polynomial copula densities, not all smooth densities or arbitrary measures. The counterexample is positively quadrant-dependent but is not claimed to be totally positive of order two. No claim of a universally most powerful replacement test, or of originality beyond the specific literature examined, is made. Independent historical-priority and mathematical audits have not been performed.

## References
1. J. J. Fernández-Durán and M. M. Gregorio-Domínguez, *Test of Bivariate Independence Based on Angular Probability Integral Transform with Emphasis on Circular-Circular and Circular-Linear Data*, arXiv:2301.02991, first public posting 2023-01-08, https://arxiv.org/abs/2301.02991 . Journal DOI: https://doi.org/10.1515/demo-2023-0103 .
2. A. Pewsey and S. Kato, *Parametric bootstrap goodness-of-fit testing for Wehrly–Johnson bivariate circular distributions*, *Statistics and Computing*, 2016, https://doi.org/10.1007/s11222-015-9605-2 .
3. D. Nelsen, *An Introduction to Copulas*, Springer, second edition, 2006. (Standard copula identities and positive quadrant dependence.)
