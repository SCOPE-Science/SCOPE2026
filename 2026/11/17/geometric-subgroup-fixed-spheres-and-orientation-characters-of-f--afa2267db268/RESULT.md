# Geometric subgroup-fixed spheres and orientation characters of forest dominance complexes

## Finding
Let \(F\) be any finite undirected simple forest and \(H\leq\operatorname{Aut}(F)\) any subgroup. Form the simple orbit graph \(Q_H(F)\): its vertices are \(H\)-orbits of vertices of \(F\), and distinct orbits are adjacent exactly when an edge of \(F\) joins them. Edges inside an orbit do not give loops. Then \(Q_H(F)\) is a forest, and the following is a canonical piecewise-linear homeomorphism:
\[
|\operatorname{Dom}(F)|^H\cong_{\mathrm{PL}}|\operatorname{Dom}(Q_H(F))|.
\]
Here the **dominance complex** \(\operatorname{Dom}(G)\) is the simplicial complex of complements of dominating vertex sets, equivalently the subsets containing no entire closed neighborhood of any vertex. Let \(\nu(G)\) be the maximum matching cardinality of \(G\). The already-established nonequivariant forest theorem of Marietti and Testa gives, for every \(H\),
\[
|\operatorname{Dom}(F)|^H\simeq S^{\nu(Q_H(F))-1}\quad\text{if }\nu(Q_H(F))\geq1,
\]
and the geometric fixed space is empty if \(\nu(Q_H(F))=0\).

When \(\nu(F)\geq1\), the action on the rank-one top integral reduced homology is completely determined: for every graph automorphism \(g\),
\[
g_*\bigm|\widetilde H_{\nu(F)-1}(\operatorname{Dom}(F);\mathbb Z)
=(-1)^{\nu(F)-\nu(Q_{\langle g\rangle}(F))}\,\mathrm{id}.
\]
In particular, for the tree with one central vertex and \(m\geq2\) pendant arms each of length two, any subgroup of the natural arm-permutation group has fixed space homotopy equivalent to \(S^{o(H)-1}\), where \(o(H)\) is its number of orbits on arms. The full arm-permutation group acts on the top integral homology by the sign character.

## Assumptions and scope
Graphs are finite, simple, undirected and may be disconnected or contain isolated vertices. Groups are finite automatically, since they act faithfully on a finite vertex set; the subgroup \(H\) may be trivial. The vertices of a simplicial complex are its allowable singleton faces: isolated graph vertices of a dominance complex can be ghost vertices and do not cause exceptions. The empty graph and zero-matching case have the empty geometric realization; the augmented complex \(\{\varnothing\}\) is denoted formally by \(S^{-1}\) only in reduced-chain calculations, never as a nonempty topological space.

For every vertex \(v\), put \(N_F[v]=\{v\}\cup\{w:\{v,w\}\in E(F)\}\). The face condition is
\[
\sigma\in\operatorname{Dom}(F)\quad\Longleftrightarrow\quad N_F[v]\nsubseteq\sigma\ \text{for every }v\in V(F).
\]
Acyclicity of \(F\) is indispensable for the sphere conclusion. No conclusion is claimed about equivariant homeomorphism to a linear sphere or about integral homology of arbitrary orbit-space quotients.

## Proof
**1. Orbit quotients of forests remain forests.** It is enough to handle a connected tree \(T\), since an automorphism permutes connected components, and the orbit graph for a component orbit equals the orbit graph of a representative under its setwise stabilizer. Barycentrically subdivide the edges of \(T\). The resulting tree has a vertex fixed by the entire stabilizer: the original tree center, either an original vertex or the midpoint of its central edge. Root there. Every nonroot vertex has a unique parent, and automorphisms preserve depth and parenthood. Therefore each nonroot orbit has a unique parent orbit, of strictly smaller depth. The quotient of the subdivided tree is connected and contains no cycle. Removing midpoint-orbit vertices (and ignoring the possible terminal central midpoint) yields exactly the simple graph on orbits of original vertices, with edges induced by original edges. This is acyclic. The argument also covers reflections interchanging the endpoints of a central edge.

**2. Exact fixed-point simplicial model.** Since \(H\) permutes vertices, a barycentric point of \(|\operatorname{Dom}(F)|\) is fixed precisely when all coordinates in each \(H\)-orbit are equal. For each orbit \(O\) define its barycentric vertex \(b_O=|O|^{-1}\sum_{v\in O}e_v\). A fixed point has a unique form \(\sum_O t_O b_O\), with \(t_O\geq0\) and \(\sum_Ot_O=1\). Its support is the union of those orbits for which \(t_O>0\). For any vertex \(v\in O\), its whole closed neighborhood lies in this union exactly when the entire closed neighborhood of \(O\) in \(Q_H(F)\) is among the selected orbits. This equivalence uses transitivity on each orbit: every member of a neighboring orbit is represented in the union. Thus the allowable sets of barycenters are exactly the faces of \(\operatorname{Dom}(Q_H(F))\). Sending the vertex \(O\) to \(b_O\), extended linearly on simplices, is a bijective simplicial realization map with an affine inverse; it is a PL homeomorphism.

