# Full Clebsch-neighborhood homology character and multiplicity-free symmetry decomposition

## Finding
Let \(C\) be the **five-regular** Clebsch graph, on the additive group \(V=\mathbb F_2^4\) with Cayley generators \(s_1=1,s_2=2,s_3=4,s_4=8,s_5=15\) in binary XOR notation. Let \(K=\mathcal N(C)\) be its ordinary open Lovász neighborhood complex. Its known nonequivariant homotopy type is \(K\simeq\bigvee^{31}S^2\); that homotopy calculation is **not** claimed as new.

The full graph automorphism group is \(G=V\rtimes S_5\), of order \(1920\). Write \(U_k=\{(z_1,\ldots,z_k)\in\mathbb Q^k:\sum z_i=0\}\) for the standard permutation-augmentation module of \(S_k\). Every character of \(V\) has a unique description \(\theta_E:V\to\{\pm1\}\), where \(E\subseteq[5]\) has even size and \(\theta_E(s_i)=-1\) precisely when \(i\in E\). Fix an arbitrary two-element subset \(E_2\) and four-element subset \(E_4\) of \([5]\), and write \(G_E=V\rtimes(S_E\times S_{E^c})\), with the natural set-stabilizer interpretation.

The **complete rational \(G\)-module structure** is the multiplicity-free direct sum
\[
\boxed{\begin{aligned}
H_2(K;\mathbb Q)\cong{}&\operatorname{Inf}_{S_5}^{G}\!\left(\bigwedge^2 U_5\right)\\
&\oplus\operatorname{Ind}_{G_{E_2}}^{G}\!\left(\theta_{E_2}\otimes(\mathbf1_{S_2}\boxtimes\operatorname{sgn}_{S_3})\right)\\
&\oplus\operatorname{Ind}_{G_{E_4}}^{G}\!\left(\theta_{E_4}\otimes(\operatorname{sgn}_{S_4}\otimes U_4)\right).
\end{aligned}}
\]
Here an expression involving a character of \(V\) and a stabilizer representation denotes the natural extended representation of the indicated semidirect product, and \(\operatorname{Inf}\) denotes inflation along \(G\twoheadrightarrow S_5\). The three direct summands are pairwise nonisomorphic, absolutely irreducible rational representations of dimensions \(6\), \(10\) and \(15\), respectively.

Equivalently, the character of **every** \(g=(t,\pi)\in G\) is
\[
\boxed{\chi_2(t,\pi)=\sum_{\substack{E\subseteq[5],\ |E|\in\{0,2,4\}\\\pi(E)=E}}\theta_E(t)\,h_E(\pi),}
\]
where, putting \(f(\pi)=|\operatorname{Fix}_{[5]}(\pi)|\),
\[
h_E(\pi)=\begin{cases}
\big((f(\pi)-1)^2-(f(\pi^2)-1)\big)/2,&|E|=0,\\
\operatorname{sgn}(\pi|_{E^c}),&|E|=2,\\
\operatorname{sgn}(\pi|_E)\big(|\operatorname{Fix}_E(\pi)|-1\big),&|E|=4.
\end{cases}
\]
The translation-fixed subspace is \(H_2(K;\mathbb Q)^V\cong\bigwedge^2U_5\) and has dimension \(6\), but \(H_2(K;\mathbb Q)^G=0\). Since the known nonzero reduced rational homology is concentrated in degree \(2\), the quotient \(K/G\) is rationally acyclic in reduced degrees. This quotient-acyclicity conclusion is not presented as new: it also follows from the previously determined action of a smaller subgroup.

## Assumptions and scope
The graph has vertex set \(\mathbb F_2^4\), with adjacency \(x\sim y\) exactly when the XOR difference \(x+y\) belongs to \(S=\{1,2,4,8,15\}\). This is the five-regular Clebsch graph, not its ten-regular complement. A nonempty subset of vertices is a face of \(K\) if and only if it has a common *open* graph neighbor. The group acts by all translations and linear maps that permute the five generators. Rational representations and characters, rather than integral module decompositions, are asserted. The formal product notation uses the convention \((t,\pi)(u,\sigma)=(t+\pi u,\pi\sigma)\).

