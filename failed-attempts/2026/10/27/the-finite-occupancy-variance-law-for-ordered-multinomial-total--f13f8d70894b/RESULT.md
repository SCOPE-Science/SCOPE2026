# The finite-occupancy variance law for ordered multinomial total variation

## Finding
Let \((X_1,\ldots,X_n)\) have the uniform multinomial distribution with \(N\) trials and \(n\) ordered cells. Put
\[
T_{n,N}=\sum_{j=1}^{n-1}|X_{j+1}-X_j|,\qquad \lambda_n=N/n.
\]
For \(\lambda>0\), let \(Z,Z'\) be independent \(\operatorname{Pois}(\lambda)\) variables, and write
\[
\mu(\lambda)=\mathbb E|Z-Z'|=2\lambda e^{-2\lambda}[I_0(2\lambda)+I_1(2\lambda)],
\]
\[
h_\lambda(k)=\mathbb E|k-Z'|,\qquad
\tau(\lambda)=\mathbb E[h_\lambda(Z)^2],
\]
where \(I_0,I_1\) are modified Bessel functions of the first kind. Define the explicit positive function
\[
\boxed{v(\lambda)=2\lambda+2\tau(\lambda)-3\mu(\lambda)^2
       -4\lambda e^{-4\lambda}I_0(2\lambda)^2.}
\]
**Theorem.** For every \(0<a<b<\infty\), uniformly over integers \(n\to\infty\) and \(N\) with \(a\le N/n\le b\),
\[
\boxed{\operatorname{Var}(T_{n,N})=n\,v(N/n)+O_{a,b}(1).}
\]
Consequently, if \(N_n/n\to\lambda\in(0,\infty)\), then \(\operatorname{Var}(T_{n,N_n})/n\to v(\lambda)>0\). The nonlocal correction is sharp: for any four distinct consecutive cells,
\[
\boxed{n\,\operatorname{Cov}(|X_2-X_1|,|X_4-X_3|)
\longrightarrow -4\lambda e^{-4\lambda}I_0(2\lambda)^2.}
\]
The coefficient obeys
\[
\boxed{v(\lambda)=4\lambda^2-12\lambda^3+O(\lambda^4)
\quad(\lambda\downarrow0),}
\]
and the previously known Gaussian high-intensity coefficient is recovered:
\[
\boxed{\lim_{\lambda\to\infty}\frac{v(\lambda)}{\lambda}
=\frac83+\frac{4(\sqrt3-3)}{\pi}.}
\]
These last two assertions concern the explicitly defined function \(v\), not a uniform simultaneous limit with \(\lambda_n\to0\) or \(\lambda_n\to\infty\).

## Assumptions and scope
All cell probabilities equal \(1/n\); counts sum exactly to \(N\). The order of cells is fixed, the linear (noncyclic) edge statistic is used, and \(n\ge4\) for the four-cell covariance. There is no independence assumption on multinomial cells. The uniform remainder requires \(N/n\) in an arbitrary fixed compact subinterval of \((0,\infty)\); the constants can depend on its endpoints. The positive Poisson intensity \(\lambda\) is otherwise unrestricted.

The series defining the coefficient converges absolutely and can be evaluated without multidimensional summation:
\[
 h_\lambda(k)=k-\lambda+2\bigl[\lambda\Pr(Z\ge k)-k\Pr(Z\ge k+1)\bigr],
\quad
 \tau(\lambda)=e^{-\lambda}\sum_{k=0}^{\infty}\frac{\lambda^k}{k!}h_\lambda(k)^2.
\]
For \(k=0\), the displayed tail identity uses the usual \(\Pr(Z\ge0)=1\).

## Proof
**1. Uniform finite-dimensional Poisson expansion.** Fix \(k\in\{2,3,4\}\). For a nonnegative integer vector \(x=(x_1,\ldots,x_k)\), let \(s=\sum_i x_i\) and \(\lambda_n=N/n\). The exact marginal law is
\[
 P_{n,k}(x)=\frac{(N)_s}{n^s\prod_i x_i!}
                 (1-k/n)^{N-s},\quad s\le N.
\]
Set \(Q_{\lambda_n,k}(x)=e^{-k\lambda_n}\lambda_n^s/\prod_i x_i!\), the law of \(k\) independent Poisson cells. Direct Taylor expansion yields
\[
 \frac{P_{n,k}(x)}{Q_{\lambda_n,k}(x)}
 =1+\frac{r_{k,\lambda_n}(s)}{n}
    +O_{a,b}\!\left(\frac{(1+s)^4}{n^2}\right),\qquad
 r_{k,\lambda}(s)=-\frac{s(s-1)}{2\lambda}+ks-\frac{\lambda k^2}{2},
\]
uniformly for \(s\le n^{1/8}\) and \(a\le\lambda_n\le b\). Here the expansions are \(\sum_{j<s}\log(1-j/N)=-s(s-1)/(2N)+O(s^3/N^2)\) and \((N-s)\log(1-k/n)=-k\lambda_n+(ks-k^2\lambda_n/2)/n+O((1+s)/n^2)\). The tails beyond \(s=n^{1/8}\) are uniformly smaller than any inverse polynomial, because under \(P_{n,k}\), \(s\sim\operatorname{Bin}(N,k/n)\), and under \(Q\), \(s\sim\operatorname{Pois}(k\lambda_n)\), both with means bounded by \(kb\). Therefore, for any fixed polynomially bounded function of these \(k\) coordinates, replacing the probability by \(Q(1+r/n)\) has error \(O_{a,b}(n^{-2})\). This is a weighted \(\ell^1\) expansion, not merely pointwise convergence.

**2. The three covariance types.** Let \(H_i=|X_{i+1}-X_i|\) and \(\mu_n=\mu(\lambda_n)\). By the \(k=2\) expansion, \(\mathbb EH_i=\mu_n+O_{a,b}(n^{-1})\). The second moment is exactly \(\mathbb EH_i^2=\mathbb E(X_{i+1}-X_i)^2=2\lambda_n\). Hence
\[
 A_n:=\operatorname{Var}(H_1)=2\lambda_n-\mu_n^2+O_{a,b}(n^{-1}).
\]
For adjacent edges, the three-dimensional Poisson limit gives
\[
 B_n:=\operatorname{Cov}(H_1,H_2)
 =\tau(\lambda_n)-\mu_n^2+O_{a,b}(n^{-1}),
\]
since conditional on their common Poisson cell the two absolute differences have mean \(h_{\lambda_n}\) and are independent.

For disjoint edges let \(S=X_1+X_2\), \(R=X_3+X_4\). In the independent Poisson law the corresponding totals are independent and both have mean \(2\lambda_n\). The first-order expansion contains an exact cancellation:
\[
 r_{4,\lambda}(s+t)-r_{2,\lambda}(s)-r_{2,\lambda}(t)
 =-\frac{(s-2\lambda)(t-2\lambda)}{\lambda}.
\]
Consequently the covariance of the two absolute contrasts is
\[
 C_n=-\frac{c(\lambda_n)^2}{\lambda_n n}+O_{a,b}(n^{-2}),
 \quad c(\lambda)=\operatorname{Cov}(|Z-Z'|,Z+Z').
\]
To evaluate \(c\), differentiate Poisson expectations, obtaining the score identity
\[
 c(\lambda)=\lambda\mu'(\lambda)
 =2\lambda e^{-2\lambda}I_0(2\lambda).
\]
The displayed Bessel identity for \(\mu\) follows from the Skellam probabilities \(\Pr(Z-Z'=j)=e^{-2\lambda}I_{|j|}(2\lambda)\) and the recurrence \(jI_j(2\lambda)=\lambda[I_{j-1}(2\lambda)-I_{j+1}(2\lambda)]\). Differentiation gives \(\mu'=2e^{-2\lambda}I_0(2\lambda)\).

**3. Exact counting and the uniform remainder.** There are \(n-1\) edge terms, \(n-2\) unordered adjacent edge pairs and \((n-2)(n-3)/2\) unordered disjoint edge pairs. Thus exactly
\[
 \operatorname{Var}(T_{n,N})=(n-1)A_n+2(n-2)B_n+(n-2)(n-3)C_n.
\]
Substitution gives \(n[2\lambda_n+2\tau(\lambda_n)-3\mu_n^2-c(\lambda_n)^2/\lambda_n]+O_{a,b}(1)\), as required. The critical point is that each of the \(\Theta(n^2)\) disjoint pairs has covariance of order \(n^{-1}\); treating it as independent gives an incorrect order-\(n\) variance.

**4. Strict positivity.** In an independent Poisson sequence define \(q(z)=h_\lambda(z)-\mu(\lambda)\) and the centered degenerate edge kernel
\[
 g(z,w)=|z-w|-\mu(\lambda)-q(z)-q(w).
\]
Then \(\mathbb E[g(Z,Z')\mid Z]=\mathbb E[g(Z,Z')\mid Z']=0\). Put \(\gamma=\operatorname{Cov}(q(Z),Z)/\lambda\). By direct orthogonal expansion,
\[
 v(\lambda)=4\operatorname{Var}\bigl(q(Z)-\gamma(Z-\lambda)\bigr)
                 +\mathbb E[g(Z,Z')^2].
\]
Indeed \(\operatorname{Cov}(|Z-Z'|,Z+Z')=2\operatorname{Cov}(q(Z),Z)\), so the second term from the sample-size constraint is precisely the squared linear projection. The second summand is strictly positive: \(g\equiv0\) would require the absolute-difference kernel to be additive, whereas its mixed rectangle at coordinates \(0,1\) equals \(0+0-1-1=-2\). Every such Poisson rectangle has positive probability for \(\lambda>0\). Thus \(v(\lambda)>0\).

**5. Boundary values of the coefficient.** Expanding the absolutely convergent Poisson series at zero gives
\[
 \mu=2\lambda-2\lambda^2+2\lambda^3+O(\lambda^4),
\quad \tau=\lambda+2\lambda^3+O(\lambda^4),
\]
and substituting in \(v\) yields \(4\lambda^2-12\lambda^3+O(\lambda^4)\). For the high-intensity coefficient, \((Z-Z')/\sqrt{2\lambda}\) and pairs of adjacent contrasts converge in moments to centered normal contrasts whose adjacent correlation is \(-1/2\). The bivariate Gaussian formula
\[
 \mathbb E|G_1G_2|=\frac{2}{\pi}
 \bigl(\sqrt{1-\rho^2}+\rho\arcsin\rho\bigr)
\]
for unit-variance normals produces the stated \(\lambda\)-coefficient; the conditioning subtraction \(c(\lambda)^2/\lambda\) is only \(O(1)\) by the Bessel large-argument asymptotic. That high-intensity constant was already derived in the motivating article and is recorded only as a consistency check.

## Verification
Run `python check_sparse_variance.py` using Python 3 standard library. The supplied `check_sparse_variance_output.txt` records **90 passed assertions**: exact small multinomial enumeration, agreement of the finite covariance decomposition with direct variance, Poisson/Bessel and score identities, disjoint-edge scaling, positive coefficients and limiting numerical crosschecks. For example \(v(1)=0.918614881174\ldots\), versus the independent-Poisson edge-variance density \(2+2\tau(1)-3\mu(1)^2=1.299324421513\ldots\); the difference \(0.380709540340\ldots\) is the necessary fixed-total correction. Exact finite calculations and floating-point experiments corroborate the proof but do not replace the uniform weighted-Poisson expansion.

## Relationship to prior work
Banić and Elezović's arXiv:2610.17046v1 (first publicly submitted 2026-10-12), Sections 3–4 and 7, establishes the exact decomposition for finite parameters and a **fixed-\(n\), \(N\to\infty\)** expansion. Its concluding remarks explicitly distinguish and leave unanalyzed the joint large-\(n\), large-\(N\) regime; its Corollary 3.5 already proves the Gaussian high-intensity constant cited above. The present statement extracts and rigorously controls the distinct finite-cell-intensity window \(N/n\to\lambda\in(0,\infty)\) and calculates its dependence-induced variance correction. Its exact finite variance formula is acknowledged as broader finite-parameter information, not claimed afresh. Banić and Elezović's arXiv:2610.13366v1 (first publicly submitted 2026-10-09) analyzes the first moment under the same null, but not the variance in this joint limit. The classical Poissonization principle, Skellam identities and Gaussian folded-moment formula are background facts, not original claims here.

## Limitations
The expansion is **not** asserted uniformly as \(\lambda_n\downarrow0\) or \(\lambda_n\to\infty\); its finite-intensity assumption is essential to the proved error bound. No central limit theorem, nonuniform-bin extension, cyclic-statistic theorem or testing-power claim is proved. The source provides an exact finite-parameter expression; a specialist should review priority against that expression, related occupancy functional limit theory and any subsequently released parts of the authors' series. The historical paper search cannot establish absolute uniqueness.

## References
1. N. Banić and N. Elezović, *Discrete total variation under the multinomial, Part 2: variance under the uniform null*, arXiv:2610.17046v1 (2026-10-12). https://arxiv.org/html/2610.17046v1
2. N. Banić and N. Elezović, *Discrete total variation under the multinomial, Part 1: expectation under the uniform null*, arXiv:2610.13366v1 (2026-10-09). https://arxiv.org/html/2610.13366v1
3. N. Banić and N. Elezović, *TVOR: Finding Discrete Total Variation Outliers among Histograms*, IEEE Access 9 (2021), 1807–1832; preprint arXiv:2012.11574.
4. Classical Poisson and Skellam identities; the folded bivariate-normal formula, as cited and used in Reference 1.
