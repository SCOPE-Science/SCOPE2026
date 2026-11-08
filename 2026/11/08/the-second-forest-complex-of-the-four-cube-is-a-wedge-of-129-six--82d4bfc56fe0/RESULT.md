# The second forest complex of the four-cube is a wedge of \(129\) six-spheres

## Finding
Let \(Q_4\) denote the sixteen-vertex four-dimensional hypercube, equivalently \(C_4\mathbin{\square}C_4\), the fully periodic \(4\times4\) square grid. Its second forest complex \(\mathcal F_2(Q_4)\) has simplices precisely the vertex subsets inducing linear forests: every component is a path (including singleton paths). The complete homotopy type is
\[
\mathcal F_2(Q_4)\simeq\bigvee^{129}S^6.
\]
Consequently, the only nonzero reduced integral homology is \(\widetilde H_6\cong\mathbb Z^{129}\); in particular there is no torsion. Although the complex is seven-dimensional, its facets occur in both dimensions six and seven. This is a classification of one finite natural graph complex, not an infinite hypercube-family theorem.

## Assumptions and scope
Label the vertices by integers \(0,1,\dots,15\), understood as four-bit words. Two distinct vertices are adjacent exactly when their bitwise exclusive-or has one set bit. A face is a subset \(S\) for which (i) each selected vertex has at most two selected neighbors and (ii) the selected induced subgraph contains no cycle. Condition (ii) cannot be dropped: some degree-two induced subsets of \(Q_4\) are cycles. Membership masks are integers whose \(v\)-th bit indicates whether \(v\) is selected. The usual nonempty-face convention is used for the Morse matching, and the empty face is included only in augmented enumeration and reduced Euler-characteristic checks. All coefficients in the homotopy and homology conclusions are integral.