For comparison with the intrinsic Čech construction, let \(Q_4\) be the four-cube on the same vertex set and let \(\operatorname{Cech}_2(Q_4)\) have simplices contained in closed graph neighborhoods \(\{x,x+1,x+2,x+4,x+8\}\). The explicitly defined affine bijection
\[
\phi(x)=15+L(x),\quad (L(1),L(2),L(4),L(8))=(14,13,11,7)
\]
is a simplicial isomorphism \(\operatorname{Cech}_2(Q_4)\cong K\). Its natural \(384\)-element four-cube symmetry group embeds as an index-five subgroup of \(G\). Thus the stated new claim genuinely concerns the additional symmetries, not a second homotopy calculation of an unrelated complex.

## Proof
**1. Faces, homotopy concentration, and full group.** The sixteen open neighborhoods have five vertices each. Exhaustive subface generation (independently repeated with the common-neighbor predicate) yields \(352\) nonempty faces, with face vector \((16,80,160,80,16)\). A sequential vertex-toggle matching uses \(160\) pairs; the complete \(1040\)-cover Hasse orientation is acyclic and leaves precisely one critical vertex and \(31\) critical two-simplices. Hence \(K\simeq\bigvee^{31}S^2\), independently confirming the pre-existing homology premise for the present explicit graph. No other reduced homology contributes to the Lefschetz calculation.

Permutations of the five generators extend uniquely to invertible linear transformations of \(V\) because their only linear dependence is \(s_1+\cdots+s_5=0\); translations give \(16\cdot5!=1920\) distinct graph automorphisms. Conversely, the ten unordered sums \(s_i+s_j\) are distinct and exhaust the vertices at distance two from zero. An automorphism fixing zero and all five neighboring vertices fixes each distance-two vertex, since the latter is the unique nonzero common neighbor of its defining pair of neighbors; therefore the point stabilizer injects into \(S_5\). This proves \(\operatorname{Aut}(C)=G\), not merely that \(G\) is a subgroup.

**2. Trace from fixed oriented simplices.** For an automorphism \(g\), the signed simplex Lefschetz sum is
\[
L(g)=\sum_{k\ge0}(-1)^k\operatorname{tr}(g\mid C_k(K;\mathbb Q))=1+\operatorname{tr}(g\mid H_2(K;\mathbb Q)).
\]
The trace on \(C_k\) is the sum of signs of the induced vertex permutations on the setwise-fixed \(k\)-simplices. The independent vertex-cycle method enumerates just those faces that are unions of cycles of the permutation \(g\), giving the same \(L(g)\). The bundled exhaustive checker evaluates both constructions for **every** one of the \(1920\) group elements and verifies agreement. It finds the full-character value distribution \((-5:80,-1:825,1:944,3:60,7:10,31:1)\). These are exact finite sums; no sampling or asymptotic extrapolation is used.

**3. Fourier projection onto character fibers.** Since \(V\) is an elementary abelian \(2\)-group, its sixteen rational characters are exactly the \(\theta_E\) indexed by even subsets \(E\). The fiber trace on the \(\theta_E\)-eigenspace, for every \(\pi\in\operatorname{Stab}_{S_5}(E)\), is the exact Fourier average
\[
\operatorname{tr}\big(\pi\mid H_2(K;\mathbb Q)_{\theta_E}\big)
=\frac1{16}\sum_{t\in V}\theta_E(t)\,\chi_2(t,\pi).
\]
The checker evaluates all \(120+10\cdot12+5\cdot24=360\) stabilizing pairs and verifies that these fiber traces equal the stated \(h_E(\pi)\). At identity they have dimensions \(6\), \(1\) and \(3\) for sizes \(0\), \(2\) and \(4\). The size-zero trace is that of \(\bigwedge^2U_5\); for size two it is the sign of the permutation of the complementary triple; for size four it is the sign-twisted augmentation character on the four-set. Over characteristic zero, equality of all finite-group characters identifies the representations.

