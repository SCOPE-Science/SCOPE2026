# Integral top-homology lattice of free-involution-fixed odd-uniform matching complexes

## Finding
For every **odd** integer \(r\geq3\) and every integer \(k\geq1\), write \(m=rk\). On the set \(V=[m]\times\{0,1\}\), let \(\tau(i,b)=(i,1-b)\). Let \(\mathcal M_r(V)\) be the simplicial matching complex of the complete \(r\)-uniform hypergraph: its vertices are the \(r\)-subsets of \(V\), and its faces are collections of pairwise disjoint such subsets. Put \(X_{r,k}=|\mathcal M_r(V)|^{\langle\tau\rangle}\).

The fixed space \(X_{r,k}\) is canonically piecewise-linearly homeomorphic to the uniform \(q\)-fold vertex inflation of \(\mathcal M_r([m])\), with \(q=2^{r-1}\). For a block \(B\in\binom{[m]}r\), write \(Q_B=\{0,1\}^{B}/\langle\mathbf1\rangle\) and \(A_B=\ker(\mathbb Z[Q_B]\xrightarrow{\varepsilon}\mathbb Z)\). Its top **integral** reduced homology has a canonical decomposition
\[
\widetilde H_{k-1}(X_{r,k};\mathbb Z)
\cong\bigoplus_{P\in\operatorname{Part}_r([m])}
\bigotimes_{B\in P} A_B,
\]
where \(\operatorname{Part}_r([m])\) denotes set partitions into \(k\) unordered \(r\)-subsets, and the order of the tensor factors determines the usual orientation sign. In particular this group is free of rank
\[
\frac{(rk)!}{(r!)^k k!}\bigl(2^{r-1}-1\bigr)^k.
\]

More precisely, the centralizer \(W=C_2\wr\mathfrak S_m=C_2^m\rtimes\mathfrak S_m\) acts on the top homology and its **integral lattice** is the signed induced tensor-augmentation module obtained from one perfect partition. For a fixed partition \(P_0\), its stabilizer is \(W_{P_0}\cong(C_2^r\rtimes\mathfrak S_r)\wr\mathfrak S_k\). Each block group permutes \(Q_B\) by coordinate flips and permutations. The outer \(\mathfrak S_k\) swaps tensor factors with an additional sign of the block permutation. With this understood,
\[
\widetilde H_{k-1}(X_{r,k};\mathbb Z)
\cong_{\mathbb Z[W]}
\operatorname{Ind}_{W_{P_0}}^W\!\left(\bigotimes_{B\in P_0}A_B\otimes\operatorname{sgn}_{\mathfrak S_k}\right).
\]
The sign tensor is shorthand for the stated block-permutation action; there is no arbitrary choice of an integral splitting. The central involution \(\tau\) acts trivially. By contrast, the corresponding top group of the **un-inflated** complex \(\mathcal M_r([m])\) vanishes: \(\widetilde H_{k-1}(\mathcal M_r([m]);\mathbb Z)=0\).

For example, at \(r=3,k=2\), \(X_{3,2}\) has ten connected components, each homeomorphic to \(K_{4,4}\), so \(\widetilde H_1(X_{3,2};\mathbb Z)\cong\mathbb Z^{90}\). At \(r=3,k=3\), the top rank is \(7560\). No assertion is made about homology in degrees below \(k-1\) for general parameters.

## Assumptions and scope
All geometric realizations use finite abstract simplicial complexes and ordinary integral simplicial homology. A fixed point of the geometric realization is not assumed to be a vertex fixed individually: barycenters of permuted vertices are included. The uniformity parameter is odd and at least three, and the original ground-set cardinality is exactly twice a multiple of \(r\). The normalizer action is the natural one from permutations commuting with \(\tau\). The theorem concerns the **geometric fixed set**, not the orbit-space quotient.

## Proof
**1. Orbit-barycenter triangulation.** A point of a simplex has nonnegative barycentric coordinates on its vertices; it is fixed by \(\tau\) exactly when its coordinates are constant on each \(\tau\)-orbit. Such a point has support that is a \(\tau\)-stable matching. Taking one barycenter for each orbit of hyperedges whose union is a matching yields an explicit affine homeomorphism, simplex by simplex, from the admissible-orbit simplicial complex onto the geometric fixed set. The inverse assigns equal coordinate mass to the two hyperedges of each orbit. These maps agree on intersections and are piecewise linear.

**2. Admissible hyperedge orbits.** Because \(r\) is odd, no \(r\)-set \(E\) satisfies \(\tau(E)=E\): an invariant set would be a union of two-element ground-point orbits and hence have even cardinality. A two-element hyperedge orbit \(\{E,\tau(E)\}\) is admissible precisely when \(E\cap\tau(E)=\varnothing\), equivalently when \(E\) includes at most one point from each pair \(\{(i,0),(i,1)\}\). Thus its support comprises exactly \(r\) different pair labels \(B\), and it is specified by a binary transversal \(b\in\{0,1\}^{B}\) modulo global bit-complement. The resulting fiber \(Q_B\) has cardinality \(2^{r-1}\).

Two different admissible orbits are compatible if and only if their supports \(B\) are disjoint: each orbit-union contains both elements of each pair indexed by its support. This is exactly the definition of the \(q\)-fold vertex inflation of \(\mathcal M_r([m])\), establishing the stated PL-homeomorphism.

