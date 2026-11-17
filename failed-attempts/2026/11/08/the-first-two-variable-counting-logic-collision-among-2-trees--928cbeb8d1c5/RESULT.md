# The first two-variable counting-logic collision among 2-trees

## Finding

A **2-tree** is a finite simple undirected graph obtained from a triangle by repeatedly adding one new vertex adjacent to exactly the two ends of an existing edge. Write \(G\equiv_{C^2}H\) if finite graphs \(G,H\) satisfy the same first-order sentences using at most two variable names and counting quantifiers, with no bound on quantifier rank or counting thresholds.

**Theorem.** Among 2-trees, the least order of two nonisomorphic \(C^2\)-equivalent graphs is **eight**. There are exactly \(39\) isomorphism types of eight-vertex 2-trees; these form exactly \(38\) \(C^2\)-equivalence classes. Exactly one class has two members, and all others are singletons. The exceptional pair consists of one outerplanar and one non-outerplanar 2-tree. Thus outerplanarity is not definable by a \(C^2\) sentence even *relative to 2-trees*.

## Assumptions and scope

All graphs are finite, simple, unlabelled for isomorphism classification, and undirected; the empty, one-vertex, and two-vertex graphs are not counted as 2-trees under the triangle-base convention used here. With the alternative convention allowing the single edge as a 2-tree, the theorem is unchanged. The claim compares **two graphs belonging to the 2-tree class**; it does not claim either graph is unidentified among every finite graph of arbitrary type. The logic \(C^2\) is unrestricted in formula depth and numerical counting constants.

## Proof

**1. Explicit witnesses.** Take four core vertices \(A,B,X,Y\), with core edges \(AB,AX,BX,AY,BY\); thus the core is \(K_4\) minus \(XY\). Add four new degree-two vertices \(p,q,r,s\). In \(G\), attach \(p,q\) to the edge \(AX\), and attach \(r,s\) to the edge \(BY\). In \(H\), attach \(p\) to \(AX\), \(q\) to \(AY\), \(r\) to \(BX\), and \(s\) to \(BY\). All attachments are along existing edges, so both are 2-trees. Both have eight vertices and thirteen edges.

In each graph the four ears have degree \(2\), the vertices \(X,Y\) have degree \(4\), and \(A,B\) have degree \(5\). Relative to the ordered degree classes \(2,4,5\), the numbers of neighbors in each class are exactly
\[
Q=\begin{pmatrix}0&1&1\\2&0&2\\2&2&1\end{pmatrix}.
\]
Hence the degree partition is equitable, of class sizes \((4,2,2)\), and it is the stable color-refinement partition in both graphs. Starting from a uniform coloring, the first refinement produces precisely these degree classes; the matrix above shows no later split can occur. Color refinement therefore cannot distinguish \(G\) from \(H\). The standard equivalence between color refinement and two-variable first-order logic with counting yields \(G\equiv_{C^2}H\).

The degree-two vertices in \(G\) have only **two distinct open neighborhoods** (each repeated twice), whereas those in \(H\) have **four distinct open neighborhoods**. This is an isomorphism invariant, so \(G\not\cong H\).

In \(G\), the five vertices \(A,X,B,p,q\) exhibit a \(K_{2,3}\) subgraph with branch vertices \(A,X\) and common neighbors \(B,p,q\); thus \(G\) is not outerplanar. In \(H\), the cycle \(A,p,X,r,B,s,Y,q,A\) is a boundary Hamiltonian cycle, and the remaining edges \(AB,AX,BX,AY,BY\) can all be drawn as noncrossing chords of this cycle. Thus \(H\) is outerplanar. Because one \(C^2\)-equivalence class contains both kinds, no \(C^2\) sentence defines outerplanarity on all 2-trees.

