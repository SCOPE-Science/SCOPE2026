# Arithmetic resonance of cross-base tent observations: a sharp bounded-versus-linear covariance law

## Finding

Let \(X\) be Lebesgue uniform on \([0,1]\), and define the centered periodic triangular observable
\[
\psi(x)=\operatorname{dist}(x,\mathbb Z)-\frac14.
\]
For each integer \(b\ge2\) and \(N\ge1\), set
\[
S_{b,N}(X)=\sum_{j=0}^{N-1}\psi(b^jX).
\]
The two sums at bases \(m\) and \(n\) use **the same initial point** \(X\).

**Exact pair-covariance theorem.** For any positive integers \(A,B\), put \(g=\gcd(A,B)\). Then
\[
\int_0^1\psi(Ax)\psi(Bx)\,dx=
\begin{cases}
\dfrac{g^4}{48A^2B^2},& A/g\text{ and }B/g\text{ both odd},\\
0,&\text{otherwise}.
\end{cases}
\tag{1}
\]

**Cross-base dichotomy.** For any integers \(m,n\ge2\):

(a) If they are multiplicatively independent, meaning \(m^j\ne n^k\) for every positive pair \(j,k\), then \(\operatorname{Cov}(S_{m,N},S_{n,N})\) converges to a finite strictly positive number \(C_{m,n}\), with an exponentially small error as \(N\to\infty\).

(b) Otherwise there are unique coprime positive integers \(r,s\) and an integer \(t\ge2\) with \(m=t^r\) and \(n=t^s\), and
\[
\lim_{N\to\infty}\frac{\operatorname{Cov}(S_{m,N},S_{n,N})}{N}=
\begin{cases}
\dfrac{1}{48\max\{r,s\}},&t\text{ even},\\
\dfrac{t^2+1}{48\max\{r,s\}(t^2-1)},&t\text{ odd}.
\end{cases}
\tag{2}
\]
This is a sharp transition between bounded and linear covariance growth. In particular, the asymptotic cross-covariance divided by \(N\) detects multiplicative dependence of the two expanding maps.

## Assumptions and scope

All bases are positive integers at least two. The maps are \(T_b(x)=bx\bmod1\), with common Lebesgue-invariant initial distribution. The observable \(\psi\) is continuous, centered, and has variance \(1/48\). The word covariance always refers to integration over the single shared \(X\). Formula (2) is not asserted for independently seeded trajectories or arbitrary observables.

## Proof

