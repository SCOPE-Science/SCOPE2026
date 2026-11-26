# Universal cross-type correlations in critical decomposable branching with immigration

## Finding

Consider a critical lower-triangular \(p\)-type Galton--Watson process with immigration, begun from zero, where \(p\ge1\) is fixed. Under the assumptions below, write \(X_{n,i}\) for the type-\(i\) population at generation \(n\). For every \(1\le i,j\le p\),

\[
\operatorname{Cov}(X_{n,i},X_{n,j})=
\frac{b_1v\,c_i c_j}{(i-1)!(j-1)!(i+j-1)(i+j)}\,n^{i+j}
+O(n^{i+j-1}),\qquad n\to\infty.
\]

Thus the Pearson correlations converge with error \(O(n^{-1})\) to the *universal* numbers

\[
R_{ij}=\frac{\sqrt{(2i-1)(2i)(2j-1)(2j)}}{(i+j-1)(i+j)},
\]

independent of immigration intensity, reproductive variance and all nonzero offspring-transfer rates. Every finite matrix \(R^{(p)}=(R_{ij})_{1\le i,j\le p}\) is strictly positive definite and has the explicit determinant

\[
\det R^{(p)}=\prod_{r=0}^{p-1}\frac{(r!)^2((r+1)!)^2}{(2r)!(2r+1)!}>0.
\]

For indices \(i,j\) that both increase through a family of such systems and satisfy \(i/j\to\theta\in(0,\infty)\), the universal correlation constants have the further limit \(R_{ij}\to4\theta/(1+\theta)^2\). No claim of a simultaneous increasing-number-of-types population limit is made.

## Assumptions and scope

There are independent, identically distributed reproduction vectors for each parent type, and independent identically distributed immigration vectors in each generation, independent across generations and of reproduction. All their coordinates have finite second moments. The population starts at \(X_0=0\). The mean offspring matrix \(A=(a_{ij})_{1\le i,j\le p}\), with row \(i\) specifying children of type \(i\) and column \(j\) a parent of type \(j\), is lower triangular, \(a_{ii}=1\), and \(a_{i+1,i}>0\) for \(1\le i<p\). The mean immigration vector is \(b\), with \(b_1>0\). Let \(v>0\) be the variance of the number of type-one children produced by one type-one parent. Define \(c_1=1\) and \(c_i=\prod_{r=1}^{i-1}a_{r+1,r}\) for \(i\ge2\). The assertion is for fixed \(p\), fixed reproduction and immigration laws, and \(n\to\infty\).

## Proof

Set \(C=A-I\), a strictly lower-triangular nilpotent matrix. The innovation vector

\[
M_k=X_k-AX_{k-1}-b
\]

is a square-integrable martingale difference. Consequently,

\[
X_n-\mathbb EX_n=\sum_{k=1}^n A^{n-k}M_k,
\quad\operatorname{Cov}(X_{n,i},X_{n,j})
=\sum_{k=1}^n\sum_{s\le i,\,t\le j}(A^{n-k})_{is}(A^{n-k})_{jt}\,\mathbb E[M_{k,s}M_{k,t}].
\]

By the binomial theorem for nilpotent matrices, \(A^h=\sum_{q=0}^{p-1}\binom hq C^q\). Hence \((A^h)_{is}=O((h+1)^{i-s})\) for \(s\le i\), while the unique length-\(i-1\) ascending path from type one gives

\[
(A^h)_{i1}=c_i\binom{h}{i-1}+O((h+1)^{i-2})\quad(i\ge2),
\qquad (A^h)_{11}=1.
\]

The mean recursion \(\mathbb EX_k=A\mathbb EX_{k-1}+b\) gives \(\mathbb E X_{k,s}=O((k+1)^s)\) and exactly \(\mathbb E X_{k,1}=b_1k\). Since a parent of type \(r\) cannot produce types below \(r\), conditional offspring covariance, immigration covariance and finite second moments imply

\[
\mathbb E[M_{k,s}M_{k,t}]=O(k^{\min(s,t)}).
\]

For \(s=t=1\), this expression is exact:

\[
\mathbb E[M_{k,1}^2]=vb_1(k-1)+\sigma_1^2,
\]

where \(\sigma_1^2\) is type-one immigration variance. A term indexed by \((s,t)\) in the covariance double sum is \(O(n^{i+j+1-\max(s,t)})\). Therefore every term except \((s,t)=(1,1)\) is \(O(n^{i+j-1})\), and the leading term is

\[
\frac{vb_1c_ic_j}{(i-1)!(j-1)!}\sum_{k=1}^n(k-1)(n-k)^{i+j-2}
+O(n^{i+j-1})
\]

