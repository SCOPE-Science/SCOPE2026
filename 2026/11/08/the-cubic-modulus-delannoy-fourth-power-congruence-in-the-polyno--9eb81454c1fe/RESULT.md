# The cubic-modulus Delannoy fourth-power congruence in the polynomial ring

## Finding

For every odd prime \(p\), write
\[
D_m(X)=\sum_{j=0}^{m}\binom mj\binom{m+j}jX^j\in\mathbb Z[X].
\]
Then **the following coefficientwise congruence in \(\mathbb Z[X]\) holds**:
\[
\boxed{\sum_{m=0}^{p-1}(-1)^m(2m+1)D_m(X)^4
\equiv p\sum_{r=0}^{(p-1)/2}(-1)^r\binom{2r}r^2
\bigl(X^2+X\bigr)^r(2X+1)^{2r}\pmod{p^3}.}
\]
Thus the same congruence holds after substituting **any integer or any \(p\)-adic integer** for \(X\). In particular, it proves Conjecture 5.2 of Guo [1], which originally asserted the evaluated congruence for integer arguments; coefficientwise validity is stronger.

## Assumptions and scope

The prime \(p\) is odd, with no congruence restriction on \(p\), and \(X\) is an indeterminate. The modulus \(p^3\) means equality of every coefficient modulo \(p^3\), not merely equality of polynomial values at a finite set of residues. Set \(T=X(X+1)\), \(C_j=\binom{2j}j\), and
\[
F_p(X)=\sum_{m=0}^{p-1}(-1)^m(2m+1)D_m(X)^4.
\]
The known identity [1, Lemma 4.1, Eq. (4.2)] proves \(F_p(X)/p\in\mathbb Z[X]\). This normalization is essential: it suffices to prove the target for \(F_p(X)/p\) modulo \(p^2\).

## Proof

**1. Exact starting identity.** Guo [1, Lemma 4.1, Eq. (4.2)] proves, for every positive integer \(N\),
\[
\frac1N\sum_{m=0}^{N-1}(-1)^{N-m-1}(2m+1)D_m(X)^4
=\sum_{i,j=0}^{N-1}\sum_{k=0}^{i}
\binom{N-1}{j+k}\binom{N+j+k}{j+k}
\binom{i+j}{i}\binom{j}{i-k}\binom{j+k}{k}
C_iC_jT^{i+j}.
\tag{1}
\]
Out-of-range binomial coefficients are interpreted as zero. The identity is an integer-polynomial identity, not a congruence. Its published proof follows by squaring the Clausen expansion
\[
D_m(X)^2=\sum_{i=0}^m\binom mi\binom{m+i}i C_iT^i,
\]
applying the binomial-product decomposition [1, Eq. (2.5)], and using the finite alternating telescoping sum
\[
\sum_{m=h}^{N-1}(-1)^{N-m-1}(2m+1)
\binom mh\binom{m+h}h
=N\binom{N-1}h\binom{N+h}h.
\]
For odd \(N=p\), the sign on the left of (1) is \((-1)^m\). Therefore (1) is an exact expression for \(F_p(X)/p\).

**2. Upgrade the binomial-product approximation by one power.** For \(0\le h<p\), every integer \(1\le a\le h\) is invertible modulo \(p^2\), and
\[
A_p(h):=\binom{p-1}h\binom{p+h}h
=(-1)^h\prod_{a=1}^{h}\left(1-\frac{p^2}{a^2}\right)
\equiv(-1)^h\pmod{p^2}.
\tag{2}
\]
For \(p\le h\le2p-2\), the original factor \(\binom{p-1}h\) vanishes. Replacing \(A_p(h)\) by \((-1)^h\) nevertheless changes each summand of (1) by a multiple of \(p^2\). Indeed, here \(h=j+k\ge p\) with \(0\le j,k<p\) and \(k\le i<p\). The addition of \(j\) and \(k\) has one base-\(p\) carry, so \(p\mid\binom{j+k}{k}\). Also \(i+j\ge k+j\ge p\), hence at least one of \(i,j\) is greater than \((p-1)/2\); consequently \(p\mid C_iC_j\). These two factors yield \(p^2\). Thus the replacement \(A_p(j+k)\rightsquigarrow(-1)^{j+k}\) is valid for **every** summand modulo \(p^2\), including the out-of-range terms.

**3. Collapse the third index.** The integer Chu–Vandermonde identity [1, Eq. (4.5)] states
\[
\sum_{k=0}^i(-1)^k\binom{j}{i-k}\binom{j+k}{k}=(-1)^i
\qquad(i,j\ge0).
\tag{3}
\]
Applying (2) and (3) to (1), with all sums finite, gives the **polynomial** congruence
\[
\frac{F_p(X)}p\equiv
\sum_{i,j=0}^{p-1}(-1)^{i+j}\binom{i+j}{i}C_iC_jT^{i+j}
\pmod{p^2}.
\tag{4}
\]

