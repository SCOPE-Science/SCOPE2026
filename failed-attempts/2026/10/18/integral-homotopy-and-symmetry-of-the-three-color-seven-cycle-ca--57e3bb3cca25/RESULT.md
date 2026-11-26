# Integral homotopy and symmetry of the three-color seven-cycle categorical product

## Finding
Let \(G=C_7\times K_3\) be the categorical (tensor) product of the seven-cycle with the complete graph on three colors, and let \(X=\operatorname{Ind}(G)\) be its **ordinary** independence complex. Then
\[
X\simeq S^3\vee\bigvee^3 S^4.
\]
In particular \(\widetilde H_3(X;\mathbb Z)\cong\mathbb Z\), \(\widetilde H_4(X;\mathbb Z)\cong\mathbb Z^3\), and all other reduced integral homology vanishes; there is no torsion. This is an exact **finite** instance of the torsion-freeness problem of Antolín Camarena and Carnero Bravo.

There is further natural equivariant information. The dihedral group \(D_7\) rotates and reflects the cycle rows, while \(S_3\) permutes the colors. Their product acts on \(X\), and its rational homology modules are
\[
\widetilde H_3(X;\mathbb Q)\cong\varepsilon_{D_7}\boxtimes\operatorname{sgn}_{S_3},\qquad
\widetilde H_4(X;\mathbb Q)\cong\mathbf1_{D_7}\boxtimes(\operatorname{sgn}_{S_3}\oplus\operatorname{Std}_{S_3}).
\]
Here \(\varepsilon_{D_7}\) is trivial on rotations and negative on reflections; \(\operatorname{Std}_{S_3}\) is the two-dimensional permutation-augmentation representation. Thus \(D_7\) acts trivially on degree-four rational homology, whereas each reflection acts by negation in degree three. Neither positive-degree homology representation has any global invariant vectors.

## Assumptions and scope
The vertex set is \(\{(r,c):0\le r<7,\ 0\le c<3\}\). Two distinct vertices \((r,c)\), \((s,d)\) are adjacent **if and only if** \(s-r\equiv1\) or \(-1\pmod7\), and \(c\ne d\). Thus this is not the Cartesian or strong product. An independent set is any vertex subset containing no graph edge, not necessarily a maximal independent set. For computation index \((r,c)\) by \(v=3r+c\), and orient all simplices by increasing index. All chain groups and boundary calculations below are integral.

## Proof
**Exhaustive finite simplicial model.** The verifier `check.py` enumerates all independent subsets by deciding each of the 21 vertices in order. The face counts by dimension \(-1,0,1,\ldots,8\), including the empty face, are
\[
(1,21,168,658,1365,1554,1022,402,84,7),
\]
for 5,282 augmented faces. Each candidate set is generated exactly once, with adjacency exclusion checked at the point of inclusion; the enumeration is exhaustive rather than sampled.

**Complete acyclic matching.** Starting with augmented faces, inspect vertices color-first, then cyclic-row order. At a vertex \(v\), match each currently unmatched face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) if both are present and currently unmatched. Remove both and continue. The empty-face pair is omitted from the resulting *nonaugmented* matching; this restores one critical vertex. The resulting 2,638 nonempty matching pairs leave exactly one critical vertex, one critical three-cell and three critical four-cells. An explicit directed-Hasse topological sort verifies acyclicity over all 25,221 nonempty codimension-one incidences: a matched incidence is directed upward and every unmatched incidence downward. Hence Forman's theorem gives a homotopy-equivalent CW complex consisting precisely of those five cells.

