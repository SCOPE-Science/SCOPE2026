# Integral homotopy and persistence of the Frucht graph's induced-forest filtration

## Finding

Let \(G\) be the twelve-vertex Frucht graph specified below. For each integer \(d\geq0\), define the vertex-induced forest complex
\[
\mathcal F_d(G)=\{S\subseteq V(G):G[S]\text{ is acyclic and }\Delta(G[S])\leq d\}.
\]
The full sequence of **integral homotopy types** is
\[
\begin{aligned}
\mathcal F_0(G)&\simeq\bigvee^3 S^2,\\
\mathcal F_1(G)&\simeq S^3,\\
\mathcal F_2(G)&\simeq\bigvee^4 S^6\vee S^7,\\
\mathcal F_d(G)&\simeq\bigvee^3 S^6\vee S^7\quad(d\geq3).
\end{aligned}
\]
The degree-zero stage is the ordinary independence complex; its homotopy type was also identified in earlier work. The new classification concerns the higher stages and their inclusion-induced homology.

All reduced integral homology groups are free. The persistence module for inclusions \(\mathcal F_d(G)\hookrightarrow\mathcal F_{d+1}(G)\), with the terminal stage constant for \(d\geq3\), **splits over \(\mathbb Z\)** into the following interval modules:
\[
\begin{array}{c|l}
\text{degree}&\text{intervals with multiplicity}\\\hline
2&3\,[0,1)\\
3&[1,2)\\
6&2\,[2,3)\quad+\quad2\,[2,\infty)\quad+\quad[3,\infty)\\
7&[2,\infty).
\end{array}
\]
In particular, the final inclusion **kills two** independent degree-six integral classes and **creates one** different degree-six class. The degree-seven class survives unchanged. This is a statement about the actual inclusion homomorphism, not a deduction from ranks alone.

## Assumptions and scope

Use vertices \(0,1,\ldots,11\), cyclic edges \(\{i,i+1\pmod{12}\}\), and twelve LCF chord proposals \(\{i,i+s_i\pmod{12}\}\), where
\[
(s_0,\ldots,s_{11})=(-5,-2,-4,2,5,-2,2,5,-2,-5,4,2).
\]
Duplicate undirected chord proposals are identified. This produces exactly eighteen edges and every vertex has degree three. The LCF graph is isomorphic to the usual Frucht graph. All faces include the empty simplex by convention; the face dimension is \(|S|-1\), and the empty induced graph is acyclic with maximum degree zero. No weighted, directed, metric or equivariant variant is asserted.

For \(d=0\) the permitted induced graph has no edges. For \(d=1\) it is a matching together with isolated vertices, and for \(d=2\) it is a disjoint union of paths. Cubicity gives \(\mathcal F_d(G)=\mathcal F_3(G)\) for \(d\geq3\). The integer-parameter filtration is discrete; half-open intervals refer to its steps, not a continuous metric parameter.

## Proof

**1. Exhaustive face identification.** The attached standard-library checker constructs the eighteen graph edges from the displayed LCF data. It tests all \(2^{12}=4096\) vertex subsets using two separately implemented cycle-detection criteria and computes the induced degree bound directly. For \(d=0,1,2,3\), the numbers of faces **including the empty face** are respectively \(169,825,2335,2542\). The corresponding face vectors, indexed by dimension \(-1,0,\ldots,8\), are
\[
\begin{array}{c|rrrrrrrrrr}
d&-1&0&1&2&3&4&5&6&7&8\\\hline
0&1&12&48&73&34&1&0&0&0&0\\
1&1&12&66&190&293&209&53&1&0&0\\
2&1&12&66&217&464&653&580&287&55&0\\
3&1&12&66&217&467&675&642&368&94&0.
\end{array}
\]

**2. Acyclic discrete-Morse matchings.** At a chosen pivot vertex \(v\), pair every still-unpaired nonempty face \(S\) omitting \(v\) with \(S\cup\{v\}\), whenever both are still unpaired; remove both faces before continuing. Leave the singleton \(\{0\}\) permanently unpaired. Use ascending vertex order for \(d=0,2,3\) and descending order for \(d=1\). Each pair is a codimension-one incidence. Orient a Hasse-diagram incidence from lower to upper unless matched, in which case reverse it. Exhaustive topological sorting of every oriented incidence proves each matching acyclic, with the following certificates:

| Stage | Matched pairs | Directed incidences | Critical nonempty cells |
| --- | ---: | ---: | --- |
| \(d=0\) | 82 | 456 | one 0-cell; three 2-cells |
| \(d=1\) | 411 | 3244 | one 0-cell; one 3-cell |
| \(d=2\) | 1164 | 11833 | one 0-cell; four 6-cells; one 7-cell |
| \(d=3\) | 1267 | 13206 | one 0-cell; four 6-cells; two 7-cells |

By the discrete-Morse theorem, these critical cells give homotopy-equivalent CW complexes, but their integer attaching degrees must still be calculated where adjacent critical dimensions occur.

**3. Integral Morse differentials.** For a matched lower simplex \(\tau\) and upper simplex \(\mu\), the incidence \([\mu:\tau]\) is \(\pm1\). In the chain contraction, replace \(\tau\) by
\[
-[\mu:\tau]^{-1}\sum_{\rho\neq\tau}[\mu:\rho]\,\rho,
\]
where the sum ranges over the other codimension-one faces of \(\mu\). Recurse until only critical faces remain. The verified acyclic matching ensures this terminates. Independently, the checker verifies the resulting projection is a chain map on **every** simplex of every stage, and checks mod-two simplicial boundary ranks without using the matching.

