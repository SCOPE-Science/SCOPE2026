# Prime-square separation by prime-detecting Eisenstein coefficients

## Finding
For odd integers \(1\le r<s\), define \(\sigma_j(n)=\sum_{d\mid n}d^j\) and
\[
 A_{r,s}(n)=(1+n^s)\sigma_r(n)-(1+n^r)\sigma_s(n),\qquad n\ge2.
\]
The positive-index Fourier coefficients of the prime-detecting Eisenstein combination associated with \((r,s)\) have a **three-way arithmetic separation**:
\[
\begin{aligned}
 A_{r,s}(n)&=0 &&\Longleftrightarrow\quad n\text{ is prime};\\
 0<A_{r,s}(n)&<n^{s+r/2} &&\Longleftrightarrow\quad n=p^2\text{ for a prime }p;\\
 A_{r,s}(n)&>n^{s+r/2} &&\Longleftrightarrow\quad n\text{ is composite but not a prime square}.
\end{aligned}
\]
In particular, for **every composite** \(n\), the sharp pointwise lower envelope is
\[
\boxed{A_{r,s}(n)\ \ge\ n^{r/2}
 \left(n^{(s-r)/2}-1\right)
 \left(n^{(r+s)/2}-1\right),}
\]
with equality precisely for prime squares. At \(n=p^2\), the exact value is
\[
\boxed{A_{r,s}(p^2)=p^r(p^{s-r}-1)(p^{r+s}-1).}
\]
The scale \(n^{s+r/2}\) is asymptotically sharp along all prime-square indices, since the ratio tends to \(1\) as \(p\to\infty\).

The first partition-theoretic prime detector of Craig, van Ittersum and Ono is
\[
 E(n)=(n^2-3n+2)M_1(n)-8M_2(n)=\frac{A_{1,3}(n)}{n+1},
\]
where the \(M_j\) are MacMahon's weighted partition functions. Thus \(E(n)=0\) on primes, \(E(p^2)=p(p^2-1)^2\), and \(E(n)>n^{7/2}/(n+1)\) for every remaining composite \(n\). This explicitly separates prime squares from all other composites using the published detector.

## Assumptions and scope
Integers satisfy \(n\ge2\) and \(r,s\) are positive odd integers with \(r<s\). Powers with half-integer exponents denote positive real roots, not congruence classes. The divisor sums include both end divisors. The coefficient sequence is that of \((D^s+1)G_{r+1}-(D^r+1)G_{s+1}\) at positive indices, where \(D=q\,d/dq\) and \(G_j\) is the Eisenstein series with positive-index coefficient \(\sigma_{j-1}(n)\). The result addresses individual coefficient magnitudes; no normalized constant term is involved.

## Proof
**1. Exact proper-divisor expansion.** Put \(h=s-r\), which is even and at least \(2\), and let
\[
 T_n(d)=d^r\bigl(1+n^s-(1+n^r)d^h\bigr).
\]
Expanding the divisor sums gives \(A_{r,s}(n)=\sum_{d\mid n}T_n(d)\). The endpoint terms cancel identically: \(T_n(1)=n^s-n^r\) and \(T_n(n)=n^r-n^s\). Consequently
\[
 A_{r,s}(n)=\sum_{\substack{d\mid n\\1<d<n}}T_n(d).
\]
For primes the sum is empty.

**2. A uniform strict estimate for every proper divisor.** If \(n\) is composite then \(n\ge4\); every proper divisor \(d>1\) obeys \(d\le n/2\). Since \(r\ge1\) and \(h\ge2\),
\[
 \frac{(1+n^r)d^h}{n^s}
 \le\frac{1+n^{-r}}{2^h}
 \le\frac{1+1/4}{4}=\frac5{16}.
\]
Therefore
\[
 T_n(d)\ge d^r\left(1+\frac{11}{16}n^s\right)
 >\frac12 n^s d^r>0.
\]
All proper-divisor contributions are strictly positive.

**3. The central divisor.** When \(n=p^2\) for a prime \(p\), the sole proper divisor is \(p\). Direct factorization gives
\[
 A_{r,s}(p^2)=T_{p^2}(p)
 =p^r(p^{s-r}-1)(p^{r+s}-1).
\]
On replacing \(p\) with \(\sqrt n\), this is precisely the claimed lower-envelope expression. Dividing by \(n^{s+r/2}\) gives
\[
 \bigl(1-p^{-(s-r)}\bigr)\bigl(1-p^{-(r+s)}\bigr),
\]
which is strictly between \(0\) and \(1\), and tends to \(1\) as \(p\) increases through primes.

