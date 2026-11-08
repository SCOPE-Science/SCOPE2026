# One-step persistence and integral symmetry of induced-degree complexes of complete bipartite graphs

## Finding
Let \(A,B\) be disjoint sets of sizes \(m,n\ge 2\), and let \(K_{m,n}\) be the complete bipartite graph with those two parts. For each integer \(r\ge 0\), define the **induced-degree complex**
\[
X_r(m,n)=\{S\subseteq A\sqcup B:\max_{v\in S}\deg_{K_{m,n}[S]}(v)\le r\}.
\]
The empty face is included, and the maximum over an empty set is zero. These are nested simplicial complexes indexed by the degree threshold \(r\).

Write \(L_A=\ker(\mathbb Z[A]\xrightarrow{\sum}\mathbb Z)\) and \(L_B=\ker(\mathbb Z[B]\xrightarrow{\sum}\mathbb Z)\). Set \(a_r=\binom{m-1}{r}\), \(b_r=\binom{n-1}{r}\), with binomial coefficients zero when the lower argument exceeds the upper one. The integral reduced homology, including the natural \(S_m\times S_n\)-action, is:
\[
\widetilde H_0(X_0;\mathbb Z)\cong\mathbb Z,
\qquad
\widetilde H_1(X_1;\mathbb Z)\cong\ker\bigl(\mathbb Z[A\times B]\xrightarrow{\sum}\mathbb Z\bigr),
\]
with every other reduced homology group in those respective levels zero. For every \(r\ge 2\),
\[
\widetilde H_j(X_r;\mathbb Z)\cong
\begin{cases}
\bigwedge^r L_A\oplus\bigwedge^r L_B,&j=r,\\
\bigwedge^r L_A\otimes_{\mathbb Z}\bigwedge^r L_B,&j=2r-1,\\
0,&\text{otherwise}.
\end{cases}
\]
These are integral and equivariant module isomorphisms. In particular, the underlying ordinary homotopy type for \(r\ge2\) is
\[
X_r(m,n)\simeq
\left(\bigvee^{a_r+b_r}S^r\right)\vee
\left(\bigvee^{a_rb_r}S^{2r-1}\right),
\]
and \(X_1\simeq\bigvee^{mn-1}S^1\), while \(X_0\simeq S^0\).

**Every transition map on reduced integral homology is zero:**
\[
\widetilde H_j(X_r;\mathbb Z)\longrightarrow
\widetilde H_j(X_{r+1};\mathbb Z)
\quad\text{is zero for all }r,j\ge0.
\]
Thus the complete reduced integral persistence is a direct sum of unit-length intervals \([r,r+1)\), with multiplicities one in degree zero at \(r=0\), \(mn-1\) in degree one at \(r=1\), and for each \(r\ge2\), multiplicities \(a_r+b_r\) in degree \(r\) and \(a_rb_r\) in degree \(2r-1\); zero multiplicities are omitted. The persistence decomposition is asserted for homology groups over \(\mathbb Z\) in the sense of the displayed maps and free groups, not as a general barcode theorem for arbitrary integer persistence modules.

For \(m=n\), part exchange swaps the two summands of \(\widetilde H_r\) for \(r\ge2\), and acts on \(\widetilde H_{2r-1}\) by \((-1)^r\) times exchange of the two tensor factors. At \(r=1\), part exchange acts by minus transpose on the oriented edge augmentation lattice; at \(r=0\), it acts by \(-1\). This determines the full integral homology action of \((S_m\times S_m)\rtimes C_2\) in the balanced case.

To read off rational characters, for any permutation \(\sigma\) of \(A\) set
\[
q_r(\sigma)=[z^r]\frac{\det(I+zP_\sigma)}{1+z}
=[z^r]\frac{\prod_{c\text{ cycle of }\sigma}(1-(-z)^{|c|})}{1+z}.
\]
For \(r\ge2\), the trace of \((\sigma,\tau)\) is \(q_r(\sigma)+q_r(\tau)\) in degree \(r\) and \(q_r(\sigma)q_r(\tau)\) in degree \(2r-1\). In the balanced case, a side-exchanging element with cycle product \(\sigma\tau\) has trace zero in degree \(r\) and \((-1)^rq_r(\sigma\tau)\) in degree \(2r-1\). At \(r=1\), the product-subgroup trace is \(f(\sigma)f(\tau)-1\) and the side-exchange trace is \(1-f(\sigma\tau)\), where \(f\) counts fixed points.

