# Shortest cyclic covers of all length-three palindromes

## Finding
Let \(\Sigma\) be a labeled alphabet of size \(q\ge 2\). Let \(L(q)\) be the shortest length of one cyclic word containing, as cyclic contiguous factors, every word \(aba\) with \(a,b\in\Sigma\), including the constant words \(aaa\). Then
\[
L(q)=3\binom q2+2q+\begin{cases}0,&q\text{ odd},\\q/2,&q\text{ even},\end{cases}
=\begin{cases}(3q^2+q)/2,&q\text{ odd},\\(3q^2+2q)/2,&q\text{ even}.\end{cases}
\]
In particular the sharp lengths for \(q=2,3,4,5,6,7,8\) are \(8,15,28,40,60,77,104\). Every alphabet size has an explicit optimum obtained by expanding an Euler tour of a connected looped complete multigraph. The extra \(q/2\) term for even alphabets comes from the parity of off-diagonal traversal multiplicities and is attained by a perfect matching.

## Assumptions and scope
A cyclic word of length \(n\) is a function \(w:\mathbb{Z}/n\mathbb{Z}\to\Sigma\). For \(n\ge1\), an indexed cyclic length-three factor at \(i\) is \((w(i),w(i+1),w(i+2))\), indices reduced modulo \(n\). A covering cyclic word must include each of the \(q^2\) distinct length-three ordinary palindromes \(aba\). The alphabet letters are distinct labels. Word reversal, alphabet relabeling and rotation are allowed but do not change the minimum length. The claim concerns covering **all** length-three ordinary palindromes by one cyclic word, not reverse-complement palindromes, all length-three factors, or a linear superstring.

## Proof
For any cyclic word \(w\), regard its successive adjacent pairs as the traversals of a closed walk in the undirected looped complete graph on \(\Sigma\). Let \(m_{ab}\) count traversals of the unordered off-diagonal edge \(\{a,b\}\) for \(a\ne b\), and let \(\ell_a\) count traversals of the loop at \(a\).

**Local edge requirements.** The factor \(aba\), for \(a\ne b\), requires two consecutive traversals of edge \(\{a,b\}\), first from \(a\) to \(b\), then back. The distinct factor \(bab\) requires a pair in the opposite order. If the edge had exactly two occurrences, the two occurrences would need to be adjacent in both circular orders to realize both factors. This could happen only in a closed walk of length two. But no covering word has length two: it must contain at least the \(q^2\ge4\) distinct indexed palindromes. Therefore every unordered pair of distinct symbols requires at least three edge traversals, \(m_{ab}\ge3\). Likewise \(aaa\) requires two consecutive traversals of loop \(\{a,a\}\), so \(\ell_a\ge2\). Summing traversals gives
\[
 n\ge3\binom q2+2q.
\]

**Parity obstruction.** For any cyclic closed walk, the number of off-diagonal traversals incident at every vertex \(a\) is even; loops contribute even degree and do not alter this. Thus \(\sum_{b\ne a}m_{ab}\equiv0\pmod 2\). At baseline \(m_{ab}=3\) this sum has parity \(q-1\). If \(q\) is even it is odd at each vertex. Put \(e_{ab}=m_{ab}-3\ge0\); then \(\sum_{b\ne a}e_{ab}\) is odd and hence at least one for each of the \(q\) vertices. Double counting gives \(\sum_{a<b}e_{ab}\ge q/2\). For odd \(q\), the earlier bound is sufficient.

