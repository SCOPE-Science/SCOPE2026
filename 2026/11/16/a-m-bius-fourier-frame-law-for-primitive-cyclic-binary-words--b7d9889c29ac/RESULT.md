# A Möbius–Fourier frame law for primitive cyclic binary words

## Finding
Let \(n\ge4\) be composite, and let \(\mathcal P_n\subset\{-1,1\}^n\) be the binary words whose least cyclic period is exactly \(n\). Equip \(\mathcal P_n\) with uniform probability and restrict the constant Walsh character and the \(n\) coordinate characters \(\chi_j(x)=x_j\), \(0\le j<n\). Set
\[
N_n=\sum_{q\mid n}\mu(q)2^{n/q},\qquad
H_n=\sum_{q\mid n}\mu(q)q2^{n/q},
\]
where \(\mu\) is the number-theoretic Möbius function. The first-Walsh Gram matrix is positive definite, the constant character has Gram eigenvalue \(1\), and the coordinate-character Gram eigenvalues, indexed by spatial Fourier frequency \(k\in\{0,\ldots,n-1\}\), are exactly
\[
\lambda_k=\frac1{N_n}\sum_{\substack{q\mid n\\q\mid k}}\mu(q)q2^{n/q}.
\]
The greatest eigenvalue is \(2^n/N_n\), attained exactly for \(\gcd(k,n)=1\), with multiplicity \(\varphi(n)\). The least is \(H_n/N_n>0\). Writing \(\operatorname{rad}(n)\) for the product of the distinct prime factors of \(n\), its eigenspace consists exactly of spatial modes with \(\operatorname{rad}(n)\mid k\), **except** when \(n=2p\) for an odd prime \(p\). In that exceptional case its eigenspace consists exactly of the even modes \(k\), and has multiplicity \(p\), rather than \(n/\operatorname{rad}(n)=1\).

For every composite \(n\ge4\), the optimal squared restriction condition number of the complete constant-plus-first-Walsh system is
\[
\boxed{\kappa_n=\frac{2^n}{H_n}.}
\]
It is finite and tends to \(1\) exponentially in \(n\). At twice an odd prime, the condition number simplifies to
\[
\boxed{\kappa_{2p}=\frac1{1-2^{1-p}}.}
\]
The normalization is probability-normalized squared \(L^2\) energy, not the ratio of unsquared singular values.

## Assumptions and scope
A cyclic word has period dividing \(d\mid n\) when \(x_{j+d}=x_j\) for all indices modulo \(n\); it is primitive when no proper divisor of \(n\) is a period. The sample set contains **all indexed primitive words**, not one representative per rotation orbit. Each orbit has size \(n\), so uniform sampling of rotation orbits followed by a uniformly random rotation yields the same distribution. The Fourier modes appearing in the theorem are spatial DFT eigenvectors of the coordinate-coordinate Gram block, not extra Walsh characters. The finite-dimensional signal space is \(\operatorname{span}\{1,\chi_0,\ldots,\chi_{n-1}\}\).

The composite-length restriction isolates the new claim from the prime-length case, where primitive binary words are precisely nonconstant binary words and a more general published first-Walsh result on surjective words already applies. The degenerate boundary \(n=2\) is not injective; every \(n\ge3\) would be injective by the argument below, but prime lengths are included only as a check, not an originality claim.