**4. Remove the second carry region.** If \(0\le i,j<p\) but \(i+j\ge p\), then \(p\mid\binom{i+j}i\) (one base-\(p\) carry) and \(p\mid C_iC_j\), again because one of the two indices exceeds \((p-1)/2\). Hence each such term in (4) vanishes modulo \(p^2\). Setting \(n=i+j\), we obtain
\[
\frac{F_p(X)}p\equiv
\sum_{n=0}^{p-1}(-T)^n
\sum_{i=0}^n\binom ni C_iC_{n-i}\pmod{p^2}.
\tag{5}
\]

**5. Evaluate the remaining convolution.** Guo's proved identity [1, Lemma 4.2, Eq. (4.3)] is
\[
\sum_{i=0}^n\binom ni C_iC_{n-i}
=\sum_{r=0}^n C_r^2\binom r{n-r}(-4)^{n-r}
\qquad(n\ge0).
\tag{6}
\]
Its published proof verifies that the two sides obey the same recurrence
\[
(n+2)^2S_{n+2}-4(3n^2+9n+7)S_{n+1}+32(n+1)^2S_n=0
\]
with \(S_0=1\) and \(S_1=4\). The accompanying verifier independently evaluates both formulas and this recurrence over 23 initial values; the all-index identity follows from the proved published lemma, **not** from these finite tests.

Substituting (6) into (5), rearrange the finite sums. If \((p+1)/2\le r<p\), then \(p\mid C_r\) and thus \(p^2\mid C_r^2\), so such \(r\) contribute zero. For \(0\le r\le(p-1)/2\), the binomial factor \(\binom r{n-r}\) is supported on \(r\le n\le2r\le p-1\), permitting the *complete* binomial sum. Accordingly,
\[
\begin{aligned}
\frac{F_p(X)}p
&\equiv\sum_{r=0}^{(p-1)/2}(-1)^rC_r^2T^r
\sum_{s=0}^r\binom rs(4T)^s\\
&=\sum_{r=0}^{(p-1)/2}(-1)^rC_r^2T^r(1+4T)^r\\
&=\sum_{r=0}^{(p-1)/2}(-1)^rC_r^2(X^2+X)^r(2X+1)^{2r}
\pmod{p^2},
\end{aligned}
\]
where \(1+4T=(2X+1)^2\). Multiplication by \(p\) proves the asserted coefficientwise congruence modulo \(p^3\). The steps never evaluate \(X\) or invert a polynomial; they are valid in \(\mathbb Z[X]\). \(\square\)

## Verification

Run `python3 verify.py` using Python 3 and its standard library. It independently builds the integer polynomials from the definition, compares **every coefficient** modulo \(p^3\) for the nine primes \(3,5,7,11,13,17,19,23,29\), and checks the normalized triple-to-double reduction modulo \(p^2\) for seven primes. It also checks the exact identity (1) at 49 small argument/size pairs and checks both sides of (6), including its recurrence, for 23 indices. The output is:

```text
VERIFY_OK primes=9 coefficients=481 lemma_4_2=23 recurrence=21 lemma_4_1=49 intermediate_primes=7 intermediate_coefficients=143 all_exact=True
```

All computations use exact integer arithmetic. Finite cases are auxiliary checks, not a substitute for the proof above; in particular no finite search establishes all primes.

## Relationship to prior work

Guo [1] proves the same congruence only modulo \(p^2\) (Theorem 1.4, Eq. (1.7)) and poses the modulo-\(p^3\) statement explicitly as Conjecture 5.2 (p. 9). The author's separate Legendre-polynomial manuscript [2] presents an equivalent formulation as Conjecture 1.5, rather than a proof. The proof here uses Guo's **already proved** exact binomial identities but adds a second-order carry analysis and upgrades the normalized congruence from modulo \(p\) to modulo \(p^2\), giving the desired new conclusion.

Wang and Zhong [3] study other sums of Delannoy polynomials, with a **single** Delannoy polynomial factor in their main congruences and different weight powers; those statements do not imply this fourth-power prime-cube result. Additional searches did not locate an earlier proof of Guo's exact conjecture, but absence of a search match cannot certify absolute historical priority.

## Limitations

The result treats odd prime moduli and their cubes, not the prime two, higher powers beyond the stated cube modulus, or arbitrary composite moduli. It establishes a congruence, not an exact integer identity between the two polynomial expressions. Historical priority remains conditional on the literature surveyed.

## References

[1] Victor J. W. Guo, *Some congruences involving powers of Delannoy polynomials*, arXiv:1412.7724v1, first posted 10 December 2014, https://arxiv.org/pdf/1412.7724 (especially Theorem 1.4, Lemmas 4.1–4.2, Eq. (4.5), and Conjecture 5.2). Published DOI: 10.1080/10652469.2015.1034123.

[2] Victor J. W. Guo, *Some congruences involving powers of Legendre polynomials*, author's open manuscript, https://math.ecnu.edu.cn/~jwguo/maths/Legendre2.pdf (Theorem 1.4 and Conjecture 1.5). Public posting date not established; used only for comparison, not cohort dating.

[3] Rong-Hua Wang and Michael X. X. Zhong, *Congruences for sums of Delannoy numbers and polynomials*, arXiv:2505.05728v1, first posted 9 May 2025, https://arxiv.org/pdf/2505.05728 (Introduction and Theorem 1.1).
