# Sharp three-gap laws and unavoidable \(k\)-full integers between four successive powers

## Finding

Let \(k\ge2\) be fixed. Let \(h_k(n)\) count the \(k\)-full positive integers strictly between \(n^k\) and \((n+1)^k\), where \(k\)-full means that every prime divisor appears to exponent at least \(k\). For nonnegative integers \(a,b,c\), the density
\[
d_k(a,b,c)=\lim_{X\to\infty}\frac1X\#\{1\le n\le X:(h_k(n),h_k(n+1),h_k(n+2))=(a,b,c)\}
\]
exists.

Define the set of *nontrivial radical scales*
\[
\Lambda_k=\left\{\left(\prod_{j=1}^{k-1}b_j^{k+j}\right)^{1/k}:b_j\in\mathbb Z_{\ge1},\ \prod_{j=1}^{k-1}b_j\ge2,\ \prod_{j=1}^{k-1}b_j\text{ is squarefree}\right\}.
\]
For \(\lambda\in\Lambda_k\), put \(p_\lambda=\lambda^{-1}\) and \(q_\lambda=(3\lambda^{-1}-1)_+\), where \((x)_+=\max\{x,0\}\). The exact joint probability generating function is
\[
\boxed{\sum_{a,b,c\ge0}d_k(a,b,c)u^av^bw^c
=\prod_{\lambda\in\Lambda_k}\left(1+\frac{u+v+w-3}{\lambda}+\left(\frac3\lambda-1\right)_+(u-1)(w-1)\right).}
\]
The product converges absolutely and uniformly when \(|u|,|v|,|w|\le1\). The last term, representing simultaneous contributions from the first and third windows by the *same radical scale*, is nonzero precisely at scales \(\lambda<3\).

Let
\[
J_k=\left\lfloor k\log_2\left(\frac32\right)\right\rfloor.
\]
Then for **every** integer \(n\ge1\),
\[
\boxed{h_k(n)+h_k(n+1)+h_k(n+2)\ge J_k.}
\]
This is a sharp positive-density lower bound: the exact support of the limiting distribution consists of **all** triples \((a,b,c)\in\mathbb Z_{\ge0}^3\) such that \(a+b+c\ge J_k\), and \(d_k(a,b,c)>0\) for each such triple. Equivalently, \(d_k(a,b,c)=0\) if and only if \(a+b+c<J_k\).

For a random vector \((H_0,H_1,H_2)\) with the limiting law, write \(C_{01}=\operatorname{Cov}(H_0,H_1)\) and \(C_{02}=\operatorname{Cov}(H_0,H_2)\). Then
\[
C_{01}=-\sum_{\lambda\in\Lambda_k}\frac1{\lambda^2},\qquad
C_{02}=C_{01}+\sum_{j=1}^{J_k}\left(\frac3{2^{1+j/k}}-1\right),
\]
so the strictly positive difference satisfies
\[
\boxed{C_{02}-C_{01}=\frac{\frac12-\log(3/2)}{\log2}\,k+O(1)\quad(k\to\infty).}
\]
(The logarithm without a subscript is natural.) These are covariances of the **limiting probability distribution**; no empirical second-moment convergence rate is asserted.

## Assumptions and scope

The parameter \(k\) is any fixed integer at least two; \(n\) ranges over positive integers; intervals are open. Perfect \(k\)-th powers occur only at endpoints, so including or excluding them from the definition of \(k\)-full does not change \(h_k\). Limits are natural densities as \(X\to\infty\) with \(k\) fixed. The \(O(1)\) in the final display is absolute as \(k\to\infty\).

The standard unique factorization of a \(k\)-full integer as \(m=A^k\prod_{j=1}^{k-1}b_j^{k+j}\), with squarefree product of the \(b_j\), underlies the radical decomposition. In particular, each nonendpoint \(k\)-full number corresponds uniquely to one \(\lambda\in\Lambda_k\) and one integer \(A\ge1\).

## Proof

**1. Radical decomposition and convergence.** The unique factorization above shows that a nonendpoint \(k\)-full number in the \(j\)-th window is of the form \((A\lambda)^k\), with \(n+j<A\lambda<n+j+1\). Every \(\lambda\in\Lambda_k\) is strictly larger than two. The convergence
\[
\sum_{\lambda\in\Lambda_k}\lambda^{-1}
\le\prod_{j=1}^{k-1}\zeta(1+j/k)-1<\infty
\]
follows by discarding the squarefree restriction. Distinct radical scales give disjoint arithmetic families by uniqueness.

