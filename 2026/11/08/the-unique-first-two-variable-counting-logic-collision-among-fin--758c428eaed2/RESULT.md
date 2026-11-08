# The unique first two-variable counting-logic collision among finite tournaments

## Finding
Let a tournament be a finite directed graph with exactly one arc between every pair of distinct vertices. In the language with a single directed binary relation and equality, let \(T\equiv_{\mathrm C^2}U\) mean equality of all two-variable first-order sentences with counting quantifiers, with no quantifier-rank restriction. Then:

1. For all tournaments \(T,U\) of order at most five, \(T\equiv_{\mathrm C^2}U\) implies \(T\cong U\).
2. On six vertices there are 56 unlabelled tournaments and 55 \(\mathrm C^2\)-equivalence classes; there is exactly one non-singleton class and it consists of two nonisomorphic tournaments.
3. The two exceptional tournaments have, respectively, zero and three induced transitive four-vertex subtournaments. For each \(n\ge 6\) there are nonisomorphic \(\mathrm C^2\)-equivalent tournaments on \(n\) vertices.

Thus the first finite tournament obstruction also separates an induced-subtournament count not determined by two-variable counting logic.

## Assumptions and scope
All objects are finite, loopless tournaments. Equivalence is unrestricted in quantifier depth, counts the two arc directions separately and uses no constants or unary colors. Relative identification here agrees with absolute identification among directed structures, since the tournament axioms are expressible using two variables. An induced four-vertex subtournament is *transitive* if its arcs respect one strict total order.

Encode a six-vertex tournament by a length-15 binary word, in lexicographic order of unordered vertex pairs \((i,j)\) with \(0\le i<j<6\); bit 1 means \(i\to j\), bit 0 means \(j\to i\). An exceptional pair is

```
A = 101001001010101
B = 101001010001101
```

These words are separate, labelled representatives of the two unlabelled types; other representatives are isomorphic to them.

## Proof
**The explicit obstruction.** In both \(A\) and \(B\), vertices \(0,1,2\) each have outdegree two and vertices \(3,4,5\) each have outdegree three. Each of these three-element degree classes induces a directed triangle. Each low-degree vertex has precisely one outgoing arc to the high-degree class, and each high-degree vertex has precisely two outgoing arcs to the low-degree class. In \(A\), the low-to-high cross-arcs are \((0,3),(1,5),(2,4)\); in \(B\), they are \((0,3),(1,4),(2,5)\). Consequently the two degree classes (of cardinalities three and three) are equitable with identical directed neighbour-count vectors \((1,1)\) on the low class and \((2,1)\) on the high class. The ordinary directed color-refinement process, starting with one vertex color and remembering outgoing and incoming neighbor-color multisets, separates these two classes by outdegree on round one but never splits either class further. It gives exactly the same color profile in both tournaments, so \(A\equiv_{\mathrm C^2}B\) by the standard \(\mathrm C^2\)/color-refinement correspondence.

Direct inspection of the 15 arc bits gives zero transitive induced subtournaments of order four in \(A\) and three in \(B\), as independently checked by `verify_mckay.py`. Therefore \(A\not\cong B\). The count also proves that \(\mathrm C^2\) does not determine the induced-transitive-four-subtournament count even on tournaments of order six.

**Exhaustiveness below and at order six.** Every tournament on \(n\ge2\) vertices arises by deleting its last vertex to obtain a tournament on \(n-1\) vertices, then choosing the orientations of its \(n-1\) incident arcs. The verifier recursively performs all such extensions of one representative from each existing isomorphism class. A complete search through the \(n!\) vertex permutations provides an exact canonical minimum for each candidate; deduplication by that minimum leaves precisely one representative per unlabelled tournament. This proves, inductively, that the enumerator is exhaustive and free of duplicate isomorphism classes. It obtains, at orders \(1,2,3,4,5,6\), the class counts \(1,1,2,4,12,56\).

For each order the verifier colors *all* representatives in one shared palette, updates a color using the previous color and sorted multisets of in-neighbor and out-neighbor colors, and stops only when the equitable partitions stabilize. Two representatives lie in one \(\mathrm C^2\)-class exactly when the sorted multisets of their final vertex colors agree. The resulting class counts are \(1,1,2,4,12,55\). At order six the sole nonsingleton class consists of precisely the two examples above. An independent check using McKay's published list of 56 nonisomorphic six-vertex tournaments obtains the same 55 classes and locates the colliding representatives in entries 49 and 50 (one-indexed). The separate generator and catalogue check are provided as runnable source.

**All larger orders.** For every integer \(m\ge0\), add \(m\) new vertices \(s_1,\dots,s_m\), orient them transitively \(s_i\to s_j\) for \(i<j\), and put an arc \(s_i\to v\) for every old vertex \(v\) in both \(A\) and \(B\). Give every new vertex its own color, while retaining the two original degree classes as colors. The paired partitions are equitable, with the same sizes and directed quotients; the common uncolored refinement is therefore identical, proving \(\mathrm C^2\)-equivalence of the augmented tournaments. Moreover each new vertex has outdegree at least six, while each old vertex retains its original outdegree at most three. Thus the original six vertices form the canonical induced subtournament of vertices of outdegree at most three in either extension. An isomorphism of the extensions would restrict to an isomorphism \(A\cong B\), a contradiction. Taking \(n=6+m\) establishes the statement for all \(n\ge6\).

## Verification
Run `g++ -std=c++17 -O2 verify.cpp -o verify && ./verify` and `python3 verify_mckay.py` from the files in this package. `verify.cpp` builds all unlabelled tournaments through order six from first principles using exact permutation-based canonicalization, then compares directed color-refinement profiles using shared colors. `verify_mckay.py` separately computes the six-vertex profiles directly from a transcription of McKay's 56-row published catalogue; it also counts induced transitive four-vertex subtournaments by exact enumeration. Expected output is recorded in `CHECKS.txt`. Both programs are finite tests; the infinite-order conclusion rests on the preceding construction.

## Relationship to prior work
Kiefer, Schweitzer and Selman (2015) establish the general relation between counting logic and color refinement and classify \(\mathrm C^2\)-identified finite binary relational structures, providing a broad theoretical test but not the 55-class six-vertex tournament partition, its unique nonisomorphic pair, or the contrasting induced transitive-four counts. McKay's six-vertex tournament catalogue establishes the 56 input types independently, but contains no \(\mathrm C^2\)-equivalence classification. The present exact first-layer census is an application and numerical refinement within that older general theory, not a new general characterization of \(\mathrm C^2\)-identification.

## Limitations
The exact uniqueness classification is only for tournaments of order at most six. The larger-order construction establishes existence, not the number of equivalence classes at higher orders. The computation has been reviewed together with the constructive argument but not independently audited. The broad 2015 classification and other unindexed specialized studies may reduce the historical novelty of the first-layer census; priority is not certified.

## References
1. S. Kiefer, P. Schweitzer, E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792v1, first submitted 2015-03-30; especially the introduction and Theorems 24 and 27. https://arxiv.org/abs/1503.08792
2. B. D. McKay, *Small tournaments*, exhaustive catalogue of 56 six-vertex tournament representatives: https://users.cecs.anu.edu.au/~bdm/data/tourn6.txt ; catalogue index: https://users.cecs.anu.edu.au/~bdm/data/digraphs.html
