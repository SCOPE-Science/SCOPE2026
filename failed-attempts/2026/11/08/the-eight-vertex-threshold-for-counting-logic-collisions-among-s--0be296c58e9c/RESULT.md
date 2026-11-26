# The eight-vertex threshold for counting-logic collisions among split graphs

## Finding
Let \(\mathcal S_n\) be the class of undirected, loopless, simple split graphs on exactly \(n\) vertices, with no additional predicates, constants, or initial vertex colours. Write \(G\equiv_{C^2}H\) when \(G\) and \(H\) satisfy the same two-variable first-order sentences with unrestricted counting quantifiers and unrestricted quantifier depth.

**Theorem.** For \(0\le n\le7\), if \(G,H\in\mathcal S_n\) and \(G\equiv_{C^2}H\), then \(G\cong H\). For every integer \(n\ge8\), there are connected, nonisomorphic graphs \(G_n,H_n\in\mathcal S_n\) with \(G_n\equiv_{C^2}H_n\). Thus eight is exactly the first order at which two nonisomorphic *split graphs* can be indistinguishable by counting two-variable logic. Since counting logic distinguishes cardinalities, the same conclusion holds when comparing split graphs of different orders.

For the order-eight pair, take a clique \(A=\{a_0,a_1,a_2,a_3\}\) and independent vertices \(B=\{b_0,b_1,b_2,b_3\}\). Define the neighbors in \(A\) of \(b_0,b_1,b_2,b_3\), respectively, as follows:

\[
\begin{aligned}
G_8 &: \{a_0,a_1\},\{a_1,a_2\},\{a_2,a_3\},\{a_3,a_0\},\\
H_8 &: \{a_0,a_1\},\{a_0,a_1\},\{a_2,a_3\},\{a_2,a_3\}.
\end{aligned}
\]

For \(n=8+t\), with \(t\ge0\), define \(G_n=K_t\vee G_8\) and \(H_n=K_t\vee H_8\), where \(\vee\) adds all possible edges across the two sides of a join.

## Assumptions and scope
A split graph is one with a partition into a clique and an independent set; the partition need not be specified in the logic and need not be unique. All graphs are finite and uncoloured. The empty graph is allowed in the small-order statement. Identification is **relative to the class of split graphs**: it is not claimed that every split graph of order at most seven is distinguishable from all graphs outside the class. The logical width is exactly at most two reusable variable names; counting thresholds may be arbitrary finite integers, and quantifier rank is not bounded.

## Proof
**Small orders.** Every split graph of order \(n\) admits a clique/independent-set partition with clique size \(k\in\{0,\ldots,n\}\). After numbering the clique before the independent set, the graph is uniquely specified *for that labelled partition* by its \(k(n-k)\) binary cross-adjacency choices. The program `split_threshold_verify.py` iterates all of these choices for every \(0\le n\le7\), so no split graph can be omitted, even when a graph has multiple valid split partitions.

The program performs \(n\) simultaneous standard vertex-colour refinement rounds on this complete collection of presentations of the same order, using **one shared dictionary** of neighbourhood-count signatures per round. It groups graphs by their resulting colour multisets. Finally, for every member of every group it finds a colour-preserving graph isomorphism to the group's first member using exhaustive adjacency-consistent backtracking. Preservation of refinement colours under any isomorphism means this restriction cannot conceal a valid isomorphism. In all 0–7 orders no group contains nonisomorphic graphs. The group counts by order \(0,1,2,3,4,5,6,7\) are, respectively, \(1,1,2,4,9,21,56,164\), in agreement with Royle's published enumeration for positive orders [1]. There are respectively \(1,2,4,10,34,162,1090,10370\) labelled-partition presentations; the double counting caused by alternative partitions is harmless.

If two graphs satisfy the same \(C^2\) sentences, then their shared vertex colour multisets agree after every finite refinement round, by the two-variable counting logic/refinement equivalence [2]. In particular, they agree after the computed \(n\) rounds and belong to a common verified group; they are therefore isomorphic. The exhaustive algorithm is finite, transparent, and available in full as a standalone source file. The finite conclusion depends on performing all these iterations and isomorphism checks, not on an incomplete sample.

