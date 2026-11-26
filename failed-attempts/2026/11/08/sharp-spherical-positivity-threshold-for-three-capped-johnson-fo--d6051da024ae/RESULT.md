# Sharp spherical positivity threshold for three-capped Johnson four-subset metrics

## Finding
For every integer \(n\ge 8\), let \(X_n=\binom{[n]}4\), and give it the three-capped Johnson distance
\[
 d_n(S,T)=\min\{4-|S\cap T|,3\}.
\]
For real \(p>0\), let \(D_p\) be the matrix with entries \(d_n(S,T)^p\). Define \(\beta_n\) to be the unique root in \((0,1)\) of
\[
 (n-10)-3(n-8)2^{\beta_n}+(2n-15)3^{\beta_n}=0.
\]
Then \(D_p\) is conditionally negative semidefinite precisely for \(0<p\le\beta_n\), and strictly so precisely for \(0<p<\beta_n\). At \(p=\beta_n\), its nullspace on the zero-sum subspace is exactly the third Johnson harmonic component \(E_3\), of dimension
\[
 m_3=\binom n3-\binom n2.
\]
The minimum Euclidean dimension of the powered metric with distances \(d_n(S,T)^{p/2}\) is \(\binom n4-1\) for \(0<p<\beta_n\) and \(\binom n4-1-m_3\) at \(p=\beta_n\). Furthermore,
\[
 \beta_8=\frac{\log2}{\log3},\qquad
 \lim_{n\to\infty}n\beta_n=\frac1{\log(9/8)}.
\]
The nonconstant spherical spectrum has a unique maximal eigenvalue for each \(0<p\le1\), always on \(E_3\); its explicit value is the left-hand side of the defining equation with \(\beta_n\) replaced by \(p\). In contrast, the untruncated Johnson distance is half the Hamming distance of binary incidence vectors and therefore has \(1\)-negative type: each coordinate cut distance is conditionally negative semidefinite. Thus capping only the disjoint-pair distance destroys \(1\)-negative type at every \(n\ge8\), and the sharp exponent actually tends to zero.

## Assumptions and scope
The Johnson space consists of all four-element subsets of \([n]\); the assumption \(n\ge8\) ensures that all four nonzero intersection-distance classes can occur. The ordinary Johnson distance is \(4-|S\cap T|\); truncation at three preserves the triangle inequality because \(\min\{a+b,3\}\le\min\{a,3\}+\min\{b,3\}\) for nonnegative \(a,b\). Conditional negative semidefiniteness means \(\sum_{S,T}c_Sc_Td_n(S,T)^p\le0\) for every real vector \(c\) with \(\sum_Sc_S=0\). Strict means strict inequality for each nonzero such vector.

Let \(A_i\) be the \(0\)-\(1\) matrix of the Johnson distance-\(i\) relation. Its orthogonal spherical components are \(E_j\), for \(0\le j\le4\), where \(E_0\) is the constant space and \(\dim E_j=\binom nj-\binom n{j-1}\) (take \(\binom n{-1}=0\)). More concretely, if \(U_j\) is the span of the incidence functions \(S\mapsto\mathbf1_{\{T\subseteq S\}}\) with \(|T|\le j\), then \(E_j=U_j\cap U_{j-1}^{\perp}\) for \(j\ge1\).

## Proof
**Johnson spherical diagonalization.** Let \(\theta_j\) and \(\nu_j\) be the eigenvalues of \(A_1\) and \(A_2\) on \(E_j\). The Johnson-scheme adjacency formula and its distance-two recurrence give
\[
 \theta_j=(4-j)(n-4-j)-j,\qquad
 \nu_j=\frac{\theta_j^2-(n-2)\theta_j-4(n-4)}4.
\]
Indeed, the graph has valency \(4(n-4)\), each adjacent pair has \(n-2\) common neighbors, and each distance-two pair has four common neighbors, whence \(A_1^2=4(n-4)I+(n-2)A_1+4A_2\). The resulting nonconstant spectra are
\[
\begin{array}{c|cc}
 j&\theta_j&\nu_j\\\hline
1&3n-16&3(n-8)(n-5)/2\\
2&2(n-7)&(n^2-21n+92)/2\\
3&n-10&-3(n-8)\\
4&-4&6
\end{array}.
\]
Set \(J\) to be the all-ones matrix. Since \(J=I+A_1+A_2+A_3+A_4\),
\[
 D_p=3^p(J-I)+(1-3^p)A_1+(2^p-3^p)A_2.
\]
Consequently on \(E_j\), for \(j\ge1\), the distance-power eigenvalue is
\[
 \lambda_j(p)=-3^p+(1-3^p)\theta_j+(2^p-3^p)\nu_j.
\]
In particular \(\lambda_3(p)=(n-10)-3(n-8)2^p+(2n-15)3^p\).

