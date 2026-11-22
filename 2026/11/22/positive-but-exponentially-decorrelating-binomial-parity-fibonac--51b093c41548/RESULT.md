# Positive but exponentially decorrelating binomial-parity Fibonacci transforms

## Finding
For every nonnegative integer \(n\), define the two nonnegative integer sums
\[
U(n)=\sum_{j=0}^{n}\bigl(\binom{n-j}{2j}\binom nj\bmod2\bigr),\qquad
V(n)=\sum_{j=0}^{n}\bigl(\binom{3j}{j}\binom nj\bmod2\bigr),
\]
where each parenthesized residue is either zero or one and \(\binom rs=0\) outside \(0\le s\le r\). Let \(X_L\) be uniform on the integers \(0\le n<2^L\). For \(L\ge2\), the covariance of \(U(X_L)\) and \(V(X_L)\) is **strictly positive**, but their Pearson correlation tends to zero at an exact exponential rate:
\[
\operatorname{Corr}(U(X_L),V(X_L))\sim C\rho^L,
\quad C=0.9980884128\ldots>0,\quad \rho=0.9865717478\ldots\in(0,1).
\]
The constants are specified algebraically in the proof. Exact finite-length formulas are given by the five generating functions below. Write \(m_U(L)=\sum_{n<2^L}U(n)\), \(m_V(L)=\sum_{n<2^L}V(n)\) and \(b_{ij}(L)=\sum_{n<2^L}i(n)j(n)\) for \(i,j\in\{U,V\}\). Then
\[
\begin{aligned}
\sum_{L\ge0}m_U(L)z^L&=\frac1{1-2z-z^2},\\
\sum_{L\ge0}m_V(L)z^L&=\frac{1+z}{1-2z-2z^2},\\
\sum_{L\ge0}b_{UU}(L)z^L&=\frac{1-z}{1-3z-z^2+z^3},\\
\sum_{L\ge0}b_{VV}(L)z^L&=\frac{1+2z-z^2}{1-3z-4z^2+2z^3},\\
\sum_{L\ge0}b_{UV}(L)z^L&=\frac1{1-3z-2z^2+z^3}.
\end{aligned}
\]
The two one-point sums and the \(UU\) second-moment *numerical sequence* are pre-existing results; they are included as necessary inputs to the joint-correlation theorem, **not claimed as novel**. The new assertion concerns the exact mixed moment and the strict-positive-yet-decaying correlation between this specific natural pair.

## Assumptions and scope
All formulas concern the ordinary integer sequence of parity counts above and uniform sampling over the complete initial binary interval. They do not concern shifts of the sampling interval or residue distributions for other primes. Fibonacci numbers are normalized by \(F_0=0\), \(F_1=1\), \(F_{r+2}=F_{r+1}+F_r\). Every sum at \(L=0\) has the sole index \(n=0\); the Pearson correlation is asserted only for \(L\ge2\), since \(U(X_0)\) and \(U(X_1)\) are constant.

## Proof
**1. Run-length representations.** Theorem 5 and Theorem 6 of Rampersad and Wiebe (2023) identify the two binomial-parity sums as run-length transforms. If the maximal runs of ones in the binary expansion of \(n\) have lengths \(\ell_1,\ldots,\ell_t\), then
\[
U(n)=\prod_{h=1}^t F_{\ell_h+1},\qquad
V(n)=\prod_{h=1}^t F_{\ell_h+2},
\]
with empty products one. Leading zeros in a length-\(L\) binary word do not affect the products. These source theorems follow from binary Lucas congruences and the explicit two-dimensional linear representations in the cited paper; the finite direct-parity comparisons in `checks/check.py` independently check their normalization through index \(1199\).

**2. A finite-word renewal identity.** For an arbitrary sequence of run weights \(w_\ell\) (\(\ell\ge0\)), with \(w_0=1\), let \(H_L\) be the sum of the products of weights of all maximal one-runs across every binary word of exactly \(L\) bits. Put \(A(z)=\sum_{\ell\ge0}w_\ell z^\ell\) and \(H(z)=\sum_{L\ge0}H_L z^L\). Every nonempty word either consists entirely of ones, or begins with a uniquely determined prefix \(1^\ell0\), \(0\le\ell<L\), followed by an arbitrary suffix. Thus
\[
H_L=w_L+\sum_{\ell=0}^{L-1}w_\ell H_{L-\ell-1},
\qquad H(z)=\frac{A(z)}{1-zA(z)}.
\]
This identity holds formally, without any convergence assumption.

**3. Evaluate all five weight series.** Apply the renewal identity to \(w_\ell=F_{\ell+1}\), \(F_{\ell+2}\), \(F_{\ell+1}^2\), \(F_{\ell+2}^2\) and \(F_{\ell+1}F_{\ell+2}\), respectively. The first two weight generating functions are
\[
\frac1{1-z-z^2},\qquad \frac{1+z}{1-z-z^2}.
\]
The three quadratic weight generating functions are, in the same order as the quadratic choices,
\[
\frac{1-z}{D(z)},\qquad
\frac{1+2z-z^2}{D(z)},\qquad
\frac1{D(z)},\qquad D(z)=1-2z-2z^2+z^3.
\]
These follow by multiplying each weight series by \(D(z)\): the Fibonacci recurrence makes every coefficient of degree at least three vanish, and the initial coefficients determine the displayed numerators. The five stated moment functions follow by substitution into \(H=A/(1-zA)\).