For example, when \(m=n=4\), the threshold-two complex has reduced homology ranks six in degree two and nine in degree three; threshold three has ranks two in degree three and one in degree five. **The degree-three transition is nevertheless zero**, despite both endpoints having nonzero homology in that same degree.

## Assumptions and scope
All graphs are finite simple graphs; \(K_{m,n}[S]\) is the subgraph induced by a vertex subset \(S\). The result covers all integers \(m,n\ge2\) and degree thresholds \(r\ge0\), including thresholds beyond the maximum graph degree. Reduced integral simplicial homology uses the usual alternating boundary. For a zero binomial coefficient the corresponding wedge or module summand is absent. Homotopy statements are ordinary (non-equivariant), whereas the integral module and character statements are equivariant.

## Proof
**1. Exact face decomposition.** Let \(\Delta_A\) and \(\Delta_B\) be full simplices on the parts. For \(r\ge1\), let \(S_A=\operatorname{skel}_{r-1}\Delta_A\) and similarly \(S_B\), and let \(J_r=S_A*S_B\) be their simplicial join. Any subset contained wholly in one part belongs to its entire full simplex. If it meets both parts in \(a,b\ge1\) vertices, the induced graph is \(K_{a,b}\), hence has maximum degree \(\max(a,b)\); it is allowed precisely when both \(a,b\le r\). Therefore, exactly as subcomplexes,
\[
X_r=J_r\cup\Delta_A\cup\Delta_B,
\quad J_r\cap\Delta_A=S_A,\quad J_r\cap\Delta_B=S_B.
\]
The two full part-simplices have empty geometric intersection. Thus \(X_r\) is obtained from \(J_r\) by attaching two contractible cones along \(S_A\) and \(S_B\).

**2. Integral skeleton cycles.** For any finite set \(A\) with \(|A|=m\), the reduced chain complex of its full simplex is \(\bigwedge^{k+1}\mathbb Z[A]\) in degree \(k\), with boundary given by contraction with the coordinate-sum functional. Since this functional splits over \(\mathbb Z\), its kernel in wedge degree \(r\) is naturally \(\bigwedge^r L_A\). The simplex is exact in positive reduced degrees, so the top reduced homology of \(S_A\) is \(\bigwedge^rL_A\) in degree \(r-1\) (zero when \(r\ge m\)), and no other reduced homology occurs. More specifically, choosing a distinguished vertex exhibits \(S_A\) as a wedge of \(\binom{m-1}{r}\) spheres of dimension \(r-1\), or a point when the binomial vanishes. The construction and chain identification are natural under permutations, even though the choice used to display a wedge is not equivariant.

**3. The high-dimensional join.** The reduced join chain complex is the tensor product of the reduced skeleton chain complexes, shifted by one degree. Because the reduced homologies of the skeletons are free, the integral Künneth formula gives
\[
\widetilde H_{2r-1}(J_r;\mathbb Z)
\cong\bigwedge^rL_A\otimes\bigwedge^rL_B,
\]
with no other reduced homology. For \(r\ge2\), the join is a wedge of \(a_rb_r\) spheres of dimension \(2r-1\) when both factors have homology, otherwise is contractible. Therefore \(J_r\) is at least \((2r-2)\)-connected. The attaching maps \(S_A,S_B\to J_r\) are nullhomotopic because their sources have dimension at most \(r-1\le2r-2\). Coning off the two nullhomotopic inclusions yields the ordinary wedge decomposition in the finding. The use of wedge splittings here is non-equivariant.

**4. Natural homology representations.** Since \(J_r\) has no homology in degrees \(r\) or \(r-1\) for \(r\ge2\), the long exact sequence of the pair \((X_r,J_r)\), excision and the relative pairs \((\Delta_A,S_A)\), \((\Delta_B,S_B)\) give a natural isomorphism
\[
\widetilde H_r(X_r;\mathbb Z)\cong
\widetilde H_{r-1}(S_A;\mathbb Z)\oplus
\widetilde H_{r-1}(S_B;\mathbb Z).
\]
Likewise, attaching the two cones does not alter reduced homology in degree \(2r-1\), so inclusion identifies the latter with \(\widetilde H_{2r-1}(J_r;\mathbb Z)\). These are isomorphisms of natural \(S_m\times S_n\)-lattices, not only equality of ranks. Exchanging parts swaps the relative summands; a top-dimensional join generator contains \(r\) vertices from each part, so reversing their order contributes \((-1)^{r^2}=(-1)^r\), proving the stated tensor-flip action.

