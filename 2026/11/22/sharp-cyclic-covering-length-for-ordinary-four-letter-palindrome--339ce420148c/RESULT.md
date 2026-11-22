# Sharp cyclic covering length for ordinary four-letter palindromes

## Finding

Let \(\Sigma\) be any alphabet with \(q\ge2\) labeled letters. Let \(P_q=\{abba:a,b\in\Sigma\}\), the set of all \(q^2\) ordinary reversal palindromes of length four. Write \(M(q)\) for the smallest length of a cyclic word containing every member of \(P_q\) as a contiguous cyclic four-letter factor (including factors crossing the cyclic boundary). No restriction is imposed on other factors or repeated occurrences. Then

\[
M(q)=\begin{cases}
(5q^2+q)/2,&q\text{ odd},\\
(5q^2+2q)/2,&q\text{ even}.
\end{cases}
\]

Thus \(M(2)=12\), \(M(3)=24\), \(M(4)=44\), \(M(5)=65\), \(M(6)=96\). The even-alphabet correction arises from the obstruction to an Euler tour in the odd-degree complete graph.

## Assumptions and scope

Letters are distinct formal alphabet symbols. The length is the number of positions on the circle, not the length of a chosen linear display with added closing symbols. A cyclic factor of length four uses successive positions modulo the circumference. Covers may contain any additional factors. The theorem concerns exactly the target set \(P_q\), not all four-letter words, tandem squares \(abab\), or Watson–Crick reverse-complement palindromes. The domain is every integer \(q\ge2\), with no fixed alphabet ordering assumption.

## Proof

**1. Overlap restrictions.** Set \(p_{ab}=abba\). A proper three-letter overlap between distinct \(p_{ab}\) and \(p_{cd}\) would require \(bba=cdd\), which forces all four letters equal and hence the two targets identical. A proper two-letter overlap requires \(ba=cd\), equivalently \((c,d)=(b,a)\). For distinct targets, \(a\ne b\). A one-letter overlap is possible precisely when their first letters agree, since the last letter of \(p_{ab}\) is \(a\).

**2. Universal lower bound.** In an arbitrary cyclic cover choose one occurrence of each of the \(q^2\) distinct targets. Order their starts cyclically and let \(d_i\) be successive positive position gaps; their sum is the circumference \(L\). By step 1 every gap is at least two. Let \(r\) count gaps equal to two and \(z\) count gaps at least four. The other gaps are at least three, hence

\[
L\ge 3q^2-r+z.
\]

Every gap of two corresponds to a directed transition \(p_{ab}\to p_{ba}\) with \(a\ne b\). The reverse transition cannot also appear among the selected circular target ordering: together they would form a separate two-cycle, impossible since \(q^2>2\) distinct target occurrences must lie in one cyclic order. Thus \(r\le\binom q2\), proving \(L\ge 3q^2-\binom q2=(5q^2+q)/2\).

**3. Even-alphabet parity obstruction.** Suppose \(q\) is even. Represent each gap-two transition by an orientation of its unordered pair \(\{a,b\}\) in \(K_q\). Since each unordered pair is used at most once, exactly \(m=\binom q2-r\) edges of \(K_q\) are absent from this directed edge set. A gap-three transition preserves the first letter of the target and is thus a loop at a vertex; each of the \(z\) gaps of length at least four supplies one additional directed transition between the first letters of its two targets. The entire cyclic target ordering is a balanced directed multigraph when its transitions are projected onto first letters. The gap-three loops do not affect balance. Every vertex has odd degree \(q-1\) in \(K_q\). Consequently each of the \(q\) vertices must be incident to an omitted undirected edge or an additional long-gap transition, because otherwise an odd-degree subgraph with no supplementary edge would need equal indegree and outdegree. Counting incidences, including both ends of a loop, gives \(2m+2z\ge q\). Therefore \(m+z\ge q/2\), and

\[
L\ge3q^2-\binom q2 +m+z\ge(5q^2+2q)/2.
\]

