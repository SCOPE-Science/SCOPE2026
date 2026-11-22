# A sharp final-spoke homotopy transition for robust clique complexes of star-deficient bicliques

## Finding
For integers \(k\ge4\) and \(a,b\ge k+1\), let \(A\sqcup B\) be a bipartition with \(|A|=a\), \(|B|=b\), choose \(u\in A\) and ordered vertices \(v_1,\ldots,v_b\in B\), and set \(G_t=K_{a,b}\setminus\{uv_1,\ldots,uv_t\}\), \(0\le t\le b\). Let \(X_t=\mathsf{Cliq}_k(G_t)\) be the simplicial complex of vertex sets whose induced subgraphs have independence number smaller than \(k\). Set
\[
d=2k-3,\quad F=\binom{a-2}{k-1}\binom{b-1}{k-1},\quad M=\binom{a-2}{k-2}.
\]
Then the complete nonequivariant integral homotopy classification is
\[
|X_t|\simeq\bigvee^{F+M(\binom{b-1}{k-1}-\binom{t}{k-1})}S^d\quad (0\le t<b),
\]
while at the final deletion,
\[
|X_b|\simeq\bigvee^F S^d\vee\bigvee^{M\binom{b-1}{k-2}}S^{d-1}.
\]
All reduced integral homology groups are free. Nothing changes up to and including the first \(k-2\) deletions; the first drop in top homology occurs at deletion \(t=k-1\), whereas the lower-degree summands appear only at \(t=b\). Each inclusion \(X_t\hookrightarrow X_{t-1}\), \(1\le t<b\), induces a split injection on \(\widetilde H_d(-;\mathbb Z)\) with free cokernel of rank \(M\binom{t-1}{k-2}\). The last inclusion induces an isomorphism in degree \(d\), while the newly born degree-\(d-1\) classes have zero image in \(X_{b-1}\).

For \(a=b=5\) and \(k=4\), the correct successive \(\widetilde H_5\)-ranks, for \(t=0,1,2,3,4,5\), are **\(16,16,16,13,4,4\)**; at \(t=5\), \(\widetilde H_4\) also has rank \(18\). These values follow directly from the displayed formula and agree with direct finite-field chain calculations. This corrects a numerical example in the earlier text; the general theorem and its proof are unchanged in substance.

## Assumptions and scope
The graph is finite, simple, and bipartite, and all removed edges share the chosen hub. The hypotheses \(k\ge4\) and \(a,b\ge k+1\) are essential to the present statement. Binomial coefficients with invalid lower indices are zero. Empty sphere wedges mean contractible spaces. Homotopy equivalences are nonequivariant, while the homology maps are induced by the actual nested inclusions \(X_b\subseteq X_{b-1}\subseteq\cdots\subseteq X_0\).

