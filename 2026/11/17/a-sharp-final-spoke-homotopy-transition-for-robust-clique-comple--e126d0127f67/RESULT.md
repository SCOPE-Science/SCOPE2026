# A sharp final-spoke homotopy transition for robust clique complexes of star-deficient bicliques

## Finding
For integers \(k\ge4\) and \(a,b\ge k+1\), choose a bipartition \(A\sqcup B\) of sizes \(a,b\), a fixed hub \(u\in A\), and an ordering \(v_1,\ldots,v_b\) of \(B\). Define \(G_t=K_{a,b}\setminus\{uv_1,\ldots,uv_t\}\) for \(0\le t\le b\). Let \(X_t=\mathsf{Cliq}_k(G_t)\), whose simplices are all subsets \(S\subseteq A\sqcup B\) such that \(\alpha(G_t[S])<k\). Set
\[
d=2k-3,\qquad F=\binom{a-2}{k-1}\binom{b-1}{k-1},\qquad M=\binom{a-2}{k-2}.
\]
The complete integral homotopy classification is
\[
|X_t|\simeq\bigvee^{F+M(\binom{b-1}{k-1}-\binom{t}{k-1})}S^d\quad(0\le t<b),
\]
and at the final deletion
\[
|X_b|\simeq\bigvee^F S^d\vee\bigvee^{M\binom{b-1}{k-2}}S^{d-1}.
\]
All homology is integral and free. Thus deletion of fewer than \(k-1\) hub edges does not change the complex at all; the first top homology loss occurs at the \((k-1)\)-st deletion, while lower-dimensional homology appears only when the last hub edge is deleted. For \(1\le t<b\), the inclusion \(X_t\hookrightarrow X_{t-1}\) induces a split injection on \(\widetilde H_d(-;\mathbb Z)\) with free cokernel of rank \(M\binom{t-1}{k-2}\). The final inclusion is an isomorphism in degree \(d\) and kills the newly appearing degree-\(d-1\) classes.

For example, with \(a=b=5\) and \(k=4\), the successive ranks of \(\widetilde H_5\) are \(13,13,13,10,1,1\) for \(t=0,1,2,3,4,5\). At \(t=5\), there are additionally \(18\) generators of \(\widetilde H_4\).

## Assumptions and scope
The graph is finite, simple, and bipartite; deleted edges must share the same endpoint \(u\). The threshold is \(k\ge4\), and both shores contain at least \(k+1\) vertices, so the two uniform skeleton factors have nonzero top homology. Binomial coefficients are zero when the lower parameter exceeds the upper. A wedge of zero spheres means a point. Homotopy equivalences are nonequivariant; the homology maps use the natural nested inclusions \(X_b\subseteq X_{b-1}\subseteq\cdots\subseteq X_0\).

## Proof
**1. Direct face classification.** Denote \(A'=A\setminus\{u\}\), and \(B_0=\{v_1,\ldots,v_t\}\). Every independent set of \(G_t\) lies entirely in \(A\), entirely in \(B\), or has the form \(\{u\}\cup T\) with \(T\subseteq B_0\). This is because every vertex of \(A'\) is adjacent to every vertex of \(B\), and \(u\) is nonadjacent exactly to \(B_0\). Consequently \(S\) is a face of \(X_t\) precisely when \(|S\cap A|\le k-1\), \(|S\cap B|\le k-1\), and, if \(u\in S\), \(|S\cap B_0|\le k-2\).

