# Constructive root-exponential approximation for compact differential Hilbert operators

## Finding

Let \(-1<\alpha<0\) and \(\beta>\alpha+2\). Set
\[
\tau=\min\{\beta-\alpha-2,-\alpha\}>0.
\]
For the differential Hilbert operator \(\mathcal H_2:A^2_\alpha(\mathbb D)\to A^2_\beta(\mathbb D)\), there are explicitly specified operators \(F_L\), for every integer \(L\ge1\), satisfying
\[
\operatorname{rank}F_L\le1+L^2,\qquad
\|\mathcal H_2-F_L\|\le C_{\alpha,\beta}\left(3^{-L}+\sqrt{L+1}\,2^{-\tau L/2}\right).
\]
Consequently, for some constants \(c_{\alpha,\beta},C'_{\alpha,\beta}>0\) and every integer \(N\ge1\),
\[
s_N(\mathcal H_2)\le C'_{\alpha,\beta}\exp(-c_{\alpha,\beta}\sqrt N).
\]
In particular \(\mathcal H_2\in S_p\) for every \(p>0\), extending the previously established range \(p\ge1\) to the complete quasi-Schatten regime. Combining this with the known compactness criterion gives, for any \(\alpha,\beta>-1\) and any \(p>0\),
\[
\mathcal H_2\in S_p(A^2_\alpha,A^2_\beta)
\quad\Longleftrightarrow\quad
-1<\alpha<0\ \text{ and }\ \beta>\alpha+2.
\]
The displayed singular-value estimate is an upper bound, with no assertion of a matching lower bound.

## Assumptions and scope

For \(\gamma>-1\), the Hilbert space \(A^2_\gamma(\mathbb D)\) consists of analytic functions with norm
\[
\|f\|_{A^2_\gamma}^2
=\frac{\gamma+1}{\pi}\int_{\mathbb D}|f(z)|^2(1-|z|^2)^\gamma\,dA(z).
\]
Its normalized monomials are \(e_k^{(\gamma)}=z^k/\sqrt{w_k(\gamma)}\), with
\[
w_k(\gamma)=\frac{\Gamma(\gamma+2)\Gamma(k+1)}{\Gamma(k+\gamma+2)}
\asymp_\gamma (k+1)^{-\gamma-1}.
\]
Initially for polynomials, let
\[
(\mathcal H_2f)(z)=\int_0^1\frac{f(t)}{(1-tz)^2}\,dt.
\]
The parameter assumptions ensure that its continuous extension is compact and Hilbert–Schmidt. The singular values \(s_N\) are counted in nonincreasing order with multiplicity, starting at \(N=1\). Throughout, implicit constants depend only on the displayed weight parameters, never on \(L,N,n,k\).

## Proof

**1. Matrix and an explicit separable approximant.** The identity
\[
(1-tz)^{-2}=\sum_{n\ge0}(n+1)t^nz^n
\]
and monomial integration yield the exact matrix
\[
b_{n,k}=\frac{n+1}{n+k+1}\sqrt{\frac{w_n(\beta)}{w_k(\alpha)}}
\qquad(n,k\ge0).
\]
This matrix is unitarily equivalent to \(\mathcal H_2\).

For \(j\ge0\) define the integer shell
\[
I_j=\{k\in\mathbb N:2^j\le k<2^{j+1}\},
\qquad c_j=\tfrac32 2^j.
\]
For a fixed integer \(L\ge1\), define the matrix \(F_L=(f^{(L)}_{n,k})\) on the normalized monomial coefficient spaces by
\[
f^{(L)}_{n,k}=
\begin{cases}
 b_{n,0},&k=0,\\
 (n+1)\sqrt{w_n(\beta)/w_k(\alpha)}
 \displaystyle\sum_{h=0}^{L-1}\frac{(c_j-k)^h}{(n+c_j+1)^{h+1}},&k\in I_j,\quad 0\le j<L,\\
0,&k\ge2^L.
\end{cases}
\]
This is not a numerical truncation of an infinite matrix: each shell term is a product of the output column vector with entries
\[
(n+1)\sqrt{w_n(\beta)}\,(n+c_j+1)^{-h-1}
\]
and the finite-support input row vector with entries
\[
\mathbf1_{I_j}(k)(c_j-k)^h/\sqrt{w_k(\alpha)}.
\]
All output vectors are square summable because \(\beta>1\). Thus \(F_L\) is a genuine bounded finite-rank operator and
\[
\operatorname{rank}F_L\le1+\sum_{j=0}^{L-1}L=1+L^2.
\]
The additional one-dimensional term handles \(k=0\) exactly.

**2. Uniform geometric approximation on every shell.** If \(k\in I_j\), then \(|c_j-k|\le 2^{j-1}\), while \(n+c_j+1\ge3\cdot2^{j-1}+1\). Therefore
\[
\left|\frac{c_j-k}{n+c_j+1}\right|\le\frac13
\quad\text{for all }n\ge0.
\]
The finite geometric identity, without an asymptotic error term, is
\[
\frac1{n+k+1}-\sum_{h=0}^{L-1}\frac{(c_j-k)^h}{(n+c_j+1)^{h+1}}
=\frac1{n+k+1}\left(\frac{c_j-k}{n+c_j+1}\right)^L.
\]
It follows that for \(1\le k<2^L\), the matrix-entry error is at most \(3^{-L}|b_{n,k}|\). By the Hilbert–Schmidt bound on operator norm, the full head-column error satisfies
\[
\|(B-F_L)P_{<2^L}\|\le3^{-L}\|B\|_{S_2},
\]
where \(P_{<2^L}\) is the input coefficient projection onto the first \(2^L\) coordinates.

**3. Quantitative tail bound.** The gamma-ratio asymptotic, valid uniformly for integer \(n,k\ge0\), gives
\[
|b_{n,k}|^2\le C_{\alpha,\beta}
\frac{(n+1)^{1-\beta}(k+1)^{\alpha+1}}{(n+k+1)^2}.
\]
For any integer \(k\ge1\), split the sum over \(n\) at \(n=k\). Then
\[
\sum_{n\ge0}|b_{n,k}|^2
\le C_{\alpha,\beta}(k+1)^{\alpha+1}
\left[(k+1)^{-2}\sum_{0\le n\le k}(n+1)^{1-\beta}
+\sum_{n>k}(n+1)^{-\beta-1}\right].
\]
Because \(\beta>1\), the first summation is bounded respectively by \(C(k+1)^{2-\beta}\), \(C\log(k+2)\), and \(C\) in the cases \(1<\beta<2\), \(\beta=2\), and \(\beta>2\); the second summation is at most \(C(k+1)^{-\beta}\). With \(\tau=\min\{\beta-\alpha-2,-\alpha\}>0\), these three cases give the common bound
\[
\sum_{n\ge0}|b_{n,k}|^2
\le C_{\alpha,\beta}(k+1)^{-1-\tau}\log(k+2).
\]
Summing the nonnegative column squares for \(k\ge2^L\), by comparison with the integral of \(x^{-1-\tau}\log(x+2)\), yields
\[
\|B(I-P_{<2^L})\|_{S_2}^2
\le C_{\alpha,\beta}(L+1)2^{-\tau L}.
\]
This argument also proves the finiteness of \(\|B\|_{S_2}\), independently of any finite computation.

**4. Approximation numbers and ideals.** Combining the head and tail estimates by the triangle inequality and using \(\|T\|\le\|T\|_{S_2}\) gives
\[
\|B-F_L\|\le C_{\alpha,\beta}
\left(3^{-L}+\sqrt{L+1}\,2^{-\tau L/2}\right).
\]
The Eckart–Young characterization of singular values as Hilbert-space approximation numbers implies
\[
s_{L^2+2}(B)\le\|B-F_L\|.
\]
For every sufficiently large \(N\), take \(L=\lfloor\sqrt{N-2}\rfloor\). The monotonicity of singular values, together with absorption of the polynomial factor \(\sqrt{L+1}\) into a slightly slower exponential, implies \(s_N(B)\le C e^{-c\sqrt N}\); adjust \(C\) for the finitely many small indices. It follows that for every \(p>0\),
\[
\sum_{N\ge1}s_N(B)^p\le C^p\sum_{N\ge1}\exp(-pc\sqrt N)<\infty.
\]
Finally, Li and Zhou's boundedness/compactness theorem proves the converse throughout \(\alpha,\beta>-1\), because every finite Schatten class is a class of compact bounded operators. This completes the proof.

## Verification

The included standalone Python 3 checker `check_differential_hilbert.py` uses exact rational arithmetic for geometric remainder identities, center-to-shell ratio bounds, finite separable factor counts, rational Bergman weight recurrences, and normalized coefficient checks. It also runs limited numerical checks of sampled column sums. The actual execution result was `DIFFERENTIAL_HILBERT_DYADIC_EXACT_OK 14947` (14,947 assertions). This checker does not prove the infinite-series tail estimates, the Schatten conclusions, or the universality in the parameters; these depend on the preceding analytic arguments.

A reproducer can construct \(F_L\) directly from the displayed finite formula, without external data. The rank bound requires only \(1+L^2\) separable factors; its output coordinate vectors have explicitly given convergent tails.

## Relationship to prior work

Li and Zhou establish the sharp cross-Bergman boundedness/compactness threshold and prove \(S_p\) membership for \(p\ge1\) in Theorem 4.2 of arXiv:2610.05672. Their formulas supply the normalized matrix used here, but neither their statement nor their proof provides the present explicit finite-rank approximation or \(0<p<1\) classification.

Peláez and Seco study generalized Hilbert operators as endomorphisms of weighted Dirichlet/Bergman spaces and give criteria for \(p\ge1\); their operator-domain assumptions and conclusion differ from this cross-space quantitative approximation theorem. Ye and Feng develop boundedness criteria for measure-induced operators between Bergman spaces, not the singular-value decay stated here. Beckermann and Townsend obtain low-rank estimates for *finite* separated Cauchy and Hankel matrices. Their foundational approximation ideas are closely related, but their finite-dimensional results do not state the infinite weighted cross-Bergman norm estimate or the tail estimate at a prescribed dyadic cutoff. Classical positive Hankel spectral asymptotics provide further nearby context but concern different matrix weights and symmetry.

## Limitations

The assertion \(\exp(-c\sqrt N)\) is an upper estimate, not a sharp spectral asymptotic. No uniform constants are asserted as the parameters approach the noncompact boundary. The construction specifically concerns the integral kernel \((1-tz)^{-2}\), standard radial weighted Bergman norms, and the compact parameter range. Generic finite Cauchy-matrix displacement bounds and related weighted-Hankel literature remain possible sources of a stronger implication or priority overlap; independent priority verification has not been performed. Only a self-review is available, not independent mathematical certification.

## References

1. S. Li and M. Zhou, *The Differential Hilbert Operator Between Weighted Bergman Spaces*, arXiv:2610.05672 (first publicly submitted 5 October 2026), especially (2.8), Theorems 3.1 and 4.2. https://arxiv.org/html/2610.05672v1
2. J. Á. Peláez and D. Seco, *Schatten classes of generalized Hilbert operators*, arXiv:1510.05455 (2015), Theorem 1 and Corollary 2. https://arxiv.org/abs/1510.05455
3. G. Ye and C. Feng, *Generalized Hilbert Operator Acting on Weighted Bergman Spaces and on Dirichlet Spaces*, arXiv:2207.11176 (2022), §4. https://arxiv.org/abs/2207.11176
4. B. Beckermann and A. Townsend, *On the singular values of matrices with displacement structure*, arXiv:1609.09494 (2016), §4.2. https://arxiv.org/html/1609.09494v1
5. C. P. Tantalakis, *Eigenvalue asymptotics for a class of multi-variable Hankel matrices*, *Concrete Operators* 10 (2023), 20220137, §1. https://doi.org/10.1515/conop-2022-0137
