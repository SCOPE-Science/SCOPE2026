# An explicit upper bound of \(157/200\) for a divisor-sum comparison density

## Finding

Let \(\sigma^*(n)\) be the sum of the unitary divisors of a positive integer \(n\) and \(\sigma^{(e)}(n)\) the sum of its exponential divisors. Let
\[
\delta=\lim_{X\to\infty}\frac1X\#\{1\le n\le X:\sigma^*(n)>\sigma^{(e)}(n)\}.
\]
The existence of this density is established in the source literature. The following strict, unconditional upper bound holds:
\[
\boxed{\delta<\frac{157}{200}=0.785.}
\]
In particular the integers satisfying the *reverse strict inequality* \(\sigma^*(n)<\sigma^{(e)}(n)\) have lower asymptotic density greater than \(43/200=0.215\).

## Assumptions and scope

All integers are positive; \(\sigma^*(1)=\sigma^{(e)}(1)=1\). If \(n=\prod_p p^{a_p}\), both functions are multiplicative and their local factors are
\[
\sigma^*(p^a)=1+p^a,\qquad \sigma^{(e)}(p^a)=\sum_{d\mid a}p^d\quad(a\ge1).
\]
The local ratio is \(\rho_p(0)=1\) and \(\rho_p(a)=(1+p^a)/(\sum_{d\mid a}p^d)\) when \(a\ge1\). For \(a\ge2\), \(\rho_p(a)<1\). The upper bound applies to the density over all positive integers, not a restricted arithmetic progression or a finite sample.

## Proof