**4. Every other composite has an off-central divisor pair.** A composite \(n\) other than a prime square possesses a factorization \(n=ab\) with distinct integers \(2\le a<b<n\): for example, take its least prime divisor and its complementary factor. By the preceding estimate and the arithmetic-geometric mean inequality,
\[
\begin{aligned}
 A_{r,s}(n)&\ge T_n(a)+T_n(b)\\
 &>\tfrac12n^s(a^r+b^r)\\
 &\ge n^s(ab)^{r/2}=n^{s+r/2}.
\end{aligned}
\]
The lower-envelope expression is strictly smaller than \(n^{s+r/2}\) for every \(n>1\), since both factors \(1-n^{-(s-r)/2}\) and \(1-n^{-(r+s)/2}\) lie in \((0,1)\). Combining this with the prime and prime-square computations proves the exact trichotomy, the lower envelope, and all equality statements.

**5. Partition detector specialization.** Craig, van Ittersum and Ono give \(E(n)=6b_n(H_6)=(n^2-n+1)\sigma_1(n)-\sigma_3(n)\). Using \(1+n^3=(n+1)(n^2-n+1)\) shows \(A_{1,3}(n)=(n+1)E(n)\). The displayed bounds follow immediately, without changing the classifications.

## Verification
The accompanying standalone `prime_square_detector_verify.py` uses three calculations: full divisor enumeration, the proper-divisor expansion, and a separately implemented prime-power factorization of both divisor sums. It checks all \(28\) pairs of odd exponents \(1\le r<s\le15\) and all \(2\le n\le2400\), for \(67{,}172\) parameter-index instances. Exactly \(9{,}996\) tested instances have prime \(n\), \(420\) have prime-square \(n\), and \(56{,}756\) have other composite \(n\). Threshold comparisons are performed using exact integer squares, not floating-point approximations. All comparisons pass as recorded in `prime_square_detector_checks.txt`. Run `python3 prime_square_detector_verify.py`. The infinite assertion rests on the proof above, not on this finite enumeration.

## Relationship to prior work
Craig, van Ittersum and Ono, *Integer partitions detect the primes* (first public preprint May 10, 2024), establish coefficient nonnegativity and zero exactly at primes for this Eisenstein family, and provide the displayed partition-detector identity. The present claim is instead a **sharp coefficient-magnitude inverse theorem**: a natural single normalization classifies prime squares among the nonzero coefficients for all odd exponent pairs, together with the exact lower envelope at each composite argument. The original proof estimates each proper-divisor contribution; it does not state this three-way separation or the prime-square equality family.

The published *Exact coefficient content of prime-detecting divisor-sum forms* (2026) determines the greatest common integer divisor of the same coefficient sequences. A common congruence modulus does not imply a pointwise magnitude separation or characterize prime-square indices. Kane–Krishnamoorthy–Lau (2025) classify the ambient prime-detecting quasimodular forms, again a distinct question. Allen and Craig's *Quasimodular Forms, Partitions, and Primes in Intervals* (arXiv:2609.32053, September 2026) studies the same coefficient family in prime-interval and factorization contexts. Its full text was not accessible for detailed implication checking; possible implicit coverage of the present inequalities is a material unresolved priority risk, not treated as a novelty certificate.

## Limitations
The threshold is a mathematical classification of the coefficients, not an efficient computational primality or prime-square test: evaluating divisor sums usually requires arithmetic information about the input. The argument does not classify prime cubes or sharper secondary minima, and it does not analyze arbitrary signed combinations of prime-detecting forms. The proof is self-contained but has not undergone an independent mathematical audit. The originality judgment is best-of-knowledge and limited by the unavailable full text of one especially relevant later preprint and by other potentially unindexed sources.

## References
1. W. Craig, J.-W. van Ittersum and K. Ono, *Integer partitions detect the primes*, arXiv:2405.06451v1 (first public May 10, 2024); *Proc. Natl. Acad. Sci. USA* 121 (2024), e2409417121. https://arxiv.org/abs/2405.06451 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC11441547/
2. *Exact coefficient content of prime-detecting divisor-sum forms* (2026), publicly available mathematical research record; comparison used its full theorem and proper-divisor proof.
3. K. Allen and W. Craig, *Quasimodular Forms, Partitions, and Primes in Intervals*, arXiv:2609.32053v1 (first public September 25, 2026). https://arxiv.org/abs/2609.32053
4. B. Kane, K. Krishnamoorthy and Y.-K. Lau, *On a conjecture about prime-detecting quasimodular forms*, arXiv:2507.00147 (2025). https://arxiv.org/abs/2507.00147
