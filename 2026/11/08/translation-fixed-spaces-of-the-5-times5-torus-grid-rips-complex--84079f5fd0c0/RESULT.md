# Translation-fixed spaces of the \(5\times5\) torus-grid Rips complex at scale \(3\)

## Finding
Let \(A=(\mathbb Z/5\mathbb Z)^2\), with distance \(d((a,b),(c,e))=\min(|a-c|,5-|a-c|)+\min(|b-e|,5-|b-e|)\), interpreting coordinate differences by representatives from \(\{0,1,2,3,4\}\). Let \(X\) be the inclusive Vietoris–Rips complex at scale \(3\) on these \(25\) points. The translation group \(A\) acts simplicially. For each \(s\in\{0,1,2,3,4\}\), set \(L_s=\langle(1,s)\rangle\), and set \(L_\infty=\langle(0,1)\rangle\). The complete classification of geometric fixed spaces is

\[
|X|^{L_s}\cong
\begin{cases}
S^1,&s=0,\\
\varnothing,&s=1,4,\\
\bigsqcup_{j=1}^{5}\{\mathrm{pt}\},&s=2,3,
\end{cases}
\qquad
|X|^{L_\infty}\cong S^1,
\qquad |X|^A=\varnothing.
\]

The trivial subgroup fixes all of \(|X|\), whose homotopy type \(\bigvee^9S^4\) was established by Adams, Adetowubo, Barriga-Acosta, Feng and Sterling (Theorem 7.1 of the cited paper) and is **not claimed as new**. Write \(V_s=\ker(\mathbb Q[A/L_s]\xrightarrow{\varepsilon}\mathbb Q)\) for the four-dimensional augmentation representation. The resulting complete rational translation action on the only nonzero reduced homology is

\[
\widetilde H_4(X;\mathbb Q)\cong \mathbb Q\oplus V_2\oplus V_3
\quad\text{as }\mathbb Q[A]\text{-modules}.
\]

Equivalently, for a translation \(g=(a,b)\), its fourth-homology trace is \(9\) for \(g=0\), \(4\) for nonzero \(g\in L_2\cup L_3\), and \(-1\) for every other nonzero \(g\).

## Assumptions and scope
The vertex set is precisely the additive group \(A\); the distance is the shortest-path \(\ell^1\) distance on the five-by-five Cartesian torus grid, and simplex membership means all pairwise distances are **at most** \(3\). The acting group is the group of translations, not the full graph automorphism group. Its subgroup lattice consists exactly of the trivial subgroup, the six lines of order \(5\) listed above, and \(A\) itself. Geometric fixed points are points in the realization fixed pointwise; taking the full subcomplex on individually fixed vertices would give an incorrect answer.

## Proof
**Orbit-complex model.** For a simplicial action of a finite group \(H\), the fixed realization \(|K|^H\) is homeomorphic to the realization of the simplicial complex whose vertices are the \(H\)-orbits of vertices of \(K\) that themselves form faces, and whose faces are collections of orbits with union a face. Indeed, barycentric coordinates of a fixed point are constant on each orbit; assigning the total weight of each orbit gives a continuous affine homeomorphism, with inverse assigning equal weight to each vertex of that orbit. This argument also covers an empty fixed space.

**The six order-five subgroups.** Each line has precisely five orbits of size five. A horizontal translation (generator \((1,0)\)) has orbits \(O_j=\{(i,j):i\in\mathbb Z/5\}\). Every such orbit has diameter \(2\), and \(O_j\cup O_k\) has diameter at most \(3\) precisely when the cyclic separation of \(j,k\) is \(1\). No three distinct orbits have admissible union. Thus the orbit complex is the five-edge cycle, whose realization is \(S^1\). Interchanging coordinates gives the vertical case \(L_\infty\).

For the slope-one generator \((1,1)\), every orbit contains two vertices differing by \((2,2)\), at distance \(4\). Therefore no orbit is itself an admissible face and the geometric fixed space is empty. The coordinate reflection \((a,b)\mapsto(a,-b)\) gives the slope-four case.