**2. Exact local three-window law.** Fix one \(\lambda\), put \(p=1/\lambda\in(0,1/2)\), and let \(x=\{n/\lambda\}\). The indicator of a contribution in window \(j\in\{0,1,2\}\) is
\[
I_j(x)=\lfloor x+(j+1)p\rfloor-\lfloor x+jp\rfloor.
\]
Since \(p<1/2\), adjacent indicators cannot both equal one. Furthermore, the first and third indicators can both equal one exactly when \(3p>1\), in which case the intersection has length \(q=(3p-1)_+\). Each marginal event has measure \(p\); thus the only patterns with positive measure are \((0,0,0)\), \((1,0,0)\), \((0,1,0)\), \((0,0,1)\), and \((1,0,1)\), with respective probabilities
\[
1-3p+q,\quad p-q,\quad p,\quad p-q,\quad q.
\]
For \(p>1/3\), the first probability vanishes, while each of the three singleton probabilities stays strictly positive because \(p<1/2\). Encoding these five outcomes yields exactly
\[
1+p(u+v+w-3)+q(u-1)(w-1).
\]
There are no boundary exceptions for positive integer \(n\) because \(\lambda\) is irrational.

**3. Finite independence.** For distinct \(\lambda_1,\ldots,\lambda_s\in\Lambda_k\), the real numbers \(1,\lambda_1^{-1},\ldots,\lambda_s^{-1}\) are linearly independent over \(\mathbb Q\): this is Lemma 2, established via Besicovitch's radical-independence theorem, in Narumi–Tachiya (2025). The Kronecker–Weyl theorem therefore makes the vector \((\{n/\lambda_i\})_{i=1}^s\) uniformly distributed on the \(s\)-torus. Thus the local three-window patterns are asymptotically independent for every finite set of scales, giving the corresponding finite product generating function.

**4. Passing to all scales.** For a scale \(\lambda\) and a positive integer \(A\) such that \(A\lambda<X+3\), there are at most three positive integers \(n\le X\) whose three-window union contains \(A\lambda\). Consequently, for any subset \(T\subset\Lambda_k\),
\[
\limsup_{X\to\infty}\frac1X\#\{n\le X:\text{some }\lambda\in T\text{ contributes to one of the three windows}\}
\le3\sum_{\lambda\in T}\lambda^{-1}.
\]
Taking \(T\) to be the complement of a growing finite set gives a tail tending to zero. Hence each three-count cylinder has a natural density, and its generating function is the stated infinite product. The product converges uniformly on the closed unit tridisc, since its factors differ from one by \(O(1/\lambda)\) there. This also establishes that the coefficients sum to one.

**5. Classifying unavoidable contributors.** If \(\lambda<3\), its defining squarefree factor must be a single prime two: a prime at least three would give \(\lambda\ge3^{1+1/k}>3\), and two distinct primes give \(\lambda>3\). Thus exactly the scales
\[
\lambda_j=2^{1+j/k},\qquad1\le j\le k-1,\quad j<k\log_2(3/2)
\]
are below three. There are exactly \(J_k\) of them because \(\log_2(3/2)\) is irrational (otherwise a positive power of three would equal a power of two). There is no scale equal to three: its \(k\)-th power would be a perfect \(k\)-th power, contradicting the nontrivial radical decomposition. Every interval \((n,n+3)\) contains some positive multiple of each \(\lambda_j\), since \(\lambda_j<3\); the corresponding distinct \(k\)-full integers lie in the union of the three windows. This proves the pointwise lower bound.

For a prescribed triple with total at least \(J_k\), distribute the \(J_k\) exceptional scales among its three coordinates as singleton outcomes. All three singleton choices have positive probability, as shown in step 2. Use finitely many distinct scales larger than three, assigning each exactly one contribution to meet the remaining required counts; infinitely many such scales exist. Require every other scale larger than three to contribute nothing. The latter event has strictly positive product probability
\[
\prod_{\lambda>3,\,\lambda\text{ not assigned}}(1-3/\lambda)>0,
\]
because \(\sum_{\lambda>3}\lambda^{-1}<\infty\) and all factors are positive. Finite independence and the tail bound from step 4 imply that each prescribed triple has strictly positive limiting density. Triples with smaller total are excluded for every \(n\), proving exact support and sharpness.