**4. Odd-alphabet construction.** For odd \(q\ge3\), take an Euler tour of the undirected complete graph \(K_q\), whose degrees \(q-1\) are even. For each consecutive tour edge \(a\to b\) place the two distinct targets \(p_{ab},p_{ba}\), consecutively. They overlap in two letters, so their starting-position gap is two. Between consecutive edge-pairs at vertex \(b\), the last target of the earlier pair ends in \(b\), while the first target of the next pair begins in \(b\), so the gap is three. At the first encounter of each vertex \(a\), insert the diagonal target \(p_{aa}\) between adjacent pairs, with one-letter overlaps on both sides. This orders every one of the \(q^2\) targets exactly once on a single cycle, with \(r=\binom q2\) two-symbol-overlap transitions and all remaining gaps three. Its length equals the odd lower bound.

**5. Even-alphabet construction.** For even \(q\ge4\), remove any perfect matching from \(K_q\). The remaining graph is connected and has even degree \(q-2\), so it admits an Euler tour. Repeat step 4 along the retained edges. At the first encounter of a vertex \(a\), insert both \(p_{aa}\) and \(p_{a\mu(a)}\), where \(\mu(a)\) is the unique matched partner of \(a\). The two insertions and their neighbors share one-letter overlaps. Every target occurs once: each retained unordered pair contributes its two orientations, each removed matched pair contributes one orientation at each endpoint, and all diagonal targets appear. There are exactly \(r=\binom q2-q/2\) gap-two transitions; every other transition has gap three. This reaches the even lower bound. For \(q=2\), the explicit cyclic word `011001111000` has length twelve and covers `0000`, `0110`, `1001`, and `1111`; the even lower bound is twelve. This completes the proof for every \(q\ge2\).

## Verification

Run `python palindrome_cover_verify.py` with Python 3 and no third-party packages. The script constructs the Euler-tour hosts for all \(2\le q\le10\), checks their circumferences and complete target coverage, and independently solves the weighted Hamiltonian tour problem exactly via subset dynamic programming for \(q=2,3,4\). Output: `VERIFY_OK constructions q=2..10; exact independent tours q=2..4`. The mathematical lower bounds and all-alphabet constructions in the proof, not the finite computation, establish the infinite theorem.

## Relationship to prior work

Orenstein and Shamir (2013) investigate optimal covers of all length-\(k\) words **up to reverse complementation**, a different and generally larger target family; their full open-access article gives this context and relevant overlap-graph techniques, but not the specified ordinary length-four palindrome-only theorem. OEIS A330022 gives the previously known **linear binary** minimum of twelve for all ordinary length-four palindromes; the binary case of the present result is not claimed as new. Published related covers of length-four tandem squares \(abab\), fixed-point-free reverse-complement palindromes, and ternary length-five ordinary palindromes involve different targets and do not provide the present arbitrary-alphabet parity formula by direct implication. No exhaustive priority claim is made.

## Limitations

The result covers ordinary four-letter palindromes and cyclic hosts only, not a complete length-by-alphabet table, a universal theorem for longer palindromes, prescribed extra factor avoidance, uniqueness or enumeration of optimal hosts, or DNA reverse-complement motif families. The exact verification is finite through ten symbols, with exact exhaustive Hamiltonian optimization through four symbols; the universal proof is separate. An unindexed equivalent result may exist. Independent review has not been performed.

## References

1. Y. Orenstein and R. Shamir, *Design of shortest double-stranded DNA sequences covering all k-mers with applications to protein-binding microarrays and synthetic enhancers*, Bioinformatics 29 (2013), i71–i79. First public article date June 19, 2013. https://pmc.ncbi.nlm.nih.gov/articles/PMC3694677/
2. J. Shallit, OEIS A330022, *Length of shortest binary string containing all palindromes of length n as substrings*, first submitted November 27, 2019. https://oeis.org/A330022
3. *Exact shortest cyclic covers of all four-letter tandem squares*, published mathematical research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-shortest-cyclic-covers-of-all-four-letter-tandem-squares--35e46779014c
4. *Sharp cyclic and linear covers of reverse-complement four-palindromes*, published mathematical research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-cyclic-and-linear-covers-of-reverse-complement-four-palind--1c5013f138d2
5. *Exact ternary length-five palindromic covers: 66 cyclic and 68 linear*, published mathematical research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-ternary-length-five-palindromic-covers-66-cyclic-and-68-li--11abece62ea8
