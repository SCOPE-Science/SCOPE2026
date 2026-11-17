# Full automorphism homology of the Möbius–Kantor independence complex

## Finding
Let \(M=G(8,3)\) be the sixteen-vertex Möbius–Kantor graph and let \(X=\operatorname{Ind}(M)\) be its ordinary simplicial independence complex. Write \(G=\operatorname{Aut}(M)\), which has order \(96\). For the two independent linear characters \(\lambda,\mu:G\to\{\pm1\}\) defined below, the **complete rational homology representations** are
\[
\widetilde H_3(X;\mathbb Q)\cong\lambda\oplus V_3,
\qquad\widetilde H_4(X;\mathbb Q)\cong\mu,
\]
where \(V_3\) is an absolutely irreducible three-dimensional rational representation. No other reduced rational homology occurs. The character of \(V_3\) on every conjugacy class is specified in the table below.

The character \(\mu\) is exactly the sign of the induced permutation of the two graph-bipartition classes. The character \(\lambda\) is the distinct linear character taking \(\lambda(r)=1\) and \(\lambda(a)=-1\) on the two displayed generators. Consequently, for the ordinary topological quotients, as graded rational cohomology rings,
\[
H^*(|X|/G;\mathbb Q)\cong\mathbb Q,\qquad
H^*(|X|/\ker\lambda;\mathbb Q)\cong H^*(S^3;\mathbb Q),\qquad
H^*(|X|/\ker\mu;\mathbb Q)\cong H^*(S^4;\mathbb Q).
\]
Thus two distinct natural normal subgroups of index two retain homology in **different degrees**, while all positive rational homology disappears under the full group.

## Assumptions and scope
Number vertices \(0,\ldots,7\) by \(u_i=i\) and \(8,\ldots,15\) by \(v_i=8+i\), with indices modulo eight. Edges of \(M\) are \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\). A simplex of \(X\) is a subset of vertices containing no edge of \(M\), oriented in increasing vertex order. All homology, representations and quotient cohomology in this result have \(\mathbb Q\)-coefficients unless explicitly stated otherwise.

Define \(r(u_i)=u_{i+1}\) and \(r(v_i)=v_{i+1}\), and the graph automorphism \(a\) by its array of images of vertices \(0,\ldots,15\):

`(0,8,11,3,4,12,15,7,1,13,14,2,5,9,10,6)`.

The permutations \(r,a\) generate all \(96\) automorphisms. Define \(\lambda(r)=+1,\lambda(a)=-1\). These prescriptions extend consistently to a group homomorphism, as verified on all \(96^2\) pairs of elements. Let \(\mu(g)\) be \(+1\) if \(g\) preserves both parts of the unique graph bipartition, and \(-1\) if it interchanges them. In particular \(\mu(r)=-1\) and \(\mu(a)=+1\). Thus the two characters and their kernels are different.

With \(R=r^{-1}\), \(A=a^{-1}\), juxtaposition denoting composition (the right factor acts first), the following **complete** class table specifies every trace. \(\chi_3\) and \(\chi_4\) are the degree-three and degree-four homology characters, while \(\chi_{V_3}=\chi_3-\lambda\).

| Class size | Representative word | \(\chi_3\) | \(\chi_4=\mu\) | \(\lambda\) | \(\chi_{V_3}\) |
|---:|:---:|---:|---:|---:|---:|
|1|e|4|1|1|3|
|1|rrrr|4|1|1|3|
|2|ararar|-4|-1|-1|-3|
|6|RR|0|1|1|-1|
|6|RaRara|0|-1|-1|1|
|8|Ra|-1|-1|-1|0|
|8|RRRa|-1|-1|-1|0|
|8|RaRa|1|1|1|0|
|8|Rara|1|1|1|0|
|12|R|0|-1|1|-1|
|12|a|-2|1|-1|-1|
|12|RRa|0|1|-1|1|
|12|RRaRa|2|-1|1|1|

## Proof
**Finite chain complex.** The graph contains 24 edges. Exhaustive generation by adjoining vertices in increasing order when no existing vertex is adjacent produces exactly 1,090 nonempty faces, by dimensions \(0,\ldots,7\) in counts \((16,96,272,376,240,72,16,2)\). The boundary of an increasing simplex \([w_0,\ldots,w_d]\) is \(\sum_{j=0}^{d}(-1)^j[w_0,\ldots,\widehat{w_j},\ldots,w_d]\). Exact sparse rational elimination gives boundary ranks \((15,81,191,181,58,14,2)\) in degrees one through seven, giving reduced Betti numbers \(\widetilde b_3=4,\widetilde b_4=1\) and zeros elsewhere. The homotopy type \(\bigvee^4S^3\vee S^4\) is also established independently by Bıyıkoğlu and Civan, Example 3.9 [1]; that nonequivariant statement is **not** a new claim here.

**All automorphisms and their traces.** Exhaustive graph-isomorphism enumeration produces precisely 96 automorphisms; the two displayed generators reach all 96 by composition. Every automorphism is verified to commute with each simplicial boundary map, including orientation signs. For every \(g\in G\), the signed simplicial Lefschetz trace
\[
L(g)=\sum_{d=0}^{7}(-1)^d\!
\sum_{\substack{\sigma\in X_d\\g\sigma=\sigma}}
\operatorname{sgn}(g|_\sigma)
\]
is computed directly on the 1,090 faces. Because the only nonzero ordinary homology is in degrees zero, three and four,
\[
L(g)=1-\chi_3(g)+\chi_4(g).
\]

