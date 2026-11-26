# The squareful three-prime \(2\)-near-perfect classification

## Finding

For odd primes \(3\le p<q\), let \(n=2p^2q\). Then \(n\) is \(2\)-near-perfect (with *exactly two distinct* omitted positive divisors) if and only if
\[
 n\in\{90,126,198,550\}.
\]
In each case the unordered omitted-divisor pair is unique:
\[
\begin{array}{c|c|c|c}
n & (p,q) & \sigma(n)-2n & \{d_1,d_2\}\\\hline
90&(3,5)&54&\{9,45\}\\
126&(3,7)&60&\{18,42\}\\
198&(3,11)&72&\{6,66\}\\
550&(5,11)&16&\{5,11\}
\end{array}
\]
These omitted divisors are all proper. This is a complete classification over unbounded primes, not merely an enumeration up to a numerical cutoff.

## Assumptions and scope

Here \(\sigma(n)=\sum_{d\mid n}d\), and a positive integer is \(2\)-near-perfect when
\[
 \sigma(n)=2n+d_1+d_2,
 \qquad d_1,d_2\mid n,\quad d_1,d_2>0,\quad d_1\ne d_2.
\]
The theorem is restricted to the natural first nonsquarefree odd-part layer \(2p^2q\) with two *distinct* odd prime factors \(p<q\). The condition \(d_i<n\) is automatic for every candidate satisfying the defining equality in this layer, because the surplus is strictly smaller than \(n\). No assertion is made for \(2^ap^bq^c\) with other exponents or for odd integers.

## Proof

Multiplicativity gives, for every permitted \(p,q\),
\[
\begin{aligned}
\Delta(p,q)&:=\sigma(2p^2q)-4p^2q\\
 &=3(p^2+p+1)(q+1)-4p^2q\\
 &=(3+3p-p^2)q+3(p^2+p+1).
\end{aligned}
\]
For \(p\ge7\), the coefficient of \(q\) is negative, and two distinct odd primes satisfy \(q\ge p+2\). Therefore
\[
\Delta(p,q)\le (3+3p-p^2)(p+2)+3(p^2+p+1)
=-p^3+4p^2+12p+9<0.
\]
The final polynomial is \(-54\) at \(p=7\), and its successive integer differences are \(-3p^2+5p+15<0\) for every integer \(p\ge7\). Thus only \(p=3\) or \(p=5\) can be \(2\)-near-perfect.

If \(p=5\), then \(\Delta(5,q)=93-7q\). Since a sum of two distinct positive divisors is at least \(3\), we need \(q\le12\). The only odd primes \(q>5\) are \(7\) and \(11\). The proper divisors of \(350=2\cdot5^2\cdot7\) are
\[
1,2,5,7,10,14,25,35,50,70,175,
\]
no two distinct members of which sum to \(44\). For \(550=2\cdot5^2\cdot11\), the surplus is \(16=5+11\), giving one valid pair. Its uniqueness follows by checking the proper divisors
\[
1,2,5,10,11,22,25,50,55,110,275.
\]
(Alternatively \(q=13\) has surplus only \(2\), so it also fails, and every larger prime has nonpositive surplus.)

If \(p=3\), then \(\Delta(3,q)=3q+39\). The positive proper divisors of \(18q\), for every prime \(q>3\), are exactly
\[
A\cup qB,\qquad A=\{1,2,3,6,9,18\},\quad B=\{1,2,3,6,9\}.
\]
When \(q\ge17\), a pair taken from \(A\) has sum at most \(27<3q+39\). A mixed pair has form \(a+bq\), where \(a\in A\), \(b\in B\). If \(b\le3\), it is at most \(3q+18\), too small; if \(b\ge6\), it is at least \(6q+1>3q+39\), too large. A pair from \(qB\) would force \(q\mid39\), impossible for prime \(q\ge17\). Consequently \(q\in\{5,7,11,13\}\).

For \(q=13\), the target surplus is \(78=6q\). An \(A+A\) pair is too small; the same mixed-pair inequalities apply for \(q=13\), since \(6q+1>3q+39\). For a \(qB+qB\) pair, two *distinct* coefficients in \(B\) would have to sum to \(6\), which never occurs. Thus \(q=13\) fails. For \(q=5,7,11\), direct divisor comparison gives precisely the three unique pairs in the displayed table. The \(p=5\) branch provides the fourth case, completing the proof. \(\square\)

## Verification

The accompanying standalone `verify.py` independently enumerates the positive divisors by a square-root method and by the prime-power Cartesian product, verifies all seven explicitly reduced prime pairs, checks their unique omitted pairs, and checks \(4371\) ordered distinct odd-prime pairs below \(500\). The output is

`VERIFY_OK finite_prime_pairs= 4371 admissible_pairs= 4 small_cases= 7`

The unbounded exclusion of all other primes is the algebraic argument in the Proof, not an inference from these finite tests. Running with `python3 verify.py` needs only the Python standard library.

## Relationship to prior work

Aryan, Madhavani, Parikh, Slattery and Zelinsky introduced systematic classifications of \(2\)-near-perfect numbers with two prime factors and an odd-prime exponent at most two [1]. Fearon, Foushee, Porosoff, Skula, Zelinsky and Zhang completed the two-prime-support classification [2]; their Section 6.2 gives examples of three-prime-support numbers and explicitly identifies classification of such families as future work. The squarefree three-prime slice \(2pq\) was previously classified [3] as giving exactly \(30\) and \(66\). The present theorem treats the first squareful odd-prime exponent, rather than an instance of either two-prime-support result or the squarefree classification. OEIS A341475 lists the four numerical values among other \(2\)-near-perfect integers but supplies no unbounded classification of this shape [4].

## Limitations

The theorem makes no claim for other three-prime exponent patterns, in particular \(2p^aq^b\) with \(a,b>1\) or \(2^kp^2q\) with \(k>1\). The complete result is elementary and narrow. Previously published unindexed equivalent classifications remain a bibliographic possibility; independent mathematical validation and independent priority assessment have not occurred.

## References

[1] V. Aryan, D. Madhavani, S. Parikh, I. Slattery, J. Zelinsky, *On 2-Near Perfect Numbers*, arXiv:2310.01305 (first public version 2023-10-02); Integers **24** (2024), A61. https://arxiv.org/abs/2310.01305

[2] R. Fearon, H. Foushee, B. Porosoff, A. Skula, J. Zelinsky, K. Zhang, *Complete characterization of 2-near perfect numbers with exactly 2 prime factors*, arXiv:2508.06651 (first public version 2025-08-08), §6.2. https://arxiv.org/html/2508.06651v3

[3] *Squarefree 2-near-perfect numbers with three prime factors*, published mathematical research record (2026); the \(2pq\) classification, separate from the \(2p^2q\) classification.

[4] OEIS Foundation, *A341475: 2-near-perfect numbers*, https://oeis.org/A341475 (finite listed terms and cited references; no claim of exhaustive support-shape classification).
