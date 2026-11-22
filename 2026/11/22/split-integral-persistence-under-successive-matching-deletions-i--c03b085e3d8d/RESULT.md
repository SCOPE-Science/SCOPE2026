# Split integral persistence under successive matching deletions in bipartite dissociation complexes

## Finding

Fix integers \(a,b\ge3\), put \(T=\min(a,b)\), and write the vertex classes of a complete bipartite graph as \(A=\{a_1,\ldots,a_a\}\) and \(B=\{b_1,\ldots,b_b\}\). Delete the matching edges in order:

\[
G_t=K_{a,b}\setminus\{a_ib_i:1\le i\le t\},\qquad 0\le t\le T.
\]

Let \(X_t=\operatorname{Ind}_2(G_t)\) be the simplicial complex of vertex subsets whose induced graph has maximum degree at most one. Then \(X_0\subseteq X_1\subseteq\cdots\subseteq X_T\). The **new conclusion concerns every inclusion map**, rather than only the homotopy type of an individual stage.

**Theorem (complete integral persistence).** In reduced integral homology, the natural degree-one maps \(\widetilde H_1(X_t;\mathbb Z)\to\widetilde H_1(X_{t+1};\mathbb Z)\) are split surjections, and the natural degree-two maps \(\widetilde H_2(X_t;\mathbb Z)\to\widetilde H_2(X_{t+1};\mathbb Z)\) are primitive split injections. Every group is free abelian. Equivalently, extending the filtration constantly beyond \(T\), the complete reduced **integral interval decomposition** is

\[
\begin{aligned}
\widetilde H_1 &: (a+b-2)\,[0,1)\;\oplus\!
 \bigoplus_{s=2}^{T}(a+b-2s+1)\,[0,s),\\
\widetilde H_2 &: \bigoplus_{s=3}^{T}(s-2)\,[s,\infty),
\end{aligned}
\]

with no other reduced homology intervals. Coefficients such as \(m\,[r,s)\) mean \(m\) copies of the integral interval module supported at the listed filtration indices. The known ranks, recalled for interpretation but **not asserted as new**, are

\[
\begin{aligned}
\operatorname{rank}\widetilde H_1(X_0)&=ab-1,\\
\operatorname{rank}\widetilde H_1(X_t)&=(a-t)(b-t)\quad(t\ge1),\\
\operatorname{rank}\widetilde H_2(X_t)&=\binom{t-1}{2}\quad(t\ge1).
\end{aligned}
\]

More precisely, for \(t\ge1\) the second homology is canonically represented (after the explicit cell identifications below) by the integral cycle lattice of the graph \(K_t\) on deleted-matching labels. Fundamental cycles of \(K_t\) based at label \(1\) form a nested, compatible integral basis: the classes indexed by \(2\le i<j\le t\) remain unchanged at every subsequent stage, while the new classes at stage \(s\) are exactly those indexed by \((i,s)\) with \(2\le i<s\).

For example, when \((a,b)=(4,5)\), the nonzero degree-one death multiplicities at stages \(1,2,3,4\) are respectively \(7,6,4,2\); one degree-two class is born at stage \(3\), and two more are born at stage \(4\). This records the complete homology maps, not only the stagewise Betti numbers.

## Assumptions and scope

All graphs are finite, undirected, simple and labeled. The forbidden edges form the prescribed initial segment of one fixed matching; arbitrary or intersecting edge faults are not included. A dissociation set is one with maximum induced degree at most one, equivalently a set inducing components of order at most two. All homology is over \(\mathbb Z\) unless another coefficient is specified. By an integral barcode we mean an isomorphism of diagrams of free abelian groups into direct sums of the indicated interval diagrams; such decompositions are established here from compatible primitive maps, not inferred from ranks alone. When \(T=3\), the degree-two barcode has only one essential class; empty sums are understood as zero. Since each \(X_t\) is nonempty and connected, reduced degree zero vanishes throughout.

## Proof

**1. One fixed relative chain model.** For all \(t\), both full simplices \(\Delta_A\) and \(\Delta_B\) belong to \(X_t\). Let \(Y=\Delta_A\sqcup\Delta_B\), a fixed two-component subcomplex. Every cross edge \(e_{ij}=\{a_i,b_j\}\) is a face. Every mixed triangle contains a unique deleted matching pair and has precisely one of the forms

\[
L_{si}=\{a_s,a_i,b_s\}\;(s\le t,\ i\ne s),\qquad
R_{sj}=\{a_s,b_s,b_j\}\;(s\le t,\ j\ne s).
\]

