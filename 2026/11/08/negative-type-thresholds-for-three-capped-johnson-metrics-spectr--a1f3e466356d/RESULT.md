# Negative-type thresholds for three-capped Johnson metrics: spectral classification and rank-density transitions

## Finding
For integers \(k\ge4\), \(n\ge2k\), let \(\mathcal J_{n,k}\) consist of all \(k\)-subsets of \(\{1,\ldots,n\}\), equipped with the metric \(\rho(S,T)=\min\{k-|S\cap T|,3\}\). A symmetric kernel \(\rho^t\) has *negative type* when \(\sum_{S,T}c_Sc_T\rho(S,T)^t\le0\) for every real zero-sum coefficient family \(\sum_Sc_S=0\). Put \(\theta_j=(k-j)(n-k-j)-j\), \(\eta_j=(\theta_j^2-(n-2)\theta_j-k(n-k))/4\), and
\[
\lambda_j(t)=-3^t-(3^t-1)\theta_j-(3^t-2^t)\eta_j\qquad (1\le j\le k).
\]
Then \(\rho\) has negative-type exponents exactly \(0<t\le\beta_{n,k}\), where \(\beta_{n,k}\) is the smallest positive zero of the displayed \(\lambda_j\), over \(j=1,\ldots,k\). In particular \(0<\beta_{n,k}\le\log(2)/\log(3)<1\); the endpoint zero-eigenspaces determine the exact dimension of the Hilbert embedding of \(\rho^{\beta_{n,k}/2}\).

For \(n\ge4k\) the sole critical Johnson harmonic degree is \(j=k-1\). Set
\[
A=\frac{(k-1)(2n-5k+4)}2,\quad B=\frac{(k-2)(2n-5k+5)}2,\quad h=n-3k+2.
\]
The unique positive solution of \(h-A2^t+B3^t=0\) is \(\beta_{n,k}\). In this regime \(\dim_{\mathbb R}\operatorname{span}\{\Phi(S):S\in\mathcal J_{n,k}\}=\binom nk-1-\binom n{k-1}+\binom n{k-2}\) for a centered optimal Hilbert configuration \(\Phi\) with squared distances \(\rho^{\beta_{n,k}}\).

For each fixed \(k\ge4\),
\[
\lim_{n\to\infty}n\beta_{n,k}=\bigl[(k-1)\log(3/2)-\log 3\bigr]^{-1}.
\]
There is a different rank-density scaling: if \(k\to\infty\) and \(n/k\to c\in[2,\infty)\), then
\[
\lim k^2\beta_{n,k}=\frac4{\log(3/2)D(c)},\qquad D(2)=2,
\]
where, for \(c>2\),
\[
D(c)=\max_{\ell\in\mathbb Z_{\ge0}}\Bigl(c((c-2)\ell-1)+c-1-((c-2)\ell-1)^2\Bigr)>0.
\]
For \(c>2\) its optimizing degrees are \(j=k-\ell\) with \(\ell\) nearest to \((c+2)/(2(c-2))\); at integral ties two harmonic levels compete asymptotically. At \(c=2\) the maximizing index recedes into a boundary layer with \(k-j=o(k)\) but \((k-j)^2+(n-2k)(k-j)\sim2k\). Thus the sharp exponent has a discrete degree-selection transition across density ratios, not simply a fixed-degree extension of the four-subset case.

## Assumptions and scope
The set size and ambient size are integers with \(k\ge4\), \(n\ge2k\); \(t>0\) is real. Distances take the values \(0,1,2,3\). The negative-type definition quantifies over every real zero-sum family, including non-symmetric ones. Hilbert dimension refers to the affine span after centering, not to the ambient dimension of a particular constructed embedding. The asymptotic density parameter \(c\) is finite, and the case \(n\ge4k\) is a separate exact finite-parameter conclusion. A tie in the leading-order density formula does not assert an exact finite-parameter eigenvalue tie.

