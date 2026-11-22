# The first two-point Fano obstruction over a five-point bow-tie base

## Finding
Let \(\mathcal H\) be the countable homogeneous \(3\)-uniform hypergraph whose finite age consists of all hypergraphs omitting the Fano plane as a not-necessarily-induced subhypergraph. Name a finite parameter set \(A\) and count complete **injective ordered** types of pairs \((x,y)\) of points outside \(A\), with \(x\ne y\).

For every parameter base on \(n\le4\) vertices, the pair-type count is \(2^{2\binom n2+n}\). On five named vertices, every base with at most one hyperedge, or with two distinct hyperedges meeting in two vertices, has exactly \(2^{25}=33{,}554{,}432\) pair types. The unique minimal obstruction under adding old hyperedges is the bow tie: two old triples meeting in precisely one vertex.

For the bow-tie base \(A=\{a,b,c,d,e\}\) with exactly the old triples \(\{a,b,c\}\) and \(\{a,d,e\}\), there are exactly
\[
T(A)=2^{25}-2\cdot2^{20}+2^{16}=31{,}522{,}816
      =\frac{481}{512}\,2^{25}
\]
complete ordered two-point types. For a fixed mutual-link set \(S=\{u\in A:\{x,y,u\}\text{ is a hyperedge}\}\), the exact number of types is
\[
N_A(S)=2^{12}\begin{cases}256,&a\notin S,\\225,&a\in S.\end{cases}
\]
The mutual-link bits are therefore independent under a uniform pair type: the four bits indexed by \(b,c,d,e\) are fair, and the bit indexed by \(a\) has probability \(225/481\). In particular, if \(K=|S|\), then
\[
\#\{\operatorname{tp}(x,y/A):K=k\}
 =2^{12}\left(256\binom4k+225\binom4{k-1}\right),\quad 0\le k\le5,
\]
with out-of-range binomial coefficients interpreted as zero. The total-variation distance between this size law and the unobstructed \(\operatorname{Binomial}(5,1/2)\) law is \(93/7696\).

Thus five is the least possible parameter size at which Fano avoidance restricts two-point types at all, even though every one-point type over every five-point base is unrestricted.

## Assumptions and scope
The relation is symmetric, irreflexive and ternary. A hypergraph omits the Fano plane if it has no injective map of the Fano plane sending all seven Fano lines to hyperedges; extra hyperedges are permitted. Parameters are individually named. Types of the ordered pair distinguish \(x\) and \(y\), require distinct points and specify all ternary atomic relations with the parameters and one another. No other language symbols occur.

The Fano plane covers every pair of its seven vertices by exactly one of its seven triples, so is \(2\)-irreducible. Consequently its omission class has free amalgamation and a countable ultrahomogeneous Fraïssé limit. Every finite Fano-free diagram on \(A\cup\{x,y\}\) occurs and determines one complete pair type by ultrahomogeneity; all such extension types are nonalgebraic. Over five old points each of \(x\) and \(y\) has \(\binom52=10\) independent old-pair incidences and there are five incidences of the form \(\{x,y,u\}\), giving \(25\) binary choices before forbidden patterns are removed.

## Proof
**First possible parameter size.** A Fano embedding needs seven distinct vertices. If \(|A|\le4\), then \(A\cup\{x,y\}\) has at most six, so none of the \(2^{2\binom{|A|}2+|A|}\) diagrams is forbidden. Every single-point extension of a five-point base has six points, hence all \(2^{10}\) one-point types exist.

**Shape of the old Fano restriction.** In a Fano plane, remove any two points \(x,y\). Exactly two of the seven lines avoid both: each point lies on three lines, and one line contains both, so five lines meet \(\{x,y\}\) and two do not. These two old lines meet at exactly one point (every pair of distinct Fano lines meets once). Thus a Fano copy on \(A\cup\{x,y\}\), for \(|A|=5\), forces two old triples meeting in one vertex. A base with zero or one old edge, or exactly two edges meeting in two vertices, therefore admits every \(25\)-bit pair diagram.

**The two completions.** Assume the two old lines are \(abc\) and \(ade\). A Fano completion must have the third line through \(a\) equal to \(axy\). The four remaining lines must connect one vertex from \(\{b,c\}\), one from \(\{d,e\}\), and one of \(x,y\). Each of those four old vertices must occur once with \(x\) and once with \(y\), because every pair belongs to exactly one line. Equivalently, the \(2\)-by-\(2\) incidence square must be colored alternately by \(x,y\). There are exactly two checkerboard completions:
\[
\begin{array}{ll}
F_1:\;axy,\ bdx,\ bey,\ cdy,\ cex;&
F_2:\;axy,\ bdy,\ bex,\ cdx,\ cey.
\end{array}
\]
Both also contain the fixed old lines \(abc,ade\). These are genuine Fano planes (each unordered pair of the seven vertices appears in exactly one of the seven listed triples). Their five required *new* triples intersect only in \(axy\), so the two forbidden events require five distinct new bits each and have a nine-bit union.

