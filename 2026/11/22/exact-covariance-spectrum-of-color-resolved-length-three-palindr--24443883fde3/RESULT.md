# Exact covariance spectrum of color-resolved length-three palindromes in uniform circular words

## Finding
Fix an integer alphabet size \(q\ge3\) and a circular sample size \(n\ge5\). Let the circular letters \(X_1,\ldots,X_n\) be independent and uniform on \(\{1,\ldots,q\}\). For each **ordered pair of distinct letters** \((a,b)\), let \(N_{ab}\) count cyclic consecutive occurrences of the precise pattern \(aba\). The vector \(N\), indexed by the \(d=q(q-1)\) ordered pairs, has mean \(\mathbb EN=(n/q^3)\mathbf1\) and **exact**, not merely asymptotic, covariance \(\operatorname{Cov}(N)=n\Sigma_q\), where
\[
(\Sigma_q)_{(a,b),(c,e)}=\frac{\mathbf1_{(a,b)=(c,e)}}{q^3}
+\frac{2\mathbf1_{(a,b)=(e,c)}}{q^4}
+\frac{2\mathbf1_{a=c}}{q^5}-\frac5{q^6}.
\]
The entire positive spectrum is as follows (a row of multiplicity zero is omitted):

| Eigenvalue | Multiplicity | Mode |
|---|---:|---|
| \(\lambda_+=(q^2+q-1+\sqrt{(q-1)(5q-1)})/q^5\) | \(q-1\) | first mixed color-contrast mode |
| \(\lambda_{\rm sym}=(q+2)/q^4\) | \(q(q-3)/2\) | symmetric zero-row edge circulation |
| \(\lambda_0=(q^2-q+3)/q^5\) | \(1\) | constant mode |
| \(\lambda_-=(q^2+q-1-\sqrt{(q-1)(5q-1)})/q^5\) | \(q-1\) | second mixed color-contrast mode |
| \(\lambda_{\rm skew}=(q-2)/q^4\) | \((q-1)(q-2)/2\) | antisymmetric zero-row edge circulation |

For every \(q\ge4\), the five displayed eigenvalue classes are *strictly ordered as listed*. For \(q=3\), the symmetric-zero-row class is absent and the other four classes are strictly ordered. In particular, \(\Sigma_q\) is positive definite. Its exact Euclidean condition number is
\[
\kappa(\Sigma_q)=\frac{q^2+q-1+\sqrt{(q-1)(5q-1)}}{q(q-2)}
=1+\frac{3+\sqrt5}{q}+O(q^{-2}).
\]
For fixed \(q\) and \(n\to\infty\), the jointly standardized motif counts converge to \(\mathcal N_d(0,\Sigma_q)\). The fully specified quadratic calibration therefore obeys
\[
\frac1n\bigl(N-\tfrac n{q^3}\mathbf1\bigr)^{\!T}\Sigma_q^{-1}
\bigl(N-\tfrac n{q^3}\mathbf1\bigr)\ \Longrightarrow\ \chi^2_{q(q-1)}.
\]

## Assumptions and scope
All statements concern **overlapping** contiguous factors, including wrap-around, not scattered subsequences and not only *distinct* palindromes. Letters are equiprobable and independent. Every \(q\ge3\) and \(n\ge5\) is covered by the exact finite covariance. The normal and chi-square limits hold for each fixed \(q\) as \(n\) increases, without an assertion uniform in jointly growing \(q\).

## Proof
**Overlap kernel.** Write \(I_i^{ab}=\mathbf1\{X_i=a,X_{i+1}=b,X_{i+2}=a\}\) with cyclic indices. Its mean is \(q^{-3}\). For \(n\ge5\), two such triple indicators can depend only at relative cyclic offsets \(0,\pm1,\pm2\). Their respective joint probabilities at these five offsets are
\[
q^{-3}\mathbf1_{(a,b)=(c,e)},\qquad
q^{-4}\mathbf1_{(a,b)=(e,c)}\quad\text{(each of the two unit offsets)},\qquad
q^{-5}\mathbf1_{a=c}\quad\text{(each of the two double offsets)}.
\]
Subtracting \(q^{-6}\) for each of these five joint terms, multiplying by the \(n\) choices of starting point, and using independence for all remaining offsets proves the displayed covariance. This argument includes \(n=5\), where the five offsets exhaust the circle.

**Invariant decomposition.** Regard a vector as an array \((f_{ab})_{a\ne b}\). Let \(I\) be identity, \(R\) interchange \((a,b)\) with \((b,a)\), \(S_{ab,ce}=\mathbf1_{a=c}\), and \(J\) be all ones. The covariance reads \(\Sigma_q=q^{-3}I+2q^{-4}R+2q^{-5}S-5q^{-6}J\). The constant space has eigenvalue \(\lambda_0\). On the symmetric arrays with every row sum zero, \(R=1\), \(S=J=0\), so the eigenvalue is \(\lambda_{\rm sym}\); this space has dimension \(q(q-3)/2\). On skew-symmetric arrays with zero row sums, \(R=-1\), \(S=J=0\), so the eigenvalue is \(\lambda_{\rm skew}\); its dimension is \((q-1)(q-2)/2\).

