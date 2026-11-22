# Even-cardinality circular arcs: a missing-triple law and a two-sphere shattering complex

## Finding
Let \(n\ge4\) be even, and label the vertices of a simple cycle \(C_n\) by \(\mathbb Z/n\mathbb Z\). Let \(\mathcal E_n\) consist of the empty vertex set, the whole vertex set, and every nonempty proper cyclic interval of **even cardinality**. An interval is a block of consecutive vertices in the cyclic order; its length is its number of vertices. For a query support \(S\), its trace family is \(\{S\cap A:A\in\mathcal E_n\}\). Let \(\Delta_n\) be the simplicial complex of all supports on which every binary trace occurs.

**Exact supports.** Every support of size at most two is shattered. A three-element support is shattered exactly when its vertices are **not** three consecutive vertices of \(C_n\). No support of size four or more is shattered. Consequently,
\[
\boxed{\Phi_n(z)=1+nz+\binom n2z^2+\left(\binom n3-n\right)z^3.}
\]
At \(n=4\), the cubic coefficient is zero and the VC dimension is two; at every even \(n\ge6\), the VC dimension is three.

**Integral topology.** At \(n=4\), \(|\Delta_4|\simeq\bigvee^3 S^1\). For every even \(n\ge6\),
\[
\boxed{|\Delta_n|\simeq\bigvee^{\binom{n-1}{3}-n}S^2.}
\]
In particular, \(\widetilde H_1(\Delta_n;\mathbb Z)=0\), \(\widetilde H_2(\Delta_n;\mathbb Z)\cong\mathbb Z^{\binom{n-1}{3}-n}\), and every integral homology group is torsion-free. Relative to unrestricted circular intervals, which shatter every triple, the even-cardinality restriction removes precisely \(n\) triangular faces and, for \(n\ge6\), precisely \(n\) independent top-dimensional sphere generators without creating first homology.

## Assumptions and scope
The cycle is finite, simple, unweighted and has even order \(n\ge4\). The hypotheses are all even-cardinality cyclic intervals **including the empty and full sets**; they are not graph balls (proper graph balls on an even cycle have odd cardinality), nor shortest paths or geodesically convex sets. Queries ask vertex membership, not edge membership. The complex \(\Delta_n\) has one vertex for each cycle vertex and downward-closed faces given by ordinary VC shattering. A wedge with \(r\) copies means the pointed wedge of \(r\) ordinary spheres.

## Proof
**1. One and two queries.** The empty interval realizes the empty trace. On any selected vertex, a length-two interval containing it realizes the positive trace. For distinct vertices \(u,v\), the whole cycle realizes the trace \(\{u,v\}\), and there is for each one of \(u,v\) an adjacent vertex outside \(\{u,v\}\), because every vertex has two distinct neighbors and only one other selected vertex is excluded. A length-two interval through that neighbor realizes the corresponding singleton trace. Thus every pair is shattered.

**2. Three-query obstruction.** If \(S=\{i,i+1,i+2\}\) (indices modulo \(n\)), the trace containing only the middle point \(i+1\) is impossible: any nonempty even-length contiguous interval containing that vertex must contain at least one of its two immediate neighbors, while the empty interval contains no points. Therefore no cyclically consecutive triple is shattered.

**3. All other triples are shattered.** Let \(S=\{a,b,c\}\) be nonconsecutive. The empty and all-positive traces are supplied by the empty and full hypotheses. For any \(x\in S\), at least one of its two cycle neighbors is outside \(S\), or \(S\) would be a consecutive triple with middle \(x\); a length-two interval through \(x\) and that neighbor realizes \(\{x\}\). To realize the two-positive trace \(\{a,b\}\) excluding \(c\), take the unique cyclic arc from \(a\) to \(b\) whose interior avoids \(c\). If its length is even, it is already a hypothesis. If its length is odd, at least one endpoint can be extended by one vertex toward \(c\) without reaching \(c\), since otherwise \(c\) would be adjacent to both endpoints and \(S\) would be consecutive. The extended arc has even length, contains \(a,b\), and still avoids \(c\). The same works for the other two pairs. Hence all eight traces occur.

**4. Four-query obstruction and enumeration.** Four queried vertices in cyclic order cannot realize the alternating trace selecting the first and third but excluding the second and fourth with any contiguous arc. The full-cycle hypothesis also cannot realize it. Therefore no four-point set is shattered, and hereditary shattering excludes all larger sets. For \(n\ge4\), the cyclically consecutive unordered triples \(\{i,i+1,i+2\}\) are \(n\) distinct triples, so there are \(\binom n3-n\) shattered triples. This proves the polynomial.

**5. Homotopy at \(n=4\).** There are no triangular faces; \(\Delta_4\) is the one-dimensional complete graph \(K_4\). A connected graph of four vertices and six edges is a wedge of three circles.

