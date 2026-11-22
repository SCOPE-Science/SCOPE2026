# Exact integrated BV decay for all iterates of the Bernstein operator

## Finding

For every integer \(n\ge2\) and every integer \(r\ge1\), the classical Bernstein operator
\[
(B_nf)(x)=\sum_{j=0}^n\binom nj x^j(1-x)^{n-j}f(j/n)
\]
acts on real *pointwise* Jordan-bounded-variation functions on \([0,1]\). Put \(Lf(x)=(1-x)f(0)+xf(1)\) and \(V(f)=\operatorname{Var}_{[0,1]}(f)\). Its sharp integrated endpoint-interpolation defect is
\[
\boxed{\sup_{V(f)>0}\frac{\|B_n^rf-Lf\|_{L^1(0,1)}}{V(f)}=C_{n,r}=\frac{\mathbf1^\mathsf T Q_n^{r-1}\mathbf1}{2(n+1)},}
\]
where \(Q_n\) is the \((n-1)\)-square strictly positive matrix
\[
(Q_n)_{ij}=\binom nj (i/n)^j(1-i/n)^{n-j},\qquad 1\le i,j\le n-1.
\]
This is half the probability that a size-\(n\) absorbing binomial Wright–Fisher chain, initially *uniformly distributed on all \(n+1\) states*, has not reached either endpoint by time \(r\), with the first observation at time one. The sharp coefficient is attained, for example, by any nonzero unit step whose only nodal change occurs across the first sample cell, or across the last sample cell.

The following complete nodal equality classification holds. Write \(d_j=f(j/n)-f((j-1)/n)\), \(1\le j\le n\). Equality for nonconstant \(f\) requires that \(d_j=0\) for all \(2\le j\le n-1\), that \(d_1d_n\le0\), and that \(V(f)=\sum_{j=1}^n|d_j|\). Conversely these conditions suffice. Thus no genuinely interior nodal jump can be extremal. For \(n=2\), the same classification holds with no interior-jump restriction.

The exact first-iterate constant and spectral asymptotics are
\[
C_{n,1}=\frac{n-1}{2(n+1)},\quad C_{n,r+1}<C_{n,r},\quad
C_{n,r}\sim\frac{1}{12a_n}\left(\frac{n-1}{n}\right)^r\quad(r\to\infty,\ n\text{ fixed}),
\]
where \(p=(p_1,\ldots,p_{n-1})\) is the unique normalized positive left Perron eigenvector of \(Q_n\), \(\sum_i p_i=1\), and \(a_n=\sum_i p_i(i/n)(1-i/n)>0\).

## Assumptions and scope

The input is a real function on the closed interval with *pointwise Jordan variation*, so sample values, including the endpoints, are part of the data and isolated changes count toward variation. These statements do not define a bounded operator on quotient \(BV\) equivalence classes mod almost-everywhere equality. All degrees and iterate counts above are finite integers. Integration is with Lebesgue measure of total mass one.

## Proof

**1. Martingale step reduction.** Let \(P_r(x,k)\) be the distribution of the size-\(n\) binomial reproduction chain at time \(r\), starting with \(X_1\sim\mathrm{Bin}(n,x)\), and thereafter with \(X_{t+1}\mid X_t=i\sim\mathrm{Bin}(n,i/n)\). Then \(B_n^rf(x)=\sum_kP_r(x,k)f(k/n)\). As \(\mathbb E[X_r/n]=x\), the chain is a bounded martingale. The step \(H_j(k)=\mathbf1_{\{k\ge j\}}\) has defect
\[
E_j(x)=\sum_{k=j}^{n-1}(1-k/n)P_r(x,k)-\sum_{k=1}^{j-1}(k/n)P_r(x,k).
\]
The endpoint step errors are \(E_1(x)=\sum_{k=1}^{n-1}(1-k/n)P_r(x,k)>0\) and \(E_n(x)=-\sum_{k=1}^{n-1}(k/n)P_r(x,k)<0\) for \(0<x<1\).

**2. Pointwise endpoint dominance.** By the triangle inequality, \(|E_j(x)|\) is bounded by the sum of the two nonnegative sums displayed above. If \(j\le\lfloor n/2\rfloor+1\), every \(k<j\) satisfies \(k/n\le1-k/n\); hence \(|E_j(x)|\le E_1(x)\). If \(j>\lfloor n/2\rfloor+1\), every \(k\ge j\) satisfies \(1-k/n\le k/n\); hence \(|E_j(x)|\le-E_n(x)\). For \(1<j<n\) the comparison with the appropriate endpoint is strict for \(0<x<1\): every intermediate binomial state has strictly positive probability, and at least one comparison weight is strict. This yields a sharp step estimate rather than a finite enumeration.