## Proof
**Spectral diagonalization.** Let \(A_1,A_2\) be the first two Johnson distance matrices; \(J\) denotes the all-ones matrix and \(I\) identity. Because the cap is exactly three,
\[
K_t=[\rho(S,T)^t]_{S,T}=3^t(J-I)+(1-3^t)A_1+(2^t-3^t)A_2.
\]
The Johnson graph has degree \(k(n-k)\), and an elementary two-step path count yields \(A_1^2=k(n-k)I+(n-2)A_1+4A_2\). The permutation representation of the symmetric group on \(k\)-sets decomposes into orthogonal harmonic summands indexed by \(j=0,\ldots,k\), of multiplicities \(m_j=\binom nj-\binom n{j-1}\), with \(A_1\)-eigenvalues \(\theta_j\). The preceding polynomial identity gives the \(A_2\)-eigenvalues \(\eta_j\); \(J\) acts as zero on every \(j\ge1\). This proves the \(\lambda_j(t)\) formula and its necessity and sufficiency for negative type.

**Existence and uniqueness of a first boundary.** Each \(\lambda_j(0)=-1\), so sufficiently small positive \(t\) works. The submetric on a fixed \((k-4)\)-element set plus the four-subsets of eight further elements is an isometric copy of \(\mathcal J_{8,4}\). Its \(j=3\) eigenvalue is \(3^t-2\), so no \(t>\log(2)/\log(3)\) works. By Schoenberg's integral representation of fractional positive powers, if \(K_t\) is conditionally negative semidefinite then so is \(K_s\) for every \(0<s<t\). Thus admissible exponents form an initial interval; continuity and the previous upper bound show that its endpoint is precisely the first positive zero of some \(\lambda_j\). A zero of a noncritical individual eigenvalue beyond this endpoint is not counted as a separate admissible boundary.

**High-ambient-size critical mode.** Write \(a=3^t-1\), \(b=3^t-2^t\). The function of \(\theta\) appearing in \(\lambda\) is a strictly concave quadratic, with vertex \(\theta_*=(n-2)/2-2a/b\). Since \(a/b<\log3/\log(3/2)<3\) for all \(t>0\), and \(n\ge4k\), direct substitution of the three neighboring eigenvalues gives
\[
\frac{\theta_k+\theta_{k-1}}2<\theta_*<\frac{\theta_{k-1}+\theta_{k-2}}2.
\]
Consequently \(j=k-1\) uniquely maximizes \(\lambda_j(t)\) for every \(t>0\); the other degrees cannot reach zero first. Substitution at \(j=k-1\) yields \(\lambda_{k-1}(t)=h-A2^t+B3^t\), with positive \(A,B\), \(\lambda_{k-1}(0)=-1\), and \(\lambda_{k-1}(1)=(k-3)(2n-5k+6)/2>0\). Its derivative \(-A\log2\,2^t+B\log3\,3^t\) changes sign at most once, from negative to positive, so its positive zero is unique. At that zero exactly the \(m_{k-1}\)-dimensional harmonic summand vanishes. Centering the negative-type kernel produces the real Hilbert Gram matrix \(-HK_tH/2\), of rank \(\binom nk-1-m_{k-1}\), where \(H=I-J/\binom nk\).

**Fixed-rank scaling.** Let \(n\to\infty\) with fixed \(k\). In the preceding exact root, set \(t=u/n\) and Taylor-expand \(2^t,3^t\). The result is
\[
\lambda_{k-1}(u/n)=-1+u\bigl((k-1)\log(3/2)-\log3\bigr)+O_k(n^{-1}),
\]
uniformly for bounded \(u\). The logarithmic coefficient is strictly positive for \(k\ge4\); uniqueness of the root proves the asserted limit.