## Proof
**1. Primitive-period inclusion and exact Gram.** For \(q\mid n\), write \(\mathcal B_{n/q}\) for the \(2^{n/q}\) words with period dividing \(n/q\). Divisor Möbius inversion yields the *pointwise indicator identity*
\[
1_{\mathcal P_n}(x)=\sum_{q\mid n}\mu(q)1_{\mathcal B_{n/q}}(x).
\]
Summing gives \(|\mathcal P_n|=N_n\). On \(\mathcal B_{n/q}\), the coordinates \(i,j\) coincide identically if \(i\equiv j\pmod{n/q}\); otherwise they are independent symmetric signs and their product sums to zero. Consequently the unnormalized coordinate Gram matrix is
\[
A_{ij}=\sum_{\substack{q\mid n\\i\equiv j\ (\mathrm{mod}\ n/q)}}\mu(q)2^{n/q}.
\]
It is circulant. For \(d\mid n\), the \(n\)-square matrix \(B_d=(1_{i\equiv j\ (\mathrm{mod}\ d)})\) acts on \(v_k=(n^{-1/2}e^{2\pi ikj/n})_j\) by the scalar \(n/d\) if \((n/d)\mid k\), and by zero otherwise. Taking \(d=n/q\) proves the stated eigenvalue formula. Global sign complement sends each primitive word to another primitive word, so every coordinate character has mean zero. Thus the constant character is orthogonal to the entire coordinate block.

**2. Strict monotonicity and the sole equality mechanism.** Let \(P\) be the set of distinct primes dividing \(n\). For \(S\subseteq P\) define
\[
F_n(S)=\sum_{q\mid\prod_{p\in S}p}\mu(q)q2^{n/q}.
\]
Then \(N_n\lambda_k=F_n(\{p\in P:p\mid k\})\). For \(p\in P\setminus S\) put \(T=n/p\) and \(m=\prod_{r\in S}r\); in particular \(m\mid T\). A direct divisor pairing gives
\[
F_n(S)-F_n(S\cup\{p\})=pH(T,m),\quad
H(T,m)=\sum_{q\mid m}\mu(q)q2^{T/q}.
\]
To prove the sign of \(H(T,m)\) without an unproved alternating-sum inequality, let \(W(T,m)\) comprise the sign words of length \(T\) that have no period dividing \(T/r\) for any prime \(r\mid m\). On words of period dividing \(T/q\), with \(q\mid m\), summing the square of the coordinate total gives exactly \(Tq2^{T/q}\): a repeated base word has total \(q\) times its base total, and independent base coordinates contribute \(T/q\) in expectation. Inclusion-exclusion therefore proves the identity
\[
H(T,m)=\frac1T\sum_{x\in W(T,m)}\left(\sum_{j=0}^{T-1}x_j\right)^2\ge0.
\]
For \(T\ge3\), a word with a single negative coordinate belongs to \(W(T,m)\) and has nonzero sum \(T-2\); hence the inequality is strict. For \(T=1\) it is also strict. For \(T=2\), it vanishes only when \(m=2\), because then the allowed words are precisely \((+,-)\) and \((-,+)\); if \(m=1\), the constant words contribute. Thus \(F_n(S)\) decreases strictly upon adding a prime, with one possible equality: \(n=2p\) for an odd prime \(p\), \(S=\{2\}\), and the added prime is \(p\).

**3. Exact extreme eigenspaces.** By the preceding monotonicity, the maximum of \(F_n(S)\) is reached only at \(S=\varnothing\), whose value is \(2^n\); there are \(\varphi(n)\) such frequencies. The minimum is \(F_n(P)=H_n\). Except for the sole equality mechanism, precisely the frequencies divisible by \(\operatorname{rad}(n)\) attain it, giving multiplicity \(n/\operatorname{rad}(n)\). If \(n=2p\) with \(p\) odd prime, the frequencies divisible by \(2\) but not \(p\) have the same minimum as those divisible by both, giving all \(p\) even frequencies. The strict inequalities elsewhere exclude further cases.

**4. Positive lower edge and exact frame conditioning.** Every primitive word of length \(n\ge3\) includes the one-negative-coordinate words, whose coordinate sum has magnitude \(n-2>0\). Taking \(T=n\), \(m=\operatorname{rad}(n)\) in the identity above gives \(H_n>0\). Since at least the two constant words are excluded, \(N_n<2^n\) and so the largest coordinate eigenvalue exceeds \(1\). All diagonal Gram entries equal \(1\), hence the trace of the coordinate Gram is \(n\) and its minimum lies below \(1\). The constant character's eigenvalue \(1\) is therefore between the two extremes and does not change the full-band squared condition ratio. This yields \(\kappa_n=2^n/H_n\).