**Constructive sharpness.** Form an undirected multigraph \(H\) with one loop at each letter and one ordinary edge between every distinct pair of letters. If \(q\) is even, add one extra copy of every edge in a fixed perfect matching. The graph is connected and Eulerian: each vertex has degree \(q+1\) when \(q\) is odd, or \(q+2\) when \(q\) is even (counting the loop twice). Fix an Euler circuit. For each off-diagonal pair, select exactly one copy of its edge; when that copy is traversed from \(a\) to \(b\), replace the step \(a\to b\) with \(a\to b\to a\to b\). Leave any second copy (which can only be in the matching) as one step. Replace each loop step \(a\to a\) by the two steps \(a\to a\to a\). These replacements retain starting and ending vertices and hence yield a single cyclic closed walk. The expanded pair contains both \(aba\) and \(bab\) as consecutive cyclic windows; the expanded loop contains \(aaa\). It therefore contains every target palindrome. Its length is exactly \(3\binom q2+2q\) plus \(q/2\) matching edges if \(q\) is even, meeting the lower bound. This proves the formula for every integer \(q\ge2\). \(\square\)

## Verification
The standalone script `palindrome_cover_check.py` constructs Euler tours with the stated expansion and validates both exact length and coverage for all alphabet sizes \(2\le q\le8\). It independently brute-forces every binary cyclic word of lengths \(1\) through \(8\), establishing no shorter binary example and giving \(16\) rooted optimal words. `palindrome_cover_ilp_check.py` gives an independently formulated integer-flow relaxation, with an exact integer optimum agreeing with the theorem at \(q=2,3,4\). Run `python palindrome_cover_check.py` (standard library) and `python palindrome_cover_ilp_check.py` (NumPy/SciPy). The mathematical proof, not these finite computations, establishes the unrestricted statement.

## Relationship to prior work
Anisiu, Anisiu and Kása (2006), Section 2 and Proposition 1, explain how consecutive palindromic factors constrain words and discuss the difficulty of storing all palindromes in consecutive de Bruijn-style windows; their inspected full text does not state the present minimum-length, parity-sensitive cyclic covering theorem. Kapun and Tsarev (2013) study a general multiplicity-based superwalk optimization problem, while Simpson (2014) studies the maximum number of distinct palindromic factors in circular words. These ask different questions and do not imply this exact all-alphabet minimum. Related indexed research treats ternary length-five ordinary palindrome covers, reverse-complement length-four covers, nonpalindromic length-three universal cycles, and length-four tandem-square covers: the target sets and sharp length functions differ. The shared use of Eulerian graph methods does not itself settle the specific parity obstruction and equality construction.

## Limitations
The theorem does not classify or count all minimizing cyclic words and does not give a shortest linear covering word. It does not extend without further work to odd palindromes of length five or more, to general antimorphic palindromes, or to more restrictive symbol-content constraints. The verified-source first public day is associated with a methodological superwalk source; the directly relevant 2006 palindrome paper was verified as published in 2006 but its first **day** of public availability was not established. Earlier equivalent literature outside the inspected sources may exist; the novelty assessment is qualified. The additional computational checks are finite corroboration, not independent mathematical certification.

## References
1. M.-C. Anisiu, V. Anisiu and Z. Kása, "Properties of palindromes in finite words," *Pure Mathematics and Applications* 17 (2006), 183–195. Complete article HTML: https://ictp.acad.ro/properties-of-palindromes-in-finite-words/ .
2. I. Kapun and S. Tsarev, "De Bruijn Superwalk with Multiplicities Problem is NP-hard," *BMC Bioinformatics* 14 (Suppl. 5), S7 (2013); dated 2013-04-10. https://pubmed.ncbi.nlm.nih.gov/23734822/ .
3. J. Simpson, "Palindromes in circular words," *Theoretical Computer Science* 550 (2014), 66–78. https://researchportal.murdoch.edu.au/esploro/outputs/journalArticle/Palindromes-in-circular-words/991005543823107891 .
4. Published related result on ternary five-letter palindrome covers, id `2026/11/2/SCOPE-exact-ternary-length-five-palindromic-covers-66-cyclic-and-68-li--11abece62ea8` (published-finding corpus index; summary inspected).
5. Published related result on length-four reverse-complement palindrome cyclic covers, id `2026/11/2/SCOPE-sharp-cyclic-and-linear-covers-of-reverse-complement-four-palind--1c5013f138d2` (published-finding corpus index; summary inspected).
