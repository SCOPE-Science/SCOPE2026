# Three-scale covariance and a sharp spectral crossing in panhandle matroid base polytopes

## Finding
For integers \(2\le r\le s\) and \(t\ge2\), put \(n=s+t\) and let \(\mathcal P_{r,s,t}\subset\mathbb R^n\) be the convex hull of the indicator vectors of the \(r\)-element subsets \(B\subseteq[n]\) satisfying \(|B\cap[s]|\ge r-1\). Let \(X\) be uniform on these vertices, and let \(C=\mathbb E[(X-\mathbb EX)(X-\mathbb EX)^{\mathsf T}]\) be its ambient Euclidean covariance matrix. Write \(d=s-r+1\).

The kernel of \(C\) is exactly the span of the all-ones vector. On its orthogonal complement, the following are the complete eigenvalues and multiplicities (equal eigenvalues are counted with combined multiplicity):

\[
\begin{aligned}
\lambda_{\mathrm{handle}}&=\frac{rd\,[d-1+t(r-1)]}{s(s-1)(d+tr)},&&\text{multiplicity }s-1,\\
\lambda_{\mathrm{tail}}&=\frac{r}{d+tr},&&\text{multiplicity }t-1,\\
\lambda_{\mathrm{bridge}}&=\frac{rd(s+t)}{s(d+tr)^2},&&\text{multiplicity }1.
\end{aligned}
\]

The handle and tail eigenspaces are the vectors supported on the corresponding block with coordinate sum zero. The bridge eigenvector is \((-\mathbf1_s/s,\mathbf1_t/t)\). The bridge eigenvalue is strictly smaller than both other eigenvalues for every allowed triple. The two remaining eigenvalues cross at the exact threshold
\[
\operatorname{sgn}(\lambda_{\mathrm{handle}}-\lambda_{\mathrm{tail}})=\operatorname{sgn}\left(t-2-\frac{r-2}{s-r+1}\right).
\]
At equality their eigenspaces merge; this can occur for integer parameters.

If \(s\to\infty\), \(r/s\to\rho\in(0,1)\) and \(t/s\to\tau\in(0,\infty)\), then
\[
\begin{aligned}
\lambda_{\mathrm{handle}}&\longrightarrow\rho(1-\rho),\\
s\lambda_{\mathrm{tail}}&\longrightarrow\frac1\tau,\\
s^2\lambda_{\mathrm{bridge}}&\longrightarrow\frac{(1-\rho)(1+\tau)}{\tau^2\rho},\\
\frac1{s^2}\frac{\lambda_{\max}(C|_{\mathbf1_n^\perp})}{\lambda_{\min}(C|_{\mathbf1_n^\perp})}&\longrightarrow\frac{\rho^2\tau^2}{1+\tau}.
\end{aligned}
\]
In particular the three principal covariance scales are constant, inverse-linear, and inverse-quadratic, and the intrinsic covariance condition number grows quadratically in the handle size.

## Assumptions and scope
All parameters are integers with \(2\le r\le s\), \(t\ge2\) and \(n=s+t\). The polytope is the standard panhandle matroid base polytope for \(\operatorname{Pan}_{r,s,n}\); the metric is the inherited Euclidean metric on the affine hyperplane \(\sum_i x_i=r\). Uniform means counting *vertices* once each, not uniform volume on the polytope or uniform sampling among all points of the ambient cube. The statements hold at the boundary \(r=s\), while the scaling result requires \(\rho<1\). The asymptotic ratios are not asserted uniformly outside the displayed parameter regime.

## Proof
Every admissible basis has either \(r\) handle elements and no tail element, or \(r-1\) handle elements and one tail element. The counts are \(\binom sr\) and \(t\binom{s}{r-1}\), respectively. Consequently the number \(K\) of tail elements is Bernoulli with
\[
p=\mathbb P(K=1)=\frac{tr}{d+tr},\qquad1-p=\frac d{d+tr}.
\]
Conditionally on \(K\), the handle coordinates are the indicator vector of a uniform \((r-K)\)-subset of \([s]\), and the tail is zero for \(K=0\) or a uniform standard basis vector for \(K=1\). Conditional handle and tail choices are independent given \(K\).

Let \(J_a=\mathbf1_a\mathbf1_a^{\mathsf T}\). The conditional handle covariance is
\[
\frac{(r-K)(s-r+K)}{s(s-1)}\bigl(I_s-J_s/s\bigr),
\]
and the averaged conditional tail covariance is \((p/t)(I_t-J_t/t)\). The conditional mean changes by
\[
v=(-\mathbf1_s/s,\mathbf1_t/t)
\]
when \(K\) changes from zero to one. The law of total covariance thus gives the exact orthogonal decomposition
\[
C=\lambda_{\mathrm{handle}}\operatorname{diag}(I_s-J_s/s,0_t)
+\lambda_{\mathrm{tail}}\operatorname{diag}(0_s,I_t-J_t/t)
+p(1-p)vv^{\mathsf T}.
\]
Because \(\|v\|^2=1/s+1/t\), the bridge eigenvalue is \(p(1-p)(1/s+1/t)\), yielding its displayed closed form. Averaging the conditional handle eigenvalue and simplifying with \(d=s-r+1\) gives the handle formula. The decomposition supplies all \(n-1\) positive eigenvalues; the remaining all-ones eigenvalue is zero.