**6. Endpoint dependence.** Under the independent-factor limiting law, every window has mean \(\sum_\lambda p_\lambda\), and both adjacent pairs have no common contributions from the same scale. For any \(\lambda\), the local covariance of the first two windows is \(-p_\lambda^2\); that of the first and third is \(q_\lambda-p_\lambda^2\). Summing these absolutely convergent series gives the stated covariances and their difference. Since the only scales with positive \(q_\lambda\) are \(\lambda_j\) above, the difference is their explicit finite sum. Finally, the summand is a Lipschitz function of \(j/k\), and its Riemann sum over \((0,\log_2(3/2))\) gives
\[
\frac{C_{02}-C_{01}}k\longrightarrow
\int_0^{\log_2(3/2)}\left(\frac32\,2^{-t}-1\right)\,dt
=\frac{\frac12-\log(3/2)}{\log2}>0,
\]
with absolute error \(O(1)\) by elementary Riemann-sum estimates. This completes the proof.

## Verification

`triple_checker.py` independently constructs the three-window count vectors for \(k=2\) through \(n=125\) and \(k=3\) through \(n=48\) both by direct integer prime-exponent sieving and by the unique radical decomposition; all 173 compared triples agree. It samples 100,000 phase cells per scale to compare the five local pattern probabilities for \(k\in\{2,3,4,5,8,12\}\), including scales above and below three, and checks the asymptotic covariance-difference constant for \(k=32,128,512,2048\). `empirical.py` provides a larger independent square-full count check over \(150000\) consecutive triple windows. All computations are finite checks of the arithmetic and local formulas; the infinite density and support assertions follow from the proof rather than from exhaustive computation.

Reproduce with standard Python 3, no third-party packages:

```bash
python3 triple_checker.py
python3 empirical.py
```

## Relationship to prior work

Narumi and Tachiya (arXiv:2512.07438, publicly posted December 8, 2025), Theorems 1–2 and Section 6, prove all fixed two-window densities and the bivariate generating function \(\prod_{\lambda\in\Lambda_k}(1+(u+v-2)/\lambda)\), and cite earlier one-window work of Shiu (1980) and Xiong–Zaharescu (2011). They also note the qualitative impossibility of four consecutive \(k\)-th powers being successive \(k\)-full numbers. These results do not supply the present *three*-window joint product, the nonzero same-scale endpoint-pair term, the exact support boundary \(J_k\), or the sharp endpoint covariance difference. Their Lemma 2 and convergence estimate are explicitly used as mathematical ingredients here. The three-window result is not an assumption-free generalization to arbitrarily many windows; its local pattern classification relies on \(2<\lambda\) and a window length of exactly three.

## Limitations

No rate of convergence in \(X\) for the triple densities is claimed. The full counts are unbounded random variables, and convergence of their empirical mixed second moments is **not** asserted; covariance formulas concern the limiting distribution. The exact support result is a positive-natural-density assertion but does not locate the first integer realizing each triple. Prior work might implicitly contain a general multicylinder formula, and older material not fully accessible has not been exhaustively ruled out. The theorem uses the cited radical-independence result and standard equidistribution theory, rather than providing new proofs of those classical inputs.

## References

1. S. Narumi and Y. Tachiya, *On the number of \(k\)-full integers between three successive \(k\)-th powers*, arXiv:2512.07438, initial posting December 8, 2025, revised February 18, 2026. https://arxiv.org/abs/2512.07438 ; full text https://arxiv.org/html/2512.07438v2 .
2. A. S. Besicovitch, *On the linear independence of fractional powers of integers*, J. London Math. Soc. 15 (1940), 3–6 (radical-independence input as applied and proved in reference 1, Lemma 2).
3. M. Xiong and A. Zaharescu, *\(k\)-full integers between successive \(k\)-th powers*, Indag. Math. 22 (2011), 77–86 (single-window generating function, as cited in reference 1).
4. P. Shiu, *On the number of square-full integers between successive squares*, Mathematika 27 (1980), 171–178, https://doi.org/10.1112/S0025579300010056 (one-window predecessor).
