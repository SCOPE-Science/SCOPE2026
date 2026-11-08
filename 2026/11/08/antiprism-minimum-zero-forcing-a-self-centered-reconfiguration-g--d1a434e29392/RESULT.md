# Antiprism minimum zero forcing: a self-centered reconfiguration graph and two propagation times

## Finding

**Theorem.** For every integer \(n\ge 4\), put \(m=2n\), and let \(G_n\) be the square of the \(m\)-cycle, with vertices \(\mathbb Z/m\mathbb Z\) and edges between distinct vertices at circular distance one or two. This is the standard \(n\)-antiprism graph. A zero-forcing move makes the unique white neighbor of a blue vertex blue. In the synchronous version all currently possible moves occur in each round.

The zero-forcing number of \(G_n\) is four. All minimum zero-forcing sets are exactly the following \(3m=6n\) **distinct** sets, with indices taken modulo \(m\):
\[
 A_i=\{i,i+1,i+2,i+3\},\qquad
 B_i=\{i,i+1,i+2,i+4\},\qquad
 C_i=\{i-2,i,i+1,i+2\}.
\]
Their synchronous propagation times are respectively \(n-2,n-1,n-1\). Consequently the complete minimum-set propagation-time enumerator is
\[
 F_n(z)=\sum_{S:\,|S|=4,\ S\text{ zero forcing}}z^{\operatorname{pt}(S)}
 =2n z^{n-2}+4n z^{n-1}.
\]

Under **token-jumping reconfiguration**, two minimum sets are adjacent exactly when they differ by replacing one vertex. The resulting graph \(\mathcal Z(G_n)\) has \(6n\) vertices and \(18n\) edges. It is connected and has the following complete adjacency specification (all indices modulo \(m\)):
\[
\begin{aligned}
N(A_i)&=\{A_{i-1},A_{i+1},B_{i-1},B_i,B_{i+1},C_i,C_{i+1},C_{i+2}\},\\
N(B_i)&=\{A_{i-1},A_i,A_{i+1},C_i,C_{i+2}\},\\
N(C_i)&=\{A_{i-2},A_{i-1},A_i,B_i,B_{i-2}\}.
\end{aligned}
\]
In particular, every \(A\)-state has degree eight and every \(B\)- or \(C\)-state has degree five. **Every state has eccentricity exactly \(n\)**, so both the radius and the diameter are exactly \(n\). This gives a nonregular, non-vertex-transitive, self-centered family of zero-forcing reconfiguration graphs with unbounded diameter and uniformly bounded degree.

## Assumptions and scope

The base graph is simple and undirected, with \(n\ge4\) and hence \(m\ge8\). The \(n=3\) octahedral boundary is not included. The zero-forcing rule is the **ordinary** rule on the base graph, not positive-semidefinite or skew zero forcing. Its propagation time counts parallel rounds, always performing all currently available forces. Reconfiguration is **unrestricted token jumping between minimum feasible sets**, not token sliding along a base-graph edge and not a process on partial blue sets. All vertices and initial sets are labelled; no symmetry quotient is taken.

## Proof

**1. Lower bound, exhaustive characterization of minimum sets.** Every vertex has degree four. Until a first force occurs from a set of initially blue vertices \(S\), some blue vertex \(v\) must have three of its four neighbors blue. Thus \(|S|\ge4\), and if \(|S|=4\), necessarily
\[
S=\{v\}\cup\bigl(N_{G_n}(v)\setminus\{w\}\bigr)
\quad\text{for some }w\in N_{G_n}(v).
\]
The closed neighborhood of \(v\) comprises \(v-2,v-1,v,v+1,v+2\). Deleting one of its four neighbors gives precisely the displayed \(A\)-, \(B\)- or \(C\)-families: deleting \(v-2\) or \(v+2\) yields consecutive four-sets \(A\); deleting \(v+1\) gives a \(B\)-set, and deleting \(v-1\) gives a \(C\)-set. For \(m\ge8\), the \(3m\) displayed sets are distinct: consecutive four-sets are characterized by having three consecutive occupied cycle edges, whereas the \(B\) and \(C\) patterns are the two nonrotationally-equivalent orientations of circular gaps \((1,1,2,m-4)\) and \((2,1,1,m-4)\). Each \(A\)-set has exactly two possible first-forcing witnesses; \(B\)- and \(C\)-sets have one. Therefore there are no other size-four zero-forcing candidates.

**2. Each candidate forces, with its exact time.** For \(A_0\), after round \(r\), while not completed, the blue vertices are exactly the cyclic interval from \(-r\) through \(3+r\), inclusive. Initially that interval has four vertices. At each subsequent round, the second vertex from either blue-interval endpoint can force the next vertex just outside that endpoint; no further vertex can be forced that round, since every other white vertex has no blue neighbor with a unique white neighbor. The interval grows by two until its size is \(m\), at round \((m-4)/2=n-2\).

For \(B_0=\{0,1,2,4\}\), the unique first-round new vertex is \(3\), forced from \(2\). This leaves the blue interval \(\{0,1,2,3,4\}\). From then onward both ends advance by one each round (with the two fronts meeting in one final vertex), and completion occurs at round \(1+\lceil(m-5)/2\rceil=n-1\). Reflection \(x\mapsto2-x\pmod m\) carries \(B_0\) to \(C_0\) and preserves the forcing process, so every \(C\)-set also has propagation time \(n-1\). Rotational symmetry covers every index. Thus all candidates force and the degree-four lower bound is sharp.

