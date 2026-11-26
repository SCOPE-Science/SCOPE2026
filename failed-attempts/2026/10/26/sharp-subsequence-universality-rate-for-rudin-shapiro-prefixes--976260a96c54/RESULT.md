# Sharp subsequence-universality rate for Rudin–Shapiro prefixes

## Finding
Let \(r_0r_1r_2\cdots\) be the binary Rudin–Shapiro word, where \(r_n\) is the parity of the number of overlapping occurrences of `11` in the usual base-two representation of \(n\), with \(r_0=0\). For \(N\ge1\), define \(U(N)\) to be the largest \(h\ge0\) such that **every** binary word of length \(h\) occurs as a scattered subsequence of the length-\(N\) prefix \(r_0\cdots r_{N-1}\). Write \(s_2(N)\) for the number of ones in the binary expansion of \(N\).

The exact values at substitution scales are
\[
U(1)=0,\quad U(2)=0,\quad U(4)=1,\quad U(8)=2,
\]
and, for every integer \(k\ge4\),
\[
\boxed{U(2^k)=
\begin{cases}
5\cdot2^{k-4}-1,&k\text{ even},\\
5\cdot2^{k-4},&k\text{ odd}.
\end{cases}}
\]
For **every** \(N\ge1\), not just powers of two, the following explicit digital discrepancy bound holds:
\[
\boxed{\left|U(N)-\frac{5N}{16}\right|\le s_2(N).}
\]
Consequently \(\lim_{N\to\infty}U(N)/N=5/16\), with error \(O(\log N)\). Equivalently, the shortest absent binary subsequence has length exactly \(U(N)+1\). These statements concern ordinary linear prefixes, not circular subsequences or contiguous factors.

## Assumptions and scope
All indices are zero-based, all words are over the fixed ambient alphabet \(\{0,1\}\), and the empty word counts as the unique length-zero subsequence. Scattered subsequences preserve order but need not use adjacent positions. The parity definition counts *overlapping* `11` pairs in standard base-two expansions; leading zeros do not change it. The substitution is the four-letter, length-two morphism
\[
\mu(0)=01,\quad \mu(1)=02,\quad \mu(2)=31,\quad \mu(3)=32,
\]
with binary coding \(c(0)=c(1)=0\), \(c(2)=c(3)=1\). Thus the first \(2^k\) bits of the word are \(c(\mu^k(0))\). The exact formula quantifies over every integer \(k\ge4\); the discrepancy bound quantifies over every positive integer \(N\).

## Proof
**1. Coding and arithmetic definition agree.** Appending a zero to the base-two expansion creates no new `11` pair, and appending a one creates exactly one if the previous last bit was one. Hence \(r_{2n}=r_n\) and \(r_{2n+1}=r_n\oplus(n\bmod 2)\). Associate the four letters with the states \((r_n,n\bmod 2)\) as follows: \(0\leftrightarrow(0,0)\), \(1\leftrightarrow(0,1)\), \(2\leftrightarrow(1,1)\), \(3\leftrightarrow(1,0)\). Their successive two children have precisely the labels in the displayed morphism, so its coded fixed point is the arithmetic word.

**2. Binary arches measure the desired invariant.** A *greedy arch* is the shortest unread prefix containing both bits; repeatedly remove such prefixes, leaving a final unary (or empty) tail. Each arch has the unique form \(b^q(1-b)\) with \(q\ge1\). If there are \(a\) arches, any prescribed binary word of length \(a\) appears as a subsequence by selecting one letter from each arch. Conversely, choose the unique final letter \(1-b\) from each arch in order. The greedy earliest embedding of this sequence ends precisely at the end of the \(a\)-th arch. Appending to it a bit absent from the remaining unary tail produces a length-\(a+1\) word that is **not** a subsequence. Thus the number of greedy arches equals \(U(N)\), including when \(a=0\).

**3. Weighted scanner.** Use residual states \(E\) (no letter seen since the preceding arch), \(Z\) (only zero seen), and \(O\) (only one seen). Reading the missing opposite bit from \(Z\) or \(O\) closes an arch and returns to \(E\); otherwise the machine retains or creates the corresponding residual state. For each \(k\ge0\) and letter \(a\in\{0,1,2,3\}\), let \(T_{k,a}\) be the transformation, with number of completed arches and final residual state, induced by scanning \(c(\mu^k(a))\). Count triples below list the outputs for initial states \((E,Z,O)\), in that order; the final residual state in each row is the same for all three inputs. Direct scanning of the sixteen-letter words at \(k=4\) gives the even table below.

