# Exact common divisors of consecutive Fibonacci cubes at every even length

## Finding

Let \(F_0=0\), \(F_1=1\), and \(F_{n+2}=F_{n+1}+F_n\). Let \(L_0=2\), \(L_1=1\), and \(L_{n+2}=L_{n+1}+L_n\) be the Lucas numbers. For every integer \(k\ge1\), define the positive integer
\[
C_3(k)=\gcd_{n\ge0}\left(\sum_{j=1}^{k} F_{n+j}^{3}\right).
\]
For every integer \(m\ge1\), put \(U_m=L_m\) when \(m\) is odd, and \(U_m=F_m\) when \(m\) is even. Then
\[
\boxed{C_3(2m)=\frac{3^{\mathbf1_{4\mid m}}}{2^{\mathbf1_{3\mid m}}}\,U_m.}
\]
The right side is an integer. Equivalently, if
\[
D_{2m}=\gcd(F_{2m+1}^{3}-1,F_{2m+2}^{3}-1),
\]
then
\[
\boxed{C_3(2m)=\begin{cases}D_{2m}/2,&3\mid m,\\D_{2m},&3\nmid m.\end{cases}}
\]
In particular, the factor of two occurs at lengths divisible by six, rather than at lengths not divisible by six. This settles the Fibonacci-cube case of the question posed in Section 6.1 of Mbirika and Spilker's study of consecutive squared Fibonacci sums, while correcting the direction of the proposed case split.

## Assumptions and scope

The starting index is any integer \(n\ge0\), and the length is any **positive even integer** \(2m\). All gcds are taken as positive gcds over the infinite collection of integer sums. No assertion is made here for odd lengths, Lucas-cube sums, arbitrary initial conditions, or powers other than three. Indicators \(\mathbf1_{P}\) equal one if predicate \(P\) holds and zero otherwise. All identities use exact integers.

## Proof

**1. The linear period divisor.** Set \(k=2m\) and
\[
G=\gcd(F_{k+1}-1,F_{k+2}-1).
\]
Standard Fibonacci–Lucas addition identities give, when \(m\) is odd,
\[
F_{2m+1}-1=L_mF_{m+1},\qquad F_{2m+2}-1=L_mF_{m+2},
\]
and, when \(m\) is even,
\[
F_{2m+1}-1=F_mL_{m+1},\qquad F_{2m+2}-1=F_mL_{m+2}.
\]
Consecutive Fibonacci numbers are coprime, as are consecutive Lucas numbers (the Euclidean algorithm applied to either recurrence reduces their gcd to the initial gcd one). Consequently
\[
G=\begin{cases}L_m,&m\text{ odd},\\ F_m,&m\text{ even}.
\end{cases}
\]
Modulo \(G\), both \(F_k=F_{k+2}-F_{k+1}\) and \(F_{k+1}-1\) vanish. The addition formula \(F_{n+k}=F_kF_{n-1}+F_{k+1}F_n\) therefore gives
\[
F_{n+k}\equiv F_n\pmod G\qquad(n\ge1),
\]
and the same holds for \(n=0\). The elementary Fibonacci and Lucas parity periods show \(G\) is even exactly when \(3\mid m\). Similarly, \(3\mid G\) exactly when \(4\mid m\): among even \(m\), \(3\mid F_m\) exactly for multiples of four; for odd \(m\), \(3\nmid L_m\).

**2. A cubic Cassini gcd lemma.** Suppose integers \(z,w\) satisfy \(w^2-zw-z^2=-1\). Then
\[
\gcd(z^3-1,w^3-1)=H\cdot\begin{cases}3,&3\mid H,\\1,&3\nmid H,\end{cases}\quad H=\gcd(z-1,w-1).
\]
To prove this, let a prime \(p\) divide both cubic differences. Over \(\mathbb F_p\), \(z^3=w^3=1\); hence \(z\) is invertible. Put \(r=w/z\). If \(r=1\), the quadratic identity gives \(z^2=1\), and \(z^3=1\) forces \(z=w=1\). If \(r\ne1\), then \(r^2+r+1=0\). Substituting into the quadratic identity gives \(2w^2=-1\); multiplying by \(w\), because \(w^3=1\), gives \(w=-2\), hence \(9=0\) in \(\mathbb F_p\). This forces \(p=3\), where \(r^3=1\) itself forces \(r=1\), a contradiction. Thus every prime divisor of the cubic gcd divides \(H\). Conversely, all primes dividing \(H\) divide both cubic differences. For each such prime \(p\ne3\), \(z^2+z+1\) and \(w^2+w+1\) are units modulo \(p\), so cubic and linear differences have identical \(p\)-adic valuations. At \(p=3\), each quadratic factor has valuation exactly one because its argument is \(1\pmod3\). Taking minimum valuations gives the claimed identity.

Take \(z=F_{k+1}\) and \(w=F_{k+2}\). Cassini's identity, with \(k\) even, says \(w^2-zw-z^2=-1\). Thus
\[
D:=\gcd(F_{k+1}^3-1,F_{k+2}^3-1)
=G\cdot\begin{cases}3,&3\mid G,\\1,&3\nmid G.\end{cases}
=3^{\mathbf1_{4\mid m}}G.
\]

