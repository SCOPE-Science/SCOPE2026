# Ten-coordinate controllability and the ovoid–spread exception in the Tutte–Coxeter graph

## Finding

Let \(H\) be the 30-vertex unit-edge Tutte–Coxeter graph, realized as the incidence graph between the 15 edges and the 15 perfect matchings of \(K_6\). For the continuous-time system
\[
\dot z=-L_Hz+E_Su,
\]
where each vertex in \(S\) receives its own independent coordinate input, the exact minimum actuator number is **ten**. Every controllable ten-vertex placement contains exactly five edge-type vertices and five matching-type vertices.

For a five-edge set \(P\) and a five-perfect-matching set \(Q\), define the \(15\times15\) incidence matrix \(B\) by \(B_{e,M}=1\) if \(e\in M\) and \(0\) otherwise, and put \(P^c=E(K_6)\setminus P\), \(Q^c=\mathcal M\setminus Q\). The placement \(S=P\cup Q\) is fully controllable **if and only if**

1. \(\operatorname{rank}_{\mathbb Q} B_{P^c,\mathcal M}=10\);
2. \(\operatorname{rank}_{\mathbb Q} B_{E(K_6),Q^c}=10\); and
3. it is **not** the case that \(P\) is the five-edge star at a vertex of \(K_6\) and \(Q\) is a one-factorization (five perfect matchings partitioning the 15 edges).

Exactly \(1518\) five-edge sets satisfy the first rank condition and exactly \(1518\) five-matching sets satisfy the second. There are exactly six eligible edge-stars and six eligible one-factorizations. Of the \(1518^2=2{,}304{,}324\) rank-eligible pairs, exactly \(6\cdot6=36\) fail, so the **exact number of controllable minimum-size placements** is
\[
\boxed{2{,}304{,}288}.
\]
This is a labeled count for the specified 30-vertex graph; no quotient by graph automorphisms is taken.

## Assumptions and scope

The underlying graph is **exactly** the simple unweighted Tutte–Coxeter incidence graph. All 30 state coordinates are independently accessible only at vertices included in \(S\). The input matrix \(E_S\) consists of distinct columns of the 30-dimensional identity matrix. All ranks and controllability statements are over \(\mathbb R\), equivalently \(\mathbb Q\) for the exact integer matrices used in the criterion. There are no variable conductances, no measurement constraints, and no claims about actuator energy or other generalized quadrangles.

Fix base vertices \(\{0,1,2,3,4,5\}\). The 15 edge-type vertices are all two-element subsets; the 15 matching-type vertices are all partitions into three disjoint pairs. The two types are connected precisely when the edge belongs to the matching. Both have graph degree three. A *point-star* is a collection of five edges incident to one base vertex; a *spread* is a partition of the 15 edges into five perfect matchings.

## Proof

**1. Complete spectral decomposition.** Index edge-type vertices first. Set \(T\) to be the unsigned \(6\times15\) vertex–edge incidence matrix of \(K_6\), and let \(J\) be the \(15\times15\) all-ones matrix. Two edges of \(K_6\) are contained in one common matching if they are disjoint, and each edge lies in three matchings. Directly,
\[
BB^{\mathsf T}=4I_{15}+J-T^{\mathsf T}T,
\qquad TT^{\mathsf T}=4I_6+J_6.
\]
Therefore \(BB^{\mathsf T}\) has eigenvalues \(9,4,0\) of multiplicities \(1,9,5\), respectively; in particular \(\operatorname{rank}B=10\). The graph Laplacian is
\[
L_H=\begin{pmatrix}3I_{15}&-B\\-B^{\mathsf T}&3I_{15}\end{pmatrix}.
\]
Its complete real eigenvalue/multiplicity list is
\[
(0,1),\quad(1,9),\quad(3,10),\quad(5,9),\quad(6,1).
\]
The \(3\)-eigenspace is \((\ker B^{\mathsf T},0)\oplus(0,\ker B)\), each direct summand of dimension five. The \(1\)- and \(5\)-eigenspaces are, respectively,
\[
\left\{(2v,B^{\mathsf T}v):Tv=0\right\},\qquad
\left\{(2v,-B^{\mathsf T}v):Tv=0\right\},
\]
where \(\ker T\) has dimension nine. The \(0\)- and \(6\)-eigenvectors can be taken as \((\mathbf1,\mathbf1)\) and \((\mathbf1,-\mathbf1)\).