For \(n=2p\), the four nonzero Möbius contributions in \(H_n\), from divisors \(1,2,p,2p\), are \(2^{2p},-2^{p+1},-4p,+4p\); cancellation proves the exceptional closed form. Finally,
\[
0\le 2^n-H_n\le\sum_{q=2}^n q2^{n/q}\le n^2 2^{n/2}.
\]
For sufficiently large \(n\), this yields \(\kappa_n=1+O(n^2 2^{-n/2})\), uniformly over composite lengths. No assertion about higher Walsh degrees follows.

## Verification
The included standalone \(\texttt{check.py}\) uses the Python standard library only. It directly enumerates all binary words through length \(13\), determines cyclic primitiveness independently, computes their exact integer Gram matrices, checks the Möbius matrix formula entry by entry, and checks the DFT eigen-equations numerically. It also checks the finite squarefree-subset monotonicity and its equality exception through length \(200\) using exact integers. The executed output is:

```text
PRIMITIVE_CYCLIC_WALSH_PASS enumerate_n=2..13; exact_Mobius_n=3..200; Fourier_eigenchecks_n=2..13
```

These finite checks are additional reproducibility evidence; the argument above proves all composite \(n\ge4\) without relying on extrapolation.

## Relationship to prior work
Primitive-word counting by Möbius inversion is classical and not claimed as new. Adamson–Deligkas–Gusev–Potapov study one- and multidimensional necklace counting, generation, ranking and unranking; their published 2021 manuscript supplies a concrete modern motivation for sampling rotation-aperiodic objects. Katz–Rahman–Ward study equality of autocorrelations of *individual* binary sequences, not the covariance of the *uniform primitive-word ensemble*. A previously public first-Walsh theorem on all surjective words covers the prime-length specialization: for prime \(n\), a word is primitive if and only if it is not constant. It does **not** determine conditional sampling on primitive words for composite \(n\), since removing smaller-period words destroys arbitrary coordinate-permutation symmetry and leaves cyclic symmetry. Published Lucas-cube first-Walsh results concern adjacency-exclusion, not period-primitivity. Existing primitive-row DFT frame-potential results concern sampling unit residues modulo a cyclic integer, not indexed cyclic words. Neither their objects nor their implications supply the present all-composite Möbius eigenvalues, exact minimal eigenspaces, or \(n=2p\) equality.

## Limitations
This is a first-Walsh (linear-character) statement, not a general high-bandwidth sampling or phase-retrieval result. It uses all indexed primitive binary words with uniform weights; unequal necklace weights or one canonical necklace representative need not give this Gram. Historical priority remains provisional: older full texts on necklace transforms and signal autocorrelations may contain an equivalent ensemble calculation; not all plausible older literature was accessible. The numerical checker alone does not establish uniqueness of a research claim or prove the infinite-dimensional assertion. No independent audit has been performed.

## References
1. D. Adamson, A. Deligkas, V. V. Gusev and I. Potapov, *Combinatorial Algorithms for Multidimensional Necklaces*, arXiv:2108.01990, first public version 2021-08-04, https://arxiv.org/abs/2108.01990 ; full HTML https://arxiv.org/html/2108.01990v2 .
2. D. J. Katz, A. Rahman and M. J. Ward, *Sequences with identical autocorrelation functions*, arXiv:2308.07467, first public version 2023-08-14, https://arxiv.org/abs/2308.07467 .
3. *Exact first-band Fourier sampling spectra on surjective words*, publicly indexed research record 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-first-band-fourier-sampling-spectra-on-surjective-words--38dfe55b7163 .
4. *Exact Lucas-cube Fourier precision and parity-split sharp frame conditioning*, publicly indexed research record 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-lucas-cube-fourier-precision-and-parity-split-sharp-frame--159f7c631a3c .