**Integral attaching maps.** Let \(\tau\) be the single critical three-simplex. Define an integral coefficient projection \(P\) on oriented three-simplices by \(P(\tau)=1\), by zero on any three-simplex that is the upper member of a Morse pair, and on each three-simplex \(\sigma\) paired upward with a four-simplex \(\eta\) by the exact signed recurrence
\[
P(\sigma)=-[\eta:\sigma]\sum_{\substack{\sigma'\subset\eta\\ \dim\sigma'=3,\ \sigma'\ne\sigma}}[\eta:\sigma']P(\sigma').
\]
Each incidence \([\eta:\sigma]\) is \(+1\) or \(-1\). The verified acyclic matching makes every recurrence terminate. Direct integer evaluation shows \(P(\partial\eta)=0\) **for all 1,554 original four-simplices**, in particular for each of the three critical four-cells. Thus the full integral cellular differential from dimension four to dimension three is the zero \(1\times3\) matrix.

The critical CW complex has no positive-dimensional cells below dimension three, so its three-skeleton is \(S^3\). Its three four-cell attaching maps belong to \(\pi_3(S^3)\cong\mathbb Z\); their degrees are exactly their integral cellular boundary coefficients, which all vanish. Hence all attaching maps are nullhomotopic and the asserted integral wedge decomposition follows. This upgrades the previously published nonzero free homology observation to a complete integral homotopy type.

**Symmetry characters.** The verifier lifts the critical three-cell to an explicit simplicial integral three-cycle \(z\) supported on 16 simplices, satisfying \(\partial z=0\) and \(P(z)=1\). For every element \(g\) of \(D_7\times S_3\), its signed simplicial action preserves the graph; therefore the induced degree-three scalar is exactly \(P(gz)\in\{\pm1\}\). Enumeration of all 84 distinct pairs of group elements confirms
\[
\chi_3(g)=\varepsilon_{D_7}(g)\operatorname{sgn}_{S_3}(g).
\]
Independently, for each of the 84 actions the signed simplicial fixed-face formula computes the reduced Lefschetz number \(L(g)=\sum_i(-1)^i\chi_i(g)\). As the integral homotopy calculation leaves homology only in degrees three and four, \(L(g)=-\chi_3(g)+\chi_4(g)\). The exact resulting character is
\[
\chi_4(g)=\operatorname{sgn}_{S_3}(g)+\bigl(\#\operatorname{Fix}_{\{0,1,2\}}(g)-1\bigr),
\]
independent of the dihedral component. This is the sum of the sign and standard characters of \(S_3\); over characteristic zero the character determines the stated rational modules. The group-character average is zero in both degrees, establishing the invariant-subspace statement.

## Verification
Run `python3 check.py` using Python 3 with its standard library only. The full verifier reads no external databases and checks the face enumeration, matching-pair counts, all directed-Hasse incidences, exact integer projections, every four-simplex's cochain vanishing, the lifted cycle's exact boundary, and all 84 natural automorphism actions and characters. Successful output is embedded as `check_output.txt` and ends with `VERIFIED`. The program itself is the reproducible exhaustive certificate for the computational steps, not evidence of independent review.

## Relationship to prior work
O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401 (first posted 2023-07-23), prove general connectivity and possible homology degree restrictions for \(C_{3r+1}\times K_n\) in Theorem 23. Their passage immediately before Question 24 **explicitly names \(C_7\times K_3\)** among examples with nonzero free homology in two adjacent dimensions. That observation, and the general possible wedge-plus-Moore-space form, are established prior work. Their Question 24 asks whether all such homology groups are torsion-free. The paper does **not** supply this precise integral wedge decomposition, three-sphere multiplicity, or \(D_7\times S_3\) symmetry character.

The published finding *A torsion-free mixed-dimensional sphere wedge for the seven-cycle categorical product with four colors* computes the distinct **four-color** graph \(C_7\times K_4\) and reports three degree-three and six degree-four spheres. Its result for four colors does not imply the three-color result by the change of parameter, since independence complexes under adding or deleting colors have nontrivial inclusion behavior. The four-color full `RESULT.md` was inspected. Other earlier categorical-product classifications treat complete-graph products or cycles of lengths divisible by three; they do not establish the present symmetry-refined exact three-color statement. This comparison is not a proof that equivalent unindexed work does not exist.

## Limitations
This is a finite computational proof for exactly seven rows and three colors, not a torsion-freeness theorem for all \(C_k\times K_n\). The actual verified group action is the indicated natural 84-element subgroup; no assertion of the full automorphism group is needed. No independent mathematical audit has occurred. Published or unindexed equivalent work may exist; computation and indexed searches cannot logically establish global novelty.

## References
- O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401 (first public 2023-07-23), especially Theorem 23 and Question 24. https://arxiv.org/html/2307.12401v2
- *A torsion-free mixed-dimensional sphere wedge for the seven-cycle categorical product with four colors*, published mathematical research record (2026); a full-text scientific comparison was made. https://github.com/published-finding corpus/2026
- S. Goyal, S. Shukla and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926 (2019). https://arxiv.org/abs/1905.06926