**Growing-rank density.** Suppose \(k\to\infty\), \(n/k\to c\ge2\), and put \(t=u/k^2\) with bounded \(u>0\). The quadratic spectral polynomial gives, uniformly whenever \(\theta_j/k\) stays bounded,
\[
\lambda_j(u/k^2)=-1+\frac{u\log(3/2)}4\Bigl(ca+c-1-a^2\Bigr)+o(1),\qquad a=\theta_j/k.
\]
When \(|\theta_j|/k\to\infty\), the negative quadratic term dominates and those modes cannot be critical. If \(c>2\), bounded \(\theta_j/k\) forces \(j=k-\ell\) with bounded integer \(\ell\); here \(a\to(c-2)\ell-1\). Maximizing over \(\ell\) gives the formula for \(D(c)\) and convergence of the first zero. Completing the square shows that its maximizing \(\ell\) is a nonnegative integer nearest \((c+2)/(2(c-2))\), with only the usual half-integer ties.

For \(c=2\), write \(d=n-2k=o(k)\) and \(\ell=k-j\). Then \(\theta_j=\ell(d+\ell+1)-k\). The values of \(\theta_j/k\) sweep across \(1\) with mesh \(o(1)\) by choosing \(\ell=o(k)\) such that \(\ell(d+\ell+1)/k\to2\). The continuous quadratic \(2a+1-a^2\) is maximized at \(a=1\) with value two. The global quadratic upper bound rules out any larger limiting eigenvalue. These matching bounds give \(D(2)=2\). Positivity of \(D(c)\) for every \(c\ge2\) follows from the indicated attainable maxima (for \(c>2\), choose a nearest integer to the positive continuous maximizer). Finally, the sign of the maximum eigenvalue at any fixed scaled \(u\) below or above the corresponding root, combined with nested negative type, yields convergence of \(k^2\beta_{n,k}\).

## Verification
An accompanying standalone Python 3 checker recomputes Johnson eigenvalues from exact integer formulas; for \((n,k)=(8,4),(9,4),(10,5),(12,5)\) it enumerates all \(k\)-subsets and verifies \(A_1\) and \(A_2\) eigenvalue relations on explicit nonzero harmonic witnesses, without constructing a floating-point eigenvalue decomposition. It additionally locates numerical threshold roots for representative parameter pairs and compares the density scaling at \(k=100,500\). This finite checker provides error detection only; the infinite-family theorem follows from the algebraic argument above. Run with `python3 verify_johnson.py`.

## Relationship to prior work
Schoenberg established the negative-type/Hilbert-embedding criterion and fractional-power inheritance. The Johnson eigenvalues and multiplicities are classical (explicitly recalled in Chen–Ghorbani–Wong, Lemma 12); Brouwer–Cioabă–Ihringer–McGinnis study the smallest eigenvalues of individual Johnson distance relations. These ingredients do not themselves state the capped-metric negative-type threshold or the rank-density mode-selection law. A prior four-subset specialization gives the \(k=4\) case, but not the complete \(k\ge5\) family or the \(n/k\to c\) transition. Possible unpublished equivalent derivations remain an originality risk.

## Limitations
The result concerns negative type of the specific three-capped Johnson distance and ordinary real Hilbert embeddings, not optimal metric distortion for arbitrary embeddings and not general caps or arbitrary association schemes. The density-limit statement does not provide a uniform error bound in \(c\) or an exact finite-parameter mode-selection law when \(2k\le n<4k\), beyond the explicit minimum-over-eigenvalues classification. The motivating-source date is the first public arXiv version of the cited Johnson-spectral reference; it is not a priority assertion about this finding. Independent validation has not been performed.

## References
1. I. J. Schoenberg, "Metric Spaces and Positive Definite Functions," Transactions of the American Mathematical Society 44 (1938), 522–536, doi:10.2307/1989894.
2. B. F. Chen, E. Ghorbani, and K. B. Wong, "Cyclic decomposition of k-permutations and eigenvalues of the arrangement graphs," arXiv:1308.5490v1 (public August 26, 2013), especially Lemma 12 in the openly accessible paper.
3. A. E. Brouwer, S. M. Cioabă, F. Ihringer, and M. McGinnis, "The smallest eigenvalues of Hamming graphs, Johnson graphs and other distance-regular graphs with classical parameters," open manuscript (2018), Section 1.2 and Section 3.