**Count and conditional law.** There are \(25\) free new triples. Forbidding the two five-bit events by inclusion-exclusion leaves \(2^{25}-2\cdot2^{20}+2^{16}\) types. If a mutual-link set \(S\subseteq A\) is prescribed, only \(20\) bits remain free. If \(a\notin S\), neither Fano pattern is possible, leaving \(2^{20}\) types. If \(a\in S\), the two checkerboards require four distinct remaining bits each and overlap on eight distinct bits, leaving \(2^{20}-2\cdot2^{16}+2^{12}=225\cdot2^{12}\). This establishes \(N_A(S)\).

Of the \(32\) possible sets \(S\), exactly \(16\) contain \(a\). Each assignment of the four other bits has the same weight independently of their values. Hence the mutual-link distribution factors as four fair Bernoulli bits and an independent Bernoulli bit of parameter \(225/(225+256)=225/481\). Summing over fixed cardinalities gives the coefficient formula. Writing \(q=225/481\), the difference from \(\operatorname{Binomial}(5,1/2)\) is \((q-1/2)(p_{k-1}-p_k)\), where \(p_j=\binom4j/16\) is the four-bit binomial mass. The total variation is \(|q-1/2|\max_j p_j=(31/962)(6/16)=93/7696\). This completes the proof.

## Verification
Run `python3 VERIFY.py` using only the Python standard library. It enumerates the \(30\) labeled Fano designs independently by exact-cover recursion on \(21\) pairs; checks that each of the \(15\) bow ties on five old points has precisely two distinct Fano completions, while each two-edge base with overlap two has none; verifies their new-edge intersection; independently enumerates all \(2^{20}=1{,}048{,}576\) one-point-link assignments when the central mutual-link bit is on; and checks every coefficient, total, ratio and total-variation identity. The recorded successful output is in `CHECKS.txt`. These are finite exhaustive checks of the only seven-point obstruction. The all-parameter cutoff is proved directly by the seven-vertex size of a Fano plane, not inferred from computation.

## Relationship to prior work
Conant (2015) gives a general framework for Fraïssé limits forbidding \(2\)-irreducible hypergraphs; the Fano plane fits that framework because every pair lies on a line. The unique Fano seven-point design and its order-\(168\) automorphism group are classical facts, discussed in Heinlein and Östergård (2022). Füredi and Simonovits (2005) study the quite different extremal edge-density question for Fano-free triple systems. A recorded exact count of all seven-vertex labeled hypergraphs containing a Fano plane studies an *unconditioned* \(35\)-bit event. It supplies the \(30\) design masks but does not state the present conditioned two-point type distribution with a fixed five-point bow tie. Previously described pair-type corrections for forbidden complete tetrahedra concern a different forbidden configuration with different minimal obstructions.

## Limitations
The detailed count and Bernoulli factorization apply to five-point bases with precisely the two specified old lines. The classification of unobstructed five-point bases is stated only for bases with at most two old edges; no formula is asserted for all denser five-point bases or more than two new points. The formula counts complete ordered logical types, not labeled realizations in a finite host. Priority relative to unindexed multivariate Fano reliability counts remains unsettled. Independent validation has not been performed.

## References
- Gabriel Conant, *An axiomatic approach to free amalgamation*, arXiv:1505.00762 (first public version May 4, 2015), especially definitions 7.18–7.20, https://arxiv.org/abs/1505.00762 .
- Zoltán Füredi and Miklós Simonovits, *Triple Systems Not Containing a Fano Configuration*, *Combinatorics, Probability and Computing* 14 (2005), 467–484, https://doi.org/10.1017/S0963548305006784 .
- Daniel Heinlein and Patric R. J. Östergård, *Algorithms and complexity for counting configurations in Steiner triple systems*, *Journal of Combinatorial Designs* 30 (2022), 527–546, https://doi.org/10.1002/jcd.21839 .
- *Exact probability that a random 7-vertex triple system contains a Fano plane*, TheoremDB statement P2586, July 24, 2026, https://www.theoremdb.org/statements/fano-plane-containment-probability/ .
