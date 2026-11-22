# Sharp \(BV\)-to-\(L^1\) mean-mixing for iterated Bernstein–Kantorovich operators

## Finding
For each integer \(n\ge1\) and \(r\ge1\), the sharp integrated error of the \(r\)-fold classical Bernstein–Kantorovich operator from its invariant Lebesgue mean on real distributional \(BV(0,1)\) has an exact finite-grid-step formula. Let \(m=n+1\), \(I_i=(i/m,(i+1)/m)\), and \(b_i(x)=\binom ni x^i(1-x)^{n-i}\). Form the rational doubly stochastic matrix
\[
M_{ij}=m\int_{I_i}b_j(x)\,dx\quad(0\le i,j\le n),
\]
and the columns \(v_j=(\mathbf1_{i<j})_{i=0}^n\) for \(1\le j\le n\). Set \(c_{j,r}=M^{r-1}v_j\), \(F_{j,r}(x)=\sum_{i=0}^n(c_{j,r})_i b_i(x)\), and \(\theta_j=j/m\). Then
\[
C_{n,r}:=\sup_{0<|Df|(0,1)<\infty}
\frac{\|K_n^r f-\int_0^1f\|_{L^1(0,1)}}{|Df|(0,1)}
=\max_{1\le j\le n}\int_0^1|F_{j,r}(x)-\theta_j|\,dx.
\tag{1}
\]
Every term is strictly positive and has a unique zero \(z_{j,r}\in(0,1)\) of \(F_{j,r}(z_{j,r})=\theta_j\). Thus it is explicitly computable as
\[
2\left[\sum_{i=0}^n(c_{j,r})_i\int_0^{z_{j,r}}b_i(x)\,dx-\theta_jz_{j,r}\right].
\tag{2}
\]
At least one grid-aligned one-jump function attains (1).

There is also a sharp long-iteration result, including the exact asymptotic coefficient and the eventual location of maximizing grid steps. Write \(\lambda_n=n/(n+1)\), \(h_i=i-n/2\), and let \(w\) be the unique rational vector satisfying
\[
M^{\mathsf T}w=\lambda_n w,\qquad \sum_{i=0}^n w_i h_i=1.
\]
Then \(w_{n-i}=-w_i\), \(w_i<0\) for \(i<n/2\), \(w_i>0\) for \(i>n/2\), and \(w_{n/2}=0\) when \(n\) is even. Define the positive rational number
\[
A_n=\frac{n}{4\lambda_n}\max_{1\le j\le n}\left|\sum_{i<j}w_i\right|.
\tag{3}
\]
For every fixed \(n\ge2\), with \(\mu_n=n(n-1)/(n+1)^2<\lambda_n\),
\[
C_{n,r}=A_n\lambda_n^r+O_n(\mu_n^{r-1})\qquad(r\to\infty).
\tag{4}
\]
For \(n=1\), \(C_{1,r}=2^{-r-1}\) exactly. For all sufficiently large \(r\) (depending on \(n\)), the maximizing grid indices in (1) are exactly \(j=(n+1)/2\) when \(n\) is odd, or the two indices \(j=n/2,n/2+1\) when \(n\) is even. Hence the worst single-jump inputs eventually sit at the central averaging-cell boundary or its reflected pair. Examples are
\[
A_1=\frac12,\quad A_2=\frac38,\quad A_3=\frac{17}{42},\quad A_4=\frac{115}{304},\quad A_5=\frac{413}{1060}.
\]
The finite-iterate formula (1), not a claimed central maximizer at every finite \(r\), is the exact result at arbitrary iteration counts.

## Assumptions and scope
Use the standard unweighted operator
\[
(K_nf)(x)=m\sum_{j=0}^n b_j(x)\int_{I_j}f(t)\,dt.
\]
Inputs are real distributional \(BV(0,1)\) equivalence classes, and \(|Df|(0,1)\) is their full interior total variation. Endpoint values of a representative are immaterial. The degree \(n\) is fixed before sending \(r\) to infinity; no estimate uniform in \(n\) is asserted. Formula (2) uses the unique real root inside \((0,1)\); beta incomplete integrals or rational-polynomial integration evaluate its terms without sampled approximations.

