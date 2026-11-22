# Point-image shattering of finite general linear groups

## Finding
Let \(q\) be a prime power, \(d\ge2\), \(V=\mathbb F_q^d\), and \(V^*=V\setminus\{0\}\). Regard the graphs of invertible linear maps
\[\Gamma_A=\{(v,Av):v\in V^*\}\qquad(A\in\operatorname{GL}(V))\]
as a family of binary concepts on the coordinate set \(X=V^*\times V^*\). For a finite \(S\subseteq X\), shattering means that for every \(P\subseteq S\) there is an invertible linear map \(A\) with \(S\cap\Gamma_A=P\).

**Theorem.** Write \(S=\{(v_1,w_1),\ldots,(v_k,w_k)\}\) without repetitions. Then \(S\) is shattered if and only if both \((v_1,\ldots,v_k)\) and \((w_1,\ldots,w_k)\) are linearly independent. In particular,
\[\boxed{\Phi_{q,d}(z)=\sum_{k=0}^d\frac{z^k}{k!}\prod_{i=0}^{k-1}(q^d-q^i)^2},\qquad\operatorname{VCdim}=d.\]
The empty product equals one. The shattered-support complex is pure of dimension \(d-1\), equals the intersection of two representable matroid independence complexes, and is not itself a matroid.

For \((q,d)=(2,2)\), \(\Phi_{2,2}(z)=1+9z+18z^2\) and \(\widetilde\beta_1=10\). For \((q,d)=(2,3)\),
\[\Phi_{2,3}(z)=1+49z+882z^2+4704z^3,\qquad(\widetilde\beta_0,\widetilde\beta_1,\widetilde\beta_2)=(0,0,3870)\quad\text{over }\mathbb F_2.\]

## Assumptions and scope
The field is arbitrary of prime-power order, including nonprime fields. The group consists of **all** invertible linear maps on \(V\); translations and semilinear field automorphisms are excluded. Coordinates are ordered source-target pairs of **nonzero vectors**, not projective points, matrix entries, or equality comparisons between two unknown maps. No restriction is imposed on \(A\) besides invertibility. Every assertion about the homology rank \(3870\) refers specifically to \((q,d)=(2,3)\), with coefficients in \(\mathbb F_2\); it is not claimed as an all-dimensional topological formula.

## Proof
**1. Necessary independence.** If \(S\) is shattered, the all-positive labeling is realized by an invertible linear map \(A\). Thus the assignments \(v_i\mapsto w_i\) respect every linear dependency. Suppose the source vectors are dependent. Choose a minimal dependent subfamily \(v_{i_1},\ldots,v_{i_s}\), with each coefficient in its unique dependence nonzero. With the first \(s-1\) prescribed assignments kept positive, linearity forces the last image to be \(w_{i_s}\), because the all-positive map already realizes every assignment in the circuit. The trace with these \(s-1\) queries positive and the last query negative is therefore impossible. Thus the sources must be independent. Invertibility of the all-positive map then forces their images to be independent too.

**2. All sign patterns extend when both sides are independent.** Fix \(S\) with independent source and target families of common size \(k\le d\). Let \(P\subseteq S\) be the queries required positive, of size \(p\). The \(p\) positive vector assignments define a linear isomorphism between their spans, so they extend to elements of \(\operatorname{GL}(V)\). Choose such an extension uniformly. For each \((v,w)\in S\setminus P\), the vector \(v\) lies outside the span of positive source vectors and \(w\) lies outside the span of positive target vectors. Conditional on the \(p\) assignments, \(Av\) is uniform among exactly \(q^d-q^p\) vectors outside the positive target span. Consequently
\[\Pr(Av=w\mid P\text{ positive})=\frac1{q^d-q^p}.\]
The union bound shows that the probability of accidentally realizing at least one of the \(k-p\) forbidden assignments is at most
\[\frac{k-p}{q^d-q^p}\le\frac{d-p}{2^d-2^p}<1\qquad(p<k\le d,\ d\ge2).\]
The strict final inequality follows, for example, from \(2^d-2^p\ge d-p+1\), valid for \(d\ge2\) and \(0\le p<d\). Therefore some invertible extension avoids every negative query. When \(p=k\), every extension already has the required trace. All \(2^k\) traces exist.

**3. Enumeration, purity, and the failure of matroid exchange.** The number of ordered independent \(k\)-tuples in \(V\) is \(N_{q,d,k}=\prod_{i=0}^{k-1}(q^d-q^i)\). Choose the ordered source and target tuples independently and divide by \(k!\), since ordering the \(k\) distinct query pairs does not change their support. This gives the polynomial. Both independent families extend to vector-space bases and a bijection of the enlarged bases, so each face extends to a size-\(d\) face; hence purity.