**1. Fourier identity.** An absolutely and uniformly convergent cosine series for the centered triangular wave is
\[
\psi(x)=-\frac{2}{\pi^2}\sum_{\substack{q\ge1\\q\text{ odd}}}\frac{\cos(2\pi qx)}{q^2}.
\]
Orthogonality over \([0,1]\) implies that an integral of terms with frequencies \(qA\) and \(q'B\) is zero unless \(qA=q'B\), in which case the cosine-product integral is \(1/2\). Write \(A=g a\) and \(B=g b\) with \(\gcd(a,b)=1\). The frequency equation is \(qa=q'b\), so \(q=b\ell\), \(q'=a\ell\). Odd \(q,q'\) are possible precisely when \(a,b\) are both odd; then \(\ell\) is odd. Therefore
\[
\int_0^1\psi(Ax)\psi(Bx)\,dx=
\frac{2}{\pi^4a^2b^2}\sum_{\ell\ge1\,\mathrm{odd}}\ell^{-4}
=\frac{1}{48a^2b^2}=\frac{g^4}{48A^2B^2},
\]
using \(\sum_{\ell\ge1,\,\mathrm{odd}}\ell^{-4}=\pi^4/96\). This proves (1), including the vanishing case.

**2. Independent bases.** Fix the finite set \(\mathcal P\) of primes dividing \(mn\), and write \(u=(v_p(m))_{p\in\mathcal P}\), \(v=(v_p(n))_{p\in\mathcal P}\). In all cases, (1) gives the nonnegative bound
\[
0\le\operatorname{Cov}\bigl(\psi(m^jX),\psi(n^kX)\bigr)
\le\frac1{48}\exp\!\left(-2\sum_{p\in\mathcal P}|ju_p-kv_p|\log p\right).
\tag{3}
\]
If the bases are multiplicatively independent, \(u,v\) are linearly independent over \(\mathbb R\). Since the map \((a,b)\mapsto au-bv\) is injective and the first-quadrant unit simplex is compact, there is a constant \(c>0\) with \(\sum_p|ju_p-kv_p|\log p\ge c(j+k)\) for all \(j,k\ge0\). Thus the nonnegative double covariance series converges absolutely, and truncating to \(j,k<N\) has error \(O(e^{-2cN})\). The limit is positive because the \(j=k=0\) term equals \(1/48\).

**3. Dependent bases.** Prime factorization of the equality of some positive powers of \(m,n\) gives unique coprime \(r,s\ge1\) and integer \(t\ge2\) with \(m=t^r,n=t^s\). For \(j,k\ge0\), write \(d=rj-sk\). Formula (1) becomes
\[
\operatorname{Cov}(\psi(m^jX),\psi(n^kX))=
\frac{t^{-2|d|}}{48}
\begin{cases}1,&t\text{ odd, or }d=0,\\0,&t\text{ even and }d\ne0.\end{cases}
\tag{4}
\]
For fixed \(d\in\mathbb Z\), coprimality of \(r,s\) ensures that integer solutions to \(rj-sk=d\) form an arithmetic progression in \((j,k)\) with step \((s,r)\). Therefore the number \(M_N(d)\) in \(0\le j,k<N\) satisfies
\[
\frac{M_N(d)}N\longrightarrow\frac1{\max\{r,s\}},\qquad 0\le M_N(d)\le\frac{N}{\max\{r,s\}}+1.
\]
Sum (4) by \(d\). Dominated convergence, using \(\sum_{d\in\mathbb Z}t^{-2|d|}<\infty\), gives (2). If \(t\) is even only \(d=0\) contributes; if \(t\) is odd, the sum is \((t^2+1)/(t^2-1)\). Every constant displayed in (2) is positive.

## Verification

An independent exact-rational integration script, `tent_cross_cov_check.py`, partitions \([0,1]\) at all triangle-wave breakpoints and integrates the products using the exact Simpson identity for quadratic polynomials on each piece. All \(784\) ordered pairs \(1\le A,B\le28\) agreed exactly with (1). It also computes representative partial sum covariances at independent and dependent pairs, including bases \((2,3)\), \((2,4)\), \((3,9)\), \((3,5)\), \((6,12)\), \((4,8)\), and \((9,27)\). These finite checks do not prove the infinite statements; the proof above does.

To reproduce: `python3 tent_cross_cov_check.py` using Python's standard library only.

## Relationship to prior work

Ahn, *The signed error-sum function of tent-map expansions* (2026), Theorem 1.2, identifies an unsigned dyadic error sum with the Takagi series, introducing the same triangular building block. It does not discuss cross-base Birkhoff-sum covariance or arithmetic resonances. Tsuneda (2024) computes auto- and cross-correlations of binary threshold observables of individual one-dimensional chaotic maps; those binary functions, and its alternating-observation construction, are different from (1)-(2). Related published results on pair-collision fluctuations of expanding-circle orbits exhibit a multiplicative-dependence resonance in a different pair-counting statistic. Such a qualitative arithmetic analogy does not imply the exact triangular covariance formula or constants here.

## Limitations

This is a covariance classification, not a claim of independence of the two orbit processes, a joint central limit theorem, or ergodic limit distribution. For multiplicatively independent bases the finite positive limit is defined by a convergent arithmetic double series; no universal closed form for it is asserted. The theorem is Lebesgue-stationary and assumes a shared initial coordinate. Historical priority remains subject to broader independent review, particularly for classical Fourier treatments of lacunary series.

## References

1. M. W. Ahn, *The signed error-sum function of tent-map expansions*, arXiv:2611.01955v1, posted 2026-11-01, Theorem 1.2. https://arxiv.org/abs/2611.01955
2. A. Tsuneda, *Auto-Correlation Functions of Chaotic Binary Sequences Obtained by Alternating Two Binary Functions*, Dynamics **4** (2024), 272–286, https://doi.org/10.3390/dynamics4020016.
3. *Arithmetic resonance dichotomy and logarithmic correction for two-orbit collision fluctuations*, accessible published research summary (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-arithmetic-resonance-dichotomy-and-logarithmic-correction-for-tw--b00fe889ce12. (Related statistic, not an independent verification of this theorem.)