**3. Homotopy of all subgroup-fixed spaces.** The orbit graph is a forest by Step 1. Ehrenborg and Hetyei established that its dominance complex is homotopy equivalent to a sphere; Marietti and Testa strengthened this to the dimension determined by its maximum matching number (their Proposition 4.11 together with their matching-number identification). Hence the sphere and empty alternatives follow from Step 2. This step applies a known theorem; the sphere calculation is not asserted to be a new nonequivariant result.

**4. Integral orientation.** Write \(d=\nu(F)-1\) and assume \(\nu(F)\geq1\). The known forest theorem implies \(\widetilde H_d(\operatorname{Dom}(F);\mathbb Z)\cong\mathbb Z\), with all other reduced homology zero. For an automorphism \(g\), the reduced Lefschetz number equals the reduced Euler characteristic of the geometric fixed set, by passage to a compatible barycentric subdivision. Step 3 gives \((-1)^{\nu(Q_{\langle g\rangle}(F))-1}\), interpreting the empty realization as reduced Euler characteristic \(-1\). On the other hand, Lefschetz is \((-1)^d\) times the integer degree on that rank-one homology group. Equating these gives the displayed orientation sign. A matching in the orbit forest lifts to a matching of \(F\), so \(\nu(Q_{\langle g\rangle}(F))\leq\nu(F)\); the exponent is nonnegative.

**5. Two-edge-arm trees.** Let \(T_m\) have vertices \(z,a_i,b_i\) and edges \(za_i,a_ib_i\) for \(1\leq i\leq m\). Each arm contributes a disjoint edge to a maximum matching, so \(\nu(T_m)=m\). If \(H\leq S_m\) has \(o(H)\) arm orbits, the orbit tree is \(T_{o(H)}\), with matching number \(o(H)\), proving the fixed-sphere profile. For a permutation \(g\) with \(c(g)\) cycles, its degree is \((-1)^{m-c(g)}\), exactly the sign of the permutation. This produces a uniform integral character, not merely a rational character calculation.

## Verification
The included standalone Python verifier constructs all unlabeled forests on at most six vertices from a graph atlas, computes all graph automorphisms, and tests trivial, cyclic, selected two-generator and full automorphism subgroups. For each action it compares the complete set of invariant dominance faces against the proposed orbit-forest dominance complex, verifies the quotient is a forest, computes reduced mod-two homology from augmented chain boundaries, and checks signed chain traces against the claimed orientation formula. In this finite range it checked \(42\) forests, \(921\) subgroup actions (including \(151\) noncyclic cases), \(10{,}450\) orbit-face subsets, \(1{,}301\) automorphism Lefschetz traces, and \(963\) chain-homology instances. Symmetric two-edge-arm trees with two through five arms were checked separately. Run `python verify_dominance_forest.py` with NetworkX installed. The recorded output ends in `DOMINANCE_FOREST_ORBIT_EQUIVALENCE_PASS`. These are finite checks, not a proof of the universal assertion.

## Relationship to prior work
Ehrenborg and Hetyei, *The topology of the independence complex* (available online 2005-11-28), Theorem 7.1, prove the nonequivariant dominance complex of a forest is homotopy equivalent to a sphere; they do not determine all subgroup-fixed spaces. Marietti and Testa, *A uniform approach to complexes arising from forests* (2008), Proposition 4.11, determine its sphere dimension via the matching number; the original paper is explicitly credited. The new statement is the arbitrary-subgroup fixed-space identification with another forest dominance complex and the derived complete integral automorphism orientation character. Fixed-space profiles for dissociation or independence complexes of trees concern different simplicial constructions and cannot imply the claim without an additional unproved comparison.

## Limitations
The result is restricted to finite forests and their vertex automorphism groups. The explicit PL identification does not give an equivariant linear-sphere structure or the full homotopy type of an arbitrary group quotient. The underlying nonequivariant homotopy theorem and matching-number dimension are preexisting. Equivalent observations might occur in unindexed equivariant graph-complex literature; independent mathematical and publication-priority evaluation have not been carried out.

## References
1. R. Ehrenborg and G. Hetyei, *The topology of the independence complex*, European Journal of Combinatorics 27 (2006), 906–923; available online 2005-11-28. DOI: 10.1016/j.ejc.2005.04.010. Author-hosted full text: https://www.ms.uky.edu/~jrge/Papers/Independence.pdf .
2. M. Marietti and D. Testa, *A uniform approach to complexes arising from forests*, Electronic Journal of Combinatorics 15 (2008), R101, published 2008-08-04. DOI: 10.37236/825. Full text: https://www.kurims.kyoto-u.ac.jp/EMIS/journals/EJC/Volume_15/PDF/v15i1r101.pdf .