**5. The first two levels.** The zero-degree complex is the disjoint union of the two full simplices, hence \(S^0\) up to homotopy. For \(r=1\), the cross-faces are exactly the \(mn\) edges with one endpoint in each part. Collapsing each contractible full part-simplex leaves a connected multigraph with two vertices and \(mn\) edges. Its integral cycle lattice is the kernel of summation of oriented edges, of rank \(mn-1\). Independent permutations permute edges, and part exchange reverses their orientation, giving the stated module actions.

**6. Death at the next degree threshold.** In degrees \(r\) and \(2r-1\), the only degree shared with the possible nonzero homology degrees \(r+1\) and \(2r+1\) of \(X_{r+1}\) is \(2r-1=r+1\), which forces \(r=2\). The maps from thresholds zero and one vanish as well because their target groups vanish in the same homological degree. It remains to check \(\widetilde H_3(X_2)\to\widetilde H_3(X_3)\). Inclusion \(J_2\hookrightarrow X_2\) is an isomorphism on reduced degree-three homology. This group is integrally generated by joins \(\partial T_A*\partial T_B\), where \(T_A,T_B\) range over oriented triangles in the respective vertex parts. In \(X_3\), the four-chain \(T_A*\partial T_B\) is defined and has simplicial boundary \(\partial T_A*\partial T_B\). Thus the entire degree-three map vanishes. Therefore every consecutive-degree filtration map vanishes, giving the stated integral persistence intervals.

**7. Rational characters.** The short exact sequence \(0\to L_A\to\mathbb Z[A]\to\mathbb Z\to0\) splits rationally; taking elementary symmetric functions of permutation eigenvalues gives the displayed determinant coefficient for \(\bigwedge^rL_A\). Tensor products multiply characters. The part-exchange traces are zero on exchanged summands and are the trace of a signed flip on the top tensor module, equal to \((-1)^rq_r(\sigma\tau)\). The one-edge case follows from the oriented-edge augmentation module.

## Verification
The bundled standalone standard-library program `verify_degree_induced.py` independently enumerates all simplices for both parts of sizes two through five, computes reduced boundary ranks over primes \(2,3,5\) for thresholds zero through four, and agrees with the theorem in 240 rank comparisons. It checks 4,096 signed reduced Lefschetz traces under product permutations and 2,464 under part-exchanging permutations, and checks 100 explicit integral triangle-join fillers for the exceptional threshold-two to threshold-three map. Running `python3 verify_degree_induced.py` reproduces `verification_output.txt`. These are exhaustive **within the stated finite ranges**, not exhaustive over the infinite parameter family; the numbered proof gives the general argument.

## Relationship to prior work
Guo, Zhao, Lai and Mao (2015, arXiv:1505.04867, first public May 19, 2015) define \(k\)-independent vertex subsets by **maximum induced degree** and study their extremal cardinalities, including regular variants in complete multipartite graphs (Proposition 2.2); they do not compute the associated simplicial filtration, its integral homology modules, or persistence maps. The regularity restriction is additional and is not imposed here.

Deshpande and Singh (2020, arXiv:2001.05448, Theorem 3.5) compute homotopy types of a differently defined higher independence complex: there each induced connected component has at most a specified number of **vertices**, rather than bounding its maximum degree. Singh (2020, arXiv:2006.13632) treats higher matching and bounded-degree graph complexes whose *vertices are graph edges*, not vertex subsets of the graph. Neither gives the present homology formulas or maps through a change in the maximum induced-degree threshold. These distinctions are statements about the precise constructions and do not assert novelty from terminology alone.

## Limitations
The theorem is restricted to complete bipartite graphs with both parts of size at least two; it does not cover arbitrary multipartite graphs or arbitrary induced-degree filtrations. The ordinary homotopy wedge equivalence is not asserted equivariant. The integral homology representations are identified, but the full integral equivariant homotopy type is not. The sources inspected do not establish a definitive publication-priority claim; a parallel formulation in unindexed literature remains possible. No independent validation has been performed.

## References
1. Z. Guo, H. Zhao, H. Lai and Y. Mao, *On the regular k-independence number of graphs*, arXiv:1505.04867, first submitted 2015-05-19, https://arxiv.org/html/1505.04867v2 .
2. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, first submitted 2020-01-15, https://arxiv.org/html/2001.05448v2 .
3. A. Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, arXiv:2006.13632, first submitted 2020-06-24, https://arxiv.org/abs/2006.13632 .
