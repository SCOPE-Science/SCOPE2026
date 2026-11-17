# Complete subgroup orbit homotopy types for the pentagonal wheel's two-particle cubical complex

## Finding
Let \(W=K_1*C_5\) be the six-vertex pentagonal wheel. Its hub is \(0\); its rim vertices are \(1,\ldots,5\), with rim indices taken modulo five. Let \(D=\mathrm{UD}_2(W)\) be the finite cubical complex of unordered pairs of disjoint *closed* cells of \(W\): a cubical cell is an unordered pair of graph vertices or edges whose endpoint sets are disjoint. The dihedral graph automorphism group \(G=D_5\), of order ten, acts on \(D\) by fixing the hub and permuting rim labels.

For **every** subgroup \(H\leq G\), its ordinary geometric quotient has the following integral homotopy type, determined solely by the conjugacy class of \(H\):

| Subgroup conjugacy type | Homotopy type of \(|D|/H\) |
|---|---|
| \(\{1\}\) | \(\bigvee^6 S^1\) |
| \(C_5\) (rim rotations) | \(\bigvee^2 S^1\) |
| \(C_2\) (any rim reflection) | \(\bigvee^2 S^1\) |
| \(D_5\) (all rim symmetries) | A point |

In particular every quotient has torsion-free integral homology and free fundamental group, and the full-symmetry quotient is contractible. This is a statement about the compact cubical graph-configuration complex and its ordinary, **not homotopy-orbit**, quotient.

## Assumptions and scope
The wheel has the ten edges \(\{0,i\}\) and \(\{i,i+1\}\) for \(1\leq i\leq5\), with \(6=1\). Two closed cells are disjoint if their endpoint sets are disjoint; distinct graph vertices count as disjoint. The cell-pair is unordered. The group element \((s,t)\), with \(s\in\mathbb Z/5\), \(t\in\{1,-1\}\), sends the rim index \(i-1\) to \(s+t(i-1)\) modulo five and fixes the hub. The four listed subgroups represent all subgroup conjugacy classes because the only possible subgroup orders are \(1,2,5,10\), with five conjugate reflection subgroups.

No identification with a configuration space on a different graph, any higher-particle space, or any claim about uniform wheel sizes is needed.

## Proof
First enumerate the cubical face poset \(P\). Its dimension-zero elements are all \(\binom62=15\) vertex pairs; its dimension-one elements are all vertex–nonincident-edge pairs (40); its dimension-two elements are all disjoint edge pairs (20). For every cell, its codimension-one faces are obtained by replacing one edge by either endpoint, giving a finite regular cubical complex. Every nonempty strict chain \(c_0<\cdots<c_r\) of cells determines a barycentric simplex. Since dimensions strictly increase, every simplex has length at most three.

For a subgroup \(H\), take the *orbits of the entire chains*, not merely the chains of orbit-cell labels. This distinction retains all multiplicities and stabilizer effects. The group preserves dimension, and an element fixing a simplex setwise fixes every member of its dimension-distinguished vertex set. Thus the quotient of the barycentric subdivision is a genuine finite \(\Delta\)-complex whose open simplices are chain orbits and whose face maps are induced by deleting chain entries. Its realization is exactly \(|D|/H\).

The exhaustive orbit enumerations, independently checked by Burnside fixed-chain counting, give these simplex counts (dimensions zero, one, two):

| \(H\) | Chain-orbit simplex counts | Free-face removals in dimension two | Remaining one-dimensional cells after all collapses |
|---|---|---:|---|
| \(\{1\}\) | \((75,240,160)\) | 160 | \((23,28)\) |
| \(C_5\) | \((15,48,32)\) | 32 | \((7,8)\) |
| \(C_2\) | \((41,122,80)\) | 80 | \((11,12)\) |
| \(D_5\) | \((11,26,16)\) | 16 | \((1,0)\) |

The complete elementary-collapse certificate is reproducible from the attached `verify.py`. For dimensions two, then one, it selects the first boundary simplex incident to precisely one surviving top-dimensional simplex and removes this face–coface pair. The program constructs the complete orbit-flag incidence maps before collapse, tests this *unique-incidence* condition before each deletion, records every pair in `verification_output.json`, and checks the residual one-dimensional incidence graph is connected. It also checks subgroup completeness by multiplication in \(D_5\).

Each step is an elementary strong deformation retraction. A connected graph with \(v\) vertices and \(e\) edges is homotopy equivalent to \(\bigvee^{e-v+1}S^1\); the residual ranks are respectively \(6,2,2,0\). Conjugate subgroups have isomorphic quotients. This completes all cases.

## Verification
Run `python3 verify.py` using only the Python standard library. Its JSON output must match `verification_output.json` byte-for-byte. The script independently counts chain orbits via both canonical orbit representatives and Burnside's lemma; checks all faces and quotient boundary multiplicities; records every free face and coface removed; verifies remaining connected graphs; and enumerates the eight actual subgroups grouped into four conjugacy types. It does not infer infinite statements from finite experiments: the theorem only concerns the exactly enumerated six-vertex wheel.

## Relationship to prior work
Abrams and Ghrist introduced and motivated graph configuration spaces in the context of collision-free motion on networks. Farley and Sabalka developed finite cubical and discrete-Morse methods for graph braid groups. Barnett and Farber established integral homological tools for ordered two-particle graph configuration spaces, including the ordered deleted-product cell model. These general works do not state this exact **unlabeled dihedral-subgroup orbit** homotopy classification. A later publicly indexed wheel calculation determines the rational \(D_5\)-character of first homology; that character implies the rational ranks of the subgroup quotients but by itself neither constructs collapses nor excludes integral torsion or nonfree fundamental groups. The new assertion is precisely the complete homotopy classification for all subgroup quotients of the specified cubical model.

## Limitations
This is a finite, graph-specific result, not a theorem for every wheel size or higher particle number. Its proof rests on a fully specified exhaustive enumeration and explicit free-face certificate; non-independent execution is not external certification. No statement is made about whether a particular nonequivariant deformation retraction from continuous configurations commutes with all graph automorphisms. An equivalent unindexed orbit-space theorem, or a stronger result outside the inspected literature, could supersede the novelty assessment.

## References
- A. Abrams and R. Ghrist, *Finding topology in a factory: configuration spaces*, arXiv:math/0009118 (first version 2000-09-12), https://arxiv.org/abs/math/0009118.
- D. Farley and L. Sabalka, *Discrete Morse theory and graph braid groups*, arXiv:math/0410539 (first version 2004-10-25), https://arxiv.org/html/math/0410539v3.
- K. Barnett and M. Farber, *Topology of configuration space of two particles on a graph, I*, arXiv:0903.2180 (first version 2009-03-12), https://arxiv.org/html/0903.2180v1.
- *Complete dihedral first-homology characters for two particles on wheel graphs*, publicly indexed result at https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-complete-dihedral-first-homology-characters-for-two-particles-on--84359f9fd52d (the published summary was available; full text was not available for inspection).
