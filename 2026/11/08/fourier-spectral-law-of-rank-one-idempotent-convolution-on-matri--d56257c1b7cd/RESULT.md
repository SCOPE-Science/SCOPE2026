# Fourier spectral law of rank-one idempotent convolution on matrix spaces

## Finding
Let \(p\) be a prime, \(n\ge 3\), and let \(G=M_n(\mathbb F_p)\) under addition. Let \(\mathcal P\) consist of rank-one idempotents, and define convolution \((C_{n,p}f)(X)=\sum_{P\in\mathcal P}f(X+P)\) on \(\ell^2(G)\). Write \(m_\lambda(A)=\dim_{\mathbb F_p}\ker(A-\lambda I)\), \(\zeta_p=e^{2\pi i/p}\), and \(Q_j(p)=\prod_{r=1}^j(1-p^{-r})\), with \(Q_0(p)=1\).

**Exact Fourier diagonalization.** For every \(A\in G\), the Fourier character \(X\mapsto\zeta_p^{\operatorname{tr}(AX)}\) has multiplier
\[
\Lambda_{n,p}(A)=\frac{p^{n-1}}{p-1}\sum_{\lambda\in\mathbb F_p}p^{m_\lambda(A)}\zeta_p^\lambda.
\]
Therefore \(\Lambda_{n,p}(A)=0\) if and only if all \(p\) eigenspace dimensions \(m_\lambda(A)\) are equal. These are **all** the convolution eigenvalues, with multiplicity one per matrix-frequency, and the singular values are their absolute values.

**Exact finite-dimensional rank.** For a vector \(\boldsymbol u=(u_\lambda)_{\lambda\in\mathbb F_p}\) of nonnegative integers, set \(t=\sum_\lambda u_\lambda\) and
\[
M_{n,p}(\boldsymbol u)=\begin{cases}
\dfrac{Q_n(p)}{Q_{n-t}(p)}\displaystyle\prod_\lambda\dfrac{p^{-u_\lambda^2}}{Q_{u_\lambda}(p)},&t\le n,\\[2mm]
0,&t>n.
\end{cases}
\]
Let \({a\brack b}_p\) denote the Gaussian binomial coefficient. For each nonnegative vector \(\boldsymbol k\), define the finite sum
\[
P_{n,p}(\boldsymbol k)=
\sum_{\substack{\boldsymbol u\ge\boldsymbol k\\\sum u_\lambda\le n}}
(-1)^{\sum_\lambda(u_\lambda-k_\lambda)}
p^{\sum_\lambda\binom{u_\lambda-k_\lambda}{2}}
\left(\prod_\lambda{u_\lambda\brack k_\lambda}_p\right)
M_{n,p}(\boldsymbol u).
\]
Then \(P_{n,p}(\boldsymbol k)\) is exactly the fraction of frequency matrices \(A\) satisfying \(m_\lambda(A)=k_\lambda\) for all \(\lambda\), and
\[
\operatorname{rank} C_{n,p}=p^{n^2}\left(1-\sum_{k=0}^{\lfloor n/p\rfloor}P_{n,p}(k,\ldots,k)\right).
\]
The formula counts rank and nullity exactly for every prime \(p\) and every \(n\ge3\); no classification of Jordan forms is needed.

**Complete limiting spectral measure.** For fixed prime \(p\) let \(Q_\infty(p)=\prod_{r\ge1}(1-p^{-r})\), and let \(J_0,\ldots,J_{p-1}\) be independent random variables with
\[
\Pr(J_\lambda=k)=Q_\infty(p)\frac{p^{-k^2}}{Q_k(p)^2}\quad(k=0,1,\ldots).
\]
As \(n\to\infty\), the empirical eigenvalue measure of \(p^{1-n}C_{n,p}\) converges weakly on \(\mathbb C\) to the law of
\[
Z_p=\frac1{p-1}\sum_{\lambda=0}^{p-1}p^{J_\lambda}\zeta_p^\lambda.
\]
Consequently the normalized singular-value measures converge to the law of \(|Z_p|\), and the nullity fraction converges to the **explicit positive atom**
\[
H_p=Q_\infty(p)^p\sum_{k=0}^\infty \frac{p^{-pk^2}}{Q_k(p)^{2p}}.
\]
Furthermore \(\lim_{p\to\infty\atop p\text{ prime}}H_p=e^{-1}\). The order of limits in this last assertion is dimension first, then prime.