On the ground set \(X\), form two vector matroids by representing a query \((v,w)\) by \(v\) on the source side and by \(w\) on the target side. The theorem identifies the complex with the intersection of their independent-set systems. It is not a matroid: take independent \(v_1,v_2\) and independent \(w_1,w_2\). The singleton queries \(e=(v_1,w_1)\), \(f=(v_1,w_2)\), and \(g=(v_2,w_2)\) are all nonloops; \(\{e,f\}\) and \(\{f,g\}\) are dependent pairs whereas \(\{e,g\}\) is independent. Parallelism of nonloops would be transitive in a matroid, a contradiction.

**4. The binary rank-three homology calculation.** In \(V=\mathbb F_2^3\) there are seven nonzero vectors. The independent-pair counts give 49 vertices, 882 edges, and 4704 triangles. The one-skeleton is connected: any two vertices can be linked through a query using a third source vector and a third target vector distinct from both endpoints. Thus the reduced \(\mathbb F_2\)-boundary rank in degree one is \(49-1=48\). The exact binary elimination of the triangle-to-edge boundary matrix gives \(\operatorname{rank}(\partial_2)=834\). The included standalone checker constructs every row and column from vector-pair incidences, forms the 4704 triangle boundaries as bitsets over the 882 edge basis vectors, and performs exact Gaussian elimination, with no randomization or floating-point steps. Consequently \(\widetilde\beta_1=882-48-834=0\) and \(\widetilde\beta_2=4704-834=3870\). All other reduced Betti numbers vanish by connectedness and dimension. For \((q,d)=(2,2)\) the complex is a connected graph with nine vertices and 18 edges, hence first Betti number \(18-9+1=10\).

## Verification
Three standalone reproducibility sources accompany this result. The C++17 program `verify_gl3.cpp` enumerates all 168 elements of \(\operatorname{GL}_3(2)\) as independent ordered bases and exhaustively tests all \(49\), \(1176\), and \(18424\) supports of sizes one, two, and three, obtaining respectively \(49\), \(882\), and \(4704\) shattered supports. Higher sizes are excluded by the general proof, not by computational extrapolation. The Python program `verify_gl3_homology.py` independently generates all faces using binary rank calculations and computes boundary rank 834. The second Python program `verify_gl2_ternary.py` enumerates all 48 invertible ternary \(2\times2\) matrices, checks every singleton and every pair among 64 possible image queries, and finds \(1+64z+1152z^2\).

Reproduction with Python 3 and a C++17 compiler:
```
g++ -O2 -std=c++17 verify_gl3.cpp -o verify_gl3
./verify_gl3
python3 verify_gl3_homology.py
python3 verify_gl2_ternary.py
```
These finite checks corroborate the field-uniform proof; they do not independently prove assertions for every prime power or dimension.

## Relationship to prior work
Hu, Weinberger and Shayevitz (public 2017) address the VC dimension of binary codes and constrained asymptotic rates, not the graph-incidence family of full general linear groups. Fitzpatrick, Iosevich, McDonald and Wyman (2021) address radius-sphere incidence learning in finite-field planes; their hypotheses are spheres indexed by centers, not graphs of linear automorphisms. Arora and Ram (public 2020) enumerate partial linear transformations by similarity invariants; specifying a partial map is related to our all-positive traces, but similarity-class enumeration neither enforces every possible signed trace nor gives the stated shattering complex. Kobayashi, Kurita and Wasa (2023) provide algorithms for enumerating common independent sets of two matroids, but do not identify the \(\operatorname{GL}(V)\) shattering complex or its face coefficients. These distinctions are about mathematical implications, not just terminology.

## Limitations
No Littlestone-dimension formula, general homotopy type, or homology outside the two stated binary examples is established. The nonmatroidality assertion does not exclude other combinatorial structures or generalized exchange axioms. The topology calculation establishes Betti numbers over \(\mathbb F_2\), not integral torsion or wedge decomposition. The literature search does not certify global historical priority; a previously unindexed equivalent automorphism-incidence result would supersede the originality claim.

## References
1. S. Hu, N. Weinberger, O. Shayevitz, *On the VC-Dimension of Binary Codes*, arXiv:1703.01586 (first public 2017-03-05), https://arxiv.org/abs/1703.01586.
2. A. Arora, S. Ram, *Enumerating Partial Linear Transformations in a Similarity Class*, arXiv:2005.06222 (first public 2020-05-13), https://arxiv.org/abs/2005.06222.
3. D. Fitzpatrick, A. Iosevich, B. McDonald, E. L. Wyman, *The VC-dimension and Point Configurations in Finite Fields*, arXiv:2108.13231 (first public 2021-08-30), https://arxiv.org/abs/2108.13231.
4. Y. Kobayashi, K. Kurita, K. Wasa, *Polynomial-Delay Enumeration of Large Maximal Common Independent Sets in Two Matroids and Beyond*, arXiv:2307.08948 (first public 2023-07-18), https://arxiv.org/abs/2307.08948.
