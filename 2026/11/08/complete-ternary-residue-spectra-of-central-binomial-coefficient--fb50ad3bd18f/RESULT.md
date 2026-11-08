# Complete ternary residue spectra of central binomial coefficients on arithmetic progressions

## Finding
For any positive integer \(b\) not divisible by three and any integer \(\beta\), define
\[
\mathcal R(b,\beta)=\left\{\binom{2(bn+\beta)}{bn+\beta}\bmod3:\ n\in\mathbb Z_{\ge1},\ bn+\beta\ge0\right\}.
\]
Then the **entire residue spectrum** is
\[
\mathcal R(b,\beta)=
\begin{cases}
\{0,1,2\},&b\text{ odd};\\
\{0,1\},&b\text{ even},\ \beta\text{ even};\\
\{0,2\},&b\text{ even},\ \beta\text{ odd}.
\end{cases}
\]
Every listed residue occurs for infinitely many admissible positive indices \(n\). Excluded residues never occur. In particular, for each positive even \(b\) coprime to three and every integer \(\beta\), the family
\(\binom{2bn+2\beta}{bn+\beta}\) omits one nonzero residue modulo three for all sufficiently large positive \(n\), contradicting the corresponding instance \(a=2b,\alpha=2\beta,p=3\) of Guo–Krattenthaler Conjecture 7.1. The simplest instance, \(\binom{4n}{2n}\), never equals \(2\pmod3\).

## Assumptions and scope
The modulus is the prime three; \(b\ge1\) is coprime to three and \(\beta\in\mathbb Z\) is unrestricted. All coefficients use nonnegative upper and lower arguments (guaranteed by \(bn+\beta\ge0\)). The asserted infinitude means infinitely many positive integers \(n\) for each included residue. The full Guo–Krattenthaler conjecture concerns general affine binomial parameters; the theorem treats the symmetric central-binomial line \(a=2b,\alpha=2\beta\) only.

## Proof
**Ternary-digit lemma.** Let \(k\ge0\) have base-three digits \(k_j\in\{0,1,2\}\). Kummer's carry criterion states that \(3\mid\binom{2k}{k}\) if and only if adding \(k\) to itself entails a carry. This is equivalent to at least one digit \(k_j=2\): if all digits belong to \(\{0,1\}\), adding the two copies generates no carries; conversely, take the least position of a digit two, where a carry must arise. When there is no such digit, Lucas' theorem gives
\[
\binom{2k}{k}\equiv\prod_j\binom{2k_j}{k_j}=2^{\sum_jk_j}
\equiv(-1)^k\pmod3,
\]
where the last equality uses that three is odd and the digit sum has the parity of \(k\). Thus
\[
\binom{2k}{k}\equiv
\begin{cases}0,&\text{some ternary digit of }k\text{ is }2;\\ (-1)^k,&\text{otherwise},\end{cases}\pmod3.
\]
**Upper restrictions.** All admissible \(k=bn+\beta\) are congruent to \(\beta\pmod b\). If \(b\) is even, their parity equals the parity of \(\beta\), so the digit lemma excludes residue \(2\) when \(\beta\) is even and excludes \(1\) when \(\beta\) is odd. No restriction beyond \(\{0,1,2\}\) is needed when \(b\) is odd.

**Constructive occurrence.** Choose an integer \(L\ge1\) such that \(3^L\equiv1\pmod b\), possible because \(\gcd(b,3)=1\); the assertion for \(b=1\) is immediate. For \(m\ge1\), let
\[
K_m=\sum_{j=1}^{m}3^{Lj}.
\]
Its ternary digits are zero or one, \(K_m\equiv m\pmod b\), and its central-binomial residue is \((-1)^m\). Choose \(m\equiv\beta\pmod b\). When \(b\) is odd both parities of such positive \(m\) occur, establishing both nonzero residues; when \(b\) is even just the prescribed nonzero residue occurs. To produce zero choose \(m\ge1\) with \(m+2\equiv\beta\pmod b\) and let
\[
Z_m=K_m+2\cdot3^{L(m+1)}.
\]
Its base-three digits include a digit two without carrying in its displayed expansion, and \(Z_m\equiv\beta\pmod b\). For any constructed \(K_m\) or \(Z_m\), multiplying by \(3^{Lt}\) for \(t\ge0\) preserves the residue modulo \(b\) and merely shifts its ternary digits. It therefore preserves its central-binomial residue, while the numbers become unbounded. For all large \(t\), writing \(k=bn+\beta\) yields an integer \(n\ge1\). This establishes infinitely many occurrences of every listed residue and completes the classification. \(\square\)

## Verification
Run `python3 artifacts/verify.py`. The independent finite checker constructs digit witnesses for every \(1\le b\le40\) coprime to three and all offsets \(-b\le\beta\le b\); it cross-checks Lucas products against explicit binomial coefficients for small \(k\) and checks actual witness congruences. The unbounded theorem is deduced from the digit lemma and the periodic-power construction, not from finite enumeration.

## Relationship to prior work
Guo and Krattenthaler formulated the general residue-attainment conjecture in their 2013 paper (Conjecture 7.1). Vsemirnov (2014) supplied counterexamples using the prime five, not the present full prime-three symmetric family. Yaqubi and Mirzavaziri (2017) and He and Yuan (2024) study related residue sets and partial results; He and Yuan explicitly pose a general exact-residue-set problem and their Theorem 1.6 requires \(p>a>b\), hence does not apply to \(p=3,a=2b\ge4\). Their Theorem 3.8 requires congruences between \(a\) and \(b\) modulo higher powers of \(p\), absent here for \(3\nmid b\). The classical Lucas and Kummer theorems themselves are not claimed as new. The contribution is the complete progression-by-progression spectrum and sharp parity boundary, including infinitely many prime-three counterexamples to the stated general conjecture. Broad literature on binomial digit distributions might still contain an equivalent formulation; historical priority requires independent specialist examination.

## Limitations
Only the prime three and the symmetric coefficient \(\binom{2k}{k}\) are classified. The theorem does not give densities or asymptotic frequencies, nor extend automatically to \(3\mid b\), other primes, or arbitrary affine binomial parameters. No claim of independent audit or complete historical priority is made.

## References
1. V. J. W. Guo and C. Krattenthaler, *Some divisibility properties of binomial and q-binomial coefficients*, arXiv:1301.7651 (first version, 2013-01-31), Section 7, Conjecture 7.1.
2. M. Vsemirnov, *On a conjecture of Guo and Krattenthaler*, *International Journal of Number Theory* **10** (2014), 1541–1543, DOI:10.1142/S1793042114500420.
3. D. Yaqubi and M. Mirzavaziri, *Some divisibility properties of binomial coefficients*, arXiv:1701.06217 (2017), Section 4.
4. Y. He and P. Yuan, *Results on some conjectures about binomial coefficients*, Bull. Math. Soc. Sci. Math. Roumanie **67** (2024), 429–448; Introduction and Section 3, https://ssmr.ro/bulletin/pdf/67-4/articol_4.pdf.
5. K. Barat and P. J. Grabner, *Distribution of Binomial Coefficients and Digital Functions*, 2001, DOI:10.1112/S0024610701002630 (historical coverage risk; abstract inspected only).
6. É. Lucas, 1878, Lucas' congruence for binomial coefficients; E. Kummer, 1852, the carry criterion for binomial-coefficient valuations.