## Assumptions and scope
The scalar field for the matrix entries is a **prime field** \(\mathbb F_p\); the complex Fourier characters use \(\zeta_p\). The main statements cover every \(n\ge3\), though the proof also gives the corresponding formulas for \(n=1,2\). Convolution is unnormalized. The rank is the complex-linear rank on functions on the additive group \(M_n(\mathbb F_p)\), of dimension \(p^{n^2}\). The asymptotic measure fixes \(p\) and varies \(n\); it is not a claim of uniformity in \(p\).

## Proof
**Step 1 — character sum.** Every rank-one idempotent has the form \(P=uv^{\mathsf T}\), with \(0\ne u\in\mathbb F_p^n\) and \(v^{\mathsf T}u=1\). Every such \(P\) has exactly \(p-1\) representations, by \((u,v)\mapsto(cu,c^{-1}v)\). For fixed \(u\), summing \(\zeta_p^{v^{\mathsf T}Au}\) over the affine hyperplane \(v^{\mathsf T}u=1\) yields zero unless \(Au=\lambda u\) for some \(\lambda\in\mathbb F_p\); then the sum is \(p^{n-1}\zeta_p^\lambda\). There are \(p^{m_\lambda(A)}-1\) nonzero such \(u\) per eigenvalue. Therefore
\[
\sum_{P\in\mathcal P}\zeta_p^{\operatorname{tr}(AP)}
=\frac{p^{n-1}}{p-1}\sum_\lambda (p^{m_\lambda(A)}-1)\zeta_p^\lambda
=\frac{p^{n-1}}{p-1}\sum_\lambda p^{m_\lambda(A)}\zeta_p^\lambda.
\]
The Fourier characters diagonalize the explicitly defined \(X+P\) convolution with precisely the displayed multiplier \(\Lambda_{n,p}(A)\). Under the alternative \(X-P\) convention, each character multiplier is complex-conjugated; this does not change the multiset or the singular values, since the map \(A\mapsto -A\) is a bijection of frequencies. Since the cyclotomic polynomial \(1+T+\cdots+T^{p-1}\) is the minimal polynomial of \(\zeta_p\), an integer linear combination \(\sum c_\lambda\zeta_p^\lambda\) vanishes exactly when all \(c_\lambda\) are equal. This proves the zero criterion and rank characterization.

**Step 2 — Gaussian mixed factorial moments.** Write \(X_\lambda(A)=m_\lambda(A)\) for a uniform \(A\). The Gaussian binomial coefficient \({X_\lambda\brack u_\lambda}_p\) counts subspaces of dimension \(u_\lambda\) in its \(\lambda\)-eigenspace. Distinct eigenspaces form an internal direct sum. Let \(s_j\) be cumulative selected dimensions. The number of ordered subspaces \((U_\lambda)\) of dimensions \(u_\lambda\) with direct sum is \(\prod_\lambda {n-s_{\lambda-1}\brack u_\lambda}_p p^{u_\lambda s_{\lambda-1}}\). For any such choice the constraints \(A|_{U_\lambda}=\lambda I\) fix \(nt\) independent matrix entries relative to a direct-sum basis, hence occur with probability \(p^{-nt}\). Multiplying and telescoping \({a\brack b}_p=p^{b(a-b)}Q_a(p)/(Q_b(p)Q_{a-b}(p))\) gives exactly
\[
\mathbb E\prod_\lambda{X_\lambda\brack u_\lambda}_p=M_{n,p}(\boldsymbol u).
\]
If \(t>n\), the product vanishes identically.

**Step 3 — finite Gaussian inversion.** For nonnegative integers \(x,k\), the Gaussian binomial theorem yields
\[
\mathbf1_{\{x=k\}}=
\sum_{u=k}^x(-1)^{u-k}p^{\binom{u-k}{2}}{u\brack k}_p{x\brack u}_p.
\]
Multiply this identity over the \(p\) eigenvalues, take expectation, substitute the mixed moments of Step 2, and obtain \(P_{n,p}(\boldsymbol k)\). Setting the dimensions equal gives the exact nullity and rank formula.

