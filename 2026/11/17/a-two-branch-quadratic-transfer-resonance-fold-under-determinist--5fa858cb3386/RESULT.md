# A two-branch quadratic-transfer resonance fold under deterministic skew-tent switching

## Finding
For the full-height skew-tent map
\[
T_s(x)=\begin{cases}x/s,&0\leq x\leq s,\\(1-x)/(1-s),&s\leq x\leq1,\end{cases}\qquad 0<s<1,
\]
let \(F=T_b\circ T_a\) denote one deterministic two-season return. Suppose \(1/2<a<2/3\) and \(2/3<b<1\). Define
\[
g(s)=2s-1,\qquad h(s)=3s^2-3s+1,\qquad c(s)=s(1-s),
\]
\[
\lambda_1=g(a)g(b),\quad\lambda_2=h(a)h(b),\quad C=-c(a)g(b)-h(a)c(b).
\]
The restriction of the Perron–Frobenius operator of \(F\) to mean-zero quadratic polynomials has a nonsemisimple double eigenvalue exactly when \(\lambda_1=\lambda_2\). This is a genuine two-by-two Jordan block, because \(C<0\). Moreover, its common eigenvalue is larger in modulus than every polynomial transfer eigenvalue of degree at least three.

The *entire* resonance locus inside the indicated rectangle has a sharp fold. Put
\[
a_*=(9+4\sqrt3-\sqrt{21})/18,\qquad b_*=(3+\sqrt3)/6.
\]
For fixed \(a\in(1/2,2/3)\), there are no resonant \(b\in(2/3,1)\) if \(a<a_*\), exactly one (a double parameter root) if \(a=a_*\), and exactly two if \(a_*<a<2/3\). At the threshold the unique choice is \(b=b_*\). Every resonant map in this rectangle has distinct quadratic transfer eigenvalues in each individual season.

At any of these resonances, let \(X\) be uniform on \([0,1]\), and set \(W(x)=x^2-1/3\). Then, for every integer \(n\geq1\), the *exact*, not merely asymptotic, two-season squared-position covariance is
\[
\operatorname{Cov}(X^2,F^n(X)^2)=\frac4{45}\lambda^n+\frac{C}{12}n\lambda^{n-1},\qquad \lambda=\lambda_1=\lambda_2.
\]
It is strictly negative when \(n>16\lambda/(15|C|)\), whereas its zero-lag value is \(4/45>0\). A concrete two-choice exact example takes \(a=13/20\) and
\[
b_{\pm}=207/254\pm \sqrt{9213}/762.
\]
Both are resonant and lie in \((2/3,1)\). For \(b_-\), the covariance is already negative at lag one return; for \(b_+\), it is positive at one return and negative from the second return onward.

## Assumptions and scope
The underlying interval is the closed unit interval with Lebesgue measure. Each season is a full-branch, strictly expanding piecewise-affine map. The two-season return \(F\) applies \(T_a\) first, \(T_b\) second, and then repeats this order. Covariance refers to the invariant Lebesgue law, not a random switching environment. The polynomial transfer assertion is about the invariant spaces of polynomial densities, not a claim that the repeated eigenvalue is isolated on the entire bounded-variation space. The resonance-count classification is asserted only for \(1/2<a<2/3< b<1\); other parameter sectors are not classified here. The time index \(n\) counts complete two-season returns.

## Proof
**Invariant measure and invariant polynomials.** Each full branch of \(T_s\) maps onto \([0,1]\), with inverse Jacobian weights \(s\) and \(1-s\). Hence its Perron–Frobenius operator is
\[
(P_s f)(x)=s f(sx)+(1-s)f(1-(1-s)x),
\]
and \(P_s1=1\), so Lebesgue measure is invariant. Setting \(u(x)=x-1/2\) and \(v(x)=x^2-x+1/6\), direct expansion gives
\[
P_su=g(s)u,\qquad P_sv=h(s)v-c(s)u.
\]
Both \(u\) and \(v\) have mean zero. The first-season/second-season return has transfer operator \(P=P_bP_a\), so on \(\operatorname{span}\{u,v\}\), in the ordered basis \((u,v)\),
\[
[P]=\begin{pmatrix}\lambda_1&C\\0&\lambda_2\end{pmatrix}.
\]
In the stated parameter rectangle \(g(b),h(a),c(a),c(b)>0\). Therefore \(C<0\). If \(\lambda_1=\lambda_2=\lambda\), then \(P=\lambda I+N\) with \(N^2=0\) and \(N\ne0\): it has precisely one eigenvector in this two-dimensional space, and
\[
P^n v=\lambda^n v+n\lambda^{n-1}C u,\qquad P^n u=\lambda^n u.
\]
No limiting argument is used.

**Sharp resonance count.** Define \(R(s)=g(s)/h(s)\). Since both factors are positive on \((1/2,1)\), the equation \(\lambda_1=\lambda_2\) is equivalent to \(R(a)R(b)=1\). Its derivative is
\[
R'(s)=\frac{-6s^2+6s-1}{h(s)^2}.
\]
Thus \(R\) increases strictly from zero to one as \(s\) moves from \(1/2\) to \(2/3\), while on \((2/3,1)\) it rises strictly from one to its unique maximum \(2/\sqrt3\) at \(b_*=(3+\sqrt3)/6\), then falls strictly to one at \(s=1\). Consequently the number of roots in \((2/3,1)\) of \(R(b)=1/R(a)\) is zero, one, or two according to \(R(a)\) being below, equal to, or above \(\sqrt3/2\). Solving \(R(a)=\sqrt3/2\) for its unique root in \((1/2,2/3)\) gives exactly the displayed \(a_*\). This is a fold of the parameter projection, not an assertion of a cusp singularity of the resonance curve itself. Every admissible resonant \(a\) and \(b\) differs from \(2/3\), whereas the single-season equality \(g(s)=h(s)\) on \((1/2,1)\) holds only at \(s=2/3\) (or the excluded endpoint one).