**6. Simple connectivity at \(n\ge6\).** The two-skeleton of the full simplex on \(n\) vertices has trivial fundamental group. Our complex has the identical one-skeleton and every triangular face except the \(n\) consecutive triples. For each omitted triangle \(T_i=\{i,i+1,i+2\}\), set \(v=i+4\pmod n\). Because \(n\ge6\), the three triangles \(\{i,i+1,v\}\), \(\{i+1,i+2,v\}\), and \(\{i,i+2,v\}\) are all nonconsecutive and hence belong to \(\Delta_n\). Their union is a disk filling the boundary of \(T_i\). Thus the missing triangle's attaching loop is null-homotopic already in \(\Delta_n\). Attaching all omitted triangles would give the simply connected full two-skeleton without changing the fundamental group. Hence \(\pi_1(\Delta_n)=0\).

**7. Integral homology and homotopy.** Since \(\Delta_n\) is a connected, simply connected two-dimensional simplicial complex, \(H_1(\Delta_n;\mathbb Z)=0\). Its second homology is a subgroup of a free abelian two-chain group, so it is free abelian. The numbers of simplices in dimensions zero, one and two are \(n\), \(\binom n2\), \(\binom n3-n\), respectively. The reduced Euler characteristic is
\[
\widetilde\chi(\Delta_n)=n-\binom n2+\binom n3-n-1=\binom{n-1}{3}-n.
\]
Therefore \(H_2(\Delta_n;\mathbb Z)\) has rank \(\binom{n-1}{3}-n\). The Hurewicz theorem gives spherical representatives for a basis of this group. The wedge of those two-sphere maps induces an isomorphism on every integral homology group between simply connected CW complexes and hence is a homotopy equivalence by the homological Whitehead theorem. This proves the stated integral homotopy type.

## Verification
Two separate implementations construct all even-length circular-arc hypotheses and compare the actual trace families on every support of sizes zero through four with the consecutive-triple rule. The Python implementation does so at even orders \(4,6,\ldots,18\), and the independent C++17 implementation at even orders \(4,6,\ldots,20\). Python additionally forms the simplicial triangle-edge incidence boundary matrix and computes its exact binary rank for even orders through \(14\), confirming the predicted mod-two Betti numbers. Use `python3 proof/check_even_arcs.py` and `g++ -O2 -std=c++17 proof/check_even_arcs.cpp -o check_even_arcs && ./check_even_arcs`. Outputs are embedded as `proof/python_results.txt` and `proof/cpp_results.txt`. Such finite checks are corroboration, not a substitute for the all-order proof or integral homotopy argument.

## Relationship to prior work
Chalopin, Chepoi, Mc Inerney, Ratel and Vaxès, *Sample compression schemes for balls in graphs*, arXiv:2206.13254 (first made public 2022-06-27), Section 4, Proposition 10, study graph balls on cycles and establish a size-three compression scheme. On **even** cycles, every non-universal ball is an **odd-cardinality** arc, so that hypothesis class is not the even-cardinality class here. The published *Radius-filtered graph balls on cycles: exact shattering polynomials and a two-phase density law* (published-finding corpus record `2026/11/8/...da8d9213216f`) computes exact ball-family shattering counts; its diameter-radius case shatters **every** triple in even order, unlike the present class, where exactly \(n\) triples fail. Its odd-order case is equivalent under concept complementation to even-length arcs on **odd** cycles, which is why the present theorem expressly restricts to even orders. The published *Parity classification and topology of geodesic shattering on finite cycles* (published-finding corpus record `2026/11/8/...eeb9c033ac3d`) restricts to shortest paths and allows only triples with antipodal pairs at even order, yielding a different complex and different homotopy ranks. Standard unrestricted circular intervals shatter all triples and give the full two-skeleton; their VC bound alone does not supply the missing-face or integral homotopy theorem here.

## Limitations
This statement is confined to even unweighted cycle orders, all even-cardinality circular intervals, and ordinary vertex-membership queries. It does not determine adaptive/Littlestone dimension, sample compression size, weighted-cycle analogues, or parity-constrained arcs on arbitrary graphs. The odd-order analogue is excluded because its shattering support count is already covered via complements of cycle balls. The literature search cannot rule out every unindexed equivalent formulation; the same-object published results inspected above do not imply the even-order homotopy classification. Finite verification does not constitute independent mathematical validation.

## References
1. J. Chalopin, V. Chepoi, F. Mc Inerney, S. Ratel, Y. Vaxès, *Sample compression schemes for balls in graphs*, arXiv:2206.13254, first submitted 2022-06-27, especially Section 4 and Proposition 10. https://arxiv.org/abs/2206.13254
2. *Radius-filtered graph balls on cycles: exact shattering polynomials and a two-phase density law*, publicly accessible mathematical result, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-radius-filtered-graph-balls-on-cycles-exact-shattering-polynomia--da8d9213216f
3. *Parity classification and topology of geodesic shattering on finite cycles*, publicly accessible mathematical result, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-parity-classification-and-topology-of-geodesic-shattering-on-fin--eeb9c033ac3d
