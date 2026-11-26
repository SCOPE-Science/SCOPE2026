# Exact Hahn-mode variance spectrum for birth-labeled leaves in uniform recursive trees

## Finding
For every integer \(n\ge3\), take a uniformly random recursive tree on labels \(1,\ldots,n\), with root 1 and independent uniform attachment of each vertex to a smaller label. Let \(L_i\) indicate that vertex \(i\) has no children at size \(n\). Set \(N=n-1\), \(X_x=L_{x+1}\) for \(1\le x\le N-1\), and let \(\Sigma_N\) be the covariance matrix of \((X_1,\ldots,X_{N-1})\). Define the positive diagonal matrix \(D_N\) by
\[
(D_N)_{xx}=\frac{x(N-x)}{N^2}.
\]
The **normalized leaf covariance** \(D_N^{-1/2}\Sigma_ND_N^{-1/2}\) has the exact, simple eigenvalues
\[
\boxed{\lambda_r=\frac{N}{N-1}\left(1-\frac{1}{r(r+1)}\right),\qquad 1\le r\le N-1.}
\]
The corresponding generalized eigenvectors of \(\Sigma_N p=\lambda D_Np\) are uniquely determined, up to scale, by being polynomials in \(x\) of degrees \(r-1\), mutually orthogonal for the discrete weights \(x(N-x)\). In particular, for **every** real deterministic weight vector \(w=(w_1,\ldots,w_{N-1})\), the sharp variance bounds are
\[
\boxed{\frac{N}{2(N-1)}\sum_{x=1}^{N-1}\frac{x(N-x)}{N^2}w_x^2
\ \le\ \operatorname{Var}\left(\sum_{x=1}^{N-1}w_xX_x\right)
\ \le\ \frac{N}{N-1}\left(1-\frac{1}{N(N-1)}\right)
\sum_{x=1}^{N-1}\frac{x(N-x)}{N^2}w_x^2.}
\]
Both constants are attained. The lower equality direction is exactly the constant-weight vector. For \(N\ge3\), the upper equality direction is the unique degree-\(N-2\) weighted-orthogonal polynomial on \(1,\ldots,N-1\). For \(N=2\), both extremal modes coincide. These inequalities compare any birth-label-weighted leaf count with the variance it would have if the leaf indicators were independent with their true individual marginals.

For a continuous real \(f\) on \([0,1]\), the exact finite result also yields
\[
\lim_{N\to\infty}\frac1N\operatorname{Var}\left(\sum_{x=1}^{N-1}f(x/N)X_x\right)=
\int_0^1t(1-t)f(t)^2\,dt-\int_0^1\!\int_0^1[\min(s,t)-st]f(s)f(t)\,ds\,dt.
\]
The limiting quadratic form lies sharply between one half and one times \(\int_0^1 t(1-t)f(t)^2\,dt\), with the lower bound attained by constants. Its orthogonal modes are shifted Jacobi polynomials with parameters \((1,1)\), and mode \(r\) retains exactly the fraction \(1-1/[r(r+1)]\) of its independent-indicator variance. No central limit theorem is claimed.

## Assumptions and scope
The tree is rooted, labels strictly increase down each edge, and the parent of every \(j\in\{2,\ldots,n\}\) is chosen independently and uniformly from \(\{1,\ldots,j-1\}\). The root and final birth are deterministic nonleaf and leaf, respectively, so the covariance concerns the \(n-2\) nonconstant indicators \(L_2,\ldots,L_{n-1}\). All formulas are finite, exact and valid for \(n\ge3\); no large-tree approximation is used in the eigenvalue statement. Weighted variances assume deterministic real weights, without positivity restrictions.

## Proof
**1. Covariance from independent attachments.** For \(2\le i<n\), vertex \(i\) is a final leaf exactly when no later birth chooses it as parent. Independent parent decisions and telescoping products give
\[
\Pr(L_i=1)=\prod_{j=i+1}^n\frac{j-2}{j-1}=\frac{i-1}{n-1}.
\]
For \(2\le i<j<n\), the later births through \(j\) avoid \(i\); the births after \(j\) must avoid both \(i\) and \(j\). Therefore
\[
\Pr(L_i=L_j=1)=\prod_{t=i+1}^{j}\frac{t-2}{t-1}\prod_{t=j+1}^{n}\frac{t-3}{t-1}=\frac{(i-1)(j-2)}{(n-1)(n-2)}.
\]
Consequently, writing \(x=i-1\) and \(y=j-1\),
\[
(\Sigma_N)_{xy}=\begin{cases}
\dfrac{x(N-x)}{N^2},&x=y,\\[3pt]
-\dfrac{\min(x,y)[N-\max(x,y)]}{N^2(N-1)},&x\ne y.
\end{cases}
\]
**2. Dirichlet Green-kernel factorization.** On interior lattice sites \(1,\ldots,N-1\) define the Dirichlet path Green matrix
\[
H_{xy}=\frac{\min(x,y)[N-\max(x,y)]}{N}.
\]
The second-difference operator \((\mathcal Af)_x=2f_x-f_{x-1}-f_{x+1}\), with \(f_0=f_N=0\), satisfies \(\mathcal AH=I\). Direct comparison of off-diagonal and diagonal entries yields
\[
\Sigma_N=\frac{N}{N-1}D_N-\frac{1}{N(N-1)}H.
\]
**3. A discrete polynomial Sturm--Liouville operator.** Put \(a_x=x(N-x)\), including \(a_0=a_N=0\), and define
\[
(\mathcal Bp)_x=2a_xp_x-a_{x-1}p_{x-1}-a_{x+1}p_{x+1}.
\]
For the inner product \(\langle p,q\rangle_a=\sum_{x=1}^{N-1}a_xp_xq_x\), the operator \(\mathcal B\) is selfadjoint: \(\langle p,\mathcal Bq\rangle_a=\langle ap,\mathcal A(aq)\rangle=\langle\mathcal Bp,q\rangle_a\). When \(p(x)\) is a polynomial of degree \(d\le N-2\), the product \(a_xp(x)\) is a degree-\(d+2\) polynomial with negative leading coefficient. Taking the negative second difference shows \(\mathcal Bp\) has degree at most \(d\), with leading coefficient \((d+1)(d+2)\) times that of \(p\). Thus the nested polynomial subspaces are invariant. On the \((N-1)\)-dimensional interior grid these have dimensions \(1,\ldots,N-1\), so the selfadjoint matrix has distinct eigenvalues \(r(r+1)\), \(1\le r\le N-1\), with unique eigenpolynomials of degrees \(r-1\). Their orthogonality follows from selfadjointness.