Every mixed tetrahedron is exactly \(F_{ij}=\{a_i,a_j,b_i,b_j\}\) for \(1\le i<j\le t\); there are no mixed faces of size five or greater. Indeed, in a mixed face of \(r\) vertices from \(A\) and \(s\) from \(B\), each vertex has at most one missing cross-neighbor, so induced degree at most one forces \(r,s\le2\). The listed cases exhaust the resulting possibilities. Hence the relative cellular chain groups \(C_\bullet(X_t,Y)\), embedded compatibly for increasing \(t\), consist of

\[
C_1=\mathbb Z\langle e_{ij}\rangle\ (ab\ \mathrm{generators}),\qquad
C_2=\mathbb Z\langle L_{si},R_{sj}\rangle,\qquad
C_3=\mathbb Z\langle F_{ij}\rangle,
\]

and vanish in all other nonzero relative degrees. Choose orientations so that the relative triangle boundaries are

\[
\partial L_{si}=e_{is}-e_{ss},\qquad
\partial R_{sj}=e_{sj}-e_{ss}.
\]

For each tetrahedron the relative boundary, up to the compatible choice of orientation, is

\[
\partial F_{ij}=L_{ij}-R_{ji}+L_{ji}-R_{ij}.
\]

The last expression is a cycle under \(\partial_2\), and the indicated orientations can be realized by reversing individual simplicial generators as necessary.

**2. Degree one as a persistent quotient.** Write \(M=\mathbb Z^{ab}=\mathbb Z\langle e_{ij}\rangle\) and \(\epsilon:M\to\mathbb Z\) for the map sending every cross-edge basis vector to \(1\). The connecting map of the pair \((X_t,Y)\) from relative first homology to \(\widetilde H_0(Y)\cong\mathbb Z\) is induced by \(\epsilon\). Consequently, with \(A_0=\ker\epsilon\), the long exact sequence gives the *natural*, simultaneous presentation

\[
\widetilde H_1(X_t;\mathbb Z)
 \cong A_0/\operatorname{im}\partial_2^{(t)}.
\]

All images lie in \(A_0\), and \(\operatorname{im}\partial_2^{(t)}\subseteq\operatorname{im}\partial_2^{(t+1)}\), so every degree-one map is **surjective as an integer group homomorphism**. To see that the source and target are torsion-free, view \(\partial_2^{(t)}\) as the ordinary incidence map of a graph \(\Gamma_t\). Its vertices are the \(ab\) symbols \(e_{ij}\), and its edges join \(e_{ss}\) to each \(e_{is}\) and \(e_{sj}\), with \(s\le t\). Incidence cokernels are free and indexed by connected components. For \(t=0\) all \(ab\) vertices are isolated. For \(t\ge1\), there is one nontrivial connected component containing every \(e_{ij}\) with \(i\le t\) or \(j\le t\), and \((a-t)(b-t)\) isolated vertices. The induced augmentation on the component lattice is the weighted sum with weights equal to component sizes; its kernel is a free subgroup of a free abelian group. This proves the displayed first-homology ranks. Each surjection between these free groups splits because the target is projective over \(\mathbb Z\), so its kernel is primitive. The successive rank differences are exactly \(a+b-2\) at \(t=1\), and \(a+b-2t+1\) for \(t\ge2\). Simultaneously splitting these finitely many nested surjections proves the degree-one barcode. Importantly, the augmentation **must be weighted by component size**; simply subtracting one component basis vector from another does not generally give a cycle.

**3. Degree two and the natural complete-graph cycle lattice.** Since \(H_1(Y)=H_2(Y)=0\), the relative long exact sequence gives a natural isomorphism \(H_2(X_t)\cong H_2(X_t,Y)\). The latter is the cycle module of the graph \(\Gamma_t\), modulo the square boundaries of its \(F_{ij}\). For \(t\ge1\), collapse all pendant edges in its nontrivial component; for each pair \(i<j\le t\) the two length-two paths between the diagonal vertices \(e_{ii}\) and \(e_{jj}\) bound exactly the square corresponding to \(F_{ij}\). Contracting one such filled square and then subdividing paths identifies the remaining cycle lattice with \(Z_1(K_t;\mathbb Z)\), the ordinary cycle lattice of the complete graph on the diagonal labels. This is a calculation of an **integral chain quotient**, not only of rational dimensions. For \(t=1,2\), that lattice is zero.