**4. Assembly and irreducibility.** Distinct \(\theta_E\) form three \(S_5\)-orbits, of sizes \(1\), \(10\), \(5\). Clifford's little-group construction for \(V\rtimes S_5\) identifies the sum of fibers in each orbit with the corresponding induction stated above. Each fiber representation of its stabilizer is absolutely irreducible (the exterior square of the standard \(S_5\)-module; a one-dimensional character; and the sign twist of the standard \(S_4\)-module), so each induced orbit representation is absolutely irreducible; their distinct \(V\)-spectral orbits make them nonisomorphic. The checker independently recovers \(\chi_2(t,\pi)\) from the three induced characters on all \(1920\) elements. Since \(\bigwedge^2U_5\) is nontrivial irreducible and the other two summands contain no \(V\)-fixed vectors, the full invariant space is zero.

The last proof step does not assert an equivariant wedge-of-spheres splitting: it is a *homology representation* decomposition.

## Verification
Run `python3 verify.py` in the directory containing the bundled standalone checker. The standard-library script constructs the complete graph and complex from the displayed definitions, proves the Morse matching acyclic by topological sorting the entire directed Hasse graph, independently counts signed fixed simplices and unions of cycles, enumerates all \(1920\) automorphisms, reconstructs all sixteen character fibers, checks all \(360\) stabilizer traces and all \(1920\) reconstructed induced-character values, and checks the affine isomorphism with the four-cube closed-star complex. It also checks all \(384\) restricted characters against the previously published four-cube Čech formula. Its captured output is `verification_output.txt` and concludes with `ALL_CHECKS_PASS`.

The finite enumeration is exhaustive **for this particular finite graph**, and therefore supplies a legitimate proof certificate for the stated finite representation. The proof does not infer an all-parameter statement from a finite experiment.

## Relationship to prior work
Kozlov (2005) established general connections between Lovász neighborhood complexes and graph Hom-complexes, without the present Clebsch-group character. Adams, Shukla, and Singh (first public 2022-12-12) proved the homotopy type of radius-one closed-neighborhood Čech complexes of hypercubes, including the four-cube case. An already published exact Clebsch-neighborhood computation and a general parity-component calculation for hypercube neighborhood complexes both give the nonequivariant wedge of \(31\) spheres; **neither is new here**.

More significantly, *Full hyperoctahedral homology character of scale-two hypercube Čech complexes* previously determined the character of the **same** simplicial complex under the natural \(384\)-element symmetry group of \(Q_4\). The affine isomorphism displayed above makes this a real overlap, not merely a similarly named result. The published smaller-group character cannot determine the traces of the other \(1536\) Clebsch symmetries or the irreducible decomposition for \(G\). Indeed, restricting a representation from a group to an index-five subgroup loses precisely that information. The checker verifies the restricted published formula on all \(384\) elements, so the new character is a genuine extension compatible with the known character. No novelty is claimed for its known restriction or for consequences that already follow from that restriction.

## Limitations
This is a rational homology representation theorem for the specific \(16\)-vertex graph and ordinary open-neighborhood complex; it does not determine integral-lattice indecomposability, the full equivariant homotopy type, or the integral homology of the quotient. All proof computations concern finite enumerations of these particular objects. The full index-five extension and multiplicity-free decomposition were not found in the inspected literature or indexed mathematical records; another unindexed or unpublished equivalent calculation cannot be excluded. Independent review has not been performed.

## References
1. D. N. Kozlov, *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes*, arXiv:math/0503613v1, first public 2005-03-28; *Topology and its Applications* 153 (2006), 2445–2454.
2. H. Adams, S. Shukla, A. Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871v1, first public 2022-12-12; Theorem 4.1.
3. *The five-regular Clebsch neighborhood complex is a wedge of thirty-one two-spheres*, publicly indexed mathematical finding, 2026-10-11.
4. *Neighborhood complexes of hypercubes collapse to explicit two-sphere wedges*, publicly indexed mathematical finding, 2026-10-11.
5. *Full hyperoctahedral homology character of scale-two hypercube Čech complexes*, publicly indexed mathematical finding, 2026-10-11; explicit closed-star character theorem.
6. R. Forman, *Morse Theory for Cell Complexes*, *Advances in Mathematics* 134 (1998), 90–145.