**3. Top boundary decomposition over perfect partitions.** Every facet of the inflated complex has at most \(k\) vertices, and facets of size \(k\) correspond to an \(r\)-block partition \(P\) of \([m]\) together with one phase from each \(Q_B\), for \(B\in P\). Fix a partition and choose an order of its blocks. The associated top-chain summand is \(\bigotimes_{B\in P}\mathbb Z[Q_B]\). Every codimension-one face of a size-\(k\) facet leaves exactly \(r\) unused pair labels, so its missing support block is uniquely determined by that face. Hence two top simplices over **different** partitions never contribute to the same oriented ridge. Consequently the full top boundary splits as the direct sum, over \(P\), of the tensor-augmentation differential for the join of the discrete sets \(Q_B\).

For the join of \(k\) nonempty discrete sets, the kernel of its top augmented boundary equals \(\bigotimes_{B\in P}\ker(\varepsilon_B)\), integrally. To see this directly, fix basepoints \(q_B^0\) and use the unimodular splitting \(\mathbb Z[Q_B]=\mathbb Z e_{q_B^0}\oplus A_B\), where \(A_B\) has basis \(e_q-e_{q_B^0}\). The boundary is the alternating sum of maps applying \(\varepsilon_B\) in one factor. In the resulting tensor direct-sum basis, every tensor containing a basepoint factor has a nonzero, separately detectable image with its first basepoint removed. Equivalently, the augmented chain complex of the join is the suspension of the tensor product of the reduced chain complexes of the discrete factors; because these chain groups are free, the top cycle group is precisely \(\bigotimes_B A_B\). This argument also applies at \(k=1\), where the boundary is the reduced augmentation to \(\mathbb Z\). As there are no chains one dimension higher, the top cycle group equals top reduced homology. Its rank is the number of set partitions, \((rk)!/((r!)^k k!)\), multiplied by \((2^{r-1}-1)^k\).

**4. Integral symmetry and comparison to the base.** Every element of \(W\) preserves admissible orbit matchings and permutes perfect partitions. The stabilizer of one partition acts on its phase sets by signed-coordinate permutations and permutes blocks. A swap of two blocks in an oriented top simplex contributes a minus sign, yielding the indicated twisted induced module over \(\mathbb Z\). This construction uses actual integer chains, not merely characters over a field. The global flip \(\tau\) complements every phase representative and hence fixes each phase class. In the un-inflated matching complex, every top simplex has one distinct free codimension-one face (remove any block, leaving that very block as the unique completion); so its top boundary is injective, including the reduced \(k=1\) case.

## Verification
The accompanying `verify.py` uses only the Python standard library. It enumerates **original** odd-uniform hyperedges for the cases \((r,m)=(3,3),(3,6),(5,5)\), checks the fixed-orbit phase cardinality, and for \((3,6)\) directly constructs 80 orbit vertices and 160 compatible pairs. Its connected-component enumeration finds ten copies of an eight-vertex, sixteen-edge graph, hence \(90\) independent cycles. Separately it constructs the integral top boundary matrices of joins of phase sets for \((q,k)=(4,1),(4,2),(4,3),(16,1),(16,2)\); their exact reductions over the fields of characteristics 2, 3, 5, and 7 give nullities \(3,9,27,15,225\). Independent arithmetic checks reproduce the partition-count formula at \((3,1),(3,2),(3,3),(5,1),(5,2)\). These finite computations corroborate, but do not replace, the universal integral tensor proof.

## Relationship to prior work
Björner, Wachs and Welker give the general vertex-inflation theorem in *Poset Fiber Theorems*, Theorem 6.2 and Corollary 6.3, which already imply the **nonequivariant rank** of an identified inflated complex; their Corollary 8.5 gives an equivariant homology decomposition **over a characteristic-zero field**. No novelty is claimed for these general inflation formulas or for a rational character consequence of them. Shareshian and Wachs study symmetric-group representations on the homology of ordinary uniform hypergraph matching complexes, likewise working over complex coefficients. The specific new object here is the **geometric fixed locus of the free involution on the complete odd-uniform hypergraph matching complex** and the direct **integral, centralizer-equivariant top lattice** with its phase action and block-orientation signs. The latter is not asserted to follow as an integral isomorphism from a characteristic-zero calculation.

## Limitations
The statement does not classify lower-dimensional homology, torsion there, or the homotopy type of the full fixed complex. The even-uniform case has individually fixed hyperedges, so the orbit description changes. The theorem uses a free involution, not a general permutation subgroup. The claimed novelty is relative to the inspected sources; a different published formulation using matching-partition inflations or signed permutation modules might cover it. No independent mathematical audit has been performed.

## References
1. A. Björner, M. L. Wachs and V. Welker, *Poset Fiber Theorems*, Transactions of the American Mathematical Society **357** (2005), 1877–1899, DOI: 10.1090/S0002-9947-04-03496-8. Lawful open text: https://www.math.miami.edu/~wachs/papers/fibers.pdf. Especially §§6 and 8.
2. J. Shareshian and M. L. Wachs, *Top homology of hypergraph matching complexes, p-cycle complexes and Quillen complexes of symmetric groups*, arXiv:0808.3114, submitted 22 August 2008. https://arxiv.org/abs/0808.3114.
3. M. Bate, B. Everitt, S. Ford and E. Ramos, *Homology of matching complexes and representations of symmetric groups*, arXiv:2312.13750. https://arxiv.org/abs/2312.13750. Compared for ordinary hypergraph matching homology only.
