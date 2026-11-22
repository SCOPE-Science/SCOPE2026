# Affine homology representation and quotient of the Paley-23 out-neighborhood complex

## Finding

Let \(Q=\{1,2,3,4,6,8,9,12,13,16,18\}\subset\mathbb F_{23}\) be the nonzero quadratic residues, and let \(K\) be the simplicial complex with facets \(u+Q\), for \(u\in\mathbb F_{23}\). This is the irreflexive common *out*-neighborhood complex of the Paley tournament, not its directed flag complex. The affine subgroup
\[
G=\{x\mapsto ax+b:a\in Q,\ b\in\mathbb F_{23}\}\cong\mathbb F_{23}\rtimes C_{11}
\]
of order \(253\) acts simplicially on \(K\).

Write \(W=\mathbb Q^{\mathbb F_{23}}/\mathbb Q\mathbf1\) for the reduced 23-point permutation module, and \(R=\mathbb Q[C_{11}]\) for the 11-dimensional regular rational module of the multiplier quotient, inflated to \(G\). **The symmetry refinement** is
\[
\boxed{\widetilde H_3(K;\mathbb Q)\cong R\oplus W^{\oplus9},\qquad
\widetilde H_4(K;\mathbb Q)\cong\mathbb Q_{\mathrm{triv}}.}
\]
In particular, the ordinary quotient has reduced rational homology
\[
\boxed{\widetilde H_i(|K|/G;\mathbb Q)\cong
 \begin{cases}\mathbb Q,&i=3,4,\\0,&\text{otherwise.}\end{cases}}
\]
The rational degree-three character is \(209\) at the identity, \(2\) on the 22 nonidentity translations, and \(0\) on the 230 affine elements with nonidentity multiplier.

**Previously known nonequivariant input, not claimed as new.** The October 25, 2026 result *A mixed-dimensional sphere wedge from the Paley tournament on 23 vertices* proves the stronger homotopy equivalence \(K\simeq\bigvee^{209}S^3\vee S^4\), hence also the complete integral homology; these nonequivariant assertions are prior work. The present contribution is solely the exact rational affine representation, its character and the rational orbit-space consequence. A later November 8, 2026 public result also gives this character; its public Git commit was later that day than the first commit of the present underlying claim, and it is credited rather than represented as independent corroboration.

## Assumptions and proof

A face is any nonempty subset of one of the \(23\) translated quadratic-residue blocks, with the empty set included conventionally. The preceding published homotopy theorem gives \(\widetilde H_3(K;\mathbb Z)=\mathbb Z^{209}\), \(\widetilde H_4(K;\mathbb Z)=\mathbb Z\), and zero reduced homology in every other degree. Nothing in this finding reproves or newly claims that nonequivariant theorem.

Every \(g(x)=ax+b\) with \(a\in Q\) sends the facet \(u+Q\) to \((au+b)+Q\). Since \(|G|=253\) is odd and \(\widetilde H_4(K;\mathbb Z)\) has rank one, its sign representation is trivial: the only integral automorphisms of \(\mathbb Z\) are \(\pm1\).

For a nonzero translation, the cyclic action on \(23\) vertices is a single orbit; no nonempty simplex (all have at most \(11\) vertices) can be invariant. Thus its **ordinary** simplicial Lefschetz number is \(0\). For \(a\ne1\), conjugation by a translation reduces \(x\mapsto ax+b\) to the pure multiplier \(x\mapsto ax\). The latter has three vertex orbits: \(\{0\}\), \(Q\), and \(-Q\), of sizes \(1,11,11\). Its only nonempty invariant faces are \(\{0\}\) and \(Q\): \(Q\) itself is a facet, whereas \(-Q\) is not a translate of \(Q\) (a direct check of the 23 residue translates gives intersection sizes at most six). The multiplier acts on the eleven-vertex facet \(Q\) by an 11-cycle, of permutation sign \(+1\), so its ordinary Lefschetz number is \(1+1=2\). The identity Lefschetz number equals \(1-209+1=-207\).