For even \(k\ge4\), put \(B=5\cdot2^{k-4}-1\). The four rows \((a;\text{count triple};\text{final state})\) are
\[
\begin{array}{c|c|c}
0&(B,B,B+1)&O\\
1&(B+1,B+1,B+2)&Z\\
2&(B+1,B+2,B+1)&O\\
3&(B,B+1,B)&Z
\end{array}.
\]
For odd \(k\ge5\), put \(B=5\cdot2^{k-4}\). The rows are
\[
\begin{array}{c|c|c}
0&(B,B,B+1)&Z\\
1&(B-1,B-1,B)&O\\
2&(B-1,B,B-1)&Z\\
3&(B,B+1,B)&O
\end{array}.
\]
These are identities for the *whole weighted state transformations*, not numerical guesses. To check the induction, scanning concatenated blocks means adding the first output count to the second block's count evaluated at the first block's final state. The morphism gives the four identities
\[
T_{k+1,0}=T_{k,0}\star T_{k,1},\quad
T_{k+1,1}=T_{k,0}\star T_{k,2},\quad
T_{k+1,2}=T_{k,3}\star T_{k,1},\quad
T_{k+1,3}=T_{k,3}\star T_{k,2},
\]
where \(\star\) explicitly denotes left-to-right scanning and *not* ordinary function-composition order. Substituting the even table gives the odd table with new base \(2(B+1)\); substituting the odd table gives the even table with new base \(2B-1\). These transformations prove both tables inductively from \(k=4\).

**4. Exact dyadic formula.** The scanner starts in state \(E\). Its output on \(c(\mu^k(0))\) is the first entry of row zero, namely \(B\) in either table. This gives the claimed formulas for \(k\ge4\). Direct scans give the stated four smaller values.

**5. Every-prefix bound.** For every letter \(a\), every initial residual state, and every \(j\ge4\), the tables show that the arch count contributed by a full block \(c(\mu^j(a))\) differs from \(5\cdot2^j/16\) by at most one. The same inequality follows by inspecting the four transformations for \(j=0,1,2,3\). Write \(N\) in binary and partition its length-\(N\) prefix, from left to right, into the natural aligned substitution blocks of lengths given by its distinct powers of two. There are exactly \(s_2(N)\) such blocks. Every aligned length-\(2^j\) block is \(c(\mu^j(a))\) for some letter \(a\), and the scanner's incoming residual state can be arbitrary. Additivity of completed-arch counts across blocks therefore gives
\[
\left|U(N)-\sum_{j\text{ used}}\frac{5\cdot2^j}{16}\right|\le s_2(N).
\]
The sum of block lengths is \(N\), proving the bound. As \(s_2(N)\le1+\lfloor\log_2N\rfloor\), division by \(N\) gives the limiting rate.

## Verification
Run `python3 verify.py` with a standard Python 3 interpreter; no third-party packages or external data are required. The script constructs the weighted transformations independently from individual binary symbols and checks both parity tables through \(k=47\). It independently expands the four-letter substitution and evaluates the arithmetic count of binary `11` pairs through a prefix of length \(2^{15}\), agreeing on every bit. It checks the dyadic formulas, verifies greedy arch count against the actual definition by all-subsequence enumeration for every binary word through length \(12\), and checks the digital discrepancy bound for every prefix length below \(2^{17}\). These finite tests confirm the calculations and conventions; the all-length theorem follows from the induction and block decomposition above.

## Relationship to prior work
The Rudin–Shapiro word and its four-letter substitution are standard; the 2015 Schaeffer–Shallit paper explicitly gives the same morphism and studies different factor predicates. The greedy arch factorization and its equality with the subsequence-universality index are established tools; Adamson (2023) treats enumeration, ranking and unranking across all finite words, while Schnoebelen–Veron (2023) develop compositional algorithms for compressed words and circular universality. Their general algorithms can *compute* the index at fixed input lengths but do not state this Rudin–Shapiro all-dyadic closed form, its \(5/16\) rate, or the all-prefix binary-weight discrepancy bound.

The published *Closed-form law for binary subsequence universality* obtains a distribution across **all** binary words of each length, not an exact property of this deterministic Rudin–Shapiro sequence. The published Rudin–Shapiro *string-attractor* census concerns covering contiguous factors, a different invariant. Neither inspected statement implies the present formulas by specialization. No claim is made that the general arch-factorization technique is new.

## Limitations
The quantitative result is for the standard binary Rudin–Shapiro coding and its origin-anchored prefixes; it does not give the universality index of every shifted factor or arbitrary automatic words. The binary-weight error bound need not be optimal for individual prefix lengths. The literature comparison is limited to accessible, inspected sources and semantic research-record search; priority could be affected by unindexed results. The mathematical proof is self-reviewed only and has not received independent audit.

## References
1. L. Schaeffer and J. Shallit, *Closed, Palindromic, Rich, Privileged, Trapezoidal, and Balanced Words in Automatic Sequences*, arXiv:1508.02074v1 (public 2015-08-09), https://arxiv.org/abs/1508.02074.
2. D. Adamson, *Ranking and Unranking k-subsequence universal words*, arXiv:2304.04583v1 (public 2023-04-10), https://arxiv.org/abs/2304.04583.
3. P. Schnoebelen and J. Veron, *On arch factorization and subword universality for words and compressed words*, arXiv:2304.11932v1 (public 2023-04-24), https://arxiv.org/html/2304.11932v1.
4. *Closed-form law for binary subsequence universality*, published research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-closed-form-law-for-binary-subsequence-universality--e77c4e8d9f37.
5. *Exact minimal string attractors for Rudin–Shapiro and regular-paperfolding dyadic prefixes*, published research record (2026), https://github.com/Resultary/2026/tree/main/2026/9/8/SCOPE079.
