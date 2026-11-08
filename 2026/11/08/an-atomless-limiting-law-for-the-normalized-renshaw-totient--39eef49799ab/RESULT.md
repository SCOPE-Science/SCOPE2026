# An atomless limiting law for the normalized Renshaw totient

## Finding

For integers \(n\ge1\), let \(T(1)=0\) and let \(T(n)\) for \(n>1\) count odd integers \(1\le x\le n\) for which both \(\gcd(x,n)=1\) and \(\gcd((x-1)/2,n)=1\). This is the totient introduced by Renshaw [1].

For each odd prime \(p\), let \(B_p\) be independent Bernoulli variables satisfying \(\Pr(B_p=1)=1/p\). Set
\[
P=\prod_{p\ge3}\left(1-\frac2p\right)^{B_p},
\qquad
\Pr(J=1/2)=\Pr(J=1/4)=\frac12,
\]
where \(J\) is independent of all \(B_p\). The infinite product is almost surely positive. Then, with uniform averaging over positive integers, 
\[
\boxed{\frac{T(n)}n\ \Longrightarrow\ W=JP.}
\]
Precisely, for every bounded continuous \(f:[0,1]\to\mathbb R\),
\[
\lim_{X\to\infty}\frac1{\lfloor X\rfloor}\sum_{1\le n\le X}f\left(\frac{T(n)}n\right)=\mathbb E f(W).
\]
The law of \(W\) is **atomless** and has **full topological support** \([0,1/2]\). For every real \(s>0\), all its positive moments are explicit:
\[
\boxed{\lim_{X\to\infty}\frac1{\lfloor X\rfloor}\sum_{1\le n\le X}\left(\frac{T(n)}n\right)^s
=\frac{2^{-s}+4^{-s}}2\prod_{p\ge3}\left(1+\frac{(1-2/p)^s-1}{p}\right).}
\]
In particular the limiting first and second moments are, respectively,
\[
\frac38\prod_{p\ge3}\left(1-\frac2{p^2}\right),\qquad
\frac5{32}\prod_{p\ge3}\left(1-\frac4{p^2}+\frac4{p^3}\right).
\]
These are limits over all integers, not merely over odd integers or prime arguments.

## Assumptions and scope

The input is an integer \(n\ge1\). Write \(n=2^e m\), where \(e\ge0\) and \(m\) is odd, and define
\[
R(m)=\prod_{p\mid m,\ p\text{ odd}}\left(1-\frac2p\right),\quad R(1)=1,
\quad\omega(m)=\#\{p:p\mid m\}.
\]
All expectations refer to the independent variables defined above, not to an assumption that divisibility by infinitely many primes is independent for a fixed integer. The finite-prime approximation and its limiting passage are proved below. The first-public-source date concerns Renshaw's source, not a publication claim for this theorem.

## Proof

**1. Reduction to a strongly multiplicative product.** Put \(x=2k+1\). For every odd prime \(p\mid m\), the two coprimality conditions say that \(k\) avoids the two distinct classes \(0\) and \(-2^{-1}\pmod p\). The Chinese remainder theorem gives \(mR(m)\) admissible classes modulo \(m\). If \(e=0\), then \(0\le k\le(m-1)/2\). Inclusion-exclusion over the two forbidden classes at each of the \(\omega(m)\) primes expresses the count through at most \(3^{\omega(m)}\) residue-class counts. Each progression contributes its interval length divided by its modulus, with absolute error at most \(1\). Thus
\[
T(m)=\frac{m+1}{2}R(m)+O\left(3^{\omega(m)}\right).
\]
If \(e=1\), then \(0\le k<m\); additionally \(k\) must be odd. Applying the same inclusion-exclusion with the additional odd residue modulo \(2\) gives
\[
T(2m)=\frac m2R(m)+O\left(3^{\omega(m)}\right).
\]
For \(e\ge2\), the admissible \(k\) are periodic with period \(2m\). Exactly \(mR(m)\) admissible residues occur in that period, and \(0\le k<2^{e-1}m\) consists of exactly \(2^{e-2}\) periods. Consequently,
\[
T(2^e m)=2^{e-2}mR(m)\qquad(e\ge2).
\]
The exceptional conventions \(T(1)=T(2)=0\) affect only finitely many inputs. With
\[
c(n)=\begin{cases}\frac12,&n\text{ odd},\\\frac14,&n\text{ even},\end{cases}
\]
we obtain uniformly
\[
\frac{T(n)}n=c(n)R(m)+O\left(\frac{1+3^{\omega(m)}}n\right).
\]
For every \(\varepsilon>0\), \(3^{\omega(m)}\ll_\varepsilon m^\varepsilon\): separate the finitely many primes \(p<3^{1/\varepsilon}\), and use \(3\le p^\varepsilon\) for all remaining primes. Thus the error tends to zero as \(n\to\infty\). The values \(T(n)/n\) always lie in \([0,1/2]\), since at most half the integers in the defining range are odd.

**2. Convergence of the arithmetic product.** Let \(U_X\) be uniformly distributed on \(\{1,\ldots,\lfloor X\rfloor\}\). For a fixed finite set of odd primes \(\mathcal P\), the vector consisting of the parity of \(U_X\) and the divisibility indicators \((\mathbf1_{p\mid U_X})_{p\in\mathcal P}\) converges, by counting residue classes modulo \(2\prod_{p\in\mathcal P}p\), to independent coordinates: a fair parity bit and Bernoulli variables of success probabilities \(1/p\). Truncating \(R\) to \(p\le y\) therefore yields the corresponding finite approximation to \(W\).