**3. Integrated sharp constant.** The symmetry \(P_r(1-x,n-k)=P_r(x,k)\) implies \(\int E_1=\int(-E_n)\). Expand any nodal data as \(f(k/n)=f(0)+\sum_{j=1}^k d_j\); affine reproduction gives \(B_n^rf-Lf=\sum_j d_jE_j\). Integrating stepwise endpoint dominance and using \(\sum|d_j|\le V(f)\) proves the upper bound. A first-cell step gives equality. Strictness for all interior jumps, positivity of \(E_1\), negativity of \(E_n\), and equality in the triangular decomposition give the stated complete equality classification.

**4. Survival formula.** With \(x\) uniform on \([0,1]\), the initial binomial state is *exactly uniform*: \(\int_0^1\binom nkx^k(1-x)^{n-k}\,dx=1/(n+1)\). Write \(\mu_r(k)=\int_0^1P_r(x,k)\,dx\). Reflection symmetry gives \(\mu_r(k)=\mu_r(n-k)\). Consequently
\[
\int_0^1E_1(x)\,dx=\sum_{k=1}^{n-1}(1-k/n)\mu_r(k)=\frac12\sum_{k=1}^{n-1}\mu_r(k)
=\frac{\mathbf1^\mathsf TQ_n^{r-1}\mathbf1}{2(n+1)}.
\]
Each interior state has positive probability to be absorbed in the next step, so the survival probability, and therefore \(C_{n,r}\), strictly decreases. At \(r=1\) uniformity gives \(C_{n,1}=(n-1)/(2(n+1))\).

**5. Sharp spectral decay.** The positive right eigenvector \(h_i=(i/n)(1-i/n)\) of \(Q_n\) has eigenvalue \(\lambda_2=(n-1)/n\), by the second binomial moment identity. Perron–Frobenius theory identifies this as the simple leading eigenvalue and a normalized positive left eigenvector \(p\). The other eigenvalues are \(\lambda_k=n!/[n^k(n-k)!]\), \(3\le k\le n\), strictly smaller than \(\lambda_2\), as follows from upper triangular action on polynomial degrees and restriction to the zero-endpoint subspace. The Perron rank-one limit yields
\[
C_{n,r}\sim\frac{(\sum_{i=1}^{n-1}h_i)(\sum_i p_i)}{2(n+1)\sum_ip_ih_i}\lambda_2^{r-1}=\frac{\lambda_2^r}{12a_n},
\]
because \(\sum_{i=1}^{n-1}h_i=(n^2-1)/(6n)\). The \(n=2\) case has a one-dimensional interior subspace and the same formula is exact.

## Verification

The standalone `checker.py` verifies exact rational binomial transition probabilities, conservation of total mass and mean, 10,912 pointwise endpoint-dominance comparisons on degrees \(2\) through \(9\), iterates \(1\) through \(8\), and rational evaluation points \(k/32\), \(1\le k\le31\). It also verifies the exact first-iterate coefficient. Output: `PASS exact rational pointwise tests 10912 for n=2..9,r=1..8,31 rational x; mass/mean and first-iterate constants`. Finite tests corroborate, not replace, the universal proof.

## Relationship to prior work

Kelisky and Rivlin (1967) proved the limiting endpoint-interpolation convergence of Bernstein iterates. Cooper and Waldron (technical report dated October 22, 1999; 2000 journal version) determined the full Bernstein eigenstructure, including the spectral ingredients used here. The present theorem concerns the distinct *sharp integrated \(BV\)-to-\(L^1\) norm at every finite iteration*, its endpoint-only equality classification, and its uniform-in-input sharp asymptotic amplitude. Neither cited source states that variational norm theorem in the inspected material. The general martingale endpoint comparison in Steps 1–2 is the new structural mechanism; the eigenvalues themselves are not claimed to be new. A previously recorded Bernstein-iteration result gives a sharp **output total-variation seminorm** under equal endpoint values, not this integrated error from linear interpolation, and has different extremizers and constants.

## Limitations

The spectral equivalence is for each fixed degree as iterate count grows; it is not a joint uniform-in-degree asymptotic. The results concern pointwise variation with sample traces, not a.e. \(BV\) classes. A non-indexed historical equivalent of the sharp variational claim remains a priority risk. The initial-source date follows the bibliographic listing for the 1967 paper, whose journal issue confirms the year but does not specify the exact day.

## References

1. R. P. Kelisky and T. J. Rivlin, “Iterates of Bernstein polynomials,” *Pacific Journal of Mathematics* 21 (1967), 511–520. https://msp.org/pjm/1967/21-3/pjm-v21-n3-p12-s.pdf
2. S. Cooper and S. Waldron, “The Eigenstructure of the Bernstein Operator,” technical report dated October 22, 1999; *Journal of Approximation Theory* 105 (2000), 133–165. https://www.academia.edu/104185671/The_Eigenstructure_of_the_Bernstein_Operator ; https://doi.org/10.1006/jath.2000.3464
