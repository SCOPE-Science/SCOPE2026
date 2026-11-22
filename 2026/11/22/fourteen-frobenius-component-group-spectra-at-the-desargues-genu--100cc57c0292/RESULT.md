# Fourteen Frobenius component-group spectra at the Desargues genus-eleven boundary

## Finding
Let \(k=\mathbb F_q\) have characteristic at least seven, and let \(\Gamma\) be the Desargues incidence graph: its twenty vertices are the ten two-subsets and ten three-subsets of a five-element set, with an edge whenever a two-subset lies in a three-subset. Glue twenty genus-zero components at thirty nodes according to \(\Gamma\), using all three marked branches on each component. This gives a maximally degenerate stable curve \(C_0\) of arithmetic genus eleven over \(k\). Its geometric automorphism group is \(S_5\times C_2\), where \(C_2\) complements subsets and interchanges the two bipartition classes.

There are exactly fourteen \(k\)-forms of \(C_0\), indexed by the seven cycle partitions \(\lambda\vdash5\) and a complementation flag \(\epsilon\in\{0,1\}\). Each admits a proper, regular, thickness-one semistable smoothing over \(k[[t]]\) with geometrically smooth generic fibre. For the Jacobian of **any** such smoothing, the geometric Néron component group \(\Phi(\bar k)\) and its finite-field rational subgroup \(\Phi(k)\) depend only on \((\lambda,\epsilon)\). In particular,
\[
\Phi(\bar k)\simeq \mathbb Z/4\oplus\mathbb Z/8\oplus(\mathbb Z/40)^2\oplus\mathbb Z/120.
\]
The complete fourteen-case rational component-group classification is:

| \(\lambda\) | \(\epsilon\) | \(\Phi(k)\) | \(|\Phi(k)|\) |
|---|---:|---|---:|
| \((5)\) | 0 | \(\mathbb Z/60\) | 60 |
| \((5)\) | 1 | \(\mathbb Z/10\) | 10 |
| \((4,1)\) | 0 | \(\mathbb Z/2\oplus\mathbb Z/24\) | 48 |
| \((4,1)\) | 1 | \(\mathbb Z/4\oplus\mathbb Z/8\) | 32 |
| \((3,2)\) | 0 | \(\mathbb Z/12\) | 12 |
| \((3,2)\) | 1 | \(\mathbb Z/2\) | 2 |
| \((3,1,1)\) | 0 | \(\mathbb Z/60\) | 60 |
| \((3,1,1)\) | 1 | \(\mathbb Z/10\) | 10 |
| \((2,2,1)\) | 0 | \(\mathbb Z/4\oplus\mathbb Z/8\oplus\mathbb Z/120\) | 3840 |
| \((2,2,1)\) | 1 | \(\mathbb Z/2\oplus\mathbb Z/8\oplus\mathbb Z/40\) | 640 |
| \((2,1,1,1)\) | 0 | \(\mathbb Z/4\oplus\mathbb Z/40\oplus\mathbb Z/120\) | 19200 |
| \((2,1,1,1)\) | 1 | \(\mathbb Z/2\oplus(\mathbb Z/40)^2\) | 3200 |
| \((1,1,1,1,1)\) | 0 | \(\mathbb Z/4\oplus\mathbb Z/8\oplus(\mathbb Z/40)^2\oplus\mathbb Z/120\) | 6144000 |
| \((1,1,1,1,1)\) | 1 | \((\mathbb Z/2)^2\oplus(\mathbb Z/10)^3\) | 4000 |