**Determining the top character.** As \(\dim_{\mathbb Q}H_4(X;\mathbb Q)=1\), each automorphism acts on that line by \(\pm1\). Independently over \(\mathbb F_{101}\) and \(\mathbb F_{103}\), the complete simplicial boundary ranks agree with the exact rational ranks. A nonzero homology cycle in degree four is constructed as a linear dependency among boundary columns and tested modulo the complete image of the boundary in degree five. Its transported class is compared with the positive and negative of that generator under **every** one of the 96 automorphisms. Both prime computations agree and give precisely \(\chi_4(g)=\mu(g)\), the sign of the graph bipartition permutation. Since the modular degree-four homology is one-dimensional and the rational and modular boundary ranks agree, the modular action detects the rational one-dimensional sign without ambiguity.

**Irreducible decomposition.** The Lefschetz identity now gives \(\chi_3=1+\mu-L\) at every group element, and the table follows by conjugacy. The linear character \(\lambda\) is verified as above, and exact character inner products give
\[
\langle\chi_3,\lambda\rangle_G=1,\qquad
\langle\chi_3,\chi_3\rangle_G=2,\qquad
\langle\chi_3-\lambda,\chi_3-\lambda\rangle_G=1.
\]
Thus \(\lambda\) appears exactly once and the complementary rational character of dimension three is absolutely irreducible; this is \(V_3\). The rank-one module in degree four is \(\mu\).

**Ordinary quotients.** For a finite simplicial group action, after barycentric subdivision the rational cellular chains of the ordinary quotient are the coinvariants of the subdivided complex; averaging over a finite group identifies their homology with rational invariant homology. The table and character orthogonality yield dimensions of invariants in degrees three and four equal to \((0,0)\) for \(G\), \((1,0)\) for \(\ker\lambda\), and \((0,1)\) for \(\ker\mu\). No other positive-degree rational homology is present. A graded rational cohomology ring with just one positive generator in degree three or four has all positive-degree products zero, yielding the displayed ring isomorphisms.

## Verification
Run `python verify_mobius_kantor.py` with Python 3, NetworkX and SymPy installed. The independent exact checks include the complete graph and simplicial complex, \(\partial^2=0\), all rational boundary ranks, full graph automorphism enumeration, the two-generator group and linear-character consistency, signed chain equivariance for all automorphisms, two modular top-homology actions, the complete thirteen-class table, character inner products, and invariant-homology dimensions for three group quotients. `verification_output.txt` contains the recorded deterministic output. Success terminates with `COMPLETE_MOBIUS_KANTOR_AUTOMORPHISM_CHARACTER_PASS`.

## Relationship to prior work
Bıyıkoğlu and Civan [1] determine the **nonequivariant** homotopy type of exactly this independence complex (and its regularity). Their Example 3.9 does not calculate the action of all graph automorphisms, irreducible homology constituents, or the rational cohomology of the ordinary quotients. A separate published computation [2] treats only the rotation subgroup \(C_8\). Its restricted characters \((4,0,0,0,4,0,0,0)\) and \((1,-1,1,-1,1,-1,1,-1)\) agree with this result when restricted to \(C_8\), but they **cannot determine the thirteen-class character** of the full 96-element group or distinguish the two index-two kernels. In particular, merely knowing the ordinary Betti numbers and an eight-element subgroup restriction does not imply the new conclusion. Knill [3] investigates graph symmetries and Lefschetz numbers on a different graph-topological object; the complete article was not obtainable in this check, so its potential overlap is a residual priority risk rather than a claim of full-text noncoverage. Other literature on Möbius **ladders** concerns nonisomorphic graphs and does not automatically imply these representations.

## Limitations
This determines rational homology representations and ordinary quotient rational cohomology rings, **not** integral homology-module structures, integral quotient homology, quotient homotopy type, or Borel equivariant cohomology. The finite modular calculations are exact finite checks, not a proof of similar statements for larger generalized Petersen graphs. The 2015 nonequivariant homotopy theorem and previously published cyclic restriction are prior work. Searches cannot establish absolute publication novelty; relevant unindexed work and the uninspected complete text of [3] remain priority risks. Independent mathematical verification has not been performed.

## References
1. T. Bıyıkoğlu and Y. Civan, *Castelnuovo-Mumford regularity of graphs*, arXiv:1503.06018v1, first publicly posted 2015-03-20, Example 3.9, https://arxiv.org/pdf/1503.06018.
2. *Cyclic symmetry on Möbius–Kantor independence homology*, public research record (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-cyclic-symmetry-on-m-bius-kantor-independence-homology--1c198fd64c4e.
3. O. Knill, *Remarks about the Moebius-Kantor graph*, arXiv:2605.30799v1, first publicly posted 2026-05-29, https://arxiv.org/abs/2605.30799 (abstract inspected; full text not obtained).
4. E. W. Weisstein, *Möbius–Kantor Graph*, MathWorld, https://mathworld.wolfram.com/Moebius-KantorGraph.html.
