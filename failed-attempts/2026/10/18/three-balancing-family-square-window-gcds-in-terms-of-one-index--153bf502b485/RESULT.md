# Three balancing-family square-window gcds in terms of one index divisor

## Finding
Let \(B_0=0,B_1=1\) and \(C_0=1,C_1=3\), with both sequences satisfying \(X_{n+2}=6X_{n+1}-X_n\). Let \(Q_0=Q_1=1\), \(Q_{j+2}=2Q_{j+1}+Q_j\), and define the Lucas-cobalancing sequence \(c_n=Q_{2n-1}\) for \(n\ge1\). For \(X\) equal to \(B,C,c\), put
\[
\mathcal G_X(k)=\gcd_{n\ge0}\sum_{i=1}^kX_{n+i}^2,\quad k\ge1,
\qquad H(k)=\gcd(k,B_k).
\]
Then, for every \(k\ge1\),
\[
\boxed{\mathcal G_B(k)=\frac{H(k)}{2^{\mathbf 1_{2\mid k}}},\qquad
\mathcal G_C(k)=H(k),\qquad
\mathcal G_c(k)=3^{\mathbf 1_{k\equiv3\pmod6}}H(k).}
\]
The fractions on the right are integers. In particular, each of these three square-window gcds divides its window length \(k\); for odd multiples of three, the third gcd has exactly one factor of three.

## Assumptions and scope
The indices \(k\) are positive integers, window starting offsets \(n\) are all nonnegative integers, and all gcds are positive gcds of the indicated infinite sets. The balancing numbers \(B_n\), Lucas-balancing numbers \(C_n\), and Lucas-cobalancing numbers \(c_n\) use the conventions above. The fourth square-window family of ordinary cobalancing numbers is not classified here. The statement identifies the three gcds through the readily specified common divisor \(H(k)\), not a factorization-free elementary formula for \(H(k)\).

## Proof
**1. Closed window sums.** The standard Pell companion identities give
\[
16 B_j^2=C_{2j}-1,\qquad 2C_j^2=C_{2j}+1,\qquad
2c_j^2=C_{2j-1}-1.
\]
They follow directly from \(B_j=(r^j-r^{-j})/(4\sqrt2)\) and \(C_j=(r^j+r^{-j})/2\), with \(r=3+2\sqrt2\), and from the companion Pell identity \(c_j=Q_{2j-1}\). Summing the two geometric progressions, for all \(n\ge0,k\ge1\), yields
\[
\sum_{i=1}^kC_{2n+2i}=B_k C_{2n+k+1},\qquad
\sum_{i=1}^kC_{2n+2i-1}=B_k C_{2n+k}.
\]
Consequently the three sums inside the gcd are, respectively,
\[
\frac{B_k C_{2n+k+1}-k}{16},\qquad
\frac{B_k C_{2n+k+1}+k}{2},\qquad
\frac{B_k C_{2n+k}-k}{2}.\tag{1}
\]

**2. Exact gcd of the companion subsequence differences.** Fix any nonnegative integer \(j\). The sequence \(E_n=C_{2n+j}\) satisfies \(E_{n+2}=34E_{n+1}-E_n\). Its adjacent differences satisfy the same recurrence; the integer transition matrix has determinant one. Thus the gcd of all adjacent differences equals the gcd of the first two, and equals \(\gcd_{n\ge0}(E_n-E_0)\). This gcd depends only on the parity of \(j\), because shifting \(j\) by two shifts the recurrence by one step and preserves the gcd. At \(j=0\) the first differences are \(16,560\); at \(j=1\) they are \(96,3264\). Hence
\[
D_j:=\gcd_{n\ge0}(C_{2n+j}-C_j)=
\begin{cases}16,&j\text{ even},\\96,&j\text{ odd}.\end{cases}\tag{2}
\]
For any integers \(A,M\), the gcd of the numbers \(A+B_k(C_{2n+j}-C_j)\), over all \(n\ge0\), is \(\gcd(A,B_k D_j)\). Applying this to (1) gives the **exact finite identities**
\[
\begin{split}
16\mathcal G_B(k)&=\gcd(B_kC_{k+1}-k,D_{k+1}B_k),\\
2\mathcal G_C(k)&=\gcd(B_kC_{k+1}+k,D_{k+1}B_k),\\
2\mathcal G_c(k)&=\gcd(B_kC_k-k,D_kB_k).
\end{split}\tag{3}
\]
No finite-search assumption is made in (2) or (3).

