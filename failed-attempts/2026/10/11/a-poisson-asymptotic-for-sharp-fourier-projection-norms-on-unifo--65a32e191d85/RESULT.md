# A Poisson asymptotic for sharp Fourier projection norms on uniform set partitions

## Finding
Fix an integer \(k\geq3\). For every integer \(n\geq2\), put \(N=kn\) and let \(\mathcal H_{n,k}\) be the set of unordered partitions of \([N]\) into \(n\) blocks of size \(k\). Equip \(\mathcal H_{n,k}\) with counting measure. Let \(P_{n,k}\) be the orthogonal projection onto its unique copy of the \(S_N\)-irreducible module of shape \((N-2,2)\). This is the first nonconstant subrepresentation spanned by pair co-location functions.

For \(M,M'\in\mathcal H_{n,k}\), define the *common-pair overlap*
\[
S(M,M')=\sum_{B\in M}\sum_{B'\in M'}\binom{|B\cap B'|}{2}.
\]
Write
\[
m=n\binom{k}{2},\qquad p=\frac{k-1}{N-1},\qquad \mu=mp,\qquad d=\frac{N(N-3)}2.
\]
The exact projection and sharp endpoint norms are
\[
P_{n,k}(M,M')=\frac{d}{|\mathcal H_{n,k}|}\frac{S(M,M')-\mu}{m-\mu},
\qquad
\|P_{n,k}\|_{\ell^1\to\ell^1}=\|P_{n,k}\|_{\ell^\infty\to\ell^\infty}
=\frac{d}{m-\mu}\,\mathbb E\,|S(M,M')-\mu|,
\]
where \(M\) is fixed and \(M'\) is uniformly random. In particular the formula is independent of the choice of \(M\). The exact kernel is included to specify normalization; the principal asymptotic assertion is the following law, for each *fixed* \(k\ge3\):
\[
S(M,M')\ \Longrightarrow\ \operatorname{Poisson}(\lambda_k),
\qquad \lambda_k=\frac{(k-1)^2}{2},\quad n\to\infty,
\]
and therefore
\[
\boxed{\displaystyle
\lim_{n\to\infty}\frac{\|P_{n,k}\|_{\ell^\infty\to\ell^\infty}}{kn}
=(k-1)e^{-\lambda_k}\frac{\lambda_k^{\lfloor\lambda_k\rfloor}}{\lfloor\lambda_k\rfloor!}.}
\]
For \(k=3\) the constant is \(4e^{-2}\); moreover the constants have the iterated-size limit
\[
\lim_{k\to\infty}\lim_{n\to\infty}\frac{\|P_{n,k}\|_{\ell^\infty\to\ell^\infty}}{kn}
=\frac1{\sqrt\pi}.
\]
No statement about jointly growing \(k\) and \(n\) is made.

## Assumptions and scope
All assertions concern complex-valued functions on the finite transitive homogeneous space \(S_N/(S_k\wr S_n)\), with unnormalized counting measure; the orthogonal projector itself is unchanged by rescaling that measure. The parameters satisfy \(k\in\mathbb Z\), \(k\ge3\), \(n\in\mathbb Z\), \(n\ge2\). The \(\ell^1\) and \(\ell^\infty\) norms use counting measure. The number of partitions is exactly \(|\mathcal H_{n,k}|=N!/((k!)^n n!)\). The convergence is with \(k\) fixed, followed separately by a limit in \(k\); neither statement supplies a uniform-in-\(k\) error term.

The finite norm can also be evaluated from an entirely explicit finite polynomial. If \(\mathcal T_{n,k}\) denotes the integer \(n\)-by-\(n\) matrices with all row and column sums \(k\), then
\[
\mathbb E[u^{S}]=\frac{(k!)^{2n}}{N!}\sum_{A\in\mathcal T_{n,k}}
\frac{u^{\sum_{i,j}\binom{A_{ij}}2}}{\prod_{i,j}A_{ij}!}.
\]
This is a finite formula, not a claim of a polynomial-time evaluation.

## Proof
**Pair-module and exact kernel.** Index unordered vertex pairs by \(e\in\binom{[N]}2\), and let \(v_e(M)=1\) when the endpoints of \(e\) lie in one block of \(M\), otherwise \(0\). Every partition satisfies \(\sum_e v_e(M)=m\) and, for each vertex \(a\), \(\sum_{e\ni a}v_e(M)=k-1\). Thus the equivariant map from the pair permutation module to functions on \(\mathcal H_{n,k}\) annihilates the \((N-1,1)\) summand after subtracting constants. The pair module is the multiplicity-free direct sum \((N)\oplus(N-1,1)\oplus(N-2,2)\); the remaining map is nonzero because the pair co-location indicators vary between partitions. Irreducibility therefore identifies its centered image with exactly one \((N-2,2)\) summand of dimension \(d=N(N-3)/2\).

Under uniform \(M\), every pair has probability \(p=(k-1)/(N-1)\) of lying in one block. Hence the centered feature vector \(w(M)=(v_e(M)-p)_e\) satisfies
\[
\langle w(M),w(M')\rangle=S(M,M')-\mu,
\qquad \|w(M)\|_2^2=m-\mu.
\]
The Gram operator of the centered incidence features is an equivariant positive operator on the single irreducible image and hence a scalar multiple of its orthogonal projector. Since the normalized Gram diagonal is one, the rank-\(d\) trace identity forces its scalar to be \(d/|\mathcal H_{n,k}|\), proving the displayed kernel. By transitivity all its absolute row sums agree. The operator norms on \(\ell^\infty\) and \(\ell^1\) are the maximum absolute row and column sums, respectively; the symmetric kernel gives their equality. Choosing phases matching one row of the kernel shows sharpness, not merely an upper bound.

**Exact overlap polynomial.** Temporarily label the \(n\) target blocks. For each matrix \(A\) of intersections with the \(n\) fixed reference blocks, the number of labeled target partitions producing \(A\) is \((k!)^n/\prod_{i,j}A_{ij}!\). There are \(N!/(k!)^n\) labeled target partitions. Dividing gives the stated generating polynomial, with exponent \(\sum_{i,j}\binom{A_{ij}}2\).

**Poisson law.** Regard \(S\) as the sum of the indicators that each of the \(m\) vertex pairs in the fixed reference blocks remains together in the random partition. Fix a positive integer \(r\). Expand the factorial moment \(\mathbb E[(S)_r]\) over ordered selections of \(r\) distinct reference pairs. If they lie in \(r\) different reference blocks, there are exactly \((n)_r\binom{k}{2}^r\) such selections. Their \(2r\) endpoints are distinct, and the probability that each selected pair stays together in the random partition is \(p^r(1+O_{k,r}(n^{-1}))\) by sequentially assigning a uniformly random permutation of the vertices to \(n\) bins of size \(k\). Their contribution therefore tends to \(\lambda_k^r\).

For every other selection, let \(t\) be the number of fixed reference blocks touched, \(v\) the number of involved vertices, and \(c\) the number of connected components of the selected-edge graph. Each component has at least two vertices, and its vertices must occupy the same random target block. For fixed \(k,r\), the probability of all required co-locations is \(O_{k,r}(N^{-(v-c)})\), including the possibility that separate components occupy the same block. The number of selections of each fixed combinatorial pattern is \(O_{k,r}(n^t)\). Unless the selection consists of one pair in each of its \(t\) touched reference blocks, at least one touched block contributes \(v_i-c_i\ge2\), so \(v-c\ge t+1\); hence every such pattern contributes \(O_{k,r}(n^{-1})\). There are finitely many patterns at fixed \(k,r\). Therefore \(\mathbb E[(S)_r]\to\lambda_k^r\) for all fixed \(r\). Factorial-moment convergence implies the Poisson weak limit, and the convergence of its second moment ensures uniform integrability for \(|S-\mu|\). As \(\mu\to\lambda_k\), this gives
\[
\mathbb E|S-\mu|\to\mathbb E|Z-\lambda_k|,\quad Z\sim\operatorname{Poisson}(\lambda_k).
\]
Finally \(d/(N(m-\mu))\to1/(k-1)\), and for \(\lambda>0\) the Poisson recursion yields \(\mathbb E|Z-\lambda|=2\lambda e^{-\lambda}\lambda^{\lfloor\lambda\rfloor}/\lfloor\lambda\rfloor!\). Since \(2\lambda_k/(k-1)=k-1\), the sharp limit follows. The classical Poisson central limit theorem gives \(\mathbb E|Z-\lambda|\sim\sqrt{2\lambda/\pi}\) as \(\lambda\to\infty\), with uniform integrability supplied by the normalized second moment. This proves the iterated \(1/\sqrt\pi\) limit.

## Verification
Run `python3 verify.py` with NumPy installed. The checker enumerates all uniform partitions at parameters \((n,k)=(2,3),(2,4),(3,3),(4,2),(4,3)\); computes exact overlap histograms and rational endpoint norms; and directly checks idempotence and rank-normalized trace of the projector matrix for the cases with at most \(280\) partitions. The output terminates with `VERIFY_OK`. The exact small-case endpoint values for the three \(k=3\) cases are \(9/5\), \(243/70\), and \(11178/1925\), respectively. These finite tests do not establish the asymptotic convergence; its proof is the factorial-moment argument above.

## Relationship to prior work
Meagher and Moura (2005) studied uniform set-partition systems and provided an established source for the underlying homogeneous spaces. Lindzey (2014) developed the spectral framework for perfect matchings, the \(k=2\) analogue. Meagher, Shirazi and Stevens (2021, Section 5, Corollary 5.3), using Bender’s 1974 asymptotic enumeration, already established the zero-overlap probability \(\Pr(S=0)\to e^{-\lambda_k}\); that special event is prior work, and their cited Bender enumeration is a close potential route to the full Poisson law. Filmus and Lindzey (2022, Section 9 and Proposition 22) explicitly derive a spherical function depending on the same pair-overlap statistic for perfect hypermatchings; **the dependence on pair overlap is not claimed to be new here**. Their primary results concern extremal partially intersecting families, not the sharp endpoint projection norm or its fixed-block-size Poisson limiting constant. The kernel used here is independently normalized by diagonal trace and exact Gram idempotence rather than relying on a printed coefficient from that reference. Indeed, substituting \(k=3,n=2\) into its displayed Proposition 22 kernel coefficient and overlap definition gives a diagonal trace of \(12\), whereas the \((4,2)\)-irreducible projector on the ten partitions has rank \(9\); the rank-\(9\) Gram normalization above passes exact idempotence. This comparison concerns only the printed normalization, not the previously established overlap dependence. The asserted additional result is the sharp \(\ell^1\)/\(\ell^\infty\) spectral-amplification limit for the projector, with its explicit \(k\)-dependent constant and iterated Gaussian constant; the previously known zero-event asymptotic and pair-overlap spherical-function structure are not presented as discoveries.

## Limitations
The result is restricted to the first nonconstant irreducible summand and does not address higher Fourier blocks, operator norms at intermediate \(\ell^p\) exponents, jointly growing \(k,n\), or rates uniform over \(k\). The literature comparison supports a specific new asymptotic, not exhaustive novelty across all combinatorial-probability terminology. Known spherical-function identities already account for the pair-overlap dependence of the finite kernel. The numerical checker is finite and cannot replace the analytic proof.

## References
1. K. Meagher and L. Moura, *Erdős–Ko–Rado theorems for uniform set-partition systems*, Electronic Journal of Combinatorics 12 (2005), R40, published 2005-08-25, https://doi.org/10.37236/1937.
2. N. Lindzey, *Intersecting Families of Perfect Matchings*, arXiv:1409.2057, first version 2014-09-06, https://arxiv.org/pdf/1409.2057.
3. Y. Filmus and N. Lindzey, *Simple Algebraic Proofs of Uniqueness for Erdős–Ko–Rado Theorems*, arXiv:2201.02887v1 (2022-01-08), Section 9, https://arxiv.org/pdf/2201.02887.
4. K. Meagher, M. N. Shirazi, and B. Stevens, *An Extension of the Erdős–Ko–Rado Theorem to uniform set partitions*, arXiv:2108.07692v1 (2021-08-17), Section 5 and Corollary 5.3, https://arxiv.org/pdf/2108.07692.
5. E. A. Bender, *The asymptotic number of non-negative integer matrices with given row and column sums*, Discrete Mathematics 10 (1974), 217–223, cited via reference [1] and Theorem 5.1 of reference 4.
