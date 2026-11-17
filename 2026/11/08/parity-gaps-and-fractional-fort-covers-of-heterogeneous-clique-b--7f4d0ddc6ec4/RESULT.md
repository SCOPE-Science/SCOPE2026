# Parity gaps and fractional fort covers of heterogeneous clique bouquets

## Finding

For integers \(m\ge2\) and \(q_1,\ldots,q_m\ge2\), let \(B(q_1,\ldots,q_m)\) be the simple graph made by identifying one common hub \(h\) in \(m\) cliques of orders \(q_i+1\). Each outer blade \(V_i\) has exactly \(q_i\) vertices. Put \(Q=\sum_iq_i\), \(o=|\{i:q_i\text{ odd}\}|\), and let \(\mathbf1_{o=m}\) indicate that all blades have odd size. Then the maximum number \(\operatorname{ft}(B)\) of pairwise disjoint forts, the minimum fractional fort-cover weight \(Z^*(B)\), and the ordinary zero-forcing number are
\[
\boxed{\operatorname{ft}(B)=\sum_{i=1}^m\lfloor q_i/2\rfloor+\mathbf1_{o=m},\qquad Z^*(B)=Q/2,\qquad Z(B)=Q-m+1.}
\]
In particular,
\[
\boxed{Z^*(B)-\operatorname{ft}(B)=o/2-\mathbf1_{o=m}.}
\]
For \(q_i=3\) for every \(i\), the gap is \(m/2-1\) and grows without bound. **These blocks are \(K_4\), not triangles.** For a bouquet of triangles, \(q_i=2\) for every \(i\), and this gap is exactly zero. No unbounded-gap assertion is made for triangle bouquets.

The complete face of optimal fractional covers is as follows. Every optimum has \(w_h=0\); every vertex on a blade with \(q_i\ge3\) has weight \(1/2\); and the two weights on each size-two blade are \(t_i,1-t_i\) with \(0\le t_i\le1\). These weights constitute an optimum if and only if
\[
\boxed{\sum_{i:q_i=2}\min\{t_i,1-t_i\}+\frac12|\{i:q_i\ge3\}|\ge1.}
\]
The fractional optimum is unique exactly when \(m=2\) or all blade sizes are at least three.

## Assumptions and scope

All graphs are finite, simple, undirected and labelled; \(m\ge2\), \(q_i\ge2\). A fort is a nonempty vertex set \(F\) such that every vertex outside \(F\) has either zero or at least two neighbors in \(F\). A minimal fort contains no proper subfort. The fort-packing number is the maximum count of pairwise vertex-disjoint forts. The fractional cover minimizes \(\sum_vw_v\), subject to \(w_v\ge0\) and \(\sum_{v\in F}w_v\ge1\) for every minimal fort. These definitions are distinct from the ordinary zero-forcing parameter. Weights may be taken at most one without changing the optimum.

## Proof

**Minimal forts.** If a fort omits the hub, every blade it meets must contain at least two fort vertices: otherwise an outside vertex of that blade has exactly one fort neighbor. Every such fort contains a pair of outer vertices of a single blade, which is itself a fort. Thus minimal hub-free forts are precisely the pairs in a single \(V_i\). If a fort contains the hub, it must meet each blade, since an unselected blade vertex would otherwise have the hub as its sole fort neighbor. Conversely the hub plus exactly one outer vertex from each blade is a fort, and none of these selected vertices can be removed without destroying that property. Every hub-containing fort contains one of these. This exhausts the minimal forts.

**Packing.** Replacing each member of a disjoint fort family by one of its minimal subforts preserves the family size. With no hub fort, the maximum count is \(\sum_i\lfloor q_i/2\rfloor\), obtained by independently pairing each blade. With one hub fort (there cannot be two), the count is at most, and can attain, \(1+\sum_i\lfloor(q_i-1)/2\rfloor\). The latter exceeds the former only if every \(q_i\) is odd. Their maximum gives the displayed packing formula.

**Fractional cover and its complete optimizer face.** Every blade has pair constraints \(w_u+w_v\ge1\) for all distinct outer vertices \(u,v\); summing them yields \(\sum_{v\in V_i}w_v\ge q_i/2\). The total objective is consequently at least \(Q/2\). Weights \(1/2\) on every outer vertex and zero on the hub attain this lower bound; every hub fort contains at least \(m\ge2\) outer vertices, so its constraint is satisfied. In any optimum the hub weight must vanish and each blade sum must equal \(q_i/2\). For \(q_i\ge3\), equality in the summed pair inequalities forces every blade weight to equal \(1/2\); for \(q_i=2\), it forces the two weights to be \(t_i,1-t_i\). The smallest weight of a hub-type minimal fort over choices of one vertex from each blade is the boxed left-hand expression, so imposing that it be at least one exactly characterizes the face. For \(m=2\), any size-two blade is forced to split equally to satisfy this constraint; when \(m\ge3\), a size-two blade admits a nonconstant perturbation about \(t_i=1/2\). This proves the uniqueness criterion.

**Ordinary zero forcing.** A blue set forces the entire graph if and only if it hits every minimal fort: the remaining white vertices of any stalled process form a fort, while a disjoint fort can never be penetrated by a force. To meet all outer pairs, at least \(q_i-1\) vertices must be chosen from each blade. Choosing exactly this many while omitting the hub leaves a hub fort disjoint from the blue set, so one additional vertex is essential. The hub and \(q_i-1\) outer vertices from each blade form a forcing set of size \(Q-m+1\), proving the formula.

The gap and the corrected \(K_4\)/triangle consequences now follow directly. A triangle blade has two outer vertices (\(q_i=2\)); a size-three outer blade is a \(K_4\) block. This distinction is essential to the stated structural example.

## Verification

A direct adjacency-based, all-forts enumeration independently checked the minimal-fort classification and disjoint-packing formula for the six profiles \((2,2),(3,3),(2,3,3),(3,3,3),(2,2,2),(3,2,4)\). It also explicitly confirmed zero fractional packing gap on bouquets of triangles. The original supplied `verify.py` reports 66 checked ordered profiles with two to four blades, sizes in \(\{2,3,4\}\) and at most 11 outer vertices. Both finite checks corroborate but do not replace the unrestricted proof.

## Relationship to prior work and limitations

Cameron, Hogben, Kenter, Mojallal and Schuerger introduced the fort-hypergraph packing and fractional-cover framework (arXiv:2310.17904). Becker, Cameron, Hanely, Ong and Previte classified minimal forts of uniform windmills (arXiv:2404.05963); this already-known classification is not claimed original. Abiad and Ghasemi Nezhad studied minimal-fort abundance on block graphs (arXiv:2609.11754). The specific contribution assessed here is the simultaneous exact packing/cover formulas, optimizer-face classification, and unbounded parity gap for **\(K_4\)-block** bouquets and their heterogeneous extensions. No corresponding unbounded gap for triangle blocks is claimed. Historical priority beyond inspected sources is not certified; computations cover only finite instances. The formulas are limited to one-hub clique bouquets, not arbitrary block graphs.
