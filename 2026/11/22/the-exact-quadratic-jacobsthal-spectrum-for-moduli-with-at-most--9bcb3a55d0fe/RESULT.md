# The exact quadratic Jacobsthal spectrum for moduli with at most two prime factors

## Finding

For each integer \(N\ge 2\), define the quadratic polynomial Jacobsthal function
\[
j_{T^2}(N)=\max\bigl\{m\ge 0:\text{some positive integer }x\text{ satisfies }\gcd(x+i^2,N)>1\ (1\le i\le m)\bigr\}.
\]
The maximum is finite for the moduli considered below. More precisely, put
\[
C_k(N)=\#\{x\bmod N:\gcd(x+i^2,N)>1\text{ for all }1\le i\le k\},\qquad C_0(N)=N.
\]
Suppose that \(N\) has one or two **distinct** prime factors and set \(R=\operatorname{rad}(N)\). Then for every integer \(k\ge0\),
\[
C_k(N)=\frac{N}{R}C_k(R).
\]
The complete values for \(k\ge1\) are as follows.

If \(R=p\) is prime, then
\[
C_1(p)=1,\qquad C_2(p)=\begin{cases}1,&p=3,\\0,&p\ne3,\end{cases}\qquad C_k(p)=0\quad(k\ge3).
\]
If \(R=pq\) with distinct primes \(p<q\), then
\[
\begin{aligned}
C_1(pq)&=p+q-1,\\
C_2(pq)&=\begin{cases}q,&p=3,\\2,&p\ne3,\end{cases}\\
C_3(pq)&=\begin{cases}1,&p\in\{2,3,5\},\\0,&p\ge7,\end{cases}\\
C_4(pq)=C_5(pq)&=\begin{cases}1,&p=3\text{ or }(p,q)=(2,3),\\0,&\text{otherwise},\end{cases}\\
C_k(pq)&=0\qquad(k\ge6).
\end{aligned}
\]
In particular,
\[
j_{T^2}(N)=
\begin{cases}
2,&R=3,\\
1,&R=p\ne3\text{ prime},\\
5,&R=pq,\ p=3\text{ or }(p,q)=(2,3),\\
3,&R=pq,\ p\in\{2,5\},\ q>3,\\
2,&R=pq,\ p\ge7.
\end{cases}
\]
For all \(k\ge0\), exactly \(C_k(N)-C_{k+1}(N)\) residue classes have an initial run of **exactly** \(k\) non-coprime shifted squares. Thus these formulas give the entire distribution of initial-run lengths. Whenever a two-prime radical supports three or more terms, exactly one residue class modulo that radical supports the third term, and the longest run is attained on exactly one class modulo the radical.

## Assumptions and scope

All primes are rational primes. Here \(\operatorname{rad}(N)\) is the product of the distinct primes dividing \(N\); \(p<q\) refers to the two primes in a two-prime radical. A polynomial shift is indexed by positive integers \(i=1,2,\ldots\), and \(x\) is a single fixed integer across the whole run. A class modulo \(N\) always has a positive representative. Prime powers are allowed, but the theorem makes no claim for radicals with three or more prime divisors. The invariant and its indexing agree with Kalmynin and Konyagin's definition in the cited paper.

## Proof

**Reduction to squarefree moduli.** For any integer \(z\), \(\gcd(z,N)>1\) if and only if \(\gcd(z,R)>1\). Hence each admissible class modulo \(R\) has exactly \(N/R\) admissible lifts modulo \(N\). This proves the scaling formula simultaneously for every \(k\), including \(k=0\).

**Local root fibers.** For prime \(\ell\), fixing \(x\bmod\ell\) covers precisely the indices \(i\) whose squares \(i^2\bmod\ell\) equal \(-x\bmod\ell\). The first six indices split into the following nonempty fibers:

| Prime | Fibers of equal squares among indices \(1,\ldots,6\) |
|---|---|
| \(2\) | \(\{1,3,5\}\), \(\{2,4,6\}\) |
| \(3\) | \(\{1,2,4,5\}\), \(\{3,6\}\) |
| \(5\) | \(\{1,4,6\}\), \(\{2,3\}\), \(\{5\}\) |

For \(\ell\ge7\), each fiber contains at most two indices among \(1,\ldots,6\), since \(i^2=a\) has at most two solutions in the field \(\mathbb F_\ell\), and the six indices are distinct modulo \(\ell\). Furthermore, indices \(1,2,3\) have three distinct squares modulo every prime \(\ell\ge7\), because their pairwise square differences are \(3,5,8\). These facts remain true even when \(\ell=7\), where a fiber can include \(\{3,4\}\).

**One prime.** Exactly one residue class \(x\bmod p\) covers \(i=1\), namely \(x=-1\). That same class covers \(i=2\) if and only if \(p\mid 4-1=3\), and cannot also cover \(i=3\), whose square differs from \(1\) by \(8\). This gives all single-prime counts.

**Two primes, first two indices.** By the Chinese remainder theorem (CRT), the number of pairs of residues covering \(i=1\) is \(q+p-1\): the first prime can cover it in one of \(q\) pairs and the second in one of \(p\) pairs, with one overlap. For \(i=1,2\), a single prime residue covers both precisely when the prime is \(3\). If \(p=3\), its one residue covers both and the \(q\)-residue is arbitrary, giving \(q\) pairs; no other pair covers both, since \(q>3\). Otherwise the two indices must be assigned to different primes, giving exactly two CRT pairs.