## Proof
**1. Faces, deletion, and link.** Write \(A'=A\setminus\{u\}\), \(B_0=\{v_1,\ldots,v_t\}\). Any independent set of \(G_t\) is wholly in \(A\), wholly in \(B\), or of the form \(\{u\}\cup T\) with \(T\subseteq B_0\). Consequently, \(S\) belongs to \(X_t\) if and only if \(|S\cap A|\le k-1\), \(|S\cap B|\le k-1\), and, when \(u\in S\), \(|S\cap B_0|\le k-2\). Let \(U_{r,E}\) be the complex of subsets of \(E\) of size at most \(r\). Then
\[
D=X_t\setminus u=U_{k-1,A'}*U_{k-1,B},\qquad L_t=\operatorname{lk}_{X_t}(u)=U_{k-2,A'}*Q_t,
\]
where \(Q_t=\{T\subseteq B:|T|\le k-1,\ |T\cap B_0|\le k-2\}\). The space \(X_t\) is obtained from \(D\) by attaching the cone on \(L_t\) along the inclusion \(L_t\hookrightarrow D\).

**2. Homotopy of the pieces.** For \(1\le r<|E|\), the independence complex \(U_{r,E}\) is a wedge of \(\binom{|E|-1}{r}\) spheres of dimension \(r-1\). Hence \(D\simeq\bigvee^F S^{2k-3}\). For \(t<b\), \(Q_t\) is the rank-\((k-1)\) truncation of the partition matroid whose two classes \(B_0\), \(B\setminus B_0\) have quotas \(k-2\), \(k-1\), respectively. Because \(B\setminus B_0\ne\varnothing\), \(Q_t\) is pure of rank \(k-1\). Matroid independence complexes are shellable and have the homotopy type of a wedge of top-dimensional spheres. Relative to \(U_{k-1,B}\), precisely \(\binom t{k-1}\) maximal faces disappear and no smaller faces disappear, so Euler characteristic determines
\[
Q_t\simeq\bigvee^{\binom{b-1}{k-1}-\binom t{k-1}}S^{k-2}\qquad(t<b).
\]
At \(t=b\), \(Q_b=U_{k-2,B}\simeq\bigvee^{\binom{b-1}{k-2}}S^{k-3}\). Taking joins, \(L_t\) is a wedge of \(M(\binom{b-1}{k-1}-\binom t{k-1})\) spheres of dimension \(2k-4\) when \(t<b\), and a wedge of \(M\binom{b-1}{k-2}\) spheres of dimension \(2k-5\) when \(t=b\).

**3. Null attachment and the wedge formulas.** The *simplicial* dimension of every \(L_t\) is at most \(2k-4\), whereas \(D\simeq\bigvee^F S^{2k-3}\) is \((2k-4)\)-connected. Cellular approximation therefore makes every inclusion map \(L_t\to D\) nullhomotopic. The homotopy cofiber of a null map is \(D\vee\Sigma L_t\). This yields both wedge formulas with integral, torsion-free reduced homology; it does not rely on finite-field homology computations.

**4. Integral persistence.** Since the maximal simplicial dimension of \(X_t\) is \(d=2k-3\), its top homology is the subgroup \(\ker(\partial_d)\) of its free integral top-chain group. For \(X_t\subseteq X_{t-1}\), one has
\[
H_d(X_t;\mathbb Z)=H_d(X_{t-1};\mathbb Z)\cap C_d(X_t;\mathbb Z).
\]
Thus \(H_d(X_{t-1};\mathbb Z)/H_d(X_t;\mathbb Z)\) embeds into the free coordinate quotient \(C_d(X_{t-1};\mathbb Z)/C_d(X_t;\mathbb Z)\). Its finite-rank quotient is torsion-free, so the inclusion splits over \(\mathbb Z\). For \(1\le t<b\), subtracting the ranks gives \(M[\binom t{k-1}-\binom{t-1}{k-1}]=M\binom{t-1}{k-2}\). At \(t=b\), the top ranks are both \(F\), hence the primitive inclusion is an isomorphism. The preceding stage has zero degree-\((d-1)\) reduced homology, so the lower-degree classes newly appearing at \(t=b\) map to zero. This proves the full statement.

## Verification and limits of computation
The accompanying `verify.py` independently tests faces from the graph's actual edges, constructs signed simplicial boundaries, and computes homology over \(\mathbb F_2\) and \(\mathbb F_3\) on the listed finite instances. In particular, direct chain reduction for \(a=b=5,k=4\) returns \(16,16,16,13,4,4\) in degree five and \(18\) in degree four at the final stage. These finite checks are corroborative, not proofs of the infinite family or of absence of integral torsion, which follow from the matroid and cofiber argument. The classification makes no claim for general patterns of missing edges, small shores, arbitrary automorphism representations, or shellability of \(X_t\).

## Relationship to prior literature
The foundational graph-complex work of Kim and Lew (2019/2022) primarily develops collapsibility/Leray bounds, not this integral homotopy filtration. Filakovský's 2026 treatment proves robust-clique homotopy theorems for square-sequence and grid-like graphs, with general thresholds for edge-glued square sequences; the dense star-deficient bicliques considered here are outside that graph class. An earlier published result for the three-robust complexes of all connected bipartite graphs covers the special case \(k=3\), which is therefore excluded from the claimed new range. Classical matroid shellability and uniform-matroid skeleton homotopy are ingredients, not claims of novelty. Priority against unindexed or inaccessible equivalent classifications remains a residual risk.

## References
1. M. Filakovský, *The Topology of k-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365 (2026), https://arxiv.org/html/2602.11365.
2. M. Kim and A. Lew, *Complexes of graphs with bounded independence number*, arXiv:1912.12605; Israel J. Math. 249 (2022), 83–120, https://arxiv.org/abs/1912.12605.
3. J. Choe and J. Jung, *A Fröberg type theorem for higher secant complexes*, arXiv:2502.20987 (2025), https://arxiv.org/abs/2502.20987.
4. A. Björner, *Shellable and Cohen–Macaulay simplicial complexes*, Trans. Amer. Math. Soc. 260 (1980), 159–183.
