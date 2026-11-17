# A lens-space product from cyclic relabeling of pentagon graph colorings

## Finding
Let \(X=|\operatorname{Hom}(C_5,K_5)|\) be the standard graph-multihomomorphism complex. The source cycle has five **fixed** positions, while the cyclic group \(G=C_5\) acts by cyclically permuting the five **target colors**. Its action is free. The ordinary geometric quotient has the integral homotopy type
\[
\boxed{X/G\simeq S^2\times L(5;1,2).}
\]
Here \(L(5;1,2)\) is the quotient of the unit sphere in \(\mathbb C^2\) by \((z,w)\mapsto(\zeta z,\zeta^2w)\) with \(\zeta=e^{2\pi i/5}\). In particular, \(\pi_1(X/G)\cong\mathbb Z/5\), and the complete integral homology is
\[
H_i(X/G;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,2,5,\\
\mathbb Z/5,&i=1,\\
\mathbb Z\oplus\mathbb Z/5,&i=3,\\
0,&\text{otherwise}.
\end{cases}
\]
The assertion is a homotopy equivalence, not an asserted equivariant homeomorphism of the unreduced complex with an orthogonal Stiefel model.

## Assumptions and scope
Number the five source vertices cyclically. A cell of \(X\) is a tuple \((A_0,\ldots,A_4)\) of nonempty subsets of the color set \(\{0,1,2,3,4\}\) with \(A_i\cap A_{i+1}=\varnothing\) (indices modulo five). Its characteristic space is \(\prod_i\Delta^{A_i}\). The generator of \(G\) replaces every color \(c\) by \(c+1\pmod5\), and does **not** move any source vertex. Quotients are the ordinary quotients of geometric realizations, not orbit-poset approximations or homotopy orbits by definition.

Write \(M=\partial\Delta^4\), the boundary of the simplex on the five colors, with the same cyclic permutation action. Its barycentric subdivision is regarded as a \(G\)-simplicial model. The target-color action on \(M\) is free: an invariant boundary point would have five equal barycentric coordinates and hence lie at the interior barycenter of the full simplex.

## Proof
**1. The two free actions and equivariant reduction.** A nonidentity element of \(G\) is a five-cycle on colors. If it fixed a point of a product cell, the unique cell containing that point in its relative interior would be stabilized. Every nonempty row subset \(A_i\) would then be invariant under a transitive five-cycle, forcing \(A_i\) to contain all five colors. Adjacent row subsets could not be disjoint. Hence \(G\) acts freely on \(X\).

Choose the independent two-vertex subset \(I=\{2,4\}\) of the source pentagon, as in Schultz's reduced model, and let \(X_I=|\operatorname{Hom}_I(C_5,K_5)|\). The natural coordinate-forgetting map \(f:X\to X_I\) is \(G\)-equivariant, because it involves only source coordinates and commutes with all target-color permutations. Csorba's reduction, proved in the precise PL setting by Schultz (Lemma 3.12 and Proposition 5.1), says that \(f\) is a nonequivariant homotopy equivalence. The target-color action on \(X_I\) is also free: each reduced cell must extend to a genuine source-pentagon coloring. A fixed reduced cell would force its nonempty retained color sets to be all five colors; since each retained source vertex has a neighbor required to carry a nonempty disjoint set, such an extension is impossible. Both spaces admit finite free \(G\)-CW structures (subdivide if necessary). The equivariant Whitehead criterion, checking only the trivial subgroup because all nontrivial fixed sets are empty, upgrades \(f\) to a \(G\)-homotopy equivalence. It induces \(X/G\simeq X_I/G\).

**2. The reduced model as a symmetric regular-neighborhood boundary.** Schultz's Section 5, particularly the explicit face-poset isomorphism (7) and Proposition 4.12, identifies \(X_I\) with the boundary \(\partial N\) of a **derived regular neighborhood** \(N\) of the diagonal \(\Delta_M\subset M\times M\). The face-poset identification uses only inclusion and complementation of color subsets. Thus it commutes with permutations of the five target-color labels, in particular with \(G\). Moreover, the derived-neighborhood construction is canonical under such simplicial automorphisms: \(N\) and \(\partial N\) are \(G\)-invariant. Hence \(X_I/G\cong(\partial N)/G\).

The diagonal \(G\)-action on \(M\times M\) is free. Passing to the quotient of an invariant derived neighborhood of an invariant triangulated submanifold gives a PL regular neighborhood \(N/G\) of \(\Delta_M/G\) in the manifold \((M\times M)/G\). This follows directly by passing the derived-star construction through a sufficiently subdivided free simplicial action. By ordinary uniqueness of regular neighborhoods, its boundary has the homotopy type of the unit sphere bundle of the normal bundle of \(\Delta_M/G\) in \((M\times M)/G\). On the diagonal, the normal bundle in \(M\times M\) is naturally \(TM\), with the induced diagonal \(G\)-action; descending gives the tangent bundle of \(B=M/G\). Therefore \(X/G\simeq S(TB)\), the unit tangent sphere bundle of \(B\).

**3. Identify the base and trivialize its tangent bundle.** Radial projection from the barycenter of the simplex identifies \(M\) \(G\)-equivariantly with the unit sphere in \(W=\{(x_0,\ldots,x_4)\in\mathbb R^5:\sum x_i=0\}\). The real four-dimensional representation \(W\) of a five-cycle splits as two oriented rotation planes with eigenweights \(1\) and \(2\); its complexification has eigenvalues \(\zeta,\zeta^2,\zeta^3,\zeta^4\). Thus \(B=M/G\cong L(5;1,2)\). It is a closed oriented three-manifold. Every oriented three-manifold is parallelizable, so \(TB\cong B\times\mathbb R^3\) and \(S(TB)\cong B\times S^2\). Combining the three steps proves the claimed homotopy equivalence.

The stated fundamental group and homology now follow from \(\pi_1(L(5;1,2))=\mathbb Z/5\), the standard integral lens-space homology, and the integral Künneth theorem (no \(\operatorname{Tor}\) contribution from the free homology of \(S^2\)).

## Verification
The standalone `verify_color_cycle.py` uses only the Python standard library. It enumerates every color class as an independent vertex subset of the source pentagon, and enumerates all five-color assignments covering every source vertex. It checks that each product cell has a five-element target-color orbit, obtains exactly \((204,1140,2600,3000,1750,414)\) orbit cells in dimensions zero through five, and checks Euler characteristic zero. The check is complete for this finite cell set, but these enumerations are independent consistency tests; the homotopy proof rests on the equivariant reduction, regular-neighborhood normal bundle, and three-manifold parallelizability, not on numerical extrapolation. The code's comments and printed assertions give an unambiguous replay procedure: `python verify_color_cycle.py`.

## Relationship to prior work
Babson–Kozlov introduced the graph-Hom complex. Schultz proved the nonequivariant Stiefel identification \(\operatorname{Hom}(C_5,K_5)\cong V_2(\mathbb R^4)\cong S^2\times S^3\) and gave the canonical smaller regular-neighborhood model used here. Dover–Özaydın strengthened equivariance for a **source reflection**, not the target-color subgroup in the claim. Those works establish the necessary constructions, but their stated results do not classify this five-cycle **target-color quotient**. Related calculations of a quotient by the full **source dihedral** group and of rational \(D_5\times S_n\) representations do not imply the displayed integral product homotopy type: the acting groups are different, and rational character information cannot decide the torsion or full homotopy type. Dasgupta's later Stiefel quotient results concern **right frame** actions rather than this target-label action.

## Limitations
Only the specified five-color target cycle is classified; the result does not classify general color subgroups, arbitrary numbers of target colors, or a full equivariant Stiefel homeomorphism. The regular-neighborhood passage uses the standard PL regular-neighborhood theorem and the fact that the source paper's displayed poset maps are color-equivariant; their target-color equivariance is checked from their defining set operations, not advertised as a separate theorem. An independent mathematical audit has not been performed. Equivalent unindexed work or an explicitly published naturality corollary may affect priority.

## References
1. E. Babson and D. Kozlov, *Complexes of graph homomorphisms*, arXiv:math/0310056, first public 2003-10-05, https://arxiv.org/abs/math/0310056 .
2. C. Schultz, *Small models of graph colouring manifolds and the Stiefel manifolds \(\operatorname{Hom}(C_5,K_n)\)*, arXiv:math/0510535, first public 2005-10-25, https://arxiv.org/abs/math/0510535 ; especially Lemma 3.12, Proposition 4.12, Proposition 5.1 and Theorem 5.2.
3. J. Dover and M. Özaydın, *Stiefel Manifolds and Coloring the Pentagon*, arXiv:1302.2831, first public 2013-02-12, https://arxiv.org/abs/1302.2831 ; especially the stated equivariance and its scope.
4. D. Dasgupta, *Characteristic classes on certain quotients of Stiefel manifolds*, arXiv:2402.10521, first public 2024-02-16, https://arxiv.org/abs/2402.10521 ; Introduction, Sections 2–3.
