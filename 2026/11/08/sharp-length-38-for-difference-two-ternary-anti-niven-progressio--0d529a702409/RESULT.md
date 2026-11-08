# Sharp length \(38\) for difference-two ternary anti-Niven progressions

## Finding
For a nonnegative integer \(n\), let \(s_3(n)\) be its sum of digits in base \(3\). A positive integer \(n\) is ternary anti-Niven when \(\gcd(n,s_3(n))=1\). Then the greatest length of an arithmetic progression of positive ternary anti-Niven integers with common difference \(2\) is exactly \(38\). More precisely, for any positive integer \(a\) and length \(L\ge1\),
\[
 \gcd(a+2j,s_3(a+2j))=1\quad(0\le j<L)
 \quad\Longrightarrow\quad L\le38.
\]
The bound is attained by \(a=86699\): all \(38\) terms \(86699,86701,\ldots,86773\) are ternary anti-Niven.

## Assumptions and scope
The numerals use their ordinary nonnegative base-three expansions, without leading-zero restrictions (leading zeros do not affect the digit sum). The starting integer is positive, the difference is exactly \(2\), and no restriction is placed on the number of digits. The theorem gives a global maximum over all starting values, not a classification or count of maximizing starts.

## Proof
**Digit-sum lemma.** Among any \(13\) consecutive positive odd integers, at least one has base-three digit sum divisible by \(3\).

Write the initial odd integer as \(27q+r\), with \(q\ge0\) and \(0\le r<27\). Its \(13\) odd-spaced terms are \(27q+r+2j\), \(0\le j\le12\). As \(r+24\le50\), all these terms lie in the two neighboring blocks indexed by \(q\) and \(q+1\). For each term, the base-three block identity gives
\[
 s_3(27q+r+2j)=s_3\!\left(q+\left\lfloor\frac{r+2j}{27}\right\rfloor\right)
 +s_3((r+2j)\bmod 27).
\]
For every possible \(r\), the following *fixed* three indices lie within **one** of these two blocks and the residues of their lower-block digit sums modulo \(3\) are exactly \(0,1,2\), respectively. In the table `L` means that all three integer values \(r+2j\) are below \(27\); `R` means that all three are at least \(27\). The columns `j0,j1,j2` give indices whose lower-block digit sums are \(0,1,2\) modulo \(3\).

```
r   block  j0 j1 j2
 0    L     0  4  1
 1    L     2  0  8
 2    L    12  3  0
 3    L     1  0  7
 4    L    11  2  0
 5    L     0  2  6
 6    L    10  1  0
 7    L     0  1  5
 8    L     9  0  1
 9    L     1  0  4
10    L     8  2  0
11    R     8 12  9
12    L     7  1  0
13    R     7 11  8
14    L     6  0  2
15    R     6 10  7
16    L     5  0  1
17    R     5  9  6
18    L     4  1  0
19    R     4  8  5
20    R     6  4 12
21    R     3  7  4
22    R     5  3 11
23    R     2  6  3
24    R     4  2 10
25    R     1  5  2
26    R     3  1  9
```

This is a complete elementary finite table: it follows by using the three-digit residues \(s_3(t)\bmod3\) for \(0\le t<27\), namely

```
t = 0..26:
0 1 2 1 2 0 2 0 1 1 2 0 2 0 1 0 1 2 2 0 1 0 1 2 1 2 0
```

At the indicated three positions, the upper-block contribution to \(s_3\) is a **single constant**, either \(s_3(q)\) or \(s_3(q+1)\). Adding a common constant modulo \(3\) to the three residues \(0,1,2\) necessarily produces a zero. This proves the lemma for arbitrary \(q\), including carries at block boundaries.

**Upper bound.** Because \(3\equiv1\pmod2\), every positive integer and its base-three digit sum have the same parity. Consequently an even integer has even, positive digit sum and is not ternary anti-Niven. Every term in an anti-Niven progression of difference \(2\) must therefore be odd.