It remains to verify that the identifications respect the *actual inclusion maps*. Take, for every \(2\le i<j\le t\), the integral cycle traversing the selected paths from label \(1\) to \(i\), from \(i\) to \(j\), and from \(j\) to \(1\). Each is represented by triangles already present at stage \(t\) and remains literally the same relative cycle at all later stages. For any fixed stage, these classes are precisely the standard integral fundamental-cycle basis obtained from the star spanning tree at vertex \(1\) in \(K_t\). On adjoining label \(t+1\), those old basis classes remain part of the enlarged basis, and exactly \(t-1\) additional ones appear. This proves that every \(H_2(X_t)\to H_2(X_{t+1})\) is a primitive split injection and gives its explicit decomposition. The same conclusion follows directly from \(\partial_3\): the new tetrahedral relation for \(\{i,t+1\}\) is the only relation containing the new triangle \(L_{t+1,i}\), so no combination of new relations can annihilate an old cycle. The fundamental-cycle description upgrades injectivity to a **primitive integral splitting**. Because the isomorphism \(H_2(X_t)\cong H_2(X_t,Y)\) is natural, these are the asserted maps on ordinary homology. The new cycles at stage \(s\) have count \(s-2\), giving the essential degree-two intervals.

**4. Higher degrees and endpoints.** All nonzero relative cells have dimension at most three, and the tetrahedral boundary vectors are independent: the coefficient of \(L_{ij}\) for \(i<j\) occurs in exactly one tetrahedral boundary and equals a unit. Thus the relative third homology vanishes integrally; all higher relative groups vanish for dimension reasons. Since \(Y\) is the disjoint union of contractible simplices, no higher absolute reduced homology survives. The first and second homology calculations, valid uniformly for \(0\le t\le T\), finish the theorem.

## Verification

The standalone Python 3 program `matching_fault_verifier.py` checks the mixed-face classification by an independent exhaustive induced-degree test. For \(3\le a\le5\), \(a\le b\le6\) and every \(0\le t\le a\), it constructs integer relative boundary matrices from the specified triangles and tetrahedra, checks \(\partial_2\partial_3=0\), evaluates homology dimensions modulo primes \(2,3,5\), and checks the induced degree-two inclusion image ranks using actual chain kernels. Its recorded output in `verification_output.txt` reports 43 stages and 129 modular checks passing. These finite tests do not establish integral primitivity or the infinite theorem: those conclusions use the component-weighted exact sequence and fundamental-cycle bases in the proof.

## Relationship to prior work

Carnero Bravo, *The Forest Filtration of a Graph* (first public 2023-07-25), introduced the maximum-degree forest filtration and explicitly identifies its degree-one stage with the second-independence complex. It classifies several graph families and motivates studying functorial changes of graph data. Two accessible pre-existing descriptions, *Mixed-dimensional dissociation homotopy under partial matching deletion from \(K_{a,b}\)* and *Homotopy of second independence complexes after deleting a bipartite matching*, already prove the individual-stage homotopy types and ranks quoted above. Both of their complete `RESULT.md` statements and proofs were inspected. The latter explicitly excludes determining inclusion maps when \(t\) increases. The former calculates a square-complex model stage by stage, without identifying the maps of the deleted-matching filtration. The **new claim is only the integral inclusion-map and barcode classification**, not the previously established stagewise homotopy or face enumeration. The compatibility of the nested integer cycle bases and the component-weighted quotient presentations is essential to that distinction. No claim of independently certified publication priority is made.

## Limitations

The statement treats only successive deletion of pairwise disjoint cross-edges, and only the second-independence/dissociation complex. It does not classify arbitrary deletion patterns, higher-independence parameters, or equivariant homotopy. Integral persistence here is a direct-sum decomposition in the ordinary abelian-group category; it does not assert compatibility with all automorphisms of the labeled graph. Known stagewise homotopy types are quoted only as background. Searches and full-text comparisons cannot exclude all uncatalogued equivalents. External independent validation has not been performed.

## References

1. A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, v1 submitted 2023-07-25, https://arxiv.org/abs/2307.13271.
2. *Mixed-dimensional dissociation homotopy under partial matching deletion from \(K_{a,b}\)*, public mathematical finding (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-mixed-dimensional-dissociation-homotopy-under-partial-matching-d--04d61268ad5a.
3. *Homotopy of second independence complexes after deleting a bipartite matching*, public mathematical finding (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-homotopy-of-second-independence-complexes-after-deleting-a-bipar--223b7506ca23.