For the slope-two generator \((1,2)\), the five orbits are \(O_j=\{(i,2i+j):i\in\mathbb Z/5\}\). Every pair of vertices of one \(O_j\) has distance at most \(3\), since differences along this orbit are \((\pm1,\pm2)\) or \((\pm2,\mp1)\). If \(j\ne k\), some two points in \(O_j\cup O_k\) differ by \((\pm2,\pm2)\), hence have distance \(4\). Explicitly, with \(\delta=k-j\in\{1,2,3,4\}\), choose \(i'-i=2\) when \(\delta\in\{3,4\}\), and choose \(i'-i=-2\) when \(\delta\in\{1,2\}\); then the second-coordinate difference has circular distance \(2\). Hence exactly five isolated orbit vertices survive. Reflecting the second coordinate gives the slope-three case. The whole group \(A\) is transitive on all \(25\) vertices, which do not span a face, so its fixed space is empty.

**Ordinary homology and representations.** Adams and coauthors proved \(|X|\simeq\bigvee^9 S^4\). An independent exhaustive acyclic Morse matching described below also proves this ordinary homotopy type without using numerical homology extrapolation. Thus \(\widetilde H_4(X;\mathbb Q)\) is nine-dimensional and is the only nonzero reduced rational homology group. The simplicial Lefschetz fixed-point theorem gives \(1+\operatorname{tr}(g\mid \widetilde H_4)=\chi(|X|^{\langle g\rangle})\) for nonidentity \(g\). The fixed-space Euler characteristics are \(0\) for the circle and empty cases, and \(5\) for the five-point cases. The resulting traces are exactly \(-1\) and \(4\), respectively; the identity trace is \(9\).

Each \(V_s\) is the four-dimensional irreducible rational cyclotomic representation inflated from \(A/L_s\cong\mathbb Z/5\), with character equal to \(4\) on \(L_s\) and \(-1\) elsewhere. The character of \(\mathbb Q\oplus V_2\oplus V_3\) is therefore precisely the calculated character. Semisimplicity of \(\mathbb Q[A]\) and equality of characters prove the representation isomorphism.

## Verification
The standalone `verify.py` enumerates all \(25{,}531\) faces including the empty face from pairwise graph distances; uses a relabelling \((x,y)\mapsto(2(x+y),2(x-y))\) over \(\mathbb Z/5\) to arrange a convenient pivot order; pairs faces by deterministic successive vertex toggles; and constructs the **complete** directed Hasse graph with every matched edge reversed. Kahn topological sorting processes all \(25{,}530\) nonempty faces, proving acyclicity. The matching has exactly \(12{,}760\) pairs and precisely one critical vertex and nine critical four-dimensional faces. Discrete Morse theory gives \(|X|\simeq\bigvee^9S^4\).

The same verifier builds every order-five orbit quotient directly from the original metric, checks its entire face vector, independently evaluates the reduced signed simplicial chain trace for **all 25 translations**, and compares it to the proposed character. Reproduce with `python3 verify.py`. The exact stdout is supplied as `verification_output.txt`. The finite certificate concerns this single specified \(25\)-vertex complex; no general torus size is inferred from it.

## Relationship to prior work
Adams–Adetowubo–Barriga-Acosta–Feng–Sterling, *Vietoris–Rips complexes of torus grids*, arXiv:2502.07134, Theorem 7.1, already proves the nine-four-sphere ordinary homotopy type. Its introduction remarks that equivariant homotopy types might have applications, but the theorem and proof determine neither the eight translation-subgroup fixed-point spaces nor the rational translation character. Sterling's related 2025 thesis explicitly describes itself as exposition of that project and does not present a corresponding group-action classification. The contribution here is the **complete fixed-point orbit geometry and the resulting rational homology representation**, not a new nonequivariant Betti number or homotopy type. Geometrically, one translation direction can fix a circle, a different direction five disconnected points, and another none, despite all acting on the same underlying nine-sphere wedge.

## Limitations
Only the translation subgroup \(A\), the exact five-by-five torus grid, and inclusive distance threshold \(3\) are considered. The conclusion is a rational representation isomorphism; no integral \(\mathbb Z[A]\)-lattice splitting, full equivariant homotopy equivalence, filtration-level naturality, or larger-grid generalization is asserted. An equivalent formulation in presently unindexed symmetry literature cannot be excluded by searches alone.

## References
1. H. Adams, A. Y. Adetowubo, H. Barriga-Acosta, Z. Feng and J. Sterling, *Vietoris–Rips complexes of torus grids*, arXiv:2502.07134v2 (2025), especially Theorem 7.1 and the discussion of equivariant topology. https://arxiv.org/abs/2502.07134
2. J. Sterling, *Vietoris–Rips Complexes of Torus Grids*, Auburn University master's thesis (2025), handle 10415/9659. https://etd.auburn.edu/handle/10415/9659
3. R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145 (standard discrete-Morse theorem).