The remaining subspace consists of arrays \(f_{ab}=u_a+v_b\) with \(\sum_a u_a=\sum_a v_a=0\). It has dimension \(2(q-1)\), and the action on each pair of contrasts \((u,v)\) is the matrix
\[
\begin{pmatrix}
q^{-3}+2(q-1)q^{-5} & 2q^{-4}-2q^{-5}\\
2q^{-4} & q^{-3}
\end{pmatrix}.
\]
Its two distinct roots are \(\lambda_+\) and \(\lambda_-\), each with multiplicity \(q-1\). All these invariant spaces are mutually orthogonal after resolving the symmetric standard two-copy action, and their dimensions sum to \(q(q-1)\), proving completeness and multiplicities.

**Strict order and positivity.** Set \(\Delta=\sqrt{(q-1)(5q-1)}\). For \(q\ge3\), \(\Delta>q+1\), \(\Delta>2q-4\), and \(\Delta<3q-1\): the first and last inequalities follow by squaring with respective positive differences \(4q(q-2)\) and \(4q^2\), and the middle follows directly or by squaring. The successive gaps in the stated order, after multiplication by \(q^5\), are \(\Delta-(q+1)\), \(3(q-1)\), \(\Delta-(2q-4)\), and \(3q-1-\Delta\). Thus all nonzero multiplicity classes are strictly ordered, the least eigenvalue is \((q-2)/q^4>0\), and the condition number and expansion follow.

**Limits.** For fixed \(q\), the vector of centered consecutive-pattern indicators along an infinite iid sequence is a bounded stationary \(2\)-dependent process. The standard multivariate \(m\)-dependent central limit theorem gives a centered Gaussian limit with covariance matrix \(\Sigma_q\). Replacing its nonwrapped count by the circular count changes at most the two terminal windows in each coordinate, an \(O(1)\) perturbation. This gives the stated circular multivariate CLT. Positive definiteness and the continuous mapping theorem imply the chi-square limit.

## Verification
Run `python3 checker.py` using Python 3 standard library only. The script independently enumerates all words for \((q,n)=(3,5),(3,6),(3,7),(4,5),(4,6)\), verifies every mean and exact cross-covariance as a rational number, checks both special circulation eigenspaces and all standard contrast generators, and compares spectral trace/Frobenius identities for \(q=3,4,5,6,8,12\). It returns `PASS: 532 independently indexed covariance/mean and spectral checks.` These finite tests do not substitute for the all-parameter proof or limit theorem.

## Relationship to prior work
The 2001 paper *A unified approach to word occurrence probabilities* develops a general overlap-matrix covariance framework for multiple contiguous patterns (especially Theorem 30); it supplies a more general mechanism for deriving covariance entries. Accordingly, no novelty is claimed for the existence of an overlap formula or for elementary single-pattern moments. Rubinchik and Shur (first public preprint 2015-05-29) study distinct palindromic factors and give basic expected counts, but not this all-color ordered-pattern covariance spectrum. Even-Zohar, Lakrec and Tessler (2020/2021) develop a spectral theory for **scattered-subsequence** word statistics, a different count operator. The contribution assessed here is the explicit complete finite-sample eigenstructure, strict mode ordering, positive-definite calibration and resulting joint chi-square statistic for the specified contiguous color-resolved motifs. These facts have not been located as statements of the inspected sources; this does not establish historical uniqueness.

## Limitations
A prior exact specialization in the extensive word-pattern statistics literature may exist. The 2001 general paper was accessible only in indexed passages, not as an independently read complete article; its coverage is therefore a residual priority risk. The result does not cover biased alphabets, length-four motifs, growing alphabet size in the Gaussian limit, or optimal testing power. The chi-square calibration is asymptotic, not an exact finite-sample chi-square law. No independent mathematical validation has been performed.

## References
- *A unified approach to word occurrence probabilities*. Discrete Applied Mathematics, DOI: https://doi.org/10.1016/S0166-218X(00)00195-5 (general overlap covariances, Theorem 30).
- M. Rubinchik and A. M. Shur, *The Number of Distinct Subpalindromes in Random Words* (public preprint 2015-05-29), https://arxiv.org/abs/1505.08043.
- C. Even-Zohar, T. Lakrec and R. J. Tessler, *Spectral Analysis of Word Statistics* (2020 preprint / 2021 publication), https://arxiv.org/abs/2012.00742 (scattered subsequences, not contiguous factors).