The numbers in the last column are the local Tamagawa numbers (numbers of rational connected components of the special fibre of the Jacobian's Néron model). The smallest, two, occurs for the complemented \((3,2)\)-twist even though the geometric component group has 6,144,000 elements.

## Assumptions and scope
All nodes are ordinary double points and all geometric irreducible components are projective lines with exactly three incident branches. A **thickness-one smoothing** means that after strict henselization at each geometric node, the completed local equation of the total space has the form \(xy=t\) multiplied by a unit; this is equivalent to regularity of the total space at the nodes. The ground field characteristic restriction is conservative and avoids exceptional small-characteristic automorphism-scheme questions. Frobenius refers to arithmetic Frobenius on the geometric graph, and \(\Phi(k)\) means fixed points under that action. The claim is not about the connected generalized Jacobian of the special fibre or arbitrary higher-thickness smoothings.

## Proof
**1. Graph and moduli point.** The bipartite graph has ten vertices of each type. A two-subset is included in exactly three three-subsets, and a three-subset contains exactly three two-subsets, so the graph is connected, cubic and has thirty edges. Its first Betti number is \(30-20+1=11\). Gluing one \(\mathbb P^1\) for every vertex along the thirty incidence edges gives a stable curve: each rational component has three distinct nodes, hence is stable, and the arithmetic genus is eleven. Every three-pointed projective line has no automorphisms fixing all three markings. Consequently any automorphism of the graph extends uniquely to the curve, and any automorphism of the stable curve induces a graph automorphism. The subgraph on two-subsets is recoverable from common-neighbor relations, which recover the line graph of the complete graph on five vertices and hence its \(S_5\) automorphism group. Complementation exchanges the two vertex classes and centralizes \(S_5\); every automorphism either preserves or exchanges the bipartition. Therefore \(\operatorname{Aut}(C_0)=S_5\times C_2\). All gluing data are defined over the ground field by choosing the marked points \(0,1,\infty\), and every graph automorphism uses a uniquely determined fractional-linear map defined over \(k\). Thus the automorphism group is the constant finite group scheme, and twists over \(k\) correspond to its fourteen conjugacy classes, since \(\operatorname{Gal}(\bar k/k)\) is procyclic.

**2. Smoothing and arithmetic action.** The deformation functor of a stable nodal curve is unobstructed, since \(\operatorname{Ext}^2\) of its cotangent complex vanishes. Its thirty node-smoothing parameters are local one-dimensional tangent tensors. For a given \(k\)-form, Frobenius permutes the corresponding geometric node directions, with semilinear scalar multipliers. On each Frobenius orbit a nonzero compatible choice exists by the finite-field Hilbert 90 theorem; setting each local deformation parameter equal to that nonzero choice times \(t\), and setting remaining global deformations compatibly, gives a deformation over \(k[[t]]\) smoothing all nodes to first order. Proper formal algebraization (the relative dualizing sheaf is ample) produces a projective family. The local thickness-one equations ensure that the total space is regular at its geometric nodes; the generic fibre is smooth and geometrically connected. Any two thickness-one smoothings of the same twisted special fibre have the same intersection graph and Frobenius action, which is all that will enter the component-group calculation.

**3. Monodromy and the fixed subgroup.** Raynaud's component-group description for a regular semistable curve identifies \(\Phi(\bar k)\) equivariantly with the graph Jacobian \(K(\Gamma)=\operatorname{Div}^0(V)/\operatorname{im}\Delta\). Write \(L\) for its twenty-by-twenty integer Laplacian, with diagonal entries three and entries minus one at incidences. Choose a sink vertex \(s\); identifying the degree-zero divisor lattice with \(\mathbb Z^{19}\) via \(e_v-e_s\) for \(v\ne s\), the graph Jacobian is the cokernel of the reduced Laplacian \(R\). For a graph automorphism \(g\), let \(P_g\) be its induced nineteen-by-nineteen matrix in this degree-zero basis, determined explicitly by \(P_g(e_v-e_s)=e_{g(v)}-e_{g(s)}\). The coinvariants have the **finite integer presentation**
\[
K(\Gamma)_{g}\simeq\operatorname{coker}\,[R\mid P_g-I_{19}].
\]
The graph's canonical monodromy pairing \(K(\Gamma)\times K(\Gamma)\to\mathbb Q/\mathbb Z\) is perfect and invariant under graph automorphisms. Thus its \(g\)-fixed subgroup is Pontryagin dual to the above coinvariant group, hence has the same abstract invariant factors. In particular it is legitimate to compute the fourteen rational group structures using Smith normal forms of these explicit rectangular integer matrices.

**4. Exact finite computation.** Index the two-subsets lexicographically first and then the three-subsets. Form \(L\) by the incidence rule; let \(g\) permute the five labels with cycle type \(\lambda\), followed by the complement map if \(\epsilon=1\). The complete self-contained matrix-construction and Smith-reduction recipe is in `verify_desargues.py` (requires Python 3.10+ and SymPy). It confirms \(\det R=6,144,000\), the invariant factors \((4,8,40,40,120)\), and the fourteen entries in the displayed table. It also checks the action on every edge, enumerates all 240 distinct \(S_5\times C_2\) graph automorphisms, and independently recomputes every group after deleting a different sink. Since Smith normal form is an exact finite algorithm over \(\mathbb Z\), these are exact integer computations, not finite-field experiments. The matrix identities in steps 1–3 reduce the infinitude of possible fields and smoothings to these fourteen exhaustive finite cases.

## Verification
Run `python verify_desargues.py` with the stated dependencies. The expected final line is `DESARGUES_14_FROBENIUS_COMPONENT_GROUPS_OK`. Independent consistency checks built into the program include connectivity via the nonzero reduced determinant, full graph automorphism enumeration, incidence preservation under each action, equality of groups for two different deleted vertices, and the order of the geometric component group. The mathematical argument relies on the classical deformation and component-group theorems named in the proof, not on program output as a substitute for those theorems.

## Relationship to prior work
The Desargues configuration and its \(S_5\)-incidence graph are classical. The geometric critical group \(\mathbb Z/4\oplus\mathbb Z/8\oplus(\mathbb Z/40)^2\oplus\mathbb Z/120\) was tabulated independently of the present computation in Tamimi's dissertation (2021, Table 1.1). Baker–Rabinoff (2013) explain the graph-Jacobian/Néron-component identification and the monodromy interpretation for semistable curves, based on Raynaud's theorem. Love–Taylor (2020) provide a general arithmetic version of the component-group correspondence, not the explicit Desargues fourteen-type integral invariant-factor calculation. Earlier configuration-space work concerns fundamental groups rather than these arithmetic components. The contribution here is the **complete arithmetic fixed-group classification for every form of one natural maximally degenerate genus-eleven curve**, not the discovery of the graph or a general new theorem on component groups.

## Limitations
The table concerns thickness-one regular semistable smoothings; higher node thickness changes the monodromy pairing and can change the group. The existence argument is not a formula for a specific plane equation of every generic fibre. The finite-field twists of the stable special fibre are classified, not all arbitrary genus-eleven stable curves. Historical priority for the fourteen numerical groups has not been established by independent specialist review; a previously unindexed equivariant Smith computation could overlap. No claim about independent validation or machine-checked formal proof is made.

## References
1. M. Baker and J. Rabinoff, *The skeleton of the Jacobian, the Jacobian of the skeleton, and lifting meromorphic functions from tropical to algebraic curves*, arXiv:1308.3864v1 (first public 2013-08-18), especially Section 2.1.
2. B. Berceanu and S. Parveen, *Fundamental Group of Desargues Configuration Spaces*, arXiv:1102.1790v1 (first public 2011-02-09), for a distinct classical-geometric Desargues configuration-space setting.
3. B. Tamimi, *The Sandpile & Smith Groups of Certain Classes of Graphs*, doctoral thesis, University of Essex (2021), Table 1.1, https://repository.essex.ac.uk/33230/1/baha_tamimi_phd_thesis_05_08_2022.pdf.
4. J. Love and L. Taylor, *An arithmetic variant of Raynaud's theorem*, arXiv:2009.10284v1 (first public 2020-09-22), for the general arithmetic setting.