## Proof
**1. Reduction to a finite stochastic matrix.** For \(f\in L^1(0,1)\), its cell-mean vector is \(a_i=m\int_{I_i}f\). The Bernstein-coefficient vector of \(K_nf\) is \(a\), while the cell means of \(K_nf\) are \(Ma\). Therefore \(K_n^rf=\sum_i(M^{r-1}a)_i b_i\). Each row of \(M\) sums to one, since \(\sum_jb_j=1\); each column sums to one because \(\int_0^1b_j=1/m\). Consequently the Lebesgue mean is invariant. Reflection \(i\mapsto n-i\) commutes with \(M\).

**2. Sharp finite-grid formula.** Every real distributional \(BV\) function has, modulo constants and null sets, a finite signed derivative-measure representation by one-jump indicators \(s_\theta=\mathbf1_{(0,\theta)}\) with total measure variation \(|Df|\). Linearity, Minkowski's inequality, and mean invariance imply that the norm in (1) is \(\sup_{0<\theta<1}\|K_n^rs_\theta-\theta\|_1\). In each averaging cell the vector of the \(m\) input-cell means of \(s_\theta\) is affine in \(\theta\). Hence \(\theta\mapsto\|K_n^rs_\theta-\theta\|_1\) is convex on each closed cell, so its maximum lies at an endpoint of some cell. The outer endpoints give zero; the remaining endpoints give precisely (1). Conversely, any maximizing step has derivative variation exactly one and attains (1).

**3. A unique crossing and exact integration.** The vector \(v_j\) is weakly decreasing and nonconstant. For every \(x\in(0,1)\), binomial laws \(\mathrm{Bin}(n,x)\) strictly increase stochastically with \(x\), so \(x\mapsto\sum_i a_i b_i(x)\) is strictly decreasing for every nonconstant decreasing vector \(a\). The corresponding cell means are strictly decreasing too. Induction therefore makes each \(F_{j,r}\) strictly decreasing. Its mean is \(\theta_j\), hence \(F_{j,r}(0)>\theta_j>F_{j,r}(1)\), yielding the unique zero and the positive-area identity (2).

**4. Spectrum and leading mode.** On polynomials of degree at most \(n\), \(K_n\) is degree preserving with diagonal entries \(\rho_k=(n)_k/(n+1)^k\), \(0\le k\le n\), in the monomial basis; this follows by expanding the mean of \(t^k\) on cell \(i\) into a degree-\(k\) polynomial in \(i\), and taking its binomial expectation. These entries are positive and strictly decrease from \(\rho_0=1\). The finite nonzero spectrum of \(K_n\) equals that of \(M\), so \(M\) is diagonalizable with simple eigenvalues \(1,\lambda_n,\mu_n,\ldots\). Direct calculation gives \(Mh=\lambda_nh\). The normalized left eigenvector \(w\) exists, is unique and rational, since \(M\) and \(\lambda_n\) are rational. Reflection and simplicity force \(w_{n-i}=-w_i\).

**5. Strict sign of the left mode.** Let \(J=\{0,\ldots,\lfloor(n-1)/2\rfloor\}\). On antisymmetric vectors under reflection, the restriction of \(M\) to the left-half coordinates has matrix \(N_{ij}=M_{ij}-M_{i,n-j}\), \(i,j\in J\). For \(x<1/2\) and \(j<n/2\), \(b_j(x)>b_{n-j}(x)\); thus every entry of \(N\) is strictly positive. The restriction \(-h|_J\) is a strictly positive right eigenvector for \(\lambda_n\). Perron–Frobenius therefore makes \(\lambda_n\) the simple dominant eigenvalue of \(N\) and gives a strictly negative left eigenvector on \(J\), once normalized by \(w\cdot h=1\). Extending antisymmetrically yields the asserted signs of \(w\), including a zero center only when present.

