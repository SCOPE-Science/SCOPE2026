# A log-periodic counting law for two-prime primitive abundant numbers
## Finding
Let \(P_2(X)\) count the positive integers \(n\le X\) that are primitive abundant in the strict sense—\(n\) is abundant and every proper divisor is deficient—and that have exactly two distinct prime factors. For \(X\ge16\), define
\[
m=\lfloor\log_4 X\rfloor,\qquad y=2^m,\qquad r=\frac{X}{4^m}\in[1,4),
\]
and
\[
U=\min\left\{\frac{X}{y},2y\right\}.
\]
Let \(\mathcal M(U)\) denote the number of Mersenne primes \(2^j-1\) with \(j\ge3\) and \(2^j-1\le U\). Then the exact counting identity is
\[
P_2(X)=\pi(U)-2-\mathcal M(U).
\]
Consequently,
\[
\frac{P_2(X)\log X}{\sqrt X}=F(r)+o(1)
\]
as \(X\to\infty\), where
\[
F(r)=
\begin{cases}
2\sqrt r,&1\le r\le2,\\
4/\sqrt r,&2\le r<4.
\end{cases}
\]
The error is uniform over the phase \(r\in[1,4)\). Hence
\[
\liminf_{X\to\infty}\frac{P_2(X)\log X}{\sqrt X}=2,
\qquad
\limsup_{X\to\infty}\frac{P_2(X)\log X}{\sqrt X}=2\sqrt2.
\]
In particular, no constant \(C\) satisfies \(P_2(X)\sim C\sqrt X/\log X\).

## Assumptions and scope
Here \(\sigma(n)\) is the sum of the positive divisors of \(n\). A number is abundant, perfect, or deficient according as \(\sigma(n)\) is greater than, equal to, or less than \(2n\). “Primitive abundant” uses the strict historical convention relevant here: an abundant number all of whose proper divisors are deficient. This differs from the weaker convention that merely forbids abundant proper divisors, because the weaker convention can allow proper perfect divisors.

The symbol \(\omega(n)\) denotes the number of distinct prime factors. The counting function \(P_2(X)\) restricts to \(\omega(n)=2\). The logarithm in the asymptotic normalization is the natural logarithm.

The factor classification used below is classical in scope: Dickson's 1913 work covers all even primitive abundant numbers with at most three distinct prime factors, as explicitly recorded by later full-text literature. The contribution assessed here is the exact counting identity and its phase-dependent asymptotic, not a novelty claim for the underlying classification.

## Proof
First, a primitive abundant number with exactly two distinct prime factors cannot be odd. Indeed, if its prime support is \(p<q\) with both primes odd, then for any positive exponents
\[
\frac{\sigma(n)}{n}<\frac{p}{p-1}\frac{q}{q-1}
\le \frac32\frac54=\frac{15}{8}<2,
\]
so \(n\) is deficient.

Thus write
\[
n=2^a p^b,
\]
where \(p\) is odd and \(a,b\ge1\). Put \(B=2^{a+1}\). Directly from the divisor-sum formula,
\[
\sigma(2^a p^b)>2\cdot2^a p^b
\quad\Longleftrightarrow\quad
(B-p)p^b>B-1. \tag{1}
\]
Since a strict primitive abundant number has \(n/p\) deficient,
\[
(B-p)p^{b-1}<B-1. \tag{2}
\]
Equation (1) forces \(B-p>0\). If \(b\ge2\), set \(d=B-p\ge1\). From (2),
\[
dp\le d p^{b-1}<B-1=p+d-1,
\]
which is equivalent to
\[
(d-1)(p-1)<0,
\]
impossible. Hence \(b=1\).

For \(b=1\), (1) becomes
\[
(p-1)(B-p-1)>0,
\]
so abundance is equivalent to
\[
p<2^{a+1}-1. \tag{3}
\]
The maximal proper divisor \(n/2=2^{a-1}p\) is deficient exactly when
\[
p>2^a-1.
\]
Because \(p\) is odd and \(2^a\) is even, this is equivalent to \(p>2^a\). The other maximal proper divisor, \(n/p=2^a\), is always deficient. Since abundancy is nondecreasing under divisibility, every divisor of either maximal proper divisor is deficient as well. Therefore
\[
n\text{ is strict primitive abundant with }\omega(n)=2
\quad\Longleftrightarrow\quad
n=2^a p,
\]
with
\[
a\ge2,\qquad 2^a<p<2^{a+1}-1. \tag{4}
\]

Condition (4) gives a bijection from odd primes \(p\ge5\) that are not Mersenne primes to these primitive abundant numbers: take
\[
a=\lfloor\log_2 p\rfloor,
\qquad n=2^a p.
\]
The sole prime that can fail the strict upper inequality in its dyadic block is the endpoint \(p=2^{a+1}-1\), precisely a Mersenne prime.

