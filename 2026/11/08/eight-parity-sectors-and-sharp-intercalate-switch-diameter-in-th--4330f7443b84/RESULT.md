# Eight parity sectors and sharp intercalate-switch diameter in the order-five Latin-square graph

## Finding

**Theorem.** Let \(\mathcal L_5\) be the set of all Latin squares of order \(5\) with fixed, individually named row, column, and symbol labels \(\{0,1,2,3,4\}\). Join distinct squares when one is obtained from the other by one intercalate exchange, changing exactly the four positions occupied by an alternating two-symbol \(2\times2\) subsquare. The resulting undirected graph decomposes as

\[
17{,}280K_1\;\sqcup\; H_1\sqcup\cdots\sqcup H_8,
\]

where the eight graphs \(H_i\) are mutually isomorphic, connected, four-regular graphs, each with \(18{,}000\) vertices and \(36{,}000\) edges. Consequently the complete graph has \(161{,}280\) vertices and \(288{,}000\) edges. Every \(H_i\) has radius and diameter exactly \(13\). From **every** vertex, the numbers of vertices at distances \(0,1,\ldots,13\) are

\[
(1,4,12,36,108,252,612,1284,2256,3624,4812,3828,1112,59).
\]

Thus precisely \(59\) squares lie at distance \(13\) from each mobile square; there are \(4{,}248{,}000\) unordered diametral pairs across the eight mobile components.

**Structural criterion.** Fix the non-group seed

```text
01234
10342
23401
34120
42013
```

and consider triples of row, column, and symbol relabelling permutations \((\rho,\kappa,\sigma)\) acting by \(L[\rho(r),\kappa(c)]=\sigma(S[r,c])\). Every mobile square is an image of this seed. The triple

\[
\bigl(\operatorname{sgn}(\rho),\operatorname{sgn}(\kappa),\operatorname{sgn}(\sigma)\bigr)\in\{+1,-1\}^3
\]

is independent of the chosen representation. Two mobile squares are joined by an intercalate-switch path **if and only if** these three signs agree. The isolated squares are precisely the other, cyclic-group-isotopic class.

## Assumptions and scope

A Latin square is a function \(L:\{0,1,2,3,4\}^2\to\{0,1,2,3,4\}\) in which each symbol occurs once in each row and column. An intercalate has row indices \(r<t\), column indices \(c<d\), and distinct symbols \(a,b\) satisfying

\[
L(r,c)=L(t,d)=a,\qquad L(r,d)=L(t,c)=b.
\]

Its switch exchanges the two symbols in those four positions and leaves every other cell fixed. Row, column, and symbol relabellings are graph automorphisms, but **configurations are not quotiented** by these relabellings. All shortest-path distances below use this single-intercalate move only, with no improper intermediate arrays or larger Latin trades.

## Proof

The theorem admits a finite exhaustive proof with two independent, runnable implementations; the following details specify what is enumerated, why it is exhaustive, and which deductions use symmetry.

**(1) Complete state space.** Enumerate all \(5!=120\) permutations as possible rows. Backtrack through five row choices, admitting the next row only when its five symbols do not duplicate any preceding symbols in their respective columns. Each complete assignment is automatically Latin; conversely every Latin square has a unique sequence of five row permutations and is reached by this search. The implementation checks that the generated list contains exactly \(161{,}280\) distinct squares. Independently, enumerate the \(56\) reduced Latin squares (first row and column in canonical order), then apply permutations of the four noninitial rows and all \(120\) symbol permutations, deduplicating to the same \(161{,}280\) labelled squares.

**(2) Exact moves and components.** For every square, inspect all \(\binom52^2=100\) choices of two rows and two columns. Perform a flip precisely when opposite cells have the same symbols. The resulting square is checked against the exhaustive state dictionary. Symmetry and uniqueness of each move are explicitly checked. Degrees are \(0\) for exactly \(17{,}280\) squares and \(4\) for exactly \(144{,}000\); hence the edge count is \(144{,}000\cdot4/2=288{,}000\). A complete graph traversal produces exactly \(17{,}280\) singleton components and eight components of size \(18{,}000\). The independent verifier uses a different move criterion: its two chosen rows induce a permutation on their symbols, and it detects swaps through the two-cycles of this permutation.

**(3) Well-defined parity and complete connectivity criterion.** Enumerate all \(120^3=1{,}728{,}000\) row/column/symbol isotopies of the displayed seed. For every labelled image, the certificate records the sign triple of its isotopy; if a different isotopy produces the same image, their triples must agree. The exhaustive test finds no conflict, establishing that the signature is intrinsic. It also finds exactly \(18{,}000\) distinct images of each of the eight triples, for \(144{,}000\) images total; every remaining square is isolated by step (2). Every adjacency has identical endpoint signs, as checked over the complete edge set, while every sign class occupies exactly one of the eight connected components found in step (2). Thus sign agreement is necessary and sufficient for reachability.