**6. Sharp coefficient and eventual centrality.** Because \(M\) has distinct eigenvalues, its spectral projection onto the \(\lambda_n\)-line is \(h w^{\mathsf T}\), with \(w\cdot h=1\). Uniformly over the finitely many \(j\),
\[
M^{r-1}v_j=\theta_j\mathbf1+\lambda_n^{r-1}h\sum_{i<j}w_i+O_n(\mu_n^{r-1}).
\]
Now \(\sum_i h_i b_i(x)=n(x-1/2)\) and \(\int_0^1|x-1/2|\,dx=1/4\). The reverse triangle inequality gives, uniformly in \(j\),
\[
\|F_{j,r}-\theta_j\|_1=\frac n4\lambda_n^{r-1}\left|\sum_{i<j}w_i\right|+O_n(\mu_n^{r-1}).
\]
The strictly negative left-half entries and strictly positive right-half entries make the magnitudes of partial sums increase strictly to the center and then decrease strictly, with a two-way tie when a central zero is present. Since \(\mu_n/\lambda_n<1\), for all sufficiently large \(r\) only those central grid indices maximize. Equations (3)–(4) follow. In degree one there are only the constant and affine eigenmodes, giving the stated exact identity.

## Verification
`checker.py` reconstructs every entry of \(M\) in exact rational arithmetic, verifies doubly stochasticity, reflection, the affine eigenmode and the rational normalized left eigenvector for degrees \(1\) through \(8\). It verifies exact parity/strict-sign identities and the five displayed \(A_n\); independently evaluates the finite-grid step roots by monotone bisection and integrates their Bernstein polynomials for iterations \(r=1,2,3,5,8,13,42\). Its long-iteration comparisons confirm the spectral coefficient numerically. Executing `python checker.py` in the delivered package produced a successful run. These finite checks corroborate, but do not replace, the proof for all degrees and all iterations.

## Relationship to prior work
Cooper and Waldron (technical report, October 22, 1999; journal 2000), Section 7, determine the classical Kantorovich operator's individual eigenvalues and eigenpolynomials. That establishes the spectral ingredients but does not state the sharp \(BV\)-to-\(L^1\) distance from the invariant mean, its exact all-power finite-grid reduction or the rational asymptotic norming constant and central extremizing steps. Kivinukk and Metsmägi (2011) estimate variation of \(K_nf-f\) for smooth data; their seminorm and approximation target differ. Bartoszek and Bartoszek (2024 preprint; journal 2025) study qualitative convergence of generalized Kantorovich iterates, rather than the present sharp classical-operator norm. Existing spectral and contraction estimates provide context but do not, as stated, imply the all-iteration sharp result without the step reduction and positive odd-block argument.

## Limitations
No all-finite-iteration central-maximizer theorem is asserted; (1) deliberately retains the finite maximization. The cutoff after which central grid steps are exactly sharp is existential for each \(n\), not accompanied by a uniform effective bound. Other function norms, weighted Kantorovich variants, complex \(BV\), and joint degree-iteration limits are outside scope. The literature comparison cannot exclude unindexed equivalent norm formulas. No independent mathematical assessment is claimed.

## References
1. S. Cooper and S. Waldron, *The eigenstructure of the Bernstein operator*, technical report dated 1999-10-22; *Journal of Approximation Theory* 105 (2000), 133–165, especially §7. DOI: https://doi.org/10.1006/jath.2000.3464 . Accessible report: https://www.academia.edu/27420260/The_Eigenstructure_of_the_Bernstein_Operator .
2. A. Kivinukk and T. Metsmägi, *Approximation in variation by the Kantorovich operators*, *Proceedings of the Estonian Academy of Sciences* 60 (2011), 201–209. https://doi.org/10.3176/proc.2011.4.01 .
3. K. Bartoszek and W. Bartoszek, *Asymptotic dynamics of generalized Kantorovich operators*, preprint https://arxiv.org/abs/2403.07633 (2024), *Results in Mathematics* 80 (2025), article 39. https://doi.org/10.1007/s00025-024-02348-4 .
