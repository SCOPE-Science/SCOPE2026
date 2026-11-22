# Weighted discrete Sobolev isometries of cycles: a unique tetrahedral symmetry point

## Finding
For each integer \(n\ge3\) and weight \(\gamma>0\), equip the **real** vector space \(\mathbb R^n\) with the first-order periodic graph-Sobolev norm
\[
 N_{n,\gamma}(f)=\sum_{i=1}^{n}|f_i|+\gamma\sum_{i=1}^{n}|f_{i+1}-f_i|,\qquad f_{n+1}=f_1.
\]
Let \(\operatorname{LIso}(n,\gamma)\) be its group of surjective real-linear isometries. Then
\[
 \boxed{\operatorname{LIso}(n,\gamma)=\{\pm P_\pi:\pi\in D_n\}\quad\text{unless }(n,\gamma)=(3,1),}
\]
where \(D_n\) denotes the dihedral permutation group of the \(n\)-cycle and \(P_\pi\) is its coordinate-permutation representation. The generic group has order \(4n\).

At the **unique exceptional parameter** \((n,\gamma)=(3,1)\), write \(f_0=0\), and for \(\sigma\in S_4\) set
\[
 (R_\sigma f)_i=f_{\sigma(i)}-f_{\sigma(0)},\qquad i=1,2,3.
\]
Then
\[
 \boxed{\operatorname{LIso}(3,1)=\{\pm R_\sigma:\sigma\in S_4\},\qquad |\operatorname{LIso}(3,1)|=48.}
\]
Consequently the balanced three-cycle has four times the isometries of every positively unbalanced three-cycle, whose group has order \(12\). A reanchoring symmetry such as \(f\mapsto(-f_1,f_2-f_1,f_3-f_1)\) exists precisely at the balanced weight.

## Assumptions and scope
All scalars and isometries are real. The cycle is simple with \(n\ge3\) distinct vertices, all vertex-mass coefficients are one, all cyclic-gradient coefficients are the common number \(\gamma>0\), and the map is a **surjective linear** self-isometry. Arbitrary nonlinear metric isometries (which also include translations), nonuniform graph weights, and other graph families are not claimed. The two generators \(R_\sigma\) and global sign are independent at the exceptional point: their groups form a direct product \(S_4\times C_2\).

## Proof
**1. Recovering exact edge vectors from the norm.** Let \(e_i\) be the standard basis and set
\[
 a_i=e_i,\qquad b_i=\gamma(e_i-e_{i+1}),\qquad i\in\mathbb Z/n\mathbb Z.
\]
These are \(2n\) pairwise nonparallel vectors, up to sign. The norm is the support function of the centrally symmetric, full-dimensional zonotope
\[
 Z_{n,\gamma}=\sum_{i=1}^{n}[-a_i,a_i]+\sum_{i=1}^{n}[-b_i,b_i].
\]
For each generator \(g\) choose a functional orthogonal to \(g\) and nonorthogonal to every other generator. Such a functional exists because its hyperplane cannot be covered by finitely many proper subspaces; the restriction \(n\ge3\) ensures no parallel generator pairs. It exposes an edge of \(Z_{n,\gamma}\) whose displacement is exactly \(2g\). Conversely a one-dimensional exposed face of a zonotope is the sum of segments parallel to its exposing hyperplane, and here must be a translate of precisely one generating segment; its displacement is \(\pm2g\). Thus the set of oriented edge displacements is exactly \(\{\pm2a_i,\pm2b_i\}\).

If \(T\) is a surjective linear isometry, equality of support functions gives \(T^{\!*}Z_{n,\gamma}=Z_{n,\gamma}\). Hence \(T^{\!*}\) permutes \(\{\pm a_i,\pm b_i\}\) **with no additional scalings** and preserves all linear dependencies between generator triples. (Here \(T^{\!*}\) denotes transpose under the standard pairing.)

**2. Dependence triples are the wheel triangles.** Adjoin a hub vertex \(0\) with potential \(f_0=0\). Regard \(a_i\) as the incidence vector for the spoke \(0i\) and \(b_i\) as \(\gamma\) times the incidence vector for the rim edge \(i(i+1)\). In a finite graph, a set of three nonparallel incidence vectors is dependent exactly when those edges form a triangle: a forest has independent incidence columns by successive leaf deletion, while a triangle has the oriented sum-zero relation.

**3. Every cycle with at least four rim vertices.** For \(n\ge4\), the wheel has exactly the \(n\) triangles comprising two adjacent spokes and their connecting rim edge. Each spoke occurs in two such triangles and each rim edge in one. Since \(T^{\!*}\) permutes dependence triples, it must preserve the spoke set and the rim set. Consequently
\[
 T^{\!*}e_i=s_i e_{\pi(i)},\qquad s_i\in\{-1,1\},
\]
for a permutation \(\pi\). The image of \(b_i\) is \(\gamma(s_i e_{\pi(i)}-s_{i+1}e_{\pi(i+1)})\); because it must be a signed rim generator, \(s_i=s_{i+1}\) and \(\pi(i),\pi(i+1)\) must be adjacent on the cycle. Connectivity forces every sign to coincide, and adjacency preservation forces \(\pi\in D_n\). Conversely each global sign times dihedral coordinate permutation plainly preserves the norm.