**Sharp witness.** Both order-eight graphs are split and connected. In each graph, four vertices have degree five (precisely \(A\)) and four have degree two (precisely \(B\)). Every clique vertex has three neighbors in \(A\) and two in \(B\), and every independent vertex has two in \(A\) and none in \(B\). Starting with a uniform colour, one refinement step therefore creates the two degree classes \(A,B\), and their interclass neighbor counts show that these two classes are equitable and remain unchanged forever. Both graphs have the same class sizes and quotient counts, so colour refinement cannot distinguish them at any depth. By [2] they are \(C^2\)-equivalent.

They are not isomorphic. Since their degree-five and degree-two sets are invariant, any isomorphism preserves \(B\). In \(H_8\), the two vertices \(b_0,b_1\) have exactly the same two-neighbor set in \(A\), whereas all four neighbor sets in \(G_8\) are distinct. Hence no isomorphism exists. This argument does not rely on finite testing.

**Every larger order.** Adjoin the same \(t\ge1\) new universal vertices to each graph. The enlarged graphs remain split, with the new universal vertices joining the clique. Their new universal degree is \(7+t\), whereas old clique degrees are \(5+t\) and old independent degrees \(2+t\). Thus the new universal vertices form a canonically recognized set, and deleting them recovers the respective nonisomorphic order-eight graphs. Each enlarged graph has the same equitable partition into the new vertices, old clique, and old independent set. The equal cell sizes and equal per-cell neighbor counts imply identical refinement colours at every depth, proving their \(C^2\)-equivalence. Both enlarged graphs remain connected.

## Verification
Run `python3 split_threshold_verify.py` using the Python standard library. The program independently generates all cross-edge masks, computes shared refinement signatures, verifies the colour-preserving adjacency bijections, checks the order-eight nonisomorphic pair, and tests universal-join witnesses at orders nine through twelve. Its expected final line is `result: PASS`.

The small-order proof is a complete finite enumeration, not a probabilistic estimate. The universal order-extension theorem is proved symbolically by the equitable partition and degree arguments; tests through order twelve only provide corroboration.

## Relationship to prior work
Royle [1] establishes split-graph enumeration and provides the exact nonisomorphic counts for orders one through seven, but does not classify the split graphs by two-variable counting logic. Arvind, Köbler, Rattan and Verbitsky [2] prove the general logic/colour-refinement connection and criteria for global amenability. Their biregular-replacement lemma (Lemma 6) explains why different cross-edge incidence matrices can be invisible to refinement; it does not assert the sharp *class-relative* split-graph cutoff of eight. Barrus [3] concerns fractional degree-sequence realization rather than counting-logic equivalence. An order-ten *orbit-refinement* threshold for split graphs concerns recovery of automorphism orbits **within one graph**, a logically different property: the order-eight graphs here may each be orbit-refined while being indistinguishable from one another.

## Limitations
The result does not assert global amenability against arbitrary nonsplit graphs, nor does it classify all nonisomorphic indistinguishable pairs on eight vertices. The minimum-order claim relies on an explicit fully exhaustive finite computation with a reproducible, dependency-free checker; it is not being asserted as a new general structural bound for all graph families. Historical priority beyond the inspected sources is not guaranteed, and no independent mathematical audit is claimed.

## References
[1] Gordon F. Royle, *Counting Set Covers and Split Graphs*, Journal of Integer Sequences 3 (2000), article 00.2.6, published June 6, 2000. https://cs.uwaterloo.ca/journals/JIS/VOL3/ROYLE/royle.pdf

[2] V. Arvind, J. Köbler, G. Rattan and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first posted February 4, 2015, particularly the introduction, Section 2 and Lemmas 5–6. https://arxiv.org/abs/1502.01255

[3] Michael D. Barrus, *On Fractional Realizations of Graph Degree Sequences*, arXiv:1310.1112, first posted October 3, 2013. https://arxiv.org/abs/1310.1112