For \(d=2\), the entire signed integral Morse differential from degree seven to six is zero. For \(d=3\), critical six-face masks are \(926,3506,3762,3890\), critical seven-face masks are \(1782,3828\), and the complete degree-seven boundary, in those orders, is
\[
\partial_7=\begin{pmatrix}0&0\\0&0\\0&1\\0&0\end{pmatrix}.
\]
All other positive-degree Morse boundaries vanish. The unique nonzero entry is a genuine integer unit, not merely a nonzero residue modulo a prime.

**4. Homotopy deduction.** The first two Morse complexes consist only of a vertex and same-dimensional positive cells, hence are the claimed sphere wedges. At \(d=2\), the six-skeleton is a wedge of four six-spheres. The zero degree vector of the seven-cell attaching map implies the map is nullhomotopic, since the Hurewicz map \(\pi_6(\bigvee^4 S^6)\to H_6(\bigvee^4 S^6;\mathbb Z)\) is an isomorphism. At \(d=3\), a unit-degree seven-cell kills one six-cell; changing the integral basis of the six-spheres and cancelling this pair leaves three six-spheres and a seven-cell with zero attaching degree. The same Hurewicz argument splits the last seven-cell as a seven-sphere. These are **integral homotopy** equivalences, not conclusions drawn solely from finite-field Betti numbers.

**5. Actual integral inclusion maps.** The checker constructs full simplicial integer cycles lifting each positive-degree Morse generator at \(d=2\), verifies their boundaries vanish, and checks that the \(d=2\) projection sends each lift to its claimed unit basis vector. Applying the \(d=3\) projection to these same chains gives
\[
\begin{array}{c|ccccc}
\text{source mask}&926&3308&3506&3762&1782\\\hline
\text{target critical chain}&926&0&3506&3762&1782.
\end{array}
\]
In the \(d=3\) Morse complex, mask \(3762\) is the boundary of critical seven-mask \(3828\). Thus a basis of \(\widetilde H_6(\mathcal F_3;\mathbb Z)\) is represented by critical masks \(926,3506,3890\), and in suitable integral bases the degree-six inclusion has matrix
\[
\begin{pmatrix}1&0&0&0\\0&0&1&0\\0&0&0&0\end{pmatrix}.
\]
It has rank two, **primitive** image and free cokernel; no degree-six torsion appears in the module or its quotient. In degree seven, mask \(1782\) maps to itself and generates the target kernel of \(\partial_7\), giving an integral isomorphism. All other inclusion maps between nonzero reduced homology groups are zero for dimensional reasons. These split integral matrices establish the displayed persistence intervals.

## Verification

Run `python3 verify.py` using Python 3 and no third-party packages. `verification_output.txt` records the exact expected stdout, ending with `FRUCHT_FOREST_FILTRATION_INTEGRAL_CERTIFICATE_PASS`. The computation checks both union-find and depth-first cycle predicates, all faces, all Morse incidence orientations, every projected chain identity, simplicial mod-two ranks, integral boundary coefficients, and explicit inclusion-induced chain representatives. The recorded output is data, not a substitute for rerunning the program or assessing the proof.

## Relationship to prior work

Taylan's publicly posted 2015 treatment of devoid complexes supplies the general simplicial framework for forbidding induced graph configurations; its explicit homotopy calculations address paths, cycles and selected forests rather than these four stages of the Frucht graph. The later forest-filtration framework of Carnero Bravo provides the exact natural filtration and classifies paths, cycles, double stars, cactus graphs and specified graph operations, but its inspected classification does not compute this three-connected cubic Halin graph. Existing Frucht-graph independence-complex results already imply the \(d=0\) homotopy type, which is included only to state the full sequence. The new content is the integral topological classification for \(d=1,2,3\) and the degree-six and degree-seven inclusion maps. Independence, Rips and matching complexes of the same graph are different simplicial constructions; their homotopy groups do not determine these maps.

## Limitations

The theorem concerns one explicitly specified twelve-vertex graph, not an infinite family of asymmetric cubic graphs. The homotopy equivalences are **nonequivariant**, and there is no claim about automorphism representations, triangulated homeomorphism types, canonical filtrations at real parameters, or stability under graph modifications. Scientific originality is assessed against inspected and indexed evidence; priority relative to unindexed work is not conclusively settled. The finite checker is exhaustive for this graph, but no formal proof assistant or independent mathematical audit is asserted.

## References

1. D. Taylan, *Matching Trees for Simplicial Complexes and Homotopy Type of Devoid Complexes of Graphs*, arXiv:1501.06754v1, first publicly submitted 2015-01-27. https://arxiv.org/abs/1501.06754
2. A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, first publicly submitted 2023-07-25. https://arxiv.org/abs/2307.13271
3. R. Frucht, *Graphs of degree three with a given abstract group*, Canadian Journal of Mathematics 1 (1949), 365–378. DOI:10.4153/CJM-1949-033-6.
4. E. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. DOI:10.1006/aima.1997.1650.
5. Previously published Frucht independence-complex calculation, searchable mathematical record: https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-frucht-graph-independence-complex-and-its-complete-vertex-de--8b7d9b2243c2 (independence-only result).
