# The independence complex of \(C_8\times K_3\) is a wedge of a four-sphere and three five-spheres

## Finding

Let \(G=C_8\times K_3\), with categorical graph product (also called the tensor or direct graph product). Its ordinary independence complex has the **integral homotopy type**
\[
\operatorname{Ind}(G)\simeq S^4\vee S^5\vee S^5\vee S^5.
\]
Consequently its reduced integral homology is free of rank one in degree four, free of rank three in degree five, and zero in every other degree. In particular, this specific graph has no integral homology torsion. The assertion does not extend to every cycle product.

## Assumptions and scope

The graph is fixed and finite. Label its 24 vertices \((i,c)\), where \(i\in\{0,\ldots,7\}\) is read modulo eight and \(c\in\{0,1,2\}\). Distinct vertices \((i,c)\) and \((j,d)\) are adjacent exactly when \(j-i\equiv\pm1\pmod8\) and \(c\ne d\). A face is a vertex subset containing no adjacent pair. Dimension means one less than the number of vertices of a nonempty face. All homotopy and homology statements refer to the geometric realization and to integer coefficients unless otherwise specified.

## Proof

**Step 1 (complete face enumeration).** Encode a face by a 24-bit integer \(s\), where bit \(3i+c\) indicates vertex \((i,c)\). For each cycle position \(i\), write its three-bit fiber \(s_i\). Two adjacent fibers can both be nonempty without an edge precisely when they each consist of the *same single color*. Thus a tuple \((s_0,\ldots,s_7)\) of three-bit masks defines an independent face if and only if, for every cyclically adjacent pair \((a,b)\), either \(a=0\), or \(b=0\), or \(a=b\) and \(a\) contains exactly one bit. This gives exactly 18,722 faces including the empty face. The verifier independently reconstructs the same 18,722 faces using all 24 original graph-neighborhood masks, not this fiber condition.

**Step 2 (explicit acyclic matching).** Order the vertices as \((0,0),(1,0),\ldots,(7,0),(0,1),\ldots,(7,1),(0,2),\ldots,(7,2)\). Starting with all faces unpaired, process each vertex \(v\) in this order. For every currently unpaired face \(\sigma\) not containing \(v\) such that \(\sigma\cup\{v\}\) is also currently unpaired, pair these two faces and remove both from the pool. These pairs are disjoint within each stage. The empty face is initially paired with the singleton encoded by integer 1; omit that pair from the ordinary, nonaugmented face poset, leaving the singleton as a critical vertex. This procedure yields exactly 9,358 pairs among the 18,721 nonempty faces and exactly five critical nonempty faces: the vertex encoded by 1, the four-dimensional face encoded by 149522, and the five-dimensional faces encoded by 4737312, 4792338 and 9584676. These integers are exact bit masks with the specified labeling, not cardinality approximations.

To certify acyclicity, orient every codimension-one face relation from the higher-dimensional face down to the lower-dimensional face, except reverse the orientation of matched relations. The executable checker constructs **every** one of the 104,568 directed Hasse edges on all 18,721 nonempty faces and removes all vertices by a topological sort. Hence there is no directed cycle and the matching is acyclic. Ordinary simplicial discrete Morse cancellation therefore produces a homotopy-equivalent CW complex with exactly one cell in each of dimensions zero and four and three cells in dimension five, and no other cells.

**Step 3 (integral attachments).** Having no cells of dimensions one, two or three, the CW four-skeleton is \(S^4\). Only the three degree-five attaching maps remain. The checker computes their *signed integer* cellular boundary coefficients, rather than just their parities. For each oriented four-face \(\tau\), let \(g(\tau)\) be its coefficient along the unique critical four-cell after the elementary cancellations. Set \(g(149522)=1\) and \(g(\tau)=0\) if \(\tau\) is neither critical nor the lower partner of a matched pair between dimensions four and five. If \(\tau\) is matched to a five-face \(\eta\), then the simplicial boundary of \(\eta\) gives the exact recurrence
\[
 g(\tau)=-\frac{\sum_{\tau'\subset\eta,\,\tau'\ne\tau,\,|\tau'|=5}[\eta:\tau']\,g(\tau')}{[\eta:\tau]},
\]
where incidence numbers \([\eta:\tau']\in\{+1,-1\}\) use ascending bit-index vertex orientation. Acyclicity makes this recursion well-founded and each denominator is a unit. The three resulting degree-five-to-degree-four integer boundary coefficients, in ascending encoded critical-mask order, are **\((0,0,0)\)**. This is explicitly recomputed rather than inferred from any field calculation.

Each five-cell is therefore attached to \(S^4\) by a map of degree zero. Since \(\pi_4(S^4)\cong\mathbb Z\) and degree classifies these attaching maps, they are nullhomotopic. Attaching three five-cells gives exactly \(S^4\vee 3S^5\), proving the claimed **integral** homotopy equivalence.

## Verification

The self-contained Python 3 program `verify.py` regenerates the full face set twice (fiber criterion and direct graph neighborhoods), constructs all matching pairs, checks every nonaugmented Hasse edge for acyclicity, evaluates the exact signed integer cancellation recurrence, and computes reduced mod-two Betti numbers by independent boundary-matrix elimination. Its executable assertions require 18,722 faces, 9,358 nonempty matched pairs, critical dimension distribution \((1,1,3)\) in dimensions zero, four and five, all three integer Morse coefficients zero, and mod-two ranks one and three in degrees four and five. Run `python3 verify.py` from the extracted artifact directory. The entire finite state space is enumerated, not sampled. The code and argument together give a reproducible finite mathematical certificate; computations for other products are not claimed.

## Relationship to prior work

Antolín Camarena and Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs* (first public arXiv version July 23, 2023; later published in *Homology, Homotopy and Applications* 26(2), 2024), prove a two-consecutive-dimensions restriction for the non-multiple-of-three cycle cases. They **specifically name** \(C_8\times K_3\) as having nonzero free homology in both possible dimensions and pose the question of integral torsion in the family. Their theorems do not provide the three/four-dimensional multiplicities in this case, the exact integer attaching maps, or this homotopy equivalence. The result here determines one explicitly motivated finite case and does **not** resolve their general torsion question.

## Limitations

This is an exact statement for a single 24-vertex graph, not a classification for arbitrary cycle lengths or complete-graph factors. The complete acyclic-matching certificate has not received an independent mathematical audit. The absence of a covering published statement in the inspected sources does not establish absolute publication priority; an equivalent computation under another representation may exist. A mod-two rank calculation alone would not prove torsion-freeness or an integral wedge, which is why the signed Morse calculation is necessary.

## References

1. O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401v1 (July 23, 2023), revised v2 (September 1, 2023); *Homology, Homotopy and Applications* 26(2) (2024), 349–373, DOI 10.4310/HHA.2024.v26.n2.a17. Available: https://arxiv.org/html/2307.12401v2 and https://arxiv.org/abs/2307.12401.
2. O. Antolín Camarena and A. Carnero Bravo, *Homotopy type through homology groups*, arXiv:2212.07509 (December 14, 2022). Background on consecutive-dimensional homology and homotopy classification.
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. Standard discrete Morse cancellation and acyclic-matching theorem.