**2. The minimum and the two separate incidence conditions.** The PBH criterion for a real symmetric matrix says that controllability with coordinate inputs in \(S\) holds exactly when restriction to \(S\) is injective on *each* eigenspace. The ten-dimensional \(3\)-eigenspace gives an immediate lower bound of ten selected vertices. More strongly, any ten-vertex controllable set must have at least five selected vertices of each type, so exactly five of each. For fixed \(P,Q\), the two \(3\)-eigenspace summands are captured precisely when their selected-coordinate restrictions are injective. Orthogonal-complement duality for the column and row spaces of \(B\) yields the two rank-ten conditions displayed in the finding. The two simple eigenvalues cause no obstruction because the corresponding eigenvectors have no zero coordinates.

**3. Counting the separately admissible five-edge sets.** Every vector in \(\ker B^{\mathsf T}\) has the form \(v_{ij}=a_i+a_j\) with \(\sum_{i=0}^5 a_i=0\). Thus the first rank condition is equivalent to the implication
\[
\bigl(a_i+a_j=0\text{ for all }ij\in P,\ \sum_i a_i=0\bigr)
\ \Longrightarrow\ a_i=0\text{ for every }i.
\]
On a bipartite connected component of the five-edge graph \((\{0,\ldots,5\},P)\), the equations have one degree of freedom, with opposite values on the bipartition classes. On a nonbipartite component an odd cycle forces all its values to zero. The final zero-sum equation eliminates the remaining degree of freedom exactly when there is only one bipartite component and its two color classes have unequal sizes (or there are no bipartite components).

For five edges on six labeled vertices, the admissible shapes and counts are: unbalanced spanning trees, \(6+\binom62\,2^3\cdot4=486\); an odd unicyclic connected component on five vertices together with one isolated vertex, \(6(12+10\cdot15)=972\); and a disjoint triangle plus a three-vertex path, \(\binom63\cdot3=60\). Their sum is \(1518\). The matching-side eligibility count \(1518\) is obtained by the dual incidence calculation, independently reproduced in the exact finite verification.

**4. The remaining mixed-eigenspace obstruction and exact census.** The restrictions for the \(1\)- and \(5\)-eigenspaces have equal rank because changing the sign of all selected matching rows leaves rank unchanged. Choose an integer basis \(v_1,\ldots,v_9\) of the rational nullspace \(\ker T\). For every candidate \((P,Q)\), form the \(10\times9\) matrix whose first five rows are the selected rows of \((2v_1\ \cdots\ 2v_9)\), and whose last five rows are the selected rows of \((B^{\mathsf T}v_1\ \cdots\ B^{\mathsf T}v_9)\). It must have rank nine.

The attached standalone `verify.py` checks this last condition exhaustively, but without redundantly testing all \(1518^2\) pairs: the natural \(S_6\) relabeling action partitions the \(1518\) admissible five-edge sets into eight complete orbits of sizes \(6,180,120,360,360,360,60,72\). For one representative of each orbit, all \(1518\) admissible matching sets are checked. The numbers passing the mixed rank test are, in the same orbit order, \(1512,1518,1518,1518,1518,1518,1518,1518\). The size-six orbit consists exactly of the six edge-stars; for its representative, exactly the six one-factorizations fail. Relabeling preserves spreads and controllability, proving that the full failure set is exactly the 36 star–spread pairs. The number of successes is
\[
6\cdot1512+(180+120+360+360+360+60+72)\cdot1518
=2{,}304{,}288.
\]
The explicit ten-vertex placement with edge indices \((0,1,2,3,5)\) and matching indices \((0,1,3,4,7)\), both zero-based in lexicographic order, passes all five PBH eigenspace tests; it also has full 30-state Kalman rank. This proves attainment of the lower bound.

