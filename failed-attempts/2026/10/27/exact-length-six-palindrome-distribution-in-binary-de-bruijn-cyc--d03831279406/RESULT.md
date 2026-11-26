# Exact length-six palindrome distribution in binary de Bruijn cycles of order five

## Finding

Consider every binary cyclic de Bruijn word of order \(5\), modulo cyclic rotation (but not reversal or bit complementation). Each cycle has length \(32\) and contains every five-bit word exactly once as a circular factor. Let \(P(B)\) be the number of *distinct* palindromic length-six circular factors of a cycle \(B\). The complete distribution among the \(2048\) cycles is

\[
\#\{B:P(B)=0\}=768,\qquad
\#\{B:P(B)=2\}=1024,\qquad
\#\{B:P(B)=4\}=256.
\]

No other value occurs. In fact the only possible palindromic six-factors occur in the two inseparable pairs
\[
\{\mathtt{001100},\mathtt{101101}\},\qquad
\{\mathtt{010010},\mathtt{110011}\}.
\]
Exactly \(768\) cycles contain neither pair, \(512\) contain only the first, \(512\) contain only the second, and \(256\) contain both. In particular, a uniform random order-five cycle has expected \(P(B)=3/2\), variance \(7/4\), and pair-presence indicator covariance \(-1/64\).

## Assumptions and scope

A cyclic factor is allowed to wrap across the end of a representative of the cycle. Cycles are identified only by cyclic rotation: reversal and complementation are **not** factored out. The statistic counts distinct palindrome words, not their number of occurrences. The statement concerns the fixed order \(5\), not all orders; it is a complete finite classification of a natural joint palindrome-presence profile.

Let \(G\) be the binary de Bruijn digraph with vertex set \(\{0,1\}^{4}\), with two directed edges \(v\longrightarrow\operatorname{suf}_3(v)b\) labeled \(vb\), for \(b\in\{0,1\}\). Directed parallel edges, if any, are always treated as distinct edges. A cycle of order \(5\) is equivalently an Euler circuit of \(G\), with a canonical rotation fixed by making the unique edge \(\mathtt{00000}\) the first edge.

## Proof

**1. Palindromic factors come in forced pairs.** Any palindromic six-factor is \(ava\), where \(v\) is a four-bit palindrome and \(a\) a bit. Thus \(v\) must lie in \(\{\mathtt{0000},\mathtt{0110},\mathtt{1001},\mathtt{1111}\}\). Every four-bit vertex occurs twice along any Euler tour, once entered through each of its two incoming edges and once left through each outgoing edge. The tour therefore determines a bijection from incoming labels \(0v,1v\) to outgoing labels \(v0,v1\). Either it pairs \(av\) with \(va\) for *both* values of \(a\), or for neither. For \(v=\mathtt{0000}\) or \(v=\mathtt{1111}\), the matching \(av\mapsto va\) would send the vertex's loop edge immediately back to itself, requiring the unique five-gram \(\mathtt{00000}\) or \(\mathtt{11111}\) to be traversed twice consecutively. This is impossible. For the other two vertices, the direct matching gives the exact pairs in the finding. Therefore \(P(B)=2(X+Y)\), where \(X\) and \(Y\) indicate the respective direct pairings at vertices \(v_1=\mathtt{0110}\) and \(v_2=\mathtt{1001}\).

**2. Counting forced local pairings.** Given a set \(S\subseteq\{v_1,v_2\}\), construct the directed graph \(G_S\) by suppressing each vertex \(v\in S\) and replacing its two forced two-edge paths \(0v\to v0\) and \(1v\to v1\) by two directed shortcut edges. This produces a balanced directed multigraph: every remaining vertex still has indegree and outdegree \(2\), and \(\mathtt{0000}\) is still present with the original loop edge \(\mathtt{00000}\). There is a bijection between Euler tours of \(G\) that realize every required direct pairing and Euler tours of \(G_S\), respecting the fixed initial loop edge. The two suppressed vertices are not adjacent, so the order of suppression is immaterial.

