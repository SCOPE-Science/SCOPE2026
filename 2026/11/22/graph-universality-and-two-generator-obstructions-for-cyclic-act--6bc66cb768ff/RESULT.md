# Graph universality and two-generator obstructions for cyclic-action packet bounds

## Finding

Let \(G=C_N\) act on a finite set \(X\). For each **distinct** stabilizer subgroup \(H\) occurring in \(X\), put \(d_H=[G:H]\), and form a graph \(P_X\) whose vertices are the indices \(d_H>1\), with an edge between distinct vertices \(d,e\) exactly when \(\gcd(d,e)>1\). Define \(\chi(\varnothing)=0\).

For the packet invariant \(\lambda_G^{\min}(X)\) introduced for minimal base generators of equivariant automorphisms in Lara-Gómez, Romero-Rosales and Ruiz-Medina, the exact identity is

\[
\lambda_G^{\min}(X)=\chi(P_X).
\]

**Universality with a fixed generator rank:** For every finite simple graph \(\Gamma\) with at least one vertex there are a finite **squarefree-order cyclic group** \(G\) and a finite \(G\)-set \(X\), with precisely one orbit of each stabilizer type, such that \(P_X\cong\Gamma\). In this construction,

\[
\operatorname{rank}\operatorname{Aut}_G(X)=
\begin{cases}
1,&E(\Gamma)=\varnothing,\\
2,&E(\Gamma)\ne\varnothing.
\end{cases}
\]

Consequently \(\lambda_G^{\min}(X)\) is arbitrarily larger than the actual minimum number of generators of \(\operatorname{Aut}_G(X)\), even when that group is abelian and two-generated.

In the **succinct orbit-index encoding** of a cyclic action (binary \(N\) and the list of distinct nontrivial divisors \(d_1,\ldots,d_r\mid N\), with one orbit for each), deciding whether \(\lambda_G^{\min}(X)\le3\) is NP-complete. The hardness persists for squarefree \(N\) and two-generated \(\operatorname{Aut}_G(X)\). This complexity assertion does **not** concern the much larger explicit permutation-table encoding of \(X\).

## Assumptions and scope

All groups and sets are finite. \(C_N\) denotes a cyclic group of order \(N\). A stabilizer type means one distinct subgroup, rather than one orbit: repeated orbits of the same type contribute only one vertex. By convention the empty graph has chromatic number zero. The packet invariant is **not** the actual rank of the automorphism group: it minimizes the number of packets of a fixed collection of base generators, where each packet has distinct subgroup types and pairwise coprime element orders. The invariant as defined in the cited paper can depend on chosen minimal quotient generating sets in general, but it does not here, since every nontrivial cyclic quotient has a one-element minimal generating set and all its generators have the same order.

## Proof

### 1. Exact packet/chromatic correspondence

For cyclic \(G\), every subgroup is normal, and its normalizer quotient \(N_G(H)/H=G/H\) is cyclic of order \(d_H\). Thus the base-generating construction has exactly one nontrivial base generator \(\eta_H\) for each type with \(d_H>1\), of order \(d_H\). Two different such generators act on different boxes, so they commute. Since there is only one generator of each type, the one-generator-per-box condition is automatic. The remaining packet condition is precisely \(\gcd(d_H,d_K)=1\) for all distinct members of a packet. Packets are therefore the independent sets of \(P_X\). Partitioning the generators into the fewest packets is equivalent, in both directions, to a proper coloring of \(P_X\) with the fewest colors. This proves the displayed equality, including the empty case.

### 2. Every graph arises from cyclic action indices

Let \(\Gamma=(V,E)\) be a finite simple graph with \(V=\{1,\ldots,r\}\) and \(r\ge1\). Choose mutually distinct primes \(q_v\) indexed by the vertices and \(p_e\) indexed by the edges. Define

\[
N=\prod_{v\in V}q_v\prod_{e\in E}p_e,
\qquad d_v=q_v\prod_{e\ni v}p_e.
\]

The integer \(N\) is squarefree; every \(d_v\) is a nontrivial divisor of \(N\); and the private factor \(q_v\) makes all \(d_v\) distinct. For \(v\ne w\), the prime sets of \(d_v\) and \(d_w\) intersect exactly when \(\{v,w\}\in E\). In fact their gcd is \(p_{\{v,w\}}\) for an edge, and one otherwise.

Take \(G=C_N\), let \(H_v\le G\) be its unique subgroup of index \(d_v\), and let

\[
X=\bigsqcup_{v\in V}G/H_v.
\]

The stabilizer types are pairwise different, each with one orbit, and \(P_X\cong\Gamma\). Part 1 gives \(\lambda_G^{\min}(X)=\chi(\Gamma)\).

### 3. The actual group rank is at most two

An equivariant automorphism preserves each orbit of the just-constructed \(X\), because nonisomorphic transitive cyclic \(G\)-sets have distinct stabilizers. Right translation on each orbit gives

\[
\operatorname{Aut}_G(X)\cong\prod_{v\in V}C_{d_v}.
\]

