# Parity gaps and fractional fort covers of heterogeneous clique bouquets

## Finding

For integers \(m\ge 2\) and \(q_1,\ldots,q_m\ge 2\), let \(B=B(q_1,\ldots,q_m)\) be the graph formed by identifying one vertex of each clique of order \(q_i+1\). Its shared vertex is the *hub* \(h\), and its disjoint outer vertex sets \(V_i\), called blades, have \(|V_i|=q_i\). Put \(Q=\sum_iq_i\), \(o=|\{i:q_i\text{ odd}\}|\), and let \(\mathbf 1_{o=m}\) be one when every blade size is odd and zero otherwise.

Write \(\operatorname{ft}(B)\) for the maximum number of pairwise disjoint forts; \(Z^*(B)\) for the minimum fractional cover of forts; and \(Z(B)\) for the standard zero forcing number. Then

\[
\boxed{\operatorname{ft}(B)=\sum_{i=1}^m\left\lfloor\frac{q_i}{2}\right\rfloor+\mathbf1_{o=m},\qquad
Z^*(B)=\frac{Q}{2},\qquad Z(B)=Q-m+1.}
\]

In particular, the additive fractional packing gap is exactly
\[
\boxed{Z^*(B)-\operatorname{ft}(B)=\frac{o}{2}-\mathbf1_{o=m}.}
\]
When all blades have size three, the gap is \(m/2-1\), so this gap is unbounded even among block graphs whose nontrivial blocks are triangles.

The complete face of optimal fractional fort covers is also explicit. Every optimum assigns zero weight to the hub; every outer vertex in a blade of size at least three has weight \(1/2\); and the two vertices in each blade of size two have weights \(t_i\) and \(1-t_i\), where \(0\le t_i\le1\). Such an assignment is optimal **if and only if**
\[
\boxed{\sum_{i:q_i=2}\min\{t_i,1-t_i\}+\frac12|\{i:q_i\ge3\}|\ge1.}
\]
In particular, the fractional optimum is unique exactly when \(m=2\) or every blade has at least three outer vertices.

## Assumptions and scope

All graphs are finite, simple, undirected and labelled. The parameters satisfy \(m\ge2\), \(q_i\ge2\). A *fort* is a nonempty set \(F\subseteq V(B)\) such that every vertex outside \(F\) has either zero or at least two neighbors in \(F\). A *minimal fort* contains no smaller fort. The fort number \(\operatorname{ft}\) is the maximum cardinality of a pairwise vertex-disjoint family of forts. The fractional zero forcing number \(Z^*\) is the optimum of
\[
\min\sum_{v\in V(B)}w_v,\qquad
w_v\ge0,\quad \sum_{v\in F}w_v\ge1\quad\text{for every minimal fort }F.
\]
The same optimum is obtained if the bounds \(w_v\le1\) are included. The ordinary zero forcing number \(Z\) uses the rule that a coloured vertex with exactly one uncoloured neighbor colours that neighbor.

## Proof

**1. Fort classification.** The minimal forts are precisely (I) all two-vertex subsets of one outer blade and (II) every set consisting of the hub together with exactly one vertex from each outer blade. This classification is known for uniformly sized windmills; the following argument records the precise structure for unequal blades.

If a fort \(F\) omits the hub, a blade containing exactly one vertex of \(F\) would have an outside vertex seeing exactly that one neighbor. Hence every populated blade contains at least two vertices, and any such blade contains a type-I fort. Minimality therefore forces \(F\) to be a type-I pair. If \(F\) includes the hub, every blade must contain at least one vertex of \(F\), since otherwise its outer vertices would each see just the hub. Conversely, any choice of the hub and one vertex per blade is a fort: every remaining outer vertex sees its chosen blade vertex and the hub. It is minimal, because removing the hub leaves singleton blade intersections, and removing any selected blade vertex leaves unchosen vertices in that blade seeing just the hub. Every fort containing the hub contains one of these type-II forts. This proves the classification.

**2. Disjoint fort packing.** Every family of disjoint forts can be replaced by one of minimal forts, without decreasing its cardinality. If it contains no type-II fort, its type-I pairs lie independently within each blade, so its maximum size is \(\sum_i\lfloor q_i/2\rfloor\). If it contains a type-II fort, it contains exactly one (all type-II forts share the hub), uses one vertex in each blade, and accommodates at most \(1+\sum_i\lfloor(q_i-1)/2\rfloor\) forts. Both bounds are attained by disjoint pairings. The difference between the second bound and the first is \(1-|\{i:q_i\text{ even}\}|\); the second is strictly larger exactly when all blade sizes are odd. Thus the stated formula for \(\operatorname{ft}(B)\) follows.