**3. The gcd of all successive differences.** Define \(A_n=F_{n+k}^3-F_n^3\) for integers \(n\ge1\). The congruence in step 1 shows \(G\mid A_n\) for all \(n\). If \(3\mid G\), then the binomial expansion of \((F_n+Gt)^3-F_n^3\) is divisible by \(3G\) for every integer \(t\), so in that case \(3G\mid A_n\). Thus \(D\mid A_n\) for every \(n\ge1\). Since \(A_1=F_{k+1}^3-1\) and \(A_2=F_{k+2}^3-1\),
\[
\gcd_{n\ge1} A_n=D.
\]
Let \(S_n=\sum_{j=1}^{k}F_{n+j}^3\). Then \(S_{n+1}-S_n=A_{n+1}\). The infinite gcd is consequently
\[
C_3(k)=\gcd(D,S_0).
\]

**4. The first sum and its precise factor of two.** A telescoping identity (verified by substituting \(F_{j+2}=F_{j+1}+F_j\)) gives
\[
2S_0=1-F_k^3+3F_kF_{k+1}^2-F_{k+1}^3.
\]
Write \(F_k=Ga\) and \(F_{k+1}-1=Gb\); the identities of step 1 give
\[
(a,b)=\begin{cases}(F_m,F_{m+1}),&m\text{ odd},\\ (L_m,L_{m+1}),&m\text{ even}.\end{cases}
\]
Expanding exactly yields
\[
2S_0=3G(a-b)+G^2(6ab-3b^2)+G^3(-a^3+3ab^2-b^3). \tag{1}
\]
If \(3\nmid G\), equation (1) shows \(D=G\mid 2S_0\). If \(3\mid G\), all three terms on the right are divisible by \(3G=D\), again giving \(D\mid2S_0\).

When \(G\) is odd, so is \(D\), and hence \(D\mid S_0\), giving \(C_3(k)=D\). When \(G\) is even, \(D/G\) is odd, and equation (1), divided by \(D\) and reduced modulo two, gives
\[
\frac{2S_0}{D}\equiv a-b\pmod2.
\]
Now \(G\) is even precisely when \(3\mid m\). If \(m\) is odd, \(a-b=-F_{m-1}\); if \(m\) is even, \(a-b=-L_{m-1}\). Because \(3\mid m\), neither \(F_{m-1}\) nor \(L_{m-1}\) is even. Therefore \(2S_0/D\) is odd, and \(\gcd(D,S_0)=D/2\). Combining both parity cases with the formula for \(D\) in step 2 proves the theorem for every \(m\ge1\).

## Verification

The accompanying standalone program `check_cubic_gcd.py` computes Fibonacci and Lucas numbers from their defining recurrences, independently enumerates the first twenty length-\(k\) cubic sums for each of 120 even lengths \(2\le k\le240\), compares their exact gcd with the closed formula, and separately checks the two-difference gcd and period congruences. The run returned `VERIFY_OK even_lengths=120 exact_sum_windows=2400`. These finite tests corroborate, but do not replace, the all-length proof. For example, \(C_3(6)=2\) while the two-difference gcd is four, and \(C_3(8)=9\) while the two-difference gcd is nine.

## Relationship to prior work

Mbirika and Spilker, *GCD of sums of k consecutive squares of generalized Fibonacci numbers* (arXiv:2204.12626, first submitted 26 April 2022), prove formulas for squares and ask in Section 6.1 about cube sums. The proposed factor-of-two split for even lengths is the reverse of the formula proved here; the present result establishes the exact invariant at **all** even lengths. The previously established first-power gcd formulas of Guyer and Mbirika (2021) are used only for context: they do not imply a cubic gcd. Frontczak (2018) provides formulas for sums of powers, including cubes, but not the infinite shifted-window gcd classification. Earlier formulas for cubic sums of Fibonacci numbers are compatible algebraic background, not a substitute for the primewise gcd and parity argument here.

## Limitations

Only the Fibonacci sequence with standard initial values and cubic powers is covered, and only even window lengths. No higher-power, Lucas-cube, or arbitrary-Gibonacci formula is claimed. The exact formulas and proof require no external computational certificates. A complete priority assessment cannot exclude unpublished or unindexed equivalent results; a separate independent review has not been performed.

## References

1. aBa Mbirika and Jürgen Spilker, *GCD of sums of k consecutive squares of generalized Fibonacci numbers*, arXiv:2204.12626v2 (2023 revision; originally submitted 2022-04-26), Section 6.1, https://arxiv.org/pdf/2204.12626.
2. Dan Guyer and aBa Mbirika, *GCD of Sums of k Consecutive Fibonacci, Lucas, and Generalized Fibonacci Numbers*, Journal of Integer Sequences 24 (2021), Article 21.9.8, https://cs.uwaterloo.ca/journals/JIS/VOL24/Mbirika/mb5.pdf.
3. Robert Frontczak, *Sums of powers of Fibonacci and Lucas numbers: A new bottom-up approach*, Notes on Number Theory and Discrete Mathematics 24 (2018), 94–103, https://nntdm.net/papers/nntdm-24/NNTDM-24-2-094-103.pdf.
4. Stuart Clary and Paul D. Hemenway, *On Sums of Cubes of Fibonacci Numbers*, Applications of Fibonacci Numbers 5 (1993), 123–136, DOI:10.1007/978-94-011-2058-6_12 (full text not inspected).