## Verification

Run `python3 verify.py` with a standard Python 3 interpreter. There are no third-party packages, network calls, input files, floating-point comparisons, randomized steps or external certificates.

The script regenerates all 15 edges and 15 matchings, verifies the incidence identities, constructs an exact rational nullspace of \(T\), checks all \(\binom{15}{5}=3003\) candidate selections on each side, establishes their geometric eligibility, enumerates all 720 label permutations, checks the eight complete point-set orbits and every one of their 1518 admissible matching partners, identifies exactly the 36 exceptional combinations, and tests full 30-state reachability on positive and negative examples.

The modular rank calculations are exact over \(\mathbb Q\), not probabilistic. The prime is \(1{,}000{,}000{,}007\). Every incidence row or column has Euclidean norm \(\sqrt3\), so a nonzero ten-by-ten incidence minor has absolute determinant at most \(3^5=243\). For the integral nine-column eigenspace test matrix constructed in the script, each row has squared Euclidean norm at most 36, so a nonzero nine-by-nine minor has absolute determinant at most \(6^9=10{,}077{,}696\). Both are smaller than the prime; hence an integer determinant is zero if and only if its reduction modulo this prime is zero. Thus all decisive finite full-rank tests certify rational full rank or rational rank deficiency.

## Relationship to prior work

The PBH criterion, graph controllability through zero forcing, and maximum-eigenvalue-multiplicity bounds are established tools; they are not claimed as new. The 2011 work by Burgarth and collaborators gives zero-forcing sufficiency, and Monshizadeh, Zhang and Camlibel (2014) develop strong structural controllability for qualitative matrix classes. Yuan and collaborators (2013) give the unrestricted-input maximum-multiplicity framework. These results do not supply the fixed-Laplacian exact census of coordinate placements here.

Zhang, Camlibel and Cao (2011) treat multiple leaders on distance-regular graphs. Their general necessary diameter bound yields only \(4|S|\ge29\) on this graph, and their general constructive sufficient set has \(30-4=26\) leaders; neither determines the sharp ten-leader classification or the 36 star–spread exceptions. The earlier incidence-graph classifications for the Heawood graph and finite affine-plane graphs concern different graphs, eigenvalue multiplicities and geometric obstructions, and do not imply this 30-vertex census.

## Limitations

This is a complete result for a single canonical 30-vertex graph, not an all-order theorem for generalized quadrangles. It relies on an exact, bounded finite enumeration of mixed-eigenspace incidences, rather than a uniform purely conceptual classification of those incidences. The result does not address weighted edges, scalar inputs shared by multiple vertices, actuator failure, or control-energy optimization. Publication-priority uncertainty remains for difficult-to-discover specialist enumerations; novelty has not been independently audited.

## References

- Burgarth, D., D'Alessandro, D., Hogben, L., Severini, S. and Young, M. *Zero forcing, linear and quantum controllability for systems evolving on networks*. arXiv:1111.1475, first public 2011-11-07. https://arxiv.org/abs/1111.1475
- Zhang, S., Camlibel, M. K. and Cao, M. *Controllability of Diffusively-Coupled Multi-Agent Systems with General and Distance Regular Coupling Topologies*. CDC-ECC 2011, 759–764. https://doi.org/10.1109/CDC.2011.6160658
- Yuan, Z., Zhao, C., Di, Z., Wang, W.-X. and Lai, Y.-C. *Exact controllability of complex networks*. Nature Communications 4, 2447 (2013). https://doi.org/10.1038/ncomms3447
- Monshizadeh, N., Zhang, S. and Camlibel, M. K. *Zero forcing sets and controllability of dynamical systems defined on graphs*. arXiv:1403.4868 (2014). https://arxiv.org/abs/1403.4868