**4. Transfer to covariance and sharp constants.** If \(\mathcal Bp=r(r+1)p\), then \(\mathcal A(D_Np)=r(r+1)p/N^2\). Since \(\mathcal AH=I\),
\[
\frac{H}{N(N-1)}p=\frac{N}{(N-1)r(r+1)}D_Np.
\]
The covariance factorization therefore gives \(\Sigma_Np=\lambda_rD_Np\) with the displayed \(\lambda_r\). Because \(D_N\) is strictly positive, these generalized eigenvalues are precisely the ordinary eigenvalues of \(D_N^{-1/2}\Sigma_ND_N^{-1/2}\). They are positive and strictly increasing in \(r\). Expanding any weight vector in the \(D_N\)-orthonormal eigenpolynomial basis gives the variance identity \(\operatorname{Var}(\sum_xw_xX_x)=\sum_r\lambda_r|\langle w,p_r\rangle_{D_N}|^2\), and hence both sharp bounds and equality conditions.

**5. Continuum limit.** Take \(w_x=f(x/N)\). The diagonal term divided by \(N\) converges by Riemann summation to \(\int_0^1t(1-t)f(t)^2dt\). The off-diagonal Green term divided by \(N\) converges to the stated double integral with kernel \(\min(s,t)-st\). The finite sharp bounds pass to the limit. For the mode description, the integral Green operator is the inverse of the Dirichlet second derivative. The generalized equation for its kernel and the weight \(t(1-t)\) becomes \(-[t(1-t)p(t)]''=r(r+1)p(t)\), whose polynomial solutions are the shifted Jacobi family with parameters \((1,1)\). Completeness follows from density of polynomials in the weighted \(L^2\) space, and the same variance factors follow. All boundary terms vanish because \(t(1-t)=0\) at both endpoints.

## Verification
Execute `python3 verify.py` from this package directory. The standard-library verifier enumerates every recursive parent array for \(3\le n\le8\), independently recomputes the marginal and pairwise leaf probabilities and their covariances as exact rationals, and checks the polynomial eigen-equations and Green-kernel transfer through \(N=15\) by exact weighted Gram--Schmidt. The recorded execution produced `VERIFY_OK assertions= 2617 recursive_trees_through_n=8 polynomial_spectra_through_N=15`. The unrestricted theorem is proved analytically above; the finite checks serve as independently implemented arithmetic checks of the formulas, not as extrapolation.

## Relationship to prior work
Classical work on random recursive-tree leaves and outdegree counts establishes aggregate distributions and Gaussian limits, including Janson (2004/2005), Zhang (2015), and Altok--Işlak (2017). Lyon--Mahmoud (2020), Section 5.1, supplies an exact **general** two-leaf cross-moment formula for arbitrary independent attachment probabilities; its specialization already covers the elementary covariance entries in step 1, which are **not asserted novel**. A separate established birth-label inclusion formula likewise provides these entries. The contribution assessed here is the exact all-mode generalized covariance spectrum, identification of its discrete orthogonal-polynomial eigenvectors, and sharp uniform-in-weight variance envelope. The reviewed related primary text reports leaf covariance and aggregate limits but does not evaluate those eigenvalues or the optimizing weight directions. Such a spectral refinement is not implied as an already-stated theorem merely by a general covariance formula; its proof requires the discrete Green-kernel and polynomial operator analysis above.

## Limitations
The theorem concerns uniform recursive attachment only; for nonuniform attachment the Green-kernel factorization and polynomial spectrum need not persist. The mode-weighted comparison is about **variance**, not stochastic ordering or independence; the negative pair covariances do not imply that all leaf indicators are independent. The joint leaf law and general covariance mechanism were known prior inputs. An inaccessible plausible earlier full text could contain an implicit or explicit spectral result; independent historical-priority review is still needed. No independent scientific verification was performed. The continuum statement is a second-moment limit, not a functional central limit theorem.

## References
1. S. Janson, *Asymptotic degree distribution in random recursive trees*, Random Structures & Algorithms **26** (2005), 69--83; first published online 16 November 2004. DOI: `10.1002/rsa.20046`.
2. Y. Zhang, *On the number of leaves in a random recursive tree*, Brazilian Journal of Probability and Statistics **29** (2015), 897--908. DOI: `10.1214/14-BJPS252`.
3. S. Altok and Ü. Işlak, *On leaf related statistics in recursive tree models*, Statistics & Probability Letters **121** (2017), 61--69. DOI: `10.1016/j.spl.2016.10.007`.
4. M. R. Lyon and H. M. Mahmoud, *Trees grown under young-age preferential attachment*, Journal of Applied Probability **57** (2020), 911--927. DOI: `10.1017/jpr.2020.49`, especially Section 5.