The positivity and strict comparisons are algebraic. First
\[
\frac{\lambda_{\mathrm{tail}}}{\lambda_{\mathrm{bridge}}}-1
=\frac{t(r-1)(s+1)}{d(s+t)}>0.
\]
Second,
\[
\frac{\lambda_{\mathrm{handle}}}{\lambda_{\mathrm{bridge}}}-1
=\frac{(r-1)(t-1)(2d+rt+r-2)}{(s-1)(s+t)}>0.
\]
Finally,
\[
\frac{\lambda_{\mathrm{handle}}}{\lambda_{\mathrm{tail}}}-1
=\frac{(r-1)[d(t-2)-(r-2)]}{s(s-1)},
\]
which proves the exact eigenvalue crossover, including equality and both strict alternatives.

For the limits, substitute \(r/s\to\rho\), \(t/s\to\tau\), and \(d/s\to1-\rho\) directly into the closed forms. The handle eigenvalue tends to \(\rho(1-\rho)>0\); the tail eigenvalue is asymptotic to \(1/(\tau s)\), and the bridge eigenvalue to \((1-\rho)(1+\tau)/(\tau^2\rho s^2)\). The bridge is always smallest and the handle eventually largest. Taking the ratio proves the condition-number limit.

## Verification
The standalone Python 3 script `panhandle_covariance_check.py` uses standard-library exact fractions. It constructs every admissible vertex for 60 small parameter triples, forms their exact covariance matrices, tests a representative eigenvector of each of the four invariant subspaces, and checks means and counts. It also evaluates the closed forms and strict inequalities for thousands of parameter triples, including integer crossing cases, and checks the scaling constants at increasing handle sizes. Execute with `python3 panhandle_covariance_check.py`; the expected final line begins `PANHANDLE_VERTEX_COVARIANCE_SPECTRAL_CHECKS_PASSED`. The proof is algebraic and does not depend on those finite checks.

## Relationship to prior work
Hanely, Martin, McGinnis, Miyata, Nasr, Vindas-Meléndez and Yin (arXiv:2201.12442, first posted 2022-01-28) define panhandle matroids and identify their base polytopes as single-halfspace truncations of hypersimplices; their calculations concern rank, facets, Ehrhart polynomials and volume. Deligeorgaki, McGinnis and Vindas-Meléndez (arXiv:2311.01640, first posted 2023-11-02) establish Ehrhart coefficient results for the same family. Ferroni and Schröter (arXiv:2208.04893) study valuative matroid invariants and split-polytopal subdivisions, not uniform-vertex covariance eigenvalues. Huh, Schröter and Wang (arXiv:1806.02675 / JEMS 2022) establish general correlation inequalities for random matroid bases, which do not specify this full panhandle spectrum, crossing or anisotropy limit. In particular, the word *spectrum* in some matroid literature refers to the independence-complex spectrum polynomial, not the Euclidean covariance operator studied here.

## Limitations
This is a complete second-moment classification of the **uniform vertex** measure only. It is not a claim about uniform interior volume, covariance of a basis-exchange random walk, the independence-complex Laplacian, or the John/Löwner ellipsoids. It does not give higher moments, quantitative convergence rates, or an optimum conditioning result among all matroids. Historical priority remains provisional because equivalent formulations under sampling, occupancy, or second-moment terminology may exist despite the source comparisons; independent expert audit has not occurred.

## References
- D. Hanely, J. L. Martin, D. McGinnis, D. Miyata, G. D. Nasr, A. R. Vindas-Meléndez, M. Yin, *Ehrhart Theory of Paving and Panhandle Matroids*, arXiv:2201.12442, first posted 2022-01-28. In particular Definition 4.1 and Proposition 4.4.
- D. Deligeorgaki, D. McGinnis, A. R. Vindas-Meléndez, *Ehrhart Bounds for Panhandle and Paving Matroids Through Enumeration of Chain Forests*, arXiv:2311.01640, first posted 2023-11-02. In particular Section 1 and its stated basis system.
- L. Ferroni, B. Schröter, *Valuative invariants for large classes of matroids*, J. London Math. Soc. 110 (2024), e12984, DOI:10.1112/jlms.12984, arXiv:2208.04893.
- J. Huh, B. Schröter, B. Wang, *Correlation bounds for fields and matroids*, J. Eur. Math. Soc. 24 (2022), 1335–1351, DOI:10.4171/JEMS/1119, arXiv:1806.02675.