**3. Complete reconfiguration adjacency and connectivity.** For four-element sets, one token jump is equivalent to intersection of cardinality three. Directly intersecting each of the three displayed forms with its translates gives precisely the three neighbor formulas in the theorem. There are \(m\) states of degree eight and \(2m\) states of degree five, so the handshaking lemma gives \((8m+10m)/2=9m=18n\) edges. The states \(A_i\) themselves induce the cycle \(C_m\), and every other state has an \(A\)-neighbor; hence the reconfiguration graph is connected.

**4. Exact radius and diameter.** Define a cyclic **center coordinate** \(\phi\) on states by
\[
\phi(A_i)=i,\quad \phi(B_i)=i,\quad \phi(C_i)=i-1\pmod m.
\]
Each edge in the explicit adjacency specification changes \(\phi\) by cyclic distance at most one. Consequently every path from any state \(X\) to \(A_{\phi(X)+n}\) has at least \(n\) edges, proving every vertex has eccentricity at least \(n\).

For the upper bound, each \(A_i\) is adjacent along the \(A\)-cycle to \(A_{i\pm1}\). Every \(B_i\) has the three consecutive \(A\)-neighbors indexed \(i-1,i,i+1\); every \(C_i\) has those indexed \(i-2,i-1,i\). For two \(A\)-states, the \(A\)-cycle gives distance at most \(n\). For an \(A\)-state and a non-\(A\)-state, the cyclic distance from the single index to the nearest index of a consecutive triple is at most \(n-1\); entering the triple costs one additional edge. For two non-\(A\)-states, the cyclic distance between their consecutive triples is at most \(n-2\); entering and leaving the \(A\)-cycle costs two additional edges. Thus every pair of states is at distance at most \(n\). Combined with the lower bound, every eccentricity, the radius and the diameter equal \(n\). Since degrees differ between states, the graph is not vertex-transitive.

## Verification

The theorem above is a closed, all-order mathematical proof. The scripts are independent corroboration, **not** a substitute for this proof. Run from a directory containing both files:

```sh
python3 check_enumeration.py
c++ -std=c++17 -O2 check_structural.cpp -o check_structural
./check_structural
```

The Python program independently enumerates every four-vertex subset for even cycle orders from eight through twenty-six, simulates all synchronous zero-forcing steps with bitmasks, rebuilds the reconfiguration graph from those successful sets, and checks the complete propagation-time and eccentricity classifications. The C++ program independently implements vertex sets and a neighbor-by-neighbor synchronous forcing simulation, enumerates all four-subsets through order twenty-two, checks all predicted sets through order thirty, and computes all reconfiguration eccentricities through order thirty. Both programs terminate with distinct PASS markers when all assertions hold.

## Relationship to prior work

The zero-forcing rule and the minimum-rank motivation originate in the classical zero-forcing literature. Hogben et al., *Propagation time for zero forcing on a graph* (arXiv:1410.4191, first posted 2014-10-15), introduce systematic propagation-time comparisons and define efficient minimum sets; no theorem in the inspected text classifies antiprism initial sets or their full time spectrum. Boyer et al., *The zero forcing polynomial of a graph* (arXiv:1801.08910, 2018-01-26), systematically count zero-forcing sets and derive formulas for paths, cycles, wheels, and other families; the inspected sections do not give the minimum-set coefficient for the **square** of an even cycle. Geneson, Haas and Hogben, *Reconfiguration graphs of zero forcing sets* (arXiv:2009.00220, 2020-09-01), introduce the exact token-jumping graph used here, including its cycle example, and study general connectivity; its inspected text does not classify the reconfiguration graph of cycle squares. These works supply the terminology and motivation, not the stated antiprism theorem.

The ordinary cycle's zero-forcing graph being a cycle is a known theorem; it does not imply this result for a graph square. General properties such as the lower bound \(Z(G)\ge\delta(G)\) or abstract reconfiguration definitions likewise do not imply the exact \(6n\)-state graph, its two propagation times, or its universal eccentricity. Searches for *antiprism*, *cycle square*, *second power of a cycle*, and *quartic circulant* did not identify an equivalent complete result in the inspected primary materials. Search absence is not a proof of priority.

## Limitations

The domain excludes the octahedral \(n=3\) boundary, where degree and possible neighborhood overlaps require separate treatment. Only minimum-cardinality zero-forcing sets and their synchronous propagation times are classified; this is not the full zero-forcing polynomial over all cardinalities. The reconfiguration move is token jumping, not token sliding or forcing-chain reversal. The work does not assert novelty of the base-graph zero-forcing rule, the lower bound, or the general reconfiguration framework. Historical priority remains subject to independent literature review, including possible unindexed equivalences or terminology not surfaced by the specified searches. No external independent audit has been carried out.

## References

1. Leslie Hogben, My Huynh, Nicole Kingsley, Sarah Meyer, Shanise Walker, Michael Young, *Propagation time for zero forcing on a graph*, arXiv:1410.4191, first posted 2014-10-15. https://arxiv.org/abs/1410.4191
2. Kirk Boyer, Boris Brimkov, Sean English, Daniela Ferrero, Ariel Keller, Rachel Kirsch, Michael Phillips, Carolyn Reinhart, *The zero forcing polynomial of a graph*, arXiv:1801.08910, first posted 2018-01-26. https://arxiv.org/abs/1801.08910
3. Jesse Geneson, Ruth Haas, Leslie Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220, first posted 2020-09-01. https://arxiv.org/abs/2009.00220
4. Eric W. Weisstein, *Antiprism Graph*, MathWorld, https://mathworld.wolfram.com/AntiprismGraph.html (graph identification, not the theorem).