**4. Three rim vertices and unequal weights.** If \(n=3\), the associated wheel is \(K_4\) and has four triangle circuits. The all-rim triangle has a minimal dependence with absolute coefficient ratios \((1,1,1)\). Each of the other three triangles comprises two spokes and one rim; its absolute coefficient ratios are \((1,1,1/\gamma)\). Because \(T^{\!*}\) sends each individual generator to a signed generator **without rescaling**, these ratios are invariant up to reordering and common multiplication. For \(\gamma\ne1\), the all-rim triangle is the only triple with three equal coefficient magnitudes; it is therefore invariant as a set. Its three edges, and hence the complementary three spokes, are preserved. The signed-coordinate argument of step 3 then implies the group \(\{\pm P_\pi:\pi\in S_3\}=\{\pm P_\pi:\pi\in D_3\}\).

**5. Three rim vertices at balance.** For \(n=3\) and \(\gamma=1\),
\[
 N_{3,1}(f)=\sum_{0\le i<j\le3}|f_i-f_j|,\qquad f_0=0.
\]
Every permutation of the four potentials, reanchored to make the new zeroth potential zero, is therefore a linear isometry, as is its negative. These give \(48\) distinct transformations. Conversely every isometry permutes the four triangle circuits. Every edge of \(K_4\) is uniquely determined by the pair of triangles that contain it; thus the induced edge permutation is determined by a permutation of the four triangles and hence by some vertex permutation. Composing with its inverse reanchoring, the transpose fixes every generator direction individually, up to sign. Its action on the three spoke basis vectors is diagonal \(\operatorname{diag}(s_1,s_2,s_3)\), and preserving each rim generator forces \(s_1=s_2=s_3\). It is therefore a global sign. This proves completeness and the stated order. \(\square\)

## Verification
The standalone `check.py` uses exact rational arithmetic to enumerate every possible signed image of the spoke generators and filters candidates by the full weighted rim-generator set. At dimensions \(n=3,4\) and weights \(\gamma\in\{1/2,1,2\}\), it finds respectively \((12,48,12)\) and \((16,16,16)\) isometries, checking their norm identities on all vectors with entries in \(\{-1,0,1\}\). The final count is `DISCRETE_W11_WHEEL_ISOMETRY_CHECK_OK 5840`. This finite verification does not prove the general theorem; the proof above covers all \(n\ge3\) and real \(\gamma>0\).

## Relationship to prior work
Hamad's *Isometric Classification of Sobolev Spaces* (arXiv:2611.09577v1, first public 6 November 2026, Theorem 1.1) classifies linear isometries of continuous \(W^{k,1}(\mathbb R^n)\) with sums of all weak-derivative \(L^1\) norms. It motivates the discrete question but neither discusses this finite cyclic graph norm nor its isolated hidden symmetry.

Cúth, Doucha and Titkos (2024, Section 6) classify isometries of graph **Lipschitz-free spaces** and their Lipschitz-function duals. Those use the transportation quotient norm and a maximum Lipschitz quotient, respectively, not the additive \(\ell_1\) vertex-plus-edge-gradient norm above. Their classification therefore does not imply this statement through an identification of norms. Padrol, Pilaud and Poullot (2023, Sections 1–2) study deformations of graphical zonotopes; their results provide geometric context, but do not give this weighted discrete Sobolev isometry classification or its weight-one exception. The proof here is self-contained and uses elementary exact edge displacements and the wheel's triangle circuits. A broader abstract graphic-matroid automorphism theorem could recover parts of the argument; no assertion of uniqueness across all existing terminology is made.

## Limitations
This is a finite-dimensional real-linear isometry classification, not a new theorem about continuous Sobolev spaces. The special weight statement assumes **uniform** rim weights. The full literature under equivalently phrased graph norm and oriented-matroid terminology is not exhaustively indexed; possible implicit prior coverage is a residual originality risk. The exact arithmetic script gives finite consistency evidence only. No independent mathematical audit is claimed.

## References
1. Samir Hamad, *Isometric Classification of Sobolev Spaces*, arXiv:2611.09577v1 (first public 6 November 2026), Theorem 1.1, https://arxiv.org/abs/2611.09577.
2. Marek Cúth, Michal Doucha, Tamás Titkos, *Isometries of Lipschitz-free Banach spaces*, Journal of the London Mathematical Society 110 (2024), e70000, Sections 1 and 6, https://doi.org/10.1112/jlms.70000.
3. Arnau Padrol, Vincent Pilaud, Germain Poullot, *Deformed Graphical Zonotopes*, Discrete & Computational Geometry, published online 13 October 2023, Sections 1–2, https://doi.org/10.1007/s00454-023-00586-x.