**1. A finite exact prime-exponent certificate.** Set \(B=503\), \(K=4000\), and \(h=(K+1)/K=4001/4000\). For each prime \(p\le B\), set
\[
E_p=\begin{cases}
16,&p\le3,\\
10,&3<p\le7,\\
7,&7<p\le17,\\
5,&17<p\le47,\\
3,&47<p\le503.
\end{cases}
\]
For \(0\le a<E_p\), define \(j_p(a)\) to be the **least integer** \(j\) such that \(\rho_p(a)\le h^j\). For \(a\ge E_p\), define \(j_p(a)=0\), which is a valid upper bound because \(E_p\ge3\) and \(\rho_p(a)<1\). Put
\[
J(n)=\sum_{p\le503}j_p(v_p(n)),\qquad
G=\{n\ge1:J(n)\le-41\}.
\]
The membership of \(n\) in \(G\) depends only on its residues modulo \(M=\prod_{p\le503}p^{E_p}\). The exact finite calculation in `verify_density.py` proves
\[
\boxed{\operatorname{dens}(G)>\frac{216}{1000}.}\tag{1}
\]
For explicit reproducibility, the script computes the exact integer numerator and denominator of this proportion and verifies \(1000\,\#G_M>216M\). For each prime, the number of residues modulo \(p^{E_p}\) with valuation \(a<E_p\) equals \((p-1)p^{E_p-a-1}\); the single remaining residue has valuation at least \(E_p\). The script convolves these integer counts over the \(96\) primes, with all logarithmic-bin comparisons checked by integer exponentiation; floating-point approximations serve only as starting guesses for the exact integer searches.

For \(n\in G\), the product of the local ratios at primes not exceeding \(503\) satisfies
\[
\log\prod_{p\le503}\rho_p(v_p(n))\le J(n)\log h
\le-41\log(1+1/4000)\le-\frac{41}{4001}<-\frac1{100}.
\tag{2}
\]
The penultimate inequality uses \(\log(1+u)\ge u/(1+u)\) for \(u>0\).

**2. A uniform upper tail bound, without independence assumptions for finite integers.** For each \(n\), the primes \(p>503\) contribute at most
\[
\log\prod_{p>503}\rho_p(v_p(n))\le S(n):=\sum_{\substack{p>503\\p\mid n}}\frac1p,
\tag{3}
\]
since at exponent one \(\log(1+1/p)\le1/p\), and at every larger exponent the local log-ratio is negative. For any finite \(X\), expand the nonnegative product
\[
\exp(1400S(n))=\prod_{503<p\le X}\left[1+(e^{1400/p}-1){\bf1}_{p\mid n}\right].
\]
Each squarefree divisor \(d\) appears in at most \(X/d\) integers up to \(X\). Consequently, **without treating divisibility indicators as independent**, for every \(X\ge1\),
\[
\frac1X\sum_{n\le X}e^{1400S(n)}
\le\prod_{p>503}\left(1+\frac{e^{1400/p}-1}{p}\right)
\le\exp\left(\sum_{m>503}\frac{e^{1400/m}-1}{m}\right).
\]
The summand decreases with \(m\), so the last exponent does not exceed
\[
F\left(\frac{1400}{503}\right),\qquad
F(z):=\int_0^z\frac{e^u-1}{u}\,du
=\sum_{j\ge1}\frac{z^j}{j\,j!}.
\]
The exact rational series bound in the verifier establishes \(F(1400/503)<7\): it sums through \(j=30\) and bounds the rest by a geometric series. The same script proves \(e^7>1000\) using a finite Taylor sum. Markov's inequality therefore gives the **uniform** estimate
\[
\frac1X\#\{n\le X:S(n)\ge1/100\}<e^{-7}<\frac1{1000}.
\tag{4}
\]

**3. Comparison and density.** Every \(n\in G\) with \(S(n)<1/100\) satisfies \(\sigma^*(n)<\sigma^{(e)}(n)\) by (2)–(3). Thus (1) and (4) imply
\[
\liminf_{X\to\infty}\frac1X\#\{n\le X:\sigma^*(n)<\sigma^{(e)}(n)\}
>\frac{216}{1000}-\frac1{1000}=\frac{43}{200}.
\]
Since the strict comparison sets are disjoint, \(\delta\le1-\liminf\operatorname{freq}(\sigma^*<\sigma^{(e)})<157/200\). This completes the proof.

## Verification

Run `python3 verify_density.py` using Python's standard library. It checks the exact local rational bins, the prime-exponent convolution, the strict proportion \(>216/1000\), the rational upper bound \(F(1400/503)<7\), and the finite Taylor certificate \(e^7>1000\). The reported numerical proportion is approximately \(0.2161377019267721\); **the proof uses only the integer inequality**. No search over all integers is claimed. The exponential tail argument is valid for every finite \(X\), then passes to the limit.

## Relationship to prior work

Trudgian's 2013 preprint introduces precisely the density \(\delta\), states that it exists, proves the squarefree lower bound \(6/\pi^2\), and reports a finite-range numerical estimate of about \(0.778307\) up to \(10^9\); it does not prove an upper bound below one. A separate, earlier reported prime-exponent construction gives a rigorous lower bound of approximately \(0.770292\), which does **not** imply the present upper bound. Minculete gives pointwise inequalities for exponential-divisor sums rather than a density upper bound for this comparison. Lelechenko develops mean-value tools for related exponential-divisor functions, but not the stated strict comparison density estimate. No equivalent explicit upper bound was found in the inspected sources; that is not a proof of historical novelty.

## Limitations

The value of \(\delta\) is **not** determined exactly. The bound \(0.785\) is not asserted optimal. The finite counting certificate is computer-assisted but consists of deterministic integer operations with exhaustive prime-exponent categories; the infinite tail bound and reduction to the density are analytic. A matching or stronger previously published upper bound outside the inspected material could alter priority; independent validation has not occurred.

## References

1. T. Trudgian, *The sum of the unitary divisor function*, arXiv:1312.4615, first submitted 17 December 2013, especially §4. https://arxiv.org/abs/1312.4615
2. N. Minculete, *On certain inequalities about arithmetic functions which use the exponential divisors*, International Journal of Number Theory 8 (2012), 1527–1535, DOI:10.1142/S1793042112500923. https://www.researchgate.net/publication/267141042_ON_CERTAIN_INEQUALITIES_ABOUT_ARITHMETIC_FUNCTIONS_WHICH_USE_THE_EXPONENTIAL_DIVISORS
3. A. V. Lelechenko, *Exponential divisor functions*, arXiv:1307.3683, first submitted 13 July 2013. https://arxiv.org/abs/1307.3683