For a finite set \(E\), write \(U_{r,E}=\{T\subseteq E:|T|\le r\}\), the rank-\(r\) uniform matroid complex. The deletion and link of the vertex \(u\) in \(X_t\) are
\[
D=X_t\setminus u=U_{k-1,A'}*U_{k-1,B},\qquad
L_t=\operatorname{lk}_{X_t}(u)=U_{k-2,A'}*Q_t,
\]
where
\[
Q_t=\{T\subseteq B:|T|\le k-1,\ |T\cap B_0|\le k-2\}.
\]
Thus \(X_t=D\cup(u*L_t)\) and \(D\cap(u*L_t)=L_t\).

**2. Matroid homotopy and exact ranks.** The independence complex \(U_{r,E}\) for \(1\le r<|E|\) is homotopy equivalent to \(\binom{|E|-1}{r}\) copies of \(S^{r-1}\) (the standard skeleton of a simplex). For \(t<b\), \(Q_t\) is the rank-\((k-1)\) truncation of the partition matroid with quota \(k-2\) on \(B_0\) and quota \(k-1\) on \(B\setminus B_0\). Because the latter class is nonempty and \(b\ge k+1\), this is a pure rank-\((k-1)\) matroid complex. Matroid independence complexes are shellable, hence have the homotopy type of wedges of spheres only in top dimension \(k-2\). Compared to \(U_{k-1,B}\), precisely the \(\binom{t}{k-1}\) top faces contained in \(B_0\) are absent, while all smaller faces are present. Euler characteristic therefore gives
\[
Q_t\simeq\bigvee^{\binom{b-1}{k-1}-\binom{t}{k-1}}S^{k-2}\qquad(t<b).
\]
At \(t=b-1\), the sole remaining neighbor is a cone point of \(Q_t\), agreeing with zero summands. At \(t=b\), all of \(B\) lies in \(B_0\), so \(Q_b=U_{k-2,B}\simeq\bigvee^{\binom{b-1}{k-2}}S^{k-3}\).

**3. Cone attachment is null.** From the standard join formula for sphere wedges,
\[
D\simeq\bigvee^F S^{2k-3}.
\]
For \(t<b\), \(L_t\) is a wedge of \(M(\binom{b-1}{k-1}-\binom{t}{k-1})\) spheres of dimension \(2k-4\). For \(t=b\), \(L_b\) is a wedge of \(M\binom{b-1}{k-2}\) spheres of dimension \(2k-5\). More strongly, the **simplicial dimension** of \(L_t\) is at most \(2k-4\). The space \(D\) is \((2k-4)\)-connected, since \(2k-3\ge5\) and it is a wedge of \((2k-3)\)-spheres. The inclusion \(L_t\hookrightarrow D\) is therefore nullhomotopic by cellular approximation. Its cone attachment gives \(X_t\simeq D\vee\Sigma L_t\), establishing both wedge formulas, with integral homology and no hidden attaching obstructions.

**4. Primitive homology maps.** Every \(X_t\) has dimension at most \(d=2k-3\). Thus \(H_d(X_t;\mathbb Z)=\ker(\partial_d:C_d(X_t;\mathbb Z)\to C_{d-1}(X_t;\mathbb Z))\). Since \(X_t\subseteq X_{t-1}\), this subgroup is exactly \(H_d(X_{t-1};\mathbb Z)\cap C_d(X_t;\mathbb Z)\) inside the free top-chain group. The quotient of the two homology lattices injects into the free coordinate quotient \(C_d(X_{t-1};\mathbb Z)/C_d(X_t;\mathbb Z)\), so it is torsion-free. The known rank difference equals
\[
M\left(\binom{t}{k-1}-\binom{t-1}{k-1}\right)=M\binom{t-1}{k-2}.
\]
Hence every inclusion for \(t<b\) is a primitive split injection in degree \(d\). At \(t=b\) the two top homology ranks are both \(F\), so primitivity makes the injection an isomorphism. Degree \(d-1\) is zero for \(t<b\), hence all degree-\(d-1\) classes at \(t=b\) have zero image under the last inclusion. This proves the full claim.

## Verification
An independent standard-library Python checker enumerates **all** vertex subsets and independently checks every candidate independent \(k\)-set against the actual edge set, without using the proof's face-factor decomposition. It constructs signed simplicial boundaries and reduces them over \(\mathbb F_2\) and \(\mathbb F_3\). Across 41 configurations covering \(k=3,4\), \((a,b)\in\{(4,4),(4,5),(5,4),(5,5),(5,6),(6,5)\}\) as selected in the code, and every \(t\in[0,b]\), observed homology ranks agree with the formula in both characteristics. The \(k=3\) checks are auxiliary sanity tests, not part of the original theorem's claimed novelty. Run `python3 verify.py` and compare to `verification.json` for exact parameters, face counts, and outputs. These finite modular checks are not a proof of the infinite-family statement or of integral torsion-freeness; those follow from the matroid, join, and cone-attachment proof above.

## Relationship to prior work
Filakovský's February 11, 2026 preprint studies \(k\)-robust clique complexes of grids and square-sequence graphs; its full text gives homotopy classifications for \(k=2,3\), and an all-threshold result restricted to edge-glued square sequences. The present near-complete bipartite graphs, with \(a,b\ge5\), are not square-sequence graphs: such graphs have at most \(2|V|-4\) edges, while these have at least \(ab-b>2(a+b)-4\). In particular those theorems do not cover the present dense star-deletion family. Kim–Lew's earlier foundational treatment principally establishes collapsibility and Leray bounds, not this homotopy and map classification. An indexed 2026 result for the three-robust complex of **all connected bipartite graphs** already covers \(k=3\); this claim therefore intentionally begins at \(k=4\). Previously reported robust-complex calculations for deleted disjoint four-cycle blocks likewise do not cover a star of missing edges. Standard uniform-matroid and matroid-shellability facts are used as ingredients, not claimed as new theorems.

## Limitations
The classification requires a single centered missing-edge star, \(a,b\ge k+1\) and \(k\ge4\). It makes no claim for general missing-edge configurations, smaller shores, integral automorphism representations, shellability of the entire complex, or arbitrary higher secant complexes. The accompanying computations are finite-field crosschecks only. Priority remains subject to unindexed or inaccessible literature and independent mathematical assessment.

## References
1. M. Filakovský, *The Topology of \(k\)-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365, first publicly posted 2026-02-11. https://arxiv.org/html/2602.11365
2. M. Kim and A. Lew, *Complexes of graphs with bounded independence number*, arXiv:1912.12605, 2019-12-29; Israel J. Math. 249 (2022), 83–120. https://arxiv.org/pdf/1912.12605
3. J. Choe and J. Jung, *A Fröberg type theorem for higher secant complexes*, arXiv:2502.20987, first posted 2025-02-28. https://arxiv.org/abs/2502.20987
4. A. Björner, *Shellable and Cohen–Macaulay simplicial complexes*, Trans. Amer. Math. Soc. 260 (1980), 159–183. (Standard matroid shellability background.)