**Step 4 — limit of the joint law.** Fix \(p\) and \(\boldsymbol u\); then \(Q_n/Q_{n-t}\to1\), so the mixed factorial moment tends to \(\prod_\lambda p^{-u_\lambda^2}/Q_{u_\lambda}\). The inversion series from Step 3 is absolutely dominated, for fixed \(\boldsymbol k\), by a product of terms of size at most \(C_{p,\boldsymbol k}p^{-\frac12\sum u_\lambda^2+O(\sum u_\lambda)}\): use \(Q_n/Q_{n-t}\le1\), \(Q_u\ge Q_\infty>0\), and \({u\brack k}_p\le p^{k(u-k)}/Q_k\). The joint probabilities therefore converge termwise to products of the one-coordinate limits. The standard finite-matrix kernel count (or the same one-variable Gaussian inversion) evaluates each marginal as \(Q_\infty p^{-k^2}/Q_k^2\), and these probabilities sum to one by Euler's \(q\)-binomial product identity. Thus there is no escaping mass, the joint limit is independent, and the continuous mapping theorem gives the complex multiplier and absolute-singular-value weak limits.

**Step 5 — zero atom and large-prime limit.** By Step 1 the zero event is \(J_0=\cdots=J_{p-1}\). Independence gives \(H_p=\sum_k\pi_p(k)^p\), the displayed convergent series. Since \(Q_\infty(p)=1-p^{-1}+O(p^{-2})\), one has \(Q_\infty(p)^p\to e^{-1}\). The tail of the sum from \(k=1\) is at most \(Q_\infty(p)^{-2p}\sum_{k\ge1}p^{-pk^2}\), which tends to zero, proving the final limit.

## Verification
The reproducible Python 3 program `verify_idempotent_spectrum.py` uses only the standard library and exact integer/fraction arithmetic. It enumerates all frequency matrices for \((p,n)=(2,2),(2,3),(2,4),(3,2),(3,3)\). It verifies the character-sum residue identity for all frequencies in each listed case except \((2,4)\), where it still verifies all Gaussian mixed-moment identities and all histogram probabilities by inversion. The exact zero counts are respectively \(8/16\), \(216/512\), \(28224/65536\), \(18/81\), and \(4860/19683\). The program prints `IDEMPOTENT_FOURIER_JOINT_MOMENT_CHECKS_OK`. These are finite consistency checks; the general theorem is proved in Steps 1–5.

## Relationship to prior work
The classical additive Fourier diagonalization of convolution is used without novelty claim. Fulman's survey of finite-field random matrices (first public March 28, 2000, arXiv:math/0003195, §§2–3) supplies stronger general cycle-index machinery that determines large-dimensional laws of rational eigenvalue primary components; the independent limiting eigenspace laws and the no-rational-eigenvalue component are **not claimed as new standalone random-matrix theory**. A previously established \(2\times2\) rank-one-idempotent convolution classification supplies the small-dimensional antecedent. The result here is the explicit combination for the full higher-dimensional additive-convolution operator, including the exact zero eigenspace criterion, the finite Gaussian-inversion rank expression, and the associated **complete limiting complex and singular spectral laws**. These consequences may be derivable from stronger unlocated character-sum or random-matrix work; priority is not asserted unconditionally.

## Limitations
The exact finite-rank expression is a finite multiple sum, not a closed product in general; this is a genuine computational cost for large \(p,n\). The limiting spectral distribution is discrete, may have overlapping values, and is stated as the pushforward of an independent product law, not as an explicit list of distinct atoms and their combined multiplicities. There are no claims for non-prime base fields, growing \(p\) jointly with \(n\), operator-norm convergence, or quantitative convergence rates. Independent peer validation has not been performed.

## References
1. J. Fulman, *Random Matrix Theory over Finite Fields: A Survey*, arXiv:math/0003195, first public March 28, 2000, https://arxiv.org/abs/math/0003195 ; especially finite-matrix cycle indices and conjugacy-class randomization.
2. J. Fulman and L. Goldstein, *Stein's Method and the Rank Distribution of Random Matrices over Finite Fields*, 2015, https://arxiv.org/abs/1211.0504 ; comparison for one-eigenspace marginals.
3. G. E. Andrews, *The Theory of Partitions*, Addison-Wesley (1976), q-binomial identities and Euler products.