**3. Fractional optimum.** The type-I constraints in a blade \(V_i\) are \(w_u+w_v\ge1\) for every distinct \(u,v\in V_i\). Summing gives \(\sum_{v\in V_i}w_v\ge q_i/2\). If \(q_i\ge3\), equality forces all vertex weights to equal \(1/2\): it is equality in every pair constraint, and three distinct vertices then determine their weights. If \(q_i=2\), equality permits precisely the pair \((t_i,1-t_i)\) with \(0\le t_i\le1\).

Adding the blade bounds yields total weight at least \(Q/2\), because the hub weight is nonnegative. The assignment \(w_h=0\) and \(w_v=1/2\) for all other vertices attains this bound and covers each type-II fort, whose weight is \(m/2\ge1\). Therefore \(Z^*(B)=Q/2\), and all optimal assignments must have hub weight zero and attain equality on every blade. For such assignments, the least weight of a type-II fort is exactly \(\sum_{q_i=2}\min(t_i,1-t_i)+|\{i:q_i\ge3\}|/2\). Requiring this number to be at least one is both necessary and sufficient. If \(m=2\), equality requires every available two-vertex blade to split weights equally. If \(m\ge3\) and there is a two-vertex blade, all half weights are feasible with slack in the type-II constraint, so some two-vertex blade weights can be varied continuously. This establishes the entire optimal face and uniqueness criterion.

**4. Ordinary zero forcing.** A set is zero forcing if and only if it meets every minimal fort: if the forcing process stalls before completion, the remaining uncoloured vertices form a fort; conversely a disjoint fort cannot be entered by a force. To meet all type-I pairs, a set contains at least \(q_i-1\) vertices of each blade. If precisely these are selected and the hub is omitted, the omitted hub and one omitted vertex of each blade form a disjoint type-II fort. Hence at least one more vertex must be selected. Choosing the hub together with \(q_i-1\) arbitrary vertices in every blade meets all minimal forts (equivalently, each remaining outer vertex is immediately forced). Thus \(Z(B)=Q-m+1\).

Combining the packing and fractional formulas gives the claimed parity gap and all corollaries.

## Verification

The accompanying standard-library script `verify.py` independently builds each graph's adjacency list from edges, enumerates *all* forts and filters inclusion-minimal ones, computes the maximum number of pairwise disjoint minimal forts by recursion, and tests the stated minimal-fort classification and exact fort-packing formula. It checks fractional feasibility of uniform half weights and independently compares sampled optimal-face assignments with all minimal-fort constraints. The direct enumeration passes all 66 ordered profiles with two to four blades, blade sizes in \(\{2,3,4\}\), and \(\sum_iq_i\le11\), yielding `VERIFY_OK`. The infinite statements and complete optimizer-face characterization follow from the proof, not from these samples.

Reproduce using `python3 verify.py`; no third-party packages are required.

## Relationship to prior work

Cameron, Hogben, Kenter, Mojallal and Schuerger introduced the fort number, fort hypergraph and fractional zero forcing through packing/covering programs. Becker, Cameron, Hanely, Ong and Previte gave the windmill minimal-fort classification and its count for uniform blades; the supporting classification above is **not claimed original in the uniform case**. Abiad and Ghasemi Nezhad established an abundance bound for minimal forts in arbitrary block graphs. The present specific contribution is the exact simultaneous fort-packing and fractional-cover evaluation, the complete optimizer face for unequal blades, and the unbounded parity-controlled additive gap for the bouquet class.

## Limitations

The theorem concerns a single common hub joining disjoint clique blades with at least two outer vertices each, not arbitrary block graphs or Cartesian graph products. It does not give an efficient method for arbitrary graphs. The minimal-fort structure for uniform windmills is prior work. Literature-priority conclusions for the new packing and fractional optimizer formulas are provisional pending independent review; computational comparisons are finite and do not establish an infinite claim.

## References

1. T. R. Cameron, L. Hogben, F. H. J. Kenter, S. A. Mojallal and H. Schuerger, *Forts, (fractional) zero forcing, and Cartesian products of graphs*, arXiv:2310.17904 (first public 2023-10-27), https://arxiv.org/abs/2310.17904.
2. P. Becker, T. R. Cameron, D. Hanely, B. Ong and J. P. Previte, *On the Number of Minimal Forts of a Graph*, arXiv:2404.05963 (first public 2024-04-09), especially the windmill section and Corollary 28, https://arxiv.org/abs/2404.05963.
3. A. Abiad and S. Ghasemi Nezhad, *Fort Abundance in Zero Forcing*, arXiv:2609.11754 (first public 2026-09-10), https://arxiv.org/abs/2609.11754.