Take any \(39\) consecutive odd integers at difference \(2\). Exactly \(13\) of them are multiples of \(3\); those \(13\) multiples form an arithmetic progression of step \(6\). Dividing by \(3\) gives \(13\) consecutive odd integers of step \(2\). By the lemma one of these quotients, say \(u\), has \(3\mid s_3(u)\). But \(s_3(3u)=s_3(u)\), so \(\gcd(3u,s_3(3u))\ge3\). Thus no \(39\)-term difference-two progression is entirely anti-Niven, and no longer one is either.

**Attainment.** For \(a=86699\), the digit sums \(s_3(a+2j)\) for \(j=0,\ldots,37\), in order, are

```
11 11 11 13 11 11 13 13 11 13 13 13 15 11 11 13 13 11 13
13 13 15 13 13 15 15 5 7 7 7 9 7 7 9 9 7 9 9
```

Direct Euclidean calculations give \(\gcd(a+2j,s_3(a+2j))=1\) for all the \(38\) indices. The self-contained script verifies these \(38\) checks in full integer arithmetic. It also confirms that the neighboring terms \(86697\) and \(86775\) are not anti-Niven, though this is not required for the global maximum. The upper and lower bounds coincide.

## Verification
Run `python3 verify.py` using an ordinary Python 3 interpreter. The script checks every one of the \(27\) residue triples, separately exhausts \(27\cdot3\cdot3=243\) choices of lower-block residue and independently variable upper-block digit sums, and verifies the \(38\)-term witness with two digit-sum implementations. It additionally samples \(5000\) small odd starts as a stress test. The symbolic block argument, rather than the sample, establishes the infinite upper bound. The captured output is in `verification_output.txt`.

## Relationship to prior work
Blau, Harrington, Lohrey, Sosis and Wong, *Arithmetic Progressions of Integers that are Relatively Prime to their Digital Sums* (arXiv:2308.05228v1, 2023), formulate anti-Niven arithmetic progressions. Their Theorem 4.1 proves a lower bound of \(b\) for common difference \(2\) when \(b=2^r+1\); their concluding remarks explicitly state that they have not established an upper bound for this class. For \(b=3\), the present result supplies the **exact** sharp value \(38\). Their Theorem 3.3 concerns bases for which \(b-1\) has an odd prime divisor, which excludes \(3\).

Harrington, Litman and Wong, *Every Arithmetic Progression Contains Infinitely Many \(b\)-Niven Numbers* (arXiv:2303.06534v1, 2023), concern integers for which the digit sum **divides** the integer, rather than integers **coprime** to their digit sum, and therefore do not imply this maximum. OEIS A064150 lists ternary Niven numbers and does not supply the sharp anti-Niven progression bound. The base-\(3\) special case of the published lower-bound theorem is substantially weaker than this exact classification.

## Limitations
No inference is made for other bases, other differences, or progressions with arbitrary signs. The result does not enumerate maximizing starts, nor assert their infinitude. The finite certificate and witness are checked in integer arithmetic; there has been no independent scientific audit. Relevant but unindexed equivalent prior work remains a possible originality risk.

## References
1. R. Blau, J. Harrington, S. Lohrey, E. Sosis and T. W. H. Wong, *Arithmetic Progressions of Integers that are Relatively Prime to their Digital Sums*, arXiv:2308.05228v1, first posted 2023-08-09, especially Theorems 3.3 and 4.1 and concluding remarks. https://arxiv.org/pdf/2308.05228
2. J. Harrington, M. Litman and T. W. H. Wong, *Every Arithmetic Progression Contains Infinitely Many \(b\)-Niven Numbers*, arXiv:2303.06534v1, first posted 2023-03-12. https://arxiv.org/pdf/2303.06534
3. OEIS Foundation, A064150, *Numbers divisible by the sum of their ternary digits*. https://oeis.org/A064150
