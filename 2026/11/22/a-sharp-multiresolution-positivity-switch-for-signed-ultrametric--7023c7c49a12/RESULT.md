# A sharp multiresolution positivity switch for signed ultrametric exponential kernels

## Finding
Let \(p\) be any prime, let \(a,b>0\), and let \(\lambda\ge0\). On the compact additive group \(G=\mathbb Z_p\), equipped with its normalized Haar probability measure, define
\[
 F_a(x)=\exp(-a|x|_p),\qquad K_{a,b,\lambda}(x,y)=F_a(x-y)-\lambda F_b(x-y).
\]
Define the explicitly convergent mass
\[
 m_p(a)=\left(1-\frac1p\right)\sum_{j=0}^{\infty}p^{-j}e^{-ap^{-j}}.
\]
The kernel is positive semidefinite on every finite subset of \(G\) **exactly** when \(0\le\lambda\le\Lambda_p(a,b)\), where
\[
 \boxed{\Lambda_p(a,b)=\begin{cases}
 m_p(a)/m_p(b),&a>b,\\
 1,&a=b,\\
 a/b,&0<a<b.
 \end{cases}}
\]
For unequal rates the kernel at its sharp endpoint remains strictly positive definite on every finite set of distinct points. Its endpoint reproducing-kernel Hilbert space is dense in \(C(G)\) when \(a<b\), but when \(a>b\) its uniform closure is exactly the codimension-one subspace of continuous Haar-mean-zero functions. Thus the two orderings exhibit different types of spectral obstruction.

The distinction survives exact multiresolution discretization, but its location changes. For \(N\ge1\), let \(G_N=\mathbb Z_p/p^N\mathbb Z_p\), and define the canonical coset-averaged kernels by averaging \(F_a\) and \(F_b\) over a difference coset. At every finite depth, the largest admissible subtraction coefficient is
\[
 \boxed{\Lambda_{p,N}(a,b)=\begin{cases}
 m_p(a)/m_p(b),&a>b,\\
 1,&a=b,\\
 c_{p,a}(N)/c_{p,b}(N),&a<b,
 \end{cases}}
\]
where the explicit positive conductor coefficient is
\[
 c_{p,a}(n)=\sum_{j=n}^{\infty}p^{-j}\big(e^{-ap^{-j}}-e^{-ap^{-(j-1)}}\big),\qquad n\ge1.
\]
When \(a>b\), the endpoint finite Gram matrix has nullity exactly one (the constant character). When \(a<b\), its finite-depth endpoint has nullity exactly \(p^N-p^{N-1}\) (all characters of conductor \(p^N\)), while at the infinite-depth endpoint every conductor coefficient is strictly positive. In the latter case the finite-resolution excess has the sharp geometric asymptotic
\[
 \boxed{\Lambda_{p,N}(a,b)-\frac ab
 =\frac ab(b-a)\frac{(p+1)(1-p^{-2})}{2(1-p^{-3})}\,p^{-N}
 +O_{p,a,b}(p^{-2N}).}
\]
The same formulas hold for all primes, including \(p=2\). No normalization by the number of sample sites is implicit in the finite Gram matrices.

## Assumptions and scope
For \(x\ne0\) write \(v_p(x)=j\) when \(x\in p^jG\setminus p^{j+1}G\), so \(|x|_p=p^{-j}\), and put \(|0|_p=0\). A character has conductor \(p^n\), \(n\ge1\), if it is trivial on \(p^nG\) but not on \(p^{n-1}G\); the trivial character has conductor level zero. A positive-semidefinite kernel satisfies \(\sum_{i,j}\overline{z_i}z_jK(x_i,x_j)\ge0\) for every finite selection of sites and complex coefficients; strict positivity requires a positive value for every nonzero coefficient vector on pairwise distinct sites. The finite quotient profile is
\[
 F_a^{(N)}(z+p^NG)=p^N\int_{z+p^NG}F_a(u)\,du.
\]
It equals \(e^{-ap^{-v_p(z)}}\) on any nonzero residue class and equals \(m_p(ap^{-N})\) on the zero residue class. The group convolution operator is normalized by Haar measure, whereas the finite Gram matrices consist of unnormalized kernel entries; their eigenvalues consequently differ from normalized Fourier coefficients by the factor \(p^N\).