**Third index.** If both primes are at least \(7\), neither can cover two among \(1,2,3\), so \(C_3=0\). With \(p=2\), the first and third indices have equal squares only modulo \(2\); covering those two fixes the \(2\)-residue, and covering \(i=2\) fixes the \(q\)-residue. For \(q=3\) this is still the unique covering, because the other possible \(2\)-fiber covers only \(i=2\) and no \(3\)-fiber covers both indices \(1,3\). With \(p=3\), the common fiber for \(i=1,2\) fixes the \(3\)-residue, and \(i=3\) fixes the \(q\)-residue; no other assignment works for \(q>3\). With \(p=5\), the common fiber for \(i=2,3\) fixes the \(5\)-residue, and \(i=1\) fixes the \(q\)-residue; again no other assignment works because \(q\ge7\). Thus \(C_3=1\) exactly when \(p\le5\).

**Fourth and fifth indices.** Because \(C_4\le C_3\), only \(p\in\{2,3,5\}\) remains. For \(p=2,q>3\), the two \(2\)-fibers among the first four indices are \(\{1,3\}\) and \(\{2,4\}\). Their respective uncovered pairs \(\{2,4\}\) and \(\{1,3\}\) have square differences \(12\) and \(8\), so no odd prime \(q>3\) can cover either pair. For \(p=5,q\ge7\), the only \(5\)-fibers with two of the first four indices are \(\{1,4\}\) and \(\{2,3\}\). The respective uncovered pairs have square differences \(5\) and \(15\), so cannot be covered by \(q\ge7\); a singleton \(5\)-fiber also cannot suffice because a \(q\)-fiber covers at most two among four indices. Thus these cases have \(C_4=0\).

For \(p=3<q\), the unique class surviving three indices uses \(x\equiv-1\pmod3\), covering all indices not divisible by \(3\), and \(x\equiv-9\pmod q\), covering \(i=3\). It also covers \(i=4,5\), so \(C_4=C_5=1\). The exception \((p,q)=(2,3)\) has unique three-index survivor \(x\equiv5\pmod6\), also covering indices \(4,5\). These are all the cases.

**Sixth index and termination.** For \(p=3<q\), the unique five-index class has \(x+6^2\equiv 0\pmod3\) only if \(3\mid(-1+36)\), which is false since \(-1+36\equiv2\pmod3\). Modulo \(q\) its residue is \(-9+36=27\), nonzero for every prime \(q>3\). For \(R=6\), the unique five-index class is \(x\equiv5\pmod6\); then \(x+36\equiv5\pmod6\) is coprime to \(6\). Thus \(C_6=0\) in every case. Since \(C_{k+1}\le C_k\), all further counts vanish. The maximum \(j_{T^2}(N)\) is the largest \(k\) with \(C_k(N)>0\), and the exact-length frequency assertion follows by subtracting nested survivor sets. This completes the proof.

## Verification

The accompanying `verify_quadratic_jacobsthal.py` uses only the Python 3 standard library. It independently evaluates \(\gcd(x+i^2,N)\) over every class for all \(2\le N\le1600\) with at most two distinct prime factors (1,059 moduli), and separately compares direct computations against CRT-local fiber enumeration over all 210 prime pairs \(p<q<79\). All six count formulas agree in these finite checks. To reproduce, run `python3 verify_quadratic_jacobsthal.py`. The finite check is diagnostic; the preceding CRT and fiber argument establishes all primes, exponents, and lengths.

## Relationship to prior work

Kalmynin and Konyagin introduced this polynomial analogue of the Jacobsthal function and investigated lower bounds on \(j_f(P(y))\) when \(P(y)\) ranges over primorials, with sieve and Galois-theoretic tools. Their Theorem 1 and subsequent proofs address growing collections of prime factors; that asymptotic bound does not supply the present complete two-prime-support spectrum or the distribution of qualifying residue classes. Here the proof is an exact local-cover classification for the specific polynomial \(T^2\), including prime-power multiplicities. Literature and research-record comparisons have not located a stronger theorem implying these exact formulas; this is a best-knowledge comparison, not a logical proof of worldwide novelty.

## Limitations

No assertion is made for three or more distinct prime factors or for polynomials other than \(T^2\). The exact counts are for **initial runs** beginning at \(i=1\), not arbitrary intervals of indices. These counts do not determine the distribution of maximal runs starting at arbitrary positions, nor do they give prime-gap estimates. Independent validation has not been performed. A previously unindexed treatment of these elementary low-support cases remains possible.

## References

1. A. Kalmynin and S. Konyagin, *A polynomial analogue of Jacobsthal function*, arXiv:2302.00459 (first public version 1 February 2023), https://arxiv.org/abs/2302.00459; *Izvestiya: Mathematics* **88** (2024), 225–235, https://doi.org/10.4213/im9467e.
2. Original definition, main theorem, and proof in the accessible preprint, https://arxiv.org/pdf/2302.00459.