The ordinary Hopf trace formula, together with the triviality of \(\widetilde H_4\), reads
\[
L(g)=1-\operatorname{tr}(g\mid\widetilde H_3)+1
=2-\chi_3(g).
\]
Consequently \(\chi_3=(209,2,0)\) on the identity, nonzero translations, and nonidentity multipliers, respectively. The character of \(W\) on these classes is \((22,-1,0)\), because it is the point-permutation character minus the trivial character; the character of the inflated regular module \(R\) is \((11,11,0)\). Therefore
\[
\chi_{R\oplus9W}=(11+9\cdot22,11-9,0)=(209,2,0)=\chi_3.
\]
Maschke semisimplicity and equality of rational characters imply the asserted isomorphism of rational \(G\)-modules. The \(G\)-invariant dimensions are \(\dim R^G=1\), \(\dim W^G=0\), and \(\dim\widetilde H_4(K;\mathbb Q)^G=1\). Applying barycentric subdivision and rational transfer for finite group actions identifies \(H_*(|K|/G;\mathbb Q)\) with invariant homology; the stated reduced quotient groups follow.

## Verification and scope

The nine-file original finite certificate enumerates \(42{,}298\) augmented faces, constructs \(20{,}762\) acyclic Morse pairs, and computes signed integer Smith forms; an independent implementation regenerated the full face vector, all \(244{,}421\) directed Hasse incidences, the differential Smith invariants \((1^{21},1^{213}0^{49},1^{48})\), both chain identities, and the fixed-face patterns for all \(253\) affine transformations. These checks corroborate the cited nonequivariant result and the fixed-face input for the new symmetry theorem. They do not certify other Paley orders, a \(G\)-equivariant homotopy splitting, any integral affine module decomposition, or integral homology of the orbit space. The orbit assertion is rational only.

## Mathematical priority and references

1. *A mixed-dimensional sphere wedge from the Paley tournament on 23 vertices*, publicly committed October 25, 2026, 18:04:35 UTC. Full proof: https://github.com/SCOPE-Science/SCOPE2026/blob/cbe8de2e7e4c261cc5f3b421a843a35dce457291/2026/10/25/a-mixed-dimensional-sphere-wedge-from-the-paley-tournament-on-23--60542e90655b/RESULT.md . This **already establishes all nonequivariant integral homology** and more, but explicitly does not determine the affine action.
2. *The Paley-23 out-neighborhood complex: a mixed sphere wedge and affine homology character*, first public SCOPE commit November 8, 2026, 17:31:43 UTC. Full proof: https://github.com/SCOPE-Science/SCOPE2026/blob/b1fae972f5df2396dcbc54148a67098549c790a4/2026/11/08/the-paley-23-out-neighborhood-complex-a-mixed-sphere-wedge-and-a--d2e37276ff47/RESULT.md . This gives the same affine character, but its first public commit was after the underlying claim's first public commit at 17:29:23 UTC that day. That ordering is a narrow public-history observation, not a claim of independent discovery.
3. A. Dochtermann and A. Singh, *Homomorphism complexes, reconfiguration, and homotopy for directed graphs*, European Journal of Combinatorics **110** (2023), arXiv:2108.10948. Their directed-neighborhood and Hom theorems give general structure, not the present order-253 affine character. https://arxiv.org/abs/2108.10948 .
4. S. Chowdhury and F. Mémoli, *A functorial Dowker theorem and persistent homology of asymmetric networks*, arXiv:1608.05432. The general Dowker framework does not specify this module. https://arxiv.org/abs/1608.05432 .

Residual priority risk: unindexed older computations of the affine action may exist, including under Hadamard \(2\)-\((23,11,5)\) design or Dowker-complex terminology. No external expert certification or publication acceptance is asserted.
