# Sharp anti-Niven progressions for short even strides in odd bases

## Finding

Write \(s_b(n)\) for the ordinary base-\(b\) digit sum of a positive integer \(n\). A positive integer is *\(b\)-anti-Niven* if \(\gcd(n,s_b(n))=1\).

**Theorem.** Let \(b\ge3\) be odd and let \(d\ge2\) be even. Assume that at least one prime divisor of \(b-1\) does not divide \(d\), and let \(p\) be the least such prime. If
\[
(p-2)d\le b+1,
\]
then the maximum number of terms in a \(b\)-anti-Niven arithmetic progression of difference \(d\) is exactly \(p-1\). There are infinitely many distinct starting values of progressions attaining this maximum.

In particular, for **every odd base** \(b\) for which \(5\mid b-1\) and \(3\nmid b-1\), the maximum length for difference \(d=4\) is exactly four and is attained infinitely often. The condition on \(b\) forces \(b\ge11\), for which \((5-2)4=12\le b+1\).

## Assumptions and scope

The base \(b\), difference \(d\), and prime \(p\) are ordinary positive integers, with the parity and divisibility restrictions stated above. Progressions mean \(n,n+d,\ldots,n+(t-1)d\) with positive starting integer \(n\) and fixed difference \(d\). The conclusion concerns the **maximum finite length** over all starts, not a single infinite progression. No assumption about the primality of \(b\), the size of any prime factor of \(b-1\), or coprimality with any auxiliary product is made.

## Proof

Put \(N=b-1\) and \(t=p-1\). Since \(b\) is odd and \(d\) is even, \(2\mid N,d\), and therefore \(p\) is odd. We construct a residue \(c\in\{0,\ldots,N-1\}\) satisfying
\[
\gcd(N,1+c+jd)=1\quad(0\le j\le p-2).\tag{1}
\]
For each prime \(q\mid N\), consider the forbidden residues of \(c\pmod q\) given by \(1+c+jd\equiv0\pmod q\). If \(q\mid d\), there is just one forbidden residue. If \(q\nmid d\), minimality of \(p\) implies \(q\ge p\), while at most \(p-1<q\) residues are forbidden. Thus at least one residue modulo each prime \(q\mid N\) is permitted. Lift it arbitrarily to a residue modulo the full power of \(q\) dividing \(N\), and apply the Chinese remainder theorem to obtain \(c\) as in (1).

For \(0\le j\le p-2\) set \(x_j=c+jd\). Our numerical hypothesis gives
\[
0\le x_j\le (b-2)+(p-2)d\le2b-1.
\]
Hence \(e_j=\lfloor x_j/b\rfloor\) is either zero or one, and the two-digit expression for \(x_j\) gives
\[
s_b(x_j)=x_j-(b-1)e_j.
\]
Define \(S_j=1+s_b(x_j)\). Then (1) implies
\[
\gcd(N,S_j)=\gcd(N,1+x_j)=1.\tag{2}
\]

The finite collection of positive integers \(S_0,\ldots,S_{p-2}\) determines a finite set of prime divisors. Choose arbitrarily large integers \(m\) such that
\[
b^m\equiv b\pmod q
\quad\text{for every prime }q\mid\prod_{j=0}^{p-2}S_j.\tag{3}
\]
Such \(m\) exist: for primes \(q\nmid b\) one may take \(m\equiv1\pmod{q-1}\) by Fermat's theorem, while for \(q\mid b\) the congruence in (3) holds for every positive \(m\). Taking a common multiple of the finitely many \(q-1\)'s yields infinitely many common exponents. Also choose \(m\) large enough that \(b^m>x_{p-2}\).

Set \(n_j=b^m+x_j\). The high digit \(1\) is separated from the lower base-\(b\) representation of \(x_j\), so \(s_b(n_j)=S_j\). If a prime \(q\) divided both \(n_j\) and \(S_j\), congruence (3) would give
\[
0\equiv n_j-S_j
\equiv b+x_j-(1+x_j-(b-1)e_j)
=(b-1)(1+e_j)\pmod q.
\]
But \(1+e_j\in\{1,2\}\), and \(2\mid b-1\). Thus every prime divisor of \((b-1)(1+e_j)\) also divides \(N\), contradicting (2). Hence \(\gcd(n_j,s_b(n_j))=1\) for every \(j\). Letting \(m\) grow through the common congruence class in (3) gives infinitely many distinct starts \(b^m+c\) and therefore the required lower bound \(p-1\).

For the matching upper bound, since \(p\mid b-1\) and \(p\nmid d\), each block of \(p\) consecutive terms of a difference-\(d\) progression contains a multiple of \(p\). Because \(b\equiv1\pmod p\), every integer \(v\) satisfies \(s_b(v)\equiv v\pmod p\). Such a multiple is not \(b\)-anti-Niven. Therefore no progression has \(p\) anti-Niven terms. Combining the upper bound with the construction finishes the proof. \(\square\)

## Verification

The included `check.py` is a standalone Python 3 standard-library script. It enumerates every odd base \(3\le b\le301\) and even difference \(2\le d\le42\) meeting the theorem's hypotheses, finds a permissible CRT residue by exact gcd arithmetic, checks every two-digit bound, and verifies the resulting witness condition by exact modular exponentiation for \(1343\) admissible pairs. In bases \(11\) and \(21\) with difference \(4\), the script additionally constructs the integers themselves and recomputes their digit sums and gcds. The recorded standard output is embedded as `check_output.txt`. These finite calculations are independent checks of examples; the proof above establishes all quantified cases.

For illustration, the algorithm gives \((b,d,p,c,m)=(11,4,5,8,7)\), with four digit sums \(9,3,7,11\). It also yields \((71,4,5,18,991)\), for which a previously restrictive auxiliary coprimality condition is not available. The theorem itself imposes no such condition.

## Relationship to prior work

Blau, Harrington, Lohrey, Sosis, and Wong introduced \(b\)-anti-Niven \(d\)-progressions and established the general \(p-1\) upper bound in their Theorem 2.5. Their Theorem 3.3 constructs infinitely many extremal progressions for \(d=2\). Their Conjecture 4.3 proposes attainability for **all** even differences in suitable odd bases. The theorem above proves the conjectured sharp value throughout the stated region of the \((b,d,p)\)-parameter space and, in particular, handles every permissible base for \(d=4,p=5\). The upper bound is cited as known, although it is re-proved here for completeness.

## Limitations

The inequality \((p-2)d\le b+1\) is a sufficient range for this construction; no necessity is asserted. For larger differences the base-\(b\) addition may produce more than one carry and the argument does not settle Conjecture 4.3. The theorem does not apply when every prime divisor of \(b-1\) divides \(d\), nor does it assert the existence of an infinite progression with one fixed starting value. Independence and exhaustive novelty have not been established; unindexed equivalent work remains a literature risk.

## References

Ryan Blau, Joshua Harrington, Sarah Lohrey, Eliel Sosis, and Tony W. H. Wong, *Arithmetic progressions of integers that are relatively prime to their digital sums*, arXiv:2308.05228, first publicly submitted 2023-08-09; see Theorems 2.5, 3.3 and Conjecture 4.3. https://arxiv.org/abs/2308.05228

The 2026 journal version is *Rocky Mountain Journal of Mathematics* 56 (2026), 13–21, according to the authors' publication listing. This later date is not used as the first-public-date anchor.