**4. Strict positivity of covariance.** Each product of Fibonacci run weights is coordinatewise nondecreasing as a function of the independent binary digits. Indeed, changing a zero to a one merges its neighboring one-runs, of lengths \(a,b\ge0\). For \(U\), the old local product \(F_{a+1}F_{b+1}\) is no greater than \(F_{a+b+2}\), because
\[
F_{a+b+2}=F_{a+2}F_{b+1}+F_{a+1}F_b.
\]
For \(V\), the new factor is strictly greater than the old one by
\[
F_{a+b+3}=F_{a+2}F_{b+2}+F_{a+1}F_{b+1}.
\]
The elementary positive-association inequality for independent fair bits now gives \(\operatorname{Cov}(U(X_L),V(X_L))\ge0\). To recall its proof, condition on the last bit, write covariance as the mean conditional covariance plus covariance of the two conditional means, and induct on the number of bits; monotonicity makes the second term nonnegative. Strictness holds whenever \(L\ge2\): condition on the next bit being one and all other bits being zero, then toggling the first bit changes \((U,V)\) from \((1,2)\) to \((2,3)\), yielding strictly positive conditional covariance. The other conditional contributions are nonnegative. Both variances are positive for \(L\ge2\).

**5. Exact exponential decorrelation.** Define \(r_{UU}\), \(r_{VV}\), \(r_{UV}\) as the largest real roots, respectively, of
\[
\begin{split}
p_{UU}(x)&=x^3-3x^2-x+1,\\
p_{VV}(x)&=x^3-3x^2-4x+2,\\
p_{UV}(x)&=x^3-3x^2-2x+1.
\end{split}
\]
The three roots are in the rational intervals \((3.2143,3.2144)\), \((3.8951,3.8952)\), and \((3.4908,3.4909)\), respectively. Their other roots are confined, respectively, to \((-0.68,-0.67)\) and \((0.46,0.47)\); \((-1.30,-1.29)\) and \((0.39,0.40)\); \((-0.84,-0.83)\) and \((0.34,0.35)\). Hence all three dominant roots are simple and strictly dominate the other roots in modulus.

For each second-moment rational function \(N_{ij}(z)/D_{ij}(z)\), define
\[
\kappa_{ij}=\frac{N_{ij}(1/r_{ij})}{-(1/r_{ij})D_{ij}'(1/r_{ij})}>0.
\]
Partial fractions then yield
\[
b_{ij}(L)=\kappa_{ij}r_{ij}^L+o(r_{ij}^L).
\]
The one-point totals have respective positive dominant roots \(\alpha=1+\sqrt2\) and \(\beta=1+\sqrt3\). The rational bounds above give \(r_{UV}>\alpha\beta/2\), \(r_{UU}>\alpha^2/2\), and \(r_{VV}>\beta^2/2\). Consequently, after division by the appropriate powers of two, each covariance or variance is asymptotic to the corresponding second-moment term, the products of first moments being exponentially smaller. Thus
\[
\operatorname{Corr}(U(X_L),V(X_L))
\sim \frac{\kappa_{UV}}{\sqrt{\kappa_{UU}\kappa_{VV}}}
\left(\frac{r_{UV}}{\sqrt{r_{UU}r_{VV}}}\right)^L.
\]
Finally \(3.4909^2<3.2143\cdot3.8951\), an exact rational comparison, proves that the parenthesized base is strictly below one. Numerical evaluation gives the constants in the finding. All root isolations and comparisons have rational arithmetic certificates in `checks/check.py`.

## Verification
The accompanying standalone `checks/check.py` uses the elementary binary Lucas parity test, not the published run-length automata, for \(1200\) independently calculated input pairs. It also enumerates all words in each of the \(15\) blocks \(0\le n<2^L\), \(0\le L\le14\), checks all five rational moment series coefficientwise, and checks exact sign changes at rational root intervals and the strict spectral inequality. The script requires only Python's standard library. Run `python3 checks/check.py`. These finite checks corroborate, but do not replace, the infinite proof above.

## Relationship to prior work
Rampersad and Wiebe (2023), Theorems 5–6, prove both individual run-length descriptions; Section 6 determines their one-point averages. Their results, including the general linear-representation method, are used here as known inputs, not claimed as new. OEIS A030186 already records exactly the \(UU\) squared-sum coefficient sequence \(1,2,7,22,71,\ldots\), with a ladder-matching interpretation and generating function. Zhang and Grossman (2018) derive generating functions of powers of recurrence sequences and provide related tiling machinery, but not this comparison of two binomial-parity transforms. The asserted distinction is the exact **mixed** dyadic moment and, especially, the positive yet exponentially vanishing Pearson correlation for this specific pair. Related published run-spectrum and binomial-parity analyses do not imply this comparison from their stated parameters; a literature and database search cannot exclude unindexed or implicit rediscoveries.

## Limitations
The result is for this exact pair and the complete uniform dyadic blocks, not every pair of run-length transforms. Correlation is undefined at the first two degenerate levels, so the domain is \(L\ge2\). The relationship between the finite moment recurrences and older general generating-function machinery makes priority assessment particularly delicate; the potentially equivalent formulation as a tensor-product transfer-matrix calculation is a residual risk. No independent external audit has been performed.

## References
- N. Rampersad and M. Wiebe, *Sums of products of binomial coefficients mod 2 and 2-regular sequences*, arXiv:2309.04012v1, 7 September 2023. https://arxiv.org/html/2309.04012
- OEIS A030186, *Number of matchings in the ladder graph*, with exact generating function, accessed 15 November 2026. https://oeis.org/A030186
- Y. Zhang and G. Grossman, *A Combinatorial Proof for the Generating Function of Powers of a Second-Order Recurrence Sequence*, J. Integer Seq. 21 (2018), 18.3.3. https://cs.uwaterloo.ca/journals/JIS/VOL21/Zhang/zhang44.pdf
