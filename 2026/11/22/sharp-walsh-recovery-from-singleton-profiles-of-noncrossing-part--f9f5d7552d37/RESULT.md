# Sharp Walsh recovery from singleton profiles of noncrossing partitions

## Finding

For each integer \(n\ge1\), let \(\mathrm{NC}(n)\) be the noncrossing partitions of the cyclically ordered labels \([n]\). Let \(s(\pi)\in\mathbb F_2^n\) be the indicator of the labels that form singleton blocks of \(\pi\), and let \(f_n(x)=\#\{\pi\in\mathrm{NC}(n):s(\pi)=x\}\). Convolve on \(\mathbb F_2^n\) with this **counting** kernel, without probability normalization. At a Walsh frequency of Hamming weight \(w\), its eigenvalue is

\[
\Lambda_{n,w}=\sum_{j=0}^w\binom wj(-2)^j C_{n-j},\qquad C_k=\frac1{k+1}\binom{2k}k.
\]

**Complete sign and zero classification.** For \(0\le w\le n-2\), all \(\Lambda_{n,w}\) are strictly positive. If \(n\) is even, \(\Lambda_{n,n-1}=0\) and \(\Lambda_{n,n}>0\); if \(n\) is odd, \(\Lambda_{n,n-1}>0\) and \(\Lambda_{n,n}<0\). Explicitly,

\[
\Lambda_{n,n}=(-1)^n\binom n{\lfloor n/2\rfloor},\qquad
\Lambda_{n,n-1}=\begin{cases}0,&n\text{ even},\\ C_{(n-1)/2},&n\text{ odd}.\end{cases}
\]

Thus the convolution is invertible at every odd order and singular at every even order, with **exact nullity \(n\)** at even order. The sharp nonzero Fourier multiplier gap is

\[
\gamma_n=\begin{cases}C_{(n-1)/2},&n\text{ odd},\\2C_{n/2-1},&n\text{ even}.\end{cases}
\]

The exact Moore–Penrose inverse norm is \(\gamma_n^{-1}\) in \(\ell^2\), and at odd order this is the inverse operator norm. The largest multiplier magnitude is \(C_n\); hence the ratio of largest to smallest nonzero singular values is \(C_n/\gamma_n\).

**Sharp endpoint recovery.** Let \(W_n=\operatorname{ran}T_n\). Among *all* linear projections \(Q\) onto \(W_n\), real or complex and not necessarily translation-invariant, the least \(\ell^1\)- and \(\ell^\infty\)-operator norms are equal, with value

\[
\mathcal P_n=\begin{cases}
1,&n\text{ odd},\\
1+\dfrac{n}{2^n}\left(\binom n{n/2}-2\right),&n\text{ even}.
\end{cases}
\]

In particular, through even \(n\), the lost Fourier fraction \(n/2^n\) tends to zero exponentially while \(\mathcal P_n\sim\sqrt{2n/\pi}\) diverges.

## Assumptions and scope

All labels are distinct and cyclically ordered. A partition is noncrossing if there are no \(a<b<c<d\) with \(a,c\) in one block and \(b,d\) in a different block. The empty singleton profile may have multiplicity, which is retained in \(f_n\). All statements use unnormalized Walsh characters \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\), counting convolution and counting-measure \(\ell^p\) norms on the Boolean group. The rank and projector statements concern all real or complex functions on the Boolean cube; \(n\) is any positive integer.

## Proof