For a finite balanced directed graph with outdegree \(2\) everywhere and with a distinguished root loop traversed first, the number of rooted Euler circuits is the number of directed spanning in-arborescences toward the root. This is the degree-two case of the directed BEST correspondence: the last exit at each nonroot vertex is its tree edge; the order of the two outgoing edges is then forced, and the root edge order is fixed by the initial loop. By the directed Matrix--Tree theorem, the number is the root-deleted cofactor of the outdegree Laplacian \(L\), where \(L_{ii}=2-\#\{i\to i\}\) and \(L_{ij}=-\#\{i\to j\}\) for \(i\ne j\). Here root is \(\mathtt{0000}\).

For complete reproducibility, form the original edge multiset as
\[
E=\{(v,(2v+b)\bmod16): v=0,\ldots,15,\ b=0,1\},
\]
and for a suppressed vertex \(v\in\{6,9\}\) delete its incident edges and add the two edges
\[
(\lfloor v/2\rfloor,2v\bmod16),\qquad
(8+\lfloor v/2\rfloor,(2v+1)\bmod16).
\]
The integer cofactors, evaluated directly by the bundled fraction-free determinant code, are
\[
\det L_{\varnothing}^{(0)}=2048,\quad
\det L_{\{6\}}^{(0)}=768,\quad
\det L_{\{9\}}^{(0)}=768,\quad
\det L_{\{6,9\}}^{(0)}=256.
\]
The notation \(L_S^{(0)}\) means delete row and column of root vertex zero, *after* forming \(G_S\). All determinants concern matrices of order at most \(15\), built by the explicit edge rule above. The two middle values count cycles satisfying \(X=1\) or \(Y=1\), and the last counts their intersection.

**3. Inclusion--exclusion.** There are \(256\) cycles with \((X,Y)=(1,1)\), \(768-256=512\) with \((1,0)\), another \(512\) with \((0,1)\), and \(2048-768-768+256=768\) with \((0,0)\). The claimed distribution of \(P(B)=2(X+Y)\) follows. For a uniform cycle, \(\mathbf E[X]=\mathbf E[Y]=3/8\) and \(\mathbf E[XY]=1/8\), yielding \(\operatorname{Cov}(X,Y)=-1/64\). The mean and variance of \(P\) follow from this same four-cell table.

## Verification

The accompanying standard-library-only `verification.py` independently checks the four integer Matrix--Tree cofactors and enumerates *all* Euler tours whose first edge is \(\mathtt{00000}\). The independent search explores \(92636\) recursive nodes, returns exactly \(2048\) complete cycles, checks their length-five factor sets, and obtains the joint histogram \((768,512,512,256)\). This is a **complete finite enumeration**, not experimental extrapolation to larger orders. The determinant argument separately proves the counts without relying on that enumeration.

## Relationship to prior work

De Bruijn cycles are classical universal cycles for all fixed-length words. Anisiu--Anisiu--Kása study the palindrome-complexity function of finite words and describe a method *using* de Bruijn words to generate all palindromes; that is not the distribution of palindromic length-six factors **contained in each** de Bruijn cycle. Burris--Motta--Shipman study *unoriented* de Bruijn sequences, which select a representative of each reversal class, rather than counting paired palindromes in ordinary binary order-five cycles. The present statistic is an exact distribution and a negative pair correlation, not a new construction of de Bruijn sequences.

## Limitations

Nothing here determines the corresponding distribution at higher orders or counts palindrome occurrences at arbitrary lengths. Uniformity is over the \(2048\) rotation classes, not over arbitrary algorithms for randomly generating Euler tours. This is a finite, exact result and its mathematical value lies in the exact joint-presence profile for the two possible nonconstant palindrome centers, not in a claim of an asymptotic law. Related literature beyond the inspected sources may still contain equivalent enumerations; the search does not prove universal novelty. No independent audit has been performed.

## References

1. M.-C. Anisiu, V. Anisiu, and Z. Kása, *Properties of palindromes in finite words*, *Pure Mathematics and Applications* 17 (2006), 183–195; publicly dated arXiv record arXiv:1002.2723 (2010-02-13), particularly sections 2 and 4.
2. C. S. Burris, F. C. Motta, and P. D. Shipman, *An Unoriented Variation on de Bruijn Sequences*, arXiv:1608.08480 (2016-08-30).
3. N. G. de Bruijn, *A combinatorial problem*, *Proceedings of the Koninklijke Nederlandse Akademie van Wetenschappen* 49 (1946), 758–764.
4. D. Zerbino and E. Birney, *Velvet: Algorithms for de novo short read assembly using de Bruijn graphs*, *Genome Research* 18 (2008), 821–829, DOI 10.1101/gr.074492.107 (de Bruijn graph motivation and applications).