Now fix \(X\ge16\), let \(m,y,r\) be as in the statement, and consider the dyadic exponent blocks in (4). Every block with \(a<m\) is completely counted because its members satisfy
\[
n<2\cdot4^a\le \frac{4^m}{2}\le X.
\]
No block with \(a>m\) contributes because then \(n>4^{m+1}>X\). In the current block \(a=m\), the size condition is exactly \(p\le X/y\), while the structural upper edge is \(p<2y-1\). Thus all eligible primes are exactly the primes at most
\[
U=\min\{X/y,2y\},
\]
except \(2\), \(3\), and the Mersenne primes. This proves the exact identity
\[
P_2(X)=\pi(U)-2-\mathcal M(U).
\]

Since \(\mathcal M(U)\le \log_2 U\), this correction is \(O(\log X)\). Also \(U=y\min\{r,2\}\) and \(y\to\infty\). The prime number theorem, uniformly for fixed multiplicative factors between \(1\) and \(2\), gives
\[
\pi(U)=\frac{U}{\log y}(1+o(1)).
\]
Moreover,
\[
\log X=2\log y+O(1),
\qquad
\sqrt X=y\sqrt r.
\]
Therefore
\[
\frac{P_2(X)\log X}{\sqrt X}
=rac{2\min\{r,2\}}{\sqrt r}+o(1),
\]
which is exactly the stated piecewise function \(F\). Its minimum on the phase interval is \(2\), approached at \(r=1\) and \(r\to4^-\), while its maximum is \(2\sqrt2\) at \(r=2\). This proves the liminf and limsup.

## Verification
The included standalone checker uses exact integer arithmetic and no external packages. It computes divisor sums for every integer up to \(500000\), examines every integer with exactly two distinct prime factors, tests the strict definition by checking all proper divisors, and compares the result with (4). It checks \(150785\) two-prime-support integers and finds \(159\) strict primitive abundant numbers, with no mismatch.

The checker also verifies the exact phase-count identity on \(49\) values spanning seven dyadic phases. Its output is:

`VERIFY_OK bound=500000 support_two_checked=150785 two_prime_pan=159 phase_identities=49 first=[20, 88, 104, 272, 304, 368, 464, 1184, 1312, 1376, 1504, 1696]`

The finite computation is corroborative only. It does not prove the asymptotic statement; the infinite argument is the exact classification, exact counting identity, the bound \(\mathcal M(U)=O(\log U)\), and the prime number theorem.

## Relationship to prior work
Dickson's 1913 paper “Even Abundant Numbers” is the historical source for the even primitive-abundant classification program. A later full-text treatment by Amato, Hasler, Melfi, and Parton explicitly states that Dickson found all even primitive abundant numbers with \(\omega\le3\). Their paper also gives a modern structural criterion for primitive abundance. Thus the two-prime factor classification used in the proof is treated as prior-covered, not as the new result.

Ivić and Avidon study the global counting function of all primitive abundant numbers. Those estimates concern the full family and do not determine the counting function after fixing \(\omega(n)=2\). OEIS A071395 tabulates strict primitive abundant numbers, A133814 records the least primitive abundant or perfect number at a prescribed power of \(2\), and A306986 counts all strict primitive abundant numbers below powers of \(10\). These tables are consistent with the classification but do not state the exact identity with \(\pi(U)\) and Mersenne-prime correction, nor the phase function \(F\).

Focused searches were made for the exact identity, its non-Mersenne-prime formulation, a two-prime-support asymptotic, and the liminf/limsup constants. No equivalent statement or stronger fixed-support result was located. The closest database results concern different divisor-sum properties on two-prime supports and do not imply this claim.

## Limitations
The theorem is restricted to the strict primitive-abundant convention and to exactly two distinct prime factors. It does not estimate the much larger family with three or more distinct prime factors, and it does not improve global bounds for all primitive abundant numbers.

The historical Dickson article was verified bibliographically and its classification scope was checked through a later full-text source, but the complete 1913 article text was not available line-by-line in the inspected open sources. This leaves a residual possibility that an equivalent counting reformulation appeared in older literature under different language. Focused modern literature, database, and equivalence searches did not locate such a statement.

## References
1. L. E. Dickson, “Even Abundant Numbers,” American Journal of Mathematics 35(4) (1913), 423–426, DOI 10.2307/2370406; issue date 1 October 1913.
2. G. Amato, M. F. Hasler, G. Melfi, and M. Parton, “Primitive abundant and weird numbers with many prime factors,” arXiv:1802.07178; Journal of Number Theory 201 (2019), 436–459.
3. A. Ivić, “The distribution of primitive abundant numbers,” Studia Scientiarum Mathematicarum Hungarica 20 (1985), 183–187.
4. M. R. Avidon, “On the distribution of primitive abundant numbers,” Acta Arithmetica 77(2) (1996), 195–205, DOI 10.4064/aa-77-2-195-205.
5. OEIS A071395, “Primitive abundant numbers”; OEIS A133814, “Smallest primitive abundant number or perfect number with \(2^n\) as a factor”; OEIS A306986, “Number of primitive abundant numbers less than \(10^n\).”