## Proof
**Complete face universe.** Exhaustively enumerate each of the \(2^{16}=65,536\) membership masks. An exact union-find cycle test and a separate componentwise test (which checks that each component's edge count is one less than its order) agree on every mask. The number of faces, including the empty set, is \(14,911\). The face vector by cardinality from zero through eight is
\[
(1,16,120,560,1732,3552,4616,3392,922).
\]
There are \(192\) maximal faces of dimension six and \(922\) of dimension seven. Their alternating count gives reduced Euler characteristic \(129\), but this count alone does not determine homotopy type.

**Two complete acyclic matchings.** Start with all \(14,910\) nonempty faces. In the forward matching, for each pivot vertex \(v=0,1,\ldots,15\), pair any still-unmatched face \(a\) omitting \(v\) with \(a\cup\{v\}\) when both are still unmatched; remove both. The reverse matching uses pivots \(15,14,\ldots,0\). In both cases exactly \(7,383\) disjoint pairs are produced, leaving one critical vertex, seven critical five-simplices and \(136\) critical six-simplices. To verify acyclicity rather than infer it from matching counts, orient each nonempty-face Hasse covering relation downwards, except reverse matched covers. For each of the two matchings the verifier constructs all \(85,424\) covering relations and removes all \(14,910\) vertices of this directed graph by a topological sort. Thus both matching orientations are acyclic. Discrete Morse theory gives a CW model with those critical-cell dimensions.

**Signed attaching degrees and integral units.** Orient every simplex by its increasing vertex labels. For each paired lower simplex \(a\) and upper simplex \(b\), the coefficient \(\epsilon(a,b)\) of \(a\) in \(\partial b\) is \(\pm1\). Recursively replace \(a\) by \(-\epsilon(a,b)\sum_{a'\ne a}\epsilon(a',b)a'\), project upper members of matched pairs to zero, and keep critical lower members. Acyclicity makes this signed recursion finite. Applied to boundaries of all critical six-simplices, it produces an exact integral Morse boundary \(\partial_6:\mathbb Z^{136}\to\mathbb Z^7\). The forward critical five-face masks, in ascending order, are \(1452,2668,17290,18538,24726,33898,57358\). Select the seven critical six-face masks \(6872,7112,7352,7592,11384,28778,34228\). Their columns, transposed into rows and ordered as listed, give the following \(7\times7\) minor:

```text
 0 -1  0 -1  0  0  0
 0  0  1  0  0  0  0
 0  0  0  1  1  0 -1
 1  0 -1  0  1  0 -1
 0  0  0 -1  0  0  0
 0  0  0  0  0  0 -1
 1  0 -1  0  0 -1  0
```

Its integer determinant is \(-1\). Hence \(\partial_6\) is surjective and *all seven nonzero Smith invariant factors are units* (there cannot be any other factors because the codomain has rank seven). The reverse-order matching gives a second \(7\times136\) matrix with a different unit minor: use critical six-face masks \(1964,1994,2908,3386,5548,7777,12590\), again obtaining determinant \(-1\). No other positive-dimensional differentials occur in either reduced CW model.

**From the boundary to homotopy.** The five-skeleton of the Morse CW model is a wedge of seven five-spheres with one zero-cell. The \(136\) six-cells attach by maps whose homotopy classes are completely specified by their integer degree vectors, because the Hurewicz map \(\pi_5(\bigvee^7S^5)\to H_5(\bigvee^7S^5;\mathbb Z)\) is an isomorphism. The seven chosen six-cells have a unimodular attaching matrix, so their attaching maps collectively form a self-homotopy equivalence of the wedge of seven five-spheres. Their mapping cone is contractible. Each of the remaining \(129\) six-cells therefore attaches to a contractible subcomplex and contributes a six-sphere. This proves the claimed wedge homotopy type, not just Betti numbers.

## Verification
Run `python3 verify_q4_forest2.py` using only Python's standard library. The self-contained checker rebuilds the graph and all subsets using two independent predicates, verifies both full directed-Hasse acyclicity tests, reconstructs both exact signed Morse boundary matrices and their specified determinant-\(-1\) minors by fraction-free integer arithmetic, and separately computes all original simplicial boundary ranks over \(\mathbb F_2\). The mod-two ranks of \(\partial_1,\ldots,\partial_7\) are \((15,105,455,1277,2275,2341,922)\); these independently yield reduced Betti rank \(129\) in degree six and zero elsewhere. The accompanying `verification_output.txt` is one actual execution record; it is not the sole basis of the proof. No external computation, proprietary package or previously recorded matrix is needed to rerun the verifier.

## Relationship to prior work
Carnero Bravo's *The Forest Filtration of a Graph* (first public arXiv posting July 25, 2023) defines \(\mathcal F_d\), proves general filtration properties and treats paths, cycles, joins, certain Cartesian ladders and categorical graph products. Its graph-product results do not give the case of the Cartesian four-fold product \(K_2\mathbin{\square}K_2\mathbin{\square}K_2\mathbin{\square}K_2\) at filtration level two. An existing exact calculation of \(\operatorname{Ind}_2(Q_4)=\mathcal F_1(Q_4)\) addresses the *first* stage and obtains \(\bigvee^{16}S^3\vee S^4\), not the second-stage result here. The separate published total three-cut complex \(\Delta^t_3(Q_4)\) also has \(129\) sphere summands, but in dimension ten; its facets are complements of independent triples, not vertex-induced linear forests. Equality of those sphere counts does not provide a reduction between the constructions. Searches of these equivalent formulations and their homotopy consequences found no stronger result implying the present classification. An unindexed equivalent computation remains possible.

## Limitations
The result concerns only \(Q_4\) and the *vertex-induced* second forest stage. It does not prove a formula for other hypercubes or determine the inclusion-induced persistent homology maps between filtration stages. The matching produces a homotopy-equivalent CW complex; a direct simplicial collapse of the original complex to a subcomplex visibly realizing this wedge is not claimed. The checker gives exhaustive finite evidence for exactly the graph and conditions specified, not an infinite-family argument. No independent external audit has been performed.

## References
1. Andrés Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, first publicly posted 2023-07-25. Full preprint: https://arxiv.org/pdf/2307.13271 .
2. *The four-cube independence complex is a wedge of seven three-spheres*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-four-cube-independence-complex-is-a-wedge-of-seven-three-sph--9947aaad144c .
3. *The total \(3\)-cut complex of the \(4\)-cube: a \(129\)-sphere wedge and its hyperoctahedral character*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-total-3-cut-complex-of-the-4-cube-a-129-sphere-wedge-and-its--ccb644c2e2a2 .