To remove the truncation, set \(a_p=-\log(1-2/p)\). For \(y\ge5\) one has \(a_p\ll1/p\), so
\[
\mathbb E\sum_{\substack{p>y\\p\mid U_X}}a_p
=\sum_{y<p\le X}a_p\frac{\lfloor X/p\rfloor}{\lfloor X\rfloor}
\le\sum_{p>y}\frac{a_p}{p}\ll\sum_{k>y}\frac1{k^2}\longrightarrow0
\]
(as \(X\ge2\); integer and noninteger endpoints are immaterial). The same estimate applies to the Bernoulli model. In particular \(\sum_{p\ge3}B_pa_p<\infty\) almost surely, so \(P=\exp(-\sum B_pa_p)>0\) almost surely. Truncated products approximate the originals uniformly in probability, and the standard bounded-continuous-function approximation proves weak convergence. Combining this with Step 1 gives the asserted law.

**3. Moments.** Since both \(T(n)/n\) and \(W\) lie in the compact interval \([0,1/2]\), weak convergence implies convergence for the continuous function \(t\mapsto t^s\) whenever \(s>0\). Independence gives
\[
\mathbb E W^s=\mathbb E J^s\,\prod_{p\ge3}\mathbb E(1-2/p)^{sB_p},
\]
which is the stated convergent Euler product. Convergence of the factors follows from \((1-2/p)^s-1=O_s(1/p)\).

**4. Absence of atoms.** For any finite initial collection of odd primes, distinct choices of the exponents \(b_p\in\{0,1\}\) yield distinct rational products \(\prod(p-2)^{b_p}/p^{b_p}\). Indeed, if two products were equal, cancel common factors and let \(p\) be the largest prime appearing on exactly one side. Its denominator supplies a negative \(p\)-adic valuation; every factor from a smaller prime has numerator and denominator strictly smaller than \(p\), so the other side has zero valuation at \(p\), a contradiction. (Factors common to the two products have already canceled.) Conditional on the infinite-prime tail, a prescribed value of \(P\) therefore allows at most one finite-prefix exponent pattern. Its probability is no more than
\[
\prod_{3\le p\le y}\max\{1/p,1-1/p\}=\prod_{3\le p\le y}(1-1/p)\longrightarrow0,
\]
by the divergence of the sum of reciprocals of the primes. Thus \(P\) has no atoms; a mixture of its scaled copies, \(W=JP\), also has none.

**5. Full support.** The positive weights \(a_p\) tend to zero, but \(\sum_{p\ge3}a_p=\infty\) (as \(a_p\ge2/p\)). Given \(L\ge0\) and \(\epsilon>0\), choose a finite subset of sufficiently large odd primes whose \(a_p\)-sum is within \(\epsilon\) of \(L\). This is possible by greedily accumulating terms smaller than \(\epsilon\) from a divergent series. Forcing exactly those Bernoulli bits among primes up to a finite cutoff has positive probability. Choose the cutoff large enough that the independent remaining tail has expectation less than \(\epsilon\); Markov's inequality then gives positive probability of an additional tail below \(2\epsilon\). (Alternatively enlarge the prescribed finite cutoff while retaining the same target pattern.) Hence every neighborhood of \(e^{-L}\) has positive probability under \(P\); letting \(L\to\infty\) gives zero in the support, and \(L=0\) gives one. Therefore the support of \(P\) is \([0,1]\), and that of \(JP\) is \([0,1/2]\). This completes the proof.

## Verification

Run `python3 verify.py` with a standard Python 3 interpreter. The program enumerates the definition directly through \(n=1200\), checks the exact high-two-adic formula and the finite CRT error, tests prefix-product injectivity for the first ten odd primes, and compares an empirical product mean through \(100000\) with its finite Euler-product approximation. The complete observed output is in `verification_output.txt`. These finite computations are checks only; Steps 1–5 establish the results for all integers and for the infinite product.

## Relationship to prior work

Renshaw [1, Section 2, Theorems 2–13] defines \(T\) and obtains exact values and pointwise bounds, including the exact branch at powers of two of exponent at least two. The use of those ingredients is not claimed as new. Steuding and Suriajaya [2, Theorem 1.1] prove a first-moment asymptotic for the multiplicative generalized Schemmel function \(\varphi_m(n)=n\prod_{p\mid n}(1-m/p)\); their theorem covers the familiar multiplicative mean calculation but not the two-component limit law of nonmultiplicative \(T(n)/n\), its full moment sequence, or its atomless full-support property. Classical residue-class equidistribution, prime harmonic divergence, and Euler-product probability techniques are also prior mathematical tools.

The claim here is the distribution of the **nonmultiplicative** normalized Renshaw function across all integers, including the independent parity mixture, its explicit moments, and a rational-product argument for atomlessness and exact support. The possibility of an older, unindexed statement obtained via a general distribution theorem remains a priority risk; the present proof is self-contained apart from classical facts.

## Limitations

No convergence rate in distribution is claimed. No absolutely continuous density or smoothness is proved; an atomless distribution need not have a density. The moment formula applies to real \(s>0\) only; negative moments are not addressed. The original source's cryptographic context is not used to infer security properties. Computational results are finite checks, not a proof of the infinite claim, and no independent validation has been performed.

## References

[1] James Renshaw, *A Totient Function Associated with Variants of Groups*, arXiv:2603.13939v1, first posted 2026-03-14, https://arxiv.org/abs/2603.13939 .

[2] Jörn Steuding and Ade Irma Suriajaya, *Mean-values associated with a generalized Schemmel function*, Annales Universitatis Scientiarum Budapestinensis, Sectio Computatorica **54** (2023), 307–319, DOI:10.71352/ac.54.307, https://ac.inf.elte.hu/Vol_054_2023/doi/307_54.html .