There are \(12\) autotopies fixing the seed: this also follows from the orbit-size calculation \(1{,}728{,}000/144{,}000=12\); all preserve each coordinate sign. The independent verifier generates the full \(18{,}000\)-element even-isotopy orbit of a mobile seed using three-cycle generators in each of the row, column, and symbol coordinates. The orbit is exactly the graph component, proving transitivity by \(A_5^3\) rather than inferring it merely from a component-size partition. Each odd relabelling of the three coordinates sends this orbit to one of the other seven components, showing all eight graphs are mutually isomorphic.

**(4) Sharp distances.** Breadth-first search through the complete \(18{,}000\)-vertex component of the seed yields the exact displayed \(14\)-entry distance distribution. Its final positive entry \(59\) occurs at distance \(13\), proving that the seed has eccentricity exactly \(13\). Since the even-isotopy subgroup acts transitively on its component by graph automorphisms, every vertex of that component has exactly the same distribution. The seven odd-isotopy images give all other mobile components, so the distribution, radius and diameter hold for every mobile component. Double counting ordered diametral pairs yields \(8\cdot18{,}000\cdot59/2=4{,}248{,}000\). An explicit second square at distance \(13\) from the displayed seed is

```text
23104
14023
31240
40312
02431
```

## Verification

The standalone files `latin5_cert.cpp` and `latin5_verify.py` implement separate exhaustive enumerations. From a POSIX shell with a C++17 compiler and Python 3, run

```sh
c++ -std=c++17 -O2 latin5_cert.cpp -o latin5_cert
./latin5_cert
python3 latin5_verify.py
```

Both require exact state, component, degree and distance counts; both independently check the symmetry reduction, using the full isotopy parity triple in C++ and an even-isotopy generator orbit plus odd cosets in Python. Their expected final output markers are `LATIN5_EXHAUSTIVE_ORBIT_CERTIFICATE_PASS` and `LATIN5_INDEPENDENT_CERTIFICATE_PASS`. All checks are finite, deterministic, exhaustive and use only standard-language libraries.

## Relationship to prior work

Wanless (2004) classified the order-five Latin squares into two isotopy classes, documented the self-switching intercalates of the non-group class, and studied a **quotient graph whose vertices are isotopy classes**, not the full labelled reconfiguration graph. Therefore his quotient statement does not determine the eight labelled mobile components or their exact diameter. The \(161{,}280\)-square count and the \(56\) reduced-square count are classical and are not presented as new. The conventional parity literature gives related restrictions, but no inspected source was found to entail both the exact eight-component connectivity classification and its sharp \(13\)-switch distances. McKay, Meynert and Myrvold (first published 2 March 2006) survey isotopy and enumeration, not the full labelled-switch metric. Jacobson and Matthews (1996) use a more permissive random-generation mechanism that can pass through improper arrays, not the strict graph defined here.

## Limitations

The result is specific to order \(5\), to fully labelled squares, and to intercalate-only moves. It does not claim a theorem for larger orders, for cycle switches of other lengths, or for algorithms allowing improper intermediate arrays. Exhaustive computation over a rigorously specified finite space is the proof method; it is not an independent formal proof assistant certificate. The historical priority assessment remains qualified: not every older source and unpublished computation could be inspected. The 2004 Wanless paper's accessible publisher listing supplies a publication **month**, not an exact first-public day; a precisely dated 2006 scholarly source is used for the archival date metadata rather than inventing a day in 2004.

## References

1. I. M. Wanless, *Cycle Switches in Latin Squares*, **Graphs and Combinatorics** 20 (2004), 545–570, DOI `10.1007/s00373-004-0567-7`. Author-hosted manuscript: https://users.monash.edu.au/~iwanless/papers/cycleswapgr.GC.pdf .
2. B. D. McKay, A. Meynert, and W. Myrvold, *Small Latin Squares, Quasigroups, and Loops*, **Journal of Combinatorial Designs**, first published 2 March 2006, DOI `10.1002/jcd.20105`.
3. M. T. Jacobson and P. Matthews, *Generating Uniformly Distributed Random Latin Squares*, **Journal of Combinatorial Designs** 4 (1996), 405–437.
4. M. J. L. Mendis and I. M. Wanless, *Latin Squares with a Unique Intercalate*, **Journal of Combinatorial Designs**, published online 29 June 2015, DOI `10.1002/jcd.21430` (abstract-level comparison; complete article not inspected).
5. OEIS A002860, number of Latin squares of order \(n\), https://oeis.org/A002860 .
