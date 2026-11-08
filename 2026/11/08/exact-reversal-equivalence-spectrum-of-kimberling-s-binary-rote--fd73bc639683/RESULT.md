# Exact reversal-equivalence spectrum of Kimberling’s binary Rote word

## Finding

Let \(\varphi:\{0,1,2\}^*\to\{0,1,2\}^*\) and \(\pi:\{0,1,2\}^*\to\{0,1\}^*\) be the morphisms
\[
\varphi(0)=01,\qquad \varphi(1)=02,\qquad \varphi(2)=0,
\quad \pi(0)=100,\quad\pi(1)=101,\quad\pi(2)=10.
\]
Set \(\mathbf T=\varphi^\omega(0)\) and \(\mathbf B=0\pi(\mathbf T)\). The latter is Kimberling’s infinite binary word. For every integer \(n\ge1\), let \(\mathcal L_n\) be its set of contiguous factors of length \(n\). Let \(P(n)=\#\{w\in\mathcal L_n:w=w^R\}\) and let \(Q(n)\) count unordered two-element pairs \(\{w,w^R\}\subseteq\mathcal L_n\) with \(w\ne w^R\). Let \(r(n)\) be the number of reversal-equivalence classes met by \(\mathcal L_n\).

**Theorem.** For \(1\le n\le9\), the ordered spectra are
\[
(P(1),\ldots,P(9))=(2,2,2,2,2,1,2,1,1),
\qquad (Q(1),\ldots,Q(9))=(0,1,2,2,2,3,2,1,0).
\]
For all integers \(n\ge10\), \(P(n)=Q(n)=0\). The word has exactly \(15\) distinct nonempty palindromic factors, with maximum length \(9\), and its reflection complexity satisfies
\[
r(n)=2n-Q(n)\quad(n\ge1),\qquad r(n)=2n\quad(n\ge10).
\]
In particular, no factor of length at least \(10\) has its reverse anywhere in \(\mathbf B\).

## Assumptions and scope

The factors are contiguous (not scattered). Reversal \(w^R\) reverses the letters without exchanging \(0\) and \(1\). A pair counted by \(Q(n)\) contains two distinct occurring factors and is counted once; an absent reverse produces no pair. Reflection complexity counts orbits intersecting the factor language, even when the language is not reversal-closed. All lengths are positive integers. The identity \(\mathbf B=0\pi(\mathbf T)\) and the ordinary factor complexity \(\#\mathcal L_n=2n\) are established in [1], Theorems 2 and 5, respectively.

## Proof

**1. Exact two-factor language of \(\mathbf T\).** Its set of length-two factors is
\[
\mathcal S_2=\{00,01,02,10,20\}.
\]
Indeed \(01\) occurs in \(\varphi(0)\). Iteratively substituting both letters of any occurring pair gives only pairs in \(\mathcal S_2\): the length-two factors of \(\varphi(00)\), \(\varphi(01)\), \(\varphi(02)\), \(\varphi(10)\), and \(\varphi(20)\) are, respectively, \(\{01,10\}\), \(\{01,10,02\}\), \(\{01,10\}\), \(\{01,02,20\}\), and \(\{00,01\}\). Closure from \(01\) generates all five pairs, and no other pair is possible by induction along substituted prefixes. Every generated pair occurs in some finite substituted prefix; hence the displayed language is exact.

**2. Exact six-factor language of \(\mathbf T\).** Every block \(\varphi^4(a)\), for \(a\in\{0,1,2\}\), has length at least \(7\) (the three lengths are \(13,11,7\)). Since \(\mathbf T=\varphi^4(\mathbf T)\), every six-letter factor lies within one block or crosses exactly one boundary between two consecutive such blocks. Conversely, every pair in \(\mathcal S_2\) occurs in \(\mathbf T\), so each factor of \(\varphi^4(uv)\) with \(uv\in\mathcal S_2\) occurs in \(\mathbf T\). Therefore
\[
\mathcal L_6(\mathbf T)=\bigcup_{uv\in\mathcal S_2}\operatorname{Fac}_6(\varphi^4(uv))
\]
exactly. Applying the five finite substitutions yields the following thirteen words:

`001020, 010010, 010102, 010201, 020100, 020101, 020102, 100102, 101020, 102010, 201001, 201010, 201020`.

**3. Finite reduction for every length at most eleven.** Each image \(\pi(a)\) has length two or three. A factor of length \(n\le11\) in \(\pi(\mathbf T)\) intersects at most six consecutive image blocks: spanning seven blocks would require at least one letter of each endpoint block and five complete intermediate blocks, a total of at least \(1+5\cdot2+1=12\) letters. Any six consecutive source letters extend the intersected blocks, so for each \(1\le n\le11\),
\[
\mathcal L_n(\mathbf B)
=\{\operatorname{pref}_n(\mathbf B)\}\cup
\bigcup_{u\in\mathcal L_6(\mathbf T)}\operatorname{Fac}_n(\pi(u)).
\tag{1}
\]
The extra prefix accounts for the only factor starting with the initial symbol outside \(\pi(\mathbf T)\); all others start within \(\pi(\mathbf T)\). The equality is exact, not a finite-prefix approximation.

**4. Complete finite reversal enumeration.** Calculate the right-hand side of (1), compare each word with its reverse, and count distinct palindrome words and unordered nonpalindromic pairs. The results are

| \(n\) | \(\#\mathcal L_n\) | \(P(n)\) | \(Q(n)\) | \(r(n)\) |
|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 0 | 2 |
| 2 | 4 | 2 | 1 | 3 |
| 3 | 6 | 2 | 2 | 4 |
| 4 | 8 | 2 | 2 | 6 |
| 5 | 10 | 2 | 2 | 8 |
| 6 | 12 | 1 | 3 | 9 |
| 7 | 14 | 2 | 2 | 12 |
| 8 | 16 | 1 | 1 | 15 |
| 9 | 18 | 1 | 0 | 18 |
| 10 | 20 | 0 | 0 | 20 |
| 11 | 22 | 0 | 0 | 22 |

The nonempty palindromic factors are exactly

- length 1: `0`, `1`; length 2: `00`, `11`; length 3: `010`, `101`;
- length 4: `0110`, `1001`; length 5: `00100`, `01010`; length 6: `010010`;
- length 7: `0010100`, `1001001`; length 8: `10100101`; length 9: `100101001`.

For additional transparent evidence, the **complete** length-ten factor language is

`0010010110, 0010100101, 0010110010, 0100101100, 0101001011, 0101100100, 0101100101, 0110010010, 0110010100, 0110010110, 1001001011, 1001010010, 1001011001, 1010010110, 1011001001, 1011001010, 1011001011, 1100100101, 1100101001, 1100101100`.

Direct reversal of each of these twenty strings gives a word outside the displayed set. The certificate script `verify.py` independently reconstructs the finite languages from the morphisms, checks this disjointness and reproduces every table entry.

**5. Infinite cutoff and reflection formula.** If both a length-\(n\) factor \(w\) and its reverse \(w^R\) occurred for some \(n\ge10\), the first ten letters of \(w\) and their reversal (the final ten letters of \(w^R\)) would both be factors of length ten. This contradicts step 4. Thus \(P(n)=Q(n)=0\) for every \(n\ge10\). For any finite factor language, each two-element reversal class saves one class compared with counting individual words; hence \(r(n)=\#\mathcal L_n-Q(n)\). By [1], \(\#\mathcal L_n=2n\); substitution of the finite spectrum completes the theorem.

## Verification

Run `python3 verify.py` in a directory containing the supplied script. It uses only the Python standard library and checks the exact pair-language closure, all five fourth-iterate boundary images, the thirteen six-factors, the right-hand side of (1) for \(1\le n\le11\), every palindrome and reversal-pair count, the twenty-element length-ten language, and the empty intersection with its reversed image. Eleven longer-prefix comparisons are supplemental consistency checks; no infinite theorem is inferred from a sampled prefix. All finite computations are derived from exhaustive small source languages proved in steps 1–3.

## Relationship to prior work

Dvořáková, Pelantová and Shallit [1] give the Tribonacci morphic representation of Kimberling’s word and prove its ordinary factor complexity \(2n\); the palindrome and reversal-equivalence spectrum above is not among their stated results. Allouche and collaborators [2] introduce reflection complexity and compute it for **complementation-symmetric** Rote words, obtaining \(n+1\), a result inapplicable to the present word: `0010` occurs in \(\mathbf B\), but its binary complement `1101` does not. Blažek, Dvořáková and Pelantová [3] treat generalized reflection complexity and other non-complementation-symmetric Rote examples, but the inspected results do not give a spectrum for this particular word. The present calculation shows that ordinary factor growth \(2n\) coexists with eventual maximal reflection growth \(2n\).

## Limitations

The exact formulas concern the fixed Kimberling word specified above, not all non-complementation-symmetric Rote words. They do not settle generalized reflection or letter-exchange complexity. Exact priority outside the checked literature remains provisional, and independent mathematical audit has not been performed.

## References

[1] L. Dvořáková, E. Pelantová, J. Shallit, *On a sequence of Kimberling and its relationship to the Tribonacci word*, arXiv:2510.11318v1 (first public 2025-10-13), https://arxiv.org/html/2510.11318v1 . Theorems 2 and 5 and §§3,5.

[2] J.-P. Allouche, J. M. Campbell, S. Li, J. Shallit, M. Stipulanti, *The reflection complexity of sequences over finite alphabets*, arXiv:2406.09302 (first public 2024-06-13), https://arxiv.org/html/2406.09302v4 . Definition 3, Theorem 51, and §6.

[3] A. Blažek, L. Dvořáková, E. Pelantová, *Generalized reflection complexity*, arXiv:2610.14637 (first public 2026-10-10), https://arxiv.org/abs/2610.14637 . §6.1 and Examples 32–33.