**2. Finite minimality and uniqueness.** Every 2-tree on at least four vertices has an ear of degree two whose two neighbors are adjacent and whose removal leaves a 2-tree; this follows by reversing the final step in a defining construction. Therefore, inductively, every isomorphism type of order \(n\) occurs among the graphs formed by attaching a new ear to **each edge of each representative** of order \(n-1\). The reverse implication is immediate from the definition. Duplicates are discarded by a complete adjacency-preserving isomorphism backtracking algorithm with sound degree and neighbor-degree pruning.

The standalone finite verifier executes precisely this exhaustive recurrence. For orders \(3,4,5,6,7,8\), the numbers of pairwise nonisomorphic representatives are, respectively, \(1,1,2,5,12,39\). Each pair of representatives is compared by color refinement **on the disjoint union**, with shared color IDs: every unmatched color multiplicity separates the pair; stabilization with matching multiplicities certifies equivalence. The resulting numbers of equivalence classes are \(1,1,2,5,12,38\). The only nontrivial class, at order eight, is isomorphic to the pair in Step 1, as checked by complete isomorphism backtracking. The enumeration visits every object by the ear-deletion induction and every pair of isomorphism types at each order; hence this is an exact finite proof of the least order and uniqueness, not a sample or extrapolation. The 2-tree type totals independently match the published enumeration A054581.

## Verification

Run `python3 verify_2tree_c2.py` in the directory containing this result. It uses only Python's standard library. It asserts graph generation and the ear-removal property; tests exact unlabelled isomorphism, independent of probabilistic hashes; runs synchronous shared-palette color refinement on all pairs; checks the degree-class quotient for both explicit witnesses; tests their nonisomorphism and whether they appear as the unique exceptional pair. The expected exact output is `ENUMERATION_OUTPUT.txt`. A separate enumeration implementation using a graph library reproduced the orders and the unique eight-vertex collision; the portable verification artifact, rather than the external library implementation, is supplied here.

## Relationship to prior work

The recursion defining 2-trees and a characterization of their degree sequences appear in Bose et al., arXiv:cs/0605011 (first submitted May 3, 2006). The unlabelled type counts are tabulated by OEIS A054581, reflecting the earlier 2-tree enumeration literature, including Labelle–Lamathe–Leroux, arXiv:math/0312424 (December 23, 2003). Arvind–Köbler–Rattan–Verbitsky, arXiv:1502.01255 (February 4, 2015), reviews the link between color refinement and \(C^2\), and establishes general amenability results, including forests. These sources supply the definitions and techniques but do not state the class-relative eight-vertex collision threshold, the unique doubleton among the \(39\) types, or the contrasting outerplanarity witnesses. The result strengthens a mere degree-sequence collision: the two graphs agree under **all iterations** of color refinement. No claim is made that the general theory of color refinement, 2-tree enumeration, or degree sequences is new.

## Limitations

The theorem is a first-obstruction classification through eight vertices, not a full classification of \(C^2\)-equivalence on larger 2-trees. Prior-art comparison was bounded, so hidden tabulations or unpublished results remain a priority risk. Reproduction and review here are not independent mathematical certification.

## References

1. P. Bose, V. Dujmović, D. Krizanc, S. Langerman, P. Morin, D. R. Wood and S. Wuhrer, *A Characterization of the Degree Sequences of 2-Trees*, arXiv:cs/0605011, first submitted 2006-05-03, https://arxiv.org/abs/cs/0605011.
2. G. Labelle, C. Lamathe and P. Leroux, *Labelled and Unlabelled Enumeration of k-Gonal 2-Trees*, arXiv:math/0312424, first posted 2003-12-23, https://arxiv.org/abs/math/0312424.
3. V. Arvind, J. Köbler, G. Rattan and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first posted 2015-02-04, https://arxiv.org/abs/1502.01255.
4. OEIS Foundation, A054581, *Number of unlabeled 2-trees with n nodes*, https://oeis.org/A054581 (record attributed to V. Jovovic, 2000-04-11).