## Proof
**1. Exact Fourier coefficients.** For \(j\ge1\), put \(\Delta_a(j)=e^{-ap^{-j}}-e^{-ap^{-(j-1)}}>0\). A uniformly convergent nested-ball expansion is
\[
 F_a(x)=e^{-a}+\sum_{j=1}^{\infty}\Delta_a(j)\mathbf1_{p^jG}(x).
\]
The Fourier coefficient of \(\mathbf1_{p^jG}\) at a character of conductor \(p^n\) equals \(p^{-j}\) when \(j\ge n\), and zero otherwise. Hence every nontrivial character of conductor \(p^n\) has coefficient \(c_{p,a}(n)>0\), while the trivial-character coefficient is \(m_p(a)\). The latter identity also follows by integrating shell measures \((1-p^{-1})p^{-j}\). Fourier--Bochner positivity on a compact Abelian group now reduces the kernel criterion to the simultaneous scalar inequalities
\[
 m_p(a)-\lambda m_p(b)\ge0,\qquad c_{p,a}(n)-\lambda c_{p,b}(n)\ge0\quad(n\ge1).
\]

**2. Strict monotonicity of conductor ratios.** Put \(R_n=c_{p,a}(n)/c_{p,b}(n)\). For positive real \(u\) define
\[
 r(u)=\frac{e^{-au}-e^{-apu}}{e^{-bu}-e^{-bpu}}.
\]
Writing \(z=(p-1)u/2\), its logarithmic derivative is
\[
 \frac{d}{du}\log r(u)=-\frac{(a-b)(p+1)}2
 +\frac{p-1}{2}\big(a\coth(az)-b\coth(bz)\big).
\]
For \(s>0\), \(g(s)=s\coth s\) satisfies \(0<g'(s)<1\). Indeed,
\(g'(s)=(\sinh s\cosh s-s)/\sinh^2s>0\), while \(g'(s)<1\) follows from \(e^{-s}\sinh s<s\). It follows that \(r(u)\) decreases strictly with \(u\) when \(a>b\), and increases strictly when \(a<b\). Its limit at zero is \(a/b\).

Each \(R_n\) is the strictly positive \(c_{p,b}\)-weighted average of \(r(p^{-j})\) over \(j\ge n\). Removing the first element of this weighted tail therefore strictly raises \(R_n\) when \(a>b\), and strictly lowers it when \(a<b\). Accordingly,
\[
 a>b:\ R_1<R_2<\cdots<a/b,\qquad
 a<b:\ R_1>R_2>\cdots>a/b,
\]
with the common limit \(a/b\).

**3. Comparing the Haar mode and the first conductor.** Directly from the first ball expansion,
\(c_{p,a}(1)=m_p(a)-e^{-a}\). The function \(a\mapsto e^{-a}/m_p(a)\) is strictly decreasing because
\[
 \frac{m_p(a)}{e^{-a}}=\int_G e^{a(1-|x|_p)}\,dx
\]
is strictly increasing. Therefore
\[
 a>b:\ \frac{m_p(a)}{m_p(b)}<R_1,
 \qquad a<b:\ \frac{m_p(a)}{m_p(b)}>R_1.
\]
When \(a>b\), the trivial Fourier coefficient is the first and unique active positivity constraint; when \(a<b\), the infimum is \(\lim_{n\to\infty}R_n=a/b\) and is not attained at any finite conductor. When \(a=b\), all Fourier coefficients are multiplied by \(1-\lambda\). These observations prove the infinite-group cutoff.

**4. Finite-depth extrema and nullities.** The quotient \(G_N\) has precisely the trivial character and characters of conductors \(p,\ldots,p^N\). Coset averaging preserves exactly those Fourier coefficients. On the full \(p^N\)-point Gram matrix, the eigenvalue corresponding to conductor level \(n\) is \(p^N(c_{p,a}(n)-\lambda c_{p,b}(n))\), with \(c_{p,a}(0)=m_p(a)\). The minimum among levels \(0,\ldots,N\) is at level zero if \(a>b\) and level \(N\) if \(a<b\). At the respective cutoff these and only these levels vanish. There are precisely \(p^N-p^{N-1}\) characters of conductor \(p^N\), giving the asserted nullities. For \(a=b\), the cutoff yields the identically zero kernel and every eigenvalue vanishes.

**5. Sharp finite-depth expansion.** Taylor expansion of the positive tail, uniform as \(n\to\infty\), gives
\[
 c_{p,a}(n)=\frac{(p-1)a}{1-p^{-2}}p^{-2n}
 -\frac{(p^2-1)a^2}{2(1-p^{-3})}p^{-3n}
 +O_{p,a}(p^{-4n}).
\]
Dividing the expansions for \(a\) and \(b\) yields
\[
 R_n=\frac ab\left[1+(b-a)\frac{(p+1)(1-p^{-2})}{2(1-p^{-3})}p^{-n}
 +O_{p,a,b}(p^{-2n})\right].
\]
Substituting \(n=N\) proves the finite-resolution excess with the claimed order and coefficient.

**6. Strictness and approximation at infinite depth.** If \(a<b\), every character coefficient is strictly positive at \(\lambda=a/b\); hence the kernel is strictly positive definite on distinct sites. Every character belongs to its reproducing-kernel Hilbert space, and finite character polynomials are uniformly dense in \(C(G)\), so the space is universal. If \(a>b\), only the trivial coefficient vanishes at \(\lambda=m_p(a)/m_p(b)\). If a nonzero finite atomic measure annihilated all other characters, Fourier uniqueness would force it to be a scalar multiple of nonatomic Haar measure, an impossibility. Thus all finite distinct-site matrices are strictly positive definite. Conversely every Hilbert-space function has zero Haar mean, while every nontrivial character lies in the space; character-polynomial density proves that its uniform closure is exactly the Haar-mean-zero subspace. This proves the endpoint dichotomy.

## Verification
The accompanying \(verify.py\) is a self-contained Python standard-library checker. It directly forms the finite coset-averaged profile and computes all discrete Fourier coefficients independently from the nested-ball formula, for primes \(2,3,5\), three quotient depths, and four unequal-rate pairs. It also tests conductor-ratio ordering, active levels, and the first geometric asymptotic correction. Its numerical assertions are supporting checks, not a substitute for the exact arguments in Steps 1--6. Running \(python3 verify.py\) from the package directory prints a single PASS message on completion.

## Relationship to prior work
The harmonic ball-filtration framework for ultrametric groups is classical. Bendikov, Cygan and Woess (2016) analyze homogeneous hierarchical Laplacians and heat-kernel oscillations on noncompact ultrametric spaces, rather than the signed exponential-of-distance profile on compact \(\mathbb Z_p\). Zúñiga-Galindo, He and Zambrano-Luna (2023) use convolution kernels and quotient groups \(G_N\) to model finite-depth non-Archimedean interactions; their results do not specify this Loewner-positivity boundary or the finite-resolution excess. Vallin and Dovgoshey (2019) characterize metric-preserving transformations, not positive-definite covariance differences. An existing log-periodically modulated \(\mathbb Z_p\) covariance classification instead studies oscillatory geometric valuation profiles. The specific result here is the sharp **two-rate comparison**, monotone conductor-ratio theorem, and resolution-dependent high-conductor singular multiplicity, not the generic Fourier criterion or the existence of the ball decomposition.

## Limitations
The theorem concerns the compact additive group of \(p\)-adic integers, ordinary real exponentials of its ultrametric distance, nonnegative subtraction strength, and canonical *coset-averaged* finite quotients. The finite-depth formula is not asserted for pointwise samples with an independently chosen diagonal convention, other profiles, or arbitrary ultrametric spaces. The finite checker cannot establish positivity at all conductors; the infinite proof does so. Literature comparisons establish only best-knowledge historical priority, not an exhaustive uniqueness or independence certificate.

## References
1. W. A. Zúñiga-Galindo, C. He and B. A. Zambrano-Luna, *p-Adic Statistical Field Theory and Convolutional Deep Boltzmann Machines*, arXiv:2302.03817, first public 2023-02-08; sections 2, 4 and Appendix A, https://arxiv.org/abs/2302.03817.
2. A. Bendikov, W. Cygan and W. Woess, *Oscillating heat kernels on ultrametric spaces*, arXiv:1610.03292, first public 2016-10-11; sections 1--3, https://arxiv.org/abs/1610.03292.
3. R. W. Vallin and O. A. Dovgoshey, *P-adic metric preserving functions and their analogues*, arXiv:1912.10411, first public 2019-12-22; sections 1--4, https://arxiv.org/abs/1912.10411.
4. *Arithmetic positivity islands for log-periodic covariances on p-adic integers*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-arithmetic-positivity-islands-for-log-periodic-covariances-on-p--9e9fab847820 (distinct oscillatory geometric profile).