**1. Every multiplier is a Catalan binomial transform.** For any prescribed set \(J\subseteq[n]\) of \(j\) labels, the partitions in which each label of \(J\) is singleton are in bijection with \(\mathrm{NC}(n-j)\), by deleting and reinstating those singleton blocks. Thus \(\#\{\pi:J\subseteq s(\pi)\}=C_{n-j}\). For a Walsh frequency support \(S\) of size \(w\), expand \((-1)^{|S\cap s(\pi)|}=\prod_{i\in S}(1-2\mathbf1_{\{i\text{ singleton}\}})\), sum over partitions, and exchange sums. This gives the displayed transform formula and proves that the multiplier depends only on \(w\).

**2. The sign pattern and exact zeros.** The Catalan moments admit the elementary beta-integral representation

\[
C_k=\frac{1}{2\pi}\int_0^4 x^k\sqrt{\frac{4-x}{x}}\,dx.
\]

For \(m=n-w\ge1\), substitute \(y=x-2\) to get

\[
\Lambda_{n,w}=\frac{1}{2\pi}\int_{-2}^{2}y^w(2+y)^{m-1}\sqrt{4-y^2}\,dy.
\]

For even \(w\), the integrand is nonnegative and positive on a set of positive measure. For odd \(w\), pairing \(y\) and \(-y\) shows that the integral is zero precisely at \(m=1\), and positive at every \(m\ge2\), because \((2+y)^{m-1}-(2-y)^{m-1}>0\) for \(0<y<2\). At \(m=0\), the integral instead becomes

\[
\Lambda_{n,n}=\frac{1}{2\pi}\int_{-2}^2 \frac{y^n(2-y)}{\sqrt{4-y^2}}\,dy=(-1)^n\binom n{\lfloor n/2\rfloor},
\]

by the even moments of the arcsine density. At \(m=1\), semicircle moments give \(\Lambda_{n,n-1}=0\) when \(n\) is even, and \(C_{(n-1)/2}\) when \(n\) is odd. Consequently the only vanishing characters are the \(n\) frequencies of weight \(n-1\) in even order.

**3. Sharp nonzero spectral gap.** From the binomial expression,

\[
\Lambda_{n,w}-\Lambda_{n,w+1}=2\Lambda_{n-1,w}\quad(0\le w<n).
\]

The positivity just established makes \(\Lambda_{n,w}\) nonincreasing for \(0\le w\le n-1\). For odd \(n\), the least positive value is therefore \(\Lambda_{n,n-1}=C_{(n-1)/2}\); the absolute value at \(w=n\) is a larger central binomial coefficient (the case \(n=1\) is equality). For even \(n\), the least positive value is \(\Lambda_{n,n-2}=2\Lambda_{n-1,n-2}=2C_{n/2-1}\); the value at \(w=n\) has larger magnitude (at \(n=2\) equality). The upper bound \(|\Lambda_{n,w}|\le C_n\) follows directly because every summand in the signed partition sum has modulus one, and equality is attained at \(w=0\). Fourier diagonalization gives the Hilbert norms and condition numbers.

**4. The unrestricted sharp endpoint projection.** For odd \(n\), \(W_n\) is the entire function space and the identity is its only projection. For even \(n\), the unique translation-commuting projection onto \(W_n\) has Walsh symbol \(\mathbf1_{\{|S|\ne n-1\}}\), hence convolution kernel

\[
p_n(x)=\mathbf1_{\{x=0\}}-2^{-n}\sum_{|S|=n-1}\chi_S(x)
=\mathbf1_{\{x=0\}}-2^{-n}(-1)^{|x|}(n-2|x|).
\]

The last identity is the direct degree-\(n-1\) Krawtchouk sum. Since the \(\ell^1\) and \(\ell^\infty\) norms of a convolution operator on a finite group both equal its kernel's absolute sum, and

\[
\sum_{x\in\mathbb F_2^n}|n-2|x||=n\binom n{n/2}\qquad(n\text{ even}),
\]

we obtain the stated \(\mathcal P_n\). To show this is optimal without invariance assumptions, average *any* projection \(Q\) onto \(W_n\) over conjugations by Boolean translations. The average is still a projection onto \(W_n\) because translations preserve \(W_n\) and every term fixes \(W_n\) pointwise. Its norm is at most \(\|Q\|\) and it commutes with translations; Fourier decomposition makes it exactly the projector with kernel \(p_n\). This works over real and complex scalars at either endpoint.

**5. Asymptotic separation.** The nullity fraction at even \(n\) is exactly \(n/2^n\). Stirling's formula gives \(\binom n{n/2}/2^n\sim\sqrt{2/(\pi n)}\), yielding \(\mathcal P_n\sim\sqrt{2n/\pi}\).

## Verification

The included pure-standard-library `verify.py` independently generates all ordinary partitions through restricted-growth strings, filters the noncrossing ones by the defining forbidden-crossing quadruple, accumulates multiplicities of singleton profiles, and computes their complete exact integer Walsh transforms. For each \(1\le n\le9\), the transform agrees at every frequency with the independent Catalan-binomial expression, and the exact zero set, least nonzero gap, and rational endpoint projection norm agree with the theorem. All algebraic multiplier formulas and sign/gap predictions were additionally checked directly in arbitrary-precision integers through \(n=120\). These finite checks support, but do not replace, the all-order proof above. Reproduce with `python3 verify.py` (8495 passed exact assertions).

## Relationship to prior work

Classical noncrossing partitions are Catalan counted. Callan (2005) studies conjugation and singleton/adjacency equidistribution, including noncrossing partitions. Munagi (2016) determines cyclic adjacency counts and records the first-singleton moment \(nC_{n-1}\) for noncrossing partitions. Mamede (2008) gives a noncrossing/nonnesting partition bijection. Those results supply the combinatorial foundation; the exact singleton-profile signed Fourier cancellation, all-order nullity, and unrestricted optimal projection norm are the additional assertions considered here. Existing results on co-block edge-incidence Fourier transforms or unrestricted set partitions use different Boolean encodings or different counting kernels and do not directly imply this theorem.

## Limitations

The kernel is weighted by the number of partitions with a given singleton profile, not the uniform indicator of the *set of distinct profiles*. The result concerns singleton-block incidence, not a pairwise co-block or graph adjacency encoding. The sharp \(\ell^1\) and \(\ell^\infty\) bounds concern projection onto the recoverable range, not the norm of the inverse on that range. The infinite-family theorem is analytically proved; finite computations alone would not establish it. Exhaustive historical priority cannot be guaranteed, particularly against differently indexed binomial-transform identities. Independent mathematical audit has not been performed.

## References

- D. Callan, *On conjugates for set partitions and integer compositions*, arXiv:math/0508052, original public version 2005-08-02. https://arxiv.org/abs/math/0508052
- A. O. Munagi, *On singletons and adjacencies of set partitions*, Rocky Mountain Journal of Mathematics 46 (2016), 301–307, DOI:10.1216/RMJ-2016-46-1-301. https://doi.org/10.1216/RMJ-2016-46-1-301
- R. Mamede, *A bijection between noncrossing and nonnesting partitions of types A and B*, arXiv:0810.1422, original public version 2008-10-08. https://arxiv.org/abs/0810.1422
- G. Kreweras, *Sur les partitions non croisées d'un cycle*, Discrete Mathematics 1 (1972), 333–350. (Classical noncrossing-partition framework, cited by the above literature.)