**3. The prime two.** The recurrences and the identities \(C_{j+2}-C_j=16B_{j+1}\) and \(B_{j+2}-B_j=2C_{j+1}\) imply
\[
C_{2u}\equiv1\pmod {16},\quad C_{2u+1}\equiv3\pmod {16},\quad B_{2u+1}\equiv2u+1\pmod {16}.
\]
Also \(B_{2u}=2B_uC_u\). If \(k=2^a u\) with \(u\) odd and \(a\ge1\), repeated doubling gives
\[
B_k=2^a B_u\prod_{j=0}^{a-1}C_{2^ju}\equiv3k\pmod{2^{a+4}}.\tag{4}
\]
It follows that \(\nu_2(B_k)=\nu_2(k)=a\) for even \(k\), and the same equality (both zero) holds for odd \(k\). When \(k\) is even, (4) gives
\[
\nu_2(B_k C_{k+1}-k)=a+3,\qquad
\nu_2(B_k C_{k+1}+k)=a+1,\qquad
\nu_2(B_k C_k-k)=a+1.\tag{5}
\]
Indeed \(C_{k+1}\equiv3\) and \(C_k\equiv1\pmod{16}\). When \(k\) is odd, \(B_k\equiv k\pmod{16}\), so
\[
16\mid B_kC_{k+1}-k,\quad
\nu_2(B_kC_{k+1}+k)=1,\quad
\nu_2(B_kC_k-k)=1.\tag{6}
\]
Taking the two-adic parts in (3) yields, respectively, \(a-1,a,a\) for even \(k\), and zero for all three gcds for odd \(k\), as asserted.

**4. All odd primes.** For a prime \(\ell\ge5\), the integers \(D_k,D_{k+1}\) are units modulo \(\ell\). Since each first argument in (3) is congruent to \(\pm k\) modulo \(B_k\), its \(\ell\)-part in (3) is exactly \(\ell^{\min(\nu_\ell(k),\nu_\ell(B_k))}\), the corresponding part of \(H(k)\).

For \(\ell=3\), the recurrence modulo three gives \(3\mid C_j\) if and only if \(j\) is odd. For odd \(k\), \(3\nmid B_k\); the first two formulas in (3) have \(D_{k+1}=16\) and therefore no factor of three, while the third has \(D_k=96\). Its first argument is \(-k\) modulo three, so it contributes **one** factor of three exactly when \(3\mid k\). For even \(k\), writing \(b=\nu_3(k)\), we have \(\nu_3(B_k)\ge b+1\): first use \(B_{2u}=2B_uC_u\) for odd \(u\) and then the doubling identity; each factor of three in the index adds a factor of three through \(B_{3j}=B_j(4C_j^2-1)\), since \(j\) stays even and \(C_j^2\equiv1\pmod3\). Thus \(\nu_3(B_kC_{k+1}\pm k)=b\), since \(C_{k+1}\) is odd-indexed and divisible by three. The first two gcds in (3) therefore have exactly the same three-part as \(H(k)\). For the third gcd, \(D_k=16\) and \(B_kC_k-k\equiv-k\pmod{3^{b+1}}\), so its three-part also equals that of \(H(k)\).

Combining the prime parts proves all three formulas. Finally, when \(k\equiv3\pmod6\), \(B_k\) is prime to three, so \(H(k)\mid k/3\); this proves that the third displayed gcd also divides \(k\). \(\square\)

## Verification
The standalone script `verify.py`, run using Python 3, computes the defining recurrences and directly takes gcds of the first three square-window sums at every \(1\le k\le240\). All three resulting values match the formulas, and additional windows are checked independently. The first-three reduction is justified independently by the order-three integer recurrence for each square sequence; the proof above does not rely on the finite test. The script additionally checks the formulas for window sums and the critical two-adic congruences, totaling 7,620 exact assertions.

## Relationship to prior work
Mbirika, Schrader, and Spilker (2023), Section 6.1, Question 30, ask for formulas for the square-window gcds of balancing, Lucas-balancing, cobalancing, and Lucas-cobalancing numbers. Their displayed observations **already suggest** that the first and second gcds differ by a factor two for even \(k\), and the second and third differ by a factor three for \(k\equiv3\pmod6\). Those numerical observations are not claimed as new. The new statement identifies all three gcds directly with the explicit arithmetic invariant \(\gcd(k,B_k)\) and proves them for every positive \(k\), including the exact two- and three-adic boundary factors. It resolves three of the four stated families in this index-gcd sense. The 2022 paper of Mbirika and Spilker treats generalized Fibonacci recurrences \(G_{n+2}=G_{n+1}+G_n\), not these three balancing-family square-window formulas.

## Limitations
The gcd \(\gcd(k,B_k)\) is not replaced by a factorization-free expression depending only on congruence classes of \(k\); the original article separately asks about simplifying such term-index gcds. The ordinary cobalancing square-window gcd is not covered. Literature comparisons do not rule out an equivalent derivation outside inspected sources. No independent audit is represented by the checks reported here.

## References
1. aBa Mbirika, Janee Schrader, and Jürgen Spilker, *Pell and Associated Pell Braid Sequences as GCDs of Sums of k Consecutive Pell, Balancing, and Related Numbers*, Journal of Integer Sequences 26 (2023), Article 23.6.4, especially §2, §6.1, Question 30. https://cs.uwaterloo.ca/journals/JIS/VOL26/Mbirika/mbir5.pdf (arXiv:2301.05758; first submitted 2023-01-13).
2. aBa Mbirika and Jürgen Spilker, *GCD of Sums of k Consecutive Squares of Generalized Fibonacci Numbers*, Fibonacci Quarterly 60 (2022), 255–269. https://arxiv.org/pdf/2204.12626 (first submitted 2022-04-26).
3. OEIS A001109 (balancing numbers), A001541 (Lucas-balancing), A002315 (Lucas-cobalancing). https://oeis.org/A001109 ; https://oeis.org/A001541 ; https://oeis.org/A002315 .