The least number of generators of a finite abelian group is the maximum of the minimum generator numbers of its Sylow subgroups. Here every private prime \(q_v\) occurs in precisely one factor, whereas every edge prime \(p_e\) occurs in precisely two factors. Since all factors are squarefree, the corresponding Sylow subgroup is \(C_p\) or \(C_p^2\), respectively. Therefore the group rank equals one when \(E\) is empty and two otherwise. Taking \(\Gamma=K_r\) for arbitrarily large \(r\) gives \(\lambda_G^{\min}(X)=r\), while the actual group rank is two, establishing an unbounded additive and multiplicative packet surplus.

For an especially small example, three distinct orbit indices \(6,10,15\) in \(C_{30}\) give packet number three, but

\[
\operatorname{Aut}_{C_{30}}(X)\cong C_6\times C_{10}\times C_{15}\cong C_{30}^2.
\]

Indeed the two elements \((1,2,0)\) and \((0,5,1)\), using additive coordinates modulo \(6,10,15\), generate the entire group.

### 4. Succinct NP-completeness

Consider inputs consisting of an integer \(N\) in binary and a list of distinct integers \(d_i>1\) in binary, with \(d_i\mid N\); they encode \(\bigsqcup_i C_N/H_i\), with \(H_i\) the unique subgroup of index \(d_i\). The decision problem \(\lambda_G^{\min}(X)\le3\) is in NP: a three-color assignment to the list is a certificate, checked by Euclidean gcd computations between every same-colored pair. No integer factorization is needed.

Reduce graph three-colorability to this problem by the construction in Part 2. The first \(|V|+|E|\) primes can be generated deterministically in polynomial time (their sizes are polynomially bounded in that number); therefore \(N\) and all \(d_v\) have total binary description of polynomial length, and they can be computed in polynomial time. Part 2 preserves the answer exactly. Three-colorability is NP-complete, so the packet decision problem is NP-hard. If necessary, append a disjoint edge to the input graph; this does not change three-colorability and guarantees a nonempty edge set, hence group rank exactly two in the output. The reduction always yields squarefree \(N\), proving the claimed restrictions. This is a many-one reduction on **succinct orbit data**; materializing the underlying \(G\)-set as a list of its points need not be polynomial-time in the length of that data.

## Verification

The independent finite checker in `verify/packet_graph_verify.py` constructs the prime-index action and computes two quantities by different algorithms: graph chromatic number by backtracking and minimum packet count by a gcd-based subset dynamic program. It checks every labelled simple graph on one through five vertices (\(1099\) graphs in total), all relevant gcd adjacencies, and the Sylow multiplicity formula. It separately checks the two explicit generators of \(C_6\times C_{10}\times C_{15}\) by generating all \(900\) elements and tests the complete-graph surplus for sizes two through eight. Run with `python3 verify/packet_graph_verify.py`; no third-party Python packages are required. The test output is provided in `verify/expected_output.txt`.

## Relationship to prior work

The July 4, 2026 preprint and November 2, 2026 journal article of Lara-Gómez, Romero-Rosales and Ruiz-Medina define the packet parameter and show that coprime-order generators from different boxes may be merged. The present result does not reprove that grouping lemma. It identifies the exact packet optimization for cyclic actions, establishes realization of arbitrary graph conflicts using **one distinct orbit per type**, proves NP-completeness in a specified finite encoding, and exhibits an unbounded gap from the true group rank. The authors' paper formulates the determination of the packet parameter as an open problem but does not give this graph realization or complexity result.

Castillo-Ramírez and Ruiz-Medina (2022/2023) determine relative rank of \(\operatorname{End}_G(X)\) modulo the units. That different invariant does not determine the number of coprime base-generator packets. Classical graph-coloring hardness, prime-support intersection representations, and the elementary finite-abelian-group rank formula are inputs, not claimed discoveries.

## Limitations

This is an exact statement about the **packet construction**, not a formula for the rank of \(\operatorname{End}_G(X)\) or a general formula for the unit-group rank in arbitrary noncyclic actions. The NP-completeness result applies to binary-index (succinct) encodings, not to an explicit-list encoding of all points of an enormous cyclic action. The finite checker tests instances rather than proving the infinite universality or complexity statements. The paper's minimal-generator choice ambiguity persists outside cyclic groups. The literature comparison cannot rule out unindexed or inaccessible equivalent claims; independent mathematical review has not occurred.

## References

1. R. H. Ruiz-Medina, V. M. Lara-Gómez, and G. Romero-Rosales, *Finite generating sets for monoids of \(G\)-equivariant functions*, arXiv:2607.04053, first posted 2026-07-04. https://arxiv.org/abs/2607.04053
2. V. M. Lara-Gómez, G. Romero-Rosales, and R. H. Ruiz-Medina, *Finite generating sets for monoids of \(G\)-equivariant functions*, *Semigroup Forum*, published online 2026-11-02, DOI:10.1007/s00233-026-10690-y. https://doi.org/10.1007/s00233-026-10690-y
3. A. Castillo-Ramírez and R. H. Ruiz-Medina, *The relative rank of the endomorphism monoid of a finite \(G\)-set*, arXiv:2203.12158 (2022), *Semigroup Forum* (2023). https://arxiv.org/abs/2203.12158
4. M. R. Garey and D. S. Johnson, *Computers and Intractability: A Guide to the Theory of NP-Completeness*, W. H. Freeman, 1979; standard NP-completeness of three-colorability.