when \(i+j>2\). For \(i=j=1\), use the exact constant matrix coefficients instead. Standard polynomial power-sum asymptotics give

\[
\sum_{k=1}^n(k-1)(n-k)^{i+j-2}=n^{i+j}\int_0^1t(1-t)^{i+j-2}\,dt+O(n^{i+j-1})
=\frac{n^{i+j}}{(i+j-1)(i+j)}+O(n^{i+j-1}).
\]

This proves the covariance formula in all cases. In particular each variance has a strictly positive leading constant. Dividing by the two standard deviations proves the displayed correlations and the \(O(n^{-1})\) error.

For positive definiteness, index rows by \(r=i-1\) and define the moment matrix

\[
H_{rs}=\frac1{(r+s+1)(r+s+2)}=\int_0^1x^{r+s}(1-x)\,dx.
\]

It is a positive-definite Gram matrix of the independent monomials \(1,x,\ldots,x^{p-1}\) in \(L^2([0,1],(1-x)dx)\). The correlation matrix is its positive diagonal congruence: \(R^{(p)}=\operatorname{diag}(H_{rr}^{-1/2})H\operatorname{diag}(H_{rr}^{-1/2})\). Shifted Jacobi polynomials for weight \(1-x\) have monic squared norms

\[
h_r=\frac{(r!)^2((r+1)!)^2}{(2r+1)!(2r+2)!}.
\]

Gram--Schmidt therefore gives \(\det H=\prod_{r=0}^{p-1}h_r\). Since \(H_{rr}=1/[(2r+1)(2r+2)]\), the stated determinant follows. Finally divide numerator and denominator of \(R_{ij}\) by \((i+j)^2\) and take the ratio limit to obtain \(4\theta/(1+\theta)^2\).

## Verification

The companion `check.py` executes exact-rational finite-difference checks of the highest-degree covariance coefficients for 18 fully specified, lower-triangular independent-Poisson offspring/immigration systems with one through six types, including nonzero long-range transfers and later-type immigration. It also checks the exact Gram determinant in nine dimensions. This is finite reproducibility evidence, not an exhaustive proof for arbitrary offspring laws; the universal statement is established by the martingale argument above. Execute `python3 check.py` from the extracted package.

## Relationship to prior work

Barczy and Bezdány (2026, arXiv:2611.02069v1, Theorem 3.1) establish the functional limit for these critical decomposable populations, with iterated-integral squared-Bessel coordinates; Appendix B recalls general conditional and unconditional moment recursions. Foster and Ney (1978) established earlier one-time weak limits, and Barczy, Bezdány and Pap (2023) and Barczy and Bezdány (2026) cover two- and three-type cases. The present result uses the known innovation and moment framework, but asserts explicit leading all-type *finite-population* covariance coefficients, an order-one relative-error estimate, a parameter-free correlation matrix, and its positive Jacobi-Gram determinant and deep-type ratio law. Weak convergence by itself does not imply second-moment convergence. These classical recursions can be used to derive our formulas; no novelty is claimed for their existence or for the underlying weak limit theorem.

## Limitations

The type number and all model parameters are fixed in the population limit; no uniform joint \(p,n\to\infty\) statement is proved. Offspring and immigration must have finite second moments, adjacent type transfers must be positive, and \(b_1v>0\). If the first-type variance or immigration mean vanishes, the leading covariance may degenerate. A relevant earlier Foster--Ney full text could not be inspected; possible implicit or explicit priority coverage in that source remains unresolved. The result has not undergone independent mathematical validation.

## References

1. M. Barczy and D. Bezdány, *Asymptotic behavior of some strongly critical decomposable multi-type Galton--Watson processes with immigration*, arXiv:2611.02069v1 (first posted 2026-11-01), https://arxiv.org/html/2611.02069v1.
2. J. Foster and P. Ney, *Limit laws for decomposable critical branching processes*, Z. Wahrscheinlichkeitstheorie verw. Gebiete **46** (1978), 13--43, https://doi.org/10.1007/BF00535685.
3. M. Barczy, D. Bezdány and G. Pap, *Asymptotic behaviour of critical decomposable 2-type Galton--Watson processes with immigration*, Stochastic Processes and their Applications **160** (2023), 318--350, https://arxiv.org/abs/2105.02508.
4. M. Barczy and D. Bezdány, *Asymptotic behavior of some strongly critical decomposable 3-type Galton--Watson processes with immigration*, Advances in Applied Probability (2026), https://arxiv.org/abs/2406.09852.
5. M. P. Quine, *The multi-type Galton--Watson process with immigration*, Journal of Applied Probability **7** (1970), 411--422, https://doi.org/10.2307/3211974.