**Unique critical spherical degree.** For \(0<p\le1\), put \(t=(3^p-2^p)/(3^p-1)\). Concavity of \(u\mapsto u^p\) yields \(t\le1/2\); the inequality \(2\cdot3^p-3\cdot2^p+1>0\) gives \(t>1/3\), because its derivative is positive for \(p\ge0\) by \(9>8\). Write \(L_j=\theta_j+t\nu_j\). Direct subtraction gives
\[
\begin{aligned}
L_1-L_3&=\frac{n-3}{2}\bigl(4+3(n-8)t\bigr)>0,\\
L_2-L_3&=\frac{n-4}{2}\bigl(2+(n-11)t\bigr)>0,\\
L_4-L_3&=(n-6)(3t-1)>0.
\end{aligned}
\]
For the middle inequality, when \(8\le n<11\) use \(t\le1/2\); otherwise both terms are nonnegative. Since \(\lambda_j=-3^p-(3^p-1)L_j\), these differences prove \(\lambda_j(p)<\lambda_3(p)\) for every \(j\ne3\) and every \(0<p\le1\).

**Threshold and excluded exponents.** One has \(\lambda_3(0)=-1\), \(\lambda_3(1)=n-7>0\), and
\[
 \lambda_3'(p)=(2n-15)3^p\log3-3(n-8)2^p\log2>0
\]
for \(p\ge0\): write \(2n-15=2(n-8)+1\) and use \(2\log3>3\log2\). Hence there is exactly one root in \((0,1)\); all nonconstant eigenvalues are negative below it, only \(E_3\) is zero at it, and \(\lambda_3\) is positive above it through \(p=1\). The standard interval property for negative type excludes every \(p>1\): if a metric has \(p\)-negative type it also has \(q\)-negative type for every \(0<q<p\), whereas this metric fails at \(q=1\).

**Embedding dimension and asymptotics.** The centered Gram matrix of squared distances \(D_p\) is \(B_p=-\tfrac12HD_pH\), where \(H=I-|X_n|^{-1}J\). For \(p\le\beta_n\), this is positive semidefinite with rank equal to the number of strictly negative nonconstant eigenvalues of \(D_p\). The asserted dimensions follow from the classical Euclidean distance-matrix characterization, and are minimal by Gram rank. Finally, for each fixed real \(c>0\),
\[
 \lambda_3(c/n)=-1+c\log(9/8)+O_c(n^{-1}).
\]
Strict monotonicity and the unique root imply \(n\beta_n\to1/\log(9/8)\). Setting \(n=8\) in the exact equation gives \(3^{\beta_8}=2\).

## Verification
Run `python3 verify_johnson_cap3.py` using Python 3 and NumPy. The program constructs the distance-power matrix directly from all four-subsets in dimensions \(n=8,9,10\), numerically diagonalizes it at three exponents including the computed critical exponent, compares **every** eigenvalue with the derived spherical eigenvalues with their exact multiplicities, checks the uniqueness of the maximal nonconstant sector, and checks the asymptotic scaling at \(n=100,1000,10000\). The concluding marker is `JOHNSON_CAP3_DISTANCE_CHECKS_PASS`. The all-dimensional proof above does not depend on these finite numerical experiments.

## Relationship to prior work
Krebs and Shaheen (2008) derive the Eberlein/Johnson spherical eigenvalues in a finite Gelfand-pair setting. Their result supplies the established harmonic diagonalization, but does not determine the negative-type threshold for the capped distance, the decisive third spherical sector, or the endpoint Euclidean rank defect. Sánchez (2011), Corollary 2.4, gives a general determinant/inverse-matrix characterization of supremal negative type and the interval property, not this explicit all-dimensional threshold or its sharp asymptotics. Earlier Deza–Maehara (1990) results concern truncated-distance embeddings, prominently two-distance graph transforms; full comparison with that source remains limited by unavailable full text. The present metric has three distinct positive distance values and is not identical to an arbitrary graph's two-distance truncation. Identifying each four-subset with its binary incidence vector makes the present metric half the six-capped Hamming metric restricted to the weight-four slice. Known power thresholds for the entire Boolean cube give only a one-way lower bound for the subset threshold, not the claimed equality or nullspace classification.

## Limitations
The theorem is confined to four-subsets with a cap at three and \(n\ge8\). It does not classify caps on higher Johnson layers, all graph metrics, other snowflake embeddings, or nonlinear Banach-space distortions. The exact root generally has no asserted elementary closed form. Literature comparison cannot exclude unlocated specialized work on capped Johnson-scheme kernels or an implicit old classification; the full original Deza–Maehara (1990) text was not examined, so independent historical-priority review is warranted. Numerical eigenvalue comparisons have finite scope and rounding error; infinite-dimensional statements rely on the preceding algebraic proof.

## References
1. M. Krebs and A. Shaheen, *On the spectra of Johnson graphs*, Electronic Journal of Linear Algebra **17** (2008), 154–167, DOI: `10.13001/1081-3810.1256`.
2. S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451v1, public preprint dated 2011-08-02; subsequently Journal of Mathematical Analysis and Applications (2012).
3. M. Deza and H. Maehara, *Metric transforms and Euclidean embeddings*, Transactions of the American Mathematical Society **317** (1990), 661–671, DOI: `10.1090/S0002-9947-1990-0974513-6` (full text not materially inspected).