**Polynomial-mode dominance.** For a polynomial of degree \(k\), the coefficient of its leading monomial under \(P_s\) is multiplied by \(d_k(s)=s^{k+1}+(-1)^k(1-s)^{k+1}\). Consequently the degree-\(k\) diagonal entry for \(P_bP_a\) is \(d_k(a)d_k(b)\), for any finite polynomial-degree restriction. For every \(k\geq3\) and \(0<s<1\),
\[
|d_k(s)|\leq s^{k+1}+(1-s)^{k+1}\leq s^4+(1-s)^4<s^3+(1-s)^3=h(s).
\]
The inequalities show \(|d_k(a)d_k(b)|<\lambda_2\); at resonance \(\lambda_1=\lambda_2\) these are the two leading nonconstant polynomial diagonal entries. The constant mode retains the simple eigenvalue one.

**Physical covariance.** On \([0,1]\), \(\int u^2=1/12\), \(\int v^2=1/180\), \(\int uv=0\), and \(W=u+v\). The transfer duality formula gives
\[
\int_0^1 W(x)W(F^n(x))\,dx=\int_0^1 W(x)(P^nW)(x)\,dx,
\]
so substitution of the Jordan power formula yields the covariance identity. Since \(\lambda>0\) and \(C<0\), its sign is the sign of \(4\lambda/45+Cn/12\), proving the strict negative threshold. For the explicit example substitute \(a=13/20\) into \(g(a)g(b)=h(a)h(b)\), obtaining the quadratic \(381b^2-621b+247=0\), with the two displayed roots. Using the rational bound \(9598/100<\sqrt{9213}<96\), whose endpoints are verified by squaring, direct substitution into \(16\lambda/(15|C|)\) and rational interval arithmetic gives respectively values strictly between \(0.78\) and \(0.80\), and strictly between \(1.28\) and \(1.31\). These disjoint rational brackets establish the two different first negative lags.

## Verification
The standalone `checker.py` uses SymPy to verify all degree-one/degree-two transfer identities, the two-season off-diagonal, orthogonality constants, threshold identities, and exact algebraic resonance at both explicit parameters. Separately it evaluates each covariance by summing fourth-degree polynomial Gauss–Legendre quadratures on *all* \(4^n\) inverse branches of the original two-season map, for \(n=1,2,3,4\), at high precision, and compares the result to the exact Jordan formula. Its expected completion line is `SEASONAL_SKEW_TENT_JORDAN_OK symbolic_operator=PASS exact_resonance=2 full_branch_correlation_cases=8`. These finite checks validate calculations but are not used to prove the infinite statements; the proof above supplies those quantifiers.

## Relationship to prior work
Bruin and Keszthelyi studied the two-parameter skew-tent family and orbit-density questions. Our maps are the full-height subfamily, but the present question is the quadratic transfer spectrum and exact deterministic seasonal covariance, rather than typical critical orbits. Butterley, Kiamari and Liverani provided a general framework for transfer spectra and Jordan blocks in affine Markov interval maps, while Suzuki studied nonleading eigenvalues of \(\beta\)-transformations. Their general framework does not state the specific two-resonance fold, its sharp parameter threshold, or the displayed covariance and sign-lag classification for deterministic compositions of full-height skew tent maps. A separate published finding treats *independent random mixtures* of full-height skew tent transfer operators and an exact Jordan-induced correlation; its mixing operator is a convex combination, not the deterministic ordered product considered here. Such general spectral/Jordan phenomena are prior knowledge; we claim neither discovery of Jordan blocks in transfer operators nor the general spectral theory.

## Limitations
The assertion covers the identified positive-branch rectangle and polynomial observables. It does not classify all parameter sectors, general initial densities, all BV spectral components, or full-system mixing rates. The exact formula computes two-season correlations from the invariant uniform law; no corresponding random-switching statement is asserted. The available public summary of the closest random-mixture finding could be read, but its complete linked repository text was unavailable; hidden stronger content therefore remains a publication-priority risk. Other equivalent treatments may exist beyond the checked sources. No independent mathematical audit or external certification has been performed.

## References
1. H. Bruin and G. Keszthelyi, *On co-\(\sigma\)-porosity of the parameters with dense critical orbits for skew tent maps and matching on generalized \(\beta\)-transformations*, first public preprint 2021-06-08, arXiv:2106.04711, https://arxiv.org/abs/2106.04711.
2. O. Butterley, N. Kiamari and C. Liverani, *Locating Ruelle–Pollicott resonances*, arXiv:2012.13145 (2020), Nonlinearity 35 (2022), https://arxiv.org/abs/2012.13145.
3. S. Suzuki, *Non-leading eigenvalues of the Perron–Frobenius operators for beta-maps*, first public 2024-10-01, arXiv:2410.00411, https://arxiv.org/abs/2410.00411.
4. *Noise-induced quadratic Jordan resonance in randomly switched skew tent maps*, public mathematical research summary (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-noise-induced-quadratic-jordan-resonance-in-randomly-switched-sk--3359bfd9dd8c (full linked material unavailable during comparison).
